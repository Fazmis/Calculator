def calc():
    num1 = int(input('\nПервое число: '))
    action = input('Действие: ')
    num2 = int(input('Второе число: '))
    action_dict = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }

    if action in action_dict:
        print(f'Итого: {action_dict[action](num1, num2)}\n')
        if input('Жми Q, чтобы завершить: ') in ['Q', 'q', 'Й', 'й']:
            return
        else:
            calc()
    else:
        print('Неверное действие!')
        calc()


print('Вас приветствует простой калькулятор :3')
calc()
