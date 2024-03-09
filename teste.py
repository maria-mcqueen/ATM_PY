from domeniu import creeazaTranzactie, getZiua, getSuma, getTipul, getNr, setZiua, setSuma, setTipul, setNr
from operatii import adaugaTranzactie, modificaTranzactie, stergeTranzactieDupaZi, \
    tranzactiiCuSumaMaiMareDecatoSumaData, tranzactiiDeoZi, stergeTranzactiiDupaTip, stergeTranzactiidinInterval, \
    tranzactiiTip, sumaTotalaDeUnAnumitTip, stergeTranzactiiMaiMiciDetip, ordonare, soldulContuluiLaoData


def testCreeazaTranzactie():
    tranzactie = creeazaTranzactie(1, 1, "retragere", 1)
    assert getZiua(tranzactie) == 1
    assert getSuma(tranzactie) == 1
    assert getTipul(tranzactie) == "retragere"
    assert getNr(tranzactie) == 1


def testSetteri():
    tranzactie = creeazaTranzactie(1, 1, "retragere", 1)

    setZiua(tranzactie, 1)
    assert getZiua(tranzactie) == 1

    setSuma(tranzactie, 1)
    assert getSuma(tranzactie) == 1

    setTipul(tranzactie, "retragere")
    assert getTipul(tranzactie) == "retragere"

    setNr(tranzactie, 1)
    assert getNr(tranzactie) == 1


def testAdaugaTranzactie():
    listaTranzactii = []
    ziua = 1
    suma = 1
    tipul = "retragere"
    nr = 1

    adaugaTranzactie(ziua, suma, tipul, nr, listaTranzactii)

    assert (len(listaTranzactii) == 1)
    tranzactie = listaTranzactii[0]
    assert getZiua(tranzactie) == 1
    assert getSuma(tranzactie) == 1
    assert getTipul(tranzactie) == "retragere"
    assert getNr(tranzactie) == 1


def testModificaTranzactie():
    listaTranzactii = []
    ziuaNoua = 2
    sumanoua = 2
    tipulNou = "depunere"
    adaugaTranzactie(1, 1, "retragere", 1, listaTranzactii)
    adaugaTranzactie(2, 2, "depunere", 2, listaTranzactii)

    modificaTranzactie(ziuaNoua, sumanoua, tipulNou, 1, listaTranzactii)

    assert (len(listaTranzactii) == 2)

    assert (getZiua(listaTranzactii[0]) == ziuaNoua)
    assert (getSuma(listaTranzactii[0]) == sumanoua)
    assert (getTipul(listaTranzactii[0]) == tipulNou)

    assert (getZiua(listaTranzactii[1]) == 2)
    assert (getSuma(listaTranzactii[1]) == 2)
    assert (getTipul(listaTranzactii[1]) == "depunere")
    assert (getNr(listaTranzactii[1]) == 2)


def teststergeTranzactieDupaZi():
    listaTranzactii = []
    adaugaTranzactie(1, 1, "retragere", 1, listaTranzactii)
    adaugaTranzactie(2, 2, "depunere", 2, listaTranzactii)

    stergeTranzactieDupaZi(2, listaTranzactii)

    assert (len(listaTranzactii) == 1)
    assert (getZiua(listaTranzactii[0]) == 1)


def testtranzactiiCuSumaMaiMareDecatoSumaData():
    listaTranzactii = []
    adaugaTranzactie(1, 70, "retragere", 1, listaTranzactii)
    adaugaTranzactie(2, 20, "depunere", 2, listaTranzactii)

    rezultat = tranzactiiCuSumaMaiMareDecatoSumaData(40, listaTranzactii)

    assert (len(rezultat) == 1)

def testSold():
    listaTranzactii = []
    adaugaTranzactie(1, 20, "retragere", 1, listaTranzactii)
    adaugaTranzactie(2, 70, "depunere", 2, listaTranzactii)

    rezultat = soldulContuluiLaoData(2,listaTranzactii)

    assert (rezultat == 1)

def testtranzactiiDeoZi():
    listaTranzactii = []
    adaugaTranzactie(1, 70, "retragere", 1, listaTranzactii)
    adaugaTranzactie(2, 20, "depunere", 2, listaTranzactii)

    rezultat = tranzactiiDeoZi(3, 50, listaTranzactii)

    assert (len(rezultat) == 1)


def teststergeTranzactiiDupaTip():
    listaTranzactii = []
    adaugaTranzactie(1, 1, "retragere", 1, listaTranzactii)
    adaugaTranzactie(2, 2, "depunere", 2, listaTranzactii)

    stergeTranzactiiDupaTip("retragere", listaTranzactii)

    assert (len(listaTranzactii) == 1)
    assert (getZiua(listaTranzactii[0]) == 2)


def teststergeTranzactiidinInterval():
    listaTranzactii = []
    adaugaTranzactie(2, 2, "retragere", 2, listaTranzactii)
    adaugaTranzactie(4, 4, "depunere", 4, listaTranzactii)

    ziMin = 1
    ziMax = 3
    stergeTranzactiidinInterval(ziMin, ziMax, listaTranzactii)

    assert (len(listaTranzactii) == 1)
    assert (getZiua(listaTranzactii[0]) == 4)


def testtranzactiiTip():
    listaTranzactii = []
    adaugaTranzactie(1, 1, "retragere", 1, listaTranzactii)
    adaugaTranzactie(2, 2, "depunere", 2, listaTranzactii)

    rezultat = tranzactiiTip("retragere", listaTranzactii)

    assert (len(rezultat) == 1)


def testsumaTotalaDeUnAnumitTip():
    listaTranzactii = []
    adaugaTranzactie(1, 70, "retragere", 1, listaTranzactii)
    adaugaTranzactie(2, 20, "depunere", 2, listaTranzactii)

    suma = sumaTotalaDeUnAnumitTip("retragere", listaTranzactii)

    assert (suma == 70)


def teststergeTranzactiiMaiMiciDetip():
    rezultat=[]
    listaTranzactii = []
    adaugaTranzactie(1, 20, "retragere", 1, listaTranzactii)
    adaugaTranzactie(2, 70, "depunere", 2, listaTranzactii)

    rezultat = stergeTranzactiiMaiMiciDetip("retragere", 40, listaTranzactii)

    assert (len(rezultat) == 1)

def testordonare():
    listaTranzactii = []
    adaugaTranzactie(1, 20, "retragere", 1, listaTranzactii)
    adaugaTranzactie(2, 70, "depunere", 2, listaTranzactii)

    rezultat = ordonare("depunere", listaTranzactii)

    assert(len(rezultat) == 1)



def testAll():
    testCreeazaTranzactie()
    testSetteri()
    testAdaugaTranzactie()
    testModificaTranzactie()
    teststergeTranzactieDupaZi()
    testtranzactiiCuSumaMaiMareDecatoSumaData()
    testtranzactiiDeoZi()
    teststergeTranzactiiDupaTip()
    teststergeTranzactiidinInterval()
    testtranzactiiTip()
    testsumaTotalaDeUnAnumitTip()
    testordonare()

