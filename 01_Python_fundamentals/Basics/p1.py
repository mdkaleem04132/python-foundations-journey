#basics of python 

print("hello world")

#variables

#data types
a = 10 #integer

b = 3.14 #float

c = "hello" #string

is_valid = True #boolean

add = None #null value


#operators

#mathematical operators
a = 10
b = 20
print(a+b)
print(a-b)
print(a*b)
print(a/b)


#comparison operators

x = 5
y = 10
print(x > y) #False
print(x < y) #True
print(x == y) #False
print(x != y) #True
print(x >= y) #False
print(x <= y) #True

#Assignment operators
a = 10
print(a) #10
a += 5 # equivalent to a = a + 5
print(a) #15
a -= 3 # equivalent to a = a - 3
print(a) #12
a *= 2 # equivalent to a = a * 2
print(a) #24
a /= 4 # equivalent to a = a / 4
print(a) #6.0


#logical operators

a = 10
b = 5

if a > 5 and b > 2:
    print("Both conditions are True")

a = 3
b = 8

if a > 5 or b > 5:
    print("At least one condition is True")

a = 4

if not (a > 5):
    print("Condition is False, so NOT makes it True")

age = 20
has_id = True

if age >= 18 and has_id:
    print("You are allowed")

if age < 18 or not has_id:
    print("You are not allowed")


# Python Operator Precedence (Highest → Lowest)

# 1. Parentheses
#    ( )

# 2. Exponentiation
#    **

# 3. Unary operators
#    +x, -x, ~x

# 4. Multiplication, Division, Floor Division, Modulus
#    *, /, //, %

# 5. Addition and Subtraction
#    +, -

# 6. Bitwise Shift
#    <<, >>

# 7. Bitwise AND
#    &

# 8. Bitwise XOR
#    ^

# 9. Bitwise OR
#    |

# 10. Comparison Operators
#    ==, !=, >, <, >=, <=

# 11. Assignment Operators
#    =, +=, -=, *=, /=, etc.

# 12. Logical NOT
#    not

# 13. Logical AND
#    and

# 14. Logical OR
#    or

# Note:
# - Parentheses () have the highest priority
# - 'not' > 'and' > 'or'
# - Use parentheses to make expressions clear and avoid confusion


# ==============================
# TYPE CONVERSION (Implicit)
# ==============================

# Python automatically converts one data type to another

a = 10        # int
b = 2.5       # float

c = a + b     # int is automatically converted to float
print(c)      # Output: 12.5
print(type(c))  # Output: <class 'float'>


# ==============================
# TYPE CASTING (Explicit)
# ==============================

# Manually converting one data type to another

# int to float
x = 5
y = float(x)
print(y)        # Output: 5.0
print(type(y))  # <class 'float'>


# float to int
a = 7.9
b = int(a)
print(b)        # Output: 7 (decimal part removed)
print(type(b))  # <class 'int'>


# int to string
num = 100
str_num = str(num)
print(str_num)        # Output: "100"
print(type(str_num))  # <class 'str'>


# string to int
s = "50"
num = int(s)
print(num)        # Output: 50
print(type(num))  # <class 'int'>


# string to float
s = "3.14"
f = float(s)
print(f)        # Output: 3.14
print(type(f))  # <class 'float'>


# ==============================
# IMPORTANT NOTES
# ==============================

# Invalid conversion will cause error
# Example:
# int("hello")  # ❌ ValueError

# Boolean conversion
print(bool(0))     # False
print(bool(1))     # True
print(bool(""))    # False
print(bool("Hi"))  # True


# avg of 2 numbers
num1 = 10
num2 = 20

avg = (num1 + num2) / 2
print("Average:", avg)


#assignment

# Take input
num = float(input("Enter a number: "))

# Get integer part and make it negative
int_part = -int(num)

# Get fractional part
fraction_part = num - int(num)

# Print results
print(int_part)
print("fraction part", fraction_part)
print()
print("hello world")
print()
