def game():
    print('                **    **  ********  **        **            **      ')
    print("               **    **  ********  **        **         **     **   ")
    print("              ********  **        **        **         **      **  ")
    print("             ********  ********  **        **         **      **  ")
    print("            **    **  **        **        **         **      **  ")
    print("           **    **  ********  ********  ********    **    **   ")
    print("          **    **  ********  ********  ********       **      ")

    def is_valid_(s):
        if str(s).isdigit():
            return True
        return False

    def is_valid(s, q, w):
        if s.isdigit():
            if q <= int(s) <= w:
                return True
        return False

    def start():
        import random
        import math
        print('Добро пожаловать в числовую угадайку')
        while True:
            l_border = input('Введите левую границу диапозона')
            if is_valid_(l_border):
                l_border = int(l_border)
                break
            elif not is_valid_(l_border):
                print('А может быть все-таки введем целое число?')
                continue
        while True:
            r_border = input('Введите правую границу диапозона')
            if is_valid_(r_border):
                r_border = int(r_border)
                break
            elif not is_valid_(r_border):
                print('А может быть все-таки введем целое число?')
                continue
        num = random.randint(l_border, r_border)
        if r_border - l_border == 1 or r_border - l_border == 2:
            try_counter = 1
        else:
            try_counter = math.ceil(math.log2(r_border - l_border))
        print(f'Количество попыток: {try_counter}')
        attempts = 0
        compare_numbers(attempts, try_counter, l_border, r_border, num)

    def continue_game():
        while True:
            restart = input('Сыграете ещё? (Введите "да" или "нет"): ')
            if restart.lower() == 'да':
                start()
            elif restart.lower() == 'нет':
                print("                 *******   **     **    ********")
                print("                *******     **   **    ********")
                print("               **   **       ** **    ***       ")
                print("              ******          ***    ********")
                print("             ******           **    ********")
                print("            **   **          **    ***     ")
                print("           ********         **    ********")
                print("          ********         **    ********")
                break
            else:
                print('Я не понимаю. Введите "да" или "нет"')
                continue

    def compare_numbers(attempts, try_counter, l_border, r_border, num):
        while attempts != try_counter + 1:
            n = input(f'Введите число от {l_border} до {r_border}')
            if is_valid(n, l_border, r_border):
                n = int(n)
                if attempts == try_counter - 1 and n != num:
                    attempts += 1
                    print(
                        'К сожалению количество попыток закончилось, попробуйте ещё раз, у вас всё обязательно получится!')
                    print(f'Загаданным числом было {num}')
                    continue_game()
                    break
                if n > num:
                    attempts += 1
                    print('Ваше число больше загаданного, попробуйте еще разок')
                elif n < num:
                    attempts += 1
                    print('Ваше число меньше загаданного, попробуйте еще разок')
                else:
                    attempts += 1
                    print('Вы угадали, поздравляем!')
                    print(f'Количество использованных попыток {attempts} из {try_counter}')
                    continue_game()
                    break
                print(f'Осталось попыток: {try_counter - attempts}')
            elif not is_valid(n, l_border, r_border) or n == '':
                print(f'А может быть все-таки введем целое число от {l_border} до {r_border}?')

    start()


game()