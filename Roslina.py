from Organizm import *
from random import randrange

class Roslina(Organizm, metaclass=ABCMeta):
    __RozmnozDzielnik = 20
    __RozmnozSzansa = 1

    def __init__(self, ws, s, w=0):
        super().__init__(ws, s, 0, w)

    def akcja(self):
        if randrange(0, self.__RozmnozDzielnik) < self.__RozmnozSzansa and self._wiek > Organizm.NOWORODEK:
            obok = self._swiat.getWolneObok(self._polozenie)
            if self._polozenie.x != obok.x or self._polozenie.y != obok.y:
                nowa = self.klonuj(obok)
                self._swiat.dodajOrganizm(nowa)
                zdarzenie = f"Nowa roslina: {self.nazwa()} ({obok.x}, {obok.y})"
                self._swiat.dodajZdarzenie(zdarzenie)

    def kolizja(self):
        pass

    def reakcja(self, drugi):
        pass

    def zmienStatusRozmnozenia(self):
        pass

    def getCzySmiercionosna(self):
        return self._czySmiercionosna()

    @abstractmethod
    def _czySmiercionosna(self):
        pass
