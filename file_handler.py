import csv

FILE_PATH = "data/students.csv"


def save_students(students):
  with open(FILE_PATH, "w", newline="") as file:
            writer = csv.writer(file)

  for s in students:
      writer.writerow([s.student_id, s.name, s.email])


def load_students():
    try:
        students = []

        with open(FILE_PATH, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                students.append(row)

        return students

    except FileNotFoundError:
        print("No saved data found.")
        return []


