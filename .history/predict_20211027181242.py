


with open("dictionary.txt", 'r', encoding="utf-8") as file:
    count = 0
    for line in file:
        if count > 50:
            break
        count += 1
        word, freq = line.split()

    
    