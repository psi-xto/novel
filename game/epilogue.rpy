
define v = Character("Виктор Сергеевич", color="#ffc8c8")
define a = Character("Алексей", color="#c8ffc8")
define an = Character("", what_italic=True)
image bg university_hall = "images/bgs/1.1.png"
image bg prologue_door = "images/bgs/1.2.png"

image alex_normal = "images/alex_normal.png"
image viktor = "images/viktor_skeptic.png"

label epilogue:
    
    stop music fadeout 2.0
    scene black
    with fade
    
    show text "{b}Эпилог{/b}" with dissolve
    $ renpy.pause(1.5)
    hide text with dissolve
    
    scene bg prologue_door
    with fade
    
    play sound door
    play music main_menu volume 0.15 fadein 5.0
    
    "Шаги по коридору эхом отдаются в пустоте."
    "Дверь открывается. Тишина."
    
    show viktor at Transform(xalign=1.0, yalign=1.0, zoom=1.05) with dissolve

    
    v "(смотрит на Алексея, не говоря ничего)"
    v "Ты знаешь, почему я тебя сюда направил?"
    
    show alex_normal at Transform(left, ypos=0.04, zoom=1.2) with moveinleft 

    
    "Алексей молчит, не находя слов."
    
    v "Потому что ты — не тот, кто знает, как взломать."
    v "Ты — тот, кто понимает, {b}почему{/b} люди это делают."
    
    if analytical_score >= 6 and practical_score >= 6 and impulsive_score <= 7:
        $ epilogue_type = "ideal"
        
        v "Ты умеешь видеть не только угрозу, но и человека за ней."
        v "В SOC такие аналитики — золото."
        v "Ты нашёл баланс между технологией и человечностью."
        
        a "Спасибо, Виктор Сергеевич. Эти три дня научили меня большему, чем год лекций."
        
    elif practical_score >= 6 and analytical_score <= 4:
        $ epilogue_type = "technician"
        
        v "Ты чётко следуешь процедурам. Это надёжно."
        v "Но иногда стоит заглянуть глубже — за цифры."
        v "За каждой атакой стоит человек. И у каждого человека — своя история."
        
        a "Постараюсь помнить об этом. Правила важны, но контекст — тоже."
        
    elif impulsive_score >= 6:
        $ epilogue_type = "enthusiast"
        
        v "Ты действуешь быстро. Это ценно в кризис."
        v "Но в информационной безопасности главное — не скорость, а точность."
        v "Иногда нужно остановиться. Подумать. И только потом — действовать."
        
        a "Да, я понял... иногда я слишком тороплюсь."
        a "Но когда видишь красный сигнал — сложно не реагировать сразу."
        
    else:
        $ epilogue_type = "newbie"
        
        v "Ты ещё ищешь свой путь."
        v "И это нормально. Главное — ты прошёл через это."
        v "Три дня в реальном SOC. Это больше, чем многие видят за всю учёбу."
        
        a "Это было... интенсивно. Но я многому научился."
        a "Даже если не всё сразу получалось."
    
    v "(достаёт из папки бумажку)"
    v "Стипендия возвращена."
    v "Ты заслужил."
    
    
    "Виктор Сергеевич протягивает официальное уведомление."
    "Алексей берёт его. Смотрит на печать, на подпись."
    
    hide viktor with dissolve
        
    an "The Phantom Data..."
    an "Да уж, подвальчик — далеко не 'Тинькофф'."
    an "Но... если тут майнили крипту на серверах 1С, значит, тут есть что-то настоящее."
    
    scene bg university_hall
    with fade

    "Алексей выходит из кабинета. Коридор кажется длиннее, чем обычно."
    "Он останавливается у знакомой двери в конце коридора."
    
    an "(читает про себя)"
    scene black with fade
    show text "The Phantom Data\nЗаходи, если не боишься" at truecenter with dissolve
    $ renpy.pause(2.0)
    hide text with dissolve
    a "...Ну, пойдём."
    
    scene black
    with fade
    
    stop music fadeout 3.0
    
    
    
    scene black
    with fade
    
    show text "Ваши итоговые показатели:" at truecenter with dissolve
    $ renpy.pause(1.5)
    hide text with dissolve
    
    python:
        total_score = analytical_score + practical_score + impulsive_score
        
        anal_percent = int((analytical_score / max(total_score, 1)) * 100)
        pract_percent = int((practical_score / max(total_score, 1)) * 100)
        impuls_percent = int((impulsive_score / max(total_score, 1)) * 100)
        res = [anal_percent, pract_percent, impuls_percent]
        
        if max(res) == anal_percent and anal_percent >= 50:
            analyst_type = "ИДЕАЛЬНЫЙ АНАЛИТИК"
            description = "Вы балансируете между техникой и человечностью. Видите не только угрозы, но и их причины."
        elif max(res) == pract_percent and pract_percent >= 50:
            analyst_type = "ТЕХНИЧЕСКИЙ СПЕЦИАЛИСТ"
            description = "Процедуры и инструкции — ваша сила. Вы надёжны, но иногда упускаете контекст."
        elif max(res) == impuls_percent and impuls_percent >= 50:
            analyst_type = "РЕАГИРУЮЩИЙ ЭКСПЕРТ"
            description = "Действуете быстро в кризисных ситуациях. Но скорость иногда берёт верх над точностью."
        else:
            analyst_type = "НАБИРАЮЩИЙ ОПЫТ НОВИЧОК"
            description = "Вы в начале пути. Главное — вы прошли через реальные ситуации и научились на них."
    
    scene black
    call screen stats_screen
    
    jump show_credits