import tkinter

# Constants
WIDTH, HEIGHT = 233, 312

# MainWindow and Widgets
root = tkinter.Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
root.title('Calculator')
root.resizable(width=False, height=False)
root['bg'] = 'Black'
entry = tkinter.Entry(root, font=('Times New Romance', 15), justify='right')
entry.insert('end', '0')


def create_digit_button(digit):
    return tkinter.Button(root, height=2, text=digit, command=lambda: add_digit(digit),
                          font=('Times New Romance', 12), bg='Black', fg='Orange')


def create_operand_button(operand):
    return tkinter.Button(root, height=2, text=operand, command=lambda: add_operand(operand),
                          font=('Times New Romance', 10), bg='Black', fg='Red')


def create_special_button(operand, command):
    return tkinter.Button(root, height=2, text=operand, command=lambda: command(),
                          font=('Times New Romance', 12), bg='Black', fg='Red')


def c_action():
    entry.delete(0, 'end')
    value = '0'
    entry.insert(0, value)


def add_digit(num):
    value = entry.get()
    entry.delete(0, 'end')
    if value == '0' or value[:-1].isalpha():
        value = num
    else:
        value = value + num
    entry.insert('end', value)


def add_operand(operand):
    if operand == '=':
        calc()
    else:
        value = entry.get()
        entry.delete(0, 'end')
        if value[-1] in '+-**/' and value[-1] not in '()':
            value = value[:-1] + operand
        else:
            value = value + operand
        entry.insert('end', value)


def negative():
    value = entry.get()
    entry.delete(0, 'end')
    entry.insert(0, eval(value + '*(-1)'))


def calc():
    value = entry.get()
    entry.delete(0, 'end')
    if value[-1] in '+-*/':
        if value[-2:] == '**':
            value = value + '2'
        else:
            value = value + value[:-1]
    try:
        entry.insert('end', eval(value))
    except (ZeroDivisionError, SyntaxError, NameError):
        entry.insert('end', 'Ошибка!')


entry.grid(row=0, columnspan=4, sticky='we', padx=5, pady=5)
create_digit_button('0').grid(row=5, column=1, sticky='nswe', padx=3, pady=3)
create_digit_button('1').grid(row=4, column=0, sticky='nswe', padx=3, pady=3)
create_digit_button('2').grid(row=4, column=1, sticky='nswe', padx=3, pady=3)
create_digit_button('3').grid(row=4, column=2, sticky='nswe', padx=3, pady=3)
create_digit_button('4').grid(row=3, column=0, sticky='nswe', padx=3, pady=3)
create_digit_button('5').grid(row=3, column=1, sticky='nswe', padx=3, pady=3)
create_digit_button('6').grid(row=3, column=2, sticky='nswe', padx=3, pady=3)
create_digit_button('7').grid(row=2, column=0, sticky='nswe', padx=3, pady=3)
create_digit_button('8').grid(row=2, column=1, sticky='nswe', padx=3, pady=3)
create_digit_button('9').grid(row=2, column=2, sticky='nswe', padx=3, pady=3)
create_operand_button('(').grid(row=1, column=0, sticky='nswe', padx=3, pady=3)
create_operand_button(')').grid(row=1, column=1, sticky='nswe', padx=3, pady=3)
create_operand_button('**').grid(row=1, column=2, sticky='nswe', padx=3, pady=3)
create_special_button('neg', negative).grid(row=1, column=3, sticky='nswe', padx=3, pady=3)
create_operand_button('+').grid(row=5, column=3, sticky='nswe', padx=3, pady=3)
create_operand_button('-').grid(row=4, column=3, sticky='nswe', padx=3, pady=3)
create_operand_button('*').grid(row=3, column=3, sticky='nswe', padx=3, pady=3)
create_operand_button('/').grid(row=2, column=3, sticky='nswe', padx=3, pady=3)
create_operand_button('=').grid(row=5, column=2, sticky='nswe', padx=3, pady=3)
create_special_button('C', c_action).grid(row=5, column=0, sticky='nswe', padx=3, pady=3)

root.mainloop()
