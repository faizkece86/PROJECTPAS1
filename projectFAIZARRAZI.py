from tkinter import *
from tkinter import messagebox
import random 


peluang = 10
x = random.randint(1,100)
info = """
Kamu kalah
Kesempatanmu telah habis
Silahkan klik menu 'Restart'
"""

menang = """
Selamat, kamu menang!!
Silahkan klik menu 'Restart'
"""

root = Tk()
root.title("Tebak Angka")
root.resizable(FALSE, FALSE)
root.config(background = "Light blue")

Label(root, text="Tebak Angka", font="Times 40 bold",
     background="light blue").grid(columnspan=2, column=0, row=0,
     pady=10, padx=20)
label1 = Label(root, text=" ", font="Normal 20",
         background="light blue")
label1.grid(row=2, column=0, columnspan=2, pady=3)
label2 = Label(root, text="Tebak Angka", font="Normal 20",
         background="light blue")
label2.grid(row=3, column=0, columnspan=2)

label3 = Label(root, text="Kamu memiliki 10 peluang", font="Normal 20",
         background="light blue")
label3.grid(row=4, column=0, columnspan=2, pady=10)

def cek_angka():
    global peluang
    try:
        if int(entry.get())>x:
            label1.config(text=entry.get())
            entry.delete(0, END)
            label2.config(text='Angka tebakan lebih kecil')
            peluang -= 1
            label3.config(text=f'tersisa {peluang} kesempatan lagi')
            if peluang == 0:
                button.config(state=DISABLED)
                entry.config(state=DISABLED)
                label2.config(text="Kesempatan telah habis")
                messagebox.showinfo("Tebak Angka", info)

        if int(entry.get())<x:
            label1.config(text=entry.get())
            entry.delete(0, END)
            label2.config(text='Angka tebakan lebih besar')
            peluang -= 1
            label3.config(text=f'tersisa {peluang} kesempatan lagi')
            if peluang == 0:
                button.config(state=DISABLED)
                entry.config(state=DISABLED)
                label2.config(text="Kesempatan telah habis")
                messagebox.showinfo("Tebak Angka", info)

        if int(entry.get()) == x:
            label1.config(text=entry.get())   
            peluang -= 1
            label2.config(text="Selamat, tebakanmu benar")
            label3.config(text=f'tersisa {peluang} kesempatan lagi')
            button.config(state=DISABLED)
            entry.config(state=DISABLED)
            messagebox.showinfo("Tebak Angka")
                        
    except:
        entry.delete(0,END)

entry = Entry(root, font="Normal 20", relief=RIDGE, bd=5)
entry.grid(column=0, row=1, ipady=5, pady=10, padx=10)
button = Button(root, text="CEK", font="Normal 17",
         relief=RIDGE, bd=5, activebackground="blue",
         command=cek_angka)
button.grid(column=1, row=1, padx=7)


def restart():
    global x, peluang
    peluang = 10
    x = random.randint(1, 100)
    print(x)
    label1.config(text=" ")
    label2.config(text="Tebak angkanya")
    label3.config(text="Kamu memiliki 10 peluang")
    button.config(state=NORMAL)
    entry.config(state=NORMAL)

menubar = Menu(root, tearoff=False)
root.config(menu=menubar)
menubar.add_command(label="Restart", command=restart)


root.mainloop()