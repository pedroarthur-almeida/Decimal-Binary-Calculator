from tkinter import *

#aqui eu crio uma janela e seto suas configuracoes, dentre elas suas dimensoes e sua cor de fundo.
window = Tk()
window.title("Decimal-Binary Calculator")
window.geometry("550x270")
window.configure(bg='#1E1E2F')

#aqui eu crio o label de bem vindo
label_welcome = Label(window, text='Welcome to calc!', font=('Consolas', 30), bg='#1E1E2F', fg='white')
label_welcome.grid(column=0, row=0, columnspan=3, pady=(10, 10)) #o columnspan serve para definir quantas colunas o label ocupara, o pady serve para definir espacos acima e abaixo do label.

#aqui eu crio os labels de exibicao
label_decimaltobinary = Label(window, text='Decimal → Binary', bg='#1E1E2F', fg='white', font=('Consolas', 15))
label_decimaltobinary.grid(column=0, row=1, sticky='w', padx=(20, 20), pady=(20, 20)) #padx, serve para fixar o espacamento horizontal, enquanto o pady fixa o espacamento vertical. o sticky serve para "grudar" o label em um local, nesse caso no "west", a esquerda.

label_binarytodecimal = Label(window, text='Binary → Decimal', bg='#1E1E2F', fg='white', font=('Consolas', 15))
label_binarytodecimal.grid(column=0, row=2, sticky='w', padx=(20, 20), pady=(10, 10))

#com o comando entry, eu crio a area onde o usuario ira digitar.
entry_decimal = Entry(window, width=20, font=('Consolas', 14))
entry_decimal.grid(column=1, row=1)

entry_binary = Entry(window, width=20, font=('Consolas', 14))
entry_binary.grid(column=1, row=2)

#por fim, crio a area de resultado.
result = Label(window, text='Result → ', bg='#1E1E2F', font=('Consolas', 15), fg='white')
result.grid(column=0, row=4, columnspan=3, pady=(30, 0))

#funcoes.
def decimaltobinary():
    try:
        decimal_value = int(entry_decimal.get())
        binary_value = bin(decimal_value)
        if binary_value.startswith('-0b'):
            binary_value = '-' + binary_value[3:]
        else:
            binary_value = binary_value[2:]
        result.config(text=f'The result of the conversion is: {binary_value}')
    except ValueError:
        result.config(text='Invalid decimal input!')

def binarytodecimal():
    try:
        binary_value = entry_binary.get()
        decimal_value = int(binary_value, 2)
        result.config(text=f'The result of the conversion is: {decimal_value}')
    except ValueError:
        result.config(text='Invalid binary input!')

#criando os botoes para converter.
button_decimaltobinary = Button(window, text='Convert', font=('Consolas', 12), command=decimaltobinary)
button_decimaltobinary.grid(column=2, row=1, padx=10)

button_binarytodecimal = Button(window, text='Convert', font=('Consolas', 12), command=binarytodecimal)
button_binarytodecimal.grid(column=2, row=2, padx=10)

#com essa funcao, eu rodo um loop infinito na janela criada.
window.mainloop()
