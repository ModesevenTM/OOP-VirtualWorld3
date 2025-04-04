from Zwierze import *

class Antylopa(Zwierze):
    AntylopaSila = 4
    __AntylopaInicjatywa = 4
    __AntylopaZasieg = 2
    __AntylopaDzielnik = 2
    __AntylopaSzanse = 1

    def __init__(self, ws, s = AntylopaSila, w = 0):
        super().__init__(ws, s, self.__AntylopaInicjatywa, w)
        self._zasieg = self.__AntylopaZasieg

    def nazwa(self):
        return "Antylopa"

    def rysowanie(self):
        return "chocolate3"

    def klonuj(self, ws):
        klon = Antylopa(ws)
        klon.setSwiat(self._swiat)
        klon.setWiek(Organizm.NOWORODEK)
        return klon

    def _czyMozeUciec(self):
        return randrange(0, self.__AntylopaDzielnik) < self.__AntylopaSzanse

    def _czyOdbilAtak(self, atakujacy):
        return False

    def _czyDobryWech(self):
        return False

    def _czyEksterminuje(self):
        return False
