"""
Student Manager — DevOps Lab 5
Module: Main Application
"""
from student import Student


def add_student(students: list, student_id: str, name: str, age: int, grade: str) -> Student:
    """Thêm một sinh viên mới vào danh sách."""
    for s in students:
        if s.student_id == student_id:
            raise ValueError(f"Student ID '{student_id}' already exists!")
    new_student = Student(student_id, name, age, grade)
    students.append(new_student)
    return new_student


def display_students(students: list) -> None:
    """Hiển thị toàn bộ danh sách sinh viên."""
    if not students:
        print("  (Danh sách trống)")
        return
    for student in students:
        print(f"  {student}")
    print(f"\nTotal: {len(students)} students")


def main():
    """Hàm chính của ứng dụng."""
    print("=" * 50)
    print("STUDENT MANAGER — DevOps Lab 5")
    print("=" * 50)

    students = []
    add_student(students, "SV001", "Nguyen Van A", 20, "K20")
    add_student(students, "SV002", "Tran Thi B", 21, "K20")
    add_student(students, "SV003", "Le Van C", 19, "K21")

    display_students(students)


if __name__ == "__main__":
    main()