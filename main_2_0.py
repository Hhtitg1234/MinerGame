import eng
import rus

while True:
    language = input("Change language pls (рус, eng): \n").strip().lower()
    if language == 'рус':
        rus.rus()
    if language == 'eng':
        eng.eng()
    else:
        print("Ошибка! Повторите ввод!")
        print("Mistake! Repeat the input!\n")
