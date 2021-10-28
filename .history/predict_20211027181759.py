


with open("dictionary.txt", 'r', encoding="utf-8") as in_file:
    with open("short_dict.txt", 'w', encoding="utf-8") as out_file:
        count = 0
        for line in in_file:
            if count > 15000:
                break
            l = line.split()
            word, freq = l[0], l[1]
            out_file.write(word + " " + freq)

    