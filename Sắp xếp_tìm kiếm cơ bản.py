
#Choice 1: Manual Input
#Nhập một dãy các số thực gồm có n số (n<=20)  lưu vào tệp INPUT.TXT
def ManualInput():
	day_so = input("Please enter input number of elements: ")
	file = open("INPUT.TXT","w")
	file.write(day_so)
	file.close()
	

#Choice 2: File input
#OUTPUT :Đọc dữ liệu từ tệp INPUT.TXT lưu vào mảng 1 chiều a và hiển thị ra màn hình
def Fileinput():
	while True:
		try:
			tep = input("Please enter the file path: ")
			file = open(tep,"r")
			break
		except:
			pass
	filec = file.read()
	filem = []
	for i in filec.split():
		filem.append(float(i))
	filem = tuple(filem)
	print(filec)
	return filem



#Choice 3: Bubble sort
# Hiển thị ra màn hình kết quả sắp xếp các phần tử trong mảng a ở câu 2 theo thứ tự tăng dần, theo từng bước của thuật toán Bubble Sort (mỗi bước hiển thị lên 1 dòng) và lưu vào tệp OUTPUT1.TXT
def Bubblesort(lst):
	lst = list(lst)
	file = open("OUTPUT1.TXT","w")
	file.close()
	while True:
		n = 0
		for i in range(len(lst) - 1):
			if float(lst[i]) > float(lst[i + 1]):
				b = lst[i]
				lst[i] = lst[i + 1]
				lst[i + 1] = b
				n += 1
		file1 = open("OUTPUT1.TXT","a")
		file1.write(" ".join([str(char) for char in lst]) + "\n")
		file1.close()
		if n == 0:
			return lst
			break



#Choice 4: Selection sort
#Hiển thị ra màn hình kết quả sắp xếp các phần tử trong mảng a ở câu 2 theo thứ tự tăng dần, theo từng bước của thuật toán Selection Sort (mỗi bước hiển thị lên 1 dòng) và lưu vào tệp OUTPUT2.TXT
def Selectionsort(lst):
	lst = list(lst)
	file = open("OUTPUT2.TXT","w")
	file.close()
	for i in range(len(lst) - 1):
		Min = lst[i]
		h = i
		for j in range(i,len(lst)):
			if float(lst[j]) < float(Min):
				Min = lst[j]
				h = j
		b = lst[i]
		lst[i] = lst[h]
		lst[h] = b
		file1 = open("OUTPUT2.TXT","a")
		file1.write(" ".join([str(char) for char in lst]) + "\n")
		file1.close()

		print(" ".join([str(char) for char in lst]))


#Choice 5: Insertion sort
#Hiển thị ra màn hình kết quả sắp xếp các phần tử trong mảng a ở câu 2 theo thứ tự tăng dần, theo từng bước của thuật toán Insert Sort (mỗi bước hiển thị lên 1 dòng) và lưu vào tệp OUTPUT3.TXT
def Insertionsort(lst):
	lst = list(lst)
	file = open("OUTPUT3.TXT","w")
	file.close()
	for i in range(1,len(lst)):
		if lst[i] < lst[i - 1]:
			for j in range(i):
				if lst[i] < lst[j]:
					lst.insert(j,lst[i])
					lst.pop(i + 1)
					break
		file1 = open("OUTPUT3.TXT","a")
		file1.write(" ".join([str(char) for char in lst]) + "\n")
		file1.close()
		print(" ".join([str(char) for char in lst]))



#Choice 6: Linear Search
#Sử dụng phương pháp tìm kiếm tuần tự, hãy liệt kê ra màn hình chỉ số các phần tử (biết rằng phần tử đầu tiên có chỉ số là 0) trong mảng a  chưa được sắp xếp ở câu 2 có giá trị lớn hơn value (value là một số thực được nhập vào từ bàn phím), kết quả tìm được lưu vào dòng tiếp theo trong tệp OUTPUT4.TXT
def Searchvalue1(lst):
	lst = list(lst)
	value = float(input("Please enter searched input value: "))
	kq = []
	for i in range(len(lst)):
		if float(lst[i]) >= value:
			kq.append(i)
	print(" ".join([str(char) for char in kq]))
	file4 = open("OUTPUT4.TXT","w")
	file4.write(" ".join([str(char) for char in kq]))
	file4.close()


#Choice 7: Binary Search
#Sử dụng phương pháp tìm kiếm nhị phân, hãy tìm chỉ số phần tử đầu tiên có giá trị bằng value (value là một số thực được nhập vào từ bàn phím) trên mảng đã a đã được sắp xếp.
def Searchvalue2(lst):
	lst1 = Bubblesort(lst)
	value = float(input("Please enter searched input value: "))

	vitri = 0
	while True:
		n = len(lst1)//2
		if len(lst1) < 3:
			if float(lst1[0]) == value:
				print(vitri)
				break
			elif float(lst1[1]) == value:
				vitri += 1
				print(vitri)
				break
			else:
				print("Gía Trị Này Không Tồn Tại")
				break
		if float(lst1[n]) > value:
			lst1 = lst1[:n]
		elif float(lst1[n]) < value:
			lst1 = lst1[n:]
			vitri += n
		else:
			lst1 = lst1[:n + 1]


if __name__ == '__main__':
	while True:
		print("""
		+-------------------Menu------------------+

		|      1.Manual Input                 |

		|      2.File input                        |

		|      3.Bubble sort                    |

		|      4.Selection sort                 |

		|      5.Insertion sort                  |

		|      6.Search > value                |

		|      7.Search = value                |

		|      0.Exit                              |

		+-----------------------------------------.+

		 
		""")




		select = input("Mời bạn nhập chức năng mong muốn: ")
		if str(select).isdigit():
			select = int(select)
			if select == 1:
				ManualInput()
			elif select == 2:
				lst = Fileinput()
			elif select == 3:
				Bubblesort(lst)
				file1 = open("OUTPUT1.TXT","r")
				print(file1.read())
			elif select == 4:
				Selectionsort(lst)
			elif select == 5:
				Insertionsort(lst)
			elif select == 6:
				Searchvalue1(lst)
			elif select == 7:
				Searchvalue2(lst)
			elif select == 0:
				exit()
			else:
				print("Chức năng không tồn tại, vui lòng chọn lại chức năng mong muốn.")
		else:
			print("Thông tin nhập vào không hợp lệ, vui lòng nhập lại!")

	






