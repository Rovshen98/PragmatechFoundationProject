
print('''
                ***
Qeydiyyatdan keçmək üçün 1 daxil edin
--------------------------------------
Sistemə daxil olmaq üçün 2 daxil edin
--------------------------------------
''')
istifadeciler=[]
class istifadeci:
    def __init__(self,ad,soyad,email,username,password):
        self.ad=ad
        self.soyad=soyad
        self.email=email
        self.username=username
        self.password=password
        
    
    def melumatigoster(self):
        return(f"Ad:{self.ad}\nSoyad:{self.soyad}\nEmail:{self.email}\nUsername:{self.username}\nPassword:{self.password}")   
    
        
def qeydiyyat():
     print('Qeydiyyatdan Keçin (Tələb olunan məlumatlar):')
     ad=input("Ad:")
     soyad=input("Soyad:")
     email=input("Email:")
     username=input("Username:")
     password=input("Password:")
     istifadechi = istifadeci(ad,soyad,email,username,password)
     istifadeciler.append(istifadechi)



while True:
    x=int(input("Daxil etmək istədiyiniz nömrə:"))
    if (x==1):
       qeydiyyat()
    elif (x==2):
        user=input("Username:")
        passw=input("Password:")
        for i in istifadeciler:
            if(user==istifadeci.self.username):
                print(i)
                
            
        
    else:
        break


    
