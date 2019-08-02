print("""
123
456
789""")
print("\n yukarıdaki sayı tuşlarına göre nereye hangi işareti koymak istiyorsanız önce o yerin numarasına sonrada O/X TUŞLARINDAN birine basınız\n")
oyun="devam"        #3 ü de aynı simge olmadığında oyun devam eder..

import random

liste=["_","_","_","_","_","_","_","_","_"]
s1=liste[0:3]   #matris 1.2.3. satırlar
s2=liste[3:6]
s3=liste[6:9]

s11=" ".join(s1)
s22=" ".join(s2)
s33=" ".join(s3)

print("Önce sen başla..")

while oyun=="devam":
    bak=1       #tamamlanması gereken  8 adet üçllere sırayla bakar
    s1=liste[0:3]   #matris 1.2.3. satırlar
    s2=liste[3:6]
    s3=liste[6:9]
    su1=[liste[0],liste[3],liste[6]]  #matris 1.2.3. sütünlar
    su2=[liste[1],liste[4],liste[7]]
    su3=[liste[2],liste[5],liste[8]]
    çap1=[liste[0],liste[4],liste[8]]     # matris iki çapraz  hizalar
    çap2=[liste[2],liste[4],liste[6]]
    arama_lis=[s1,s2,s3,su1,su2,su3,çap1,çap2]
    s11=" ".join(s1)
    s22=" ".join(s2)
    s33=" ".join(s3)

    try:
        print(s11,s22,s33,"\n....İşaretleyeceğin yeri seç..",sep="\n")
        yer=int(input(""))  #oyuncunun seçeceği yer 0-8 nolu tuşlarla belirlenir
    except ValueError:
        print("\nlütfen sizden istenilen değeri giriniz..\n")
    if yer>9 or yer<1:
        print("Lütfen sizden istenilen değerlerden birini giriniz..")
        continue
    
    else:                   #hangi yer seçilmiş ise oraya"O" konacak
        if liste[yer-1]=="_":
            liste[yer-1]="O"
        else:
            print("Bu yer dolu.. başka bir yer seçin...")
            continue

            
            
    s1=liste[0:3]   #işaretler gösterilecek 
    s2=liste[3:6]
    s3=liste[6:9]
    su1=[liste[0],liste[3],liste[6]]  #matris 1.2.3. sütünlar
    su2=[liste[1],liste[4],liste[7]]
    su3=[liste[2],liste[5],liste[8]]
    çap1=[liste[0],liste[4],liste[8]]     # matris iki çapraz  hizalar
    çap2=[liste[2],liste[4],liste[6]]
    arama_lis=[s1,s2,s3,su1,su2,su3,çap1,çap2]
    s11=" ".join(s1)
    s22=" ".join(s2)
    s33=" ".join(s3)
  # print(s11,s22,s33,sep="\n")
                
## SIRA BİLGİSAYARDA

#istenilen hizalarda var olan "o" sayıları
    while bak==True:
                   
        for k in arama_lis:
            if k.count("O")==3:                                     #3 adet "O"varsa oyun biter
                print("Tebrikler oyunu kazandınız")
                #bak=False                                                              ################???????????
                oyun="bitti"
                
                break
        if bak==True:                                               # bilgisayar istenlen sıralarda 2 adet "O" varsa diğer kısım boş ise oraya X koyar
            sıra=-1
            for k in arama_lis:
                sıra+=1
                if k.count("O")==2:
                    if k.count("X")==0:
                        arama_lis[sıra][k.index("_")]="X"
                        bak=False
                        break
        if bak==True:

            sıra=-1   
            for k in arama_lis:
                sıra+=1
                if k.count("O")==1:
                    o_yer=k.index("O")                      
                    if k.count("X")==2:
                        continue
                    elif k.count("X")==1:
                        arama_lis[sıra][k.index("_")]="X"
                        bak=False                                       # tek bir O olan 3 lü grupda diğer iki yerden biri X ise boşluk olan yere  Xkoyacak
                    elif k.count("X")==0:
                            s=0
                            while o_yer !=s:                                #tek bir "o" olan sırada diğer iki boşluktan birine rastgele X ataması
                                s=random.randint(0,2)
                            
                            arama_lis[sıra][s]="X"
                            bak=False
                            break
            
##arama_lis=[s1,s2,s3,su1,su2,su3,çap1,çap2]
            
    s1=arama_lis[0]             #arama listesindeki değişiklikler gruplara atılır
    s2=arama_lis[1]
    s3=arama_lis[2]
    su1=arama_lis[3]
    su2=arama_lis[4]
    su3=arama_lis[5]
    çap1=arama_lis[6]
    çap2=arama_lis[7]

    liste[0:3]=s1           #gruplardaki değişiklikler listeye aktarılır
    liste[3:6]=s2
    liste[6:9]=s3
    [liste[0],liste[3],liste[6]]=su1
    [liste[1],liste[4],liste[7]]=su2
    [liste[2],liste[5],liste[8]]=su3
    [liste[0],liste[4],liste[8]]=çap1
    [liste[2],liste[4],liste[6]]=çap2
    s11=" ".join(s1)
    s22=" ".join(s2)
    s33=" ".join(s3)
    print(arama_lis,"SON ÇIKTI")
    print(s11,s22,s33,"ASASASASA",sep="\n")
                
  


    
        

                
    

