import tkinter as tk
raiz = tk.Tk()
raiz.title("Primera ventana")
raiz.geometry("520x480")
entrada = tk.Entry()
entrada.place(x=50, y=50, width = 150)
boton = tk.Button(text="aceptar")
boton.place(x=50, y=100)
raiz.mainloop()
