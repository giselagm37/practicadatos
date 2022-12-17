import tkinter as tk
import baseDatos 
from tkinter import messagebox
import utils
import base64 #viene con Python incripta el codigo(se hace en login y donde se registra)

windows=tk.Tk()
windows.title("Registro de Usuarios")
windows.geometry("400x400")

#texto
lUsername=tk.Label(text='Ingresar nombre de usuario') ##font= para cambio de letra
lUsername.place(x=10,y=10) 
#ingrese datos#Usuario
eUsername=tk.Entry()
eUsername.place(x=200,y=10)

#Fecha de nacimiento
lNacimiento=tk.Label(text='Ingrese fecha de Nacimiento')
lNacimiento.place(x=10, y=50)
#Entry
eNacimiento=tk.Entry()
eNacimiento.place(x=200, y=50)

#mail
lEmail=tk.Label(text='Ingrese su mail')
lEmail.place(x=10, y=90)
eEmail=tk.Entry()
eEmail.place(x=200,y=90)

#password
lPassword=tk.Label(text='Ingrese contraseña')
lPassword.place(x=10, y=130)
ePassword=tk.Entry(show="*")#no se ve la contraseña
ePassword.place(x=200,y=130)

#validar usuario
def registrar():
    username=eUsername.get()
    uValidate=userValidate(username)
    nacimiento=eNacimiento.get()
    email=eEmail.get()
    password=ePassword.get()
    if uValidate:
        baseDatos.saveData(username,nacimiento,email,password)
        messagebox.showinfo('mensaje', 'usuario registrado exitosamente')
    limpiarFormulario()

##no guarda las contraseñas pero no las registra en la base
def comprobarPassword():
    password=ePassword.get()
    password=password.encode('ascii')
    password=base64.b64encode(password)
    if len(password)<8:
        messagebox.showinfo('Mensaje','La contraseña debe tener al menos 8 caracteres')
        limpiarFormulario()
        
def registrar():
    username=eUsername.get()
    nacimiento=eNacimiento.get()
    email=eEmail.get()
    password=ePassword.get()
    if utils.nameValidator(username):
        if utils.dateValidator(nacimiento):
            if utils.emailValidator(email):   
                try:
                  baseDatos.saveData(username,nacimiento,email,password)
                  messagebox.showinfo('Mensaje','Usuario registrado exitosamente')
                  limpiarFormulario()
                except:
                  messagebox.showinfo('Mensaje','El usuario no pudo ser registrado')
            else:
                messagebox.showinfo('Mensaje','Correo electronico con formato incorrecto')
        else:
            messagebox.showinfo('Mensaje','Fecha con formato incorrecto')
            limpiarFormulario()                    


def userValidate(username):
    if len(username)<4:
        messagebox.showinfo('mensaje','El usuario debe tener al menos 4 caracteres')
        
    

#limpiar formulario
def limpiarFormulario():
    eUsername.delete(0,tk.END) 
    eNacimiento.delete(0,tk.END)
    eEmail.delete(0,tk.END)  
    ePassword.delete(0,tk.END)

#Boton
bRegistrar=tk.Button(text='Registrar',bg='blue4',fg='white',command=registrar)
bRegistrar.place(x=150, y=170)

tk.mainloop()