def tranzactiiDeoZi(ziua, suma, listaTranzactii):
    '''
    tipareste tranzactiile efectuate inainte de o zi si mai mari decat o suma data
    :param ziua: nr natural
    :param suma: float
    :param listaTranzactii: lista de dictionare de tip tranzactii
    :return: lista de dictionare de tip tranzactie
    '''

    rezultat = []
    for tranzactie in listaTranzactii:
        if getZiua(tranzactie) < ziua and getSuma(tranzactie) > suma:
                rezultat.append(tranzactie)
    return rezultat

def main():
    listaTranzactii=[1, 20, "retragere", 1]



main()