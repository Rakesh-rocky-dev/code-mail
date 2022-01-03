
import imaplib
import email
from pprint import pprint
from tkinter import *
from tkinter import messagebox
from functools import lru_cache
email_id_data = ""
mail_pswd = ""
def cred():
   global email_id_data, mail_pswd
   data = open("Credentials/cred.txt", "r")
   mail_data = data.read()
   email_data = mail_data.partition(",")
   email_id = email_data[0]
   pswd = email_data[2]
   email_id_data = email_id
   mail_pswd = pswd

cred()
print(email_id_data, mail_pswd)


@lru_cache(maxsize=None)
def read():
	global email_id_data, mail_pswd
	host = "imap.gmail.com"
	mail = imaplib.IMAP4_SSL(host)
	mail.login("007codemail@gmail.com", mail_pswd)
	mail.select("Inbox")
	_, search_data = mail.search(None, 'ALL')

	my_msg = []
	for num in search_data[0].split():
		email_data = {}
		_, data = mail.fetch(num, '(RFC822)')

		_, mail_data = data[0]
		email_msg = email.message_from_bytes(mail_data)

		for header in ['subjects', 'to', 'from', 'data']:
			email_data[header] = email_msg[header]

		for part in email_msg.walk():
	            	 if part.get_content_type() == "text/plain":
	               		body = part.get_payload(decode=True)
	               		email_data['body'] = body.decode()
		my_msg.append(email_data)
	return my_msg



try:
	read()
except:
	message_box = messagebox.showerror("Error!","Either Email address or Password is wrong please restart the app :(")



msg_data = read()
length = len(read())
data_from = []
data_body = []
for i in range(length):
	from_data = msg_data[i]['from']
	body_data = msg_data[i]['body']
	if "<" in list(from_data):
		from_data = from_data.split("<")[1].split(">")[0]
	else:
		from_data = from_data

	data_from.append(from_data)
	data_body.append(body_data)
pprint(f"from: {data_from}, body: {data_body}")

root = Tk()
root.title("Read_mail")
root.geometry("1080x690")
root.iconbitmap("Resources/code.ico")
j = 1
frame = Frame(root)
myscrollbar = Scrollbar(frame, orient='vertical')
myscrollbar.pack(side=RIGHT, fill=Y)
hscrollbar = Scrollbar(frame, orient='horizontal')
hscrollbar.pack(side=BOTTOM, fill=X)
listbox = Listbox(frame, bg="#53565A", fg="white",
                  width=150, height=35, border=4)
for i in range(len(data_from)):

    from_msg = data_from[i]
    body_msg = data_body[i]
    listbox.insert(j, " From: \n")
    j = j + 1
    listbox.insert(j, f" {from_msg}\n")
    j = j + 1
    listbox.insert(j, " Body: \n")
    j = j + 1
    listbox.insert(j, f" {body_msg}\n")
    j = j + 1
    listbox.insert(j, "	__________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    j = j + 1


listbox.config(yscrollcommand=myscrollbar.set)
myscrollbar.config(command=listbox.yview)
listbox.config(xscrollcommand=hscrollbar.set)
hscrollbar.config(command=listbox.xview)
listbox.pack()
frame.pack(fill=BOTH, expand=1)

root.mainloop()
