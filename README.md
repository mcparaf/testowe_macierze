# generator macierzy

## setup

Zainstaluj zależności: `pip3 install -r requirements.txt`

## używanie

`python3 generate.py <wymiar n> <wymiar m>`

Skrypt wygeneruje 3 pliki: lhs.txt, rhs.txt i result.txt. Dwa pierwsze wyniki zawieraja argumenty mnożenia macierzy a trzeci zawiera wynik.

Każda z macierzy jest podana w następujący sposób:
```
<wymiar n> <wymiar m>
a b c ... n
... [m-2 wierszy]
a b c ... n
```
