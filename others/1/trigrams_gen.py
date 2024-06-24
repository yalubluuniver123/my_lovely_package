from nltk import word_tokenize
from nltk.util import ngrams
from collections import defaultdict, Counter

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text.lower()

text_data = load_data("text.txt")
tokens = word_tokenize(text_data)

trigrams = list(ngrams(tokens, 3))

trigram_model = defaultdict(Counter)

for trigram in trigrams:
    trigram_model[(trigram[0], trigram[1])][trigram[2]] += 1

def generate_text(starting_words, model, num_words=20):
    sentence = list(starting_words)

    for _ in range(num_words):
        next_word = model[tuple(sentence[-2:])].most_common(1)[0][0]
        sentence.append(next_word)

    return ' '.join(sentence)

starting_words = ("выдался", "прекрасный")
generated_text = generate_text(starting_words, trigram_model)
print(generated_text)