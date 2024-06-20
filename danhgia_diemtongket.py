
# Hàm xeploai_hocsinh():
# Phân loại học lực của từng học sinh theo điểm trung bình của từng môn và điểm trung bình chuẩn.
def xeploai_hocsinh(file_name):
	danhsach = open(file_name)
	xeploai = dict()
	for line in danhsach:
		line = line.split(";")
		if len(line) < 2:
			continue
		dtb_chuan = ((float(line[1]) + float(line[5]) + float(line[6]))*2 + float(line[2]) + float(line[3]) + float(line[4]) + float(line[7]) + float(line[8]))/11
		diemct = min(float(line[1]),float(line[2]),float(line[3]),float(line[4]),float(line[5]),float(line[6]),float(line[7]),float(line[8]))
		if dtb_chuan > 9 and diemct > 8:
			xeploai_tungmon = "Xuat Sac"
		elif dtb_chuan > 8 and diemct > 6.5:
			xeploai_tungmon = "Gioi"
		elif dtb_chuan > 6.5 and diemct > 5:
			xeploai_tungmon = "Kha" 
		elif dtb_chuan > 6 and diemct > 4.5:
			xeploai_tungmon = "TB Kha"
		else:
			xeploai_tungmon = "TB"
		xeploai[line[0]] = xeploai_tungmon
	return xeploai


# Hàm xeploai_thidaihoc_hocsinh():
# Phân loại theo tổng điểm trung bình của từng khối thi cho từng học sinh.
def xeploai_thidaihoc_hocsinh(file_name):
	danhsach = open(file_name)
	xeploai_daihoc = dict()
	for line in danhsach:
		line = line.split(";")
		if len(line) < 2:
			continue
		khoi_A = float(line[1]) + float(line[2]) + float(line[3])
		khoi_A1= float(line[1]) + float(line[2]) + float(line[6])
		khoi_B = float(line[1]) + float(line[3]) + float(line[4])
		khoi_C = float(line[5]) + float(line[7]) + float(line[8])
		khoi_D = float(line[1]) + float(line[5]) + float(line[6])*2
		if khoi_A >= 24:
			xeploai_A = 1
		elif khoi_A >= 18:
			xeploai_A = 2
		elif khoi_A >= 12:
			xeploai_A = 3
		else:
			xeploai_A = 4

		if khoi_A1 >= 24:
			xeploai_A1 = 1
		elif khoi_A1 >= 18:
			xeploai_A1 = 2
		elif khoi_A1 >= 12:
			xeploai_A1 = 3
		else:
			xeploai_A1 = 4
		
		if khoi_B >= 24:
			xeploai_B = 1
		elif khoi_B >= 18:
			xeploai_B = 2
		elif khoi_B >= 12:
			xeploai_B = 3
		else:
			xeploai_B = 4
		
		if khoi_C >= 21:
			xeploai_C = 1
		elif khoi_C >= 15:
			xeploai_C = 2
		elif khoi_C >= 12:
			xeploai_C = 3
		else:
			xeploai_C = 4

		if khoi_D >= 32:
			xeploai_D = 1
		elif khoi_D >= 24:
			xeploai_D = 2
		elif khoi_D >= 20:
			xeploai_D = 3
		else:
			xeploai_D = 4

		xeploai_daihoc[line[0]] = list((xeploai_A,xeploai_A1,xeploai_B,xeploai_C,xeploai_D))
	return xeploai_daihoc

# Hàm main():
# Thực thi 2 hàm xeploai_hocsinh() và xeploai_thidaihoc_hocsinh(), đồng thời ghi kết quả ra file "danhgia_hocsinh.txt".
# Output là file "danhgia_hocsinh.txt", với format giống với file "diem_chitiet.txt" như đề bài cho ban đầu.                         
if __name__ == "__main__": 
	file_name = "diem_trungbinh.txt"
	a = xeploai_hocsinh(file_name)
	b = xeploai_thidaihoc_hocsinh(file_name)
	print(a)
	print(b)
	kqq = '"Ma HS", "xeploai_TB chuan", "xeploai_A", "xeploai_A1", "xeploai_B ", "xeploai_C", "xeploai_D"'
	for i in a:
		c = b.get(i)
		hs = str(i) + ";" + str(a.get(i)) + ";" + str(c[0]) + ";" + str(c[1]) + ";" + str(c[2]) + ";" + str(c[3]) + ";" + str(c[4])
		kqq = str(kqq) + "\n" + str(hs)
	file_new = open("danhgia_hocsinh.txt" , "w")
	file_new.write(str(kqq))
