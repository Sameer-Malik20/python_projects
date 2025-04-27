num = int(input("Enter a number: "))

prime = True
for i in range (3,num):
    if num % i == 0:
        prime = False
        break

print(f"{num} is prime") if prime else print(f"{num} is not prime")
