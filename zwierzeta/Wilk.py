from Zwierze import *


class Wilk(Zwierze):
    WilkSila = 9
    __WilkInicjatywa = 5

    def __init__(self, ws, s=WilkSila, w=0):
        super().__init__(ws, s, self.__WilkInicjatywa, w)

    def nazwa(self):
        return "Wilk"

    def rysowanie(self):
        return "dim gray"

    def klonuj(self, ws):
        klon = Wilk(ws)
        klon.setSwiat(self._swiat)
        klon.setWiek(Organizm.NOWORODEK)
        return klon

    def _czyMozeUciec(self):
        return False

    def _czyOdbilAtak(self, atakujacy):
        return False

    def _czyDobryWech(self):
        return False

    def _czyEksterminuje(self):
        return False