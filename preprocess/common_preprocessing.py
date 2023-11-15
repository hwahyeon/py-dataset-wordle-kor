import re
import json

# 숫자 제거
def remove_numbers(text):
    return re.sub(r'\d+', '', text)

# 한글 따로쓰기 변경
def decompose(syllable):
    LEADING_CONSONANTS = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
    VOWELS = [
        'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 
        'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 
        'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 
        'ㅡ', 'ㅢ', 'ㅣ'
    ]
    TRAILING_CONSONANTS = [
        '', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 
        'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 
        'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 
        'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 
        'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
    ]

    COMPLEX_CONSONANTS_MAP = {
        'ㄲ': ('ㄱ', 'ㄱ'),
        'ㄳ': ('ㄱ', 'ㅅ'),
        'ㄵ': ('ㄴ', 'ㅈ'),
        'ㄶ': ('ㄴ', 'ㅎ'),
        'ㄸ': ('ㄷ', 'ㄷ'),
        'ㄺ': ('ㄹ', 'ㄱ'),
        'ㄻ': ('ㄹ', 'ㅁ'),
        'ㄼ': ('ㄹ', 'ㅂ'),
        'ㄽ': ('ㄹ', 'ㅅ'),
        'ㄾ': ('ㄹ', 'ㅌ'),
        'ㄿ': ('ㄹ', 'ㅍ'),
        'ㅀ': ('ㄹ', 'ㅎ'),
        'ㅄ': ('ㅂ', 'ㅅ'),
        'ㅃ': ('ㅂ', 'ㅂ'),
        'ㅆ': ('ㅅ', 'ㅅ'),
        'ㅉ': ('ㅈ', 'ㅈ'),
    }

    COMPLEX_VOWELS_MAP = {
        'ㅘ': ('ㅗ', 'ㅏ'),
        'ㅙ': ('ㅗ', 'ㅐ'),
        'ㅚ': ('ㅗ', 'ㅣ'),
        'ㅝ': ('ㅜ', 'ㅓ'),
        'ㅞ': ('ㅜ', 'ㅔ'),
        'ㅟ': ('ㅜ', 'ㅣ'),
        'ㅢ': ('ㅡ', 'ㅣ'),
        'ㅒ': ('ㅑ', 'ㅣ'),
        'ㅖ': ('ㅕ', 'ㅣ'),
    }

    if '가' <= syllable <= '힣':
        base = ord(syllable) - ord('가')
        lead = base // (21 * 28)
        vowel = (base // 28) % 21
        trail = base % 28
        
        lead_char = LEADING_CONSONANTS[lead]
        if lead_char in COMPLEX_CONSONANTS_MAP:
            lead_char = ''.join(COMPLEX_CONSONANTS_MAP[lead_char])
        
        vowel_char = VOWELS[vowel]
        if vowel_char in COMPLEX_VOWELS_MAP:
            vowel_char = ''.join(COMPLEX_VOWELS_MAP[vowel_char])
        
        trail_char = TRAILING_CONSONANTS[trail]
        if trail_char in COMPLEX_CONSONANTS_MAP:
            trail_char = ''.join(COMPLEX_CONSONANTS_MAP[trail_char])
        
        return f"{lead_char}{vowel_char}{trail_char}"
    else:
        return syllable

# 따로쓰기 한글 string으로 변경
def hangul_decompose(string):
    return "".join(decompose(ch) for ch in string)

# JSON로 데이터 저장
def save_to_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)