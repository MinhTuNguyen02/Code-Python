while True:
    n = int(input("Nhap nam sinh:"))
    if n > 1900 and n < 2024:
        break

print("Tuoi cua ban la",2024-n)