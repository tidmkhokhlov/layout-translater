import sys
letter_dict = {
    'Q': 'Й', 'q': 'й',
    'W': 'Ц', 'w': 'ц',
    'E': 'У', 'e': 'у',
    'R': 'К', 'r': 'к',
    'T': 'Е', 't': 'е',
    'Y': 'Н', 'y': 'н',
    'U': 'Г', 'u': 'г',
    'I': 'Ш', 'i': 'ш',
    'O': 'Щ', 'o': 'щ',
    'P': 'З', 'p': 'з',
    '{': 'Х', '[': 'х',
    '}': 'Ъ', ']': 'ъ',

    'A': 'Ф', 'a': 'ф',
    'S': 'Ы', 's': 'ы',
    'D': 'В', 'd': 'в',
    'F': 'А', 'f': 'а',
    'G': 'П', 'g': 'п',
    'H': 'Р', 'h': 'р',
    'J': 'О', 'j': 'о',
    'K': 'Л', 'k': 'л',
    'L': 'Д', 'l': 'д',
    ':': 'Ж', ';': 'ж',
    '"': 'Э', "'": 'э',

    'Z': 'Я', 'z': 'я',
    'X': 'Ч', 'x': 'ч',
    'C': 'С', 'c': 'с',
    'V': 'М', 'v': 'м',
    'B': 'И', 'b': 'и',
    'N': 'Т', 'n': 'т',
    'M': 'Ь', 'm': 'ь',
    '<': 'Б', ',': 'б',
    '>': 'Ю', '.': 'ю',
}

def translate(text: str) -> str:
    for letter in text:
        if letter_dict.get(letter):
            text = text.replace(letter, letter_dict.get(letter), 1)
    return text

if __name__ == '__main__':
    data = sys.stdin.read()
    data = translate(data)
    sys.stdout.write(data)