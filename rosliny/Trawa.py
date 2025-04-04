from Roslina import *


class Trawa(Roslina):
    __TrawaSila = 0

    def __init__(self, ws, w = 0):
        super().__init__(ws, self.__TrawaSila, w)

    def nazwa(self):
        return "Trawa"

    def rysowanie(self):
        return "lawn green"

    def klonuj(self, ws):
        klon = Trawa(ws)
        klon.setSwiat(self._swiat)
        klon.setWiek(Organizm.NOWORODEK)
        return klon

    def _czySmiercionosna(self):
        return False

    def _czyDoEksterminacji(self):
        return False
