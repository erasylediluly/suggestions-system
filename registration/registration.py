#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Apr 20, 2020 02:44:00 PM +06  platform: Windows NT

import sys
sys.path.insert(1, 'C:\\Users\\Erasyl Ediluly\\Desktop\\4 semester\\Advanced Algorithms\\final project\\main')
import main
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
from tkinter import *
import registration_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    registration_support.set_Tk_var()
    top = Registration (root)
    registration_support.init(root, top)
    root.mainloop()

w = None
def create_Registration(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Registration(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    registration_support.set_Tk_var()
    top = Registration (w)
    registration_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Registration():
    global w
    w.destroy()
    w = None

class Registration:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        option = IntVar()
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+374+150")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Registration")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.017, rely=0.022, relheight=0.967
                , relwidth=0.975)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.name_en = tk.Entry(self.Frame1)
        self.name_en.place(relx=0.349, rely=0.234,height=25, relwidth=0.417)
        self.name_en.configure(background="white")
        self.name_en.configure(disabledforeground="#a3a3a3")
        self.name_en.configure(font="TkFixedFont")
        self.name_en.configure(foreground="#000000")
        self.name_en.configure(highlightbackground="#d9d9d9")
        self.name_en.configure(highlightcolor="black")
        self.name_en.configure(insertbackground="black")
        self.name_en.configure(selectbackground="#c4c4c4")
        self.name_en.configure(selectforeground="black")

        self.surname_en = tk.Entry(self.Frame1)
        self.surname_en.place(relx=0.342, rely=0.345,height=30, relwidth=0.417)
        self.surname_en.configure(background="white")
        self.surname_en.configure(disabledforeground="#a3a3a3")
        self.surname_en.configure(font="TkFixedFont")
        self.surname_en.configure(foreground="#000000")
        self.surname_en.configure(highlightbackground="#d9d9d9")
        self.surname_en.configure(highlightcolor="black")
        self.surname_en.configure(insertbackground="black")
        self.surname_en.configure(selectbackground="#c4c4c4")
        self.surname_en.configure(selectforeground="black")

        self.number_en = tk.Entry(self.Frame1)
        self.number_en.place(relx=0.342, rely=0.483,height=25, relwidth=0.417)
        self.number_en.configure(background="white")
        self.number_en.configure(disabledforeground="#a3a3a3")
        self.number_en.configure(font="TkFixedFont")
        self.number_en.configure(foreground="#000000")
        self.number_en.configure(highlightbackground="#d9d9d9")
        self.number_en.configure(highlightcolor="black")
        self.number_en.configure(insertbackground="black")
        self.number_en.configure(selectbackground="#c4c4c4")
        self.number_en.configure(selectforeground="black")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.07, rely=0.211, height=46, width=136)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Name''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.104, rely=0.354, height=21, width=85)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Surname''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.104, rely=0.471, height=36, width=106)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Mobile  number''')

        self.password_en = tk.Entry(self.Frame1)
        self.password_en.place(relx=0.342, rely=0.598, height=25, relwidth=0.417)

        self.password_en.configure(background="white")
        self.password_en.configure(disabledforeground="#a3a3a3")
        self.password_en.configure(font="TkFixedFont")
        self.password_en.configure(foreground="#000000")
        self.password_en.configure(highlightbackground="#d9d9d9")
        self.password_en.configure(highlightcolor="black")
        self.password_en.configure(insertbackground="black")
        self.password_en.configure(selectbackground="#c4c4c4")
        self.password_en.configure(selectforeground="black")

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.138, rely=0.589, height=35, width=55)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Password''')

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.291, rely=0.046, height=48, width=218)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {MS Sans Serif} -size 15")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Registration''')

        self.customer_rb = tk.Radiobutton(self.Frame1)
        self.customer_rb.place(relx=0.376, rely=0.69, relheight=0.103
                , relwidth=0.168)
        self.customer_rb.configure(activebackground="#ececec")
        self.customer_rb.configure(activeforeground="#000000")
        self.customer_rb.configure(background="#d9d9d9")
        self.customer_rb.configure(disabledforeground="#a3a3a3")
        self.customer_rb.configure(foreground="#000000")
        self.customer_rb.configure(highlightbackground="#d9d9d9")
        self.customer_rb.configure(highlightcolor="black")
        self.customer_rb.configure(justify='left')
        self.customer_rb.configure(text='''customer''')
        self.customer_rb.configure(variable=option)
        self.customer_rb.configure(value = 0)
        self.customer_rb.configure(command = lambda: self.Enter_regis.configure(command = lambda: register_cus(self,top)))

        self.employee_en = tk.Radiobutton(self.Frame1)
        self.employee_en.place(relx=0.547, rely=0.701, relheight=0.08
                , relwidth=0.15)
        self.employee_en.configure(activebackground="#ececec")
        self.employee_en.configure(activeforeground="#000000")
        self.employee_en.configure(background="#d9d9d9")
        self.employee_en.configure(disabledforeground="#a3a3a3")
        self.employee_en.configure(foreground="#000000")
        self.employee_en.configure(highlightbackground="#d9d9d9")
        self.employee_en.configure(highlightcolor="black")
        self.employee_en.configure(justify='left')
        self.employee_en.configure(text='''employee''')
        self.employee_en.configure(variable=option)
        self.employee_en.configure(command = lambda: self.Enter_regis.configure(command = lambda: register_emp(self,top)))
        self.employee_en.configure(value = 1)
        
        self.Enter_regis = tk.Button(self.Frame1)
        self.Enter_regis.place(relx=0.393, rely=0.828, height=45, width=117)
        self.Enter_regis.configure(activebackground="#ececec")
        self.Enter_regis.configure(activeforeground="#000000")
        self.Enter_regis.configure(background="#d9d9d9")
        self.Enter_regis.configure(disabledforeground="#a3a3a3")
        self.Enter_regis.configure(foreground="#000000")
        self.Enter_regis.configure(highlightbackground="#d9d9d9")
        self.Enter_regis.configure(highlightcolor="black")
        self.Enter_regis.configure(pady="0")
        self.Enter_regis.configure(text='''Enter''')

        self.Back_regis = tk.Button(self.Frame1)
        self.Back_regis.place(relx=0.034, rely=0.023, height=35, width=87)
        self.Back_regis.configure(activebackground="#ececec")
        self.Back_regis.configure(activeforeground="#000000")
        self.Back_regis.configure(background="#d9d9d9")
        self.Back_regis.configure(disabledforeground="#a3a3a3")
        self.Back_regis.configure(foreground="#000000")
        self.Back_regis.configure(highlightbackground="#d9d9d9")
        self.Back_regis.configure(highlightcolor="black")
        self.Back_regis.configure(pady="0")
        self.Back_regis.configure(text='''<Back''')
        self.Back_regis.configure(command = lambda: back(top))
def back(top):
    top.destroy()
    main.vp_start_gui()
import sqlite3
def get_connection():
    con = sqlite3.connect('C:\\Users\\Erasyl Ediluly\\Desktop\\4 semester\\Advanced Algorithms\\final project\\database\\database.db')
    return con
def register_cus(self,top):
    con = get_connection()
    cursor = con.cursor()
    cursor.execute("""INSERT INTO customer VALUES(?,?,?,?)""",[(self.number_en.get()),(self.name_en.get()),(self.surname_en.get()),(self.password_en.get())])
    con.commit()
    top.destroy()
    main.vp_start_gui()
def register_emp(self,top):
    con = get_connection()
    cursor = con.cursor()
    cursor.execute("""INSERT INTO employee VALUES(?,?,?,?)""",[(self.number_en.get()),(self.name_en.get()),(self.surname_en.get()),(self.password_en.get())])
    con.commit()
    top.destroy()
    main.vp_start_gui()
if __name__ == '__main__':
    vp_start_gui()





