


with open("dictionary.txt", 'r', encoding="utf-8"), open("short_dict.txt") as in_file, out_file:
    count = 0
    for line in file:
        if count > 15000:
            break
        count += 1
        l = line.split()
        word, freq = l[0], l[1]
        print(word, freq)

    