class Course:
    """
    Represents a course in the university system.
    """

    def __init__(self, course_id, title):
        self.course_id = course_id
        self.title = title
        self.students = []

    # Method 1
    def add_student(self, student_name):
        if student_name not in self.students:
            self.students.append(student_name)

    # Method 2
    def remove_student(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)

    # Method 3
    def list_students(self):
        return self.students

    # Method 4
    def get_course_info(self):
        return f"{self.course_id} - {self.title}"
