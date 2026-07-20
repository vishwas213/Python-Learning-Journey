phonebook = {
    "devanshu": "9876543210",
    "Vishwas": "9123456789",
    "dushyant": "9988776655",
    "dhiru": "7836250982",
}

name = input("name of the person : ")

if name in phonebook:
    print(name ,";", phonebook[name])
else:
    print("Contact not found")