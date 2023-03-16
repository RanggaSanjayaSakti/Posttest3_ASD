from prettytable import PrettyTable

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
                
class LinkedList:
    def __init__(self):
        self.head = None
    
    def tambahdepan(self, value):
        if self.head is None :
            self.head = Node(value)
        else : 
            nodebaru = Node(value)
            nodebaru.next = self.head
            self.head = nodebaru
    
    def hapusnode(self, position):
        if self.head is None:
            return
        index = 0
        current = self.head
        while current.next and index < position:
            previous = current
            current = current.next
            index += 1
        if index < position:
            print("\nIndex is out of range.")
        elif index == 0:
            self.head = self.head.next
        else:
            previous.next = current.next
    def index1(self, index):
        current_node = self.head
        current_index = 0

        while current_node is not None:
            if current_index == index:
                return current_node

            current_node = current_node.next
            current_index += 1
            
    def printlist1(self):
        if self.head is None:
            print("Linked list kosong")
        else :
            tabel1 = PrettyTable()
            tabel1.field_names = ["No", "Nama Pasien"]
            n = self.head
            a = 1
            while n is not None:
                tabel1.add_row([a,n.data])
                a += 1
                n = n.next
                print(tabel1)
    
class linkedlist_insertion:
    def __init__(self):
        self.head = None
    
    def tambahdepan2(self, value):
        if self.head is None :
            self.head = Node(value)
        else : 
            nodebaru = Node(value)
            nodebaru.next = self.head
            self.head = nodebaru
    
    def printlist2(self):
        if self.head is None:
            print("Linked list kosong")
        else :
            tabel2 = PrettyTable()
            tabel2.field_names =  ["No", "Nama Pasien"]
            n = self.head
            b = 1
            while n is not None:
                tabel2.add_row([b,n.data])
                b += 1
                n = n.next
            print(tabel2)
            
class linkedlist_delete:
    def __init__(self):
        self.head = None
    
    def tambahdepan3(self, value):
        if self.head is None :
            self.head = Node(value)
        else : 
            nodebaru = Node(value)
            nodebaru.next = self.head
            self.head = nodebaru
    
    def printlist3(self):
        if self.head is None:
            print("Linked list kosong")
        else :
            tabel3 = PrettyTable()
            tabel3.field_names = ["No", "Nama Pasien"]
            n = self.head
            c = 1
            while n is not None:
                tabel3.add_row([c,n.data])
                c += 1
                n = n.next
                print(tabel3)
                
listnya = LinkedList()
listnya1 = linkedlist_insertion()
listnya2 = linkedlist_delete()

def menambahdata():
    inputA = input("masukan nama pasien :")
    listnya.tambahdepan(inputA)
    listnya1.tambahdepan2(inputA)
def menghapus():
    hapus = int(input("Masukan nomor pasien yang ingin dihapus : "))
    b = listnya.index1(hapus-1)
    listnya2.tambahdepan3(b.data)
    listnya.hapusnode(hapus-1)
  
while True:
    print("""
   ============================   
   |========== Menu ==========|    
   |  1. Masukan Data         |
   |  2. Menghapus Data       |
   |  3. Melihat Data         |
   |  4. History data         |
   |  5. Keluar dari program  |
   ============================
    """)
    pilih = input("Masukan Yang Ingin Anda Lakukan :")
    if pilih == "1":    
        menambahdata()
    elif pilih == "2":
        listnya.printlist1()
        menghapus()
    elif pilih == "3":    
        listnya.printlist1()
    elif pilih == "4" :
        while True:
            print("""
            Menu History
            1. Pasien yang pernah dirawat inap
            2. Pasien yang sudah keluar dari rawat inap
            3. Kembali ke Menu awal
            """)
            pilih1 = input("Masukan Menu : ")
            if pilih1 == "1":
                print("List data pasien yang pernah dirawat inap")
                listnya1.printlist2()
            elif pilih1 == "2":
                print("List data pasien yang telah keluar dari rawat inap")
                listnya2.printlist3()
            elif pilih1 == "3":
                break
            else:
                print('Input Salah')
    elif pilih == "5":
        print("anda keluar dari program")
        exit()
    else :
        print("masukan inputan dengan benar")