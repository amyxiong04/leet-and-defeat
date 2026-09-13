class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create graph
        course_graph = {course: [] for course in range(numCourses)}

        # populate it
        for course, prereq in prerequisites:
            course_graph[course].append(prereq)

        visiting = set()

        # dfs function to check if each course is safe
        def dfs(course):
            # cycle
            if course in visiting:
                return False

            if course_graph[course] == []:
                return True

            visiting.add(course)

            for prereq in course_graph[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)
            
            return True

        for course in course_graph:
            if not dfs(course):
                return False

        return True