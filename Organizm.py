from abc import ABCMeta, abstractmethod
from Wspolrzedne import *

class Organizm(metaclass=ABCMeta):
    NOWORODEK = -1
    _zycie = True
    _poRozmnozeniu = False
    _swiat = None

    def __init__(self, ws, s, i, w=0):
        self._polozenie = ws
        self._poprzednie = ws
        self._sila = s
        self._inicjatywa = i
        self._wiek = w

    @abstractmethod
    def akcja(self):
        pass

    @abstractmethod
    def kolizja(self):
        pass

    @abstractmethod
    def rysowanie(self):
        pass

    @abstractmethod
    def nazwa(self):
        pass

    def getSila(self):
        return self._sila

    def getInicjatywa(self):
        return self._inicjatywa

    def getWiek(self):
        return self._wiek

    def getPolozenie(self):
        return self._polozenie

    def getPoprzednie(self):
        return self._poprzednie

    def getZycie(self):
        return self._zycie

    def getSwiat(self):
        return self._swiat

    def getPoRozmnozeniu(self):
        return self._poRozmnozeniu

    def setSila(self, s):
        self._sila = s

    def setWiek(self, w):
        self._wiek = w

    def setMartwy(self):
        self._zycie = False

    def setSwiat(self, sw):
        self._swiat = sw

    def setRozmnozylSie(self):
        self._poRozmnozeniu = True

    def zwiekszWiek(self):
        self._wiek += 1

    @abstractmethod
    def zmienStatusRozmnozenia(self):
        pass

    @abstractmethod
    def klonuj(self, ws):
        pass

    def getCzyDoEksterminacji(self):
        return self._czyDoEksterminacji()

    @abstractmethod
    def _czyDoEksterminacji(self):
        pass
