import pickle
import random
from tabulate import tabulate

f=open("book_data.dat","ab")
j=open("book_rent.dat","ab")
k=open("new_books.dat","ab")
l=open("book_details.dat","ab")

def book_entry():
        f=open("book_data.dat","rb")
        nm=input("Enter Book Name:")
        genre=input("Enter Genre:")
        author=input("Enter Author Name:")
        year=input("Enter Year Of Publishing:")
        ISBN=input("Enter ISBN Code:")
        rec=pickle.load(f)
        f.close()
        #writing to file
        for i in rec:
            if i==genre:
                rec[genre].append(nm)
                break
        else:
            rec[genre]=[nm]
        copy=rec.copy()
        bk_data=[nm, genre, author, year, ISBN]
        f=open("book_data.dat","wb")
        pickle.dump(copy,f)
        print(nm, "Successfully Added")
        f.close()    
        
        j=open("book_details.dat","rb")
        rec=pickle.load(j)
        j.close()
        j=open("book_details.dat", "wb")
        rec.append(bk_data)
        pickle.dump(rec,j)
        j.close()
def Display_Books():
    try:
        f=open("book_data.dat","rb")
        rec=pickle.load(f)
        f.seek(0)
        print(tabulate(rec, headers="keys", tablefmt="fancy_grid"))
    except EOFError:
        print("File Dosen't Exist")
    
    
def Upcoming_Books():
    try:
        f=open("new_books.dat","rb")
        rec=pickle.load(f)
        print(tabulate(rec, headers="Upcoming", tablefmt="fancy_grid"))
    except EOFError:
        print()
        print("No Upcoming Books")
    
    

def Book_Renting():
    try:
        f=open("book_data.dat","rb")
        data=pickle.load(f)
        flag=0
        bk_name=input("Enter name of book:")
        for i in data:
            for j in data[i]:
                if bk_name.title()==j:
                    print("Book Found!")
                    book=bk_name
                    data[i].remove(bk_name)
                    #book details update
                    k=open("book_details.dat","rb")
                    rec=pickle.load(k)
                    k.close()
                    k=open("book_details.dat", "wb")
                    for dat in rec:
                        if dat[0]==bk_name:
                            rec.remove(dat)
                    pickle.dump(rec,k)
                    k.close()
                    #book details upd over
                    ref=str(random.randint(1000,9999))
                    print("Your Rent Reference ID:",str(ref))
                    flag=1
                    l=open("book_rent.dat","ab")
                    rent_1=[book, ref]
                    rent_2=[rent_1]
                    pickle.dump(rent_2,l)
                    l.close()
                    break
        f.close()
        f=open("book_data.dat","wb")
        pickle.dump(data,f)
        if flag==0:
            print("Book Not Found")
    except EOFError:
        print("File Dosen't Exist")
                
                
def Book_Rented():
    try:
        f=open("book_rent.dat","rb")
        rec=pickle.load(f)
        print((tabulate(rec,headers=["Book Name","Reference ID"], tablefmt="fancy_grid")))
        f.close()
    except EOFError:
        print("No Records Found")

def Remove_Book():
    while True:    
        print("1: REMOVE FROM BOOK RENTING")
        print("2: REMOVE FROM UPCOMING BOOKS")
        print("3: RETURN TO MAIN MENU")
        ch= int(input("Enter Option:"))
        if ch==1:
            try:
                f=open("book_rent.dat","rb")
                rec=pickle.load(f)
                f.close()
                f=open("book_rent.dat","ab")
                flag=0
                book_name=input("Enter Book Name To Be Removed:")
                for i in rec:
                    if i[0]==book_name:
                        rec.remove(i)
                        print("Removal Sucessful")
                        flag=1
                if flag==0:
                    print("Book Not Found")
                f.close()
                f=open("book_rent.dat","wb")
                f.close()
                f=open("book_rent.dat","ab")
                pickle.dump(rec,f)
                break
            except EOFError:
                print("No Books Rented")
        
        elif ch==2:
            try:
                f=open("new_books.dat","rb")
                rec=pickle.load(f)
                f.close()
                f=open("new_books.dat","ab")
                flag=0
                book_name=input("Enter Book Name To Be Removed:")
                for i in rec:
                    if i[0]==book_name:
                        rec.remove(i)
                        print("Removal Successful")
                        flag=1
                if flag==0:
                    print("Book Not Found")
                f.close()
                f=open("new_books.dat","wb")
                f.close()
                f=open("new_books.dat","ab")
                pickle.dump(rec,f)
                break
            except EOFError:
                print("No Upcoming Books Found")
        
        elif ch==3:
            break
        
        else:
            print("Wrong Choice")
def Search():
    print()
    print("1: SEARCH USING NAME")
    print("2: SEARCH USING ISBN CODE")
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        try:
            sea_nm=input("Enter The Name Of Book:")
            f=open("book_details.dat", "rb")
            flag=0
            rec=pickle.load(f)
            for i in rec:
                if i[0]==sea_nm:
                    flag=1
                    new=[i]
                    print(tabulate(new, headers=["Name", "Genre", "Author", "Year", "ISBN"], tablefmt="fancy_grid", stralign="center"))
            if flag==0:
                print("Book Not Found")
        except EOFError:
            print("Sorry, There Are No Books Avaliable Right Now!")
    if ch==2:
        try:
            sea_ISBN=input("Enter ISBN Code:")
            f=open("book_details.dat", "rb")
            flag=0
            rec=pickle.load(f)
            for i in rec:
                if i[4]==sea_ISBN:
                    flag=1
                    new=[i]
                    print(tabulate(new, headers=["Name", "Genre", "Author", "Year", "ISBN"], tablefmt="fancy_grid", stralign="center"))
            if flag==0:
                print("Book Not Found")
        except EOFError:
            print()
            print("Sorry, There Are No Books Avaliable Right Now!")
def Modify_Book():
    bk=input("Enter Book Name To Be Modified:")
    try:
        f=open("book_details.dat", "rb")
        rec=pickle.load(f)
        flag=0    
        f.close()
        for i in rec:
            if i[0]==bk:
                i[1]=input("Enter Genre:")
                i[2]=input("Enter Author Name:")
                i[3]=input("Enter Year Of Publishing:")
                i[4]=input("Enter ISBN:")
                print()
                print("Update Sucessful")
                flag=1
        if flag==0:
            print("Book Not Found")
        f=open("book_details.dat", "wb")
        pickle.dump(rec, f)
        f.close()
    except EOFError:
        print("Sorry, There Are No Books Avaliable Right Now!")
            
        
def security():
    user=["Manager","Owner"]
    password={"Manager":"1234","Owner":"5678"}
    print("LOGIN PORTAL")
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
     print("4 : BOOK RENTING")
     print("5 : BOOKS RENTED")
     print("6 : SEARCH FOR A BOOK")
     print("7 : REMOVE BOOK DATA")
     print("8 : MODIFY BOOK DETAILS")   
     print("9 : EXIT")
     print()
     
     choice = int(input("Please Select An Above Option: ")) 
     if(choice== 1): 
         book_entry()
         print()
         q=input("Would you like to continue?(y/n)")
         if q=="n":
             break
     elif (choice==2): 
         Display_Books()
         print()
         q=input("Would you like to continue?(y/n)")
         if q=="n":
             break
     elif (choice==3): 
         Upcoming_Books()
         print()
         q=input("Would you like to continue?(y/n)")
         if q=="n":
             break
     elif (choice==4): 
         Book_Renting()
         print()
         q=input("Would you like to continue?(y/n)")
         if q=="n":
             break
     elif (choice==5): 
         Book_Rented()
         print()
         q=input("Would you like to continue?(y/n)")
         if q=="n":
             break
     elif choice==7:
        Remove_Book()
        q=input("Would you like to continue?(y/n)")
        if q=="n":
             break
    
     elif (choice == 6):
         Search()
         q=input("Would you like to continue?(y/n)")
         if q=="n":
             break
     elif (choice==8):
          Modify_Book()
          q=input("Would you like to continue?(y/n)")
          if q=="n":
             break
        
     elif choice==9:
         break
     else: 
        print(" Wrong choice..........")
