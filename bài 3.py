def ho_ten(sothuannghich):
    str1 = str(sothuannghich);    
    str2 = str1[::-1]; 
    if (str1 == str2):
        return ("là số thuận nghịch")
    else:
        return ("không là số thuận nghịch")
ten = str(len(input("tên: Tiep ")))
dem=str(len(input("dem: Nang  ")))
ho=str(len(input("ho: Bui ")))

sothuannghich=ten+dem+ho
print("họ tên đầy đủ; ",ho +dem + ten)
print(sothuannghich ,"là",ho_ten(sothuannghich))