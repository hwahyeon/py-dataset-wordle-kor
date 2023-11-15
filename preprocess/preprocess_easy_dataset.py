from preprocess.common_preprocessing import hangul_decompose, remove_numbers, save_to_json
import pandas as pd
import os

def read_and_process_file(file_path):
    decomposed_list = []
    data = pd.read_excel(file_path)
    filtered_words = data[data['품사'] == '명']['단어'].tolist()

    for item in filtered_words:
        processed_item = hangul_decompose(remove_numbers(item))
        if len(processed_item) == 5:
            decomposed_list.append(processed_item)

    return decomposed_list

def process(directory_path, output_path):
    all_decomposed_data = []

    for filename in os.listdir(directory_path):
        if filename.endswith('.xls') or filename.endswith('.xlsx'):
            file_path = os.path.join(directory_path, filename)
            decomposed_data = read_and_process_file(file_path)
            all_decomposed_data.extend(decomposed_data)

    save_to_json(all_decomposed_data, output_path)
