from Zwierze import *


class Owca(Zwierze):
    OwcaSila = 4
    __OwcaInicjatywa = 4

    def __init__(self, ws, s=OwcaSila, w=0):
        super().__init__(ws, s, self.__OwcaInicjatywa, w)

    def nazwa(self):
        return "Owca"

    def rysowanie(self):
        return "light gray"

    def klonuj(self, ws):
        klon = Owca(ws)
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
        return
