def count_characters(string):
    # returns the number of times each character occurs in a string
    count_dict = {}
    for c in string:
        if c in count_dict:
            # add count if letter is in string
            count_dict[c] += 1
        else:
            # returns 1 as count of letter in string
            count_dict[c] = 1
    print(count_dict)


count_characters("Dynasty")
