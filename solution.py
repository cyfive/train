import train

# длинна поезда задается здесь
my_train = train.Train(13)
my_train.print_train()
carriages_cnt = 0

# Если свет в "первом" вагоне не включен, то включаем его
if not my_train.get_light_status():
    my_train.set_light_status(True)

# Идем вперед пока не встретим вагон со включенным светом
while True:
    my_train.step_fwd()
    carriages_cnt += 1

    if my_train.get_light_status():
        # Выключем свет в вагоне
        my_train.set_light_status(False)
        # ... и возвращаемся назад на пройденое число вагонов
        backward_steps = carriages_cnt
        while backward_steps > 0:
            my_train.step_bwd()
            backward_steps -= 1
        
        # если свет выключен, то мы нашли искомое число вагонов
        if not my_train.get_light_status():
            print(f"Found wagoons: {carriages_cnt}")
            break
        else: # иначе идем опять вперед
            carriages_cnt = 0
