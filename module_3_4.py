def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        a= other_words[i].upper()
        b= root_word.upper()
        if a.find(b) >=0:
           same_words.append(other_words[i])
        if b.find(a) >=0:
           same_words.append(other_words[i])
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print()
print(result1)
print(result2)

