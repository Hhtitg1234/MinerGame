import time
import keyboard as k
import functions_rus
# На будущее! Сделать английскую версию и русскую путем создания 2 функций и запуска их тут в зависимости от выбора!


def rus():
    # Переменные
    coins = 9999999999
    coins_per_sec = 0.5
    energy = 50000000000
    energy_consumption = 1
    lvl = 0
    loose = False

    # Горячие клавиши
    k.add_hotkey('t', lambda: print(f"Баланс: {coins}\nМонеты в секунду: {coins_per_sec}\n"
                                    f"Потребление энергии: {energy_consumption}\nЭнергия: {energy}\nУровень: {lvl}\n"))
    k.add_hotkey('p', lambda: print("Суть игры заключается в том, чтобы прокачаться до 10 уровня.\n"
                                    "Для этого вам нужно купить майнинговые фермы, которые увеличат ваш доход.\n"
                                    "Изначально ваш доход составляет 0,5 монеты в секунду. Чтобы купить ферму,\n"
                                    "нажмите клавишу S, и откроется магазин, в котором будут представлены фермы для\n"
                                    "майнинга, отличающиеся по мощности и стоимости. Купить их не составит труда.\n"
                                    "В игре также присутствует потребление электроэнергии. При покупке более мощной\n"
                                    "фермы потребление электроэнергии увеличивается. Чтобы увеличить запас энергии,\n"
                                    "приобретите запас электроэнергии из хранилища энергии, нажав клавишу E.\n"
                                    "Изначально потребление энергии составляет 1 кВт в секунду.\n"
                                    "При покупке новой фермы уровень увеличивается. Когда вы покупаете новую ферму,\n"
                                    "старая исчезает. Чтобы узнать статистику (количество монет, количество монет в\n"
                                    "секунду, уровень и потребление энергии), нажмите клавишу T\n"))

    # Начало игры
    start_btn = input("Здравствуйте, нажмите любую клавишу для запуска игры: ")

    if start_btn != '`':
        print("Добро пожаловать в MinerGame!\n")
        print("Если вы хотите ознакомиться с гайдом для игры, нажмите клавишу P\n")
        while not loose:
            while not loose:
                time.sleep(1)
                coins += coins_per_sec
                energy -= energy_consumption
                btn_s = k.is_pressed('s')
                btn_e = k.is_pressed('e')
                if energy <= 0:
                    print("Закончилась энергия! Купите ее!\n")
                    break
                if lvl == 5:
                    print("Поздравляю!!! Вы прошли игру!!!")
                    loose = True

                # Магаз энергии
                if btn_e:
                    functions_rus.shop_list_energy()
                    while True:
                        choice_btn1 = k.is_pressed('1')
                        choice_btn_exit_shop = k.is_pressed('c')
                        if choice_btn1:
                            if coins >= 250:
                                print("Отлично! Вы купиили запал энергии! Я вернул тебя в меню разделов\n"
                                      "Выберите раздел: D, F, G, H, J, E-выход из магазина\n")
                                energy += 1000
                                coins -= 250
                                break

                            else:
                                print("Недостаточно средств\n")
                                time.sleep(0.1)
                        elif choice_btn_exit_shop:
                            print("Вы вышли из магазина энергии! Заходите еще!\n")
                            break

                # Магаз майнеров
                elif btn_s:
                    print("Выберите раздел: D, F, G, H, J, E-выход из магазина\n")
                    while True:
                        choice_btn1 = k.is_pressed('d')
                        choice_btn2 = k.is_pressed('f')
                        choice_btn3 = k.is_pressed('g')
                        # choice_btn4 = k.is_pressed('h')
                        # choice_btn5 = k.is_pressed('j')
                        choice_btn_exit_shop = k.is_pressed('e')

                        # РАЗДЕЛ 1
                        if choice_btn1:
                            functions_rus.shop_list_1()
                            while True:
                                btn_1 = k.is_pressed('1')
                                btn_2 = k.is_pressed('2')
                                btn_esc = k.is_pressed('c')
                                if btn_1:
                                    if coins >= 20:
                                        print("Отлично! Вы купили майнер 1 уровня. Твой уровень: 1.\n"
                                              "Я вернул тебя в меню разделов\n"
                                              "Выберите раздел: D, F, G, H, J, E-выход из магазина\n")
                                        lvl = 1
                                        coins_per_sec = 2
                                        energy_consumption = 3
                                        coins -= 20
                                        break
                                    else:
                                        print("Недостаточно средств\n")
                                        time.sleep(0.1)
                                if btn_2:
                                    if coins >= 120:
                                        print("Отлично! Вы купили майнер 2 уровня. Твой уровень: 2.\n"
                                              "Я вернул тебя в меню разделов\n"
                                              "Выберите раздел: D, F, G, H, J, E-выход из магазина\n")
                                        lvl = 2
                                        coins_per_sec = 5
                                        energy_consumption = 6
                                        coins -= 120
                                        break
                                    else:
                                        print("Недостаточно средств\n")
                                        time.sleep(0.1)
                                elif btn_esc:
                                    print("Вы вышли в меню разделов!\n"
                                          "Выберите раздел: D, F, G, H, J, E-выход из магазина\n")
                                    break

                        # РАЗДЕЛ 2
                        elif choice_btn2:
                            functions_rus.shop_list_2()
                            while True:
                                btn_1 = k.is_pressed('1')
                                btn_2 = k.is_pressed('2')
                                btn_esc = k.is_pressed('c')
                                if btn_1:
                                    if coins >= 350:
                                        print("Отлично! Вы купили майнер 3 уровня. Твой уровень: 3.\n"
                                              "Я вернул тебя в меню разделов\n"
                                              "Выберите раздел: D, F, G, H, J, E-выход из магазина\n")
                                        lvl = 3
                                        coins_per_sec = 10
                                        energy_consumption = 15
                                        coins -= 350
                                        break
                                    else:
                                        print("Недостаточно средств\n")
                                        time.sleep(0.1)
                                elif btn_2:
                                    if coins >= 550:
                                        print("Отлично! Вы купили майнер 4 уровня. Твой уровень: 4.\n"
                                              "Я вернул тебя в меню разделов\n"
                                              "Выберите раздел: D, F, G, H, J, E-выход из магазина\n")
                                        lvl = 4
                                        coins_per_sec = 13
                                        energy_consumption = 14
                                        coins -= 550
                                        break
                                    else:
                                        print("Недостаточно средств\n")
                                        time.sleep(0.1)
                                elif btn_esc:
                                    print("Вы вышли в меню разделов!\n"
                                          "Выберите раздел: D, F, G, H, J, E-выход из магазина\n")
                                    break
                        # РАЗДЕЛ 3
                        elif choice_btn3:
                            functions_rus.shop_list_3()
                            while True:
                                btn_1 = k.is_pressed('1')
                                # btn_2 = k.is_pressed('2')
                                btn_esc = k.is_pressed('c')
                                if btn_1:
                                    if coins >= 700:
                                        print("Отлично! Вы купили майнер 5 уровня. Твой уровень: 5.\n"
                                              "Я вернул тебя в меню разделов\n"
                                              "Выберите раздел: D, F, G, H, J, E-выход из магазина\n")
                                        lvl = 5
                                        coins_per_sec = 15
                                        energy_consumption = 14
                                        coins -= 700
                                        break
                                    else:
                                        print("Недостаточно средств\n")
                                        time.sleep(0.1)
                                # if btn_2:
                                    # if coins >= 120:
                                #     print("Nice! U buy lvl 2 miner. Your lvl is 2. I have returned you to the spoils")
                                    #     lvl = 2
                                    #     coins_per_sec = 5
                                    #     energy_consumption = 6
                                    #     coins -= 120
                                    #     break
                                    # else:
                                    #     print("Недостаточно средств\n")
                                    #     time.sleep(0.1)
                                elif btn_esc:
                                    print("Вы вышли в меню разделов!\n"
                                          "Выберите раздел: D, F, G, H, J, E-выход из магазина\n")
                                    break
                        # Выход из магазина
                        elif choice_btn_exit_shop:
                            print("Вы вышли из магазина майнеров. Заходите еще!\n")
                            break
            # ПОТЕРЯ ЭНЕРГИИ
            functions_rus.shop_list_energy()
            while not loose:
                btn_1 = k.is_pressed('1')
                if btn_1:
                    if coins >= 250:
                        print("Отлично! Вы купиили запал энергии! Я вернул тебя в добычу монет.\n")
                        energy += 1000
                        coins -= 250
                        break

                    else:
                        print("Недостаточно средств")
                        print("Увы, но вы проиграли.")
                        loose = True
                        break
