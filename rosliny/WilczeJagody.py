from Roslina import *


class WilczeJagody(Roslina):
    __WilczeJagodySila = 0

    def __init__(self, ws, w = 0):
        super().__init__(ws, self.__WilczeJagodySila, w)

    def nazwa(self):
        return "Wilcze jagody"

    def rysowanie(self):
        return "magenta"

    def klonuj(self, ws):
        klon = WilczeJagody(ws)
        klon.setSwiat(self._swiat)
        klon.setWiek(Organizm.NOWORODEK)
        return klon

    def _czySmiercionosna(self):
        return True

    def _czyDoEksterminacji(self):
        return False
