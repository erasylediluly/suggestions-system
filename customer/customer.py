#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Apr 20, 2020 02:49:22 PM +06  platform: Windows NT

import sys
sys.path.insert(1, 'C:\\Users\\Erasyl Ediluly\\Desktop\\4 semester\\Advanced Algorithms\\final project\\main')
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

import customer_support
import main
def vp_start_gui(id,name):
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Customer (id,name,root)
    customer_support.init(root,top)
    root.mainloop()

w = None
# def create_Customer(rt, *args, **kwargs):
#     '''Starting point when module is imported by another module.
#        Correct form of call: 'create_Customer(root, *args, **kwargs)' .'''
#     global w, w_win, root
#     #rt = root
#     root = rt
#     w = tk.Toplevel (root)
#     top = Customer (w)
#     customer_support.init(w, top, *args, **kwargs)
#     return (w, top)

def destroy_Customer():
    global w
    w.destroy()
    w = None
def log_out(root):
    root.destroy()
    main.vp_start_gui()
class Customer:
    def __init__(self,id,name,top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("605x450+359+165")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Customer")
        top.configure(background="#000000")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.0, rely=0.089, relheight=0.911
                , relwidth=0.998)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(0, text="Your orders", compound="left", underline="-1"
                ,)
        self.TNotebook1_t2.configure(background="#808080")
        self.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2.configure(highlightcolor="black")
        self.TNotebook1_t3 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t3, padding=3)
        self.TNotebook1.tab(1, text="Make order", compound="none", underline="-1"
                ,)
        self.TNotebook1_t3.configure(background="#808080")
        self.TNotebook1_t3.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t3.configure(highlightcolor="black")

        self.name_lbl = tk.Label(top)
        self.name_lbl.place(relx=0.0, rely=0.022, height=21, width=185)
        self.name_lbl.configure(activebackground="#f9f9f9")
        self.name_lbl.configure(activeforeground="black")
        self.name_lbl.configure(background="#000000")
        self.name_lbl.configure(disabledforeground="#a3a3a3")
        self.name_lbl.configure(foreground="#ffffff")
        self.name_lbl.configure(highlightbackground="#d9d9d9")
        self.name_lbl.configure(highlightcolor="black")
        self.name_lbl.configure(text=name)

        self.Scrolledlistbox1_search = ScrolledListBox(self.TNotebook1_t2)
        self.Scrolledlistbox1_search.place(relx=0.033, rely=0.495
                , relheight=0.404, relwidth=0.358)
        self.Scrolledlistbox1_search.configure(background="white")
        self.Scrolledlistbox1_search.configure(cursor="xterm")
        self.Scrolledlistbox1_search.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1_search.configure(font="TkFixedFont")
        self.Scrolledlistbox1_search.configure(foreground="black")
        self.Scrolledlistbox1_search.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1_search.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1_search.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1_search.configure(selectforeground="black")

        self.from1_en = tk.Entry(self.TNotebook1_t2)
        self.from1_en.place(relx=0.168, rely=0.13,height=20, relwidth=0.223)
        self.from1_en.configure(background="white")
        self.from1_en.configure(cursor="fleur")
        self.from1_en.configure(disabledforeground="#a3a3a3")
        self.from1_en.configure(font="TkFixedFont")
        self.from1_en.configure(foreground="#000000")
        self.from1_en.configure(highlightbackground="#d9d9d9")
        self.from1_en.configure(highlightcolor="black")
        self.from1_en.configure(insertbackground="black")
        self.from1_en.configure(selectbackground="#c4c4c4")
        self.from1_en.configure(selectforeground="black")

        self.Label3 = tk.Label(self.TNotebook1_t2)
        self.Label3.place(relx=0.033, rely=0.13, height=21, width=64)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''From''')

        self.where1_en = tk.Entry(self.TNotebook1_t2)
        self.where1_en.place(relx=0.167, rely=0.234,height=20, relwidth=0.223)
        self.where1_en.configure(background="white")
        self.where1_en.configure(disabledforeground="#a3a3a3")
        self.where1_en.configure(font="TkFixedFont")
        self.where1_en.configure(foreground="#000000")
        self.where1_en.configure(highlightbackground="#d9d9d9")
        self.where1_en.configure(highlightcolor="black")
        self.where1_en.configure(insertbackground="black")
        self.where1_en.configure(selectbackground="#c4c4c4")
        self.where1_en.configure(selectforeground="black")

        self.Label4 = tk.Label(self.TNotebook1_t2)
        self.Label4.place(relx=0.033, rely=0.234, height=21, width=64)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Where''')

        self.type1_en = tk.Entry(self.TNotebook1_t2)
        self.type1_en.place(relx=0.167, rely=0.339,height=20, relwidth=0.223)
        self.type1_en.configure(background="white")
        self.type1_en.configure(disabledforeground="#a3a3a3")
        self.type1_en.configure(font="TkFixedFont")
        self.type1_en.configure(foreground="#000000")
        self.type1_en.configure(highlightbackground="#d9d9d9")
        self.type1_en.configure(highlightcolor="black")
        self.type1_en.configure(insertbackground="black")
        self.type1_en.configure(selectbackground="#c4c4c4")
        self.type1_en.configure(selectforeground="black")

        self.Label5 = tk.Label(self.TNotebook1_t2)
        self.Label5.place(relx=0.017, rely=0.339, height=31, width=84)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Type of cargo''')

        self.Scrolledlistbox1_result = ScrolledListBox(self.TNotebook1_t2)
        self.Scrolledlistbox1_result.place(relx=0.467, rely=0.078, relheight=0.82
                , relwidth=0.502)
        self.Scrolledlistbox1_result.configure(background="white")
        self.Scrolledlistbox1_result.configure(cursor="xterm")
        self.Scrolledlistbox1_result.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1_result.configure(font="TkFixedFont")
        self.Scrolledlistbox1_result.configure(foreground="black")
        self.Scrolledlistbox1_result.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1_result.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1_result.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1_result.configure(selectforeground="black")

        self.from2_en = tk.Entry(self.TNotebook1_t3)
        self.from2_en.place(relx=0.183, rely=0.104,height=20, relwidth=0.257)
        self.from2_en.configure(background="white")
        self.from2_en.configure(disabledforeground="#a3a3a3")
        self.from2_en.configure(font="TkFixedFont")
        self.from2_en.configure(foreground="#000000")
        self.from2_en.configure(highlightbackground="#d9d9d9")
        self.from2_en.configure(highlightcolor="black")
        self.from2_en.configure(insertbackground="black")
        self.from2_en.configure(selectbackground="#c4c4c4")
        self.from2_en.configure(selectforeground="black")

        self.where2_en = tk.Entry(self.TNotebook1_t3)
        self.where2_en.place(relx=0.183, rely=0.208,height=20, relwidth=0.257)
        self.where2_en.configure(background="white")
        self.where2_en.configure(disabledforeground="#a3a3a3")
        self.where2_en.configure(font="TkFixedFont")
        self.where2_en.configure(foreground="#000000")
        self.where2_en.configure(highlightbackground="#d9d9d9")
        self.where2_en.configure(highlightcolor="black")
        self.where2_en.configure(insertbackground="black")
        self.where2_en.configure(selectbackground="#c4c4c4")
        self.where2_en.configure(selectforeground="black")

        self.type2_en = tk.Entry(self.TNotebook1_t3)
        self.type2_en.place(relx=0.183, rely=0.313,height=20, relwidth=0.257)
        self.type2_en.configure(background="white")
        self.type2_en.configure(disabledforeground="#a3a3a3")
        self.type2_en.configure(font="TkFixedFont")
        self.type2_en.configure(foreground="#000000")
        self.type2_en.configure(highlightbackground="#d9d9d9")
        self.type2_en.configure(highlightcolor="black")
        self.type2_en.configure(insertbackground="black")
        self.type2_en.configure(selectbackground="#c4c4c4")
        self.type2_en.configure(selectforeground="black")

        self.Label6 = tk.Label(self.TNotebook1_t3)
        self.Label6.place(relx=0.033, rely=0.104, height=21, width=74)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''From''')

        self.Label7 = tk.Label(self.TNotebook1_t3)
        self.Label7.place(relx=0.033, rely=0.208, height=21, width=74)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Where''')

        self.Label8 = tk.Label(self.TNotebook1_t3)
        self.Label8.place(relx=0.017, rely=0.313, height=21, width=94)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''Type of cargo''')

        self.Scrolledlistbox2_search = ScrolledListBox(self.TNotebook1_t3)
        self.Scrolledlistbox2_search.place(relx=0.5, rely=0.052, relheight=0.846
                , relwidth=0.452)
        self.Scrolledlistbox2_search.configure(background="white")
        self.Scrolledlistbox2_search.configure(cursor="xterm")
        self.Scrolledlistbox2_search.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox2_search.configure(font="TkFixedFont")
        self.Scrolledlistbox2_search.configure(foreground="black")
        self.Scrolledlistbox2_search.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox2_search.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox2_search.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox2_search.configure(selectforeground="black")

        self.Make_btn = tk.Button(self.TNotebook1_t3)
        self.Make_btn.place(relx=0.067, rely=0.599, height=64, width=187)
        self.Make_btn.configure(activebackground="#ececec")
        self.Make_btn.configure(activeforeground="#000000")
        self.Make_btn.configure(background="#d9d9d9")
        self.Make_btn.configure(disabledforeground="#a3a3a3")
        self.Make_btn.configure(foreground="#000000")
        self.Make_btn.configure(highlightbackground="#d9d9d9")
        self.Make_btn.configure(highlightcolor="black")
        self.Make_btn.configure(pady="0")
        self.Make_btn.configure(text='''Make an order''')

        self.log_out_cus = tk.Button(top)
        self.log_out_cus.place(relx=0.826, rely=0.022, height=24, width=52)
        self.log_out_cus.configure(activebackground="#ececec")
        self.log_out_cus.configure(activeforeground="#000000")
        self.log_out_cus.configure(background="#000000")
        self.log_out_cus.configure(disabledforeground="#a3a3a3")
        self.log_out_cus.configure(foreground="#ffffff")
        self.log_out_cus.configure(highlightbackground="#d9d9d9")
        self.log_out_cus.configure(highlightcolor="black")
        self.log_out_cus.configure(pady="0")
        self.log_out_cus.configure(text='''Log out''')
        self.log_out_cus.configure(command = lambda: log_out(top))

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.367, rely=0.022, height=21, width=145)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#000000")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Customer mode''')

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def size_(self):
        sz = tk.Listbox.size(self)
        return sz

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

# if __name__ == '__main__':
#     vp_start_gui()





