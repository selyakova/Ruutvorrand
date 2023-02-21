from tkinter import *
from tkinter import ttk
def solver(a,b,c):
    D=b*b-4*a*c
    if D>=0:
        x1=(-b+sqrt(D)/(2*a))
        x1=(-b-sqrt(D)/(2*a))
        text="D= %s \n x1 = %s \n x2 = %s \n" % (D,x1,x2)
    else:
        text="D= %s \n See korrutis "
    return text
def inserter(value):
    output.delete("0.0",END)
    output.insert("0.0",value)
def handler():
    try:
        a_val=float(a.get())
        b_val=float(a.get())
        c_val=float(a.get())
        inserter(solver(a_val,b_val,c_val))
    except ValueError:
        inserter("Error")
aken=Tk()
aken.title("Ruutvõrrand")
aken.geometry("600x300")
aken.resizable(width=False,height=False)
aken.mainloop()
f_top=Frame(aken)
f_bot=Frame(aken)
f_top.pack()
f_bot.pack()
a=Entry(f_top,width=5,font="Arial 20")
a.pack(side=LEFT,pady=10,padx=10)
a_lab=Label(f_top,text="x^2+",font="Arial 20").pack(side=LEFT,pady=10)
b=Entry(f_top,width=5,font="Arial 20")
b.pack(side=LEFT,pady=10,padx=10)
b_lab=Label(f_top,text="x+",font="Arial 20").pack(side=LEFT,pady=10)
c=Entry(f_top,width=5,font="Arial 20")
c.pack(side=LEFT,pady=10,padx=10)
c_lab=Label(f_top,text="=0",font="Arial 20").pack(side=LEFT,pady=10)
btn=Button(f_top,text="Lahendada",font="Arial 20 bold",command=handler).pack(side=LEFT,pady=10,padx=10)
output=Text(f_bot,bg="ace8e3",fg="green",font="Arial 20")
output.pack(expand=1,fill=BOTH,side=LEFT)





