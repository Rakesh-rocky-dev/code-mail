from tkinter import *
from tkinter.font import Font
import qrcode
from PIL import Image
root = Tk()
root.title("Codec")
root.geometry("1080x690")
root.iconbitmap("Resources/code.ico")
main_frame= Frame(root)
string_to_bin_frame = Frame(main_frame)
str_bin_out = Entry(string_to_bin_frame, width=30)
def string_to_bin():
   global str_bin_out, bin_entry
   bin_string = bin_entry.get()
   print(bin_string)
   for i in bin_string:
      result_binary = ''.join(format(ord(i), '08b'))
      data = result_binary
   str_bin_out.delete(0, END)
   str_bin_out.insert(0,data)

string_to_morse_frame = Frame(main_frame)
str_mor_out = Entry(string_to_morse_frame, width=30)
def string_to_morse_code():
   global str_mor_out, str_to_morse_entry
   value = str_to_morse_entry.get()
   string = value.upper()
   morse_code = {'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.', 'G': '__.', 'H': '....', 'I': '..', 'J': '.___', 'K': '_._', 'L': '._..', 'M': '__', 'N': '_.', 'O': '___', 'P': '.__.', 'Q': '__._', 'R': '._.', 'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._','Y': '_.__', 'Z': '__..', '1': '.____', '2': '..___', '3': '...__', '4': '...._', '5': '.....', '6': '_....', '7': '__...', '8': '___..', '9': '____.', '0': '______', '?': '..__..', '!': '_._.__', '.': '._._._', ',': '__..__', ';': '_._._.', ':': '___...', '+': '._._.', '-': '_...._', '/': '_.._.', '=': '_..._'}
   result = []
   for element in range(0, len(string)):
      result_data = morse_code.get(string[element])
      result.append(result_data)
   data = "".join(result)
   str_mor_out.delete(0,END)
   str_mor_out.insert(0, data)

morse_to_string_frame = Frame(main_frame)
mor_str_out = Entry(morse_to_string_frame, width=30)
def morse_code_to_string():
   global mor_str_out, morse_to_entry
   value = morse_to_entry.get()
   alpha_code = {'._': 'A', '_...': 'B', '_._.': 'C', '_..': 'D', '.': 'E', '.._.': 'F', '__.': 'G', '....': 'H', '..': 'I', '.___': 'J', '_._': 'K', '._..': 'L', '__': 'M', '_.': 'N', '___': 'O', '.__.': 'P', '__._': 'Q', '._.': 'R', '...': 'S', '_': 'T', '.._': 'U', '..._': 'V', '.__': 'W', '_.._': 'X',
                 '_.__': 'Y', '__..': 'Z', '.____': '1', '..___': '2', '...__': '3', '...._': '4', '.....': "5", '_....': "6", '__...': "7", '___..': "8", '____.': "9", '______': "0", '..__..': "?", '_._.__': "!", '._._._': ".", '__..__': ",", '_._._.': ";", '___...': ":", '._._.': "+", '_...._': "-", '_.._.': "/", '_..._': "="}
   code = value.split()
   for element in range(0, len(code)):
      result = alpha_code.get(code[element])
   result_data = "".join(result)
   print(result_data)
   mor_str_out.delete(0, END)
   mor_str_out.insert(0, result_data)



string_to_qrcode_frame = Frame(main_frame)
def string_to_qrcode():
   global str_to_qr_entry, canvas
   y = str_to_qr_entry.get()
   img = qrcode.make(y)
   img.save("OUTPUT/qr_code.png")

def clear(entry, output_entry):
   entry.delete(0, END)
   output_entry.delete(0, END)

def clear_qr():
   global str_to_qr_entry
   str_to_qr_entry.delete(0, END)

str_to_bin = Label(string_to_bin_frame, text="String to Binary Converter", font=("Helvetica", 15))
str_to_bin.pack(pady=3)
enter_label = Label(string_to_bin_frame, text="Enter the string:")
enter_label.pack(pady=3)
bin_entry = Entry(string_to_bin_frame, width=30)
bin_entry.pack(pady=3)
string_to_bin_entry = bin_entry.get()
str_bin_btn = Button(string_to_bin_frame, text="Convert",
                     width=30, bg="#1EE8AB", command=string_to_bin)
str_bin_btn.pack(pady=3)
clear_btn = Button(string_to_bin_frame, text="Clear", width=30,
                   bg="#1EE8AB", command=lambda: clear(bin_entry, str_bin_out))
clear_btn.pack(pady = 3)

str_bin_out.pack(pady=3)

string_to_bin_frame.pack(side=RIGHT, padx=30)
str_morse = Label(string_to_morse_frame,
                  text="String To Morse Code", font=("Helvetica", 15))
str_morse.pack(pady=3)
str_morse_en_la = Label(string_to_morse_frame, text="Enter the String: ")
str_morse_en_la.pack(pady=3)
str_to_morse_entry = Entry(string_to_morse_frame, width=30)
str_to_morse_entry.pack(pady=3)
str_to_morse_string = str_to_morse_entry.get()
str_mor_btn = Button(string_to_morse_frame, width=30,
                     text="Convert", bg="#1EE8AB", command=string_to_morse_code)
str_mor_btn.pack(pady=3)
clear_str_mor = Button(string_to_morse_frame, width=30,
                       text="Clear", bg="#1EE8AB")
clear_str_mor.config(command=lambda: clear(str_to_morse_entry, str_mor_out))
clear_str_mor.pack(pady=3)

str_mor_out.pack(pady=3)
string_to_morse_frame.pack(side=RIGHT, padx=30)
morse_str = Label(morse_to_string_frame, text="Morse To String",
                  font=("Helvetica", 15))
morse_str.pack(pady=3)
morse_str_en_la = Label(morse_to_string_frame, text="Enter the Morse Code: ")
morse_str_en_la.pack(pady=3)
morse_to_entry = Entry(morse_to_string_frame, width=30)
morse_to_entry.pack(pady=3)
morse_to_str_string = str_to_morse_entry.get()
mor_str_btn_fr = Frame(morse_to_string_frame)
mor_str_btn_fr.pack(pady=3)
mor_str_btn = Button(mor_str_btn_fr, width=30, text="Convert",
                     bg="#1EE8AB", command=morse_code_to_string)
mor_str_btn.pack(pady=3)
clear_mor_str = Button(mor_str_btn_fr, width=30, text="Clear", bg="#1EE8AB")
clear_mor_str.config(command=lambda: clear(morse_to_entry, mor_str_out))
clear_mor_str.pack(pady=3)

mor_str_out.pack(pady=3)

morse_to_string_frame.pack(side=RIGHT, padx=30)
str_to_qr_la = Label(string_to_qrcode_frame,
                     text="String To Qr code", font=("Helvetica", 15))
str_to_qr_la.pack(pady=3)
enter_str_qr_la = Label(string_to_qrcode_frame, text="enter the string:")
enter_str_qr_la.pack(pady=3)
str_to_qr_entry = Entry(string_to_qrcode_frame, width=30)
str_to_qr_entry.pack(pady=3)
qr_img_btn = Button(string_to_qrcode_frame, width=30, bg="#1EE8AB",text="Save & Convert", command=string_to_qrcode)
qr_img_btn.pack(pady=3)
clear_entry_btn = Button(string_to_qrcode_frame, text="Clear", width=30, bg="#1EE8AB", command=clear_qr)
clear_entry_btn.pack(pady=3)
string_to_qrcode_frame.pack(side=RIGHT, padx=30)

main_frame.pack(pady=250)
root.mainloop()