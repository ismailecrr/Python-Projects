import random
import time

print("***************** sayı tahmin oyunu *******************")
print("1 ile 40 arasında sayı giriniz")

tahmin_hakki=7
rastgele_sayi=random.randint(1,40)
while True:
    sayi=int(input("sayi giriniz:"))
    if (sayi<rastgele_sayi):
        print("kontrol ediliyor")
        time.sleep(2)
        print("daha büyük sayi giriniz:")
        tahmin_hakki-=1
    elif (sayi>rastgele_sayi):
        print("kontrol ediliyor")
        time.sleep(2)
        print("daha küçük sayi giriniz:")
        tahmin_hakki-=1
    else:
        print("kontrol ediliyor")
        time.sleep(2)
        print("doğru tahmin ettiniz sayi:",rastgele_sayi)
    if (tahmin_hakki==0):
        print("sayiyi bulamadin kaybettin..")
        print("sayi:",rastgele_sayi)
        break

