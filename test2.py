def word_count(str):
    count = dict()
    word = str.split()

    for w in word:
        if w in count:
            count[w] += 1
        else:
            count[w] = 1

    return count
print( word_count("abc bca cba abc abc cba"))
