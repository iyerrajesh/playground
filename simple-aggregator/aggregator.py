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
    diff_years = diff.days // 365
    diff_months = diff.days // 30
    diff_hours = diff.seconds // 3600
    diff_mins = diff.seconds // 60

    if diff.days < 0:
        return {"error": "to date is < from date"}

    ys = df[(df['cust_id'] == cust) &
             (df['year'] > from_dt.year) & (df['year'] < to_dt.year)]

    if diff_years or (diff_years == 0 and from_dt.year < to_dt.year):
        mms1 = df[(df['cust_id'] == cust) &
                (df['year'] == from_dt.year) & (df['month'] > from_dt.month) & (df['month'] <= 12)]
        mms2 = df[(df['cust_id'] == cust) &
                  (df['year'] == to_dt.year) & (df['month'] >= 1) & (df['month'] < to_dt.month)]
        mms = pd.concat([mms1, mms2])
    else:
        mms = df[(df['cust_id'] == cust) &
                (df['year'] == from_dt.year) & (df['month'] > from_dt.month) & (df['month'] < to_dt.month)]

    if diff_months or (diff_months == 0 and from_dt.month < to_dt.month):
        # days d > f_d & d < t_d
        ds1 = df[(df['cust_id'] == cust) &
                 (df['year'] == from_dt.year) & (df['month'] == from_dt.month) & (df['day'] > from_dt.day)]
        ds2 = df[(df['cust_id'] == cust) &
                (df['year'] == to_dt.year) & (df['month'] == to_dt.month) & (df['day'] >= 1) &
                (df['day'] < to_dt.day)]

        ds = pd.concat([ds1, ds2])
    else:
        ds = df[(df['cust_id'] == cust) &
                (df['year'] == from_dt.year) & (df['month'] == from_dt.month) &
                (df['day'] > from_dt.day) & (df['day'] < to_dt.day)]
    #print(ds)
    # hours
    if diff.days or (diff.days == 0 and from_dt.day < to_dt.day):
        # d == f_d & h > f_h & h <= 23 & d == t_d & h >= 0 & h < t_h()
        hs1 = df[(df['cust_id'] == cust) & (df['year'] == from_dt.year) & (df['month'] == from_dt.month) &
                 (df['day'] == from_dt.day) & (df['hour'] > from_dt.hour) & (df['hour'] <= 23)]
        hs2 = df[(df['cust_id'] == cust) & (df['year'] == to_dt.year) & (df['month'] == to_dt.month) &
                 (df['day'] == to_dt.day) & (df['hour'] >= 0) & (df['hour'] < to_dt.hour)]
        hs = pd.concat([hs1, hs2])
    else:
        # d == f_d & h > f_h & h < t_h
        hs = df[(df['cust_id'] == cust) & (df['year'] == from_dt.year) & (df['month'] == from_dt.month) &
                (df['day'] == from_dt.day) &(df['hour'] > from_dt.hour) & (df['hour'] < to_dt.hour)]

    # mins
    if diff_hours or (diff_hours == 0 and from_dt.hour < to_dt.hour):
        # h == f_h & m > f_m & m <= 59 & h == t_h & m >=0 & m < t_m
        ms1 = df[(df['cust_id'] == cust) & (df['year'] == from_dt.year) & (df['month'] == from_dt.month) &
                 (df['day'] == from_dt.day) &
                 (df['hour'] == from_dt.hour) & (df['minute'] > from_dt.minute) & (df['minute'] <= 59)]
        ms2 = df[(df['cust_id'] == cust) & (df['year'] == to_dt.year) & (df['month'] == to_dt.month) &
                 (df['day'] == to_dt.day) &
                 (df['hour'] == to_dt.hour) & (df['minute'] >= 0) & (df['minute'] < to_dt.minute)]
        ms = pd.concat([ms1, ms2])
    else:
        # d == f_d  & h == f_h & m > f_m & m < t_m
        ms1 = df[(df['cust_id'] == cust) & (df['year'] == from_dt.year) & (df['month'] == from_dt.month) &
                (df['day'] == from_dt.day) & (df['hour'] == from_dt.hour) &
                (df['minute'] > from_dt.minute) & (df['minute'] < to_dt.minute) ]
        # ms2 = df[(df['cust_id'] == cust) & (df['year'] == from_dt.year) & (df['month'] == from_dt.month) &
        #         (df['day'] == to_dt.day) & (df['hour'] == to_dt.hour) & (df['minute'] <= to_dt.minute)]
        ms = pd.concat([ms1])
    # secs
    if diff_mins or (diff_mins == 0 and from_dt.minute < to_dt.minute):
        # h == f_h & m == f_m & s >= f_s & s <=59
        # h == t_h m == t_m & s >= 0 & s <= t_s
        ss1 = df[(df['cust_id'] == cust) & (df['year'] == from_dt.year) & (df['month'] == from_dt.month) &
                 (df['day'] == from_dt.day) &
                 (df['hour'] == from_dt.hour) & (df['minute'] == from_dt.minute) &
                 (df['second'] >= from_dt.second) & (df['second'] <= 59)]
        ss2 = df[(df['cust_id'] == cust) & (df['year'] == to_dt.year) & (df['month'] == to_dt.month) &
                 (df['day'] == to_dt.day) &
                 (df['hour'] == to_dt.hour) &(df['minute'] == to_dt.minute) &
                 (df['second'] >= 0) &(df['second'] <= to_dt.second)]
        ss = pd.concat([ss1,ss2])
    else:
        # d == f_d & h == f_h & m == f_m & s >= f_s &\
        # h == t_h & m == t_m & s <= t_s
        ss = df[(df['cust_id'] == cust) & (df['year'] == from_dt.year) & (df['month'] == from_dt.month) &
                 (df['day'] == from_dt.day) & (df['hour'] == from_dt.hour) &
                 (df['minute'] == from_dt.minute) &
                 (df['minute'] == to_dt.minute) &
                 (df['second'] >= from_dt.second) & (df['second'] <= to_dt.second)]
    buckets = pd.concat([ys, mms, ds, hs, ms, ss])
    print(buckets)
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

