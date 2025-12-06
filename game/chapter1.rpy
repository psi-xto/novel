
image bg office_soc  = "images/bgs/2.1.png"
image bg workspace = "images/bgs/2.2.png"
image attack_chain = "images/chapter1/chain.png"
image chat_message = "images/chapter1/chat.png"
image siem_alert = "images/chapter1/alert.png"
define a = Character("Алексей", color="#c8ffc8")
define m = Character("Максим", color="#c8c8ff")
define inner = Character("", kind=nvl, what_italic=True)
transform screen_center:
    xalign 0.5
    yalign 0.5

label chapter_1:
    nvl clear
    scene bg office_soc 
    with fade

    show max_1 at Transform(xalign=1.0,ypos=0.04, zoom=1.15) with moveinright
    show alex_normal at Transform(left, ypos=0.04, zoom=1.2) with moveinleft 

    #play music "audio/first_shift.mp3" fadein 2.0
    #play sound "audio/server_hum.wav" loop

    m "Ну что, пришла свежая кровь? Добро пожаловать в SOC. Вижу, Виктор Сергеевич тебя \"по рекомендации\" направил."

    a "Да... Стипендию нужно отрабатывать."

    m "Расслабься. У нас тут половина команды с такими же \"рекомендациями\" начинала. Это твоё рабочее место."
    m "Три монитора — твои глаза. SIEM — твоё чтиво на ближайшее время. Чат — твои уши. И да, кофе вон там, в углу."
    scene bg workspace 
    with fade

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
        #play sound "audio/siem_alert.wav"
        show siem_alert at screen_center with dissolve
        $ renpy.pause(1)

        m "Давай остановимся на одной вкладке подробнее. Это - твой первый \"клиент\". Смотри — SIEM ругается на множественные неудачные входы."
        hide siem_alert
        menu:
            "СРОЧНО БЛОКИРОВАТЬ IP!":
                $ impulsive_score += 2
                $ analytical_score -= 1
                $ renpy.pause(1.0)
                #show chat_blocked_message at center with dissolve
                $ renpy.pause(2.0)
                m "Так мы сами создаем проблемы. Ты только что отключил обновления безопасности. Следующий раз — проверь, кто за этим IP."
                #hide chat_blocked_message with dissolve

            "ПРОВЕРИТЬ ИСТОРИЮ АКТИВНОСТИ IP":
                $ analytical_score += 2
                $ practical_score += 1
                $ renpy.pause(1.0)
                #show ip_history at center with dissolve
                $ renpy.pause(2.0)
                m "Верный подход. Это не атака — это автоматическая проверка статуса. Ложное срабатывание."
                m "Теперь ты знаешь, как отличить шум от сигнала."
                #hide ip_history with dissolve

            "ЭТО МЕЛОЧЬ, ИГНОРИРОВАТЬ":
                $ impulsive_score += 1
                $ practical_score -= 2
                $ renpy.pause(1.0)
                #show siem_overload at center with dissolve
                $ renpy.pause(2.0)
                m "Из мелочей складываются большие проблемы. Ты перегрузил систему. Теперь мы не увидим настоящую атаку."
                m "Ты не виноват. Но ты должен понять: в SOC мелочи — это фундамент."
                #hide siem_overload with dissolve

        hide siem_login_alert

    scene black

    nvl clear
    inner "Пока что силы у разработчика закончились. Демоверсия тоже."
    #     #play sound "audio/email_ping.wav"
    #     show phishing_email at center with dissolve

    #     m "Следующий кейс — сотрудник прислал подозрительное письмо."
    #     m "Найди три признака фишинга. У тебя 2 минуты."

    #     $ phishing_found = 0

    #     call screen phishing_minigame

    #     if phishing_found >= 3:
    #         $ analytical_score += 3
    #         m "Отлично! Все признаки нашёл. Так и нужно — не доверять ни одному письму без проверки."
    #     elif phishing_found >= 1:
    #         $ practical_score += 1
    #         m "Хорошо, но можно было глубже копнуть. Фишинг — это не про ссылки. Это про психологию."
    #     else:
    #         $ impulsive_score += 2
    #         $ analytical_score -= 2
    #         m "В реальной жизни ты бы сейчас заразил всю сеть."

    #     hide phishing_email with dissolve

    #     #play sound "audio/day_end_bell.wav"
    #     #stop music fadeout 2.0
    #     show maxim neutral at right
    #     show alexey thinking at left

    #     m "Ну что, первый день прошёл."

    #     if analytical_score > 4:
    #         m "Вижу, ты любишь всё проверять основательно. Это ценно в расследованиях."
    #     elif practical_score > 4:
    #         m "Работаешь по инструкции, без лишних рисков. Надёжно."
    #     elif impulsive_score > 4:
    #         m "Действуешь быстро, но иногда слишком импульсивно. Учись тормозить."
    #     else:
    #         m "Неплохо для первого раза. Главное — не останавливайся."

    #     m "Завтра, наверняка, будет интереснее — хотя даже этого я тебе обещать не могу."

    #     show maxim hand_paper
    #     $ renpy.pause(1.0)

    #     "[Внутренний голос Алексея] \"The Phantom Data\"... Да уж, подвальчик — далеко не \"Тинькофф\". Но... если тут майнили крипту на серверах 1С, значит, тут есть что-то настоящее."

    #     $ renpy.pause(1.5)
    #     "[Внутренний голос Алексея] \"Заходи, если не боишься\"..."

    #     $ renpy.pause(1.0)
    #     "[Внутренний голос Алексея] ...Ну, пойдём."

    #     scene office_soc with fade
    #     #play sound "audio/door_close.wav"
    #     $ renpy.pause(2.0)

    # # Переход к главе 2
    # jump chapter_2