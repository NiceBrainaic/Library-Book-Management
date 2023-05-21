def book_entry():
    nm=input("enter book name:")
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
    print('')
    
def salary_entry():
    print('function#5')
    

    
while (True):
 print("1 : Add BOOK")
 print("2 : AVAILABLE BOOKS")
 print("3 : UPCOMING BOOKS")
 print("4 : BOOKS FOR RENT")
 print("5 : BOOKS RENTED")
 print("8 : Exit")
 
 choice = int(input("Please Select An Above Option: ")) 
 if(choice== 1): 
     book_entry()
 elif (choice==2): 
     Show_EMP() 
 elif (choice==3): 
     per_setter() 
 elif (choice==4): 
     Show_Rates()
 elif (choice==5): 
     salary_entry()
 elif (choice == 8):
     break
 else: 
     print(" Wrong choice..........")
