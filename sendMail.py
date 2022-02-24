from tkinter import *
from tkinter.filedialog import askopenfilename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import smtplib
from email import encoders
from tkinter import messagebox
root = Tk()
root.title("Code Mail")
root.geometry('1080x690')
root.iconbitmap("Resources/code.ico")

file_path = ""

def open_file():
   global f
   global file_path
   file = askopenfilename(filetypes=[("All files", "*.*")])
   if file is not None:
      file_path = file


mail_id = ""
mail_pswd = ""
def cred():
   global mail_id, mail_pswd
   data = open("Credentials/cred.txt", "r")
   mail_data = data.read()
   email_data = mail_data.partition(",")
   email_id = email_data[0]
   pswd = email_data[2]
   mail_id = email_id
   mail_pswd = pswd
cred()

def send():
   global mail_id, mail_pswd
   to = to_mail.get()
   Subject = subject_entry.get()
   Body = body_entry.get()
   global file_path
   global f
   from_addr = str(mail_id)
   password = str(mail_pswd)
   msg = MIMEMultipart()
   msg['From'] = from_addr
   msg['To'] = to
   msg['Subject'] = Subject
   msg['Body'] = Body

   if file_path == "" :
      msg.attach(MIMEText(Body, 'plain'))
      print(msg)
   else:
      msg.attach(MIMEText(Body, 'plain'))

      filename = file_path.split("/")
      filename = filename[-1]

      attachment = open(file_path, "rb")

      p = MIMEBase('application', 'octet-stream')
      p.set_payload((attachment).read())
      encoders.encode_base64(p)
      p.add_header('Content-Disposition',
                   "attachment; filename= %s" % filename)
      msg.attach(p)



   smtp = smtplib.SMTP('smtp.gmail.com', 587)
   smtp.starttls()
   smtp.login(from_addr, password)
   text = msg.as_string()
   smtp.sendmail(from_addr, to, text)
   smtp.quit




def trial():
   try:
	   send()
   except:
	   messagebox.showerror("Error!", "Either Email address or Password is wrong please restart the app :(")



to_email = Label(root, text="To email address:", font=("aharoni", 15))
to_email.pack()
to_mail = Entry(root, width=100)

to_mail.pack()
subject_label = Label(root, text="Subject:", font=("aharoni", 15))
subject_label.pack()
subject_entry = Entry(root, width=100)

subject_entry.pack()
body_label = Label(root, text="Body:", font=("aharoni", 15))
body_label.pack()
body_entry = Entry(root, width=100)

body_entry.pack()
btn = Button(root, text='Open', bg="#1EE8AB", width=30, command=open_file)

btn.pack(side=TOP, pady=10)

send_btn = Button(root, text="send", bg="#1EE8AB", width=30, command=trial)
send_btn.pack()

root.mainloop()
