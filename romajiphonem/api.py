import re
from typing import Any, Iterator, Optional


def phonemize(text: str) -> str:
    return re.sub(r"[A-Za-z][A-Za-z\s']{2,}", _romaji_word_to_kana, text)


def _romaji_word_to_kana(match: re.Match[str]) -> str:
    match.group()
    return "・".join(
        "".join(_romaji_word_to_kana_iter(word)) for word in match.group(0).split(" ")
    )


def _romaji_word_to_kana_iter(text: str) -> Iterator[str]:
    prev_char: Optional[str] = None
    mapping: Any = None

    for char in text.lower():
        if prev_char == char:
            if vowel := _VOWELS.get(char):
                yield vowel
            elif char == "n":
                yield "ン"
            elif char in ("l", "m"):
                yield ""
            else:
                yield "ッ"
            continue
        prev_char = char

        current = (mapping or _DEFAULT_MAPPING).get(char)

        if not current:
            if mapping:
                yield mapping.get("", "")
            else:
                yield char  # Maybe an abnormal case.
            mapping = _DEFAULT_MAPPING.get(char)
            continue

        if isinstance(current, str):
            yield current
            mapping = None
            continue

        mapping = current

    if mapping:
        yield mapping[""]


_VOWELS = {"a": "ア", "i": "イ", "u": "ウ", "e": "エ", "o": "オ"}
_DEFAULT_MAPPING = {
    "a": "ア",
    "b": {
        "": "ブ",
        "a": "バ",
        "i": "ビ",
        "u": "ブ",
        "e": "ベ",
        "o": "ボ",
        "y": {
            "": "ビー",
            "a": "ビャ",
            "i": "ビ",
            "u": "ビュ",
            "e": "ビェ",
            "o": "ビョ",
        },
    },
    "c": {
        "": "ク",
        "a": "カ",
        "i": "シ",
        "u": "ク",
        "e": "セ",
        "o": "コ",
        "h": {"": "チ", "a": "チャ", "i": "チ", "u": "チュ", "e": "チェ", "o": "チョ"},
        "y": {
            "": "シー",
            "a": "チャ",
            "i": "チ",
            "u": "チュ",
            "e": "チェ",
            "o": "チョ",
        },
        "k": {
            "": "ック",
            "a": "ッカ",
            "i": "ッキ",
            "u": "ック",
            "e": "ッケ",
            "o": "ッコ",
            "y": {
                "": "ッキー",
                "a": "ッキャ",
                "i": "ッキ",
                "u": "ッキュ",
                "e": "ッキェ",
                "o": "ッキョ",
            },
        },
    },
    "d": {
        "": "ド",
        "a": "ダ",
        "i": "ディ",
        "u": "ドゥ",
        "e": "デ",
        "o": "ド",
        "y": {
            "": "ディー",
            "a": "ヂャ",
            "i": "ヂ",
            "u": "ヂュ",
            "e": "ヂェ",
            "o": "ヂョ",
        },
    },
    "e": "エ",
    "f": {"": "フ", "a": "ファ", "i": "フィ", "u": "フ", "e": "フェ", "o": "フォ"},
    "g": {
        "": "グ",
        "a": "ガ",
        "i": "ギ",
        "u": "グ",
        "e": "ゲ",
        "o": "ゴ",
        "h": {"": "グ", "a": "ギャ", "i": "ギ", "u": "グ", "e": "ゲ", "o": "ギョ"},
        "y": {
            "": "ギー",
            "a": "ギャ",
            "i": "ギィ",
            "u": "ギュ",
            "e": "ギェ",
            "o": "ギョ",
        },
    },
    "h": {
        "": "ハ",
        "a": "ハ",
        "i": "ヒ",
        "u": "フ",
        "e": "ヘ",
        "o": "ホ",
        "y": {
            "": "ヒー",
            "a": "ヒャ",
            "i": "ヒ",
            "u": "ヒュ",
            "e": "ヒェ",
            "o": "ヒョ",
        },
    },
    "i": "イ",
    "j": {"": "ジ", "a": "ジャ", "i": "ジ", "u": "ジュ", "e": "ジェ", "o": "ジョ"},
    "k": {
        "": "ク",
        "a": "カ",
        "i": "キ",
        "u": "ク",
        "e": "ケ",
        "o": "コ",
        "y": {
            "": "キー",
            "a": "キャ",
            "i": "キ",
            "u": "キュ",
            "e": "キェ",
            "o": "キョ",
        },
    },
    "l": {"": "ル", "a": "ラ", "i": "リ", "u": "ル", "e": "レ", "o": "ロ", "y": "リー"},
    "m": {"": "ム", "a": "マ", "i": "ミ", "u": "ム", "e": "メ", "o": "モ"},
    "n": {
        "": "ン",
        "a": "ナ",
        "i": "ニ",
        "u": "ヌ",
        "e": "ネ",
        "o": "ノ",
        "y": {
            "": "ニー",
            "a": "ニャ",
            "i": "ニ",
            "u": "ニュ",
            "e": "ニェ",
            "o": "ニョ",
        },
    },
    "o": "オ",
    "p": {
        "": "プ",
        "a": "パ",
        "i": "ピ",
        "u": "プ",
        "e": "ペ",
        "o": "ポ",
        "h": {"": "フ", "a": "ファ", "i": "フィ", "u": "フ", "e": "フェ", "o": "フォ"},
        "y": {
            "": "ピー",
            "a": "ピャ",
            "i": "ピ",
            "u": "ピュ",
            "e": "ピェ",
            "o": "ピョ",
        },
    },
    "q": {"": "ク", "a": "クァ", "i": "クィ", "u": "ク", "e": "クェ", "o": "クォ"},
    "r": {"": "ア", "a": "ラ", "i": "リ", "u": "ル", "e": "レ", "o": "ロ", "y": "リー"},
    "s": {
        "": "ス",
        "a": "サ",
        "i": "シ",
        "u": "ス",
        "e": "セ",
        "o": "ソ",
        "h": {
            "": "シー",
            "a": "シャ",
            "i": "シ",
            "u": "シュ",
            "e": "シェ",
            "o": "ショ",
        },
        "y": {
            "": "シー",
            "a": "シャ",
            "i": "シ",
            "u": "シュ",
            "e": "シェ",
            "o": "ショ",
        },
    },
    "t": {
        "": "ト",
        "a": "タ",
        "i": "ティ",
        "u": "トゥ",
        "e": "テ",
        "o": "ト",
        "c": {
            "": "トク",
            "a": "トカ",
            "i": "トシ",
            "u": "トク",
            "e": "トセ",
            "o": "トコ",
            "h": {
                "": "ッチ",
                "a": "ッチャ",
                "i": "ッチ",
                "u": "ッチュ",
                "e": "ッチェ",
                "o": "ッチョ",
            },
        },
        "h": {
            "": "ス",
            "a": "テャ",
            "i": "ティ",
            "u": "テュ",
            "e": "テェ",
            "o": "テョ",
        },
        "s": {"": "ツ", "a": "ツァ", "i": "ツィ", "u": "ツ", "e": "ツェ", "o": "ツォ"},
        "y": {
            "": "ティー",
            "a": "チャ",
            "i": "チ",
            "u": "チュ",
            "e": "チェ",
            "o": "チョ",
        },
    },
    "u": "ウ",
    "v": {
        "": "ヴ",
        "a": "ヴァ",
        "i": "ヴィ",
        "u": "ヴ",
        "e": "ヴェ",
        "o": "ヴォ",
    },
    "w": {"": "ウ", "a": "ワ", "i": "ウィ", "u": "ウ", "e": "ウェ", "o": "ヲ"},
    "x": {
        "": "ックス",
        "a": "クサ",
        "i": "クシ",
        "u": "クス",
        "e": "クセ",
        "o": "クソ",
    },
    "y": {"": "イ", "a": "ワ", "i": "ウィ", "u": "ウ", "e": "ウェ", "o": "ヲ"},
    "z": {
        "": "ズ",
        "a": "ザ",
        "i": "ジ",
        "u": "ズ",
        "e": "ゼ",
        "o": "ゾ",
        "y": {
            "": "ジー",
            "a": "ジャ",
            "i": "ジ",
            "u": "ジュ",
            "e": "ジェ",
            "o": "ジョ",
        },
    },
}