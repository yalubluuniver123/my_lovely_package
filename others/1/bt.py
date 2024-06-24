import random
import nltk


def load_text(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def generate_ngrams(text):
    tokens = nltk.word_tokenize(text)
    bigrams = list(nltk.bigrams(tokens))
    trigrams = list(nltk.trigrams(tokens))
    return bigrams, trigrams


def generate_sentence_with_bigrams(bigrams):
    sentence = []
    if bigrams:
        start_words = [bigram[0] for bigram in bigrams]
        next_word = random.choice(start_words)
        sentence.append(next_word)

        while True:
            next_word_options = [bigram[1] for bigram in bigrams if bigram[0] == next_word]
            if not next_word_options:
                break
            next_word = random.choice(next_word_options)
            sentence.append(next_word)
            if len(sentence) > 10:
                break

    return ' '.join(sentence)


def generate_sentence_with_trigrams(trigrams):
    sentence = list(random.choice(trigrams))
    while True:
        next_word_options = [trigram[2] for trigram in trigrams if trigram[:2] == tuple(sentence[-2:])]
        if not next_word_options:
            break
        next_word = random.choice(next_word_options)
        sentence.append(next_word)
        if len(sentence) > 20:
            break
    return ' '.join(sentence)


filename = 'text.txt'
text = load_text(filename)
bigrams, trigrams = generate_ngrams(text)

print("2gr:")
for _ in range(3):
    sentence = generate_sentence_with_bigrams(bigrams)
    print(sentence)

print("\n\n3gr:")
for _ in range(3):
    sentence = generate_sentence_with_trigrams(trigrams)
    print(sentence)
