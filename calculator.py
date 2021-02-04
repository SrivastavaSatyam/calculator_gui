# importing necessary libraries/modules-------------------------------------

from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox

# initializing the tkinter window-------------------------------------------

root=Tk()
root.title("Calculator")
root.maxsize(300, 300)
x=root.winfo_x()
y=root.winfo_x()
root.geometry("+%d+%d" % (x+500,y+240))

# add this to disable your window close button .  
def donothing():
    pass
root.protocol('WM_DELETE_WINDOW', donothing) 

# Menubar Functions in calculator------------------------------------------------

def about():
    tkinter.messagebox.showinfo("Calculator"," A Python made GUI Calculator, that will help you to do simple calculation.\n© Satyam Srivastava")

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def destroy():
    exit=tkinter.messagebox.askyesno("Calculator","Are you sure you want to exit.")
    if exit>0:
        root.destroy()

# Adding menubar in calculator------------------------------------------------

menu=Menu(root)
root.config(menu=menu)
filemenu = Menu(menu,tearoff=0,activebackground='#00008B',activeborderwidth=5,font=("@Adobe Kaiti Std R", 10))
menu.add_cascade(label="Options",menu=filemenu)
filemenu.add_command(label="About",command=about)
filemenu.add_separator()
filemenu.add_cascade(label="All Clear",command=clrdisplay)
menu.add_cascade(label="Exit",command=destroy)



# Adding images in Calculator------------------------------------------------------

p1=PhotoImage(file=r'C:\PROJECTS\hotel_management\CALCULATOR\img\calculator.png')
root.iconphoto(False,p1)

p=PhotoImage(file = "C:/PROJECTS/hotel_management/CALCULATOR/img/tags.png" )
path = p.subsample(16,18)


# Functions for Calculator------------------------------------------------------

operator=""
text_Input=StringVar()

def  btnclick(numbers):
    global operator
    operator += str(numbers)
    text_Input.set(operator)
    
def remove():
    global operator
    a=len(operator)
    e.delete(a-1,"end")  
    operator=operator[0:-1]  
    

def eqals():
    try:
        global operator
        sumup=str(eval(operator))
        text_Input.set(sumup) 
        operator=''

    except:
        tkinter.messagebox.showerror("Calculator","Something went wrong.")

# Setting Frame for calculator--------------------------------------------------

frm1=Frame(root)
frm1.pack()

scrollbar = Scrollbar(frm1)
scrollbar.grid( row=2,column=10 )


e=Entry(frm1,textvariable=text_Input,bd=5,selectbackground="blue",width=10,justify="right",font=('Verdana',30),xscrollcommand = scrollbar.set)
e.grid(row=2,column=6,columnspan=9)
scrollbar.config( command = e.xview )


#Making  the necessary buttons required--------------------------------------------------

btn1=Button(frm1,text="7",width=8,height=3,bg="white",bd=4, command=lambda: btnclick("7"))
btn1.grid(row=3,column=6)
btn2=Button(frm1,text="8",width=8,height=3,bg="white",bd=4, command=lambda: btnclick("8"))
btn2.grid(row=3,column=7)
btn3=Button(frm1,text="9",width=8,height=3,bg="white",bd=4, command=lambda: btnclick("9"))
btn3.grid(row=3,column=8)
btn4=Button(frm1,text="+",width=8,height=3,bg="blue",foreground="white",bd=4, command=lambda: btnclick("+"))
btn4.grid(row=3,column=9)
btn5=Button(frm1,text="4",width=8,height=3,bg="white",bd=4, command=lambda: btnclick("4"))
btn5.grid(row=4,column=6)
btn6=Button(frm1,text="5",width=8,height=3,bg="white",bd=4, command=lambda: btnclick("5"))
btn6.grid(row=4,column=7)
btn7=Button(frm1,text="6",width=8,height=3,bg="white",bd=4, command=lambda: btnclick("6"))
btn7.grid(row=4,column=8)
btn8=Button(frm1,text="-",width=8,height=3,bg="blue",foreground="white",bd=4, command=lambda: btnclick("-"))
btn8.grid(row=4,column=9)
btn9=Button(frm1,text="1",width=8,height=3,bg="white",bd=4, command=lambda: btnclick("1"))
btn9.grid(row=5,column=6)
btn10=Button(frm1,text="2",width=8,height=3,bg="white",bd=4, command=lambda: btnclick("2"))
btn10.grid(row=5,column=7)
btn11=Button(frm1,text="3",width=8,height=3,bg="white",bd=4, command=lambda: btnclick("3"))
btn11.grid(row=5,column=8)
btn12=Button(frm1,text="*",width=8,height=3,bg="blue",foreground="white",bd=4, command=lambda: btnclick("*"))
btn12.grid(row=5,column=9)
btn13=Button(frm1,text="=",width=8,height=3,bg="blue",foreground="white",bd=4,command=eqals)
btn13.grid(row=6,column=8)
btn14=Button(frm1,image=path,bg="blue",width=60,height=50,foreground="white",bd=4, command=remove)
btn14.grid(row=6,column=7)
btn15=Button(frm1,text="0",width=8,height=3,bg="blue",foreground="white",bd=4, command=lambda: btnclick("0"))
btn15.grid(row=6,column=6)
btn16=Button(frm1,text="÷",width=8,height=3,bg="blue",foreground="white",bd=4, command=lambda: btnclick("/"))
btn16.grid(row=6,column=9)

# Run the Tkinter event loop----------------------------

root.mainloop()
