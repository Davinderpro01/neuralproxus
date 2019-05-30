from tkinter import *
Devin = Tk()

Devin.geometry("230x130")

Alexander = LabelFrame(Devin).place(x=50, y=20)

#creamos un input donde ingresar valores
Label(Alexander, text = 'primer numero: ').grid(row = 1, column = 0)
var1 = Entry(Alexander)
var1.grid(row = 1, column = 1)

# igual que arriba una etiqueta y un campo input para ingresar valores
Label(Alexander, text = 'segundo numero: ').grid(row = 2, column = 0)
var2 = Entry(Alexander)
var2.grid(row = 2, column = 1)

Boton = Button(Alexander, text = "Dividir").place(x=90, y=50)

Devin.title('Devin  solórzano')

Devin.mainloop()


"# genovese" 
