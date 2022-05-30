"""filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form ddmmyy: ")
if birthday in pi_string:
    print("yes")
else:
    print("no")"""

filename = 'learning_python.txt'

with open('learning_python.txt') as file_object:
    content = file_object.read()
print(content)

with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())