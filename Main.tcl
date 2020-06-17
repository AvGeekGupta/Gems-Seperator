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
        -menu "$top.m77" -background #bce8f5 
    wm focusmodel $top passive
    wm geometry $top 1920x1001+-9+-9
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1920 1001
    wm minsize $top 1920 1001
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm title $top "Gems Seperator"
    vTcl:DefineAlias "$top" "Main" vTcl:Toplevel:WidgetProc "" 1
    ttk::separator $top.tSe43 \
        -orient vertical 
    vTcl:DefineAlias "$top.tSe43" "Vertical_Seperator_1" vTcl:WidgetProc "Main" 1
    ttk::separator $top.tSe44
    vTcl:DefineAlias "$top.tSe44" "Horizontal_Seperator_1" vTcl:WidgetProc "Main" 1
    ttk::separator $top.tSe45
    vTcl:DefineAlias "$top.tSe45" "Horizontal_Seperator_2" vTcl:WidgetProc "Main" 1
    ttk::label $top.tLa46 \
        -background #bce8f5 -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft New Tai Lue} -size 40 -weight bold -underline 1} \
        -relief flat -text {Gems Seperator} 
    vTcl:DefineAlias "$top.tLa46" "Heading_Label" vTcl:WidgetProc "Main" 1
    ttk::label $top.tLa47 \
        -background #bce8f5 -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 20 -weight bold -slant italic} \
        -relief flat -text Welcome 
    vTcl:DefineAlias "$top.tLa47" "Welcome_Label" vTcl:WidgetProc "Main" 1
    ttk::label $top.tLa48 \
        -background #bce8f5 -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 20 -weight bold -slant italic} \
        -relief flat -text Name 
    vTcl:DefineAlias "$top.tLa48" "Name_Label" vTcl:WidgetProc "Main" 1
    ttk::label $top.tLa49 \
        -background #bce8f5 -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 20 -underline 1} -relief flat \
        -text {General Options} 
    vTcl:DefineAlias "$top.tLa49" "General_Option_Label" vTcl:WidgetProc "Main" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu50 \
        -takefocus {} -text {Log Out} 
    vTcl:DefineAlias "$top.tBu50" "Log_Out_Button" vTcl:WidgetProc "Main" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu51 \
        -takefocus {} -text {Upload Data} 
    vTcl:DefineAlias "$top.tBu51" "Upload_Data_Button" vTcl:WidgetProc "Main" 1
    ttk::label $top.tLa52 \
        -background #bce8f5 -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 20 -underline 1} -relief flat \
        -text {Engine Controls} 
    vTcl:DefineAlias "$top.tLa52" "Control_Label" vTcl:WidgetProc "Main" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu53 \
        -takefocus {} -text {Train System} 
    vTcl:DefineAlias "$top.tBu53" "Train_Button" vTcl:WidgetProc "Main" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu54 \
        -takefocus {} -text {Start Engine} 
    vTcl:DefineAlias "$top.tBu54" "Start_Button" vTcl:WidgetProc "Main" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu55 \
        -takefocus {} -text {Stop Engine} 
    vTcl:DefineAlias "$top.tBu55" "Stop_Button" vTcl:WidgetProc "Main" 1
    ttk::label $top.tLa56 \
        -background #bce8f5 -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 20 -underline 1} -relief flat \
        -text {Write Data on file} 
    vTcl:DefineAlias "$top.tLa56" "Write_Label" vTcl:WidgetProc "Main" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu58 \
        -takefocus {} -text {Training Data} 
    vTcl:DefineAlias "$top.tBu58" "Training_Data_Button" vTcl:WidgetProc "Main" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu59 \
        -takefocus {} -text {Run Results} 
    vTcl:DefineAlias "$top.tBu59" "Running_Data_Button" vTcl:WidgetProc "Main" 1
    ttk::style configure TFrame -background $vTcl(actual_gui_bg)
    ttk::frame $top.tFr60 \
        -borderwidth 5 -relief raised -width 1125 -height 615 -cursor circle 
    vTcl:DefineAlias "$top.tFr60" "Picture_Frame" vTcl:WidgetProc "Main" 1
    ttk::label $top.tLa61 \
        -background #bce8f5 -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 20 -weight bold -underline 1} \
        -relief flat -text {Current Gems data} 
    vTcl:DefineAlias "$top.tLa61" "Run_Label" vTcl:WidgetProc "Main" 1
    ttk::label $top.tLa62 \
        -background #bce8f5 -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 15} -relief flat \
        -text {Blue Gems :} 
    vTcl:DefineAlias "$top.tLa62" "Blue_Label" vTcl:WidgetProc "Main" 1
    ttk::label $top.tLa63 \
        -background #bce8f5 -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 15} -relief flat \
        -text {Brown Gems :} 
    vTcl:DefineAlias "$top.tLa63" "Brown_Label" vTcl:WidgetProc "Main" 1
    ttk::label $top.tLa64 \
        -background #bce8f5 -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 15} -relief flat \
        -text {Green Gems :} 
    vTcl:DefineAlias "$top.tLa64" "Green_Label" vTcl:WidgetProc "Main" 1
    ttk::label $top.tLa66 \
        -background #bce8f5 -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 15} -relief flat \
        -text {Pink Gems :} 
    vTcl:DefineAlias "$top.tLa66" "Pink_Label" vTcl:WidgetProc "Main" 1
    ttk::label $top.tLa67 \
        -background #bce8f5 -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 15} -relief flat \
        -text {Red Gems :} 
    vTcl:DefineAlias "$top.tLa67" "Red_Label" vTcl:WidgetProc "Main" 1
    ttk::label $top.tLa68 \
        -background #bce8f5 -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 15} -relief flat \
        -text {Yellow Gems :} 
    vTcl:DefineAlias "$top.tLa68" "Yellow_Label" vTcl:WidgetProc "Main" 1
    ttk::label $top.tLa69 \
        -background #bce8f5 -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 15} -relief flat \
        -text {Total Gems :} 
    vTcl:DefineAlias "$top.tLa69" "Total_Label" vTcl:WidgetProc "Main" 1
    ttk::label $top.tLa70 \
        -background #ffffff -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 15} -relief sunken -text 0 
    vTcl:DefineAlias "$top.tLa70" "Blue_Count_Label" vTcl:WidgetProc "Main" 1
    ttk::label $top.tLa71 \
        -background #ffffff -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 15} -relief sunken -text 0 
    vTcl:DefineAlias "$top.tLa71" "Brown_Count_Label" vTcl:WidgetProc "Main" 1
    ttk::label $top.tLa72 \
        -background #ffffff -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 15} -relief sunken -text 0 
    vTcl:DefineAlias "$top.tLa72" "Green_Count_Label" vTcl:WidgetProc "Main" 1
    ttk::label $top.tLa73 \
        -background #ffffff -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 15} -relief sunken -text 0 
    vTcl:DefineAlias "$top.tLa73" "Pink_Count_Label" vTcl:WidgetProc "Main" 1
    ttk::label $top.tLa74 \
        -background #ffffff -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 15} -relief sunken -text 0 
    vTcl:DefineAlias "$top.tLa74" "Red_Count_Label" vTcl:WidgetProc "Main" 1
    ttk::label $top.tLa75 \
        -background #ffffff -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 15} -relief sunken -text 0 
    vTcl:DefineAlias "$top.tLa75" "Yellow_Count_Label" vTcl:WidgetProc "Main" 1
    ttk::label $top.tLa76 \
        -background #ffffff -foreground $vTcl(actual_gui_fg) \
        -font {-family {Microsoft Tai Le} -size 15} -relief sunken -text 0 
    vTcl:DefineAlias "$top.tLa76" "Total_Count_Label" vTcl:WidgetProc "Main" 1
    set site_3_0 $top.m77
    menu $site_3_0 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) \
        -font $vTcl(actual_gui_font_menu_desc) \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    ttk::separator $top.tSe78 \
        -orient vertical 
    vTcl:DefineAlias "$top.tSe78" "TSeparator1" vTcl:WidgetProc "Main" 1
    ttk::separator $top.tSe79 \
        -orient vertical 
    vTcl:DefineAlias "$top.tSe79" "TSeparator2" vTcl:WidgetProc "Main" 1
    ttk::separator $top.tSe80
    vTcl:DefineAlias "$top.tSe80" "TSeparator3" vTcl:WidgetProc "Main" 1
    ttk::separator $top.tSe81
    vTcl:DefineAlias "$top.tSe81" "TSeparator4" vTcl:WidgetProc "Main" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tSe43 \
        -in $top -x 290 -y 140 -height 850 -anchor nw -bordermode inside 
    place $top.tSe44 \
        -in $top -x 10 -y 130 -width 1900 -anchor nw -bordermode inside 
    place $top.tSe45 \
        -in $top -x 300 -y 760 -width 1610 -anchor nw -bordermode inside 
    place $top.tLa46 \
        -in $top -x 710 -y 20 -width 505 -relwidth 0 -height 92 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa47 \
        -in $top -x 10 -y 80 -width 158 -relwidth 0 -height 47 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa48 \
        -in $top -x 170 -y 80 -width 456 -relwidth 0 -height 47 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa49 \
        -in $top -x 30 -y 150 -anchor nw -bordermode ignore 
    place $top.tBu50 \
        -in $top -x 30 -y 220 -width 238 -relwidth 0 -height 60 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tBu51 \
        -in $top -x 30 -y 470 -width 238 -relwidth 0 -height 60 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa52 \
        -in $top -x 30 -y 400 -anchor nw -bordermode ignore 
    place $top.tBu53 \
        -in $top -x 30 -y 310 -width 228 -relwidth 0 -height 60 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tBu54 \
        -in $top -x 30 -y 560 -width 228 -relwidth 0 -height 60 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tBu55 \
        -in $top -x 30 -y 650 -width 228 -relwidth 0 -height 60 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa56 \
        -in $top -x 20 -y 760 -anchor nw -bordermode ignore 
    place $top.tBu58 \
        -in $top -x 30 -y 830 -width 228 -relwidth 0 -height 60 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tBu59 \
        -in $top -x 30 -y 920 -width 228 -relwidth 0 -height 60 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tFr60 \
        -in $top -x 540 -y 140 -width 1125 -relwidth 0 -height 615 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.tLa61 \
        -in $top -x 960 -y 770 -width 294 -relwidth 0 -height 64 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa62 \
        -in $top -x 310 -y 850 -anchor nw -bordermode ignore 
    place $top.tLa63 \
        -in $top -x 310 -y 890 -anchor nw -bordermode ignore 
    place $top.tLa64 \
        -in $top -x 840 -y 850 -anchor nw -bordermode ignore 
    place $top.tLa66 \
        -in $top -x 840 -y 890 -anchor nw -bordermode ignore 
    place $top.tLa67 \
        -in $top -x 1410 -y 850 -anchor nw -bordermode ignore 
    place $top.tLa68 \
        -in $top -x 1410 -y 890 -anchor nw -bordermode ignore 
    place $top.tLa69 \
        -in $top -x 840 -y 950 -anchor nw -bordermode ignore 
    place $top.tLa70 \
        -in $top -x 700 -y 850 -width 97 -relwidth 0 -height 35 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa71 \
        -in $top -x 700 -y 890 -width 97 -relwidth 0 -height 35 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa72 \
        -in $top -x 1280 -y 850 -width 97 -relwidth 0 -height 35 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa73 \
        -in $top -x 1280 -y 890 -width 97 -relwidth 0 -height 35 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa74 \
        -in $top -x 1800 -y 850 -width 97 -relwidth 0 -height 35 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa75 \
        -in $top -x 1800 -y 890 -width 97 -relwidth 0 -height 35 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa76 \
        -in $top -x 1230 -y 950 -width 97 -relwidth 0 -height 35 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tSe78 \
        -in $top -x 1390 -y 840 -height 90 -anchor nw -bordermode inside 
    place $top.tSe79 \
        -in $top -x 810 -y 840 -height 90 -anchor nw -bordermode inside 
    place $top.tSe80 \
        -in $top -x 300 -y 940 -width 1610 -anchor nw -bordermode inside 
    place $top.tSe81 \
        -in $top -x 300 -y 830 -width 1610 -anchor nw -bordermode inside 

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

