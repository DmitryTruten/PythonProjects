"""filename = 'programming'

with open(filename, 'a') as file_object:
    file_object.write('\n1337\n')
    file_object.write('Because it's my meaning of life.')"""

# 10-3 Guest
"""name_prompt = input("What's your name? ")
filename = 'guest'

with open(filename, 'w') as file_object:
    file_object.write(name_prompt)"""

# 10-4 Guest book

# Визначаємо змінну, що ссилається на файл, в який будемо записувати імена
"""filename = 'guest_book'

# Записуємо заголовок до файлу у режимі запису
with open(filename, 'w') as file_object:
    file_object.write("Guest List\n")

# Створюємо лічильник для нумерації гостей за списком
count = 0

# Головний цикл
while True:
    name_prompt = input("What's your name? (enter stop to end program) ")
    count += 1
    if name_prompt == 'stop':
        break

    count_and_name = f'{count}. {name_prompt.title()}'

# Записуємо відформатовані імена до файлу в режимі допису
    with open(filename, 'a') as file_object:
        file_object.write(count_and_name + '\n')
        print(f"Hello, {name_prompt.title()}. Nice to meet you!\n")"""






