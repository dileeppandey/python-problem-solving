"""
Given a sorted list of intervals, insert a given interval to it's rightful place, merge overlapping intervals caused by
the insertion of new interval

eg
[[1,2], [3,5], [7,9]], [4, 6]
[[1,2], [3,6], [7,9]]

"""


class Interval:

    def __init__(self, start, end):
        self.start = start
        self.end = end


def insert_interval(intervals, new_interval):
    """Return a mutually exclusive list of intervals after inserting new_interval

    Params:
        intervals: List(Intervals)
        new_interval: Interval

    Return:
        List(Interval)
    """
    length = len(intervals)
    if length < 1:
        return [new_interval]

    i, start, end, merged = 0, new_interval.start, new_interval.end, []

    while i < length and intervals[i].end < start:
        merged.append(intervals[i])
        i += 1

    while i < length and new_interval.start < intervals[i].end:
        new_interval.start = min(new_interval.start, intervals[i].start)
        new_interval.end = max(new_interval.end, intervals[i].end)
        i += 1

    merged.append(new_interval)

    while i < length:
        merged.append(intervals[i])
        i += 1

    return merged
