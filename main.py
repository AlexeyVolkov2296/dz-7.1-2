def polish(s):
     polish_list = s.strip().split(' ')
     operators_list = ['/', '*', '-', '+']
     assert not len(polish_list) != 3, 'Не правильный формат нотации'

     operator = polish_list[0]
     assert operator in operators_list, "No signs -, +, /, *"

     try:
         operand_1 = int(polish_list[1])
         operand_2 = int(polish_list[2])
     except ValueError:
         return print(f'Ошибка приравнения  строки к числу')

     if operator == "+":
         print(operand_1 + operand_2)
     elif operator == "-":
         print(operand_1 - operand_2)
     elif operator == "*":
         print(operand_1 * operand_2)
     elif operator == "/":
         try:
             print(operand_1 / operand_2)
         except ZeroDivisionError:
             print(f'Деление на ноль не возможно')

if __name__ == '__main__':
     polish(input('введите польскую нотацию: '))