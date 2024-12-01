from tkinter import *
import calendar

root = Tk()
root.geometry("160x150")
root.title("calendar")

def showCal():
    root2 = Tk()
    root2.geometry("550x565")
    root2.title(entry.get())
    fetch_year = int(entry.get())
    ctcal = calendar.calendar(fetch_year)
    yrcal = Label(root2, text=ctcal, font = "Consolas 10 bold")
    yrcal.grid(row=5, column=1, padx=20)
    root2.mainloop()

l1 = Label(root, text="calandar", bg="dark gray", font=("roboto",28,'bold'))
l1.grid(row=1, column=1)
l2 = Label(root, text="enter year", bg="light green", font=("roboto", 15, 'bold'))
l2.grid(row=2, column=1)

entry = Entry(root)
entry.grid(row=3, column=1)

b1 = Button(root, text="show calendar", bg="black", fg="white", command=showCal)
b1.grid(row=4,column=1)
b2 = Button(root, text="close", bg="navy blue",fg=("pink"), command=exit)
b2.grid(row=5, column=1)

root.mainloop()