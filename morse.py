import pyaudio
import numpy as np

SPECIAL_SYMBOLS = [
    ' ', '!', '@',
    '#', '№', '$',
    ';', '%', '^',
    ':', '&', '(', ')',
    ',', '`', '~',
    '<', '>', '.',
    '/', '?', '"',
    '{', '}', '[',
    ']', '|', '-',
    '+', '=', '\\',
    "'", '«', '»',
    '—', '–'
]
NUMBERS = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '0'
]
LETTERS = {
    'а': '*_', 'б': '_***', 'в': '*__', 'г': '__*', 'д': '_**',
    'е': '*', 'ж': '***_', 'з': '__**', 'и': '**',
    'й': '*___', 'к': '_*_', 'л': '*_**', 'м': '__',
    'н': '_*', 'о': '___', 'п': '*__*', 'р': '*_*',
    'с': '***', 'т': '_', 'у': '**_', 'ф': '**__',
    'х': '****', 'ц': '_**_', 'ч': '___.', 'ш': '____',
    'щ': '___*_', 'ъ': '_*___', 'ы': '_*__', 'ь': '_**_',
    'э': '**_**', 'ю': '**__*', 'я': '*_*_'
}


def play_sound(audio_data, sample_rate=44100):
    p = pyaudio.PyAudio()

    stream = p.open(
        format=pyaudio.paFloat32,
        channels=1,
        rate=sample_rate,
        output=True
    )

    stream.write(audio_data.tobytes())

    stream.stop_stream()
    stream.close()

    p.terminate()


def encrypt(item: str) -> str:
    item = item.lower()
    encrypted_item = ''
    for el in item:
        if el not in SPECIAL_SYMBOLS and el not in NUMBERS:
            encrypted_item += f' {LETTERS[el]} '
        else:
            encrypted_item += el
    return encrypted_item.strip()


def decrypt(item: str) -> str:
    item = item.lower().split()
    decrypted_item = ''
    for el in item:
        if el not in SPECIAL_SYMBOLS and el not in NUMBERS:
            for key, value in LETTERS.items():
                if el == value:
                    decrypted_item += key
        else:
            decrypted_item += el
    return decrypted_item.strip()


def play_short_sound() -> int:
    FREQUENCY = 440
    SHORT_DURATION = 0.1  # Исправлено: использовать SHORT_DURATION вместо DURATION
    SAMPLE_RATE = 44100

    t = np.linspace(0, SHORT_DURATION, int(SAMPLE_RATE * SHORT_DURATION))
    audio_data = np.sin(2 * np.pi * FREQUENCY * t)

    play_sound(audio_data, SAMPLE_RATE)

    return 0


def play_long_sound() -> int:
    FREQUENCY = 440
    LONG_DURATION = 0.2  # Исправлено: использовать LONG_DURATION вместо DURATION
    SAMPLE_RATE = 44100

    t = np.linspace(0, LONG_DURATION, int(SAMPLE_RATE * LONG_DURATION))
    audio_data = np.sin(2 * np.pi * FREQUENCY * t)

    play_sound(audio_data, SAMPLE_RATE)

    return 0


def play_morse(item: str) -> int or str:
    item = item.replace(' ', '')
    if '*' in item or '_' in item:
        for el in item:
            if el == '*':
                print(el, end=' ')
                play_short_sound()
            else:
                print(el, end=' ')
                play_long_sound()
        return 0
    else:
        print('Текст должен быть на азбуке морзе!!!')


def main():
    morse_text = '*__*  *_*  **  *__  *  _ !'
    print(encrypt('Привет!'))
    print(decrypt(morse_text))
    play_morse('*** ___ ***')


if __name__ == '__main__':
    main()
