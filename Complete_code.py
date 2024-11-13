class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self):
        return self.calculate_average() >= 40


class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self):
        name = input("Enter student name or type exit : ")
        if name.lower() == 'exit':
            return False  

        scores = list(map(int, input("Enter scores for subjects (maths, science, english): ").split()))
        student = Student(name, scores)
        self.students[name] = student
        print(f"Student '{name}' added successfully")
        return True  

    def class_average(self):
        if not self.students:
            return 0
        total_score = sum(student.calculate_average() for student in self.students.values())
        return total_score / len(self.students)

    def display_student_performance(self):
        for name, student in self.students.items():
            print(f"Student Name: {name}")
            print(f"Scores: {student.scores}")
            print(f"Average Score: {student.calculate_average()}")
            print(f"Passing Status: {'Passing' if student.is_passing() else 'Failing'}")


# PerformanceTracker and add students until "stop" is entered
performance_tracker = PerformanceTracker()
while performance_tracker.add_student():
    pass  

# Display performance of each student and class average
performance_tracker.display_student_performance()
print("Class Average:", performance_tracker.class_average())
