import tkinter as tk
import baseDatos
from tkinter import messagebox #deja mensaje en pantalla
import base64

windows=tk.Tk()
windows.title("Registro de usuarios")
windows.geometry('400x200')

lUsername=tk.Label(text='Ingrese su nombre de usuario')
lUsername.place(x=10, y=20)
eUsername=tk.Entry()
eUsername.place(x=200, y=20)

lPassword=tk.Label(text='Ingrese su contraseña')
lPassword.place(x=10, y=70)
ePassword=tk.Entry(show='*')
ePassword.place(x=200, y=70)

#Trae datos del entry
def login():
    username=eUsername.get()
    password=ePassword.get()
    password=password.encode('ascii')
    password=base64.b64encode(password)
    if baseDatos.loginData(username,password):
        messagebox.showinfo('mensaje','Bienvenido a la plataforma')
    else:
        messagebox.showinfo('mensaje','Usuario o contraseña incorrectos')
    limpiarFormulario()     #para limpiarlo siempre   
                
#limpia formulario
def limpiarFormulario():
    eUsername.delete(0,tk.END)
    ePassword.delete(0,tk.END)

bLogin=tk.Button(text='login',bg='blue4', fg='white',command=login)
bLogin.place(x=150, y=170)

tk.mainloop()    