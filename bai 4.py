ten = input(" Nhập tên đầy đủ: buinangtiep ")
print(ten)
n = len(ten)
def isThuanNghich(n):
    str1 = str(n);     # ep kieu so n thanh chuoi
    str2 = str1[::-1]; # dao nguoc chuoi str1
    if (str1 == str2):
        return True;
    else:
        return False;
 
n = int(input("BUI NANG TIEP thi n = "));
print("Tổng các chữ số của", n , "là", isThuanNghich(n));
m = int(input("BUI NANG TIEP thi m = "));
print("Tổng các chữ số của", m , "là", isThuanNghich(m));
print("Tổng các chữ số của", n , "là", isThuanNghich(n));
ten = input(" Nhập tên và id sinh viên: Tiep 1451020235  ")
print(ten)
n = len(ten)
values=input(" chuỗi tạo ra ở câu a: ")
l=values.split(",")
t=tuple(l)
print (l)
print (t)