import sys
import argparse as ap

en2ru = {
    '~': 'Ё', '`': 'ё',

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
ru2en = {value: key for key, value in en2ru.items()}

def translate(data: str, dir: str) -> str:
    func = en2ru if dir == 'en2ru' else ru2en
    return "".join(func.get(ch, ch) for ch in data)

def main():
    try:
        AP = ap.ArgumentParser()
        AP.add_argument("--dir", choices=("en2ru", "ru2en"), default="en2ru")
        args = AP.parse_args()

        data = sys.stdin.read()

        if data.strip():
            sys.stderr.write('\a')
            sys.stderr.flush()

        sys.stdout.write(translate(data, args.dir))

        sys.stdout.flush()
        return 0
    except Exception as e:
        print(e)
        return 1

if __name__ == '__main__':
    sys.exit(main())