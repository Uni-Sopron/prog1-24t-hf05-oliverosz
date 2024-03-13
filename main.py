"""The entry point of the application."""

import penztar_mod


def run():
    while True:
        print("0 - Kilépés\n", "1 - Pénztáros mód\n", "2 - Admin mód", sep="")
        choice = int(input("Válasszon menüpontot: "))
        if choice == 0:
            break
        elif choice == 1:
            penztar_mod.penztar_menu()


if __name__ == "__main__":
    run()
