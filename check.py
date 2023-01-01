from uzwords import words
from difflib import get_close_matches

def checkWord(word,words=words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    available = False # inxel kalima nest

    if word in matches:
        available = True # mavjud
        matches = word

    elif 'х' in word:
        word = word.replace('х', 'х')
        matches.update(get_close_matches(word, words))
    elif 'Х' in word:
        word = word.replace('Х', 'Х')
        matches.update(get_close_matches(word, words))


    return {'available': available, 'matches': matches}


if __name__ == '__main__':
    print(checkWord("хат"))
    print(checkWord("хатш"))

