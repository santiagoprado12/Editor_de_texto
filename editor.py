from tkinter import *

ruta=""  #La utilizaremos para almacenar la ruta de un fichero

def nuevo():
    mensaje.set("Nuevo fichero")
    
def abrir():
    mensaje.set("abrir fichero")
def guardar():
    mensaje.set("guardar fichero")
def guardar_como():
    mensaje.set("guardar como")



root=Tk()
root.title("Mi editor")

#Menu superior 
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Nuevo",command=nuevo)
filemenu.add_command(label="Abrir",command=abrir)
filemenu.add_command(label="Guardar",command=guardar)
filemenu.add_command(label="Guardar como",command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")


#Caja de texto central
texto=Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0,padx=6,pady=4,font=("Consolas",12))

# Moitor inferior
mensaje=StringVar()
mensaje.set("Bienvenido a tu editor")
monitor=Label(root,textvar=mensaje,justify='left')
monitor.pack(side="left")


root.config(menu=menubar)


root.mainloop()