bin_numb=list(input("Input a binary number :"))
result = 0
for i in range(len(bin_numb)):
    digit = bin_numb.pop()
    if digit =='1':
        result = result + pow(2,i)
print("The decimal value of the number is " , result)
