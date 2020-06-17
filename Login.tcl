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
set vTcl(active_menu_fg) #000000
}




proc vTclWindow.top42 {base} {
    global vTcl
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -borderwidth 5 -menu "$top.m43" -relief raised -background #bce8f5 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1920x1001+-9+-9
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1920 1000
    wm minsize $top 1920 1001
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm title $top "Gems Seperator - Login"
    vTcl:DefineAlias "$top" "Login_Page" vTcl:Toplevel:WidgetProc "" 1
    set site_3_0 $top.m43
    menu $site_3_0 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    ttk::label $top.tLa45 \
        -background #bce8f5 -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 40 -weight bold -underline 1} \
        -relief flat -text {Gems Seperator} 
    vTcl:DefineAlias "$top.tLa45" "Heading_Label" vTcl:WidgetProc "Login_Page" 1
    vTcl:copy_lock $top.tLa45
    ttk::label $top.tLa46 \
        -background #bce8f5 -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 30 -weight bold -underline 1} \
        -relief flat -text {User Login} 
    vTcl:DefineAlias "$top.tLa46" "User_Login_Label" vTcl:WidgetProc "Login_Page" 1
    vTcl:copy_lock $top.tLa46
    ttk::label $top.tLa47 \
        -background #bce8f5 -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 20} -relief flat \
        -text {Username :} 
    vTcl:DefineAlias "$top.tLa47" "Username_Label" vTcl:WidgetProc "Login_Page" 1
    vTcl:copy_lock $top.tLa47
    ttk::label $top.tLa48 \
        -background #bce8f5 -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 20} -relief flat \
        -text {Password :} 
    vTcl:DefineAlias "$top.tLa48" "Password_Label" vTcl:WidgetProc "Login_Page" 1
    vTcl:copy_lock $top.tLa48
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu49 \
        -takefocus {} -text Login 
    vTcl:DefineAlias "$top.tBu49" "Login_Button" vTcl:WidgetProc "Login_Page" 1
    vTcl:copy_lock $top.tBu49
    text $top.tex50 \
        -background white -font {-family {Microsoft Tai Le} -size 20} \
        -foreground black -height 44 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 404 -wrap word 
    .top42.tex50 configure -font "-family {Microsoft Tai Le} -size 20"
    .top42.tex50 insert end text
    vTcl:DefineAlias "$top.tex50" "Username_Textbox" vTcl:WidgetProc "Login_Page" 1
    vTcl:copy_lock $top.tex50
    text $top.tex51 \
        -background white -font {-family {Microsoft Tai Le} -size 20} \
        -foreground black -height 44 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 404 -wrap word 
    .top42.tex51 configure -font "-family {Microsoft Tai Le} -size 20"
    .top42.tex51 insert end text
    vTcl:DefineAlias "$top.tex51" "Password_Textbox" vTcl:WidgetProc "Login_Page" 1
    vTcl:copy_lock $top.tex51
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tLa45 \
        -in $top -x 700 -y 60 -anchor nw -bordermode ignore 
    place $top.tLa46 \
        -in $top -x 830 -y 280 -anchor nw -bordermode ignore 
    place $top.tLa47 \
        -in $top -x 656 -y 520 -width 166 -height 46 -anchor nw \
        -bordermode ignore 
    place $top.tLa48 \
        -in $top -x 666 -y 620 -width 156 -height 46 -anchor nw \
        -bordermode ignore 
    place $top.tBu49 \
        -in $top -x 840 -y 760 -width 238 -relwidth 0 -height 50 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tex50 \
        -in $top -x 940 -y 520 -width 404 -relwidth 0 -height 44 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tex51 \
        -in $top -x 940 -y 620 -width 404 -relwidth 0 -height 44 -relheight 0 \
        -anchor nw -bordermode ignore 

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
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

