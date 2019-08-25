from tkinter import *
from DES2 import *
root = Tk()

root.title("Simulation Exact Result")
'''
test_bt = Button(root,text="run test",bg="pink" )
test_bt.grid(row = 9 , column = 1)

#rand_bt = Button(root,text="run random",bg="blue"  )
#rand_bt.grid(row = 9 , column = 3)

'''
label_run = Label(root,bg = "green" , text = "status")
label_run.grid(row = 9  , column= 2)

label_run.configure(text= "RANDOM RUN")

#img = PhotoImage(file = r'stockIcon.gif')
#root.tk.call('wm', 'iconphoto', root._w, img)


def myname():
    print("I'm Nazanin Bayati master student of IUST at CE college")
    print("std# : 96723056")
def myemail():
    print("Email: n_bayati@comp.iust.ac.ir")
menu=Menu(root)
root.config(menu=menu)

profileMenu = Menu(menu)
menu.add_cascade(label="About me", menu=profileMenu )
profileMenu.add_command(label="Profile" , command = myname)
profileMenu.add_separator()
profileMenu.add_command(label="Email" , command = myemail)

exitMenu = Menu(menu)
menu.add_cascade(label = "Exit"  , command = quit)



status= Label(root,text = "                                                 " , fg ="gray")
status.grid(row=0)
status= Label(root,text = "                       " , fg ="gray")
status.grid(column=4)

lable3=Label(root , text="Service Number")
lable3.grid(row=1)
entry3  = Entry(root)
entry3.grid(row=1,column = 1)
entry3.insert(END,str(NumberService))

lable4=Label(root,text="           System Clock            ")
lable4.grid(row=1,column = 2)
entry4 = Entry(root)
entry4.grid(row=1 , column = 3)
entry4.insert(END,str(clock))

lable5=Label(root , text="Area under B(t)")
lable5.grid(row=2)
entry5  = Entry(root)
entry5.grid(row=2,column = 1)
entry5.insert(END,str(Area_under_B))

lable6=Label(root,text="Area under Q(t)")
lable6.grid(row=2,column = 2)
entry6 = Entry(root)
entry6.grid(row=2 , column = 3)
entry6.insert(END,str(Area_under_Q))

lable7=Label(root , text="Total delay")
lable7.grid(row=3)
entry7  = Entry(root)
entry7.grid(row=3,column = 1)
entry7.insert(END,str(totdelay))


lable8=Label(root,text="value of Wq")
lable8.grid(row=3,column = 2)
entry8 = Entry(root)
entry8.grid(row=3 , column = 3)
entry8.insert(END,str(Wq))

lable9=Label(root , text="value of Lq")
lable9.grid(row=4)
entry9  = Entry(root)
entry9.grid(row=4,column = 1)
entry9.insert(END,str(Lq))

lable10=Label(root,text="value of Rou")
lable10.grid(row=4,column = 2)
entry10 = Entry(root)
entry10.grid(row=4 , column = 3)
entry10.insert(END,str(p))

lable11=Label(root , text="value of L")
lable11.grid(row=5)
entry11  = Entry(root)
entry11.grid(row=5,column = 1)
entry11.insert(END,str(L))

lable12=Label(root,text="value of Es")
lable12.grid(row=5,column = 2)
entry12 = Entry(root )
entry12.grid(row=5 , column = 3)
entry12.insert(END,str(value_of_Es))

lable13=Label(root , text="value of W")
lable13.grid(row=6)
entry13  = Entry(root)
entry13.grid(row=6,column = 1)
entry13.insert(END,str(W))

lable14=Label(root,text="value of Landa")
lable14.grid(row=6,column = 2)
entry14 = Entry(root)
entry14.grid(row=6 , column = 3)
entry14.insert(END,str(Landa))


lable1=Label(root , text="value of Mou")
lable1.grid(row=7)
entry1  = Entry(root)
entry1.grid(row=7,column = 1)
entry1.insert(END,str(M))


lable2=Label(root,text="Throughput")
lable2.grid(row=7,column = 2)
entry2 = Entry(root)
entry2.grid(row=7 , column = 3)
entry2.insert(END,str(throughput))

status= Label(root,text = "                                                 " , fg ="gray")
status.grid(row=8)


status= Label(root,text = "                                                 " , fg ="gray")
status.grid(row=10)
status= Label(root,text = "Welcome to NBayati_Simulation Program :) " , fg ="gray")
status.grid(row=11)
root.mainloop()













#@NAZANIN BAYATI




















