import hashlib
def passwordhashing(passwd: str, algo1: str, algo2: str) -> str:
    try:
        hashOb = hashlib.new(algo1)
        hashOb.update(passwd.encode('utf-8'))
        hash1 = hashOb.digest() 
        hashObj2 = hashlib.new(algo2)
        hashObj2.update(hash1)
        genHash= hashObj2.hexdigest()
        return genHash
    except ValueError:
        return f"Algorithm not Supported."
def main():
    passwd = input("Enter the password to hash: ")
    print("Available Hashing Algorithms are : \n")
    print("1. MD5\n 2.SHA256\n 3. SHA512")
    ch1 = int(input("\nSelect the first hashing algorithm: "))
    ch2 = int(input("\nSelect the second Hashing Algorithm: "))

    if (ch1 and ch2 < 1) or (ch1 and ch2 > 3):
        print("Invalid choice")
        return
    if(ch1==1):
        algo1="md5"
    elif(ch1==2):
        algo1="sha256"
    else:
        algo1="sha512"
    
    if(ch2==1):
        algo2="md5"
    elif(ch2==2):
        algo2="sha256"
    else:
        algo2="sha512"

    Generated_Hash= passwordhashing(passwd,algo1 , algo2)
    print(f"\nThe Hash of the given password is: {Generated_Hash}")

if __name__ == "__main__":
    main()
