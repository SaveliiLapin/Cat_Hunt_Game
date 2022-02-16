import variables as v
import nickname_menu as nnm
import main_menu as mm
import game as g
import pause_menu as p
import lose as l
import end as e
import top_players as tp

while True:
    if v.SCREEN_CHOICE == 0:
        nnm.name_menu()
    elif v.SCREEN_CHOICE == 1:
        mm.main_menu()
    elif v.SCREEN_CHOICE == 2:
        g.game()
    elif v.SCREEN_CHOICE == 3:
        p.pause()
    elif v.SCREEN_CHOICE == 4:
        l.lose()
    elif v.SCREEN_CHOICE == 5:
        e.end()
    elif v.SCREEN_CHOICE == 6:
        tp.top_players()

# БАГИ
# враг пропадает сразу, если попал в него, когда он собирается передвинуться
# убитого, но еще не исчезнувшего врага, нельзя прострелить насквозь
# если поставить ограничение по FPS в любом из меню, где есть выбор, прямоугольник выбора будет запаздывать с изменением размера

# ХОТЕЛОСЬ БЫ УЗНАТЬ
# как сделать полноценный ввод с клавиатуры без использования списков
# как сделать простейшее сетевое соединение
