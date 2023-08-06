import argparse
from dateutil import parser

import pandas as pd


def aggregate(df: pd.DataFrame, cust: str, from_date: str, to_date: str) -> dict:

    try:
        from_dt = parser.isoparse(from_date)
        to_dt = parser.isoparse(to_date)
    except ValueError:
        return {"error": "from, to - invalid date format"}

    df['timestamp'] = pd.to_datetime(df['timestamp'], format='ISO8601')
    df['year'] = df['timestamp'].dt.year
    df['month'] = df['timestamp'].dt.month
    df['day'] = df['timestamp'].dt.day
    df['hour'] = df['timestamp'].dt.hour
    df['minute'] = df['timestamp'].dt.minute
    df['second'] = df['timestamp'].dt.second

    diff = to_dt - from_dt
    if diff.days > 0:
        b1 = df[(df['cust_id'] == cust) &
                (df['year'] >= from_dt.year) & (df['year'] <= to_dt.year) &
                (df['month'] >= from_dt.month) & (df['month'] <= to_dt.month) &
                (df['day'] > from_dt.day) & (df['day'] < to_dt.day)]
        b2 = df[(df['cust_id'] == cust) &
                (df['day'] == from_dt.day) & (df['month'] >= from_dt.month) & (df['year'] >= from_dt.year) &
                (df['year'] <= to_dt.year) &
                (df['hour'] > from_dt.hour) & (df['hour'] <= 23)]
        b3 = df[(df['cust_id'] == cust) &
                (df['day'] == from_dt.day) & (df['month'] >= from_dt.month) & (df['year'] >= from_dt.year) &
                (df['year'] <= to_dt.year) &
                (df['hour'] == from_dt.hour) & (df['minute'] >= from_dt.minute) & (df['second'] >= from_dt.second)]
        b4 = df[(df['cust_id'] == cust) &
                (df['day'] == to_dt.day) & (df['month'] <= to_dt.month) & (df['year'] >= from_dt.year) &
                (df['year'] <= to_dt.year) &
                (df['hour'] >= 0) & (df['hour'] < to_dt.hour)]
        b5 = df[(df['cust_id'] == cust) &
                (df['day'] == to_dt.day) & (df['month'] <= to_dt.month) & (df['year'] >= from_dt.year) &
                (df['year'] <= to_dt.year) &
                (df['hour'] == to_dt.hour) & (df['minute'] <= to_dt.minute) & (df['second'] <= to_dt.second)]

        buckets = pd.concat([b1, b2, b3, b4, b5])
    else:
        b1 = df[(df['cust_id'] == cust) &
                    (df['day'] == from_dt.day) & (df['month'] == from_dt.month) & (df['year'] == from_dt.year) &
                    (df['hour'] > from_dt.hour) & (df['hour'] < to_dt.hour)]
        b2 = df[(df['cust_id'] == cust) &
                    (df['day'] == from_dt.day) & (df['month'] == from_dt.month) & (df['year'] == from_dt.year) &
                    (df['hour'] == from_dt.hour) & (df['minute'] >= from_dt.minute) & (df['second'] >= from_dt.second)]
        b3 = df[(df['cust_id'] == cust) &
                    (df['day'] == to_dt.day) & (df['month'] == from_dt.month) & (df['year'] == from_dt.year) &
                    (df['hour'] == to_dt.hour) & (df['minute'] <= to_dt.minute) & (df['second'] <= to_dt.second)]

        buckets = pd.concat([b1, b2, b3])

    grouped = buckets.groupby(['year', 'month', 'day','hour'])
    r = grouped.count()['event_type'].to_dict()

    out = {}
    for k, v in r.items():
        dt_str = f"{k[0]}-{k[1]}-{k[2]}:T{k[3]}:00:00"
        out[dt_str] = v
    return out


if __name__ == "__main__":
    c_parser = argparse.ArgumentParser(description="Aggregates events into hourly buckets.")
    c_parser.add_argument("-c", '--cust_id', type=str, help="customer id to query for events")
    c_parser.add_argument("-f", "--file_path", type=str, help="path to file with events data")
    c_parser.add_argument("-fd", "--from_date", type=str, help="start date for query (YYYY-MM-DD:THH:MM:SS:00Z)")
    c_parser.add_argument("-td", "--to_date", type=str, help="start date for query (YYYY-MM-DD:THH:MM:SS:00Z)")
    args = c_parser.parse_args()

    d_frame = pd.read_csv(args.file_path, header=None)
    d_frame.columns = ['cust_id', 'event_type', 'txn_id', 'timestamp']
    res = aggregate(d_frame, args.cust_id, args.from_date, args.to_date)
    print(res)

