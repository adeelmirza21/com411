print("program started")
print("enter an ASCII code")

ascii =int(input())

if ascii in range (32, 126):
    print(f"The character represented by the ASCII value {ascii} is: {chr(ascii)}")

else:
    print("the character cannot be displayed")

print("program has ended")