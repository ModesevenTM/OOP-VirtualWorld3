from Zwierze import *
from queue import Queue

class CyberOwca(Zwierze):
    CyberOwcaSila = 11
    __CyberOwcaInicjatywa = 4

    def __init__(self, ws, s=CyberOwcaSila, w=0):
        super().__init__(ws, s, self.__CyberOwcaInicjatywa, w)

    def akcja(self):
        czyJestBarszcz = False
        mapa = [[0] * self._swiat.getSzerokosc() for _ in range(self._swiat.getWysokosc())]
        for org in self._swiat.getOrganizmy():
            if org.getCzyDoEksterminacji():
                mapa[org.getPolozenie().y][org.getPolozenie().x] = 1
                czyJestBarszcz = True
        if not czyJestBarszcz:
            super().akcja()
        else:
            wizyty = [[99999] * self._swiat.getSzerokosc() for _ in range(self._swiat.getWysokosc())]
            q = Queue()
            q.put([self._polozenie.x, self._polozenie.y])
            wizyty[self._polozenie.y][self._polozenie.x] = 0
            while not q.qsize() == 0:
                coord = q.get(False)
                if mapa[coord[1]][coord[0]] == 1 and (coord[0] != self._polozenie.x or coord[1] != self._polozenie.y):
                    while not q.qsize() == 0:
                        q.get(False)
                    nx = coord[0]
                    ny = coord[1]
                    while True:
                        if wizyty[ny][nx] == 1:
                            self._poprzednie = self._polozenie
                            self._polozenie = Wspolrzedne(nx, ny)
                            zdarzenie = f"{self.nazwa()} ({self._poprzednie.x},{self._poprzednie.y}) -> ({self._polozenie.x},{self._polozenie.y})"
                            self._swiat.dodajZdarzenie(zdarzenie)
                            return
                        coordX = [1, -1, 0, 0]
                        coordY = [0, 0, 1, -1]
                        for i in range(4):
                            nextX = nx + coordX[i]
                            nextY = ny + coordY[i]
                            if 0 <= nextX < self._swiat.getSzerokosc() and 0 <= nextY < self._swiat.getWysokosc() and \
                                    wizyty[nextY][nextX] == wizyty[ny][nx] - 1:
                                nx = nextX
                                ny = nextY
                                break
                else:
                    coordX = [1, -1, 0, 0]
                    coordY = [0, 0, 1, -1]
                    for i in range(4):
                        nx = coord[0] + coordX[i]
                        ny = coord[1] + coordY[i]
                        if 0 <= nx < self._swiat.getSzerokosc() and 0 <= ny < self._swiat.getWysokosc() and \
                                wizyty[ny][nx] > wizyty[coord[1]][coord[0]] + 1:
                            wizyty[ny][nx] = wizyty[coord[1]][coord[0]] + 1
                            q.put([nx, ny])


    def nazwa(self):
        return "CyberOwca"

    def rysowanie(self):
        return "blue"

    def klonuj(self, ws):
        klon = CyberOwca(ws)
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
        return True
