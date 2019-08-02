while True:
    print ("\nAklınızdan 1-100 arasında bir sayı tutun....Ben bunu bilmeye çalışacağım..")
    giris=input ("\n Eğer sayıyı tuttu iseniz Enter tuşuna basınız ve oyun başlasın...\n Oyundan çıkmak için ise q tuşuna basınız..")
    tahmin=50
    düsük_tahminler=[0]
    yüksek_tahminler=[100]
    if giris=="q":
        break
    elif giris=="":
        while True:

            cevap=input("\nSayın {} mi?  \n\n Tuttuğun sayı bundan büyük ise '+' küçük ise '-' , tuttuğun sayı {} ise enter tuşuna basın   ".format (tahmin,tahmin))
            if cevap=="+":
                düsük_tahminler=düsük_tahminler+[tahmin]
                alt_sın=max(düsük_tahminler)
                üst_sın=min(yüksek_tahminler)
                tahmin=alt_sın+(üst_sın-alt_sın)//2
                print("\nDüşük değerler...:",düsük_tahminler,"...min=  ",alt_sın,"\nYüksek değerler...:",yüksek_tahminler,"...max=  ",üst_sın)
                continue
#

            elif cevap=="-":
                yüksek_tahminler=yüksek_tahminler+[tahmin]
                alt_sın=max(düsük_tahminler)
                üst_sın=min(yüksek_tahminler)
                tahmin=üst_sın-(üst_sın-alt_sın)//2
                print("\nDüşük değerler...:",düsük_tahminler,"...min=  ",alt_sın,"\nYüksek değerler...:",yüksek_tahminler,"...max=  ",üst_sın)
                continue

            elif cevap=="":
                print("\n***Elhamdulillah,, nihayet sayını bulabildim..***\n".center(80))
                break

    else:
        print("Lütfen sizden istenilen seçeneklerden birini tuşlayın ki ben de sayınızı tahmin edebileyim..")




    
    
               
