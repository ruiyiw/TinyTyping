


with open("dictionary.txt", 'r', encoding="utf-8") as file:
    count = 0
    for line in file:
        if count > 10000:
            break
        count += 1
        l = line.split()
        word, freq = l[0], l[1]
        print(word, freq)

    print(count)
    