from datetime import datetime
from typing import List


class Person:
    """Base class for Student and Professor"""

    def __init__(self, name: str, id_number: str):
        self.name = name
        self.id_number = id_number

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name} (ID: {self.id_number})"

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.id_number == other.id_number
        return False


class Student(Person):
    """Represents a student, storing their enrollments and grades."""

    def __init__(self, name: str, id_number: str):
        super().__init__(name, id_number)
        self.enrollments: list[Enrollment] = []

    def enroll(self, course: "Course", semester: str):
        enrollment = Enrollment(self, course, semester)
        self.enrollments.append(enrollment)
        course.add_student(self)
        return enrollment

    def calculate_gpa(self, start_date: datetime, end_date: datetime) -> float:
        """Calculates GPA for a specific period"""
        total_points, total_credits = 0, 0
        for enrollment in self.enrollments:
            if enrollment.semester_date >= start_date and enrollment.semester_date <= end_date:
                if enrollment.grade is not None:
                    total_points += enrollment.grade * enrollment.course.credits
                    total_credits += enrollment.course.credits
        return round(total_points / total_credits, 2) if total_credits else 0.0

    def __str__(self):
        return super().__str__() + f" | Enrolled in {len(self.enrollments)} courses"


class Professor(Person):
    """Represents a professor, storing assigned courses."""

    def __init__(self, name: str, id_number: str):
        super().__init__(name, id_number)
        self.courses: list[Course] = []

    def assign_course(self, course: "Course"):
        self.courses.append(course)
        course.assign_professor(self)

    def __str__(self):
        return super().__str__() + f" | Teaching {len(self.courses)} courses"


class Course:
    """Represents a course with a name, code, credits, and professor."""

    def __init__(self, name: str, course_code: str, credits: int):
        self.name = name
        self.course_code = course_code
        self.credits = credits
        self.professor: Professor = None
        self.students: List[Student] = []

    def assign_professor(self, professor: Professor):
        self.professor = professor

    def add_student(self, student: Student):
        self.students.append(student)

    def __str__(self):
        return f"Course: {self.name} ({self.course_code}), Credits: {self.credits}, Professor: {self.professor.name if self.professor else 'TBA'}"


class Enrollment:
    """Represents the relationship between a student and a course."""

    def __init__(self, student: Student, course: Course, semester: str):
        self.student = student
        self.course = course
        self.semester = semester
        self.semester_date = datetime.strptime(semester, "%Y-%m")
        self.grade = None  # Grade will be assigned later

    def assign_grade(self, grade: float):
        self.grade = grade

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.name} ({self.semester}) - Grade: {self.grade if self.grade is not None else 'N/A'}"


class Administration:
    """Handles GPA calculation and report generation."""

    @staticmethod
    def generate_report(student: Student, start_date: datetime, end_date: datetime):
        gpa = student.calculate_gpa(start_date, end_date)
        print(f"Student Report for {student.name} (ID: {student.id_number})")
        print(f"GPA from {start_date.strftime('%Y-%m')} to {end_date.strftime('%Y-%m')}: {gpa}")
        print("Enrolled Courses:")
        for enrollment in student.enrollments:
            if start_date <= enrollment.semester_date <= end_date:
                print(
                    f"  - {enrollment.course.name} ({enrollment.semester}): Grade {enrollment.grade if enrollment.grade is not None else 'N/A'}"
                )


# Example Usage
if __name__ == "__main__":
    student = Student("Alice Johnson", "S1001")
    professor = Professor("Dr. Smith", "P2001")
    course1 = Course("Mathematics", "MATH101", 3)
    course2 = Course("Physics", "PHYS101", 4)

    professor.assign_course(course1)
    professor.assign_course(course2)

    enrollment1 = student.enroll(course1, "2025-01")
    enrollment2 = student.enroll(course2, "2025-01")

    enrollment1.assign_grade(3.7)  # Assign grades
    enrollment2.assign_grade(3.9)

    start_date = datetime.strptime("2025-01", "%Y-%m")
    end_date = datetime.strptime("2025-06", "%Y-%m")

    Administration.generate_report(student, start_date, end_date)
