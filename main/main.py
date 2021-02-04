
import sys
sys.path.insert(1, 'C:\\Users\\Erasyl Ediluly\\Desktop\\4 semester\\Advanced Algorithms\\final project\\login')
sys.path.insert(1, 'C:\\Users\\Erasyl Ediluly\\Desktop\\4 semester\\Advanced Algorithms\\final project\\registration')
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

import main_support
import login
import registration
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Main_Page (root)
    main_support.init(root, top)
    root.mainloop()

w = None
def create_Main_Page(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Main_Page(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Main_Page (w)
    main_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Main_Page():
    global w
    w.destroy()
    w = None
def register(self):
    self.destroy()
    registration.vp_start_gui()
def log_in(self):
    self.destroy()
    login.vp_start_gui()
class Main_Page:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {MS Sans Serif} -size 15"

        top.geometry("600x450+342+125")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Main Page")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.017, rely=0.022, relheight=0.944
                , relwidth=0.958)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#004040")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="#646464646464")

        self.LoginBtn = tk.Button(self.Frame1)
        self.LoginBtn.place(relx=0.157, rely=0.588, height=54, width=127)
        self.LoginBtn.configure(activebackground="#ececec")
        self.LoginBtn.configure(activeforeground="#000000")
        self.LoginBtn.configure(background="#ffffff")
        self.LoginBtn.configure(disabledforeground="#a3a3a3")
        self.LoginBtn.configure(font="-family {MS Sans Serif} -size 15")
        self.LoginBtn.configure(foreground="#000000")
        self.LoginBtn.configure(highlightbackground="#d9d9d9")
        self.LoginBtn.configure(highlightcolor="black")
        self.LoginBtn.configure(pady="0")
        self.LoginBtn.configure(text='''Login''')
        self.LoginBtn.configure(command = lambda:log_in(top))

        self.Label = tk.Label(self.Frame1)
        self.Label.place(relx=0.243, rely=0.094, height=141, width=284)
        self.Label.configure(activebackground="#f9f9f9")
        self.Label.configure(activeforeground="black")
        self.Label.configure(background="#004040")
        self.Label.configure(disabledforeground="#a3a3a3")
        self.Label.configure(font="-family {MS Sans Serif} -size 19")
        self.Label.configure(foreground="#ffffff")
        self.Label.configure(highlightbackground="#d9d9d9")
        self.Label.configure(highlightcolor="black")
        self.Label.configure(text='''Logistics company''')

        self.SignUpBtn = tk.Button(self.Frame1)
        self.SignUpBtn.place(relx=0.626, rely=0.588, height=54, width=127)
        self.SignUpBtn.configure(activebackground="#ececec")
        self.SignUpBtn.configure(activeforeground="#000000")
        self.SignUpBtn.configure(background="#ffffff")
        self.SignUpBtn.configure(disabledforeground="#a3a3a3")
        self.SignUpBtn.configure(font=font9)
        self.SignUpBtn.configure(foreground="#000000")
        self.SignUpBtn.configure(highlightbackground="#d9d9d9")
        self.SignUpBtn.configure(highlightcolor="black")
        self.SignUpBtn.configure(pady="0")
        self.SignUpBtn.configure(text='''Sign_up''')
        self.SignUpBtn.configure(command = lambda:register(top))
if __name__ == '__main__':
    vp_start_gui()