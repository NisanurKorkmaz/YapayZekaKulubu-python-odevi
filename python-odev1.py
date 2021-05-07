#birinci soru : cift sayi kontrolu

s1=int(input("bir sayi giriniz "))

if(s1%2==0):
    print("girilen sayi cift sayidir")
else:
    print("girilen sayi tek sayidir")


#ikinci soru : 5 tane sayi alip asal olup olmadiginin kontrolu

for i in range(5):

    sayi=int(input("bir sayi giriniz: "))
    asalmi = True

    if(sayi==1):
        print("1 sayisi asal degil")
    else :
        for i in range(2, sayi):
            if(sayi%i==0):
                asalmi = False
                break
    
    if(asalmi):
        print(f"girilen {sayi} sayisi asaldir")
    else:
        print("girilen sayi asal degil")
        

#ucuncu soru :

def TemizVeri():
    ilk_string ="Ah5me4t"
    ikinci_string = "M9eHm4eT"
    ucuncu_string ="Ha3K5a1n"
    
    ilk_temiz=""
    ikinci_temiz=""
    ucuncu_temiz=""
    
    myList=[letter for letter in ilk_string] #karakterleri tek tek diziye atar
    
    i=0
    while i<len(myList) :
        s=myList[i]
        if s.isalpha() :
            ilk_temiz+=s
        i+=1
    
    Birlesmis_deger=""
    
    ilk_temiz=ilk_temiz.lower()
    ilk_temiz=ilk_temiz.title()
    Birlesmis_deger+=ilk_temiz
    Birlesmis_deger+="-"
    
    
    
    myList=[letter for letter in ikinci_string] #karakterleri tek tek diziye atar
    i=0
    while i<len(myList) :
        s=myList[i]
        if s.isalpha() :
            ikinci_temiz+=s
        i+=1
    
    ikinci_temiz=ikinci_temiz.lower()
    ikinci_temiz=ikinci_temiz.title()
    Birlesmis_deger+=ikinci_temiz
    Birlesmis_deger+="-"
    
    
    
    myList=[letter for letter in ucuncu_string] #karakterleri tek tek diziye atar
    i=0
    while i<len(myList) :
        s=myList[i]
        if s.isalpha() :
            ucuncu_temiz+=s
        i+=1
    ucuncu_temiz=ucuncu_temiz.lower()
    ucuncu_temiz=ucuncu_temiz.title()
    Birlesmis_deger+=ucuncu_temiz
    
    return Birlesmis_deger
    

print(TemizVeri())
