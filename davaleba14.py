import csv
from collections import defaultdict


FIELDNAMES = ["id", "name", "age", "grade", "subject_name", "mark"]


students = [
    {'id': 8, 'name': 'Nika', 'age': 19, 'grade': 'B', 'subject_name': 'Physic', 'mark': 87},
    {'id': 19, 'name': 'Nuca', 'age': 18, 'grade': 'B', 'subject_name': 'Mathematic', 'mark': 84},
    {'id': 11, 'name': 'Archil', 'age': 21, 'grade': 'C', 'subject_name': 'Mathematic', 'mark': 74},
    {'id': 25, 'name': 'Nino', 'age': 20, 'grade': 'A', 'subject_name': 'Informatic', 'mark': 95},
    {'id': 22, 'name': 'Giga', 'age': 20, 'grade': 'A', 'subject_name': 'Biology', 'mark': 81},
    {'id': 31, 'name': 'Lana', 'age': 22, 'grade': 'B', 'subject_name': 'Geography', 'mark': 88},
    {'id': 3, 'name': 'Nino', 'age': 23, 'grade': 'B', 'subject_name': 'Informatic', 'mark': 85},
]

new_student = {
    'id': 5,
    'name': 'Demetre',
    'age': 18,
    'grade': 'A',
    'subject_name': 'Informatic',
    'mark': 94
}


#CSV ფაილში სტუდენტების ჩაწერა და id-ის მიხედვით დალაგება
def write_students(filename, students_list):
    sorted_students = sorted(students_list, key=lambda student: student["id"])

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(sorted_students)


# CSV ფაილიდან სტუდენტების წაკითხვა
def read_students(filename, student_id=None):
    students_list = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            student = {
                "id": int(row["id"]),
                "name": row["name"],
                "age": int(row["age"]),
                "grade": row["grade"],
                "subject_name": row["subject_name"],
                "mark": int(row["mark"])
            }
            students_list.append(student)

    # თუ id არ გადმომცა, აბრუნებს ყველა სტუდენტს
    if student_id is None:
        return students_list

    # თუ id გადმომცა, აბრუნებს მხოლოდ კონკრეტული სტუდენტის მონაცემებს
    return [student for student in students_list if student["id"] == student_id]


# 1.ახალი სტუდენტის დამატება და id-ის მიხედვით დალაგება
def add_student(filename, new_student_data):
    students_list = read_students(filename)

    for student in students_list:
        if student["id"] == new_student_data["id"]:
            print("ასეთი id-ით სტუდენტი უკვე არსებობს.")
            return

    students_list.append(new_student_data)
    write_students(filename, students_list)

    print("სტუდენტი წარმატებით დაემატა.")


# 3.საშუალო ქულის დათვლა საგნების მიხედვით
def calculate_average_marks(filename):
    students_list = read_students(filename)

    subjects = defaultdict(list)

    for student in students_list:
        subjects[student["subject_name"]].append(student["mark"])

    averages = {}

    for subject, marks in subjects.items():
        averages[subject] = round(sum(marks) / len(marks), 2)

    return averages


# 4.სტუდენტის ქულის განახლება id-ისა და საგნის მიხედვით
def update_student_mark(filename, student_id, subject_name, new_mark):
    students_list = read_students(filename)
    updated = False

    for student in students_list:
        if student["id"] == student_id and student["subject_name"] == subject_name:
            student["mark"] = new_mark
            updated = True
            break

    if updated:
        write_students(filename, students_list)
        print("ქულა წარმატებით განახლდა.")
    else:
        print("სტუდენტი ან საგანი ვერ მოიძებნა.")


#პროგრამის გაშვება
filename = "students.csv"

#საწყისი მონაცემების CSV ფაილში ჩაწერა
write_students(filename, students)

# 5.ახალი სტუდენტის დამატება
add_student(filename, new_student)

#ყველა სტუდენტის წაკითხვა
print("\nყველა სტუდენტი:")
for student in read_students(filename):
    print(student)

#კონკრეტული სტუდენტის წაკითხვა
print("\nსტუდენტი id = 19:")
print(read_students(filename, 19))

#საშუალო ქულები საგნების მიხედვით
print("\nსაგნების საშუალო ქულები:")
print(calculate_average_marks(filename))

#Nuca-ს მათემატიკის ქულის განახლება
update_student_mark(filename, 19, "Mathematic", 90)

print("\nგანახლებული სტუდენტი id = 19:")
print(read_students(filename, 19))