from preprocess.common_preprocessing import hangul_decompose, save_json
import pandas as pd
import os

def filter_data(file_path):
    data = pd.read_excel(file_path)
    condition_pos = data['품사'].isin(['명사', '감·명', '관·명', '명·부', '의존 명사'])
    condition_unit = data['구성 단위'] == '단어'
    condition_category = data['범주'].isna()
    return data[condition_pos & condition_unit & condition_category]

def process_words(filtered_data):
    # 사전 생성 시에도 동일한 문자열 변형 로직 적용
    modified_words = filtered_data.iloc[:, 0].str.replace('-', '')
    word_to_meaning = dict(zip(modified_words, filtered_data['뜻풀이']))

    result_set = set()
    first_column = modified_words  # 이미 변형된 단어 사용
    short_words = first_column[first_column.str.len() <= 3]
    result_set.update(short_words)

    wordle_list = []
    for word in result_set:
        decomposed_word = hangul_decompose(word)
        if len(decomposed_word) == 5:
            decomposed_data = {
                'key': word,
                'value': decomposed_word,
                'mean': word_to_meaning.get(word, '')  # '뜻풀이' 추가
            }
            wordle_list.append(decomposed_data)
    return wordle_list

def process_files(file_path, output_path):
    filtered_data = filter_data(file_path)
    wordle_list = process_words(filtered_data)
    save_json(wordle_list, output_path, append=True)

def process(directory_path, output_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.xls') or filename.endswith('.xlsx'):
            process_files(os.path.join(directory_path, filename), output_path)