class Interval:
    def __init__(self, start, end):
        if not (isinstance(start, (int, float)) and isinstance(end, (int, float))):
            raise ValueError("Start and end must be numeric values.")
        if start > end:
            raise ValueError("Start must be less than or equal to end.")
        self.start = start
        self.end = end

    def __str__(self):
        return f"[{self.start}, {self.end}]"

    def is_overlapping(self, other_interval):
        return not (self.end < other_interval.start or self.start > other_interval.end)

    @staticmethod
    def intersection_static(interval1, interval2):
        if interval1.is_overlapping(interval2):
            return Interval(max(interval1.start, interval2.start), min(interval1.end, interval2.end))
        return None

    def __and__(self, other_interval):
        return Interval.intersection_static(self, other_interval)

    @staticmethod
    def union_static(interval1, interval2):
        if interval1.is_overlapping(interval2):
            return Interval(min(interval1.start, interval2.start), max(interval1.end, interval2.end))
        return None

    def __or__(self, other_interval):
        return Interval.union_static(self, other_interval)

    def __sub__(self, other_interval):
        if not self.is_overlapping(other_interval):
            return self
        if self.start < other_interval.start:
            return Interval(self.start, min(self.end, other_interval.start - 1))
        if self.end > other_interval.end:
            return Interval(max(self.start, other_interval.end + 1), self.end)
        return None  # No remaining interval


if __name__ == "__main__":
    interval1 = Interval(1, 5)
    interval2 = Interval(3, 8)

    print("Interval 1:", interval1)
    print("Interval 2:", interval2)
    print("Do intervals overlap?", interval1.is_overlapping(interval2))
    print("Intersection Result:", interval1 & interval2)
    print("Union Result:", interval1 | interval2)
    print("Difference Result 1:", interval1 - interval2)
    print("Difference Result 2:", interval2 - interval1)
