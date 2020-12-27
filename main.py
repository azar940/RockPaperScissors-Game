from tkinter import *
import random
#head
root = Tk()
root.title("Rock/Paper/Scissors By Aziz")
root.iconbitmap('016-c.png')
root.geometry("500x400")
root.columnconfigure([0, 1, 2], weight=3)
root.rowconfigure([0, 2], weight=2)

iconrock = PhotoImage(file=r"C:\Users\AZAR\Downloads\Compressed\rock.png")
iconpaper = PhotoImage(file=r"C:\Users\AZAR\Downloads\Compressed\Paper.png")
iconscissor = PhotoImage(file=r"C:\Users\AZAR\Downloads\Compressed\Scissors.png")
iconwin1 = PhotoImage(file=r"C:\Users\AZAR\Downloads\Compressed\001-trophy.png")
iconwin2 = PhotoImage(file=r"C:\Users\AZAR\Downloads\Compressed\002-winner.png")
iconwin3 = PhotoImage(file=r"C:\Users\AZAR\Downloads\Compressed\003-medal.png")
iconwin4 = PhotoImage(file=r"C:\Users\AZAR\Downloads\Compressed\004-winner-1.png")
iconlost1 = PhotoImage(file=r"C:\Users\AZAR\Downloads\Compressed\006-lost.png")
iconlost2 = PhotoImage(file=r"C:\Users\AZAR\Downloads\Compressed\007-signal.png")
iconta3adol1 = PhotoImage(file=r"C:\Users\AZAR\Downloads\Compressed\005-panel.png")
iconta3adol2 = PhotoImage(file=r"C:\Users\AZAR\Downloads\Compressed\008-humanpictos.png")

items = ["1", "2", "3"]
rch = random.choice(items)

iconwin = [iconwin1, iconwin2, iconwin3, iconwin4]
iconlost = [iconlost1, iconlost2]
iconta3adol = [iconta3adol1, iconta3adol2]
iconwinrandomchoosed = random.choice(iconwin)
iconlostrandomchoosed = random.choice(iconlost)
iconta3adolrandomchoosed = random.choice(iconta3adol)


print(rch)

#def body
def buttonicond(win,img,text,rw,clm,clms,rws,id,nd):
    Button(win,  image=img, text=text, state=nd, command=lambda: choose(id)).grid(row=rw, column=clm, columnspan=clms, rowspan=rws, sticky=N+S+W+E)

def finchoose(text,imgw):
    Label(root, text=text, font = '100', bg="#BA4747").grid(row=1, column=0,columnspan=2, sticky=N+S+W+E)
    Label(root, image=imgw, bg="#BA4747").grid(row=1, column=2, sticky=N+S+W+E)


def choose(id):
    global winer
    global butz
    global buty
    global butx
    global but1
    global but2
    global but3

    if rch == "1":
        butz = buttonicond(root, iconrock, "", 0, 0, 1, 1, id="1", nd=DISABLED)
        buty = buttonicond(root, iconrock, "", 0, 1, 1, 1, id="2", nd=DISABLED)
        butx = buttonicond(root, iconrock, "", 0, 2, 1, 1, id="3", nd=DISABLED)
    elif rch == "2":
        butz = buttonicond(root, iconpaper, "", 0, 0, 1, 1, id="1", nd=DISABLED)
        buty = buttonicond(root, iconpaper, "", 0, 1, 1, 1, id="2", nd=DISABLED)
        butx = buttonicond(root, iconpaper, "", 0, 2, 1, 1, id="3", nd=DISABLED)
    else:
        butz = buttonicond(root, iconscissor, "", 0, 0, 1, 1, id="1", nd=DISABLED)
        buty = buttonicond(root, iconscissor, "", 0, 1, 1, 1, id="2", nd=DISABLED)
        butx = buttonicond(root, iconscissor, "", 0, 2, 1, 1, id="3", nd=DISABLED)
    if id == rch:
        but1 = buttonicond(root, iconrock, "", 2, 0, 1, 1, id="1", nd=DISABLED)
        but2 = buttonicond(root, iconpaper, "", 2, 1, 1, 1, id="2", nd=DISABLED)
        but3 = buttonicond(root, iconscissor, "", 2, 2, 1, 1, id="3", nd=DISABLED)
        #messagebox.showinfo(title="winer!!?",message="ta3adooool!")
        txt="ta3adooool!"
        finchoose(txt, iconta3adolrandomchoosed)
    elif id == "1" and rch == "3":
        #messagebox.showinfo(title="winer!!?", message="neta li rebe7ti!")
        txt = "neta li rebe7ti!!"
        finchoose(txt, iconwinrandomchoosed)
        but1 = buttonicond(root, iconrock, "", 2, 0, 1, 1, id="1", nd=DISABLED)
        but2 = buttonicond(root, iconrock, "", 2, 1, 1, 1, id="2", nd=DISABLED)
        but3 = buttonicond(root, iconrock, "", 2, 2, 1, 1, id="3", nd=DISABLED)
    elif id == "2" and rch == "1":
        but1 = buttonicond(root, iconpaper, "", 2, 0, 1, 1, id="1", nd=DISABLED)
        but2 = buttonicond(root, iconpaper, "", 2, 1, 1, 1, id="2", nd=DISABLED)
        but3 = buttonicond(root, iconpaper, "", 2, 2, 1, 1, id="3", nd=DISABLED)
        txt = "neta li rebe7ti!!"
        finchoose(txt, iconwinrandomchoosed)
        #messagebox.showinfo(title="winer!!?", message="neta li rebe7ti!")
    elif id == "3" and rch == "2":
        but1 = buttonicond(root, iconscissor, "", 2, 0, 1, 1, id="1", nd=DISABLED)
        but2 = buttonicond(root, iconscissor, "", 2, 1, 1, 1, id="2", nd=DISABLED)
        but3 = buttonicond(root, iconscissor, "", 2, 2, 1, 1, id="3", nd=DISABLED)
        txt = "neta li rebe7ti!!"
        finchoose(txt, iconwinrandomchoosed)
        #messagebox.showinfo(title="winer!!?", message="neta li rebe7ti!")




    elif rch == "1" and id == "3":
        but1 = buttonicond(root, iconscissor, "", 2, 0, 1, 1, id="1", nd=DISABLED)
        but2 = buttonicond(root, iconscissor, "", 2, 1, 1, 1, id="2", nd=DISABLED)
        but3 = buttonicond(root, iconscissor, "", 2, 2, 1, 1, id="3", nd=DISABLED)
        txt = "kheserti!!"
        finchoose(txt, iconlostrandomchoosed)
        #messagebox.showinfo(title="winer!!?", message="kheserti!")
    elif rch == "2" and id == "1":
        but1 = buttonicond(root, iconrock, "", 2, 0, 1, 1, id="1", nd=DISABLED)
        but2 = buttonicond(root, iconrock, "", 2, 1, 1, 1, id="2", nd=DISABLED)
        but3 = buttonicond(root, iconrock, "", 2, 2, 1, 1, id="3", nd=DISABLED)
        txt = "kheserti!!"
        finchoose(txt, iconlostrandomchoosed)
        #messagebox.showinfo(title="winer!!?", message="kheserti!")
    elif rch == "3" and id == "2":
        but1 = buttonicond(root, iconpaper, "", 2, 0, 1, 1, id="1", nd=DISABLED)
        but2 = buttonicond(root, iconpaper, "", 2, 1, 1, 1, id="2", nd=DISABLED)
        but3 = buttonicond(root, iconpaper, "", 2, 2, 1, 1, id="3", nd=DISABLED)
        txt = "kheserti!!"
        finchoose(txt, iconlostrandomchoosed)
        #messagebox.showinfo(title="winer!!?", message="kheserti!")

butz=buttonicond(root, iconrock, "", 0, 0, 1, 1,id="1", nd=DISABLED)
buty=buttonicond(root, iconpaper, "", 0, 1, 1, 1,id="2", nd=DISABLED)
butx=buttonicond(root, iconscissor, "", 0, 2, 1, 1,id="3", nd=DISABLED)
but1=buttonicond(root, iconrock, "", 2, 0, 1, 1,id="1", nd=NORMAL)
but2=buttonicond(root, iconpaper, "", 2, 1, 1, 1,id="2", nd=NORMAL)
but3=buttonicond(root, iconscissor, "", 2, 2, 1, 1,id="3", nd=NORMAL)


root.mainloop()
