login_adi="Haci"
login_password="1234"
name=input("Adinizi girin:")
kodu=input("Kodu daxil edin:")
if ((login_adi==name) and (login_password==kodu)):
    print("Sisteme giris etdiz")
elif ((login_adi!=name) and (login_password==kodu)):
    print("Isdifadeci adi yalnis")
elif ((login_adi==name) and (login_password != kodu)):
    print("Isdifadeci kodu yalnis")

