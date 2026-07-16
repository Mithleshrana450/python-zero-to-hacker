class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = []

    def add_marks(self, mark):
        self.marks.append(mark)

    def get_average(self):
        return sum(self.marks) / len(self.marks)

    def get_grade(self):
        avg = self.get_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def __str__(self):
        return f"{self.name} ({self.roll_no}) - Avg: {self.get_average():.1f}, Grade: {self.get_grade()}"


# Example
s = Student("Mithlesh", 25)
s.add_marks(85)
s.add_marks(90)
s.add_marks(80)

print(s)