import config
from preprocess.preprocess_easy_dataset import process as preprocess_easy
from preprocess.preprocess_imdt_dataset import process as preprocess_imdt
from preprocess.preprocess_hard_dataset import process as preprocess_hard
from preprocess.prepocess_all_dataset import process as preprocess_all

def preprocess_all_datasets():
    # dataset1 폴더의 파일들을 전처리
    preprocess_easy(config.DATASET1_PATH, config.EASY_MODE_OUTPUT_PATH)

    # dataset2 폴더의 파일들을 전처리
    preprocess_imdt(config.DATASET2_PATH, config.IMDT_MODE_OUTPUT_PATH)

    # dataset3 폴더의 파일들을 전처리
    preprocess_hard(config.DATASET3_PATH, config.HARD_MODE_OUTPUT_PATH)

    # dataset3 폴더의 파일들을 전처리 (모든 의미를 포함한 사전 형식으로)
    preprocess_all(config.DATASET3_PATH, config.ALL_MODE_OUTPUT_PATH)

if __name__ == "__main__":
    preprocess_all_datasets()