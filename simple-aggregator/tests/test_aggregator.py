import pandas as pd
from aggregator import aggregate
import pytest


@pytest.fixture(scope="module")
def events_sample():
    data = [
      ["customer_id_1", "event_1", "txn1", "2022-03-01 03:01:00.154+00"],
      ["customer_id_1", "event_2", "txn2", "2022-03-01 04:29:00.154+00"],
      ["customer_id_1", "event_3", "txn3", "2022-03-01 04:15:00.154+00"],
      ["customer_id_1", "event_4", "txn4", "2022-03-01 05:08:00.154+00"],
    ]
    d_frame = pd.DataFrame(data, columns=['cust_id', 'event_type', 'txn_id', 'timestamp'])
    return d_frame


@pytest.fixture(scope="module")
def events_detailed():
    data = [
        ["b4f9279a0196e40632e947dd1a88e857", "event_1", "txn1", "2002-03-01 03:01:00.154+00"],
        ["b4f9279a0196e40632e947dd1a88e857", "event_2", "txn2", "2012-03-01 04:29:00.154+00"],
        ["b4f9279a0196e40632e947dd1a88e857", "event_3", "txn3", "2020-03-01 04:15:00.154+00"],
        ["b4f9279a0196e40632e947dd1a88e857", "event_4", "txn4", "2021-03-01 05:08:00.154+00"],
        ["b4f9279a0196e40632e947dd1a88e857", "event_1", "txn1", "2022-03-01 03:01:00.154+00"],
        ["30330c9c4e7173ba9474c46ee5191570", "event_2", "txn2", "2022-03-01 04:29:00.154+00"],
        ["b4f9279a0196e40632e947dd1a88e857", "event_3", "txn3", "2022-03-01 04:15:00.154+00"],
        ["b4f9279a0196e40632e947dd1a88e857", "event_4", "txn4", "2022-03-02 05:08:00.154+00"],
        ["b4f9279a0196e40632e947dd1a88e857", "event_1", "txn1", "2022-03-02 13:01:00.154+00"],
        ["b4f9279a0196e40632e947dd1a88e857", "event_2", "txn2", "2022-03-05 04:29:00.154+00"],
        ["30330c9c4e7173ba9474c46ee5191570", "event_3", "txn3", "2022-03-01 04:15:00.154+00"],
        ["30330c9c4e7173ba9474c46ee5191570", "event_4", "txn4", "2022-03-01 05:08:00.154+00"],
        ["30330c9c4e7173ba9474c46ee5191570", "event_1", "txn1", "2022-03-01 03:01:00.154+00"],
        ["1abb42414607955dbf6088b99f837d8f", "event_2", "txn2", "2021-03-03 04:29:00.154+00"],
        ["b4f9279a0196e40632e947dd1a88e857", "event_3", "txn3", "2022-03-01 14:15:00.154+00"],
        ["1abb42414607955dbf6088b99f837d8f", "event_4", "txn4", "2022-02-01 05:08:00.154+00"],
        ["1abb42414607955dbf6088b99f837d8f", "event_4", "txn4", "2022-02-01 05:18:00.154+00"],
        ["1abb42414607955dbf6088b99f837d8f", "event_4", "txn4", "2022-02-01 15:08:00.154+00"],
        ["1abb42414607955dbf6088b99f837d8f", "event_4", "txn4", "2022-02-02 07:08:00.154+00"],
        ["1abb42414607955dbf6088b99f837d8f", "event_4", "txn4", "2022-02-02 07:18:00.154+00"],
        ["1abb42414607955dbf6088b99f837d8f", "event_4", "txn4", "2022-02-02 07:28:00.154+00"],
    ]
    d_frame = pd.DataFrame(data, columns=['cust_id', 'event_type', 'txn_id', 'timestamp'])
    return d_frame


class TestAggregateBasic:
    def test_sample_data(self, events_sample):
        cust = "customer_id_1"
        from_date = "2022-03-01 03:00:00Z"
        to_date = "2022-03-03 05:00:00Z"
        res = aggregate(events_sample, cust, from_date, to_date)
        assert res == {'2022-3-1:T3:00:00': 1, '2022-3-1:T4:00:00': 2, '2022-3-1:T5:00:00': 1}

    def test_invalid_date_range(self, events_sample):
        cust = "customer_id_1"
        from_date = "2021-03-04 05:00:00.154+00"
        to_date = "2021-03-03 03:00:00.154+00"
        res = aggregate(events_sample, cust, from_date, to_date)
        assert res == {}

    def test_from_time_gt_end_time(self, events_sample):
        cust = "customer_id_1"
        from_date = "2021-03-03 05:00:00Z"
        to_date = "2021-03-03 03:00:00Z"
        res = aggregate(events_sample, cust, from_date, to_date)
        assert res == {}

    def test_invalid_date_format(self, events_sample):
        cust = "customer_id_1"
        from_date = "2021-03-04 05:00:00Z"
        to_date = "2021-03-03 33:00:00Z"
        res = aggregate(events_sample, cust, from_date, to_date)
        assert res == {'error': 'from, to - invalid date format'}

    def test_unknown_customer(self, events_sample):
        cust = "unknown_customer"
        from_date = "2021-03-03 01:00:00Z"
        to_date = "2021-03-03 13:00:00Z"
        res = aggregate(events_sample, cust, from_date, to_date)
        assert res == {}


class TestAggregateData:
    def test_days_across_months(self, events_detailed):
        cust = "1abb42414607955dbf6088b99f837d8f"
        from_date = "2022-02-01T00:00:00Z"
        to_date = "2022-03-03T17:00:00Z"
        res = aggregate(events_detailed, cust, from_date, to_date)
        assert res == {'2022-2-1:T5:00:00': 2, '2022-2-1:T15:00:00': 1, '2022-2-2:T7:00:00': 3}

    def test_same_day(self, events_detailed):
        cust = "b4f9279a0196e40632e947dd1a88e857"
        from_date = "2022-03-01T00:00:00Z"
        to_date = "2022-03-01T23:00:00Z"
        res = aggregate(events_detailed, cust, from_date, to_date)
        assert res == {'2022-3-1:T3:00:00': 1, '2022-3-1:T4:00:00': 1, '2022-3-1:T14:00:00': 1}

    def test_days_within_months(self, events_detailed):
        cust = "1abb42414607955dbf6088b99f837d8f"
        from_date = "2022-02-01T00:00:00Z"
        to_date = "2022-02-02T23:00:00Z"
        res = aggregate(events_detailed, cust, from_date, to_date)
        assert res == {'2022-2-1:T15:00:00': 1, '2022-2-1:T5:00:00': 2, '2022-2-2:T7:00:00': 3}

    def test_days_across_years_full(self, events_detailed):
        cust = "b4f9279a0196e40632e947dd1a88e857"
        from_date = "2002-01-01T00:00:00Z"
        to_date = "2022-12-31T23:00:00Z"
        res = aggregate(events_detailed, cust, from_date, to_date)
        assert res == {'2002-3-1:T3:00:00': 1, '2012-3-1:T4:00:00': 1, '2020-3-1:T4:00:00': 1, '2021-3-1:T5:00:00': 1,
                       '2022-3-1:T3:00:00': 1, '2022-3-1:T4:00:00': 1, '2022-3-1:T14:00:00': 1, '2022-3-2:T5:00:00': 1,
                       '2022-3-2:T13:00:00': 1, '2022-3-5:T4:00:00': 1}

    def test_days_across_years_partial(self, events_detailed):
        cust = "b4f9279a0196e40632e947dd1a88e857"
        from_date = "2018-01-01T00:00:00Z"
        to_date = "2021-12-31T23:00:00Z"
        res = aggregate(events_detailed, cust, from_date, to_date)
        assert res == {'2020-3-1:T4:00:00': 1, '2021-3-1:T5:00:00': 1}

