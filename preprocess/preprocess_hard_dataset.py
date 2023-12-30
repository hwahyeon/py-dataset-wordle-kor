from preprocess.common_preprocessing import hangul_decompose, save_json
import pandas as pd
import os
from collections import defaultdict

def extract_data(file_path):
    data = pd.read_excel(file_path)

    condition_pos = data['품사'].isin(['명사', '감·명', '관·명', '명·부', '의존 명사'])
    condition_unit = data['구성 단위'] == '단어'
    condition_category = data['범주'].isna()

    filtered_data = data[condition_pos & condition_unit & condition_category]

    # 필요한 열 추출
    result = filtered_data[['어휘', '뜻풀이']]
    return result

def process_words(data):
    data['어휘'] = data['어휘'].str.replace('-', '')

    # 각 어휘에 대한 모든 뜻풀이와 분해된 단어를 저장할 defaultdict 생성
    word_info = defaultdict(lambda: {'meanings': [], 'decomposed': ''})

    for index, row in data.iterrows():
        decomposed_word = hangul_decompose(row['어휘'])
        if len(decomposed_word) == 5:
            word_info[row['어휘']]['meanings'].append(row['뜻풀이'])
            word_info[row['어휘']]['decomposed'] = decomposed_word

    # defaultdict에서 딕셔너리 리스트로 변환
    word_list = [
        {'key': word, 'value': info['decomposed'], 'mean': mean}
        for word, info in word_info.items() for mean in info['meanings']
    ]

    return word_list

def process_files(file_path, output_path):
    filtered_data = extract_data(file_path)
    wordle_list = process_words(filtered_data)
    save_json(wordle_list, output_path, append=True)

def process(directory_path, output_path):
    print('hey')
    for filename in os.listdir(directory_path):
        if filename.endswith('.xls') or filename.endswith('.xlsx'):
            process_files(os.path.join(directory_path, filename), output_path)