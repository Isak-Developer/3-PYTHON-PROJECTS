Balance=1000

from datetime import datetime
now=datetime.now()
current_time =now.strftime("%d-%m-%y \n %H-%M-%S")

CreatePin=int(input("Fadlan Gali PIN-Kaaga Cusub"))
ConfirmPin=int(input("Fadlan Ku Celi Gali PIN-Kaaga Cusub"))

if CreatePin != ConfirmPin:
    print("Fadlan Iska Hubi PIN-Kaaaga")
else:
    pin=int(input("Fadlan Gali Pinkaaga"))
    
    if pin == ConfirmPin:
        print("[-EVC PLUS-]")
        print("1. Itus Haraaga")
        print("2. Kaarka hadalka")
        print("3. Bixi Bill")
        print("4. Uwareeji EVC Plus")
        print("5. Warbixin kooban")
        print("6. Salaam bank")
        print("7. Maareynta")
        print("8. TAAJ")
        print("9. Bill Payment")
        Option=int(input("Fadlan Option dooro "))
        if Option == 1:
            print("[-EVC PLUS-]")
            print(f"Haraagagu waa {Balance}$")
        elif Option == 2:
            print("KAARKA HADALKA")
            print("1. Ku shubo Airtime")
            print("2. Ugu shub Airtime")
            print("3. MIFI Packages")
            print("4. Ku shubo Internet")
            print("5. Ugu Shub qof kale (MMT)")
            Airtime=int(input("Falan dooro"))
            if Airtime == 1:
                money=int(input("Fadlan Gali Lacagta "))
                Balance-=money
                if Balance < money:
                    print("Haraagagu Xisaabtaada kuguma filna!")
                else:
                    print(f"Waxaad Ku shubatay ${money} Haraagagu waa ${Balance}")
            elif Airtime== 2:
                mobile=int(input("Falan Gali mobileka "))
                money=int(input("Fadlan gali Lacagta "))
                print(f"ma hubtaa in aad ${money} aad ugu shubto {mobile}?")
                print(f" 1. Haa \n 2. Maya")
                hubin=int(input("Fadlan dooro"))
                if hubin==1:
                    if Balance < money:
                        print("Haraagagu Xisaabtaada kuguma filna!")
                    else:
                        Balance-=money
                        print(f"${money} ayaad u wareejisay {mobile}, Taarikhdu {current_time}, Haraagagu waa ${Balance}")
                elif hubin==2:
                    print("Waad ka laabatay lacag diridii Mahadsanid")
                else:
                    print("MACSALAAMO!!")
            elif Airtime == 3:
                print("3. MIFI Packages")
            elif Airtime == 4:
                print("4. Ku shubo Internet")
            elif Airtime == 5:
                print("5. Ugu Shub qof kale (MMT)")
            else:
                print("MACSALAAMO")
        elif Option == 3:
            print("3. Bixi Bill")
        elif Option == 4:
            print("[-EVC PLUS-]")
            mobile=int(input("Falan Gali mobileka"))
            money=int(input("Falan Gali Lacagta"))
            print(f"Ma hubtaa inaad {money}$ u wareejiso {mobile}?")
            print("1. Haa \n2. Maya")
            hubin=int(input("Fadlan dooro"))
            if hubin == 1:
                if Balance < money:
                    print("Haraagagu Xisaabtaada kuguma filna!")
                else:
                    Balance-=money
                    print(f"${money} ayaad u wareejisay {mobile} Taarikhdu {current_time} Haraagagu waa ${Balance}")
            elif hubin == 2:
                print("Waad ka laabatay lacag diridii Mahadsanid")
            else:
                print("MACSALAAMO")
            
        elif Option == 5:
            print("Warbixin Kooban")
            print("1. Last Action")
            print("2. Wareejintii u dambeysay")
            print("3. Iibsashadii u danbeysay")
            print("4. Last 3 Actions")
            print("5. Email Me My Activity")
        elif Option == 6:
            print("")
        elif Option == 7:
            print("7. Maareynta")
        elif Option == 8:
            print("8. TAAJ")
        elif Option == 9:
            print("9. Bill Payment")
            
        else:
            print("MACSALAAMO")
    
    
    else:
        print("Numbarka Sirta aad galisay waa khalad")