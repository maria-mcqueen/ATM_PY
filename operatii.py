from domeniu import creeazaTranzactie, getNr, setZiua, setSuma, setTipul, getZiua, getTipul, getSuma


def adaugaTranzactie(ziua, suma, tipul, nr, listaTranzactii):
    '''
    adauga o tranzactie in lista
    :param ziua: nr. natural
    :param suma: float
    :param tipul: string
    :param nr: nr natural
    :param listaTranzactii: lista de dictionare de tipul tranzactie
    :return:
    '''
    tranzactie = creeazaTranzactie(ziua, suma, tipul, nr)
    listaTranzactii.append(tranzactie)


def modificaTranzactie(ziuaNoua, sumaNoua, tipulNou, nr, listaTranzactii):
    '''
    modifica o tranzactie dupa nr
    :param ziuaNoua: nr. natural
    :param sumaNoua: float
    :param tipulNou: string
    :param nr: nr natural
    :param listaTranzactii: lista de dictionare de tip tranzactie
    :return:
    '''
    for tranzactie in listaTranzactii:
        if getNr(tranzactie) == nr:
            setZiua(tranzactie, ziuaNoua)
            setSuma(tranzactie, sumaNoua)
            setTipul(tranzactie, tipulNou)


def stergeTranzactieDupaZi(ziua, listaTranzactii):
    '''
    sterge o carte dupa zi
    :param nr: nr. natural
    :param listaTranzactii: lista de dictionare de tipul tranzazctii
    :return:
    '''

    for tranzactie in listaTranzactii:
        if getZiua(tranzactie) == ziua:
            listaTranzactii.remove(tranzactie)


def stergeTranzactiiDupaTip(tipul, listaTranzactii):
    i = 0
    while i < len(listaTranzactii):
        if getTipul(listaTranzactii[i]) == tipul:
            listaTranzactii.pop(i)
            i = i - 1
        i += 1


def stergeTranzactiidinInterval(ziMin, ziMax, listaTranzactii):
    '''
    gaseste tranzctiile cuprinse intr-un interval de pret dat
    :param ziMin: nr natural
    :param ziMax: nr natural
    :param listaTranzactii: lista de dictionare de tip tranzactii
    :return:
    '''
    for tranzactie in listaTranzactii:
        if ziMin < getZiua(tranzactie) < ziMax:
            listaTranzactii.remove(tranzactie)


'''def sumePreturiPerAutor(listaCarti):

   # calculeaza suma peturilor cartilor fiecarui autor
   # :param listaCarti: lista de dictionare de tipul carte
   # :return: un dicitonar, continand drept chei numele autorilor
    #         si drept valori suma preturilor cartilor lor

    rezultat = {}
    for carte in listaCarti:
        autor = getTipul(carte)
        pret = getNr(carte)
        if autor in rezultat:
            rezultat[autor] += pret
        else:
            rezultat[autor] = pret
    return rezultat'''


def tranzactiiCuSumaMaiMareDecatoSumaData(suma, listaTranzactii):
    '''
    tipareste tranzactiile care au o suma mai mare decat o suma data
    :param suma: float
    :param listaTranzactii: lista de dictionare de tip tranzactii
    :return: lista de dictionare de tip tranzactie
    '''

    rezultat = []
    for tranzactie in listaTranzactii:
        if suma < getSuma(tranzactie):
            rezultat.append(tranzactie)

    return rezultat


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

    '''i = 0
    rezultat=[]
    while i < len(listaTranzactii):
        if getSuma(listaTranzactii[i]) > suma and getZiua(listaTranzactii[i]) < ziua:
            rezultat.append(listaTranzactii[i])
            
        i += 1
    return rezultat'''

def tranzactiiTip(tipul, listaTranzactii):
    '''
    tipareste tranzactiile de un anumit tip
    :param tipul: string
    :param listaTranzactii: lista de dictionare de tip tranzactie
    :return: lista de dictionare de tip tranzactie
    '''
    rezultat = []
    for tranzactie in listaTranzactii:
        if getTipul(tranzactie) == tipul:
            rezultat.append(tranzactie)
    return rezultat


def sumaTotalaDeUnAnumitTip(tipul, listaTranzactii):
    '''
    tipareste suma tranzactiilor de un anumit tip
    :param tipul: string
    :param listaTranzactii: lista de dictionare de tip tranzactie
    :return: suma totala a tranzactiilor
    '''

    suma = 0
    for tranzactie in listaTranzactii:
        if getTipul(tranzactie) == tipul:
            suma = suma + getSuma(tranzactie)
    return suma


def stergeTranzactiiMaiMiciDetip(suma, tipul, listaTranzactii):
    '''
    sterge tranzactiile mai mici decat o suma data si care au tipul specificat
    :param suma:
    :param tipul:
    :param listaTranzactii:lista de dictionare de tip tranzactie
    :return:
    '''
    for tranzactie in listaTranzactii:
        if getTipul(tranzactie) == tipul:
            if getSuma(tranzactie) < suma:
                listaTranzactii.remove(tranzactie)


def soldulContuluiLaoData(ziua, listaTranzactii):
    '''
    afiseaza soldul contului la o data specificata
    :param ziua: nr natural
    :param listaTranzactii: lista de dictionare de tip tranzactie
    :return: o suma reprezentand soldul contului
    '''

    suma = 0
    for tranzactie in listaTranzactii:
        if getZiua(tranzactie) < ziua + 1:
            if getTipul(tranzactie) == "depunere":
                suma = suma + getSuma(tranzactie)
            else:
                suma = suma - getSuma(tranzactie)
    return suma


def ordonare(tipul,listaTranzactii):
    '''
    afiseaza tranzactiile de un anumit tip ordonat dupa suma
    :param tipul: string
    :param listaTranzactii: lista de dictionare de tip tranzactie
    :return:
    '''
    rezultat=[]
    for tranzactie in listaTranzactii:
        if getTipul(tranzactie) == tipul:
            rezultat.append(tranzactie)
    rezultat.sort(key=lambda tranzactie: getSuma(tranzactie))
    return rezultat