def creeazaTranzactie(ziua, suma, tipul, nr):
    '''
    creeaza un dictionar de tipul tranzactie
    :param ziua: nr. natural
    :param suma: float
    :param tipul: string
    :param nr: nr. natural
    :return: un dicitonar de tipul tranzactie
    '''
    return {
        "ziua": ziua,
        "suma": suma,
        "tipul": tipul,
        "nr": nr
    }


def getZiua(tranzactie):
    return tranzactie["ziua"]


def getSuma(tranzactie):
    return tranzactie["suma"]


def getTipul(tranzactie):
    return tranzactie["tipul"]


def getNr(tranzactie):
    return tranzactie["nr"]


def setZiua(tranzactie, ziua):
    tranzactie["ziua"] = ziua


def setSuma(tranzactie, suma):
    tranzactie["suma"] = suma


def setTipul(tranzactie, tipul):
    tranzactie["tipul"] = tipul


def setNr(tranzactie, nr):
    tranzactie["nr"] = nr


def toString(tranzactie):
    return "Ziua: " + str(getZiua(tranzactie)) + ", suma: " + str(getSuma(tranzactie)) + \
           ", tipul: " + getTipul(tranzactie) + ", NR: " + str(getNr(tranzactie))