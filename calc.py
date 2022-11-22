# Створіть командно (2-3 учні) програму-калькулятор. Перший учень створює проект/файл/клас,
# де буде знаходитися програма й надіслати його за допомогою інструментів IDE на віддалений сервер.
# Кожний наступний учень повинен клонувати проект на свій комп’ютер, додати свої частинки програми,
# зробити коміти й надіслати ці зміни на віддалений сервер.

def func_sum(x, y) -> int:
    return x + y


def func_subtraction(x, y) -> int:
    return x - y


def func_division(x, y) -> int:
    return x / y


def func_multiplication(x, y) -> int:
    return x * y


print("Welcome to HBVY calculator")

print("""Available Operations :
'+'
'-'
'*'
'/'
'exit'
""")


def is_number(obj):
    try:
        float(obj)
        return True
    except ValueError:
        return False


while True:
    step = input('Choose the operation : ')
    match step:
        case '+':
            number_1 = input('Enter 1st number : ')
            number_2 = input('Enter 2nd number : ')
            if is_number(number_1) and is_number(number_2):
                print(f"Result is : {func_sum(float(number_1), float(number_2))}")
            else:
                print("Wrong input!")
        case '-':
            number_1 = input('Enter 1st number : ')
            number_2 = input('Enter 2nd number : ')
            if is_number(number_1) and is_number(number_2):
                print(f"Result is : {func_subtraction(float(number_1), float(number_2))}")
            else:
                print("Wrong input!")
        case '*':
            number_1 = input('Enter 1st number : ')
            number_2 = input('Enter 2nd number : ')
            if is_number(number_1) and is_number(number_2):
                print(f"Result is : {func_multiplication(float(number_1), float(number_2))}")
            else:
                print("Wrong input!")
        case '/':
            number_1 = input('Enter 1st number : ')
            number_2 = input('Enter 2nd number : ')
            if number_2 == '0':
                print("You can't devide by zero")
            elif is_number(number_1) and is_number(number_2):
                print(f"Result is : {func_division(float(number_1), float(number_2))}")
            else:
                print("Wrong input!")
        case 'exit':
            print("\nBye bye :)")
            break
        case other:
            print("Wrong input!")

