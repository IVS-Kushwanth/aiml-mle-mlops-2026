#Using for loops
for i in range(1, 16):
    print(i)
    
#using while loops
i=1
while i < 16:
    print(i)
    i += 1
#using reverse loops 
for i in range (15, 0, -1):
    print(i)
#3 important cases
#1st case:
N =int(input("Enter a number: "))
for i in range(N,2, -3):
    print(i)
#2nd case:
N=int(input("Enter a number: "))
for i in range(-N,N+1,+5):
    print(i)
#3rd case:
M=int(input("Enter a number: "))
N=int(input("Enter a positive number: "))
p=abs(int(input("Enter a number: ")))
for i in range(M,-N,-p):
    print(i, end=" ")
    