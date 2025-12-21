define a = Character("Алексей", color="#c8ffc8")
define v = Character("Виктор Сергеевич", color="#c8c8ff")
define inner = Character("", kind=nvl, what_italic=True)

image bg university_hall = "images/bgs/1.1.png"
image bg prologue_door = "images/bgs/1.2.png"

image alex_normal = "images/alex_normal.png"
image alex_notebook = "images/alex_nb.png"
image alex_wow = "images/alex_wow.png"
image viktor_normal = "images/viktor_normal.png"
image viktor_sad = "images/viktor_sad.png"
image viktor_skeptic = "images/viktor_skeptic.png"
image max_1 = "images/max_1.png"
image max_2 = "images/max_2.png"



label prologue:
    play music steps
    inner "Новелла\n«The Phantom Data»" with dissolve
    $renpy.pause(1.0)
    scene black
    show text "Вы — Алексей, студент направления «Информационная безопасность».\nВаша практика начинается не в офисе мечты...\n...а в подвале, где постоянно что-то происходит." with dissolve
    $renpy.pause(1.0)
    scene bg university_hall with fade
    play music "audio/prologue_theme.mp3" fadein 2.0
    nvl clear
    inner "ПРОЛОГ: {b}Распределение на практику{/b}"

    nvl clear
    window show
    stop music fadeout 0.5
    play music talks

    nvl clear
    scene bg prologue_door with fade
    show viktor_normal at Transform(xalign=1.0, yalign=1.0, zoom=1.05) with moveinright
    v "Алексей! А у меня для тебя... особый путь. Помнишь свой \"тест на безопасность \" серверной?"
    show alex_normal at Transform(left, ypos=0.04, zoom=1.2) with moveinleft 
    a "Тот, из-за которого у нас на неделю отменили стипендию?"
    v "Тот самый. Но есть способ всё исправить. Компания «The Phantom Data» готова взять тебя на практику."

    a "\"The Phantom Data\"? Это что за компания?"

    v "Мониторят IT-инфраструктуру. Недавно, например, раскопали историю — сисадмин в одном из дата-центров майнил крипту на серверах под систему 1С. Полгода работала \"самая дорогая бухгалтерия в городе\"."

    a "Звучит... сомнительно. А нельзя меня куда-нибудь в нормальное место?"
    hide viktor_normal with dissolve
    show viktor_skeptic at Transform(xalign=1.0, yalign=1.0, zoom=1.05) with dissolve
    v "В \"Типкофф\" — нет. А в \"The Phantom Data\" — да. И если их руководитель даст тебе хорошую характеристику... стипендию вернут. Досрочно."

    a "Ну ладно... А что я там вообще делать-то буду?"

    v "Сначала — помогать с рутиной. Мониторить проблемы, разбирать входящие заявки."

    menu:
        "«Эх... Ладно, лишь бы стипендию вернули.»":
            $ practical_score += 2
            a "Эх... Ладно, лишь бы стипендию вернули."

        "«Надеюсь, там хоть кофе есть нормальный...»":
            $ impulsive_score += 2
            a "Надеюсь, там хоть кофе есть нормальный..."

        "«Майнинг в 1С... Это хоть забавно. Любопытно, как они это обнаружили.»":
            $ analytical_score += 2
            a "Майнинг в 1С... Это хоть забавно. Любопытно, как они это обнаружили."

    nvl clear
    "А Серёга-то сейчас, наверное, уже кофе в новой кружке с логотипом \"Типькофф\" пьёт..."
    nvl clear
    window show

    v "Вот и славно. Держи адрес. Удачи."
    play sound door

    scene bg university_hall with fade

    "Алексей берёт бумажку. Сцена плавно переходит к двери с табличкой:"
    scene black with dissolve
    show text "«The Phantom Data. Заходи, если не боишься»."
    stop music fadeout 0.5
    $ renpy.pause(2.0)

    $ renpy.save("prologue_complete", "Пролог завершен")

    jump chapter_1