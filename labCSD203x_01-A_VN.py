#Lab 1.1 - Số Fibonacci bé
def Fibonacci(n):
	if n >= 0 and n <= 45:
		if n <= 1:
			return n
		else:
			return Fibonacci(n - 1) + Fibonacci(n - 2)

a = int(input())
print(Fibonacci(a))

#Lab 1.2 - Chữ số cuối của một số Fibonacci lớn
n = int(input())
def Fibonacci(n):
	if n >= 0 and n <= 10**7:
		f0 = 0
		f1 = 1
		fn = 0
		for i in range(1,n):
			fn = f0 + f1
			f0 = f1
			f1 = fn
		print(fn%10)
Fibonacci(n)


#Lab 2.1 - Đổi tiền
m = int(input())
def soluongtien(m):
	if m < 1 or m > 10**3:
		quit()

	lst = [10,5,1]
	a = 0
	for i in lst:
		a += m//i
		m = m%i
		if m == 0:
			break
	return a
print(soluongtien(m))


#Lab 2.2 - Tối đa giá trị của chiến lợi phẩm
# Uses python3
import sys

def get_optimal_value(n,w):
	td = dict()
	for i in range(n):
		vp = input()
		td.update({int(vp.split()[0])/int(vp.split()[1]):int(vp.split()[1])})
	st = 0
	while True:
		if  w <= td[max(td)]:
			st += w*max(td)
			break
		else:
			st += (td[max(td)]) * max(td)
			w = w - td[max(td)]
			td.pop(max(td))
	return round(st,4)


if __name__ == "__main__":
	tt = input()
	n = int(tt.split()[0])
	w = int(tt.split()[1])
	print(get_optimal_value(n,w))


#Lab 2.3 - Tối đa doanh thu từ vị trí đặt quảng cáo trực tuyến
#Uses python3

import sys
def max_dot_product(n):
    res = 0
    a = input().split()
    b = input().split()
    while (n > 0):
        res += (int(max(a))*int(max(b)))
        a.remove(max(a))
        b.remove(max(b))
        n = n - 1
    return res
        

if __name__ == '__main__':
    n = int(input())
    print(max_dot_product(n))



#Lab 2.4 - Thu thập chữ ký
def doanduong(n):
	lst = []
	for i in range(n):
		tt = input().split()
		set1 = set()
		for i1 in range(int(tt[0]),int(tt[1]) + 1):
			set1.add(i1)
		lst.append(set1)
	def vonglap(lst2):
		lst = list(lst2)
		lst1 = lst2
		for i2 in lst:
			for i3 in lst:
				if len(i3&i2) > 0:
					try:
						lst1.remove(i2)
						lst1.remove(i3)
					except:
						pass
					if i3&i2 not in lst1:
						lst1.append(i3&i2)
					break
				
		if lst1 == lst:
			return lst1
		else:
			return vonglap(lst1)
	kqq = vonglap(lst)
	kq = ""
	for x in range(len(kqq)):
		kq += str(max(kqq[x])) + " "
	print(len(kqq))
	print(kq)

if __name__ == '__main__':
	n = int(input())
	doanduong(n)


#Lab 2.5 - Tối đa số lượng giải thưởng trong một cuộc thi
def phatkeo(n):
	lst = []
	skeo = 1
	while True:
		if n - skeo <= skeo:
			skeo = n
			lst.append(skeo)
			break
		lst.append(skeo)
		n = n - skeo
		skeo += 1
	kq = ""
	for i in range(len(lst)):
		kq += str(lst[i]) + " "

	print(len(lst))
	print(kq)




if __name__ == '__main__':
	n = int(input())
	phatkeo(n)




#6 1 5 8 12 13 16
#6 8 1 23 1 11 5
#Lab 3.1 - Tìm kiếm nhị phân
def timkiem(a,b):
	a = a.split()
	b = b.split()
	a = a[1:]
	b = b[1:]
	kq = ""
	for i in b:
		y = 0
		c = a
		x = len(c)//2
		while True:
			if len(c) == 1 and c[x] != i:
				y = -1
				break
			else:
				if int(c[x]) < int(i):
					y += x
					c = c[x:]
					x = len(c)//2
				elif int(c[x]) > int(i):
					c = c[:x]
					x = len(c)//2
				elif c[x] == i:
					y += x
					break
		kq += str(y) + " "
	print(kq)

if __name__ == '__main__':
	a = input()
	b = input()
	timkiem(a,b)


#Lab 3.2 - “Phần tử đa số”
#Yêu cầu chia làm 2 mảng đệ quy
def timkiem(x,ds):
	kq = 0
	for i in ds:
		if int(x) == int(i):
			kq += 1
	return kq

if __name__ == '__main__':
	n = int(input())
	a = input().split()
	a1 = a[:len(a)//2]
	a2 = a[len(a)//2:]
	Output = 0
	for i in a:
		daso = timkiem(i,a1) + timkiem(i,a2)
		if daso > len(a)//2:
			Output = 1
			break
	print(Output)



#Lab 4.1 - Máy tính nguyên thủy

def main(n):
	if n == 1:
		pass
	else:
		ls = [0]*(n + 1)
		t = [2,3]
		for i in range(2, n + 1):
			kq = ls[i - 1] + 1
			if n == i:
				ff = i - 1
			for j in t:
				if i%j == 0 and ls[int(i/j)] < kq :
					kq = ls[int(i/j)] + 1
					if n == i:
						ff = i/j
			ls[i] = kq
		lst.append(int(ff))
		return main(int(ff))

if __name__ == '__main__':
	n = int(input())
	lst = []
	main(n)
	print(len(lst))
	lst = lst[::-1]
	print(" ".join([str(char) for char in lst]),n)

#Lab 4.2 - Lấy nhiều vàng nhất có thể
def main(W,n,lst):
	kk = [0]*(W+1)
	for i in range(1,W + 1):
		kq = kk[i - 1] + 1
		for j in lst:
			if i < int(j):
				continue
			if kk[i - int(j)] + 1 < kq:
	
				kq = kk[i - int(j)] + 1

		kk[i] = kq
	kq = len(kk) - 1
	while True:
		if kk[kq] < n:
			print(kq)
			break
		kq -= 1

if __name__ == '__main__':
	balo = input().split()
	lst = input().split()
	W = int(balo[0])
	n = int(balo[1])
	main(W,n,lst)



#Lab 5.1 - Sắp xếp 3-phân đoạn
def sapxep(lst):
	lst1 = []
	lst2 = []
	lst3 = []
	if len(lst) <= 1:
		return lst
	h = lst[len(lst)//2]
	for i in lst:
		if int(i) < int(h):
			lst1.append(i)
		elif int(i) > int(h):
			lst3.append(i)
		else:
			lst2.append(i)


	lstn = lst1 + lst2 + lst3

	if lstn == lst:
		return lst
	else:
		return sapxep(lst1) + lst2 + sapxep(lst3)
if __name__ == '__main__':
	n = int(input())
	lst = input().split()
	kq = sapxep(lst)
	print(" ".join([str(char) for char in kq]))

#Lab 7.1 - Kiểm tra các dấu ngoặc trong đoạn mã


def find_mismatch(text):
    stack = []
    for i, char in enumerate(text):
        if char in '({[':
            stack.append((char, i))
        elif char in ')}]':
            if not stack:
                return i + 1
            open_char, open_index = stack.pop()
            if (open_char == '(' and char != ')') or  (open_char == '[' and char != ']') or (open_char == '{' and char != '}'):
                return i + 1
    if stack:
        return stack[0][1] + 1
    return 'Success'


a = input()
print(find_mismatch(a))


#Lab 8.1 - Tính chiều caoclass ĐỉnhCây:
class ĐỉnhCây:
    def __init__(self, giá_trị):
        self.giá_trị = giá_trị
        self.con = []

def xây_dựng_cây(cha):
    đỉnh = [ĐỉnhCây(i) for i in range(len(cha))]
    gốc = None
    for i, cha_của_đỉnh in enumerate(cha):
        if cha_của_đỉnh == -1:
            gốc = đỉnh[i]
        else:
            đỉnh[cha_của_đỉnh].con.append(đỉnh[i])
    return gốc

def tìm_chiều_cao(đỉnh):
    if not đỉnh.con:
        return 1
    chiều_cao_con_lớn_nhất = 0
    for con in đỉnh.con:
        chiều_cao_con_lớn_nhất = max(chiều_cao_con_lớn_nhất, tìm_chiều_cao(con))
    return chiều_cao_con_lớn_nhất + 1

# Đọc dữ liệu đầu vào
số_đỉnh = int(input())
cha_của_đỉnh = list(map(int, input().split()))

# Xây dựng cây từ mô tả
gốc = xây_dựng_cây(cha_của_đỉnh)

# Tính và in ra chiều cao của cây
chiều_cao = tìm_chiều_cao(gốc)
print(chiều_cao)


#Lab 9.1 - Duyệt cây nhị phân

class caynhiphan:
    def __init__(self, khoa, trai, phai):
        self.khoa = khoa
        if trai != -1:
            self.trai = trai
        else:
            self.trai = None
        if phai != -1:
            self.phai = phai
        else:
            self.phai = None

def them(nut):
    if nut.phai:
        nut.phai = lst[nut.phai]
        them(nut.phai)
    if nut.trai:
        nut.trai = lst[nut.trai]
        them(nut.trai)


def PrintTree(nut):
    if nut.trai:
        PrintTree(nut.trai)
    lst1.append(nut.khoa)
    if nut.phai:
        PrintTree(nut.phai)
def PrintTree1(nut):
    lst2.append(nut.khoa)
    if nut.trai:
        PrintTree1(nut.trai)
    if nut.phai:
        PrintTree1(nut.phai)
def PrintTree2(nut):
    if nut.trai:
        PrintTree2(nut.trai)
    if nut.phai:
        PrintTree2(nut.phai)
    lst3.append(nut.khoa)

n = int(input())
lst = []
for i in range(n):
    moi_dinh = input().split()
    lst.append(caynhiphan(int(moi_dinh[0]), int(moi_dinh[1]), int(moi_dinh[2])))

Goc = lst[0]
them(Goc)
lst1 = []
lst2 = []
lst3 = []
PrintTree(Goc),PrintTree1(Goc),PrintTree2(Goc)
print(" ".join([str(char) for char in lst1]))
print(" ".join([str(char) for char in lst2]))
print(" ".join([str(char) for char in lst3]))


#Lab 10.1 - Chuyển đổi mảng thành heap

def min_heapify(mang, n, i, hoan_doi):
    nho_nhat = i
    trai = 2 * i + 1
    phai = 2 * i + 2

    # Tìm nút con có giá trị nhỏ nhất để đổi chỗ với nút cha
    if trai < n and mang[trai] < mang[nho_nhat]:
        nho_nhat = trai

    if phai < n and mang[phai] < mang[nho_nhat]:
        nho_nhat = phai

    # Nếu nút con nhỏ nhất khác nút cha, thực hiện hoán đổi và ghi nhận hoán đổi
    if nho_nhat != i:
        mang[i], mang[nho_nhat] = mang[nho_nhat], mang[i]
        hoan_doi.append((i, nho_nhat))
        min_heapify(mang, n, nho_nhat, hoan_doi)

def xay_dung_min_heap(mang):
    n = len(mang)
    hoan_doi = []

    # Xây dựng min-heap bằng cách gọi min_heapify cho từng nút cha từ cuối cùng đến đầu mảng
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(mang, n, i, hoan_doi)

    return hoan_doi

n = int(input())  # Nhập số lượng phần tử trong mảng
mang = list(map(int, input().split()))  # Nhập mảng số nguyên

hoan_doi = xay_dung_min_heap(mang)  # Xây dựng min-heap từ mảng

print(len(hoan_doi))  # In ra số lần hoán đổi cần thiết để xây dựng min-heap
for swap in hoan_doi:
    print(swap[0], swap[1])  # In ra các cặp hoán đổi tương ứng

#Lab 10.2 - Xử lý song song


def thread(lst,lst1):
	lst = lst[::-1]
	i = 0
	while (len(lst) > 0):
		for x in range(len(lst1)):
			if i == int(lst1[x]):
				lst1[x] = int(lst1[x]) + int(lst.pop())
				print(x,i)
		i += 1

if __name__ == "__main__":
	n = int(input().split()[0])
	lst = input().split()
	lst1 = [0]*n
	thread(lst,lst1)


#Lab 11.1 – Danh bạ điện thoại
def danh_ba(n):
	for i in range(n):
		a = input().split()
		if a[0] == "add":
			ds[a[1]] = a[2]
		elif a[0] == "find":
			if len(ds) > 0 and len(lst) < 1:
				lst.append(len(ds))
			if a[1] in ds :
				lst.append(ds[a[1]])
			else:
				lst.append("not found")
		elif a[0] == "del":
			if a[1] in ds :
				ds.pop(a[1])
			else:
				pass

if __name__ == '__main__':
	ds = dict()
	lst = []
	n = int(input())
	danh_ba(n)
	for item in lst:
		print(item)




#Lab 11.2 - Hashing (Băm) với chain (chuỗi)
        
def checkk(string,check):
    h = 0
    kq = 0
    for c in string:
        kq += 263**h*ord(c)
        h += 1
    if (kq%1000000007)%5 == int(check):
        lst1.append(string)
lst = list()
lst2 = list()
m = int(input().strip())
n = int(input().strip())
for i in range(n):
    query = input().strip().split()
    if query[0] == 'add':
        lst2.append(query[1])
    elif query[0] == 'del':
        if query[1] in lst2:
            lst2.remove(query[1])
    elif query[0] == 'find':
        if query[1] in lst2:
            lst.append("yes")
        else:
            lst.append("no")
    elif query[0] == 'check':
        lst1 = []
        for string in lst2:
            checkk(string,(query[1]))
        lst.append(" ".join([str(char) for char in lst1]))


for item in lst:
    if len(item) < 1:
        continue
    print(item)


#Lab 11.3 - Tìm pattern (mẫu string) trong văn bản
def RabinKarp(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    d = 1
    q = 1
    h = (d**(pattern_len - 1))%q
    p = 0
    t = 0
    result = []
    for i in range(pattern_len):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(text_len - pattern_len + 1):
        if p == t:
            match = True
            for j in range(pattern_len):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                result.append(i)
        if i < text_len - pattern_len:
            t = (t - h * ord(text[i])) % q
            t = (t * d + ord(text[i + pattern_len])) % q
            t = (t + q) % q
    return result

if __name__ == '__main__':
    pattern = input()
    text = input()
    result = RabinKarp(text, pattern)
    print(*result)



#Lab 12.1 - Tìm lối thoát khỏi một mê cung
def DFS(graph, u, v, visited):
    visited[u] = True
    if u == v:
        return True
    for i in graph[u]:
        if not visited[i]:
            if DFS(graph, i, v, visited):
                return True
    return False

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
u, v = map(int, input().split())
visited = [False] * (n+1)
if DFS(graph, u, v, visited):
    print(1)
else:
    print(0)

#Lab 12.2 - Thêm lối thoát cho mê cung
def dfs(graph, v, visited):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
visited = [False] * n
count = 0
for i in range(n):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1

print(count)

#Lab 13.1 - Tính số chặng bay tối thiểu
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Đọc hai đỉnh u và v từ input
u, v = map(int, input().split())

# Sử dụng BFS để tìm đường ngắn nhất từ u đến v
vis = [False] * (n+1)
dis = [-1] * (n+1)
queue = [u]
vis[u] = True
dis[u] = 0

while queue:
    current = queue.pop(0)
    for n in graph[current]:
        if not vis[n]:
            vis[n] = True
            dis[n] = dis[current] + 1
            queue.append(n)
        if n == v:
            print(dis[v])
            exit()

# Nếu không tìm thấy đường đi từ u đến v, xuất ra -1
print(-1)


#Lab 13.2 - Kiểm tra xem một đồ thị có phải là lưỡng phân không
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def is_bipartite(graph):
    n = len(graph)
    colors = [0] * n

    def dfs(node, color):
        colors[node] = color
        for j in graph[node]:
            if colors[j] == color:
                return False
            if colors[j] == 0 and not dfs(j, -color):
                return False
        return True

    for i in range(n):
        if colors[i] == 0 and not dfs(i, 1):
            return 0
    return 1


print(is_bipartite(graph))




#Lab 14.1 - Tính chi phí tối thiểu cho một chuyến bay
m,n = map(int,input().split())
dothi = [[0]*(m+1) for _ in range(m+1)]
for _ in range(n):
	u1, v1, t1 = map(int,input().split())
	dothi[u1][v1] = t1

kq = dict()
for i in range(1,n+1):
	kq[i] = 9999
u,v =  map(int,input().split())
vip = 0
for i in range(1,m+1):
	kq1 = dict()
	for x in range(1,m+1):
		if dothi[u][x] > 0:
			if int(dothi[u][x]) + int(vip) < int(kq[x]):
				kq[x] = int(dothi[u][x]) + int(vip)
				kq1[x] = int(dothi[u][x]) + int(vip)

	if len(kq1) > 0:
		u, vip1 = min(kq1.items(), key=lambda x: x[1])
		vip += vip1


if kq[v] > 9998:
	print("-1")
else:
	print(kq[v])



#Lab 14.2 - Phát hiện sự bất thường trong tỷ giá hối đoái
INF = 10**9

def Bell(n, edges, source):
    distance = [INF] * n
    distance[source] = 0

    for i in range(n - 1):
        for u, v, w in edges:
            if distance[u] != INF and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    for u, v, w in edges:
        if distance[u] != INF and distance[u] + w < distance[v]:
            return 1
    return 0

n, m = map(int, input().split())
edges = []

for i in range(m):
    u, v, w = map(int, input().split())
    edges.append((u - 1, v - 1, w))

print(Bell(n, edges, 0))




#Lab 15.1 - Tìm tất cả các lần xuất hiện của một pattern trong một string

def tim_vi_tri_chuoi_con(pattern, genome):
    vi_tri = []
    do_dai_pattern = len(pattern)
    do_dai_genome = len(genome)
    
    for i in range(do_dai_genome - do_dai_pattern + 1):
        if genome[i:i+do_dai_pattern] == pattern:
            vi_tri.append(i)
    
    return vi_tri

# Đọc input
chuoi_con = input()
chuoi_nguon = input()

# Tìm và in ra các vị trí xuất hiện của chuỗi con trong chuỗi nguồn
vi_tri_chuoi_con = tim_vi_tri_chuoi_con(chuoi_con, chuoi_nguon)
for vi_tri in vi_tri_chuoi_con:
    print(vi_tri, end=' ')
