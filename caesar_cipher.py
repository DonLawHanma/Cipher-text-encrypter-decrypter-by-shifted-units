# Caesar cipher encryptor / decryptor

def caesar_cipher(text, shift, mode="encrypt"):
    if mode == "decrypt":
        shift = -shift

    result = ""

    # ord(char) converts a letter to its ASCII number, e.g. A = 65, a = 97
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Non-letter characters like punctuation, spaces, and numbers pass through unchanged
            result += char

    return result


def get_valid_shift():
    while True:
        try:
            shift = int(input("Enter shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            print("Shift must be between 1 and 25.")
        except ValueError:
            print("Shift must be a number.")


def main():
    print("=== Caesar Cipher Tool ===")

    while True:
        mode = input("encrypt or decrypt? (e/d/q to quit): ").strip().lower()

        if mode == "q":
            break

        if mode not in ("e", "d"):
            print("Invalid choice. Try again. (e/d/q to quit)")
            continue

        text = input("Enter your message: ")

        if not text:
            print("Message cannot be empty.")
            continue

        shift = get_valid_shift()
        action = "encrypt" if mode == "e" else "decrypt"
        output = caesar_cipher(text, shift, action)

        print(f"Result: {output}\n")


if __name__ == "__main__":
    main()
