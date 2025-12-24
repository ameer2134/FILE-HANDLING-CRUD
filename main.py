from pathlib import Path

def readfileandfolder():
    path = Path('.')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item} ")

def createfile():
    try:
        readfileandfolder()
        name = input("PLEASE TELL ME YOUR FILE NAME :-")
        P = Path(name)
        
        if not P.exists():
            with open(P, "w", encoding="utf-8") as fs:
                data = input("WHAT DO YOU WANT TO WRITE IN THIS FILE:-")
                fs.write(data)
            print("FILE HAS BEEN CREATED SUCCESSFULLY")
        else:
            print("THIS FILE IS ALREADY EXISTS")

    except Exception as err:
        print(f"AN ERROR ECCURS AS {err}") 


def readfile():
    try:
        readfileandfolder()
        name = input("PLEASE TELL ME YOUR FILE NAME TO READ:-")
        P = Path(name)

        if P.exists() and P.is_file():
            with open(P, "r", encoding="utf-8") as fs:
                content = fs.read()
            print("\n--- FILE CONTENT START ---\n")
            print(content)
            print("\n--- FILE CONTENT END ---\n")
        else:
            print("FILE DOES NOT EXIST OR IS NOT A REGULAR FILE")
    except Exception as err:
        print(f"AN ERROR OCCURS AS {err}")
def updatefile():
    try:
        readfileandfolder()
        name = input("PLEASE TELL ME YOUR FILE NAME TO UPDATE:-")
        P = Path(name)

        if P.exists() and P.is_file():
            data = input("WHAT DO YOU WANT TO WRITE IN THIS FILE (this will append):-")
            with open(P, "a", encoding="utf-8") as fs:
                fs.write(data)
            print("FILE UPDATED SUCCESSFULLY")
        else:
            print("FILE DOES NOT EXIST OR IS NOT A REGULAR FILE")
    except Exception as err:
        print(f"AN ERROR OCCURS AS {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("PLEASE TELL ME YOUR FILE NAME TO DELETE:-")
        P = Path(name)

        if P.exists() and P.is_file():
            P.unlink()
            print("FILE DELETED SUCCESSFULLY")
        else:
            print("FILE DOES NOT EXIST OR IS NOT A REGULAR FILE")
    except Exception as err:
        print(f"AN ERROR OCCURS AS {err}")
print("PRESS 1 FOR CREATING A FILE:-")
print("PRESS 2 FOR READING  A FILE:-")
print("PRESS 3 FOR UPDATING A FILE:-")
print("PRESS 4 FOR DELETION A FILE:-")

check = int(input("PLEASE GIVE ME YOUR RESPONSE:-"))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()       