
#define two numbers
a=5
b=3
print("initial numbers:")
print(f"a={a}(binary:{bin(a)})")
print(f"b={b}(binary:{bin(b)})")
#bitwise AND
and_result=a&b
print("\nBitwise AND:")
print(f"{a}&{b}={and_result}(binary:{bin(and_result)})")
#bitwise OR
or_result=a|b
print("\nBitwise OR:")
print(f"{a}|{b}={or_result}(binary:{bin(or_result)})")
#bitwise XOR
xor_result=a^b
print("\nBitwise XOR:")
print(f"{a}^{b}={xor_result}(binary:{bin(xor_result)})")
#bitwise NOT
not_result=~a
print("\nBitwise NOT:")
print(f"~{a}={not_result}(binary:{bin(not_result)})")
#LEFT SHIFT
left_shift_result=a<<2
print("\nLEFT_SHIFT:")
print(f"{a}<<2={left_shift_result}(binary:{bin(left_shift_result)})")
#RIGHT SHIFT
right_shift_result=a>>2
print("\nRIGHT_SHIFT :")
print(f"{a}>>2={right_shift_result}(binary:{bin(right_shift_result)})")
