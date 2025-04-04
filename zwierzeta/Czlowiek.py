from Zwierze import *
from Kierunki import *


class Czlowiek(Zwierze):
    CzlowiekSila = 5
    __CzlowiekInicjatywa = 4
    CzlowiekWzrost = 5

    def __init__(self, ws, s=CzlowiekSila, w=0):
        super().__init__(ws, s, self.__CzlowiekInicjatywa, w)

    def akcja(self):
        if self._swiat.getTura() - self._swiat.getKiedyUmiejetnosc() <= self.CzlowiekWzrost:
            if self._swiat.getTura() == self._swiat.getKiedyUmiejetnosc():
                zdarzenie = f"{self.nazwa()} ({self._polozenie.x}, {self._polozenie.y}) - sila: {self._sila}->{self._sila + self.CzlowiekWzrost}"
                self._sila += self.CzlowiekWzrost
            else:
                zdarzenie = f"{self.nazwa()} ({self._polozenie.x}, {self._polozenie.y}) - sila: {self._sila}->{self._sila - 1}"
                self._sila -= 1
            self._swiat.dodajZdarzenie(zdarzenie)
        self._poprzednie = self._polozenie
        match self._swiat.getRuchCzlowieka():
            case Kierunki.gora:
                if self._polozenie.y - 1 >= 0:
                    self._polozenie = Wspolrzedne(self._polozenie.x, self._polozenie.y - 1)
            case Kierunki.dol:
                if self._polozenie.y + 1 < self._swiat.getWysokosc():
                    self._polozenie = Wspolrzedne(self._polozenie.x, self._polozenie.y + 1)
            case Kierunki.lewo:
                if self._polozenie.x - 1 >= 0:
                    self._polozenie = Wspolrzedne(self._polozenie.x - 1, self._polozenie.y)
            case Kierunki.prawo:
                if self._polozenie.x + 1 < self._swiat.getSzerokosc():
                    self._polozenie = Wspolrzedne(self._polozenie.x + 1, self._polozenie.y)
        if self._polozenie.x != self._poprzednie.x or self._polozenie.y != self._poprzednie.y:
            zdarzenie = f"{self.nazwa()} ({self._poprzednie.x},{self._poprzednie.y}) -> ({self._polozenie.x},{self._polozenie.y})"
            self._swiat.dodajZdarzenie(zdarzenie)

    def zwiekszWiek(self):
        super().zwiekszWiek()
        self._swiat.setRuchCzlowieka(Kierunki.stoi)

    def setMartwy(self):
        super().setMartwy()
        self._swiat.setZycieCzlowieka(False)

    def nazwa(self):
        return "Czlowiek"

    def rysowanie(self):
        return "black"

    def klonuj(self, ws):
        klon = Czlowiek(ws)
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
