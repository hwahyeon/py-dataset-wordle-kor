from preprocess.common_preprocessing import hangul_decompose, save_json
import pandas as pd
import os

def read_and_process_file(file_path):
    data = pd.read_excel(file_path)
    return data[data['품사'] == '명사']['표제어'].tolist()

def decompose_words(words):
    return [hangul_decompose(word) for word in words if len(hangul_decompose(word)) == 5]


def decompose_words(words):
    decomposed_list = []

    for word in words:
        decomposed_word = hangul_decompose(word)

        if len(decomposed_word) == 5:
            decomposed_data = {
                'key': word,
                'value': decomposed_word
            }
            decomposed_list.append(decomposed_data)

    return decomposed_list


def process_file(file_path, output_path):
    words = read_and_process_file(file_path)
    decomposed_words = decompose_words(words)
    save_json(decomposed_words, output_path, append=True)

def process(directory_path, output_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.xls') or filename.endswith('.xlsx'):
            process_file(os.path.join(directory_path, filename), output_path)
