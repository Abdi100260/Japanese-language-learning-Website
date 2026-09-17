import streamlit as st
import pandas as pd

st.title("**_Welcome To Kotonoki 言ノ木_**")

st.caption("""
> *"Humankind cannot gain anything without first giving something in return. To obtain, something of equal value must be lost. That is the Law of Equivalent Exchange."*

### Welcome to **Kotonoki (言ノ木)**

Language learning often stalls when the trade feels broken—spending hours passively staring at flashcards, giving up your free time, and getting frustration in return. 

This platform was built on a different principle: **active engagement is the ultimate catalyst**. Fluency cannot be gained through passive absorption. To truly acquire Japanese, short-term comfort and static study habits are traded for hands-on, interactive practice. 

Every feature here—from structured reference matrices to targeted review systems—is designed to ensure your effort yields maximum retention. You bring the consistency and focus; Kotonoki provides the architecture to make that exchange worth it.

---

**Ready to start?** Pick a section below to dive into today's review session.
""")


# --- 1. JAPANESE ALPHABET (KANA) ---
with st.expander("Japanese Alphabet (仮名)", expanded=False):
    dp_kana = pd.DataFrame({
        "Kana": [
            "あ", "い", "う", "え", "お",
            "か", "き", "く", "け", "こ",
            "さ", "し", "す", "せ", "そ",
            "た", "ち", "つ", "て", "と",
            "な", "に", "ぬ", "ね", "の",
            "は", "ひ", "ふ", "へ", "ほ",
            "ま", "み", "む", "め", "も",
            "や", "ゆ", "よ",
            "ら", "り", "る", "れ", "ろ",
            "わ", "を", "ん"
        ],
        "Romaji": [
            "a", "i", "u", "e", "o",
            "ka", "ki", "ku", "ke", "ko",
            "sa", "shi", "su", "se", "so",
            "ta", "chi", "tsu", "te", "to",
            "na", "ni", "nu", "ne", "no",
            "ha", "hi", "fu", "he", "ho",
            "ma", "mi", "mu", "me", "mo",
            "ya", "yu", "yo",
            "ra", "ri", "ru", "re", "ro",
            "wa", "wo", "n"
        ],
        "Katakana": [
            "ア", "イ", "ウ", "エ", "オ",
            "カ", "キ", "ク", "ケ", "コ",
            "サ", "シ", "ス", "セ", "ソ",
            "タ", "チ", "ツ", "テ", "ト",
            "ナ", "ニ", "ヌ", "ネ", "ノ",
            "ハ", "ヒ", "フ", "ヘ", "ホ",
            "マ", "ミ", "ム", "メ", "モ",
            "ヤ", "ユ", "ヨ",
            "ラ", "リ", "ル", "レ", "ロ",
            "ワ", "ヲ", "ン"
        ]
    })
    st.dataframe(dp_kana, use_container_width=True)

st.divider()

# --- 2. GRADE 1 KANJI ---
with st.expander("Kanji (漢字)", expanded=False):
    dp_kanji = pd.DataFrame({
        "Kanji": [
            "一", "二", "三", "四", "五", "六", "七", "八", "九", "十",
            "百", "千", "日", "月", "火", "水", "木", "金", "土", "年",
            "早", "夕", "上", "下", "左", "右", "中", "大", "小", "長",
            "円", "入", "出", "人", "名", "女", "男", "子", "目", "耳",
            "口", "手", "足", "山", "川", "田", "天", "空", "気", "雨",
            "竹", "草", "花", "石", "林", "森", "貝", "犬", "車", "町",
            "村", "本", "文", "字", "学", "校", "王", "玉", "音", "糸",
            "見", "立", "休", "生", "先", "赤", "青", "白", "正", "力"
        ],
        "Romaji": [
            "ichi", "ni", "san", "yon / shi", "go", "roku", "nana / shichi", "hachi", "kyuu / ku", "juu",
            "hyaku", "sen", "hi / nichi", "tsuki / getsu", "hi / ka", "mizu / sui", "ki / moku", "kane / kin", "tsuchi / do", "toshi / nen",
            "haya / sou", "yuu / seki", "ue / jou", "shita / ka", "hidari / sa", "migi / u", "naka / chuu", "oo / dai", "chii / shou", "naga / chou",
            "en / maru", "hai / nyuu", "de / shutsu", "hito / jin", "na / mei", "onna / jo", "otoko / dan", "ko / shi", "me / moku", "mimi / ji",
            "kuchi / kou", "te / shu", "ashi / soku", "yama / san", "kawa / sen", "ta / den", "ten", "sora / kuu", "ki", "ame / u",
            "take / chiku", "kusa / sou", "hana / ka", "ishi / seki", "hayashi / rin", "mori / shin", "kai", "inu / ken", "kuruma / sha", "machi / chou",
            "mura / son", "hon", "bun / mon", "ji", "gaku / mana", "kou", "ou", "tama / gyo", "oto / on", "ito / shi",
            "mi / ken", "ta / ritsu", "yasu / kyuu", "nama / sei", "saki / sen", "aka / seki", "ao / sei", "shiro / haku", "tada / sei", "chikara / ryoku"
        ],
        "Meaning": [
            "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "hundred", "thousand", "sun / day", "moon / month", "fire", "water", "tree / wood", "gold / money", "earth / soil", "year",
            "early", "evening", "up / above", "down / below", "left", "right", "inside / middle", "big / large", "small / little", "long / leader",
            "yen / circle", "enter / insert", "exit / go out", "person", "name", "woman", "man", "child", "eye", "ear",
            "mouth", "hand", "foot / leg", "mountain", "river", "rice field", "heaven / sky", "sky / empty", "spirit / air", "rain",
            "bamboo", "grass", "flower", "stone", "grove", "forest", "shellfish", "dog", "car / vehicle", "town",
            "village", "book / origin", "sentence / writing", "character / letter", "study / learn", "school", "king", "jewel / ball", "sound", "thread",
            "see / look", "stand", "rest", "life / birth", "ahead / previous", "red", "blue", "white", "correct / right", "power / strength"
        ]
    })
    st.dataframe(dp_kanji, use_container_width=True)

st.divider()

# --- 3. ESSENTIAL BEGINNER WORDS ---
with st.expander("Essential Beginner Words (日常単語)", expanded=False):
    dp_easy_words = pd.DataFrame({
        "Word": [
            "こんにちは", "ありがとう", "すみません", "はい", "いいえ", "さようなら",
            "水", "猫", "犬", "本", "車", "友達", "家", "時間",
            "食べる", "飲む", "行く", "来る", "見る", "話す",
            "美味しい", "良い", "大きい", "小さい", "楽しい"
        ],
        "Romaji": [
            "konnichiwa", "arigatou", "sumimasen", "hai", "iie", "sayounara",
            "mizu", "neko", "inu", "hon", "kuruma", "tomodachi", "ie", "jikan",
            "taberu", "nomu", "iku", "kuru", "miru", "hanasu",
            "oishii", "ii", "ookii", "chiisai", "tanoshii"
        ],
        "Meaning": [
            "Hello / Good afternoon", "Thank you", "Excuse me / Sorry", "Yes", "No", "Goodbye",
            "Water", "Cat", "Dog", "Book", "Car", "Friend", "House / Home", "Time",
            "To eat", "To drink", "To go", "To come", "To see / watch", "To speak",
            "Delicious", "Good", "Big", "Small", "Fun / Enjoyable"
        ],
        "Category": [
            "Greeting", "Greeting", "Greeting", "Greeting", "Greeting", "Greeting",
            "Noun", "Noun", "Noun", "Noun", "Noun", "Noun", "Noun", "Noun",
            "Verb", "Verb", "Verb", "Verb", "Verb", "Verb",
            "Adjective", "Adjective", "Adjective", "Adjective", "Adjective"
        ]
    })
    st.dataframe(dp_easy_words, use_container_width=True)

st.divider()

# --- 4. BASIC GRAMMAR & PARTICLES ---
with st.expander("Basic Grammar & Particles (助詞)", expanded=False):
    dp_easy_grammar = pd.DataFrame({
        "Grammar Point": [
            "は (wa)", "が (ga)", "を (wo)", "に (ni)", "で (de)", "の (no)", "と (to)", "も (mo)"
        ],
        "Function": [
            "Topic marker", "Subject marker", "Direct Object marker", 
            "Target location / Time marker", "Context location / Tool marker", 
            "Possession / Modifier marker", "And / With marker", "Also / Too marker"
        ],
        "Example": [
            "私は学生です (I am a student)",
            "雨が降っています (It is raining)",
            "水を飲みます (I drink water)",
            "日本に行きます (I go to Japan)",
            "バスで行きます (I go by bus)",
            "私の本 (My book)",
            "友達と話します (I talk with a friend)",
            "私も行きます (I will go too)"
        ],

        "Example(Romaji)": [
            "Watashi wa gakusei desu",
            "Ame ga futteimasu",
            "Mizu wo nomimasu",
            "Nihon ni ikimasu",
            "Basu de ikimasu",
            "Watashi no hon",
            "Tomodachi to hanashimasu",
            "Watashi mo ikimasu"
        ]
    })
    st.dataframe(dp_easy_grammar, use_container_width=True)
