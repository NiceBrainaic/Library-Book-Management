import pickle
f=open("book_data","rb")

def book_entry():
    nm=input("enter book name:")
    author=input("enter name of the author:")
    print(nm,"Sucessfully added")
    
    
def Show_EMP():
    print('Story book:-')
    print('1.Harry potter')
    print('2.Famous five')
    print('3.Wimpy kid')
    print('4.The lord of rings')
    print('Autobiography:-')
    print('1.Wings of fire')
    print('2.The diary of young girl')
    print('3.Long walk to freedom')
    
    
def per_setter():
    print('Don Quixote')
    print('The little prince')
    print('The adventures of tintin')
    
def Show_Rates():
    print('War and peace')
    print('Song of solomon')
    print('The golden bypass')
    print("Harry potter and the sorcerer's stone")
    
def salary_entry():
    print('A Tale of two Cities')
    print('Wimpy kid')


def total_book():
    print('10')
def security():
    user=["Manager","Owner"]
    password={"Manager":"1234","Owner":"5678"}
    for i in range(1,4):
        user_in=input("Enter The Username:")
        if user_in in user:
            pass
        else:
            print("Username Not Found")
            continue
        pass_in=input("Enter The Password:")
        rgt_pass=password.get(user_in)
        if rgt_pass==pass_in:
            break
        else:
            print("Password Incorrect") 
            print("Please Try Again")
            continue
    else:
        print("Multiple Times Failed. Exiting Application")
        exit()
    print()
    print("WELCOME",user_in)
    print()
security()
print('******************************WELCOME TO CLASSIC BOOK SHOP MANAGEMENT PORTAL******************************')
while (True):
 print()
 print("1 : ADD BOOK DATA")
 print("2 : AVAILABLE BOOKS STATUS")
 print("3 : UPCOMING BOOKS STATUS")
 print("4 : BOOKS AVAILABLE FOR RENT")
 print("5 : BOOKS RENTED")
 print("6 : TOTAL BOOKS SOLD")
 print("8 : Exit")
 print()
 
 choice = int(input("Please Select An Above Option: ")) 
 if(choice== 1): 
     book_entry()
     print()
     q=input("Would you like to continue?(y/n)")
     if q=="n":
         break
 elif (choice==2): 
     Show_EMP()
     print()
     q=input("Would you like to continue?(y/n)")
     if q=="n":
         break
 elif (choice==3): 
     per_setter()
     print()
     q=input("Would you like to continue?(y/n)")
     if q=="n":
         break
 elif (choice==4): 
     Show_Rates()
     print()
     q=input("Would you like to continue?(y/n)")
     if q=="n":
         break
 elif (choice==5): 
     salary_entry()
     print()
     q=input("Would you like to continue?(y/n)")
     if q=="n":
         break
 elif (choice == 8):
     break
 else: 
     print(" Wrong choice..........")
