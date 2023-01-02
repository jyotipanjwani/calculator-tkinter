from tkinter import *
root = Tk()
root.geometry("600x400")
def addition():
    s=int(en1.get())+int(en2.get())
    r.set(s)
    print(s) 
    
def subtraction():
    k=int(en1.get())-int(en2.get())
    r.set(k)
    print(k)




#Hiii we are just testing our git




#designing the code 
# XYZ design
root.title("Calculator")
n1 = Label(text="give 1st number")
n1.pack()
r =StringVar()
en1 = Entry()
en1.pack()
n2 = Label(text="give 2nd number")
n2.pack()
en2 = Entry()
en2.pack()
bnt = Button(text="add",command=addition)
bnt.pack()
bnt2 = Button(text="subb",command=subtraction)
bnt2.pack()
pri = Label(root, textvariable=r)
pri.pack()
root.mainloop()