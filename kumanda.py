import random
import time

class kumanda():
    def __init__(self,tv_durum="kapalı",tv_ses=0,kanal_listesi=["trt"],kanal="trt") :
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
    def tv_ac(self):
        if(self.tv_durum=="açık"):
            print("televizyon açık")
        else:
            print("televizyon açılıyor")
            self.tv_durum="açık"
    def tv_kapat(self):
        if(self.tv_durum=="kapalı"):
            print("televizyon kapalı")
        else:
            print("televizyon kapanıyor")
            self.tv_durum="kapalı"
    def ses_ayarlari(self):

        while True:
         cevap=input("ses azalt:'<'\nsesi arttır:'>'\nçıkış:çıkıs")
         if(cevap=="<"):

            if(self.tv_ses!=0):

                self.tv_ses-=1
                print("ses:",self.tv_ses)
         elif(cevap==">"):
             if(self.tv_ses!=31):
                self.tv_ses+=1
                print("ses:",self.tv_ses)
         else:
            print("ses güncellendi:",self.tv_ses)
            break
    def kanal_ekle(self,kanal_ismi):
        print("kanal ekleniyor...")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)
        print("kanal eklendi..")
    
        self.kanal_listesi.remove(kanal_ismi)
    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)

        self.kanal=self.kanal_listesi(rastgele)

        print("şuan ki kanal:",self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "tv durumu:{}\ntv ses:{}kanal listesi:{}\nşuan ki kanal:{}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)
kumanda=kumanda()

print("""
televizyon uygulaması
      1.tv aç
      2.tv kapat
      3.ses ayarları
      4.kanal ekle
      5.kanal sayısını öğrenme
      6.rastgele kanal seçme
      7.televizyon bilgileri
      çıkmak için 'q' ya basın.
""")
while True:
    islem=input("işlem seçiniz:")
    if(islem=="q"):
        print("program kapatılıyor")
        break
    elif(islem=="1"):
        kumanda.tv_ac()
    elif(islem=="2"):
        kumanda.tv_kapat()
    elif(islem=="3"):
        kumanda.ses_ayarlari()
    elif(islem=="4"):
        kanal_isimleri=input("kanal isimleri','ile ayırarak giriniz")

        kanal_listesi=kanal_isimleri.split(",")
        for eklenecekler in kanal_isimleri:
            kumanda.kanal_ekle(eklenecekler)
    elif(islem=="5"):
        print("kanal sayıları:",len(kumanda))
    elif(islem=="6"):
        kumanda.rastgele_kanal()
    elif(islem=="7"):
        print(kumanda)
    else:
        print("geçersiz işlem")


    
    



        
