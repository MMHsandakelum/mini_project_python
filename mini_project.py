def top_marks(subject, dataset):
    max_marks = 0
    stu_name = ""

    for name, marks in dataset.items():
        if max_marks < marks:
            max_marks = marks
            stu_name = name

    return stu_name, max_marks

def get_marks(record: tuple):
    return (record[1])

lines = None
with open('data.txt') as file:
    lines = file.readlines()

if not lines:
    print("something went wrong")
    exit()

marks_lines = lines[1:]
subject_marks = {}
student_marks = {}
messages = []

for lines in marks_lines:
    entries = lines.split()

    name = entries[0].strip()
    subject = entries[1].strip()
    marks = int(entries[2].strip())

    if subject not in subject_marks:
        subject_marks[subject] = {}

    subject_marks[subject][name] = marks

    prev_marks = student_marks.get(name, 0)
    student_marks[name] = prev_marks + marks

# print(subject_marks)

for subject, dataset in subject_marks.items():
    name, marks = top_marks(subject, dataset)
    msg = f"Top student for {subject} is {name} with {marks} marks. "
    messages.append(msg)
    print(msg)

marks_list = [(name, marks) for name, marks in student_marks.items() ]

marks_list.sort(key=get_marks, reverse=True)

top = marks_list[0]
msg = f"Top student is {top[0]} with {top[1]} marks"
messages.append(msg)
print(msg)


with open('result.txt', 'w') as file:
    for msg in messages:
        file.write(msg)
        file.write('\n')

# print(student_marks)