import pandas as pd
import numpy as np
# Mở tệp, Nếu tệp tồn tại, bạn có thể in ra một thông báo xác nhận. Nếu tệp không tồn tại
# bạn nên cho người dùng biết rằng không thể tìm thấy tệp và nhắc lại họ.
while True:
	try:
		file_name = input("Enter a filename: ")
		file = open(file_name + ".txt")
		print("Successfully opened",file_name)
		break
	except:
		print("File cannot be found.")
		print("Successfully opened",file_name)

print("**** ANALYZING ****")
hople = []
khong_hople = []
#Lấy thông tin và tách ra
for i1 in file:
	i = i1.strip().split(",")
	if i[0][0] == "N":
		try:
			if int(i[0][1:]) > 0 and len(i[0]) == 9:
				if len(i) == 26:
					yy = 1
					for j in i[1:]:
						if j in ['A','B','C','D','']:
							continue
						else:
							print("Invalid line of data: does not contain exactly 26 values:")
							print(i1)
							khong_hople.append(i)
							yy = 0
							break
					if yy > 0:
						hople.append(i)
				else:
					print("Invalid line of data: N# is invali")
					print(i1)
					khong_hople.append(i)
			else:
				print("Invalid line of data: N# is invali")
				print(i1)
				khong_hople.append(i)
		except:
			print("Invalid line of data: N# is invali")
			print(i1)
			khong_hople.append(i)
	else:
		print("Invalid line of data: N# is invali")
		print(i1)
		khong_hople.append(i)
if len(khong_hople) < 1:
	print("No errors found!")

#Hiển thị thông báo

print("**** REPORT ****")
print("Total valid lines of data:",len(hople))
print("Total invalid lines of data:",len(khong_hople))
#Dùng thư viện Pandas để phân tích
data = pd.DataFrame(hople)
data.reset_index(drop=True)
columnsss = ["Name",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
data.columns = columnsss
#Chuỗi đáp án
answer_key = ['B', 'A', 'D', 'D', 'C', 'B', 'D', 'A', 'C', 'C', 'D', 'B', 'A', 'B', 'A', 'C', 'B', 'D', 'A', 'C', 'A', 'A', 'B', 'D', 'D']
              #1    2    3    4    5    6    7    8    9    10    11   12   13  14   15   16   17   18   19   20  21    22   23   24    25  
ket_qua = {}
#Tính điểm
for i in data.iloc:
	cau_hoi = 1
	diem = 0
	while (cau_hoi < 26):
		if i[cau_hoi] == "":
			diem = diem
		elif str(i[cau_hoi]) == str(answer_key[cau_hoi - 1]):
			diem += 4
		else:
			diem -= 1
		cau_hoi += 1

	ket_qua[i["Name"]] = diem
#Tìm giá trị trung vị
lst_trungvi = list(ket_qua.values())
n = len(lst_trungvi)
lst_trungvi.sort()
if n % 2 == 1:
	gt_trungvi = lst_trungvi[n//2]
else:
	gt_trungvi = (lst_trungvi[n//2 - 1] + lst_trungvi[n//2])/2
#Hiển thị thong báo
print("Mean (average) score:",(sum(ket_qua.values())/len(ket_qua)))
print("Highest score:",max(ket_qua.values()))
print("Lowest score:",min(ket_qua.values()))
print("Range of scores:",max(ket_qua.values()) - min(ket_qua.values()))
print("Median score:",int(gt_trungvi))
#tạo main
def tao_file(ket_qua,file_name):
	file_out = str(file_name) + "_grades.txt"
	for i in ket_qua:
		tep_file = open(file_out,"a")
		tep_file.write(str(i) + "," + str(ket_qua[i]) + "\n")
	print("đã tạo file")
tao_file(ket_qua,file_name)
