from tkinter import *
import wikipedia
import pyttsx3
tk = Tk()
tk.title("Wikipedia Searcher...")
tk.geometry("200x200")
wiki_icon = PhotoImage(file="C:\\Users\\mycom\\OneDrive\\Documents\\wiki-icon.png")
tk.iconphoto(tk,wiki_icon)
label1 = Label(tk,text="Search wikipedia",font="Courier",bg="#81ecec",fg="white").grid(row=0,column=2)
av = StringVar()
entry = Entry(tk,textvariable=av).grid(row=1,column=2,columnspan=400)
def run():
    ai = pyttsx3.init()
    av1 = av.get()
    a = wikipedia.summary(av1,sentences=2)
    print(a)
    ai.say("according to wikipedia "+a)
    ai.runAndWait()
Button(tk,text="Search",font="Courier",bg="#6c5ce7",fg="white",command=run).grid(row=2,column=1,columnspan=400)
tk.config(bg="#81ecec")
tk.mainloop()
