class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map_course = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            map_course[crs].append(pre)
        
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if map_course[crs] == []:
                return True

            visiting.add(crs)
            for p in map_course[crs]:
                if not dfs(p):
                    return False
            visiting.remove(crs)
            map_course[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True