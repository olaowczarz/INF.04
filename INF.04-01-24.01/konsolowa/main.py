pesel = [0, 6, 2, 7, 2, 0, 0, 7, 5, 4, 3]
waga_cyfr = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

user = input("Podaj pesel, oddzielając liczby spacją: ").split()
wprowadzony_pesel = list(map(int, user[:11]))

'''**********************************************
nazwa funkcji: jaka_plec
opis funkcji: Funkcja pobiera 10 pozycje PESELu. Sprawdza czy jest ona parzysta, jesli tak zwraca wartosc 'k', jesli nie zwraca wartosc 'm'.
parametry: brak?
zwracany typ i opis: Funkcja zwraca string w zaleznosci od parzystosci cyfry. 'k' oznacza kobiete, natomiast 'm' mezczyzne.
autor: Ola Owczarz
**********************************************'''

def jaka_plec (pesel):
    if(pesel[9]%2==0):
        return 'K'
    else:
        return 'M'

'''**********************************************
nazwa funkcji: suma_kontrolna
opis funkcji: Funkcja oblicza sumę kontrolną poprzez mnożenie odpowiadających sobie miejscami cyfr i ich wagi oraz je sumuje. Następnie sprawdza czy modulo wyniku jest równe 0.
parametry: brak?
zwracany typ i opis: Funkcja zwraca wartość logiczną true albo false w zależności od modulo z sumy kontrolnej.
autor: Ola Owczarz
**********************************************'''

def suma_kontrolna (pesel):
    s = 0
    for i in range(10):
        s = s + (pesel[i] * waga_cyfr[i])
    m = s%10
    if(m == 0):
        r=0
    else:
        r = 10-m

    if(r == pesel[10]):
        return r == pesel[10]

'''**********************************************
nazwa funkcji: sprawdz
opis funkcji: Funkcja zamienia informacje zwrócone przez ostatnie funkcje na pełne słowa, wyświetla PESEL, płeć oraz poprawność PESELu.
parametry: plec - wartosc zwracana przez funkcje sprawdz_plec
           suma_k - wartosc zwracana przez funkcje sprawdz_sume_kontrolna
zwracany typ i opis: ?
autor: Ola Owczarz
**********************************************'''

def sprawdz(pesel):
    plec = jaka_plec(pesel)
    suma_k = suma_kontrolna(pesel)

    print("Pesel: ", pesel , ': Kobieta' if plec == 'K' else ': Mężczyzna', ". Suma kontrolna jest " ,  'prawidłowa.' if suma_k else 'nieprawidłowa.')

sprawdz(pesel)
