import time
from tkinter import messagebox
import tkinter as tk
from tkinter import *

#root section
root = tk.Tk()
root.geometry("300x170")
root.title("Time Counter")

#variable 
hour=StringVar()
minute=StringVar()
second=StringVar()
hour.set("00")
minute.set("00")
second.set("00")

# Use of Entry class to take input from the user
hourEntry= Entry(root, width=2, font=("Arial",18,""),textvariable=hour)
hourEntry.place(x=80,y=20) 
minuteEntry= Entry(root, width=2, font=("Arial",18,""),textvariable=minute)
minuteEntry.place(x=130,y=20)
secondEntry= Entry(root, width=2, font=("Arial",18,""),textvariable=second)
secondEntry.place(x=180,y=20)

#flag                                                               
flag=False

#start function   
def start():
    try:# the input provided by the user is stored in here :temp
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    if (temp == 0):
        messagebox.showinfo("Countdown Completed", "Timer completed  \t\t\n\n")    
    global flag
    if temp > 0 and  flag==False:
        temp -= 1
        mins,secs = divmod(temp,60) 
        hours=0
        if mins >60:
            hours, mins = divmod(mins, 60)
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        root.update()
        time.sleep(1)
        start()    

#reset function   
def reset():    
    hour.set("00")
    minute.set("00")
    second.set("00")

#stop function     
def stops(): 
    hour.set("00")
    minute.set("00")
    second.set("00")
    start()

#pause function
def pauses():
    global flag
    flag=True

#resume function
def resumes():
    global flag
    flag = False
    start()

# button widget
btn0=Button(root, text='Start',bd='5',bg="cyan",command= start)
btn0.place(x = 82,y = 75)

btn1=Button(root, text='Stop',bd='5',bg="cyan",command=stops)
btn1.place(x = 132,y = 75)

btn2=Button(root, text='Reset',bd='5',bg="cyan",command= reset)
btn2.place(x = 180,y = 75)

btn3=Button(root, text='Pause',bd='5',bg="yellow",command= pauses)
btn3.place(x = 90,y = 115)

btn4=Button(root, text='Resume',bd='5',bg="yellow",command= resumes)
btn4.place(x = 150,y = 115)

# infinite loop which is required to run tkinter program infinitely until an interrupt occurs
root.mainloop()
