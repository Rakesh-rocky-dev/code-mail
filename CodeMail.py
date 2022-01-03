
from tkinter import *
import login

root = Tk()
root.title("Code Mail")
root.geometry("350x250")
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
send_mail_btn = Button(root, text="Send Mail", width=30,
                    fg="white", bg="#1EE8AB", command=sending)
send_mail_btn.pack(pady=15)
read_mail_btn = Button(root, text="Read Mail", width=30,
                       fg="white", bg="#1EE8AB", command=reading)
read_mail_btn.pack(pady=15)
astro_btn = Button(root, text="Astro Graph", width=30,
                   fg="white", bg="#1EE8AB", command=astrographing)
astro_btn.pack(pady=15)
astro_btn = Button(root, text="Codec", width=30,
                   fg="white", bg="#1EE8AB", command=codecing)
astro_btn.pack(pady=15)
root.mainloop()
