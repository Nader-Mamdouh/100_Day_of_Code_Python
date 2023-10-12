def encrypt(text, shift):
    enc_text = ""
    for char in text:
        if char.isalpha():
            index = (alphabet.index(char)+shift)
            enc_char = alphabet[index]
            enc_text += enc_char
        else:
            enc_text += char
    print("the encoded text is :", enc_text)


def decrypt(text, shift):
    dec_text = ""
    for char in text:
        if char.isalpha():
            index = (alphabet.index(char)-shift)
            dec_char = alphabet[index]
            dec_text += dec_char
        else:
            dec_text += char
    print("the decoded text is :", dec_text)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt , 'decode' to decrypt : \n")
text = input("Type your massege : \n").lower()
shift = int(input("Type the shift number : \n"))
shift = shift % 26
if direction == "encode":
    encrypt(text, shift)
else:
    decrypt(text, shift)
