class Film:
    def __init__(self, tytul="", liczba_wypozyczen=0):
        self.tytul = tytul[:20]
        self.liczba_wypozyczen = liczba_wypozyczen
    
    def pobierz_liczbę_wypożyczeń(self):
        return self.liczba_wypozyczen

    def inkrementuj_wypozyczenia(self):
        self.liczba_wypozyczen += 1

film = Film()
print("Po inicjalizacji:", film.tytul, film.liczba_wypozyczen)

film.tytul = "Intelstellar"[:20]
print("Po ustawieniu tytułu:", film.tytul)

film.pobierz_liczbę_wypożyczeń()
print("Przed inkrementacją wypożyczeń: ", film.liczba_wypozyczen)
film.inkrementuj_wypozyczenia()
print("Po inkrementacji wypożyczeń:", film.liczba_wypozyczen)
