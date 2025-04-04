from Zwierze import *


class BarszczSosnowskiego(Roslina):
    __SosnowskiSila = 10

    def __init__(self, ws, w = 0):
        super().__init__(ws, self.__SosnowskiSila, w)

    def akcja(self):
        for x in range(self._polozenie.x - 1, self._polozenie.x + 2):
            for y in range(self._polozenie.y - 1, self._polozenie.y + 2):
                pozycja = self._swiat.getZajete(Wspolrzedne(x, y))
                if isinstance(pozycja, Zwierze) and pozycja.getZycie() and not pozycja.getCzyEksterminuje():
                    zdarzenie = f"{self.nazwa()}({self._polozenie.x},{self._polozenie.y}) zabil {pozycja.nazwa()}({pozycja.getPolozenie().x},{pozycja.getPolozenie().y})"
                    self._swiat.dodajZdarzenie(zdarzenie)
                    pozycja.setMartwy()
        super().akcja()

    def nazwa(self):
        return "Barszcz Sosnowskiego"

    def rysowanie(self):
        return "khaki1"

    def klonuj(self, ws):
        klon = BarszczSosnowskiego(ws)
        klon.setSwiat(self._swiat)
        klon.setWiek(Organizm.NOWORODEK)
        return klon

    def _czySmiercionosna(self):
        return True

    def _czyDoEksterminacji(self):
        return True
