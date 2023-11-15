# 한글 Wordle을 위한 데이터 전처리

## Description
본 프로젝트는 한글 Wordle에서 사용할 dataset을 추출하는 것을 목적으로 합니다.  
한글 Wordle에서 필요한 데이터셋의 특징은 아래와 같습니다.

- 품사가 명사여야 한다.
- 풀어쓰기로 반환한다.
  - `하늘`은 `ㅎㅏㄴㅡㄹ`
  - `너울`은 `ㄴㅓㅇㅜㄹ`
- 풀어쓰기에서 겹자모는 두 칸을 사용한다.
    - `꼬마`는 `ㄱㄱㅗㅁㅏ`
    - `과거`는 `ㄱㅗㅏㄱㅓ`
- 모든 데이터는 다섯 글자로 이루어져야 한다.

## Project Structure
```
root/  
│  
├── datasets/  
│   ├── dataset1/                    # 국립국어연구원 한국어 학습용 Dataset files  
│   ├── dataset2/                    # 국립국어원 한국어 기초사전 Dataset files  
│   └── dataset3/                    # 우리말샘 Dataset files  
│  
├── output/  
│  
├── preprocess/  
│   ├── __init__.py  
│   ├── common_preprocessing.py      # Common preprocessing functions  
│   ├── preprocess_easy_dataset.py   # Script for preprocessing dataset1
│   ├── preprocess_imdt_dataset.py   # Script for preprocessing dataset2
│   └── preprocess_hard_dataset.py   # Script for preprocessing dataset3
│  
├── main.py  
└── config.py  
```

## Output
JSON 파일로 output/에 저장된다.

## Dataset
- [우리말샘](https://opendict.korean.go.kr/) 사전
- [국립국어원 한국어 기초사전](https://krdict.korean.go.kr/)
- [국립국어연구원](https://www.korean.go.kr/front/etcData/etcDataView.do?mn_id=46&etc_seq=71) 한국어 학습용 어휘 목록
