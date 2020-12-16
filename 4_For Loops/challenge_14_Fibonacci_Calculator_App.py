#For Loops Challenge 14:  Fibonacci Calculator App

print("Welcome to the Fibonacci Calculator App")

#Get user input
num = int(input("\nHow many digits of the Fibonacci Sequence would you like to compute: "))

#Compute the values of the fib
fib = [1,1]
for i in range(num-2):
    new_fib = fib[i] + fib[i+1]
    fib.append(new_fib)

#Display the fib values
print("\nThe first " + str(num) + " numbers of the Fibonacci Sequence are: ")
for number in fib:
    print(number)

#Compute the golden ratio
golden = []
for i in range(len(fib)-1):
    ratio = fib[i+1]/fib[i]
    golden.append(ratio)

#Display the golden ratio values
print("\nThe corresponding Golden Ratio values are: ")
for ratio in golden:
    print(ratio)

print("\nThe ratio of consecutive Fibonacci terms approaches Phi; 1.618...")
