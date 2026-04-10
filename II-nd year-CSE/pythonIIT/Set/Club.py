records = [
    "Arun:AI,ML,Robotics",
    "Bala:ML,IoT",
    "Chitra:AI,CyberSecurity",
    "Divya:Robotics,IoT,AI",
    "Ezhil:ML,CyberSecurity",
    "Farah:AI,ML",
    "Ganesh:IoT,Robotics,AI",
    "Hari:ML"
]
clubs = set()

for record in records:
   club_part = record.split(":")[1]
   club_list = club_part.split(",")
   for club in club_list:
      clubs.add(club)
print(clubs)
[24bcs155@mepcolinux set]$cat hw.py
records = [
    "Arun:AI,ML,Robotics",
    "Bala:ML,IoT",
    "Chitra:AI,CyberSecurity",
    "Divya:Robotics,IoT,AI",
    "Ezhil:ML,CyberSecurity",
    "Farah:AI,ML",
    "Ganesh:IoT,Robotics,AI",
    "Hari:ML"
]

#1. Unique student names
students = set()

for record in records:
    name = record.split(":")[0]
    students.add(name)
print("Unique students name")
print(students)

#2. Unique clubs
clubs = set()

for record in records:
    club_part = record.split(":")[1]
    club_list = club_part.split(",")

    for club in club_list:
        clubs.add(club)
print("Unique clubs")
print(clubs)

#3 & 4. Student → Club mapping
student_clubs = {}

for record in records:
    parts = record.split(":")
    name = parts[0]
    club_list = parts[1].split(",")

    club_set = set()
    for club in club_list:
        club_set.add(club)

    student_clubs[name] = club_set

print(student_clubs)

#5. Students in both AI and ML
result = set()

for name in student_clubs:
    if "AI" in student_clubs[name]:
        if "ML" in student_clubs[name]:
            result.add(name)
print("Students in both AI and ML")
print(result)

#6. AI but NOT Robotics
result = set()

for name in student_clubs:
    if "AI" in student_clubs[name]:
        if "Robotics" not in student_clubs[name]:
            result.add(name)
print("Student in AI but not in Robotics") 
print(result)

#7. Clubs common to students whose names start with a vowel
vowel_students = []

for name in student_clubs:
    if name[0].lower() in "aeiou":
        vowel_students.append(name)

common_clubs = set(student_clubs[vowel_students[0]])

for name in vowel_students:
    new_common = set()
    for club in common_clubs:
        if club in student_clubs[name]:
            new_common.add(club)
    common_clubs = new_common
print("Clubs common to students whose names start with a vowel")
print(common_clubs)

#8. Union of clubs (names end with consonant)
union_clubs = set()

for name in student_clubs:
    if name[-1].lower() not in "aeiou":
        for club in student_clubs[name]:
            union_clubs.add(club)
print("Union of clubs and student name end with a constant")
print(union_clubs)

#9. All characters in student names
characters = set()

for name in students:
    for ch in name.lower():
        characters.add(ch)
print("All characters in student name")
print(characters)

#10. Characters present in every student name
names_list = list(students)
common_chars = set(names_list[0].lower())

for name in names_list:
    new_common = set()
    for ch in common_chars:
        if ch in name.lower():
            new_common.add(ch)
    common_chars = new_common
print("Character present in every student name")
print(common_chars)

#11. Names whose letters come only from "Arun"
arun_letters = set("arun")
result = set()

for name in student_clubs:
    valid = True
    for ch in name.lower():
        if ch not in arun_letters:
            valid = False
    if valid:
        result.add(name)
print("Names whose letters come only from ")
print(result)

#12. Duplicate club combinations
club_sets = list(student_clubs.values())
visited = []

for clubs in club_sets:
    count = 0
    for c in club_sets:
        if c == clubs:
            count += 1

    if count > 1 and clubs not in visited:
        print(clubs, "->", count, "students")
        visited.append(clubs)
print("Duplicate club combinations")
print(club_sets)


#13. Sort students (NO sorted())
students_list = list(student_clubs.items())

for i in range(len(students_list)):
    for j in range(i + 1, len(students_list)):
        a = students_list[i]
        b = students_list[j]

        if len(a[1]) < len(b[1]) or (len(a[1]) == len(b[1]) and a[0] > b[0]):
            students_list[i], students_list[j] = students_list[j], students_list[i]
print("Sort students clubs")
print(students_list)

#14. Final students
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

hari_clubs = student_clubs["Hari"]
final_students = set()

for name in student_clubs:
    clubs = student_clubs[name]

    if is_prime(len(name)):
        vowel_club = False
        for c in clubs:
            if c[0].lower() in "aeiou":
                vowel_club = True

        common = False
        for c in clubs:
            if c in hari_clubs:
                common = True

        if vowel_club and not common:
            final_students.add(name)
print("Final students")
print(final_students)
