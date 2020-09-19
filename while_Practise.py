login_adi="Haci"
login_password="1234"
while True:
    name = input("Adinizi girin:")
    kodu = input("Kodu daxil edin:")
    if ((login_adi == name) and (login_password == kodu)):
        print("Sisteme giris etdiz")
        break
    elif ((login_adi != name) and (login_password == kodu)):
        print("Isdifadeci adi yalnis")
    elif ((login_adi == name) and (login_password != kodu)):
        print("Isdifadeci kodu yalnis")
        print("Isdifadeci kodunu deyisdirmek isdeyirsinizse C - ye basin")
        change=input()
        if change=="C":
            yeniparol=input("Yeni parolu daxil edin")
            login_password=yeniparol
            print("Ugurla basa catmisdir")
        else:
            print("Yeniden cehd edin")


