"""Standalone script to encode text into Morse code and base64."""

import base64

MORSE_CODE: dict[str, str] = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/",
}


def encode_text(text: str) -> tuple[str, str]:
    """Return a ``(morse_string, base64_string)`` tuple for *text*.

    Characters not present in :data:`MORSE_CODE` are silently skipped in the
    Morse output.  The base64 encoding uses the UTF-8 representation of *text*.
    """
    morse_string = " ".join(MORSE_CODE[ch] for ch in text.upper() if ch in MORSE_CODE)
    base64_string = base64.b64encode(text.encode("utf-8")).decode("ascii")
    return morse_string, base64_string


if __name__ == "__main__":
    sample = "Hello World"
    morse, b64 = encode_text(sample)
    print(f"Input:  {sample}")
    print(f"Morse:  {morse}")
    print(f"Base64: {b64}")
