from domeniu import toString
from operatii import adaugaTranzactie, modificaTranzactie, stergeTranzactieDupaZi, stergeTranzactiiDupaTip, \
    stergeTranzactiidinInterval, tranzactiiCuSumaMaiMareDecatoSumaData, tranzactiiDeoZi, tranzactiiTip, \
    sumaTotalaDeUnAnumitTip, stergeTranzactiiMaiMiciDetip, soldulContuluiLaoData, ordonare


def printMenu():
    print("1. Adauga tranzactie {ziua} {suma} {tipul} {nr}")
    print("2. Modifica tranzactie {ziuaNoua} {sumaNoua} {tipulNou} {nr}")
    print("3. Sterge tranzactie dupa zi {ziua}")
    print("4. Sterge tranzactie dupa tip {tipul}")
    print("5. Sterge tranzactie din interval de zile {ziMin} {ziMax}")
    print("6. Afiseaza tranzactiile cu suma mai mare decat o suma data {suma}")
    print("7. Tipareste tranzactiile efectuate inainte de o zi si mai mari decat o suma data {suma} {ziua}")
    print("8. Tipareste tranzactiile de un anumit tip {tipul}")
    print("9. Tipareste suma tranzactiilor de un anumit tip {tipul}")
    print("10.Sterge tranzactiile mai mici decat o suma data si care au tipul specificat {suma} {tipul}")
    print("11.Soldul contului la o data anume {ziua}")
    print("12.Afiseaza tranzactiile de un anumit tip ordonat dupa suma {tipul}")
    print("a. Afiseaza tranzactiile")
    print("13.Undo")
    print("x. Iesire")


def printTranzactii(listaTranzactii):
    for tranzactie in listaTranzactii:
        print(toString(tranzactie))


def uiAdaugaTranactie(listaTranzactii, comanda):
    try:
        parametri = comanda.split()[1]
        ziua = int(parametri.split(',')[0])
        suma = float(parametri.split(',')[1])
        tipul = parametri.split(',')[2]
        nr = int(parametri.split(',')[3])
        adaugaTranzactie(ziua, suma, tipul, nr, listaTranzactii)
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)


def uiModificaTranzactie(listaTranzactii, comanda):
    try:
        parametri = comanda.split()[1]
        ziua = int(parametri.split(',')[0])
        suma = float(parametri.split(',')[1])
        tipul = parametri.split(',')[2]
        nr = int(parametri.split(',')[3])
        modificaTranzactie(ziua, suma, tipul, nr, listaTranzactii)
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)


def uistergeTranzactieDupaZi(listaTranzactii, comanda):
    try:
        parametri = comanda.split()[1]
        ziua = int(parametri.split()[0])
        stergeTranzactieDupaZi(ziua, listaTranzactii)
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)


def uistergeTranzactiiDupaTip(listaTranzactii, comanda):
    try:
        parametri = comanda.split()[1]
        tipul = parametri.split()[0]
        stergeTranzactiiDupaTip(tipul, listaTranzactii)
    except IndexError as e:
        print(e)


def uistergeTranzactiidinInterval(listaTranzactii, comanda):
    try:
        parametri = comanda.split()[1]
        ziMin = int(parametri.split(',')[0])
        ziMax = int(parametri.split(',')[1])
        return stergeTranzactiidinInterval(ziMin, ziMax, listaTranzactii)
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)


def uitranzactiiCuSumaMaiMareDecatoSumaData(listaTranzactii, comanda):
    try:
        parametri = comanda.split()[1]
        suma = int(parametri.split()[0])
        print(tranzactiiCuSumaMaiMareDecatoSumaData(suma, listaTranzactii))
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)


def uitranzactiiDeoZi(listaTranzactii, comanda):
    try:
        parametri = comanda.split()[1]
        ziua = int(parametri.split(',')[0])
        suma = int(parametri.split(',')[1])
        return tranzactiiDeoZi(ziua, suma, listaTranzactii)
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)


def uitranzactiiTip(listaTranzactii, comanda):
    try:
        parametri = comanda.split()[1]
        tipul = parametri.split()[0]
        return tranzactiiTip(tipul, listaTranzactii)
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)


def uisumaTotalaDeUnAnumitTip(listaTranzactii, comanda):
    try:
        parametri = comanda.split()[1]
        tipul = parametri.split()[0]
        return sumaTotalaDeUnAnumitTip(tipul, listaTranzactii)
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)


def uistergeTranzactiiMaiMiciDetip(listaTranzactii, comanda):
    try:
        parametri = comanda.split()[1]
        suma = int(parametri.split(',')[0])
        tipul = parametri.split(',')[1]
        return stergeTranzactiiMaiMiciDetip(suma, tipul, listaTranzactii)
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)


def uisoldulContuluiLaoData(listaTranzactii, comanda):
    try:
        ziua = int(comanda.split()[1])
        return soldulContuluiLaoData(ziua, listaTranzactii)
    except ValueError as e:
        print(e)

def uiordonare(listaTranzactii,comanda):
    try:
        tipul = comanda.split()[1]
        return ordonare(tipul,listaTranzactii)
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)


def meniu():
    listaTranzactii = []
    listaveche=[]
    while True:
        printMenu()
        comanda = input("Dati comanda: ")
        operatiune = comanda.split()[0]
        if operatiune == "adauga":
            uiAdaugaTranactie(listaTranzactii, comanda)
            listaveche.append(listaTranzactii[:])
        elif operatiune == "modifica":
            uiModificaTranzactie(listaTranzactii, comanda)
            listaveche.append(listaTranzactii[:])
        elif operatiune == "sterge_tranzactie_dupa_zi":
            listaveche.append(listaTranzactii[:])
            uistergeTranzactieDupaZi(listaTranzactii, comanda)
        elif operatiune == "sterge_tranzactie_dupa_tip":
            listaveche.append(listaTranzactii[:])
            uistergeTranzactiiDupaTip(listaTranzactii, comanda)
        elif operatiune == "sterge_tranzactie_din_interval":
            listaveche.append(listaTranzactii[:])
            uistergeTranzactiidinInterval(listaTranzactii, comanda)
        elif operatiune == "tranzactii_cu_suma_mai_mare":
            uitranzactiiCuSumaMaiMareDecatoSumaData(listaTranzactii, comanda)
        elif operatiune == "tranzactii_de_o_zi":
            print(uitranzactiiDeoZi(listaTranzactii, comanda))
        elif operatiune == "tranzactii_tip":
            uitranzactiiTip(listaTranzactii, comanda)
        elif operatiune == "suma_totala_tip":
            print(uisumaTotalaDeUnAnumitTip(listaTranzactii, comanda))
        elif operatiune == "sterge_tranzactii_mai_mici":
            listaveche.append((listaTranzactii[:]))
            uistergeTranzactiiMaiMiciDetip(listaTranzactii, comanda)
        elif operatiune == "soldul_contului":
            print(uisoldulContuluiLaoData(listaTranzactii, comanda))
        elif operatiune == "ordonare":
            print(uiordonare(listaTranzactii,comanda))
        elif operatiune == "afiseaza":
            printTranzactii(listaTranzactii)
        elif operatiune == "undo":
            try:
                listaTranzactii = listaveche.pop()
            except IndexError as e:
                print(e)
        elif operatiune == "iesire":
            break
        else:
            print("Comanda gresita! Reincercati")