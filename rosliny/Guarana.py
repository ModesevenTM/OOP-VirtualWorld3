from Roslina import *


class Guarana(Roslina):
    __GuaranaSila = 0
    __GuaranaKolizja = 3

    def __init__(self, ws, w = 0):
        super().__init__(ws, self.__GuaranaSila, w)

    def reakcja(self, drugi):
        zdarzenie = f"{drugi.nazwa()} ({drugi.getPolozenie().x}, {drugi.getPolozenie().y}) - sila: {drugi.getSila()}->{drugi.getSila() + self.__GuaranaKolizja}"
        self._swiat.dodajZdarzenie(zdarzenie)
        drugi.setSila(drugi.getSila() + self.__GuaranaKolizja)

    def nazwa(self):
        return "Guarana"

    def rysowanie(self):
        return "red"

    def klonuj(self, ws):
        klon = Guarana(ws)
        klon.setSwiat(self._swiat)
        klon.setWiek(Organizm.NOWORODEK)
        return klon

    def _czySmiercionosna(self):
        return False

    def _czyDoEksterminacji(self):
        return False