from tkinter import *

# esta es la función que ejecuta la división
def Dividir():
    if (float(Vartexto1.get()) % float(Vartexto2.get()) == 0):
        VarResultado.set("El resultado es: " + str( float(Vartexto1.get()) / float(Vartexto2.get()) ) + ", la division \n fue exacta.")
    else:
        VarResultado.set("El resultado es: " + str( float(Vartexto1.get()) / float(Vartexto2.get()) ) + ", la division \n fue inexacta.")

Devin = Tk()
Devin.title("Devin Solórzano")

Devin.geometry("400x210")

#Darle diseño al frame
Alexander = LabelFrame(Devin, text = "División")
Alexander.pack()

#creamos un input donde ingresar valores
texto1 = Label(Alexander, text = 'Primer numero: ').grid(row = 1, column = 0)
Vartexto1 = StringVar()
cuadro1 = Entry(Alexander, textvariable= Vartexto1).grid(row = 1, column = 1, padx = 50, pady = 20)

# igual que arriba una etiqueta y un campo input para ingresar valores
texto2 =Label(Alexander, text = 'Segundo numero: ').grid(row = 2, column = 0)
Vartexto2 = StringVar()
cuadro2 = Entry(Alexander, textvariable= Vartexto2).grid(row = 2, column = 1, padx = 50, pady = 10)

Boton = Button(Alexander, text = "División", command = Dividir).grid(row = 3, columnspan = 2, pady = 10)

VarResultado = StringVar()
Cuadro3 = Entry(Alexander, textvariable=VarResultado, justify = "center").grid(row = 4, columnspan = 2, pady = 10, sticky = W + E)

Devin.mainloop()


