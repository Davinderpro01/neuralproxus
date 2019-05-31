from tkinter import ttk
from tkinter import *
Devin = Tk()
Devin.title("Devin Solórzano")

Devin.geometry("400x200")

#Darle diseño al frame
Alexander = LabelFrame(Devin, text = "División")
Alexander.pack()

#creamos un input donde ingresar valores
texto1 = Label(Alexander, text = 'Primer numero: ').grid(row = 1, column = 0)
cuadro1 = Entry(Alexander).grid(row = 1, column = 1, padx = 50, pady = 20)

# igual que arriba una etiqueta y un campo input para ingresar valores
texto2 =Label(Alexander, text = 'Segundo numero: ').grid(row = 2, column = 0)
cuadro2 = Entry(Alexander).grid(row = 2, column = 1, padx = 50, pady = 10)

Boton = Button(Alexander, text = "División").grid(row = 3, columnspan = 2, pady = 10)

#imprimir mensaje
mensaje = Label(Alexander, text = ' ', fg= "red").grid(row = 4, columnspan = 2)

# esta es la función que ejecuta la división
def dividir():
    resultado = float(cuadro1.get() ) / float( cuadro2.get())
    resultado2 = float(cuadro1.get() ) % float( cuadro2.get())
    if(resultado2 == 0):
        mensaje['text'] = 'La division es exacta y es: {}'.format(resultado)
    else:
        mensaje['text'] = 'La division es inexacta y es: {}'.format(resultado) 

Devin.mainloop()


