
string = [input() for _ in range(3)]

for i in range(3):
    if string[i].isdigit():
        num = int(string[i]) + (3 - i)
        break

if num % 15 == 0:
    result = "FizzBuzz"
elif num % 3 == 0:
    result = "Fizz"
elif num % 5 == 0:
    result = "Buzz"
else:
    result = num

print(result)