def str_func(words):
    return words.upper

def capitalize_words(sentence):
    '''функция делает заглавными первые буквы каждого слова в строке'''
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
