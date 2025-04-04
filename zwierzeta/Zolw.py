from Zwierze import *


class Zolw(Zwierze):
    ZolwSila = 2
    __ZolwInicjatywa = 1
    __ZolwDzielnik = 4
    __ZolwSzanse = 1
    __ZolwOdparcie = 5

    def __init__(self, ws, s=ZolwSila, w=0):
        super().__init__(ws, s, self.__ZolwInicjatywa, w)

    def akcja(self):
        if randrange(0, self.__ZolwDzielnik) < self.__ZolwSzanse:
            super().akcja()

    def nazwa(self):
        return "Zolw"

    def rysowanie(self):
        return "green4"

    def klonuj(self, ws):
        klon = Zolw(ws)
        klon.setSwiat(self._swiat)
        klon.setWiek(Organizm.NOWORODEK)
        return klon

    def _czyMozeUciec(self):
        return False

    def _czyOdbilAtak(self, atakujacy):
        return atakujacy.getSila() < self.__ZolwOdparcie

    def _czyDobryWech(self):
        return False

    def _czyEksterminuje(self):
        return False