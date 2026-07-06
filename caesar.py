

alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']



def caesar(original_text, shift_amount, encode_or_decode):
    result = ""

    for letter in original_text:

        if letter not in alphabet:
            result += letter
        else:
            position = alphabet.index(letter)
            if encode_or_decode == 'encode':
                shifted_position = position + shift_amount
            if encode_or_decode == 'decode':
                shifted_position = position - shift_amount
            shifted_position %= len(alphabet)
            result += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {result}")



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

answer = input("Put y if you want to continue and n if not:\n").lower()

while answer == 'y':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    answer = input("Put y if you want to continue and n if not:\n").lower()


