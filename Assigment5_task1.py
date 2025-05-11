## Task 1: Create a Dictionary of Student Marks

student_marks = {'Marks': 85 ,
              'Alice': 80,
              'Boby': 90,
              'Charlie': 75}

student_name = input('Enter the Student''s Name:')

if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print('Students mot found in the record')