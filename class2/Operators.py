1. Arithmetic Operators  #(Mathematical operations)

a = 10
b = 3

print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.3333
print(a // b)  # Floor Division: 3
print(a % b)   # Modulus (Remainder): 1
print(a ** b)  # Exponentiation: 10^3 = 1000


2. Assignment Operators  #(Value assign karne ke liye)

x = 5
x += 3   # x = x + 3 → 8
x -= 2   # x = x - 2 → 6
x *= 4   # x = x * 4 → 24
x /= 3   # x = x / 3 → 8.0
x %= 5   # x = x % 5 → 3.0
x **= 2  # x = x ** 2 → 9.0
x //= 3  # x = x // 3 → 3.0


3. Comparison Operators  #(Dono values compare karne ke liye)

a = 10
b = 5

print(a == b)  # False (Equal to)
print(a != b)  # True (Not equal to)
print(a > b)   # True (Greater than)
print(a < b)   # False (Less than)
print(a >= b)  # True (Greater than or equal to)
print(a <= b)  # False (Less than or equal to)


4. Logical Operators  #(True ya False check karne ke liye)

x = True
y = False

print(x and y)  # False (Dono true hone chahiye)
print(x or y)   # True (Agar ek bhi true ho)
print(not x)    # False (True ko False aur False ko True banata hai)


5. Identity Operators #(is aur is not)

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is c)      # True (Same memory location)
print(a is b)      # False (Alag memory locations)
print(a == b)      # True (Values same hain)
print(a is not b)  # True (Memory location different hai)


6. Membership Operators #(in aur not in)

fruits = ["apple", "banana", "mango"]

print("banana" in fruits)   # True (banana list mein hai)
print("grape" not in fruits) # True (grape list mein nahi hai)


7. Bitwise Operators # (Binary numbers pe operations)

a = 5  #  0101 (Binary)
b = 3  #  0011 (Binary)

print(a & b)   # 1 (AND → 0001)
print(a | b)   # 7 (OR  → 0111)
print(a ^ b)   # 6 (XOR → 0110)
print(~a)      # -6 (NOT → 1010 in 2’s complement)
print(a << 1)  # 10 (Left shift → 1010)
print(a >> 1)  # 2 (Right shift → 0010)