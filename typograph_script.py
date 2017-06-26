from re import sub


LINK_SYMBOL = '\u00A0'
ENDASH = '\u2013'
REGEXP_PATTERNS = [
    # quotes replacement
    (r'("|\')(.*)\1', r'«\2»'),
    # removal of excess gaps and transfers of lines
    (r'\s+', r' '),
    # hyphens replacement
    (r'\s+-\s+', '\u2014'),
    # hyphens replacement by a short dash in phone numbers
    (r'(8|\+7)\s*\(\s*(\d{1,3})\s*\)\s*(\d{3})\s*-\s*(\d{2})\s*-\s*(\d{2})',
     r'\1 (\2) \3{0}\4{0}\5'.format(ENDASH)),
    # linking of numbers with the subsequent words
    (r'(\b[а-яА-Яa-zA-Z]{1,2}\b)(\s+)(\b[а-яА-Яa-zA-Z]+\b)', r'\1{0}\3'.format(LINK_SYMBOL)),
    # linking of the unions and any words from 1-2 symbols with the subsequent words
    (r'(\b\d+\b)(\s+)(\b[а-яА-Яa-zA-Z]+\b)', r'\1{0}\3'.format(LINK_SYMBOL)),
]


def format_text(text):
    for pattern, replacement in REGEXP_PATTERNS:
        text = sub(pattern, replacement, text)
    return text
