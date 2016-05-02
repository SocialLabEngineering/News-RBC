import pymorphy2
import pandas as pd

if __name__ == "__main__":
    morph = pymorphy2.MorphAnalyzer()
    common_words_frequency = dict()
    words_frequency = []

    with open('texts.txt', 'r') as input:
        texts = input.read().split('\n')

    for i in range(len(texts)):
        words_frequency.append(dict())

    for i, text in enumerate(texts):
        print('Extracted all nouns from text {}'.format(i))
        for word in text.split(' '):
            p = morph.parse(word)[0]
            if p.tag.POS == "NOUN":
                normal_form = p.normal_form
                words_frequency[i][normal_form] = words_frequency[i].get(normal_form, 0) + 1
                common_words_frequency[normal_form] = common_words_frequency.get(normal_form, 0) + 1

    common_words = sorted(common_words_frequency, key=common_words_frequency.get, reverse=True)

    print('Forming dict of word...')
    final_dict = dict()
    for word in common_words:
        final_dict[word] = [0 for i in range(len(words_frequency))]

    for i, wf in enumerate(words_frequency):
        for word in wf:
            final_dict[word][i] += wf[word]

    arr =[]
    for word in common_words:
        arr.append(final_dict[word])
    print('Dict formed')

    print('Converting table to csv...')
    table = pd.DataFrame(arr, index=common_words, columns=[i for i in range(1, len(texts) + 1)])
    table.to_csv('words_frequency.csv', sep=' ', header=False)
    print('Table converted. It is in words_frequency.csv')
