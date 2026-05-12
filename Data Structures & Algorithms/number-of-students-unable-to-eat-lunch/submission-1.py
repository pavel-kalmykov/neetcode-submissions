class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_count = Counter(students)
        for sandwich in sandwiches:
            if students_count[sandwich]:
                students_count[sandwich] -= 1
            else:
                break
        return sum(students_count.values())