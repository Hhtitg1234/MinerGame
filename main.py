import time
import keyboard as k
import functions


# Переменные
coins = 0
coins_per_sec = 0.5
energy = 500
energy_consumption = 1
lvl = 0
loose = False


# Горячие клавиши
k.add_hotkey('t', lambda: print(f"Balance: {coins}\nCoins per second: {coins_per_sec}\n"
                                f"Energy consumption: {energy_consumption}\nEnergy: {energy}\nLVL: {lvl}\n"))
k.add_hotkey('p', lambda: print("The essence of the game is to swing up to level 10. To do this, you need to buy\n"
                                "mining farms that will increase your income.\n"
                                "Initially, your income is 0.5 coins per second. To buy a farm, press the S key and a\n"
                                "store will open, which will have different\n"
                                "mining farms in terms of capacity and cost. It won't be a problem to buy them.\n"
                                "There is also an electricity consumption in the game. By buying a more powerful farm\n"
                                ",electricity consumption increases. To increase your energy supply, buy a store of\n"
                                "electricity in the store. Initially, the energy consumption is 1 kW per hour. When \n"
                                "buying a new farm, the level increases. When you buy a new farm, the old one\n"
                                "disappears. To find out stat\n"
                                "(number of coins, coins per second, level and energy consumption), press the T key\n"))

# Начало игры
start_btn = input("Здравствуйте, нажмите любую клавишу для запуска игры: ")

if start_btn != '`':
    print("Welcome to MinerGame!\n")
    print("If U want to read a reference, pls press P key\n")
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
                print("U WIN!!!")
                loose = True

            # Магаз энергии
            if btn_e:
                functions.shop_list_energy()
                while True:
                    choice_btn1 = k.is_pressed('1')
                    choice_btn_exit_shop = k.is_pressed('c')
                    if choice_btn1:
                        if coins >= 250:
                            print("Nice! U buy store of electricity! I have returned you to the spoils\n")
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
                print("Выберите раздел: D, F, G, H, J, E-exit\n")
                while True:
                    choice_btn1 = k.is_pressed('d')
                    choice_btn2 = k.is_pressed('f')
                    choice_btn3 = k.is_pressed('g')
                    # choice_btn4 = k.is_pressed('h')
                    # choice_btn5 = k.is_pressed('j')
                    choice_btn_exit_shop = k.is_pressed('e')

                    # РАЗДЕЛ 1
                    if choice_btn1:
                        functions.shop_list_1()
                        while True:
                            btn_1 = k.is_pressed('1')
                            btn_2 = k.is_pressed('2')
                            btn_esc = k.is_pressed('c')
                            if btn_1:
                                if coins >= 20:
                                    print("Nice! U buy lvl 1 miner. Your lvl is 1. I have returned you to the spoils\n")
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
                                    print("Nice! U buy lvl 2 miner. Your lvl is 2. I have returned you to the spoils\n")
                                    lvl = 2
                                    coins_per_sec = 5
                                    energy_consumption = 6
                                    coins -= 120
                                    break
                                else:
                                    print("Недостаточно средств\n")
                                    time.sleep(0.1)
                            elif btn_esc:
                                print("Вы вышли в меню разделов! Выберите раздел: D, F, G, H, J, E-exit\n")
                                break

                    # РАЗДЕЛ 2
                    elif choice_btn2:
                        functions.shop_list_2()
                        while True:
                            btn_1 = k.is_pressed('1')
                            btn_2 = k.is_pressed('2')
                            btn_esc = k.is_pressed('c')
                            if btn_1:
                                if coins >= 350:
                                    print("Nice! U buy lvl 3 miner. Your lvl is 3. I have returned you to the spoils\n")
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
                                    print("Nice! U buy lvl 4 miner. Your lvl is 4. I have returned you to the spoils\n")
                                    lvl = 4
                                    coins_per_sec = 13
                                    energy_consumption = 14
                                    coins -= 550
                                    break
                                else:
                                    print("Недостаточно средств\n")
                                    time.sleep(0.1)
                            elif btn_esc:
                                print("Вы вышли в меню разделов! Выберите раздел: D, F, G, H, J, E-exit\n")
                                break
                    # РАЗДЕЛ 3
                    elif choice_btn3:
                        functions.shop_list_3()
                        while True:
                            btn_1 = k.is_pressed('1')
                            # btn_2 = k.is_pressed('2')
                            btn_esc = k.is_pressed('c')
                            if btn_1:
                                if coins >= 700:
                                    print("Nice! U buy lvl 5 miner. Your lvl is 4. I have returned you to the spoils\n")
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
                                print("Вы вышли в меню разделов! Выберите раздел: D, F, G, H, J, E-exit\n")
                                break
                    # Выход из магазина
                    elif choice_btn_exit_shop:
                        print("Вы вышли из магазина майнеров. Заходите еще!\n")
                        break
        # ПОТЕРЯ ЭНЕРГИИ
        functions.shop_list_energy()
        while not loose:
            btn_1 = k.is_pressed('1')
            if btn_1:
                if coins >= 250:
                    print("Nice! U buy store of electricity! I have returned you to the spoils")
                    energy += 1000
                    coins -= 250
                    break

                else:
                    print("Недостаточно средств")
                    print("Увы, но вы проиграли.")
                    loose = True
                    break
