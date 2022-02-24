from asyncore import read
from tkinter import *
import login

root = Tk()
root.title("Code Mail")
root.geometry("450x300")
root.iconbitmap("Resources/code.ico")
def sending():
   print("send")
   import sendMail
def reading():
   print("reading")
   import ReadMail
def astrographing():
   print("astrographing")
   import astrograph
def codecing():
   import codec
def logout():
   file = open("Credentials\cred.txt", 'w')
   file.write(" ")
   file.close()
   
send_mail_btn = Button(root, text="Send Mail", width=30,
                    fg="white", bg="#1EE8AB", command=sending)
send_mail_btn.pack(pady=15)
read_mail_btn = Button(root, text="Read Mail", width=30,
                       fg="white", bg="#1EE8AB", command=reading)
read_mail_btn.pack(pady=15)
astro_btn = Button(root, text="Astro Graph", width=30,
                   fg="white", bg="#1EE8AB", command=astrographing)
astro_btn.pack(pady=15)
code_btn = Button(root, text="Codec", width=30,
                   fg="white", bg="#1EE8AB", command=codecing)
code_btn.pack(pady=15)
logout_btn = Button(root, text="LogOut", width=30,fg="white", bg="#1EE8AB", command=logout)
logout_btn.pack(pady=15)
root.mainloop()
