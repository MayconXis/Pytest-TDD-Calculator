from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title('Calculadora Compass Uol')
root.geometry('408x355')
root.minsize(408,355)

root.configure(background='#282828')

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#ffffff', bg="#f38508", font=('futura', 25, 'bold'), justify=CENTER)

e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)

#funções operadores
def botao_divisao() :
    return
def botao_click() :
    return
def botao_multiplica() :
    return
    
def botao_subtracao() :
    return
divide = Button(root,
                text='÷',
                padx= 40,
                pady=20,
                command=botao_divisao,
                fg='#ffffff',
                activeforeground='#ffffff',
                bg="#000000",
                activebackground="#3D3D3D",
                relief=FLAT,
                font=('futura', 12, 'bold')
)
#primeira fileira           
divide.grid(row=0, column=4)
um = Button(    root,
                text='1',
                padx= 40,
                pady=20,
                command=lambda: botao_click(1) ,
                fg='#ffffff',
                activeforeground='#ffffff',
                bg="#000000",
                activebackground="#3D3D3D",
                relief=FLAT,
                font=('futura', 12, 'bold')
)
um.grid(row=1, column=1)

dois = Button(  root,
                text='2',
                padx= 40,
                pady=20,
                command=lambda: botao_click(2) ,
                fg='#ffffff',
                activeforeground='#ffffff',
                bg="#000000",
                activebackground="#3D3D3D",
                relief=FLAT,
                font=('futura', 12, 'bold')
)
dois.grid(row=1, column=2)

tres = Button(root,
                text='3',
                padx= 40,
                pady=20,
                command=lambda: botao_click(3) ,
                fg='#ffffff',
                activeforeground='#ffffff',
                bg="#000000",
                activebackground="#3D3D3D",
                relief=FLAT,
                font=('futura', 12, 'bold')
)

tres.grid(row=1, column=3)

multiplica = Button(root,
                text='x',
                padx= 40,
                pady=20,
                command=botao_multiplica ,
                fg='#ffffff',
                activeforeground='#ffffff',
                bg="#000000",
                activebackground="#3D3D3D",
                relief=FLAT,
                font=('futura', 12, 'bold')
)

multiplica.grid(row=1, column=4)

#segunda fileira
quatro = Button(root,
                text='4',
                padx= 40,
                pady=20,
                 command=lambda: botao_click(4) ,
                fg='#ffffff',
                activeforeground='#ffffff',
                bg="#000000",
                activebackground="#3D3D3D",
                relief=FLAT,
                font=('futura', 12, 'bold')
)

quatro.grid(row=2, column=1)

cinco = Button(root,
                text='5',
                padx= 40,
                pady=20,
                 command=lambda: botao_click(5) ,
                fg='#ffffff',
                activeforeground='#ffffff',
                bg="#000000",
                activebackground="#3D3D3D",
                relief=FLAT,
                font=('futura', 12, 'bold')
)

cinco.grid(row=2, column=2)
seis = Button(root,
                text='6',
                padx= 40,
                pady=20,
                 command=lambda: botao_click(6) ,
                fg='#ffffff',
                activeforeground='#ffffff',
                bg="#000000",
                activebackground="#3D3D3D",
                relief=FLAT,
                font=('futura', 12, 'bold')
)

seis.grid(row=2, column=3)


subtracao = Button(root,
                text='-',
                padx= 40,
                pady=20,
                command=botao_subtracao ,
                fg='#ffffff',
                activeforeground='#ffffff',
                bg="#000000",
                activebackground="#3D3D3D",
                relief=FLAT,
                font=('futura', 12, 'bold')
)
subtracao.grid(row=3, column=4)
#terceira fileira
sete = Button(root,
                text='7',
                padx= 40,
                pady=20,
                 command=lambda: botao_click(7) ,
                fg='#ffffff',
                activeforeground='#ffffff',
                bg="#000000",
                activebackground="#3D3D3D",
                relief=FLAT,
                font=('futura', 12, 'bold')
)

sete.grid(row=3, column=1)

oito = Button(root,
                text='8',
                padx= 40,
                pady=20,
                 command=lambda: botao_click(8) ,
                fg='#ffffff',
                activeforeground='#ffffff',
                bg="#000000",
                activebackground="#3D3D3D",
                relief=FLAT,
                font=('futura', 12, 'bold')
)

oito.grid(row=3, column=2)

nove = Button(root,
                text='9',
                padx= 40,
                pady=20,
                 command=lambda: botao_click(9) ,
                fg='#ffffff',
                activeforeground='#ffffff',
                bg="#000000",
                activebackground="#3D3D3D",
                relief=FLAT,
                font=('futura', 12, 'bold')
)

nove.grid(row=3, column=3)

root.mainloop()