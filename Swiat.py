from zwierzeta.Czlowiek import *
from Kierunki import *
from Wspolrzedne import *

class Swiat:
    __tura = 0
    __organizmy = []
    __zdarzenia = []
    __ruchCzlowieka = Kierunki.stoi
    __kiedyUmiejetnosc = -Czlowiek.CzlowiekWzrost * 2
    __czyCzlowiekZyje = True

    def __init__(self, sz, wys):
        self.__szerokosc = sz
        self.__wysokosc = wys

    def getSzerokosc(self):
        return self.__szerokosc

    def getWysokosc(self):
        return self.__wysokosc

    def getTura(self):
        return self.__tura

    def getRuchCzlowieka(self):
        return self.__ruchCzlowieka

    def getNazwaRuchu(self):
        match self.__ruchCzlowieka:
            case Kierunki.gora:
                return "góra"
            case Kierunki.dol:
                return "dół"
            case Kierunki.lewo:
                return "lewo"
            case Kierunki.prawo:
                return "prawo"
        return "brak"

    def getKiedyUmiejetnosc(self):
        return self.__kiedyUmiejetnosc

    def getZycieCzlowieka(self):
        return self.__czyCzlowiekZyje

    def setSzerokosc(self, s):
        self.__szerokosc = s

    def setWysokosc(self, w):
        self.__wysokosc = w

    def setTura(self, t):
        self.__tura = t

    def setRuchCzlowieka(self, k):
        self.__ruchCzlowieka = k

    def setKiedyUmiejetnosc(self, ku):
        self.__kiedyUmiejetnosc = ku

    def setZycieCzlowieka(self, z):
        self.__czyCzlowiekZyje = z

    def dodajOrganizm(self, org):
        org.setSwiat(self)
        self.__organizmy.append(org)

    def getZajete(self, ws):
        zwroc = None
        for organizm in self.__organizmy:
            obecny = organizm.getPolozenie()
            if ws.x == obecny.x and ws.y == obecny.y and (zwroc is None or organizm.getSila() > zwroc.getSila()):
                zwroc = organizm
        return zwroc

    def getKolizja(self, org):
        for organizm in self.__organizmy:
            if org != organizm and org.getPolozenie().x == organizm.getPolozenie().x and \
                    org.getPolozenie().y == organizm.getPolozenie().y and org.getWiek() > Organizm.NOWORODEK:
                return organizm
        return None

    def getWolneObok(self, ws):
        kierunki = []
        if ws.x - 1 >= 0 and self.getZajete(Wspolrzedne(ws.x - 1, ws.y)) is None:
            kierunki.append(Wspolrzedne(ws.x - 1, ws.y))
        if ws.x + 1 < self.__szerokosc and self.getZajete(Wspolrzedne(ws.x + 1, ws.y)) is None:
            kierunki.append(Wspolrzedne(ws.x + 1, ws.y))
        if ws.y - 1 >= 0 and self.getZajete(Wspolrzedne(ws.x, ws.y - 1)) is None:
            kierunki.append(Wspolrzedne(ws.x, ws.y - 1))
        if ws.y + 1 < self.__wysokosc and self.getZajete(Wspolrzedne(ws.x, ws.y + 1)) is None:
            kierunki.append(Wspolrzedne(ws.x, ws.y + 1))
        if len(kierunki) > 0:
            return kierunki[randrange(0, len(kierunki))]
        else:
            return ws

    def getOrganizmy(self):
        return self.__organizmy

    def usunMartwe(self):
        for i in range(len(self.__organizmy) - 1, -1, -1):
            self.__organizmy[i].zmienStatusRozmnozenia()
            if not self.__organizmy[i].getZycie():
                self.__organizmy.pop(i)

    def usunWszystkie(self):
        self.__organizmy.clear()

    def getZdarzenia(self):
        return self.__zdarzenia

    def dodajZdarzenie(self, zd):
        self.__zdarzenia.append(zd)

    def wyczyscZdarzenia(self):
        self.__zdarzenia.clear()

    def przeprowadzTure(self):
        self.__organizmy = sorted(self.__organizmy, key=lambda x:(x.getInicjatywa(),x.getWiek()), reverse=True)
        for i in range(len(self.__organizmy)):
            if self.__organizmy[i].getZycie() and self.__organizmy[i].getWiek() > Organizm.NOWORODEK:
                self.__organizmy[i].akcja()
                self.__organizmy[i].kolizja()
            self.__organizmy[i].zwiekszWiek()

    def nowaTura(self):
        self.wyczyscZdarzenia()
        self.__tura += 1
        self.przeprowadzTure()
        self.usunMartwe()

    def uzyjUmiejetnosci(self):
        if self.__tura + 1 >= self.__kiedyUmiejetnosc + 2 * Czlowiek.CzlowiekWzrost:
            self.__kiedyUmiejetnosc = self.__tura + 1