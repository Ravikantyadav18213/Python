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
        if len(books)>0:
           old_book_title=input("enter book title to update:").capitalize()
           if old_book_title in books:
                new_title=input("Enter book new title to update:").capitalize()
                books[books.index(old_book_title)]=new_title . capitalize()
                print(f"{old_book_title}Book title updated succesfully!!")
           else:
               print(f"{old_book_title}Book title not found try again!!")
        else:
            print("no book available so first add the books!!")

    elif choice==4:
        if len(books)>0:
            old_book_title=input("enter book title to remove:").capitalize()
            if old_book_title in books:
                books.remove(old_book_title.capitalize())
                print(f"{old_book_title}Book removed successfully")
            else:
                print(f"{old_book_title}Book title not found try again!!")
        else:
            print("no book available so first add the books!!")

    elif choice==5:
        print("Thank for using our services")
        break