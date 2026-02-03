

def contare(n):
    if n==0:
        return 0
    else:
        return n + contare(n-1)


def fattoriale(n):
    if n==0:
        return 1
    else:
        return n*fattoriale(n-1)

def contaParole(stringa):
    if stringa=="":
        return 0
    else:

        return 1+contaParole(stringa[1:])

def sommaLista(n):
    if n==[]:
        return 0
    else:
        return n[-1] + sommaLista(n[:-1])

def find(lista, x):
    if lista == []:
        return False

    if lista[0]==x:
        return True
    else:
        return find(lista[1:], x)

def massimo(lista):

    if len(lista)==1:
        return lista[0]

    if lista[0] > lista[-1]:
        return massimo(lista[:-1])
    else:
        return massimo(lista[1:])






if __name__ == '__main__':
    n=5
    print(contare(n))

    n = 4
    print(fattoriale(n))

    testo = "algoritmi"
    print(contaParole(testo))

    numeri = [3, 7, 2, 5]
    print(sommaLista(numeri))

    numeri = [4, 7, 1, 9, 3]
    x = 9
    print(find(numeri, x))

    num = [8, 3, 10, 2, 7]
    print(massimo(num))