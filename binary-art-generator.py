#Select emoji
emoji = input("Please type a character to incorporate into the art. If you don't want one, just copy and paste ⬛.")

while True:
    if len(emoji) == 1:
        break
    emoji = input("Please only type one character.")

print()

#Select image length 
while True:
    length = input("Please enter a value from 1-5 for your picture length: ")
    
    if length.isdigit():
        length = int(length)
        if 1 <= length <= 5:
            break

    print("Please make sure your response is a digit between 1 and 5.")

print()

#Select text
text = input("Please enter the text you want to convert.")

#Convert to binary 
binary = ''.join(format(ord(c), '08b') for c in text)

#Replace bits
binary_art = binary.replace('1', emoji).replace('0', '⬜')

print()

#Print result
chunk_size = length * 8

for i in range(0, len(binary_art), chunk_size):
    print(binary_art[i:i + chunk_size])




