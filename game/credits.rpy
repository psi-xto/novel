label show_credits:
    scene black
    with fade
    
    stop music fadeout 3.0
    stop sound fadeout 3.0
    
    $ renpy.pause(1.0)
    
    show text "The Phantom Data" at truecenter with dissolve
    $ renpy.pause(2.0)
    hide text with dissolve
    
    play music main_menu volume 0.2 fadein 2.0
    
    call screen credits_screen
    
    show text "УрФУ, 2025" at truecenter with dissolve
    $ renpy.pause(1.0)
    hide text with dissolve
    
    stop music fadeout 2.0
    scene black
    with fade
    
    return

screen credits_screen():
    zorder 1000
    modal True
    
    textbutton "Пропустить титры" xalign 0.5 yalign 0.95:
        background "#333333"
        hover_background "#555555"
        text_color "#ffffff"
        action Return()
    
    add Solid("#0a0a1a")
    
    frame:
        xalign 0.5
        yalign 0.0
        xsize 800
        ysize 1080
        background None
        
        at transform:
            linear 15.0 yalign 1.0
            
        vbox:
            xalign 0.5
            ypos 200
            spacing 40
            
            text "Над игрой работали:" size 36 color "#4cc9f0" xalign 0.5
                        
            vbox:
                xalign 0.5
                
                text "Тимлид:" size 24 color "#ffffff" xalign 0.5
                text "Константинов Г. А." size 28 color "#4361ee" xalign 0.5
                                
                text "Разработчик:" size 24 color "#ffffff" xalign 0.5
                text "Павленко П. С." size 28 color "#4cc9f0" xalign 0.5
                
                
                text "Гейм-дизайнер:" size 24 color "#ffffff" xalign 0.5
                text "Кондрыкинский Г. В." size 28 color "#f72585" xalign 0.5
                
                
                text "Аналитик:" size 24 color "#ffffff" xalign 0.5
                text "Морозов А. И." size 28 color "#ff9e00" xalign 0.5
                
                
                text "Дизайнер:" size 24 color "#ffffff" xalign 0.5
                text "Вотинова М. А." size 28 color "#7209b7" xalign 0.5
            
            null height 20
            
            text "Спасибо за игру!" size 30 color "#00ff88" xalign 0.5
            text "Надеемся, вам понравилось погружение \n в мир информационной безопасности" size 22 color "#ffffff" xalign 0.5
    
    timer 10.0 action Return()