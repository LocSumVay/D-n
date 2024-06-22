
class nut:
    def __init__(self,data):
        self.data = data
        self.next = None

class dslienket:
    def __init__(self):
        self.dau = None
        self.duoi = None

    def them(self,data):
        data = nut(data)
        if self.dau == None:
            self.dau = data
            self.duoi = data
        else:
            self.duoi.next = data
            self.duoi = data
    #Choice 3: Display data
    def print(self):
        hientai = self.dau
        print('ID  | Title  | Quantity | Price')
        while hientai != None:
            print(" |  ".join([str(char) for char in hientai.data]))
            hientai = hientai.next


    def luu(self,file_out):
        hientai = self.dau
        file_ou = open(file_out,"w")
        file_ou.close()
        while hientai != None:
            file_ou = open(file_out,"a")
            file_ou.write((" ".join([str(char) for char in hientai.data]) + "\n"))
            file_ou.close()
            hientai = hientai.next
    #Choice 5: Search by ID
    def tim(self,id_tim):
        hientai = self.dau
        truoc = None
        kk = 0
        while hientai != None:
            if str(id_tim) == str(hientai.data[0]):
                print('ID  | Title  | Quantity | Price')
                print(" |  ".join([str(char) for char in hientai.data]))
                kk = 1
                break
            hientai = hientai.next
        if int(kk) < 1:
            print("ID is not in the dataset!")
        try:
            return hientai.data[2]
        except:
            pass

    def queue(self):
        hientai = self.dau
        lst = []
        print('ID  | Title  | Quantity | Price')
        while hientai != None:
            lst.append(hientai.data)
            hientai = hientai.next
        while len(lst) > 0:
            val = lst.pop()
            print(" |  ".join([str(char) for char in val]))

    #Choice 6: Deleted by ID
    def xoa(self,giatri):
        hientai = self.dau
        truoc = None
        kk = 0
        while hientai != None:
            if str(giatri) == str(hientai.data[0]):
                print('ID  | Title  | Quantity | Price')
                print(" |  ".join([str(char) for char in hientai.data]))
                kk = 1
                break
            hientai = hientai.next


        hientai = self.dau
        truoc = None
        while hientai != None and str(giatri) != str(hientai.data[0]):

            truoc = hientai
            hientai = hientai.next

        if hientai == self.dau:
            self.dau = self.dau.next
        else:
            truoc.next = hientai.next

        if int(kk) < 1:
            print("ID is not in the dataset!")

    def sapxep(self):
        hientai = self.dau
        lst = []
        while hientai != None:
            lst.append(hientai.data)
            hientai = hientai.next
        print('ID  | Title  | Quantity | Price')
        lst = sorted(lst)
        for i in lst:
            print(" |  ".join([str(char) for char in i]))



    def queue(self):
        hientai = self.dau
        lst_queue = []
        print('ID  | Title  | Quantity | Price')
        while hientai != None:
            lst_queue.append(hientai.data)
            print(" |  ".join([str(char) for char in hientai.data]))
            hientai = hientai.next

    def stack(self):
        hientai = self.dau
        lst = []
        print('ID  | Title  | Quantity | Price')
        while hientai != None:
            lst.append(hientai.data)
            hientai = hientai.next
        while len(lst) > 0:
            val = lst.pop()
            print(" |  ".join([str(char) for char in val]))
        
#Choice 1: Load data from file and display
def file_input():
    while True:
        try:
            file_in = input("Please enter the find path:")
            file_in = open(file_in,"r")
            for i in file_in:
                i = i.split()
                kq.them(i)
            print("The file is loaded successfully!")
            break
        except:
            print("File-path is not correct!")



#Choice 2: Input & add to the end
def themsp():
    ID = input("Please enter the new product ID:")
    ten = input("Please enter the product's name:")
    sl = int(input("Please enter the product's quantity:"))
    gia = float(input("Please enter the product's price:"))
    kq.them([ID,ten,sl,gia])



#Choice 4: Save product list to file
def outfile():
    file_out = input("Please enter the output path:")
    kq.luu(file_out)
    print("The file is saved successfully!")


#Biểu diễn số lượng sản phẩm (đang ở hệ đếm cơ số 10) của trong Linked List ra hệ đếm nhị phân bằng phương pháp đệ quy.
def nhiphan(so_luong):
    if int(so_luong) == 0:
        return 0
    sodu = int(so_luong)%2
    return str(sodu) + str(nhiphan(so_luong//2))


if __name__ == "__main__":
    kq = dslienket()
    while True:
        print("""
        +-------------------Menu------------------+

        1. Load data from file and display

        2. Input & add to the end.

        3. Display data

        4. Save product list to file.

        5. Search by ID

        6. Delete by ID

        7. Sort by ID.

        8. Convert to Binary 

        9. Load to stack and display

        10. Load to queue and display.

        Exit:

        0. Exit

        +-----------------------------------------.+
        """)

        select = input("Mời bạn nhập chức năng mong muốn: ")
        if str(select).isdigit():
            select = int(select)
            if select == 1:
                file_input()
            elif select == 2:
                themsp()
            elif select == 3:
                kq.print()
            elif select == 4:
                outfile()
            elif select == 5:
                id_tim = input("Please enter the ID: ")
                kq.tim(id_tim)
            elif select == 6:
                giatri = input("Please enter the ID:")
                kq.xoa(giatri)
            elif select == 7:
                kq.sapxep()
            elif select == 8:
                id_tim = input("Please enter the ID:")
                try:
                    print("Convert quantity to binary: ",nhiphan(int(kq.tim(id_tim)))[::-1][1:])
                except:
                    kq.tim(id_tim)
            elif select == 9:
                kq.stack()
            elif select == 10:
                kq.queue()
            elif select == 0:
                exit()
            else:
                print("Chức năng không tồn tại, vui lòng chọn lại chức năng mong muốn.")
        else:
            print("Thông tin nhập vào không hợp lệ, vui lòng nhập lại!")




