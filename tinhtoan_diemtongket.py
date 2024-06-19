# Hàm tinhtoan_diemtongket(): Tính điểm trung bình cho từng môn học của từng học sinh:
# Input là file "diem_chitiet.txt".
# Output là 1 dict: {"Mã học sinh" : {"Môn học" : Điểm trung bình}}.
def tinhdiem_trungbinh(file_name):
	danhsach = open(file_name)
	tep0 = danhsach.readline()
	tep = tep0.strip()
	for line in danhsach:
		line1 = line.split(";")
		if len(line1) < 2:
			continue
		diemtb = {"Toan": -1, "Ly": -1, "Hoa": -1, "Sinh": -
		    1, "Van": -1, "Anh": -1, "Su": -1, "Dia": -1}
		tep1 = str(line1[0])
		for monhoc in line1:
			if len(monhoc) < 2:
				continue
			monhoc = monhoc.split()
			for diemtp in monhoc:
				diemtp = diemtp.split(",")
				if len(diemtp) == 4:
					diemtp = round(int(diemtp[0])*5/100 + int(diemtp[1])*10 /
					               100 + int(diemtp[2])*15/100 + int(diemtp[3])*70/100, 2)
				elif len(diemtp) == 5:
					diemtp = round(int(diemtp[0])*5/100 + int(diemtp[1])*10/100 + int(
					    diemtp[2])*10/100 + int(diemtp[3])*15/100 + int(diemtp[4])*60/100, 2)
				else:
					diemtp = diemtp

				for diem_tung_mon in diemtb:
					if int(diemtb[diem_tung_mon]) < 0:
						diemtb[diem_tung_mon] = diemtp
						break
				tep1 = str(tep1) + ";" + str(diemtp)
		tep = str(tep) + "\n" + str(tep1)
		ketqua = {line1[0]: diemtb}
		print(ketqua)
	return tep

# Hàm luudiem_trungbinh(): Lưu điểm trung bình của từng học sinh vào 1 file txt:
# Input: Đường dẫn cho file ouput, dict điểm tổng kết.
# Output: File "diem_trungbinh.txt".
def luudiem_trungbinh(duong_dan_output,file_name):
	file = open(duong_dan_output, "w")
	file.write(str(tinhdiem_trungbinh(file_name)))


# Hàm main():
# Thực thi 2 hàm tinhtoan_diemtongket() và luudiem_trungbinh().
if __name__ == "__main__":
	file_name = "diem_chitiet.txt"
	duong_dan_output = "diem_trungbinh.txt"
	tinhdiem_trungbinh(file_name)
	luudiem_trungbinh(duong_dan_output,file_name)




