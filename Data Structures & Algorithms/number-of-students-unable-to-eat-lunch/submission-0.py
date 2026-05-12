class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        rotations = 0
        while students and rotations < len(students):
            if sandwiches[0] == students[0]:
                sandwiches.popleft()
                students.popleft()
                rotations = 0
            else:
                students.append(students.popleft())
                rotations += 1
        return rotations