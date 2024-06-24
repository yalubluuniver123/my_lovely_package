import random

# Загрузка текста романа "Братья Карамазовы"
with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Функция для разделения текста на предложения
def split_into_sentences(text):
    return text.split(".")

# Функция для разделения предложения на слова
def split_into_words(sentence):
    return sentence.split()

# Функция для создания биграмм и триграмм из текста
def generate_ngrams(text):
    sentences = split_into_sentences(text)
    ngrams = []
    for sentence in sentences:
        words = split_into_words(sentence)
        # Биграммы
        for i in range(len(words) - 1):
            ngrams.append((words[i], words[i+1]))
    return ngrams

# Создание биграмм из текста
ngrams = generate_ngrams(text)

# Функция для создания словаря из биграмм
def create_model(ngrams):
    model = {}
    for ngram in ngrams:
        prefix = tuple(ngram[:-1])
        suffix = ngram[-1]
        if prefix not in model:
            model[prefix] = []
        model[prefix].append(suffix)
    return model

# Генерация предложения на основе модели
def generate_sentence(model, max_length):
    sentence = []
    prefix = random.choice(list(model.keys()))
    sentence.extend(prefix)
    while len(sentence) < max_length:
        if prefix not in model:
            break
        next_word = random.choice(model[prefix])
        sentence.append(next_word)
        prefix = tuple(sentence[-(len(prefix)):])
    return " ".join(sentence)

# Создание модели
model = create_model(ngrams)

# Генерация трех предложений
for i in range(3):
    print(f"Предложение {i+1}: {generate_sentence(model, 10)}")
