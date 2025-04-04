from Zwierze import *


class Lis(Zwierze):
    LisSila = 3
    __LisInicjatywa = 7

    def __init__(self, ws, s=LisSila, w=0):
        super().__init__(ws, s, self.__LisInicjatywa, w)

    def nazwa(self):
        return "Lis"

    def rysowanie(self):
        return "orange"

    def klonuj(self, ws):
        klon = Lis(ws)
        klon.setSwiat(self._swiat)
        klon.setWiek(Organizm.NOWORODEK)
        return klon

    def _czyMozeUciec(self):
        return False

    def _czyOdbilAtak(self, atakujacy):
        return False

    def _czyDobryWech(self):
        return True

    def _czyEksterminuje(self):
        return False