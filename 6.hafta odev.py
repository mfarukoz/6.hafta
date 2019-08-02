##ODEV 1: Sayi Tahmin
##
##Kullanicidan aklindan 0-100 araliginda bir sayi tutmasini isteyelim.

print("""
                Sayi Tahmin Oyunu

            Aklindan tuttugun bir sayiyi
        en hizlisindan bilmeye calisacagim...

                Basarilar!!!...
                """)
print("Aklindan bir sayi tut!!!\n")
ilk=[0]
son=[100]
import random
sayi=input("Bir sayi tuttun mu (Y/N): ")    #Sayi tuttugundan emin olalim.

while True:
    if sayi=="n" or sayi=="N":
        print("Hadi bi sayi tut da oyun baslasin...\n")
        continue
    if sayi!="n" and sayi!="N" and sayi!="y" and sayi!="Y": 
        print("Lutfen dogru secenek giriniz...")
        continue
    if sayi=="":
        print("Lutfen bos birakmayiniz, tekrar deneyiniz...\n")
        continue
    elif sayi=="y" or sayi=="Y":        #Sayi tuttuysa ayni sayi verdiginde uyarma
        if ilk[-1]>=son[0]:
            print("{}sayisindan baska sayi olamaz".format(secim))
            print("Tekrar tahmini secim yapiyoruz.\n")
            ilk[0]
            son[100]
            continue
        else:
            secim=random.randrange(ilk[-1],son[0]) #aksi halde tahmin edip cıktı verelim.
            print("\nTuttugun sayi: ",secim,"?","\n")
            pass
            while True:
                sayi2=input("Aklindan tuttugun sayiyi buldum mu?(Y/N): ") #Her seferinde dogru sayiyi buldu mu degilmi diye soralim.
                if sayi2=="y" or sayi2=="Y":
                    print("\n !!! Tebrik et beni nasil buldum ama... :) !!!\n")
                    break
        
                if sayi2=="n" or sayi2=="N":
                    print("\nEger tuttugun sayi bu sayidan buyukse '+', kucukse '-' yaz...\n")
                    islem=input("Seciminiz: ")  #Secime gore arttirip azaltalim.
                    if islem!="+" and islem!="-" and islem!="":
                        print("Lutfen verilen degerşerden birini giriniz...")
                        continue
                    else:
                        if islem=="+":
                            ilk.append(secim) #Bu secimleri listeye kaydedelim.
                            ilk.sort()
                            break
                        elif islem=="-":
                            son.append(secim)
                            son.sort()
                            break
                        
                            
