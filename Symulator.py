import turtle
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.messagebox import showinfo

from Swiat import Swiat
from Wspolrzedne import Wspolrzedne
from rosliny.BarszczSosnowskiego import *
from rosliny.Guarana import *
from rosliny.Mlecz import *
from rosliny.Trawa import *
from rosliny.WilczeJagody import *
from zwierzeta.Antylopa import *
from zwierzeta.CyberOwca import *
from zwierzeta.Czlowiek import *
from zwierzeta.Lis import *
from zwierzeta.Owca import *
from zwierzeta.Wilk import *
from zwierzeta.Zolw import *


class Symulator:
    __MinWymiar = 10
    __MaxWymiar = 40
    __InitOrganizm = -2

    def __init__(self):
        self.__screen = turtle.Screen()
        turtle.title("Jakub Wojtkowiak, 193546")
        self.__screen.setup(1280, 720)
        while True:
            try:
                self.__x = int(turtle.textinput("Symulator", "Wpisz szerokosc <10, 40>"))
                if 10 <= self.__x <= 40:
                    break
            except:
                pass
        while True:
            try:
                self.__y = int(turtle.textinput("Symulator", "Wpisz wysokosc <10, 40>"))
                if 10 <= self.__y <= 40:
                    break
            except:
                pass
        self.__wypelnijPola(self.__x, self.__y)
        self.__swiat = Swiat(self.__x, self.__y)
        self.__generujSwiat()
        self.__rysujInterfejs()
        self.__rysowanie()
        self.__screen.listen()
        self.__screen.onkey(lambda: self.__zmienKierunekRuchu(Kierunki.gora), "Up")
        self.__screen.onkey(lambda: self.__zmienKierunekRuchu(Kierunki.dol), "Down")
        self.__screen.onkey(lambda: self.__zmienKierunekRuchu(Kierunki.lewo), "Left")
        self.__screen.onkey(lambda: self.__zmienKierunekRuchu(Kierunki.prawo), "Right")
        self.__screen.mainloop()

    def __wypelnijPola(self, x, y):
        self.__pola = []
        canvas = self.__screen.getcanvas()
        for i in range(y):
            self.__pola.append([])
            for j in range(x):
                przycisk = Button(canvas.master, bg="white", command=lambda i=i, j=j: self.__aktywujPole(j, i))
                przycisk.pack()
                przycisk.place(x=10 + 15 * j, y=10 + 15 * i, width=15, height=15)
                self.__pola[i].append(przycisk)

    def __aktywujPole(self, x, y):
        if self.__swiat.getZajete(Wspolrzedne(x, y)) is None:
            menu = Tk()
            menu.title('Wybór organizmu')
            menu.geometry('500x250')
            ttk.Label(menu, text="Wybierz organizm",
                      background='green', foreground="white",
                      font=("Times New Roman", 15)).grid(row=0, column=1)
            ttk.Label(menu, text="Wybierz:",
                      font=("Times New Roman", 10)).grid(column=0,
                                                         row=5, padx=10, pady=25)
            tekst = StringVar(menu)
            organizm = ttk.Combobox(menu, width=27, textvariable=tekst)
            organizm['values'] = ("Barszcz Sosnowskiego",
                                "Guarana",
                                "Mlecz",
                                "Trawa",
                                "Wilcze jagody",
                                "Antylopa",
                                "CyberOwca",
                                "Lis",
                                "Owca",
                                "Wilk",
                                "Zolw")
            organizm.grid(column=1, row=5)
            organizm.current(0)

            przycisk = Button(menu, text="OK", command=lambda: [self.__dodajOrganizm(tekst.get(), x, y, self.__InitOrganizm, 0), menu.destroy(), self.__rysowanie()])
            przycisk.grid(column=1, row=7)

            menu.mainloop()

    def __dodajOrganizm(self, nazwa, x, y, sila, wiek):
        nowy = None
        if nazwa == "Barszcz Sosnowskiego":
            nowy = BarszczSosnowskiego(Wspolrzedne(x, y), wiek)
        elif nazwa == "Guarana":
            nowy = Guarana(Wspolrzedne(x, y), wiek)
        elif nazwa == "Mlecz":
            nowy = Mlecz(Wspolrzedne(x, y), wiek)
        elif nazwa == "Trawa":
            nowy = Trawa(Wspolrzedne(x, y), wiek)
        elif nazwa == "Wilcze jagody":
            nowy = WilczeJagody(Wspolrzedne(x, y), wiek)
        elif nazwa == "Antylopa":
            nowy = Antylopa(Wspolrzedne(x, y), Antylopa.AntylopaSila, wiek)
        elif nazwa == "CyberOwca":
            nowy = CyberOwca(Wspolrzedne(x, y), CyberOwca.CyberOwcaSila, wiek)
        elif nazwa == "Czlowiek":
            nowy = Czlowiek(Wspolrzedne(x, y), Czlowiek.CzlowiekSila, wiek)
            self.__swiat.setZycieCzlowieka(True)
            self.__ruchCzlowieka.configure(state="normal")
        elif nazwa == "Lis":
            nowy = Lis(Wspolrzedne(x, y), Lis.LisSila, wiek)
        elif nazwa == "Owca":
            nowy = Owca(Wspolrzedne(x, y), Owca.OwcaSila, wiek)
        elif nazwa == "Wilk":
            nowy = Wilk(Wspolrzedne(x, y), Wilk.WilkSila, wiek)
        elif nazwa == "Zolw":
            nowy = Zolw(Wspolrzedne(x, y), Zolw.ZolwSila, wiek)
        if nowy is not None:
            if sila != self.__InitOrganizm:
                nowy.setSila(sila)
            self.__swiat.dodajOrganizm(nowy)

    def __generujSwiat(self):
        pozycja = Wspolrzedne(0, 0)
        szablony = [
            BarszczSosnowskiego(pozycja),
            Guarana(pozycja),
            Mlecz(pozycja),
            Trawa(pozycja),
            WilczeJagody(pozycja),
            Antylopa(pozycja),
            CyberOwca(pozycja),
            Lis(pozycja),
            Owca(pozycja),
            Wilk(pozycja),
            Zolw(pozycja)
        ]
        for i in range(len(szablony)*3):
            while True:
                pozycja = Wspolrzedne(randrange(0, self.__swiat.getSzerokosc()),
                                      randrange(0, self.__swiat.getWysokosc()))
                if self.__swiat.getZajete(pozycja) is None:
                    break
            org = szablony[i % len(szablony)].klonuj(pozycja)
            org.setWiek(0)
            self.__swiat.dodajOrganizm(org)
        while True:
            pozycja = Wspolrzedne(randrange(0, self.__swiat.getSzerokosc()),
                                  randrange(0, self.__swiat.getWysokosc()))
            if self.__swiat.getZajete(pozycja) is None:
                break
        self.__swiat.dodajOrganizm(Czlowiek(pozycja))

    def __rysujPlansze(self):
        for organizm in self.__swiat.getOrganizmy():
            self.__pola[organizm.getPolozenie().y][organizm.getPolozenie().x].configure(bg=organizm.rysowanie())

    def __rysowanie(self):
        if self.__swiat.getZycieCzlowieka():
            self.__ruchCzlowieka.configure(background="black")
            if self.__swiat.getTura() + 1 >= self.__swiat.getKiedyUmiejetnosc() + 2 * Czlowiek.CzlowiekWzrost:
                self.__elixir.configure(state="normal")
        else:
            self.__ruchCzlowieka.configure(background="white")
            self.__elixir.configure(state="disabled")
        self.__nrTury.configure(text=f"Tura nr. {self.__swiat.getTura()+1}")
        self.__wyczyscPrzyciski()
        self.__rysujPlansze()
        self.__wyswietlDziennikTejTury()

    def __wyczyscPrzyciski(self):
        for i in range(self.__swiat.getWysokosc()):
            for j in range(self.__swiat.getSzerokosc()):
                self.__pola[i][j].configure(bg="white")

    def __wyswietlDziennikTejTury(self):
        self.__dziennik['state'] = 'normal'
        self.__dziennik.delete(1.0, END)
        zdarzenia = self.__swiat.getZdarzenia()
        if len(zdarzenia) > 0:
            for i in range(len(zdarzenia) + 1):
                if i == 0:
                    self.__dziennik.insert(END, f"W turze {self.__swiat.getTura()}:\n")
                else:
                    self.__dziennik.insert(END, f"{zdarzenia[i - 1]}\n")
        else:
            self.__dziennik.insert(END, "Brak wydarzeń w poprzedniej turze.")
        self.__dziennik['state'] = 'disabled'

    def __graj(self):
        self.__swiat.nowaTura()
        self.__ruchCzlowieka.configure(text="Człowiek nie ruszy się")
        self.__rysowanie()

    def __rysujInterfejs(self):
        canvas = self.__screen.getcanvas()
        load = Button(canvas.master, text="Wczytaj", command=self.__odczyt)
        load.pack()
        load.place(x=850, y=10, width=100, height=40)
        save = Button(canvas.master, text="Zapisz grę", command=self.__zapis)
        save.pack()
        save.place(x=850, y=60, width=100, height=40)
        legend = Button(canvas.master, text="Legenda", command=self.__wyswietlLegende)
        legend.pack()
        legend.place(x=850, y=110, width=100, height=40)
        proceed = Button(canvas.master, text="Zatwierdź", command=self.__graj)
        proceed.pack()
        proceed.place(x=850, y=160, width=100, height=40)
        exit = Button(canvas.master, text="Wyjdź", command=self.__screen.bye)
        exit.pack()
        exit.place(x=850, y=210, width=100, height=40)
        self.__elixir = Button(canvas.master, text="Eliksir", command=lambda: [self.__swiat.uzyjUmiejetnosci(), self.__elixir.configure(state="disabled")])
        self.__elixir.pack()
        self.__elixir.place(x=850, y=260, width=100, height=40)
        self.__ruchCzlowieka = ttk.Label(canvas.master, text="Człowiek nie ruszy się",
                  background='black', foreground="white")
        self.__ruchCzlowieka.place(x=850, y=320)
        self.__nrTury = ttk.Label(canvas.master,
                  background='black', foreground="white")
        self.__nrTury.place(x=850, y=340)
        frame = Frame(canvas.master)
        self.__dziennik = Text(frame, fg="white", bg="black", state="disabled")
        self.__dziennik.pack(side=LEFT,expand=True)
        sb = Scrollbar(frame)
        sb.pack(side=RIGHT, fill=BOTH)

        self.__dziennik.config(yscrollcommand=sb.set)
        sb.config(command=self.__dziennik.yview)

        frame.pack(expand=True)
        frame.place(x=700, y=400, width=250, height=250)

    def __odczyt(self):
        filetypes = (('Plik zapisu', '*.sav'),
               ('Wszystkie pliki', '*.*')
        )
        filename = filedialog.askopenfilename(
                title='Wybierz plik',
                initialdir='/',
                filetypes=filetypes)
        if filename == "":
            showinfo(title="Błąd",message="Nie wybrano żadnego pliku.")
        else:
            try:
                plik = open(filename, "r")
                config = plik.readline().strip().split(" ")
                for i in range(self.__swiat.getWysokosc()):
                    for j in range(self.__swiat.getSzerokosc()):
                        self.__pola[i][j].destroy()
                self.__screen.update()
                self.__swiat.setSzerokosc(int(config[0]))
                self.__swiat.setWysokosc(int(config[1]))
                self.__swiat.setTura(int(config[2]))
                self.__swiat.setKiedyUmiejetnosc(int(config[3]))
                self.__swiat.wyczyscZdarzenia()
                self.__swiat.usunWszystkie()
                self.__swiat.setZycieCzlowieka(False)
                self.__ruchCzlowieka.configure(state="disabled")
                self.__wypelnijPola(self.__swiat.getSzerokosc(), self.__swiat.getWysokosc())
                for linia in plik:
                    elem = linia.strip().split(";")
                    if len(elem) != 5:
                        break
                    x = int(elem[1])
                    y = int(elem[2])
                    sila = int(elem[3])
                    wiek = int(elem[4])
                    self.__dodajOrganizm(elem[0], x, y, sila, wiek)
                plik.close()
                self.__rysowanie()
            except:
                pass

    def __zapis(self):
        filetypes = (('Plik zapisu', '*.sav'),
                     ('Wszystkie pliki', '*.*')
                     )
        filename = filedialog.asksaveasfilename(
            title='Wybierz miejsce zapisu i nazwę pliku',
            initialdir='.',
            filetypes=filetypes)
        if filename == "":
            showinfo(title="Błąd", message="Nie wybrano żadnego pliku.")
        else:
            try:
                if not filename.endswith(".sav"):
                    filename += ".sav"
                plik = open(filename, "w")
                plik.write(f"{self.__swiat.getSzerokosc()} {self.__swiat.getWysokosc()} {self.__swiat.getTura()} {self.__swiat.getKiedyUmiejetnosc()}\n")
                organizmy = self.__swiat.getOrganizmy()
                for i in range(len(organizmy)):
                    plik.write(f"{organizmy[i].nazwa()};{organizmy[i].getPolozenie().x};{organizmy[i].getPolozenie().y};{organizmy[i].getSila()};{organizmy[i].getWiek()}\n")
                plik.close()
            except:
                pass

    def __wyswietlLegende(self):
        showinfo(title="Legenda", message="""Kolory organizmów:
- kremowy: Barszcz Sosnowskiego
- czerwony: Guarana
- żółty: Mlecz
- zielony: Trawa
- magenta: Wilcze jagody
- brązowy: Antylopa
- niebieski: CyberOwca
- czarny: Człowiek
- pomarańczowy: Lis
- jasnoszary: Owca
- ciemnoszary: Wilk
- ciemnozielony: Żółw""")

    def __zmienKierunekRuchu(self, kierunek):
        self.__swiat.setRuchCzlowieka(kierunek)
        self.__ruchCzlowieka.configure(text=f"Ruch człowieka: {self.__swiat.getNazwaRuchu()}")
