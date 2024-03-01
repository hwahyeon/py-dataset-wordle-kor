# Data preprocessing for Korean Wordle

## Description
The purpose of this project is to extract datasets to be used in Korean Wordle.  
The characteristics of the dataset required for Korean Wordle are as follows.

- Only nouns are used in the datasets.
- It is returned in a decomposed writing style.
  - `하늘` → `ㅎㅏㄴㅡㄹ`
  - `너울` → `ㄴㅓㅇㅜㄹ`
- In the decomposed writing, double consonants use two spaces.
    - `꼬마` → `ㄱㄱㅗㅁㅏ`
    - `과거` → `ㄱㅗㅏㄱㅓ`
- All output data must consist of five characters.

## Project Structure
```
root/  
│  
├── datasets/  
│   ├── dataset1/                   # 국립국어연구원 한국어 학습용 Dataset files  
│   ├── dataset2/                   # 국립국어원 한국어 기초사전 Dataset files  
│   └── dataset3/                   # 우리말샘 Dataset files  
│  
├── output/  
│  
├── preprocess/  
│   ├── __init__.py  
│   ├── common_preprocessing.py     # Common preprocessing functions  
│   ├── preprocess_easy_dataset.py  # Script for preprocessing dataset1
│   ├── preprocess_imdt_dataset.py  # Script for preprocessing dataset2
│   ├── preprocess_hard_dataset.py  # Script for preprocessing dataset3
│   └── preprocess_all_dataset.py   # Script for preprocessing dataset3 (dictionary)
│  
├── main.py  
└── config.py  
```

## Output
Each of the preprocessing python scripts generate a JSON file which is saved in `/output/`.

## Dataset
- [우리말샘](https://opendict.korean.go.kr/) 사전
- [국립국어원 한국어 기초사전](https://krdict.korean.go.kr/)
- [국립국어연구원 한국어 학습용 어휘 목록](https://www.korean.go.kr/front/etcData/etcDataView.do?mn_id=46&etc_seq=71)
