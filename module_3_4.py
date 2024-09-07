def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower():
            same_words.append(i)
    return same_words
    #return [i for i in other_words if root_word.lower() in i.lower()]


result = single_root_words('город', 'пригородный', 'городской', 'град', 'городничий')
result2 = single_root_words('модель', 'МоДельер', 'МОДельНЫЙ', 'ДЕЛЬНЫй', 'немодельный')
print(result)
print(result2)
