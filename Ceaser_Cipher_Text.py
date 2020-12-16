alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encoded_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        encoded_text += new_letter
    print(f"The encoded text is {encoded_text}")

def decrypt(text, shift):
    original_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        new_letter = alphabet[new_position]
        original_text += new_letter
    print(f"The encoded text is {original_text}")

if user_choice == "encode":
    encrypt(text, shift)
elif user_choice == "decode":
    decrypt(text, shift)
else:
    print("Wrong entry")