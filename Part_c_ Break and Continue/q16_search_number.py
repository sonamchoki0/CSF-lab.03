numbers = [2, 4, 6, 8, 10]
search_num = 8

print("List:", *numbers)
print(f"Searching for: {search_num}")

for num in numbers:
    if num == search_num:
        print("Number found")
        break
else:
    print("Number not found")