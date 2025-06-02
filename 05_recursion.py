'''
facorial(1) = 1
facorial(2) = 2 X 1
facorial(3) = 3 X 2 X 1
facorial(4) = 4 X 3 X 2 X 1
facorial(5) = 5 X 4 X 3 X 2 X 1

facorial(n) = n X n-1 X........3 X 2 X 1
facorial(n) = n * factorial(n-1)

'''

# # Recursive function
# def show(n):
#     if(n==0):    # :=Base case
#         return
#     print(n)
#     show(n-1)

# show(5) # 5,4=n-1,3=n-2,2=n-3,1


def factorial(n):
    if(n==0 or n==1):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")


 