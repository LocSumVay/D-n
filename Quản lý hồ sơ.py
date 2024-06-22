
#Lớp Person1 chứa thông tin và hành vi cần thiết cho mỗi hồ sơ nhân viên - Lớp Node để quản lý thông tin và hành  của vi mỗi node trong cây nhị phân tìm kiếm
class MyPerson:
    def __init__(self, id, name, dob, birthplace):
        self.id = id
        self.name = name
        self.dob = dob
        self.birthplace = birthplace
    
    def __str__(self):
        return f"{self.id}    {self.name}    {self.dob}    {self.birthplace}"
       
#Lớp Node chứa thông tin và  các hành vi cơ bản của một cây nhị phân tìm kiếm
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if self.left is None:
                self.left = Node(data)
            elif self.right is None:
                self.right = Node(data)
            else:
                if self.left.right:
                    self.right.insert(data)
                else:
                    self.left.insert(data)
#Choice 4: Breadth-First Traversal traverse
    def breadth_first_traversal(self):
        queue = [kq]
        while queue:
            node = queue.pop(0)
            try:
                print(node.data)
            except:
                pass
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
#Choice 5: Search by Person ID
    def timkiem(self,them):
        queue = [kq]
        n = 0
        while queue:
            node = queue.pop(0)
            try:
                if node.data.id == them:
                    print("""Search for ID = {}
    ID | Name | Day of Birth | Birthplace
    {}
    Please type anything to come back to the main menu!""".format(them,node.data))
                    n = 1
                    break
            except:
                pass

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if n == 0:
            print("""Search for ID = {}
"The searched ID is not valid".
Please type anything to come back to the main menu!""".format(them))

#Choice 3: Inorder traverse
    def Inorder(self):
        if self.left:
            self.left.Inorder()
        try:
            print(self.data)
        except:
            pass
        if self.right:
            self.right.Inorder()

#Choice 6: Delete by Person ID 
    def de_lete(self):
        if self.right:
            self.data = self.right.data
            self.right.de_lete()
        elif self.left:
            self.data = self.left.data
            self.left.de_lete()
        else:
            self.data = None
            del self.data
            return True

    def delete(self,xoa):
        if self.left:
            self.left.delete(xoa)
        if self.right:
            self.right.delete(xoa)
        try:
            if self.data.id == xoa:
                print("""Delete the person with ID = {}

        ID | Name | Day of Birth | Birthplace

        {}       

        Please type anything to come back to the main menu!""".format(xoa,self.data))
                self.de_lete()
                return True
        except:
            print("""Delete the person with ID = {}

"The searched ID is not valid".

Please type anything to come back to the main menu!""".format(xoa))
            
#Tim kiem  ID đã bị trùng  !

    def xet(self,xet,listt):
        if self.data is None:
            return True
        if self.left:
            self.left.xet(xet,listt)
        if self.right:
            self.right.xet(xet,listt)
        if self.data.id == xet:
            listt.append(self.data.id)
            return True




#- Lớp Main chứa code để tạo ra menu và thực hiện các chức năng của bài toán.
#Một số phương thức quan trọng của các lớp. (Ngoài các lớp, phương thức này sinh viên có thể thêm các lớp và phương thức nữa nếu cảm thấy cần thiết).
if __name__ == '__main__':
    kq = Node(None)
    while True:
        print("""+-------------------Menu------------------+

Person Tree:

1. Load the data from the file.

2. Insert a new Person.

3. Inorder traverse

4. Breadth-First Traversal traverse

5. Search by Person ID

6. Delete by Person ID

Exit:

0. Exit

+-----------------------------------------.+""")

        select = input("Mời bạn nhập chức năng mong muốn: ")
        if str(select).isdigit():
            select = int(select)
            if select == 1:
                while True:
                    file = input("Please enter the find path:")
                    try:
                        file = open(file)
                        break
                    except:
                        print("File-path is not correct!")
                for i in file:
                    j = i.split()
                    try:
                        kq.insert(MyPerson(int(j[0]),j[1],j[2],j[3]))
                    except:
                        pass
               
            elif select == 2:
                while True:
                    listt = []
                    idd = int(input("Please insert the New ID:"))
                    kq.xet(idd,listt)
                    if len(listt) > 0:
                        print("This ID has been chosen, please choose another ID!")
                        continue
                    else:
                        break
                name = input("Please insert the Name:")
                birthplace = input("Please insert the Birthplace:")
                date = input("Please insert the Birth of Date:")
                print("""New ID: {}

Name: {}

Birthplace: {}

Day of birth: {}

Please type anything to come back to the main menu!""".format(idd,name,birthplace,date))
                kq.insert(MyPerson(idd,name,date,birthplace))
            elif select == 3:
                print("ID | Name | Day of Birth | Birthplace")
                kq.Inorder()
                print("Please type anything to come back to the main menu!")
            elif select == 4:
                print("ID | Name | Day of Birth | Birthplace")
                kq.breadth_first_traversal()
                print("Please type anything to come back to the main menu!")
            elif select == 5:
                them = int(input("Please insert the ID:"))
                kq.timkiem(them)
            elif select == 6:
                xoa = int(input("Please insert the ID:"))
                kq.delete(xoa)
            elif select == 0:
                exit()
            else:
                print("Chức năng không tồn tại, vui lòng chọn lại chức năng mong muốn.")
        else:
            print("Thông tin nhập vào không hợp lệ, vui lòng nhập lại!")
