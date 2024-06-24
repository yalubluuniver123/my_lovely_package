def count_lines_and_sentences(filename):
    num_lines = 0
    num_sentences = 0

    with open(filename, 'r',encoding='utf-8') as file:
        for line in file:
            if line != "\n":
                num_lines += 1
            num_sentences += line.count('.') + line.count('!') + line.count('?') + line.count('...')

    return num_lines, num_sentences


filename = 'pismo_k_oneginu.txt'
# filename = '123.txt'
lines, sentences = count_lines_and_sentences(filename)
print("Количество строк в файле:", lines)
print("Количество предложений в файле:", sentences)
