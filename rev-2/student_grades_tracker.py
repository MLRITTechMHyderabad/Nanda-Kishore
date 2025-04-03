def calculate_avg_grade(students):
    for k,v in students.items():
        print(f"{k} has an average grade of {sum(v)/len(v)}")

def highest_grade(students):
    best_student = None
    best_avg = 0

    for student, grades in students.items():
        avg_grade = sum(grades) / len(grades)
        if avg_grade > best_avg:
            best_avg = avg_grade
            best_student = student

    print(f"Student with the highest average grade: {best_student} ({best_avg:.2f})")

def passed_students(students):
    passed = {k: sum(v) / len(v) for k, v in students.items() if (sum(v) / len(v)) >= 50}
    print(f"Number of students who passed: {len(passed)}")



students = {"Nanda":[85, 90, 78, 92],
            "Laxman":[60, 65, 70, 75],
            "Kishore":[40, 45, 50, 55],
            "Sai":[95, 100, 98, 92]}
calculate_avg_grade(students)
highest_grade(students)
passed_students(students)



s = [("Nanda",19),
     ("Kishore",18),
     ("Sai",20),
     ("Nanda",21)]

fil = lambda x:x[1]>=20
maps = list(filter(fil,s))
print(maps)
# local
# enclosing
# class
# global


# warrior = Warrior("Thor", 100, 20, 10, 5,67)
# mage = Mage("Gandalf", 80, 25, 5, 7, mana=30)
# archer = Archer("Alex", 75, 22, 8, 10, critical_chance=0.3)