print("Program enkripsi dan deksripsi menggunakan metode caesar")
print("Nama : Redja Djata Saputra")
print("NIM : 20190801239")

List_huruf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# fungsi enkripsi dengan parameter List_huruf
def enkripsi(List_huruf):
    str = input("Pesan yang akan dienkripsi : ") 
    key = int(input("Key : ")) 

    str = str.lower() 
    result = '' 

    for char in str: 
        if char in List_huruf: 
            n = List_huruf.index(char) 
            encrypt = (n - key) % 26
            convert = List_huruf[encrypt] 
            result = result + convert 
        else:
            result = result + ' ' 

    print(f"Result : {result}") 

def dekripsi(List_huruf):
    str = input("Pesan Hasil Deksripsi : ") 
    key = int(input("Key : ")) 

    str = str.lower() 
    result = '' 

    for char in str:
        if char in List_huruf:
            n = List_huruf.index(char) 
            encrypt = (n + key) % 26 
            convert = List_huruf[encrypt] 
            result = result + convert 
        else:
            result = result + ' ' 
    print(f"Result : {result}") 

pilihan = 'y'

while (pilihan == 'y'):
    print(" \t\t\t------- Program Enkripsi dan Deksripsi -------")
    print("Menu Program : ")
    print("1. Dekripsi Data")
    print("2. Enkripsi Data")
    print("3. Keluar")

    menu = input("Menu yang dipilih : ")
    print("-------------------------------------")

    if menu == '1':
        print("Menu Dekripsi Data")
        dekripsi(List_huruf)

    elif menu == '2':
        print("Menu Enkripsi Data")
        enkripsi(List_huruf)

    elif menu == '3':
        print("Program Selesai, terima kasih.")
        break
    else:
        print("Menu tidak ditemukan")

    print("------------------------------------")
    pilihan = input("Apakah ingin melanjutkan ? (Y/n) : ")
    print("------------------------------------")
