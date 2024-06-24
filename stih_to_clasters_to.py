import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('russian'))

with open('tihiy_don.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = word_tokenize(text.lower())

filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

freq_dist = FreqDist(filtered_words)
most_common_words = freq_dist.most_common(int(input("Введите N:")))

print("Наиболее часто встречающиеся слова:")
for word, freq in most_common_words:
    print(f"{word}: {freq}")

common_word_set = set([word for word, _ in most_common_words])
sentences_with_common_words = []
for sentence in nltk.sent_tokenize(text):
    if len(set(word_tokenize(sentence.lower())) & common_word_set) > 1:
        sentences_with_common_words.append(sentence)

print("\nПредложения, содержащие более одного наиболее часто встречающегося слова:")
for sentence in sentences_with_common_words:
    print(sentence)

plt.figure(figsize=(10, 6))
words, freqs = zip(*most_common_words)
plt.bar(words, freqs)
plt.xlabel('Слово')
plt.ylabel('Частота')
plt.title('Распределение наиболее часто встречающихся слов')
plt.xticks(rotation=90)
plt.show()

mu, sigma = np.mean(freqs), np.std(freqs)
x = np.linspace(min(freqs), max(freqs), 100)
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))
plt.plot(x, y, color='red', linestyle='--', label='Нормальное распределение')
plt.legend()
plt.show()

kmeans = KMeans(n_clusters=3)
X = np.array(freqs).reshape(-1, 1)
kmeans.fit(X)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print("\nКластеры ключевых слов:")
for i in range(len(centroids)):
    cluster_words = [word for j, (word, freq) in enumerate(most_common_words) if labels[j] == i]
    print(f"Кластер {i+1}: {cluster_words}")
