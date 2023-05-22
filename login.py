import customtkinter as ctk
from tkinter import *
ctk.set_appearance_mode("dark")
ctk.set_appearance_mode("dark blue")

janela = ctk.CTk()
janela.geometry("800x400")
janela.title("Sistema de Login")
janela.iconbitmap("icon.png")
janela.resizable(False, False)

# inserindo a imagem na tela de login

img = PhotoImage(file="log.png")
Label_img = ctk.CTkLabel(master=janela, image=img)
Label_img.place(x=1, y=5)


janela.mainloop()



