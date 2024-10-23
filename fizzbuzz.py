# add your code here
#print numbers 1-100
for i in range(1, 101):
#if dividable by 3 print Fizz
    if i%3==0:
        print("Fizz")
#if dividable by 5 print Buzz
    elif i%5==0:
        print("Buzz")
#if dividable by 3 & 5 print FizzBuzz
    elif i%3==0 and i%5==0:
        print("FizzBuzz")
#if not dividable by 3 5 or 3 & 5 print number
else:
    print(i)