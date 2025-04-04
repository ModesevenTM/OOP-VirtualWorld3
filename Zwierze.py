from Roslina import *
from random import randrange

class Zwierze(Organizm, metaclass=ABCMeta):
    _zasieg = 1

    def __init(self, ws, s, i, w = 0):
        super().__init__(ws, s, i, w)

    def akcja(self):
        if not self._czyDobryWech() or not self.czyWszyscySilniejsi():
            kierunki = []
            if self._polozenie.x - self._zasieg >= 0:
                kierunki.append(Wspolrzedne(self._polozenie.x - self._zasieg, self._polozenie.y))
            if self._polozenie.x + self._zasieg < self._swiat.getSzerokosc():
                kierunki.append(Wspolrzedne(self._polozenie.x + self._zasieg, self._polozenie.y))
            if self._polozenie.y - self._zasieg >= 0:
                kierunki.append(Wspolrzedne(self._polozenie.x, self._polozenie.y - self._zasieg))
            if self._polozenie.y + self._zasieg < self._swiat.getWysokosc():
                kierunki.append(Wspolrzedne(self._polozenie.x, self._polozenie.y + self._zasieg))

            if len(kierunki) > 0:
                while True:
                    nowe = kierunki[randrange(0, len(kierunki))]
                    self._poprzednie = self._polozenie
                    self._polozenie = nowe
                    if self._czyDobryWech() and self._swiat.getKolizja(self) is not None and self._swiat.getKolizja(self).getSila() > self._sila:
                        self._polozenie = self._poprzednie
                    else:
                        zdarzenie = f"{self.nazwa()} ({self._poprzednie.x},{self._poprzednie.y}) -> ({self._polozenie.x},{self._polozenie.y})"
                        self._swiat.dodajZdarzenie(zdarzenie)
                        break

    def kolizja(self):
        kolidujacy = self._swiat.getKolizja(self)
        if kolidujacy is not None:
            if self.nazwa() == kolidujacy.nazwa():
                self.__rozmnoz(kolidujacy)
            elif isinstance(kolidujacy, Zwierze):
                self.walcz(kolidujacy)
            else:
                self.zjedz(kolidujacy)

    def walcz(self, kolidujacy):
        if not self._ucieknij() and not kolidujacy.getUcieknij():
            if self._sila < kolidujacy.getSila():
                if self._czyOdbilAtak(kolidujacy):
                    kolidujacy._polozenie = kolidujacy.getPoprzednie()
                else:
                    zdarzenie = f"{kolidujacy.nazwa()} zabil {self.nazwa()} ({self._polozenie.x}, {self._polozenie.y})"
                    self._swiat.dodajZdarzenie(zdarzenie)
                    self.setMartwy()
            else:
                if kolidujacy.getCzyOdbilAtak(self):
                    self._polozenie = self._poprzednie
                else:
                    zdarzenie = f"{self.nazwa()} zabil {kolidujacy.nazwa()} ({self._polozenie.x}, {self._polozenie.y})"
                    self._swiat.dodajZdarzenie(zdarzenie)
                    kolidujacy.setMartwy()

    def zjedz(self, kolidujacy):
        if kolidujacy.getZycie():
            kolidujacy.reakcja(self)
            kolidujacy.setMartwy()
            zdarzenie = f"{self.nazwa()} zjadl {kolidujacy.nazwa()} ({self._polozenie.x}, {self._polozenie.y})"
            self._swiat.dodajZdarzenie(zdarzenie)
            if kolidujacy.getCzySmiercionosna() and not (self._czyEksterminuje() and kolidujacy.getCzyDoEksterminacji()):
                zdarzenie = f"{kolidujacy.nazwa()} zabil {self.nazwa()} ({self._polozenie.x}, {self._polozenie.y})"
                self._swiat.dodajZdarzenie(zdarzenie)
                self.setMartwy()

    def czyWszyscySilniejsi(self):
        mozliwosci = [
            Wspolrzedne(self._polozenie.x - 1, self._polozenie.y),
            Wspolrzedne(self._polozenie.x + 1, self._polozenie.y),
            Wspolrzedne(self._polozenie.x, self._polozenie.y - 1),
            Wspolrzedne(self._polozenie.x, self._polozenie.y + 1),
        ]
        for ws in mozliwosci:
            pozycja = self._swiat.getZajete(ws)
            if pozycja is not self and (pozycja is None or pozycja.getSila() <= self._sila):
                return False
        return True

    def zmienStatusRozmnozenia(self):
        self._poRozmnozeniu = False

    @abstractmethod
    def _czyOdbilAtak(self, atakujacy):
        pass

    @abstractmethod
    def _czyMozeUciec(self):
        pass

    @abstractmethod
    def _czyDobryWech(self):
        pass

    def _czyDoEksterminacji(self):
        return False

    def _ucieknij(self):
        if self._czyMozeUciec():
            ucieczka = self._swiat.getWolneObok(self._polozenie)
            if ucieczka.x != self._polozenie.x or ucieczka.y != self._polozenie.y:
                zdarzenie = f"{self.nazwa()} uciekl [({self._polozenie.x},{self._polozenie.y})->({ucieczka.x},{ucieczka.y})]"
                self._polozenie = ucieczka
                self._swiat.dodajZdarzenie(zdarzenie)
                return True
        return False

    def __rozmnoz(self, rodzic):
        if rodzic.getWiek() > Organizm.NOWORODEK:
            self._polozenie = self._poprzednie
            wolne = self._swiat.getWolneObok(rodzic.getPolozenie())
            if (wolne.x != rodzic.getPolozenie().x or wolne.y != rodzic.getPolozenie().y) and not self._poRozmnozeniu and not rodzic.getPoRozmnozeniu():
                dziecko = self.klonuj(wolne)
                self._swiat.dodajOrganizm(dziecko)
                zdarzenie = f"Nowe zwierze: {self.nazwa()} ({wolne.x}, {wolne.y})"
                self._swiat.dodajZdarzenie(zdarzenie)
                self._poRozmnozeniu = True
                rodzic.setRozmnozylSie()

    def getCzyOdbilAtak(self, atakujacy):
        return self._czyOdbilAtak(atakujacy)

    def getCzyMozeUciec(self):
        return self._czyMozeUciec()

    def getCzyDobryWech(self):
        return self._czyDobryWech()

    def getUcieknij(self):
        return self._ucieknij()

    def getCzyEksterminuje(self):
        return self._czyEksterminuje()

    @abstractmethod
    def _czyEksterminuje(self):
        pass
