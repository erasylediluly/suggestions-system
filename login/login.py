#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Apr 20, 2020 02:39:13 PM +06  platform: Windows NT

import sys
sys.path.insert(1, 'C:\\Users\\Erasyl Ediluly\\Desktop\\4 semester\\Advanced Algorithms\\final project\\main')
sys.path.insert(1, 'C:\\Users\\Erasyl Ediluly\\Desktop\\4 semester\\Advanced Algorithms\\final project\\customer')
sys.path.insert(1, 'C:\\Users\\Erasyl Ediluly\\Desktop\\4 semester\\Advanced Algorithms\\final project\\employee')
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from tkinter import messagebox
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
from tkinter import *
import login_support
import main
import customer
import employee
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    login_support.set_Tk_var()
    top = Login (root)
    login_support.init(root, top)
    root.mainloop()

w = None
def create_Login(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Login(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    login_support.set_Tk_var()
    top = Login (w)
    login_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Login():
    global w
    w.destroy()
    w = None

class Login:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        option = IntVar()
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+373+180")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Login")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.017, rely=0.022, relheight=0.956
                , relwidth=0.958)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.313, rely=0.047, height=70, width=214)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {MS Sans Serif} -size 15")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Login''')

        self.Number_en = tk.Entry(self.Frame1)
        self.Number_en.place(relx=0.452, rely=0.395,height=30, relwidth=0.39)
        self.Number_en.configure(background="white")
        self.Number_en.configure(cursor="fleur")
        self.Number_en.configure(disabledforeground="#a3a3a3")
        self.Number_en.configure(font="TkFixedFont")
        self.Number_en.configure(foreground="#000000")
        self.Number_en.configure(highlightbackground="#d9d9d9")
        self.Number_en.configure(highlightcolor="black")
        self.Number_en.configure(insertbackground="black")
        self.Number_en.configure(selectbackground="#c4c4c4")
        self.Number_en.configure(selectforeground="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.139, rely=0.372, height=40, width=104)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Mobile number''')

        self.Customer_rb = tk.Radiobutton(self.Frame1)
        self.Customer_rb.place(relx=0.47, rely=0.233, relheight=0.058
                , relwidth=0.153)
        self.Customer_rb.configure(activebackground="#ececec")
        self.Customer_rb.configure(activeforeground="#000000")
        self.Customer_rb.configure(background="#d9d9d9")
        self.Customer_rb.configure(disabledforeground="#a3a3a3")
        self.Customer_rb.configure(foreground="#000000")
        self.Customer_rb.configure(highlightbackground="#d9d9d9")
        self.Customer_rb.configure(highlightcolor="black")
        self.Customer_rb.configure(justify='left')
        self.Customer_rb.configure(text='''Customer''')
        self.Customer_rb.configure(variable=option)
        self.Customer_rb.configure(value=0)
        self.Customer_rb.configure(command = lambda:c(self,top))

        self.Employee_rb = tk.Radiobutton(self.Frame1)
        self.Employee_rb.place(relx=0.661, rely=0.233, relheight=0.07
                , relwidth=0.153)
        self.Employee_rb.configure(activebackground="#ececec")
        self.Employee_rb.configure(activeforeground="#000000")
        self.Employee_rb.configure(background="#d9d9d9")
        self.Employee_rb.configure(disabledforeground="#a3a3a3")
        self.Employee_rb.configure(foreground="#000000")
        self.Employee_rb.configure(highlightbackground="#d9d9d9")
        self.Employee_rb.configure(highlightcolor="black")
        self.Employee_rb.configure(justify='left')
        self.Employee_rb.configure(text='''Employee''')
        self.Employee_rb.configure(variable=option)
        self.Employee_rb.configure(value=1)
        self.Employee_rb.configure(command = lambda:e(self,top))

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.122, rely=0.209, height=40, width=94)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Login as''')

        self.Password_en = tk.Entry(self.Frame1)
        self.Password_en.place(relx=0.452, rely=0.512,height=30, relwidth=0.39)
        self.Password_en.configure(background="white")
        self.Password_en.configure(disabledforeground="#a3a3a3")
        self.Password_en.configure(font="TkFixedFont")
        self.Password_en.configure(foreground="#000000")
        self.Password_en.configure(highlightbackground="#d9d9d9")
        self.Password_en.configure(highlightcolor="black")
        self.Password_en.configure(insertbackground="black")
        self.Password_en.configure(selectbackground="#c4c4c4")
        self.Password_en.configure(selectforeground="black")

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.157, rely=0.488, height=50, width=84)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Password''')

        self.Enter_login = tk.Button(self.Frame1)
        self.Enter_login.place(relx=0.4, rely=0.698, height=50, width=127)
        self.Enter_login.configure(activebackground="#ececec")
        self.Enter_login.configure(activeforeground="#000000")
        self.Enter_login.configure(background="#d9d9d9")
        self.Enter_login.configure(disabledforeground="#a3a3a3")
        self.Enter_login.configure(foreground="#000000")
        self.Enter_login.configure(highlightbackground="#d9d9d9")
        self.Enter_login.configure(highlightcolor="black")
        self.Enter_login.configure(pady="0")
        self.Enter_login.configure(text='''Enter''')

        self.Back_login = tk.Button(self.Frame1)
        self.Back_login.place(relx=0.052, rely=0.023, height=24, width=36)
        self.Back_login.configure(activebackground="#ececec")
        self.Back_login.configure(activeforeground="#000000")
        self.Back_login.configure(background="#d9d9d9")
        self.Back_login.configure(disabledforeground="#a3a3a3")
        self.Back_login.configure(foreground="#000000")
        self.Back_login.configure(highlightbackground="#d9d9d9")
        self.Back_login.configure(highlightcolor="black")
        self.Back_login.configure(pady="0")
        self.Back_login.configure(text='''Back''')
        self.Back_login.configure(command = lambda: back(top))
def back(self):
    self.destroy()
    main.vp_start_gui()
def login_as_customer(top,self):
    con = get_connection()
    cursor = con.cursor()
    cursor.execute("""SELECT password FROM customer WHERE customer_id = ?""",[(self.Number_en.get())])
    num = self.Number_en.get()
    l = cursor.fetchall()
    if(len(l) != 0):
        password = l[0][0]
        if(self.Password_en.get() == password):
            cursor.execute("""SELECT name || ' ' || surname FROM customer WHERE customer_id = ?""",[(self.Number_en.get())])
            l = cursor.fetchall()
            top.destroy()
            customer.vp_start_gui(num,l[0][0])
        else:
            messagebox.showerror("Error", "Incorrect password or login")
    else:
        messagebox.showerror("Error", "Incorrect password or login")
    con.commit()
def login_as_employee(top,self):
    con = get_connection()
    cursor = con.cursor()
    cursor.execute("""SELECT password FROM employee WHERE employee_id = ?""",[(self.Number_en.get())])
    l = cursor.fetchall()
    num = self.Number_en.get()
    if(len(l) != 0):
        password = l[0][0]
        if(self.Password_en.get() == password):
            cursor.execute("""SELECT name || ' ' || surname FROM employee WHERE employee_id = ?""",[(self.Number_en.get())])
            l = cursor.fetchall()
            top.destroy()
            employee.vp_start_gui(num,l[0][0])
        else:
            messagebox.showerror("Error", "Incorrect password or login")
    else:
        messagebox.showerror("Error", "Incorrect password or login")
    con.commit()
def c(self,top):
    self.Enter_login.configure(command = lambda: login_as_customer(top,self))
def e(self,top):
    self.Enter_login.configure(command = lambda: login_as_employee(top,self))
import sqlite3
def get_connection():
    con = sqlite3.connect('C:\\Users\\Erasyl Ediluly\\Desktop\\4 semester\\Advanced Algorithms\\final project\\database\\database.db')
    return con
if __name__ == '__main__':
    vp_start_gui()





