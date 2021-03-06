#############################################################################
# Generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#  Apr 20, 2020 02:53:25 PM +06  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) firebrick
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top43 {base} {
    global vTcl
    if {$base == ""} {
        set base .top43
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m53" -background #000000 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 605x450+383+171
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1370 749
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Employee"
    vTcl:DefineAlias "$top" "Employee" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    ttk::style configure TNotebook -background $vTcl(actual_gui_bg)
    ttk::style configure TNotebook.Tab -background $vTcl(actual_gui_bg)
    ttk::style configure TNotebook.Tab -foreground $vTcl(actual_gui_fg)
    ttk::style configure TNotebook.Tab -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TNotebook.Tab -background [list disabled $vTcl(actual_gui_bg) selected $vTcl(pr,guicomplement_color)]
    ttk::notebook $top.tNo52 \
        -width 604 -height 410 -takefocus {} 
    vTcl:DefineAlias "$top.tNo52" "TNotebook1" vTcl:WidgetProc "Employee" 1
    frame $top.tNo52.t1 \
        -background #808080 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black 
    vTcl:DefineAlias "$top.tNo52.t1" "TNotebook1_t2_1" vTcl:WidgetProc "Employee" 1
    $top.tNo52 add $top.tNo52.t1 \
        -padding 0 -sticky nsew -state normal -text {Taken orders} -image {} \
        -compound left -underline -1 
    set site_4_0  $top.tNo52.t1
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $site_4_0.scr60 \
        -background $vTcl(actual_gui_bg) -height 75 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 125 
    vTcl:DefineAlias "$site_4_0.scr60" "Scrolledlistbox1_search" vTcl:WidgetProc "Employee" 1

    $site_4_0.scr60.01 configure -background white \
        -cursor xterm \
        -disabledforeground #a3a3a3 \
        -font TkFixedFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10
    entry $site_4_0.ent67 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 134 
    vTcl:DefineAlias "$site_4_0.ent67" "from1_en" vTcl:WidgetProc "Employee" 1
    label $site_4_0.lab68 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text From 
    vTcl:DefineAlias "$site_4_0.lab68" "Label3_2" vTcl:WidgetProc "Employee" 1
    entry $site_4_0.ent69 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 134 
    vTcl:DefineAlias "$site_4_0.ent69" "where1_en" vTcl:WidgetProc "Employee" 1
    label $site_4_0.lab70 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Where 
    vTcl:DefineAlias "$site_4_0.lab70" "Label4_3" vTcl:WidgetProc "Employee" 1
    entry $site_4_0.ent71 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 134 
    vTcl:DefineAlias "$site_4_0.ent71" "type1_en" vTcl:WidgetProc "Employee" 1
    label $site_4_0.lab72 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Type of cargo} 
    vTcl:DefineAlias "$site_4_0.lab72" "Label5_4" vTcl:WidgetProc "Employee" 1
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $site_4_0.scr82 \
        -background $vTcl(actual_gui_bg) -height 75 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 125 
    vTcl:DefineAlias "$site_4_0.scr82" "Scrolledlistbox1_result" vTcl:WidgetProc "Employee" 1

    $site_4_0.scr82.01 configure -background white \
        -cursor xterm \
        -disabledforeground #a3a3a3 \
        -font TkFixedFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10
    place $site_4_0.scr60 \
        -in $site_4_0 -x 0 -relx 0.033 -y 0 -rely 0.495 -width 0 \
        -relwidth 0.358 -height 0 -relheight 0.404 -anchor nw \
        -bordermode ignore 
    place $site_4_0.ent67 \
        -in $site_4_0 -x 0 -relx 0.168 -y 0 -rely 0.13 -width 134 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.lab68 \
        -in $site_4_0 -x 0 -relx 0.033 -y 0 -rely 0.13 -width 0 \
        -relwidth 0.107 -height 0 -relheight 0.055 -anchor nw \
        -bordermode ignore 
    place $site_4_0.ent69 \
        -in $site_4_0 -x 0 -relx 0.167 -y 0 -rely 0.234 -width 134 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.lab70 \
        -in $site_4_0 -x 0 -relx 0.033 -y 0 -rely 0.234 -width 0 \
        -relwidth 0.107 -height 0 -relheight 0.055 -anchor nw \
        -bordermode ignore 
    place $site_4_0.ent71 \
        -in $site_4_0 -x 0 -relx 0.167 -y 0 -rely 0.339 -width 134 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.lab72 \
        -in $site_4_0 -x 0 -relx 0.017 -y 0 -rely 0.339 -width 0 \
        -relwidth 0.14 -height 0 -relheight 0.081 -anchor nw \
        -bordermode ignore 
    place $site_4_0.scr82 \
        -in $site_4_0 -x 0 -relx 0.467 -y 0 -rely 0.078 -width 0 \
        -relwidth 0.502 -height 0 -relheight 0.82 -anchor nw \
        -bordermode ignore 
    frame $top.tNo52.t2 \
        -background #808080 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black 
    vTcl:DefineAlias "$top.tNo52.t2" "TNotebook1_t3_5" vTcl:WidgetProc "Employee" 1
    $top.tNo52 add $top.tNo52.t2 \
        -padding 0 -sticky nsew -state normal -text Orders -image {} \
        -compound none -underline -1 
    set site_4_1  $top.tNo52.t2
    entry $site_4_1.ent74 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 154 
    vTcl:DefineAlias "$site_4_1.ent74" "from2_en" vTcl:WidgetProc "Employee" 1
    entry $site_4_1.ent75 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 154 
    vTcl:DefineAlias "$site_4_1.ent75" "where2_en" vTcl:WidgetProc "Employee" 1
    entry $site_4_1.ent76 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 154 
    vTcl:DefineAlias "$site_4_1.ent76" "type2_en" vTcl:WidgetProc "Employee" 1
    label $site_4_1.lab77 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text From 
    vTcl:DefineAlias "$site_4_1.lab77" "Label6" vTcl:WidgetProc "Employee" 1
    label $site_4_1.lab78 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Where 
    vTcl:DefineAlias "$site_4_1.lab78" "Label7" vTcl:WidgetProc "Employee" 1
    label $site_4_1.lab79 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Type of cargo} 
    vTcl:DefineAlias "$site_4_1.lab79" "Label8" vTcl:WidgetProc "Employee" 1
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $site_4_1.scr80 \
        -background $vTcl(actual_gui_bg) -height 75 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 125 
    vTcl:DefineAlias "$site_4_1.scr80" "Scrolledlistbox2_search" vTcl:WidgetProc "Employee" 1

    $site_4_1.scr80.01 configure -background white \
        -cursor xterm \
        -disabledforeground #a3a3a3 \
        -font TkFixedFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $site_4_1.scr81 \
        -background $vTcl(actual_gui_bg) -height 75 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 125 
    vTcl:DefineAlias "$site_4_1.scr81" "Scrolledlistbox2_result" vTcl:WidgetProc "Employee" 1

    $site_4_1.scr81.01 configure -background white \
        -cursor xterm \
        -disabledforeground #a3a3a3 \
        -font TkFixedFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10
    place $site_4_1.ent74 \
        -in $site_4_1 -x 0 -relx 0.167 -y 0 -rely 0.104 -width 154 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_1.ent75 \
        -in $site_4_1 -x 0 -relx 0.183 -y 0 -rely 0.208 -width 154 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_1.ent76 \
        -in $site_4_1 -x 0 -relx 0.183 -y 0 -rely 0.313 -width 154 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_1.lab77 \
        -in $site_4_1 -x 0 -relx 0.033 -y 0 -rely 0.104 -width 0 \
        -relwidth 0.123 -height 0 -relheight 0.055 -anchor nw \
        -bordermode ignore 
    place $site_4_1.lab78 \
        -in $site_4_1 -x 0 -relx 0.033 -y 0 -rely 0.208 -width 0 \
        -relwidth 0.123 -height 0 -relheight 0.055 -anchor nw \
        -bordermode ignore 
    place $site_4_1.lab79 \
        -in $site_4_1 -x 0 -relx 0.017 -y 0 -rely 0.313 -width 0 \
        -relwidth 0.157 -height 0 -relheight 0.055 -anchor nw \
        -bordermode ignore 
    place $site_4_1.scr80 \
        -in $site_4_1 -x 0 -relx 0.03 -y 0 -rely 0.417 -width 0 \
        -relwidth 0.418 -height 0 -relheight 0.482 -anchor nw \
        -bordermode ignore 
    place $site_4_1.scr81 \
        -in $site_4_1 -x 0 -relx 0.5 -y 0 -rely 0.052 -width 0 \
        -relwidth 0.452 -height 0 -relheight 0.846 -anchor nw \
        -bordermode ignore 
    set site_3_0 $top.m53
    menu $site_3_0 \
        -activebackground SystemHighlight \
        -activeforeground SystemHighlightText -background #000000 \
        -font TkDefaultFont -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    label $top.lab54 \
        -activebackground #f9f9f9 -activeforeground black -background #000000 \
        -disabledforeground #a3a3a3 -font TkDefaultFont -foreground #ffffff \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Name and surname} 
    vTcl:DefineAlias "$top.lab54" "name_lbl" vTcl:WidgetProc "Employee" 1
    button $top.but55 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #000000 -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground #ffffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -pady 0 -text {Log out} 
    vTcl:DefineAlias "$top.but55" "log_out_btn" vTcl:WidgetProc "Employee" 1
    label $top.lab56 \
        -activebackground #f9f9f9 -activeforeground black -background #000000 \
        -disabledforeground #a3a3a3 -font TkDefaultFont -foreground #ffffff \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Employee mode} 
    vTcl:DefineAlias "$top.lab56" "Label2" vTcl:WidgetProc "Employee" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tNo52 \
        -in $top -x 0 -y 0 -rely 0.089 -width 0 -relwidth 0.998 -height 0 \
        -relheight 0.911 -anchor nw -bordermode ignore 
    place $top.lab54 \
        -in $top -x 0 -y 0 -rely 0.022 -width 0 -relwidth 0.24 -height 0 \
        -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.but55 \
        -in $top -x 0 -relx 0.817 -y 0 -rely 0.022 -anchor nw \
        -bordermode ignore 
    place $top.lab56 \
        -in $top -x 0 -relx 0.367 -y 0 -rely 0.022 -width 0 -relwidth 0.24 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top43 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

