def intre0si10(l):
    for numar in range(10):
        if numar>=0 or numar<=10:
            return 1
        else: return 0

def subsecvintre0si10(l):
    k=0
    ok=0
    subsecvmax=[]
    for i in range(len(l)):
        if 0<l[i]<10:
            if len(subsecvmax)<len(l):
                subsecvmax.append(l[i])
                k=k+1
                ok=0
        else:
            k=0
            ok=1
    if ok==1:
        for i in range (k):
            subsecvmax.remove(l[len(subsecvmax)])
    return subsecvmax


def serepeta(a,b):
        if(a==b):
            return True
        else: return False


def crescsaurep(l):
    subsec=[]
    i=0
    '''for i in range(len(l)-1):'''
    while i < (len(l)-1):
        if l[i]<l[i+1]:
            subsec.append(l[i])
            i = i+1
        else:
            if i<len(l)-1:
                if l[i-1]==l[i] or l[i-1]==l[i+1] or l[i]==l[i+1]:
                    subsec.append(l[i])
                    subsec.append(l[i+1])
                    '''subsec.append(l[i+2])'''
                    i=i+2
                else: i=i+1
    return subsec

def citireLista():
    l = []
    n = int(input('Dati nr. de elemente: '))
    for i in range(n):
        l.append(int(input()))
    return l

def printMenu():
    print("1. Citire lista")
    print("2. Afisare proprietatea 8")
    print("3. Afisare proprietatea 9")
    print("4. Iesire")

def main():
    l = []
    ruleaza=True
    while ruleaza==True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(subsecvintre0si10(l))
        elif optiune == "3":
            print(crescsaurep(l))
        elif optiune == "4":
            ruleaza=False
        else:
            print("Optiune invalida, reincercati: ")
main()