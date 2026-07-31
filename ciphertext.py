# we will be making a ceaser cipher encryptor / decriptor 
def caesar_cipher(text, shift, mode="encrypt"):
    if mode == "decrypt":
        shift = -shift
    result = ""
    # ord(char) converts a letter to its ascii number .i.e A = 65, a = 97
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)  
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else: # non letter characters like punctuatuion spaces and numbers go through unchanged
            result += char
    return result 

def main():
    print("=== Caesar Cipher Tool ===")
    while True:
        mode = input("encrypt or decrypt? (e/d/q to quit): ").strip().lower() # remove any white space, only entries are lowercase
        if mode == "q":
            break
        if mode not in ("e","d"):
            print("Invalid choice. try again. (e/d/q to quit): ") # if letter is not e or d 
            continue
        text = input("Enter your message: ")
        try:
            shift = int(input("Enter shift value (1-25): ")) # how far should the cipher change the characters
        except ValueError:
            print("Shift must be a number.")
            continue
        action = "encrypt" if mode == "e" else "decrypt"
        output = caesar_cipher(text, shift, action)
        print(f"Result: {output}\n")

if __name__ == "__main__":
    main()
