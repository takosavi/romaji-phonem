from pytest import mark

from romajiphonem.api import phonemize


@mark.parametrize(
    ("text", "expected"),
    (
        ("Flutter Mane", "フルッテア・マネ"),
        ("Sandy Shocks", "サンディー・ショックス"),
        ("Skeledirge", "スケレディアゲ"),
        ("Zacian", "ザシアン"),
        ("Xerneas", "クセアネアス"),
        ("Yveltal", "イヴェルタル"),
        ("Zygarde", "ジーガアデ"),
        ("Tatsugiri", "タツギリ"),
        ("Gholdengo", "ギョルデンゴ"),
        ("Garchomp", "ガアチョムプ"),
        ("Corviknight", "コアヴィクニグト"),
        ("Haxorus", "ハクソルス"),
        ("Gyarados", "ギャラドス"),
        ("Blacephalon", "ブラセファロン"),
        ("Jolteon", "ジョルテオン"),
        ("Sylveon", "シールヴェオン"),
        ("Wooper", "ヲオペア"),
        ("Quagsire", "クアグシレ"),
        ("Hatenne", "ハテンネ"),
        ("Silvally", "シルヴァリー"),
        ("Grimmsnarl", "グリムスナアル"),
        ("Sirfetch'd", "シアフェッチド"),
        ("Mimikyu", "ミミキュ"),
        ("Marshadow", "マアシャドウ"),
        ("Typhlosion", "ティーフロシオン"),
        ("Ponyta", "ポニータ"),
        ("Gorebyss", "ゴレビーッス"),
        ("Hydregion", "ヒードレギオン"),
        ("Thundurus", "テュンドゥルス"),
        ("Pyukumuku", "ピュクムク"),
        ("Cyclizar", "シークリザア"),
        ("Chien-Pao", "チエン-パオ"),
        ("あいうえお", "あいうえお"),
        ("DDラリアット", "DDラリアット"),
        (
            "もちはFlutter Maneを繰り出した! ゆけ! Muk!",
            "もちはフルッテア・マネを繰り出した! ゆけ! ムク!",
        ),
    ),
)
def test_phonemize(text: str, expected: str):
    assert phonemize(text) == expected
