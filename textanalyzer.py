def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

if __name__ == "__main__":
    filename = input("Enter a filename: ")
    char     = input("Enter a char: ")

    with open(filename) as f:
        text = f.read()
        
    print("The text:")
    print("=========")
    print(text)
    print()
    print("The character {0} appears {1} times.". format(char,count_char(text, char)))
    for char in "abcdefghijklmnopqrstuvwxyz":
        perc = 100 * count_char(text, char) / len(text)
        print("{0} - {1}%".format(char, round(perc, 2)))