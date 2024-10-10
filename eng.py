import time
import keyboard as k
import functions_eng


def eng():
    coins = 0
    coins_per_sec = 0.5
    energy = 500
    energy_consumption = 1
    lvl = 0
    loose = False

    # Горячие клавиши
    k.add_hotkey('t', lambda: print(f"Balance: {coins}\nCoins per second: {coins_per_sec}\n"
                                    f"Energy consumption: {energy_consumption}\nEnergy: {energy}\nLVL: {lvl}\n"))
    k.add_hotkey('p', lambda: print("The essence of the game is to swing up to level 10.\n"
                                    "To do this, you need to buy mining farms that will increase your income.\n"
                                    "Initially, your income is 0.5 coins per second. To buy a farm, press the S key\n"
                                    "and a store will open, which will have different mining farms in terms of\n"
                                    "capacity and cost. It won't be a problem to buy them.\n"
                                    "There is also an electricity consumption in the game. By buying a more powerful\n"
                                    "farm,electricity consumption increases. To increase your energy supply\n"
                                    "purchase a supply of electricity from the energy store by pressing the E key.\n"
                                    "Initially, the energy consumption is 1 kW per hour. When buying a new farm,\n"
                                    "the level increases. When you buy a new farm, the old one disappears.\n"
                                    "To find out stat (number of coins, coins per second, level and\n"
                                    "energy consumption), press the T key\n"))

    # Начало игры
    start_btn = input("Hello, press any key to start the game: ")

    if start_btn != '`':
        print("Welcome to MinerGame!\n")
        print("If you want to familiarize yourself with the guide for the game, press the P key\n")
        while not loose:
            while not loose:
                time.sleep(1)
                coins += coins_per_sec
                energy -= energy_consumption
                btn_s = k.is_pressed('s')
                btn_e = k.is_pressed('e')
                if energy <= 0:
                    print("I've run out of energy! Buy it!\n")
                    break
                if lvl == 5:
                    print("Congratulations!!! You have passed the game!!!")
                    loose = True

                # Магаз энергии
                if btn_e:
                    functions_eng.shop_list_energy()
                    while True:
                        choice_btn1 = k.is_pressed('1')
                        choice_btn_exit_shop = k.is_pressed('c')
                        if choice_btn1:
                            if coins >= 250:
                                print("Great! You bought a fuse of energy! I got you back into coin mining.\n")
                                energy += 1000
                                coins -= 250
                                break

                            else:
                                print("Insufficient funds\n")
                                time.sleep(0.1)
                        elif choice_btn_exit_shop:
                            print("You have left the energy store! Come back again!\n")
                            break

                # Магаз майнеров
                elif btn_s:
                    print("Select the section: D, F, G, H, J, E-exit the store\n")
                    while True:
                        choice_btn1 = k.is_pressed('d')
                        choice_btn2 = k.is_pressed('f')
                        choice_btn3 = k.is_pressed('g')
                        # choice_btn4 = k.is_pressed('h')
                        # choice_btn5 = k.is_pressed('j')
                        choice_btn_exit_shop = k.is_pressed('e')

                        # РАЗДЕЛ 1
                        if choice_btn1:
                            functions_eng.shop_list_1()
                            while True:
                                btn_1 = k.is_pressed('1')
                                btn_2 = k.is_pressed('2')
                                btn_esc = k.is_pressed('c')
                                if btn_1:
                                    if coins >= 20:
                                        print("Great! You have bought a level 1 miner. Your level: 1.\n"
                                              "I brought you back to the menu of the razels\n"
                                              "Select the section: D, F, G, H, J, E-exit the store\n")
                                        lvl = 1
                                        coins_per_sec = 2
                                        energy_consumption = 3
                                        coins -= 20
                                        break
                                    else:
                                        print("Insufficient funds\n")
                                        time.sleep(0.1)
                                if btn_2:
                                    if coins >= 120:
                                        print("Great! You have bought a level 2 miner. Your level is 2.\n"
                                              "I brought you back to the menu of the razels\n"
                                              "Select the section: D, F, G, H, J, E-exit the store\n")
                                        lvl = 2
                                        coins_per_sec = 5
                                        energy_consumption = 6
                                        coins -= 120
                                        break
                                    else:
                                        print("Insufficient funds\n")
                                        time.sleep(0.1)
                                elif btn_esc:
                                    print("You have entered the section menu!\n"
                                          "Select the section: D, F, G, H, J, E-exit the store\n")
                                    break

                        # РАЗДЕЛ 2
                        elif choice_btn2:
                            functions_eng.shop_list_2()
                            while True:
                                btn_1 = k.is_pressed('1')
                                btn_2 = k.is_pressed('2')
                                btn_esc = k.is_pressed('c')
                                if btn_1:
                                    if coins >= 350:
                                        print("Great! You have bought a level 3 miner. Your level is 3.\n"
                                              "I brought you back to the menu of the razels\n"
                                              "Select the section: D, F, G, H, J, E-exit the store\n")
                                        lvl = 3
                                        coins_per_sec = 10
                                        energy_consumption = 15
                                        coins -= 350
                                        break
                                    else:
                                        print("Insufficient funds\n")
                                        time.sleep(0.1)
                                elif btn_2:
                                    if coins >= 550:
                                        print("Great! You have bought a level 4 miner. Your level is 4.\n"
                                              "I brought you back to the menu of the razels\n"
                                              "Select the section: D, F, G, H, J, E-exit the store\n")
                                        lvl = 4
                                        coins_per_sec = 13
                                        energy_consumption = 14
                                        coins -= 550
                                        break
                                    else:
                                        print("Insufficient funds\n")
                                        time.sleep(0.1)
                                elif btn_esc:
                                    print("You have entered the section menu!\n"
                                          "Select the section: D, F, G, H, J, E-exit the store\n")
                                    break
                        # РАЗДЕЛ 3
                        elif choice_btn3:
                            functions_eng.shop_list_3()
                            while True:
                                btn_1 = k.is_pressed('1')
                                # btn_2 = k.is_pressed('2')
                                btn_esc = k.is_pressed('c')
                                if btn_1:
                                    if coins >= 700:
                                        print("Great! You have bought a level 5 miner. Your level is 5.\n"
                                              "I brought you back to the menu of the razels\n"
                                              "Select the section: D, F, G, H, J, E-exit the store\n")
                                        lvl = 5
                                        coins_per_sec = 15
                                        energy_consumption = 14
                                        coins -= 700
                                        break
                                    else:
                                        print("Insufficient funds\n")
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
                                    print("You have entered the section menu!\n"
                                          "Select the section: D, F, G, H, J, E-exit the store\n")
                                    break
                        # Выход из магазина
                        elif choice_btn_exit_shop:
                            print("You have left the miner store. Come back again!\n")
                            break
            # ПОТЕРЯ ЭНЕРГИИ
            functions_eng.shop_list_energy()
            while not loose:
                btn_1 = k.is_pressed('1')
                if btn_1:
                    if coins >= 250:
                        print("Great! You bought a fuse of energy! I got you back into coin mining.\n")
                        energy += 1000
                        coins -= 250
                        break

                    else:
                        print("Insufficient funds")
                        print("Alas, you have lost.")
                        loose = True
                        break
