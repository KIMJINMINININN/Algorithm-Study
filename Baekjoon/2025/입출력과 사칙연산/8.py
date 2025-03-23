def yearReturnFunc(year):
    return year - 543

year = int(input("년도를 입력해주세요: "))
print(year - 543)

if 1000 <= year <= 3000:
    print(year - 543)
else:
    print("년도를 정확하게 입력해주세요.")