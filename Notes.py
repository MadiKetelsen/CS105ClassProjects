#More Definite Loops and Accumulator Pattern (2-13-25)
for myChar in 'hello':
    print(myChar)
#prints it verticle
for myChar in 'hello':
    print(myChar, end=", ")
#prints string all on one line with commas and a space in between
for myChar in ['red', 3.14, 5]:
    print(myChar, end=", ")
#prints list all on one line with commas and a space in between
for num in range(5):
    print(num, end= ".")
#prints list of numbers 0-4
range(4, 8)
#puts out 4,5,6,7,
range(-5, 10, 2)
# prints out -5, 1, 7
def main():
    product = 1
    for num in range(2, 10, 3):
        print('num is', num)
        product = product * num
    print()
    print('product is', product)
main()
#prints num is 5, num is 8, product is 80

#More with Numbers and Random
int(-3.4)
#rounds to -3
float(2.5)
#doesn't round
abs(-3)
#absolute value gives back 3
round(3.7)
#gives back 4 and rounds to the nearest even integer
round(4.9094387, 3)
#rounds the first number to whatever many decimal places the 2nd number is. This spits back 4.909
#there is a math library in your photos so don't delete that

