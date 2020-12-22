import tkinter as tk
global final
final=0
last=0
count=1
root=tk.Tk()
#task=======================
def b1():
    global count
    label.insert(tk.END,1)  
    count=0
def b2():
    global count
    label.insert(tk.END,2)
    count=0
def b3():
    global count
    label.insert(tk.END,3)
    count=0
def b4():
    global count
    label.insert(tk.END,4)
    count=0
def b5():
    global count
    label.insert(tk.END,5)
    count=0
def b6():
    global count
    label.insert(tk.END,6)
    count=0
def b7():
    global count
    label.insert(tk.END,7)
    count=0
def b8():
    global count
    label.insert(tk.END,8)
    count=0
def b9():
    global count
    label.insert(tk.END,9)
    count=0
def b0():
    global count
    label.insert(tk.END,0)
    count=0
    
            
def addition():
    global final
    global last,fi
    global count
    fi=float(label.get())
    label.delete(0,tk.END)
    final=final+fi
    last=1
    count=0
def subtraction():
    global final
    global last,fi
    global count
    cs=0
    fi=float(label.get())
    if cs!=0:
        final=final-fi
    final=fi
    cs=1    
    last=2
    label.delete(0,tk.END)
    count=0
def multiplication():
    global final
    global last,fi
    global count
    cm=0
    fi=float(label.get())
    if cm!=0:
        final=final*fi
    final=fi
    cm=1
    last=3
    label.delete(0,tk.END)
    count=0
def division():
    global final
    global last,fi
    global count
    cd=0
    fi=float(label.get())
    if cd!=0:
        final=final/fi
    final=fi
    cd=1
    last=4
    label.delete(0,tk.END)
    count=0
def equal():
    global final
    global last,fi
    
    if last==1:
        fi=float(label.get())
        final+=fi
        label.delete(0,tk.END)
        label.insert(0,final)
    elif last==2:
        fi=float(label.get())
        final-=fi
        label.delete(0,tk.END)
        label.insert(0,final)
    elif last==3:
        fi=float(label.get())
        final*=fi
        label.delete(0,tk.END)
        label.insert(0,final)
    elif last==4:
        fi=float(label.get())
        final/=fi
        label.delete(0,tk.END)
        label.insert(0,final)
    else:
        fi=float(label.get())
        label.delete(0,tk.END)
        label.insert(0,fi)
        
    final=0
    fi=0
        
def deci():
    global count
    if count!=1:
        label.insert(tk.END,".")
def cl():
    global final
    global last,fi
    label.delete(0,tk.END)
    final=0
    fi=0
    
    
  
#keys=============================        
label=tk.Entry()
b1=tk.Button(master=root,text="1",command=b1)
b2=tk.Button(master=root,text="2",command=b2)
b3=tk.Button(master=root,text="3",command=b3)
b4=tk.Button(master=root,text="4",command=b4)
b5=tk.Button(master=root,text="5",command=b5)
b6=tk.Button(master=root,text="6",command=b6)
b7=tk.Button(master=root,text="7",command=b7)
b8=tk.Button(master=root,text="8",command=b8)
b9=tk.Button(master=root,text="9",command=b9)
b0=tk.Button(master=root,text="0",command=b0)
add=tk.Button(master=root,text="+",command=addition)
sub=tk.Button(master=root,text="-",command=subtraction)
multi=tk.Button(master=root,text="*",command=multiplication)
divi=tk.Button(master=root,text="/",command=division)
result=tk.Button(master=root,text="=",command=equal)
point=tk.Button(master=root,text=".",command=deci)
clear=tk.Button(master=root,text="C",command=cl)

#design===============================
label.grid(column=0,row=0,columnspan=3)
b1.grid(column=0,row=1)
b2.grid(column=1,row=1)
b3.grid(column=2,row=1)
b4.grid(column=0,row=2)
b5.grid(column=1,row=2)
b6.grid(column=2,row=2)
b7.grid(column=0,row=3)
b8.grid(column=1,row=3)
b9.grid(column=2,row=3)
b0.grid(column=1,row=4)

add.grid(column=2,row=4)
sub.grid(column=4,row=1)
multi.grid(column=4,row=2)
divi.grid(column=4,row=3)
result.grid(column=0,row=4)
point.grid(column=4,row=4)
clear.grid(column=4,row=0)


root.mainloop()
