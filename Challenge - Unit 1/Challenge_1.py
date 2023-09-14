#Unit 1 - Challenge 1:
#Implement a recursive function to calculate the factorial of a given number.


def fact(n):
  if (n < 2):
    return 1
  else:
    return n * fact(n - 1)


num = int(input("Enter number : "))
res = fact(num)
print("Factorial of {} is {}".format(num, res))
