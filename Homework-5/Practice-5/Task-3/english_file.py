# Вспоминаем работу с файлом.
# Есть файл, в котором много англоязычных текстовых строк.
# Считаем частоту встретившихся слов в файле, но через функции и map, без единого цикла!


def schet_slov():
    my_text = open('english_file.txt', 'r')
    text_string = my_text.read().lower()
    word_dict = {}

    def del_symbols():
        symbols = ['!', '.', ',', '-', '?']
        for symbol in symbols:
            if symbol in text_string:
                text_string.replace(symbol, '')

    del_symbols()

    for word in text_string.split():
        if len(word) > 1:
            if word_dict.get(word):
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        else:
            continue

    for i in sorted(word_dict):
        print(str(word_dict[i]) + ' --> ' + str(i))


schet_slov()
