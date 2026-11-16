
import random

class Futbolcu:

    def __init__(self):
        self.puan = 100
        self.can = 3

    def hareket_yap(self, secim):

        if secim == 1:
            self.puan = self.puan - 25
            print("Topu kaptirdin! -25 puan")

        elif secim == 2:
            self.puan = self.puan + 15
            print("Rakibi calimladin! +15 puan")

        elif secim == 3:
            self.puan = self.puan + 30
            print("GOOOL! +30 puan")

        elif secim == 4:
            sans = random.randint(1, 5)

            if sans == 1:
                self.puan = self.puan + 50
                print("ROVESATA GOL! +50 puan")
            else:
                print("Rovesata basarisiz!")

        else:
            print("Hatali secim!")

    def can_kontrol(self):

        if self.puan <= 0:
            self.can = self.can - 1

            if self.can > 0:
                self.puan = 100
                print("Bir can hakkin gitti!")
                print("Yeni puan:", self.puan)
                print("Kalan can:", self.can)

            else:
                print("GAME OVER!")


def menu_yazdir():

    print("1- Topu rakibe kaptir")
    print("2- Rakibi calimla")
    print("3- Gol at")
    print("4- Rovesata dene")


futbolcu = Futbolcu()

print("FUTBOL OYUNUNA HOS GELDIN!")

while futbolcu.can > 0:

    menu_yazdir()

    secim = int(input("Seciminizi yapin: "))

    futbolcu.hareket_yap(secim)

    futbolcu.can_kontrol()

    if futbolcu.can > 0:
        print("Guncel puan:", futbolcu.puan)
        print("Kalan can:", futbolcu.can)

print("OYUN BITTI!")
