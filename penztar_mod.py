import database as db


def penztar_menu() -> None:
    while True:
        print(
            """0 - Vissza a főmenübe
1 - Új törzsvendég
2 - Rendelés
3 - Befizetés"""
        )
        choice = int(input("Válasszon menüpontot: "))
        if choice == 1:
            uj_vendeg()
        elif choice == 0:
            break


def uj_vendeg():
    name = input("Vendég neve: ")
    if not db.new_guest(name):
        print("Ilyen nevű vendég már létezik!")
