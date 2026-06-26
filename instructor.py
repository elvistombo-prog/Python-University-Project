class Instructor:
    """
    Represents an instructor in the university system.
    """

    def __init__(self, instructor_id, name, department):
        self.instructor_id = instructor_id
        self.name = name
        self.department = department
        self.courses = []

    # Method 1
    def assign_course(self, course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)

    # Method 2
    def remove_course(self, course_name):
        if course_name in self.courses:
            self.courses.remove(course_name)

    # Method 3
    def view_courses(self):
        return self.courses

    # Method 4
    def get_details(self):
        return f"{self.instructor_id} - {self.name} - {self.department}"
