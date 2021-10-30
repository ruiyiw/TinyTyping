import sys


# with open("dictionary.txt", 'r', encoding="utf-8") as in_file:
#     with open("short_dict.txt", 'w', encoding="utf-8") as out_file:
#         count = 0
#         for line in in_file:
#             count += 1
#             if count > 15000:
#                 break
#             l = line.split()
#             print(count)
#             word, freq = l[0], l[1]
#             out_file.write(word + '\n')


dictionary = []
with open("short_dict.txt", 'r', encoding="utf-8") as in_file:
    for line in in_file:
        l = line.split()
        word = l[0]
        dictionary.append(word)


string = ""
for line in sys.stdin:
    if "N" == line.rstrip():
        string = ""
        continue
    if "Q" == line.rstrip():
        break
    string += line.rstrip()
    pred_dict = {}

    word_len = len(string)
    count = 0
    for word in dictionary:
        if len(word) > word_len and word[0:word_len] == string:
            count += 1
            pred_dict[word] = count # words in pred_list is ranked from higher to lower naturally

    letter_freq_dict = {}
    for word in pred_dict:
        if len(letter_freq_dict) > 5:
            break
        letter = word[word_len] # already made sure that words in pred_list is at least one character longer than string
        if letter_freq_dict.__contains__(letter):
            letter_freq_dict[letter] += 1
        else:
            letter_freq_dict[letter] = 1

    # print(letter_freq_dict)
    final_list = sorted(letter_freq_dict, key=letter_freq_dict.get, reverse=True)
    print(final_list[0:3])
    # print(pred_list)
