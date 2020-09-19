try:
    #db connection open
    sayi = int(input("sayi gir:"))
    # connection error
    print("congrats")
    #db connection close
except:
    print("ı gave up") 
    #db connection close
finally:
    print("her durumda tetiklenir")
