from tkinter import *


print("starting")
root = Tk()
root.title("Code Mail")
root.geometry("1080x690")
root.iconbitmap("Resources/code.ico")
login_tab = Frame(root)
def credentials():
   email = entry_username.get()
   paswd = entry_password.get()
   file = open("Credentials/cred.txt", "w")
   cred_data = f"{email},{paswd}"
   file.write(cred_data)
   print(email, paswd)
   file.close()
   data = open("Credentials/cred.txt", "r")
   mail_data = data.read()
   email_data = mail_data.partition(",")
   email_id = email_data[0]
   pswd = email_data[2]
   print(email_id, pswd)
   root.destroy()
   return email_id, pswd

def login_page():
   global entry_username, entry_password
   frame = Frame(login_tab, width=50, height=100)
   frame.pack(pady=30)
   login_label = Label(frame, text="Login")
   login_label.config(font=("aharoni", 50))
   login_label.pack(pady=30)
   label_username = Label(frame, text="Email:")
   label_username.pack(pady=5)
   entry_username = Entry(frame, width=30)
   entry_username.pack(pady=5)
   label_password = Label(frame, text="Password")
   label_password.pack(pady=5)
   entry_password = Entry(frame, width=30)
   entry_password.pack(pady=5)
   submit_button = Button(frame, width=30, bg="#1EE8AB", text="Login", command=credentials)
   submit_button.pack(pady=15)
   login_tab.pack()

login_page()
root.mainloop()


