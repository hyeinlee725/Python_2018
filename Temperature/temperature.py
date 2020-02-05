from tkinter import *
def f2c(): #화씨->섭씨
    temp = float(e1.get()) 
    mytemp = (temp-32)*5/9 
    e2.insert(0, str(mytemp))

def c2f(): #섭씨->화씨
	# 아래를 완성하시오.
    temp = float(e2.get())
    mytemp = (temp*9/5)+32
    e1.insert(0, str(mytemp))
   

   

window  = Tk()

l1 = Label(window , text="화씨")
l2 = Label(window, text="섭씨")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(window, text="화씨->섭씨", command=f2c)
# 아래 문장을 적절하게 고치시오
b2 = Button(window, text="섭씨->화씨", command=c2f)

b1.grid(row=2, column=0)
b2.grid(row=2, column=1)

window.mainloop()


