# Program to find the element not making a pair
# Function to calculate the number that is odd occurring 
 
def OddOccurring(arr):
    res = 0
    for element in arr:
        res = res ^ element  #XOR checks if its same number
    return res
 
arr = []
n = int(input("Enter array size : "))
while(n):
    num = int(input("Enter number : "))
    arr.append(num)
    n-=1
 
print("\n\nOdd occurring number is : ",OddOccurring(arr))