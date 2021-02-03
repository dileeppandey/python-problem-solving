"""
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive
intervals

eg

[[1,4], [2,5], [7,9]]
[[1,5], [7,9]]

[[1,10], [2,3], [5,9]]



start = i[0][0]
end = i[0][1]

for s, e in range(1, length):
    if s <= end:
        end = max(e, end)
    else:
        result.append([start, end])
        start = s
        end = e

result.append([start, end])

"""


class Interval:

    def __init__(self, start, end):
        self.start = start
        self.end = end


def merge_interval(intervals):
    """Return a list of mutually exclusive intervals

    Params:
        intervals: List[(start, end), ...]

    Return:
        List(Interval)
    """
    length = len(intervals)

    if not length:
        return []

    result = []

    # Sort the intervals based on the start time
    intervals.sort(key=lambda x: x.start)

    start, end = intervals[0].start, intervals[0].end

    for i in range(1, length):
        s = intervals[i].start
        e = intervals[i].end
        if s <= end:
            end = max(end, e)
        else:
            result.append(Interval(start, end))
            start = s
            end = e

    result.append(Interval(start, end))
    return result
