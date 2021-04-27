from tkinter import *
root = Tk()
def btnClick(number):
   global operator, display_input
   operator=operator+str(number)
   # print(operator) #debuging
   display_input.set(operator)
   # print(display_input.set(operator)) #debug

def clearDisplay():
    global operator
    operator=""
    display_input.set(operator)

def btnEqual():
    global operator
    answer = str(eval(operator))
    display_input.set(answer)
    operator=""

# main window

root.wm_title("Calculator")
display_input=StringVar() #StringVar() - tikinter variable ex- IntVar()
operator=""
# display
display = Entry(master=root, textvariable=display_input, bg="powder blue", bd=30, insertwidth=4, font=('Arial',20,'bold'),justify='right')
display.grid(columnspan=4)
# Button
# first raw
btn7 = Button(master=root, text="7", padx=16, fg='black', bg="powder blue", font=('arial',20,'bold'),command=lambda :btnClick('7'))
btn7.grid(row=1,column=0)
btn8 = Button(master=root, text="8", padx=16, fg='black',bg="powder blue", font=('arial',20,'bold'),command=lambda :btnClick(8))
btn8.grid(row=1,column=1)
btn9 = Button(master=root, text="9", padx=16, fg='black',bg="powder blue", font=('arial',20,'bold'),command=lambda :btnClick(9))
btn9.grid(row=1,column=2)
btnAdd = Button(master=root, text="+", padx=16, fg='black',bg="powder blue", font=('arial',20,'bold'),command=lambda :btnClick('+'))
btnAdd.grid(row=1,column=3)

# second raw
btn4 = Button(master=root, text="4", padx=16, fg='black', bg="powder blue", font=('arial',20,'bold'),command=lambda :btnClick(4))
btn4.grid(row=2,column=0)
btn5 = Button(master=root, text="5", padx=16, fg='black',bg="powder blue", font=('arial',20,'bold'),command=lambda :btnClick(5))
btn5.grid(row=2,column=1)
btn6 = Button(master=root, text="6", padx=16, fg='black',bg="powder blue", font=('arial',20,'bold'),command=lambda :btnClick(6))
btn6.grid(row=2,column=2)
btnSub = Button(master=root, text="-", padx=16, fg='black',bg="powder blue", font=('arial',20,'bold'),command=lambda :btnClick('-'))
btnSub.grid(row=2,column=3)

# third raw
btn1 = Button(master=root, text="1", padx=16, fg='black', bg="powder blue", font=('arial',20,'bold'),command=lambda :btnClick(1))
btn1.grid(row=3,column=0)
btn2 = Button(master=root, text="2", padx=16, fg='black',bg="powder blue", font=('arial',20,'bold'),command=lambda :btnClick(2))
btn2.grid(row=3,column=1)
btn3 = Button(master=root, text="3", padx=16, fg='black',bg="powder blue", font=('arial',20,'bold'),command=lambda :btnClick(3))
btn3.grid(row=3,column=2)
btnMul = Button(master=root, text="X", padx=16, fg='black',bg="powder blue", font=('arial',20,'bold'),command=lambda :btnClick('*'))
btnMul.grid(row=3,column=3)

# 4th raw
btnClear = Button(master=root, text="C", padx=16, fg='black', bg="powder blue", font=('arial',20,'bold'),command=clearDisplay)
btnClear.grid(row=4,column=0)
btn0 = Button(master=root, text="0", padx=16, fg='black',bg="powder blue", font=('arial',20,'bold'),command=lambda :btnClick(0))
btn0.grid(row=4,column=1)
btnEq = Button(master=root, text="=", padx=16, fg='black',bg="powder blue", font=('arial',20,'bold'),command=btnEqual)
btnEq.grid(row=4,column=2)
btnDiv = Button(master=root, text="/", padx=16, fg='black',bg="powder blue", font=('arial',20,'bold'),command=lambda :btnClick('/'))
btnDiv.grid(row=4,column=3)

root.mainloop()


# Already here to get an idea for clone repository
# Test pull request
