from tkinter import *

def Dividir():
    if float(Vartexto1.get()) % float(Vartexto2.get()) == 0:
        VarResultado.set("El resultado es = " + str( float(Vartexto1.get()) / float(Vartexto2.get())) + " y es exacta" )
    else:
        VarResultado.set("El resultado es = " + str( float(Vartexto1.get()) / float(Vartexto2.get())) + " y es inexacta" )

Ventana = Tk()

Ventana.title("Devin Alexander Solórzano Morales")

Ventana.geometry("400x210")

Cuadro = LabelFrame(Ventana, text = "Operaciones")
Cuadro.pack()

texto1 = Label(Cuadro, text ="introduzca su primer número: ").grid(row = 1, column = 0)
Vartexto1 = StringVar()
cuadrito1= Entry(Cuadro, textvariable = Vartexto1).grid(row = 1, column = 1, padx = 20, pady =10)

texto2 = Label(Cuadro, text ="introduzca su segundo número: ").grid(row = 2, column = 0)
Vartexto2 = StringVar()
cuadrito2= Entry(Cuadro, textvariable = Vartexto2).grid(row = 2, column = 1, padx = 20, pady =10)

Boton = Button(Cuadro, text = "Resultado", command = Dividir).grid(row = 3, columnspan = 2, pady = 10)

VarResultado = StringVar()
cuadrito3= Entry(Cuadro, textvariable = VarResultado, justify = "center").grid(row = 4, columnspan = 2, pady = 10, sticky = W + E)



Ventana.mainloop()