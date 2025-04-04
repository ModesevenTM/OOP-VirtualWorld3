from Roslina import *


class Mlecz(Roslina):
    __MleczSila = 0
    __MleczAkcja = 3

    def __init__(self, ws, w = 0):
        super().__init__(ws, self.__MleczSila, w)

    def akcja(self):
        for i in range(self.__MleczAkcja):
            super().akcja()

    def nazwa(self):
        return "Mlecz"

    def rysowanie(self):
        return "yellow3"

    def klonuj(self, ws):
        klon = Mlecz(ws)
        klon.setSwiat(self._swiat)
        klon.setWiek(Organizm.NOWORODEK)
        return klon

    def _czySmiercionosna(self):
        return False

    def _czyDoEksterminacji(self):
        return False
