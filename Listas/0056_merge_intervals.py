class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []

        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        inter = intervals[0]
        for i in range(1, len(intervals)):
            new = intervals[i]

            if inter[1]>=new[0]:
                if inter[1]<new[1]:
                    inter[1] = new[1]
            else:
                res.append(inter)
                inter = new
        res.append(inter)
        return res