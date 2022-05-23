hesap={
    "ad":"Ali",
    "soyadı":"Laçın",
    "hesap no":"123456789",
    "bakiye":"15000"
    }
def bakiye_kontrol(hesap):
    print("Hesabınızdaki tutar:",hesap["bakiye"])

def para_cek(hesap,tutar):
    if int(hesap["bakiye"])>=tutar:
        print("Paranızı alabilirsiniz")
    else:
        print("Hesabınızda yeterli miktarda para bulunmamaktadır.")

def para_yatir(hesap,miktar):
    yeni_bakiye=int(hesap["bakiye"])+miktar
    print("Yeni hesap bakiyesi:",yeni_bakiye)

secim=int(input("Lütfen yapılacak işlemi seçiniz.1/Bakiye Kontrol,2/Para Çekme,3/Para Yatırma"))
if secim==1:
    bakiye_kontrol(hesap)
elif secim==2:
    tutar=int(input("Lütfen çekmek istediğiniz tutarı giriniz:"))
    para_cek(hesap,tutar)
else:
    miktar=int(input("Lütfen yatırmak istediğiniz tutarı belirtiniz:"))
    para_yatir(hesap,miktar)

