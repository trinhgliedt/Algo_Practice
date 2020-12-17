Python Program to Find Armstrong Number in an Interval
# Example to find all Armstrong numbers between two integers. To solve this problem, we have used nested loop and if statement.
# A positive integer is called an Armstrong number of order n if

# abcd... = an + bn + cn + dn + ...
# For example,

# 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.


# Source Code
# Program to check Armstrong numbers in a certain interval

lower = 100
upper = 2000

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
# Output

# 153
# 370
# 371
# 407
# 1634
# Here, we have set the lower limit 100 in variable lower and upper limit 2000 in variable upper. We have used for loop to iterate from variable lower to upper. In iteration, the value of lower is increased by 1 and checked whether it is an Armstrong number or not.

# You can change the range and test out by changing the variables lower and upper. Note, the variable lower should be lower than upper for this program to work properly.