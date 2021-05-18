import sys
from tkinter import *
import os

 


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Rejestracja")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Podaj dane", ).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Nazwa użytkownika  ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Hasło ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="By Kola1025#7777").pack()
    Button(register_screen, text="Rejestracja", width=10, height=1, bg="green", command = register_user).pack()
 
 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Podaj dane do logowania").pack()
    Label(login_screen, text="By Kola#7777").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Nazwa Użytkowanika  ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Hasło  ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, bg="#93F600", command = login_verify).pack()
 
def info():
    global info_screen
    info_screen = Toplevel(main_screen)
    info_screen.title("Informacje")
    info_screen.geometry("300x250")
    info_screen.configure(bg="#93F600")
    Label(info_screen, text="By Kola1025 #7777", bg="#93F600",).pack()
    Label(info_screen, text="V0.2", bg="#93F600").pack()
    Label(info_screen, text="18 May 2021", bg="#93F600").pack()
    Button(info_screen, text="Zamknij", bg="green", command=zamknij2).pack()
    Label(text="") 
    


def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Zarejestrowano pomyślnie", fg="green", font=("calibri", 11)).pack()
 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            kal_zwyk()

            
            
        else:
            password_not_recognised()
 
    else:
        user_not_found()

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Sukces")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Zalogowano Pomyślnie").pack()
    Button(login_success_screen, text="OK", command=kal_zwyk).pack()
    
def kal_zwyk():
    global kal_zwyk_screen
    kal_zwyk_screen = Toplevel(login_screen)
    kal_zwyk_screen.title("Wybierz wersje")
    kal_zwyk_screen.geometry("150x150")
    Label(kal_zwyk_screen, text="Wybier wersję:").pack()
    Button(kal_zwyk_screen, text="Profesjonalny", command=pro ).pack()
    Button(kal_zwyk_screen, text="Zwykły",command=zwyk).pack()
    Button(kal_zwyk_screen, text="Zamknij", command=zamknij1).pack()

def zwyk():
    import calc

def pro():
    global pro_screen
    pro_screen = Toplevel(login_screen)
    pro_screen.title("Ta funkcja wyjdzie w wersji 0.3 Przepraszamy" )
    Label(pro_screen, text="Ta funkcja wyjdzie w wersji 0.3 Przepraszamy").pack()
    Button(pro_screen, text="OK",command=zamknij).pack()
     


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Sukces")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Złe hasło ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="Użytkownik nie znaleziony").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def zamknij2():
    info_screen.destroy()

def zamknijperm():
    sys.exit()

def zamknij1():
    kal_zwyk_screen.destroy()

def zamknij():
    pro_screen.destroy()


def delete_login_success():
    login_success_screen.destroy()
    
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x350")
    main_screen.title("Calculit!") 
    Label(text="Wybierz Metodę", bg="#007FFF", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Logowanie", bg="#BCE27F", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Rejestracja", bg="#BCE27F", height="2", width="30", command=register).pack()
    Label(text="").pack()
    Button(text="Informacje", bg="#BCE27F", height="2", width="30", command=info).pack()
    Label(text="").pack()
    Button(text="Zamknij", bg="#BCE27F", height="2", width="30", command=zamknijperm).pack()
    main_screen.mainloop()


 
main_account_screen()
 


