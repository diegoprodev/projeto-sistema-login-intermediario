import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_appearance_mode("dark blue")

janela = customtkinter.CTk()
janela.geometry("700x400")
janela.title("Sistema de Login")
janela.iconbitmap("icon.ico")
janela.resizable(False, False)

# inserindo a imagem na tela de login

img = PhotoImage(file="log.png")
Label_img = customtkinter.CTkLabel(master=janela, image=img)
Label_img.place(x=1, y=5)


janela.mainloop()



