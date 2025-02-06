'''**********************************************
nazwa funkcji: nwd
opis funkcji: Funkcja sprawdza największy wspólny dzielnik dwóch liczb całkowitych.
parametry: a- pierwsza liczba
           b- druga liczba
zwracany typ i opis: Funkcja zwraca największy wspólny dzielnik w zmiennej typu int.
autor: Ola Owczarz
***********************************************'''

def nwd(a, b):
    while a!= b:
        if a>b:
            a = a-b
        else:
            b= b-a
    return a

print(nwd(18,27))
