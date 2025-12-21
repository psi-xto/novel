image alex_normal = "images/alex_normal.png"
image alex_notebook = "images/alex_nb.png"
image alex_wow = "images/alex_wow.png"
image viktor_normal = "images/viktor_normal.png"
image viktor_sad = "images/viktor_sad.png"
image viktor_skeptic = "images/viktor_skeptic.png"
image max_1 = "images/max_1.png"
image max_2 = "images/max_2.png"


image attack_chain = "images/chapter1/chain.png"
image chat_message = "images/chapter1/chat.png"
image siem_alert = "images/chapter1/alert.png"
define a = Character("Алексей", color="#c8ffc8")
define m = Character("Максим", color="#c8c8ff")
define inner = Character("", kind=nvl, what_italic=True)
transform screen_center:
    xcenter 0.5
    ycenter 0.5


label chapter_1:
    nvl clear
    scene black
    show text "Глава 1\n{b}ПЕРВЫЙ ДЕНЬ{/b}" with dissolve
    $ renpy.pause(2.0)
    nvl clear
    scene office_soc 
    with fade
    play music servers volume 0.5
    show max_1 at Transform(xalign=1.0,ypos=0.04, zoom=1.15) with moveinright
    show alex_normal at Transform(left, ypos=0.04, zoom=1.2) with moveinleft 

    m "Ну что, пришла свежая кровь? Добро пожаловать в SOC. Вижу, Виктор Сергеевич тебя \"по рекомендации\" направил."

    a "Да... Стипендию нужно отрабатывать."

    m "Расслабься. У нас тут половина команды с такими же \"рекомендациями\" начинала. Это твоё рабочее место."
    m "Три монитора — твои глаза. SIEM — твоё чтиво на ближайшее время. Чат — твои уши. И да, кофе вон там, в углу."
    scene workspace 
    with fade
    stop music  fadeout 1.0
    play music siem volume 0.5 fadein 2.0

    $ examined_items = 0

    $ seen_siem = False
    $ seen_chat = False
    $ seen_chain = False

    label examine_loop:
        menu:
            "Посмотреть на SIEM":
                if not seen_siem:
                    show siem_alert at screen_center with dissolve
                    $ renpy.pause(1.5)
                    m "Запомни: SIEM — система мониторинга безопасности. Собирает данные со всех устройств и сигнализирует о подозрительных действиях."
                    m "Это не просто красный сигнал. Это история. Нужно понять, кто и зачем пытается войти."
                    hide siem_alert with dissolve
                    $ seen_siem = True
                    $ examined_items += 1
                else:
                    m "Ты уже изучил SIEM."

            "Посмотреть на чат":
                if not seen_chat:
                    show chat_message at screen_center with dissolve
                    $ renpy.pause(1.5)
                    m "Да уж, кому то с ночной смены так и не ответили... Что поделать."
                    hide chat_message with dissolve
                    $ seen_chat = True
                    $ examined_items += 1
                else:
                    m "Чат уже проверен."

            "Посмотреть на схему на стене":
                if not seen_chain:
                    show attack_chain at screen_center with dissolve
                    $ renpy.pause(1.5)
                    m "Любая атака начинается с одного клика. Твоя задача — остановить его до того, как он станет катастрофой."
                    hide attack_chain with dissolve
                    $ seen_chain = True
                    $ examined_items += 1
                else:
                    m "Схема уже изучена."

        if examined_items >= 3:
            jump after_examination

        jump examine_loop

    label after_examination:
        hide siem_alert
        hide chat_message
        hide attack_chain

        jump part2
    label part2:
        show siem_alert at screen_center with dissolve
        $ renpy.pause(1)

        m "Давай остановимся на одной вкладке подробнее. Это - твой первый \"клиент\". Смотри — SIEM ругается на множественные неудачные входы."
        hide siem_alert
        menu:
            "Cрочно блокировать IP!":
                $ impulsive_score += 2
                $ analytical_score -= 1
                m "Так мы сами создаем проблемы. Ты только что отключил обновления безопасности. Следующий раз — проверь, кто за этим IP."

            "Проверить историю активности IP":
                $ analytical_score += 2
                $ practical_score += 1
                m "Верный подход. Это не атака — это автоматическая проверка статуса. Ложное срабатывание."
                m "Теперь ты знаешь, как отличить шум от сигнала."

            "Это мелочь, игнорировать":
                $ impulsive_score += 1
                $ practical_score -= 2
                m "Из мелочей складываются большие проблемы. Ты перегрузил систему. Теперь мы не увидим настоящую атаку."
                m "Ты не виноват. Но ты должен понять: в SOC мелочи — это фундамент."

        hide siem_login_alert

    scene black

    nvl clear
    play sound notify

    m "Так, а у нас уже появился следующий кейс — сотрудник прислал подозрительное письмо."
    m "Найди три признака фишинга. У тебя ровно 60 секунд! Время пошло."

    $ phishing_found = 0
    $ phishing_attempts = 0

    call screen phishing_minigame

    if phishing_found >= 2:
        play sound success volume 0.5
        $ analytical_score += 3
        m "Отлично! Все признаки нашёл. Так и нужно — не доверять ни одному письму без проверки."
    elif phishing_found >= 1:
        play sound success volume 0.5
        $ practical_score += 1
        m "Хорошо, но можно было глубже копнуть. Фишинг — это не про ссылки. Это про психологию."
    else:
        play sound bad volume 0.33
        $ impulsive_score += 2
        $ analytical_score -= 2
        m "Ты много где напутал..."
        m "В реальной жизни, поведись бы получатель на это, он потерял бы все свои деньги, или еще хуже - заразил корпоративную сеть. Мы и нужны для того, чтобы не было никаких \"если\". "

    stop music fadeout 5

    scene office_soc with fade
    show max_1 at Transform(xalign=1.0,ypos=0.04, zoom=1.15) with moveinright
    show alex_normal at Transform(left, ypos=0.04, zoom=1.2) with moveinleft 

    m "Ну что, первый день прошёл."

    if analytical_score > 4:
        m "Вижу, ты любишь всё проверять основательно. Это ценно в расследованиях."
    elif practical_score > 4:
        m "Работаешь по инструкции, без лишних рисков. Надёжно."
    elif impulsive_score > 4:
        m "Действуешь быстро, но иногда слишком импульсивно. Учись тормозить."
    else:
        m "Неплохо для первого раза. Главное — не останавливайся."

    m "Завтра, наверняка, будет интереснее — хотя даже этого я тебе обещать не могу."

    $ renpy.pause(1.0)

    scene black with fade

    a "\"The Phantom Data\"... Да уж, подвальчик — далеко не \"Тинькофф\". Но... если тут майнили крипту на серверах 1С, значит, тут есть что-то настоящее."
    a "\"Заходи, если не боишься\"..."
    a "...Ну, пойдём."

    play sound door
    $ renpy.pause(1.0)

    $ renpy.save("chapter1_complete", "Глава 1 завершена")

jump chapter_2