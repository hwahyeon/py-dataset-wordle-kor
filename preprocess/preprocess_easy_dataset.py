from decompose import hangul_decompose
import pandas as pd
import json
import re
import os

# 숫자 제거 함수
def remove_numbers(text):
    return re.sub(r'\d+', '', text)

# preprocess 함수
def process(directory_path, output_path):
    decomposed_list = []

    # 디렉토리 내의 모든 엑셀 파일 처리
    for filename in os.listdir(directory_path):
        if filename.endswith('.xls') or filename.endswith('.xlsx'):
            file_path = os.path.join(directory_path, filename)
            data = pd.read_excel(file_path)

            # 첫 번째 행을 리스트로 변환
            first_column = data.iloc[:, 0].tolist()

            for i in first_column:
                s = hangul_decompose(remove_numbers(i))
                if len(s) == 5:
                    decomposed_list.append(s)

    # 결과를 JSON 형식으로 저장
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(decomposed_list, json_file, ensure_ascii=False, indent=4)
