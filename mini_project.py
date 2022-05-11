lines = None
with open('data.txt') as file:
    lines = file.readlines()

if not lines:
    print("something went wrong")
    exit()

marks_lines = lines[1:]
subject_marks = {}

for lines in marks_lines:
    entries = lines.split()

    name = entries[0].strip()
    subject = entries[1].strip()
    marks = int(entries[2].strip())

    if subject not in subject_marks:
        subject_marks[subject] = {}

    subject_marks[subject][name] = marks

print(subject_marks)