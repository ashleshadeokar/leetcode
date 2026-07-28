from collections import deque
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        lx, ly = location
        angles = []
        same = 0

        # populate angles arr with angles relative to our position
        for x, y in points:
            if lx - x == 0 and ly - y == 0:
                same += 1
                continue
            # atan2 gives result in radians - convert to deg
            angle_rad = math.atan2(y - ly, x - lx)
            angle_deg = math.degrees(angle_rad)
            # make sure angle is positive
            if angle_deg < 0:
                angle_deg += 360
            angles.append(angle_deg)

        # no angles: all the points are at the same location
        if not angles:
            return same

        angles.sort()
        extended = angles + [a + 360 for a in angles]

        window = deque()
        maxpoints = float('-inf')

        # sliding window approach
        for a in extended:
            window.append(a)
            # if current window is wider than the angle, adjust
            while (window[-1] - window[0]) > angle:
                window.popleft()
            maxpoints = max(maxpoints, len(window))

        if maxpoints > len(angles):
            maxpoints = len(angles)

        return maxpoints + same

                