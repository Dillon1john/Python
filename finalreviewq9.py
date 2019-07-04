CST_courses=['CST 1100', 'CST 1101', 'CST 1201', 'CST 1204']
GenEd_courses=['ENG 1101', 'ENG 1121', 'MAT 1375', 'PSY 1101']
current_courses=GenEd_courses
for i in CST_courses:
    current_courses.append(i)
print(current_courses[5])
