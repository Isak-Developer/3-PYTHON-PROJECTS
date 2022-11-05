pin=1234
password=int(input("Fadlan Gali Pin-kaaga"))
if password == pin:
    print("[-EVC PLUS-]")
    print("1. Itus Haraaga")
    print("2. Kaarka hadalka")
    print("3. Bixi Bill")
    print("4. Uwareeji EVC Plus")
    #CHOOSE OPTION
    Option=int(input("Fadlan Option dooro"))   
    #START OPTION ONE
    if Option==1:
        print("[-EVC PLUS-]")
        print("Haraagagu waa 100000$")
     #START OPTION TWO
    elif Option==2:
        print("KAARKA HADALKA")
        print("1. Ku shubo Airtime")
        print("2. Ugu shub Airtime")
        kaar=int(input("Falan dooro"))
        if  kaar==1:
            money=int(input("Fadlan Gali Lacagta"))
            print("Waxaad Ku shubatay",money,"$")
        elif kaar==2:
            mobile=int(input("Falan Gali mobileka"))
            money=int(input("Fadlan gali Lacagta"))
            print("ma hubtaa in aad",money,"$ ugu shubto",mobile)
            print("1. Haa")
            print("2. Maya")
            hubin=int(input("Fadlan dooro"))
            if hubin==1:
                print("$",money,"ayaad u wareejisay",mobile,"Tar:03/11/22 12:00:00 Haraagagu waa 1000$.")
            else:
                print("waa ka labatay ")    
        else:
            print("Macsalaamo")

     #START OPTION THREE    
    elif Option==3:
        print("3. Bixi Bill")

     #START OPTION FOUR    
    elif Option==4:
        print("[-EVC PLUS-]")
        mobile=int(input("Falan Gali mobileka"))
        money=int(input("Fadlan gali Lacagta"))
        print("Ma hubtaa inaad ",money,"$ u wareejiso ",mobile,"?")
        print("1. Haa")
        print("2. Maya")
        hubin=int(input("Fadlan dooro"))
        if hubin==1:
            print("$",money,"ayaad u wareejisay",mobile,"Tar:03/11/22 12:00:00 Haraagagu waa 1000$.")
        else:
            print("waa ka labatay")         
    elif Option==5:
        print("5. Warbixin Kooban")
    elif Option==6:
        print("6. Salaam Bank")
    elif Option==7:
        print("7. Maareynta")
    elif Option==8:
        print("8. TAAJ")
    elif Option==9:
        print("9. Bill Payment")
    else:
        print("Macsalaamo")
else:
    print("Numbarka Sirta aad galisay waa khalad")















