books=[]
while True:
    print("---eLibrary---")
    print("1:addbooks\n2:showbooks\n3:updateboks\n4:deletebooks\n5:exit")
    choice=int(input("enter choice number:"))
    if choice==1:
        title=input("enter book title:").capitalize()
        if title not in books:
            books.append(title)
            print(f"{title} books added sucessfully")
        else:
            print(f"{title} books is already exists so add another book!!")
    elif choice==2:
        if len(books)==0:
            print("no books available try again")
        else:
            print("Available book are:",books)
    elif choice==3:
        pass
    elif choice==4:
        pass
    elif choice==5:
        print("Thank for using our services")
        break