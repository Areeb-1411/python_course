st = input("Enter a string with letters and digits: ")
count = 0
print("Even digits found:")
for i in st:
    if i.isdigit() and int(i) % 2 == 0:
        print(i, end=' ')
        count += 1

print("\nTotal even digits:", count)

