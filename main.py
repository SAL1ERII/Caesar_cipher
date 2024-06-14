def int_check(txt):
    while True:
        new_input = input(txt).strip()
        try:
            return int(new_input)
        except ValueError:
            print('Error!')


def ascii_into_symbol(ascii_line):
    sym_line = "".join([chr(sym_ascii) for sym_ascii in ascii_line])
    return sym_line


def caesar_cipher(str_line):
    while True:
        check = int_check("If you want to encrypt a string, enter - 1, if you want to decrypt - 2:")
        if check == 1:
            key = int_check("Enter key num: ")
            new_ascii_line = [ord(char)+key for char in str_line]
            return ascii_into_symbol(new_ascii_line)
        elif check == 2:
            key = int_check("Enter key num: ")
            new_ascii_line = [ord(char)-key for char in str_line]
            return ascii_into_symbol(new_ascii_line)
        else:
            continue


def main():
    print(caesar_cipher(input("Enter string: ")))


if __name__ == "__main__":
    main()