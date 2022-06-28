import tkinter

# Constants
WIDTH, HEIGHT = 640, 480

# MainWindow and Widgets
root = tkinter.Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
root.title('Calculator')
root.resizable(width=False, height=False)


def button_click(button, number='', list_num=None, sign = None):
    if list_num is None:
        list_num = []
    sign_dict = {
        '+': lambda x: x[0] + x[1],
        '-': lambda x: x[0] - x[1],
        '*': lambda x: x[0] - x[1],
        '/': lambda x: x[0] - x[1],
        '=': lambda x: x[0],
        None: 'Ошибка :с'
    }
    if button not in '+-*/=':
        number += button
    elif button != '=':
        list_num.append(number)
        number = ''
        sign = button
    else:
        label.configure(text=f'{sign_dict[sign]}')


def place_buttons(width, height, button_width=8, button_height=4):
    label = tkinter.Label(root, text='Начните писать выражение!', width=width, font=('Time New Romance', 18))
    label.place(x=(width - label.winfo_reqwidth())//2, y=30)

    zero = tkinter.Button(root, text='0', width=button_width, height=button_height, command=button_click('0'))
    reqwidth = zero.winfo_reqwidth()
    reqheight = zero.winfo_reqheight()
    x_bt = (width - reqwidth)//2
    y_bt = height - reqheight - 10
    zero.place(x=x_bt, y=y_bt)

    one = tkinter.Button(root, text='1', width=button_width, height=button_height, command=button_click('1'))
    x_bt = (width - reqwidth) // 2 - reqwidth - 5
    y_bt = height - 2*reqheight - 15
    one.place(x=x_bt, y=y_bt)

    two = tkinter.Button(root, text='2', width=button_width, height=button_height, command=button_click('2'))
    x_bt = (width - reqwidth) // 2
    y_bt = height - 2*reqheight - 15
    two.place(x=x_bt, y=y_bt)

    three = tkinter.Button(root, text='3', width=button_width, height=button_height, command=button_click('3'))
    x_bt = (width - reqwidth) // 2 + reqwidth + 5
    y_bt = height - 2*reqheight - 15
    three.place(x=x_bt, y=y_bt)

    four = tkinter.Button(root, text='4', width=button_width, height=button_height, command=button_click('4'))
    x_bt = (width - reqwidth) // 2 - reqwidth - 5
    y_bt = height - 3 * reqheight - 20
    four.place(x=x_bt, y=y_bt)

    five = tkinter.Button(root, text='5', width=button_width, height=button_height, command=button_click('5'))
    x_bt = (width - reqwidth) // 2
    y_bt = height - 3 * reqheight - 20
    five.place(x=x_bt, y=y_bt)

    six = tkinter.Button(root, text='6', width=button_width, height=button_height, command=button_click('6'))
    x_bt = (width - reqwidth) // 2 + reqwidth + 5
    y_bt = height - 3 * reqheight - 20
    six.place(x=x_bt, y=y_bt)

    seven = tkinter.Button(root, text='7', width=button_width, height=button_height, command=button_click('7'))
    x_bt = (width - reqwidth) // 2 - reqwidth - 5
    y_bt = height - 4 * reqheight - 25
    seven.place(x=x_bt, y=y_bt)

    eight = tkinter.Button(root, text='8', width=button_width, height=button_height, command=button_click('8'))
    x_bt = (width - reqwidth) // 2
    y_bt = height - 4 * reqheight - 25
    eight.place(x=x_bt, y=y_bt)

    nine = tkinter.Button(root, text='9', width=button_width, height=button_height, command=button_click('9'))
    x_bt = (width - reqwidth) // 2 + reqwidth + 5
    y_bt = height - 4 * reqheight - 25
    nine.place(x=x_bt, y=y_bt)

    plus = tkinter.Button(root, text='+', width=button_width, height=button_height, command=button_click('+'))
    x_bt = (width - reqwidth) // 2 + 2 * reqwidth + 10
    y_bt = height - 2 * reqheight - 15
    plus.place(x=x_bt, y=y_bt)

    minus = tkinter.Button(root, text='-', width=button_width, height=button_height, command=button_click('-'))
    x_bt = (width - reqwidth) // 2 + 2 * reqwidth + 10
    y_bt = height - 3 * reqheight - 20
    minus.place(x=x_bt, y=y_bt)

    multiply = tkinter.Button(root, text='*', width=button_width, height=button_height, command=button_click('*'))
    x_bt = (width - reqwidth) // 2 + 2 * reqwidth + 10
    y_bt = height - 4 * reqheight - 25
    multiply.place(x=x_bt, y=y_bt)

    divide = tkinter.Button(root, text='/', width=button_width, height=button_height, command=button_click('/'))
    x_bt = (width - reqwidth) // 2 + 2 * reqwidth + 10
    y_bt = height - 5 * reqheight - 30
    divide.place(x=x_bt, y=y_bt)

    equals = tkinter.Button(root, text='=', width=button_width, height=button_height, command=button_click('='))
    x_bt = (width - reqwidth) // 2 + 2 * reqwidth + 10
    y_bt = height - reqheight - 15
    equals.place(x=x_bt, y=y_bt)


root.mainloop()
