import json


def start():
    while True:
        print("1 - Giris\n2 - Qeydiyyat\n3 - Sifreni unutdum\n4 - Cixish")
        cavab = int(input("Icra elemek istediyiniz emri secin: "))
        while 1 > cavab or 4 < cavab:
            cavab = int(input("1 ile 4 arasi secim edin: "))
        if cavab == 1:
            girish()
        if cavab == 2:
            qeydiyyat()
        if cavab == 3:
            sifreBerpasi()
        if cavab == 4:
            pass
        break


def girish():
    login = input("Istifadeci adinizi daxil edin: ")
    parol = input("Sifrenizi daxil edin")
    with open("db.json", "r") as file:
        json.load(file)
        file.read(file["Istifadeciler"]["login"])


def qeydiyyat():
    print("Qeydiyyat bolumunde butun xanalar mutle doldurulmalidir")
    login = input("Istifadeci adinizi daxil edin: ")
    parol = input("Parolunuzu daxil edin: ")
    parolTekrar = input("Parolunuzu tekrar edin: ")
    eMail = input("e-mailinizi daxil edin: ")
    while login == "" or parol == "" or parolTekrar == "" or eMail == "":
        print("Butun xanalari doldurmaginiz mutleqdir")
        login = input("Istifadeci adinizi daxil edin: ")
        parol = input("Parolunuzu daxil edin: ")
        parolTekrar = input("Parolunuzu tekrar edin: ")
        eMail = input("e-mailinizi daxil edin: ")
    if parolTekrar != parol:
        print("Sifreni 2 bolmeyede duzgun daxil edin.")
        login = input("Istifadeci adinizi daxil edin: ")
        parol = input("Parolunuzu daxil edin: ")
        parolTekrar = input("Parolunuzu tekrar edin: ")
        eMail = input("e-mailinizi daxil edin: ")

    with open("db.json","a") as file:
        json.dump(jsonCreate(login,parol,eMail),file)

def sifreBerpasi():
    pass


start()

def jsonCreate(loginYarat,parolYarat,eMailYarat,):
    melumatlar = {}
    melumatlar["Istifadeciler"] = []
    melumatlar["Istifadeciler"].append({"Login": loginYarat,
                                        "Parol": parolYarat,
                                        "eMail": eMailYarat})
    return melumatlar