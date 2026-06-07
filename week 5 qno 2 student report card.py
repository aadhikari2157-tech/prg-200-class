class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()

        if avg >= 80:
            return "A"
        elif avg >= 65:
            return "B"
        elif avg >= 50:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"
        
    def display(self):
        avg = self.average()
        status = "Pass" if avg >= 40 else "Fail"

        print(f"Name: {self.name}")
        print(f"Average: {avg:.2f}")
        print(f"Grade: {self.grade()}")
        print(f"Result: {status}")
        print("-" * 30)