import random

def generate_number():
    return random.randint(1, 10)

def user_answer():
    print(f"Вопрос {number_of_question + 1}:")
    print(f"{num1} {operator} {num2} = ?")
    return input("Ответ: ")

def get_correct_answer():
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    else:
        return num1 * num2

def check_answer():
    global score
    if int(answer) == correct_answer:
        score += 1
        print("Правильно!\n")
    else:
        print(f"Неправильно! Правильный ответ: {correct_answer}\n")

def result():
    print(f"Ваш итоговый счет: {score}")
    if score == 5:
        print("Отличный результат! Вы настоящий математик!")
    elif score >= 3:
        print("Хороший результат! Продолжайте заниматься математикой!")
    else:
        print("Плохой результат. Попробуйте еще раз.")

score = 0

for number_of_question in range(5):
    num1 = generate_number()
    num2 = generate_number()
    operator = random.choice(['+', '-', '*'])
    answer = user_answer()
    correct_answer = get_correct_answer()
    check_answer()

result()
