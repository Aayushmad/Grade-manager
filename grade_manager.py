class GradeManager:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        return self.grades

    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def is_pass(self):
        return self.get_average() >= 40