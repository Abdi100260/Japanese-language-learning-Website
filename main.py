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
with st.expander("Super basic Kanji (漢字)", expanded=False):
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
with st.expander("Super basic Beginner Words (日常単語)", expanded=False):
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

# Initialize navigation state
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# --- GLOBAL NAVIGATION BAR ---
if st.session_state.current_page != "home":
    if st.button("← Back to Dashboard"):
        st.session_state.current_page = "home"
        st.rerun()

# ---------------------------------------------------------
# VIEW 1: HOME DASHBOARD (2 Cards Side-by-Side)
# ---------------------------------------------------------
if st.session_state.current_page == "home":
    st.title("**_Kotonoki 言ノ木_**")
    st.markdown("🐆 Choose your learning path")

    # Create 2 equal-width columns
    col1, col2 = st.columns(2)

    # --- COLUMN 1: KOTOBA (WORDS) CARD ---
    with col1:
        with st.container(border=True):
            # Lion Idol - Kotoba / Words Image
            st.image(
                "https://images.unsplash.com/photo-1534188753412-3e26d0d618d6?w=600&auto=format&fit=crop&q=60", 
                caption="Kotoba Track (言葉)",
                use_container_width=True
            )
            st.markdown("言葉 (Kotoba) — Words")
            st.write("Master essential beginner vocabulary at full lion speed.")
            
            if st.button("Open N5 Words", use_container_width=True, key="btn_words"):
                st.session_state.current_page = "n5_words"
                st.rerun()

    # --- COLUMN 2: BUNPOU (GRAMMAR) CARD ---
    with col2:
        with st.container(border=True):
            # Lion Idol - Bunpou / Grammar Image
            st.image(
                "https://images.unsplash.com/photo-1561731216-c3a4d99437d5?w=600&auto=format&fit=crop&q=60", 
                caption="Bunpou Track (文法)",
                use_container_width=True
            )
            st.markdown("文法 (Bunpou) — Grammar")
            st.write("Construct Japanese sentences fast with foundational particles.")
            
            if st.button("Open N5 Grammar", use_container_width=True, key="btn_grammar"):
                st.session_state.current_page = "n5_grammar"
                st.rerun()

# ---------------------------------------------------------
# VIEW 2: KOTOBA (N5 WORDS) SECTION
# ---------------------------------------------------------
# ---------------------------------------------------------
# VIEW 2: KOTOBA (N5 WORDS) SECTION
# ---------------------------------------------------------
elif st.session_state.current_page == "n5_words":
    st.title("🐆 言葉 (Kotoba) — N5 Essential Words")

    st.markdown(
        """
        Mastering core vocabulary is the fastest way to unlock Japanese comprehension. 
        This JLPT N5 collection highlights high-frequency words, daily items, basic verbs, and essential adjectives.
        """
    )

    dp_n5_words = pd.DataFrame({
        "Word": [
            # Greetings & Polite Expressions
            "こんにちは", "おはよう", "こんばんは", "おやすみ", "さようなら", "ありがとう", "すみません", "はい", "いいえ",
            # Nouns: Food & Drink
            "水", "お茶", "ご飯", "料理", "魚", "肉", "野菜", "果物",
            # Nouns: People & Society
            "人", "友達", "先生", "学生", "会社員", "家族", "父", "母",
            # Nouns: Objects & Places
            "本", "車", "電車", "家", "部屋", "学校", "病院", "店", "国", "日本",
            # Nouns: Time
            "時間", "今日", "明日", "昨日", "今", "毎日", "年", "月", "日",
            # Verbs (Dictionary Form)
            "食べる", "飲む", "行く", "来る", "帰る", "見る", "聞く", "読む", "書く", "話す", "買う", "起きる", "寝る", "勉強する", "する",
            # i-Adjectives
            "大きい", "小さい", "高い", "安い", "新しい", "古い", "いい", "悪い", "美味しい", "楽しい", "暑い", "寒い",
            # na-Adjectives
            "静か", "賑やか", "有名", "親切", "好き", "嫌い", "綺麗", "元気"
        ],
        "Romaji": [
            # Greetings & Polite Expressions
            "konnichiwa", "ohayou", "konbanwa", "oyasumi", "sayounara", "arigatou", "sumimasen", "hai", "iie",
            # Nouns: Food & Drink
            "mizu", "ocha", "gohan", "ryouri", "sakana", "niku", "yasai", "kudamono",
            # Nouns: People & Society
            "hito", "tomodachi", "sensei", "gakusei", "kaishain", "kazoku", "chichi", "haha",
            # Nouns: Objects & Places
            "hon", "kuruma", "densha", "ie", "heya", "gakkou", "byouin", "mise", "kuni", "nihon",
            # Nouns: Time
            "jikan", "kyou", "ashita", "kinou", "ima", "mainichi", "toshi / nen", "tsuki / getsu", "hi / nichi",
            # Verbs (Dictionary Form)
            "taberu", "nomu", "iku", "kuru", "kaeru", "miru", "kiku", "yomu", "kaku", "hanasu", "kau", "okiru", "neru", "benkyou suru", "suru",
            # i-Adjectives
            "ookii", "chiisai", "takai", "yasui", "atarashii", "furui", "ii", "warui", "oishii", "tanoshii", "atsui", "samui",
            # na-Adjectives
            "shizuka", "nigiyaka", "yuumei", "shinsetsu", "suki", "kirai", "kirei", "genki"
        ],
        "Meaning": [
            # Greetings & Polite Expressions
            "Hello / Good afternoon", "Good morning", "Good evening", "Good night", "Goodbye", "Thank you", "Excuse me / Sorry", "Yes", "No",
            # Nouns: Food & Drink
            "Water", "Green tea", "Meal / Cooked rice", "Cuisine / Cooking", "Fish", "Meat", "Vegetable", "Fruit",
            # Nouns: People & Society
            "Person", "Friend", "Teacher", "Student", "Company employee", "Family", "Father", "Mother",
            # Nouns: Objects & Places
            "Book", "Car", "Train", "House / Home", "Room", "School", "Hospital", "Shop / Store", "Country", "Japan",
            # Nouns: Time
            "Time", "Today", "Tomorrow", "Yesterday", "Now", "Everyday", "Year", "Month", "Day",
            # Verbs (Dictionary Form)
            "To eat", "To drink", "To go", "To come", "To return / go home", "To see / watch", "To hear / listen", "To read", "To write", "To speak", "To buy", "To wake up", "To sleep", "To study", "To do",
            # i-Adjectives
            "Big", "Small", "Expensive / Tall", "Cheap", "New", "Old", "Good", "Bad", "Delicious", "Fun / Enjoyable", "Hot (weather/touch)", "Cold (weather)",
            # na-Adjectives
            "Quiet", "Lively / Bustling", "Famous", "Kind / Helpful", "Liked", "Disliked", "Pretty / Clean", "Healthy / Energetic"
        ],
        "Category": [
            # Greetings & Polite Expressions
            "Greeting", "Greeting", "Greeting", "Greeting", "Greeting", "Greeting", "Greeting", "Greeting", "Greeting",
            # Nouns
            "Noun", "Noun", "Noun", "Noun", "Noun", "Noun", "Noun", "Noun",
            "Noun", "Noun", "Noun", "Noun", "Noun", "Noun", "Noun", "Noun",
            "Noun", "Noun", "Noun", "Noun", "Noun", "Noun", "Noun", "Noun", "Noun", "Noun",
            "Noun", "Noun", "Noun", "Noun", "Noun", "Noun", "Noun", "Noun", "Noun",
            # Verbs
            "Verb", "Verb", "Verb", "Verb", "Verb", "Verb", "Verb", "Verb", "Verb", "Verb", "Verb", "Verb", "Verb", "Verb", "Verb",
            # Adjectives
            "i-Adjective", "i-Adjective", "i-Adjective", "i-Adjective", "i-Adjective", "i-Adjective", "i-Adjective", "i-Adjective", "i-Adjective", "i-Adjective", "i-Adjective", "i-Adjective",
            "na-Adjective", "na-Adjective", "na-Adjective", "na-Adjective", "na-Adjective", "na-Adjective", "na-Adjective", "na-Adjective"
        ]
    })
    st.dataframe(dp_n5_words, use_container_width=True)



# ---------------------------------------------------------
# VIEW 3: BUNPOU (N5 GRAMMAR) SECTION
# ---------------------------------------------------------
elif st.session_state.current_page == "n5_grammar":
    st.title("🐆 文法 (Bunpou) — Complete JLPT N5 Grammar Syllabus")

    st.markdown(
        """
        Grammar patterns and particles form the core structural framework of Japanese. 
        Below is an expanded reference list covering 50 essential JLPT N5 particles, verb forms, sentence structures, and conjunctions.
        """
    )

    n5_grammar_data = [
        # --- PARTICLES ---
        {"Grammar Point": "は (wa)", "Category": "Particle", "Function": "Topic marker", "Example": "私は学生です", "Romaji": "Watashi wa gakusei desu", "Meaning": "I am a student"},
        {"Grammar Point": "が (ga)", "Category": "Particle", "Function": "Subject marker / Identifier", "Example": "雨が降っています", "Romaji": "Ame ga futteimasu", "Meaning": "It is raining"},
        {"Grammar Point": "を (wo)", "Category": "Particle", "Function": "Direct Object marker", "Example": "水を飲みます", "Romaji": "Mizu wo nomimasu", "Meaning": "I drink water"},
        {"Grammar Point": "に (ni)", "Category": "Particle", "Function": "Target location / Specific time / Goal", "Example": "７時に学校に行きます", "Romaji": "Shichi-ji ni gakkou ni ikimasu", "Meaning": "I go to school at 7 o'clock"},
        {"Grammar Point": "で (de)", "Category": "Particle", "Function": "Location of action / Means / Tool", "Example": "バスで図書館へ行きます", "Romaji": "Basu de toshokan e ikimasu", "Meaning": "I go to the library by bus"},
        {"Grammar Point": "の (no)", "Category": "Particle", "Function": "Possession / Noun modifier", "Example": "私の本", "Romaji": "Watashi no hon", "Meaning": "My book"},
        {"Grammar Point": "と (to)", "Category": "Particle", "Function": "And (complete list) / With", "Example": "友達と話します", "Romaji": "Tomodachi to hanashimasu", "Meaning": "I talk with a friend"},
        {"Grammar Point": "も (mo)", "Category": "Particle", "Function": "Also / Too", "Example": "私も行きます", "Romaji": "Watashi mo ikimasu", "Meaning": "I will go too"},
        {"Grammar Point": "へ (e)", "Category": "Particle", "Function": "Direction toward", "Example": "日本へ行きます", "Romaji": "Nihon e ikimasu", "Meaning": "I am going to Japan"},
        {"Grammar Point": "から (kara)", "Category": "Particle", "Function": "From (start time/place) / Because", "Example": "９時から始まります", "Romaji": "Ku-ji kara hajimarimasu", "Meaning": "It starts from 9 o'clock"},
        {"Grammar Point": "まで (made)", "Category": "Particle", "Function": "Until / Up to", "Example": "５時まで勉強します", "Romaji": "Go-ji made benkyou shimasu", "Meaning": "I study until 5 o'clock"},
        {"Grammar Point": "より (yori)", "Category": "Particle", "Function": "Than (comparison)", "Example": "これよりそれが好きです", "Romaji": "Kore yori sore ga suki desu", "Meaning": "I like that more than this"},
        {"Grammar Point": "だけ (dake)", "Category": "Particle", "Function": "Only / Just", "Example": "一つだけあります", "Romaji": "Hitotsu dake arimasu", "Meaning": "There is only one"},
        {"Grammar Point": "しか...ない (shika...nai)", "Category": "Particle", "Function": "Only / Nothing but (with negative)", "Example": "100円しかありません", "Romaji": "Hyaku-en shika arimasen", "Meaning": "I only have 100 yen"},
        {"Grammar Point": "か (ka)", "Category": "Particle", "Function": "Question marker / Or", "Example": "これですか？", "Romaji": "Kore desu ka?", "Meaning": "Is it this one?"},
        {"Grammar Point": "ね (ne)", "Category": "Particle", "Function": "Agreement seeker (Right? / Isn't it?)", "Example": "いい天気ですね", "Romaji": "Ii tenki desu ne", "Meaning": "Nice weather, isn't it?"},
        {"Grammar Point": "よ (yo)", "Category": "Particle", "Function": "Emphasis / New information", "Example": "美味しいですよ", "Romaji": "Oishii desu yo", "Meaning": "It's delicious, you know!"},
        {"Grammar Point": "や (ya)", "Category": "Particle", "Function": "And (non-exhaustive list)", "Example": "本やペンを買いました", "Romaji": "Hon ya pen wo kaimashita", "Meaning": "I bought things like books and pens"},
        {"Grammar Point": "など (nado)", "Category": "Particle", "Function": "Et cetera / Things like", "Example": "野菜や果物などを食べます", "Romaji": "Yasai ya kudamono nado wo tabemasu", "Meaning": "I eat vegetables, fruits, and so on"},

        # --- COPULA & VERB CONJUGATIONS ---
        {"Grammar Point": "です / だ (desu / da)", "Category": "Copula", "Function": "To be (polite / plain)", "Example": "彼は先生です", "Romaji": "Kare wa sensei desu", "Meaning": "He is a teacher"},
        {"Grammar Point": "~ます (~masu)", "Category": "Verb Form", "Function": "Polite present/future verb ending", "Example": "毎日勉強します", "Romaji": "Mainichi benkyou shimasu", "Meaning": "I study every day"},
        {"Grammar Point": "~ました (~mashita)", "Category": "Verb Form", "Function": "Polite past tense", "Example": "昨日映画を見ました", "Romaji": "Kinou eiga wo mimashita", "Meaning": "I watched a movie yesterday"},
        {"Grammar Point": "~ません (~masen)", "Category": "Verb Form", "Function": "Polite negative present/future", "Example": "肉を食べません", "Romaji": "Niku wo tabemasen", "Meaning": "I do not eat meat"},
        {"Grammar Point": "~ませんでした (~masen deshita)", "Category": "Verb Form", "Function": "Polite past negative", "Example": "勉強しませんでした", "Romaji": "Benkyou shimasen deshita", "Meaning": "I did not study"},
        {"Grammar Point": "~ない (~nai)", "Category": "Verb Form", "Function": "Casual negative verb form", "Example": "今日は行かない", "Romaji": "Kyou wa ikanai", "Meaning": "I won't go today"},
        {"Grammar Point": "~なかった (~nakatta)", "Category": "Verb Form", "Function": "Casual past negative form", "Example": "安くなかった", "Romaji": "Yasukunakatta", "Meaning": "It was not cheap"},

        # --- TE-FORM PATTERNS ---
        {"Grammar Point": "~てください (~te kudasai)", "Category": "Expression", "Function": "Please do (polite request)", "Example": "ここに書いてください", "Romaji": "Koko ni kaite kudasai", "Meaning": "Please write here"},
        {"Grammar Point": "~てもいい (~te mo ii)", "Category": "Expression", "Function": "May do (permission)", "Example": "写真を撮ってもいいです", "Romaji": "Shashin wo totte mo ii desu", "Meaning": "You may take photos"},
        {"Grammar Point": "~てはいけない (~te wa ikenai)", "Category": "Expression", "Function": "Must not do (prohibition)", "Example": "ここで煙草を吸ってはいけない", "Romaji": "Koko de tabako wo sutte wa ikenai", "Meaning": "You must not smoke here"},
        {"Grammar Point": "~ている (~te iru)", "Category": "Verb Form", "Function": "Progressive action / Resulting state", "Example": "今本を読んでいる", "Romaji": "Ima hon wo yonde iru", "Meaning": "I am reading a book now"},
        {"Grammar Point": "~てから (~te kara)", "Category": "Conjunction", "Function": "After doing X, then Y", "Example": "手を洗ってから食べます", "Romaji": "Te wo aratte kara tabemasu", "Meaning": "I eat after washing my hands"},

        # --- INTENTIONS, DESIRES & RULES ---
        {"Grammar Point": "~たい (~tai)", "Category": "Expression", "Function": "Want to do (desire)", "Example": "寿司が食べたいです", "Romaji": "Sushi ga tabetai desu", "Meaning": "I want to eat sushi"},
        {"Grammar Point": "~たくない (~takunai)", "Category": "Expression", "Function": "Don't want to do", "Example": "どこも行きたくない", "Romaji": "Dokomo ikitakunai", "Meaning": "I don't want to go anywhere"},
        {"Grammar Point": "~つもり (~tsumori)", "Category": "Expression", "Function": "Plan / Intend to do", "Example": "来年日本に行くつもりです", "Romaji": "Rainen Nihon ni iku tsumori desu", "Meaning": "I plan to go to Japan next year"},
        {"Grammar Point": "~ほうがいい (~hou ga ii)", "Category": "Expression", "Function": "Had better (advice)", "Example": "早く寝たほうがいいです", "Romaji": "Hayaku neta hou ga ii desu", "Meaning": "You had better go to sleep early"},
        {"Grammar Point": "~なければならない (~nakereba naranai)", "Category": "Expression", "Function": "Must do (obligation)", "Example": "薬を飲まなければならない", "Romaji": "Kusuri wo nomanakereba naranai", "Meaning": "I must take medicine"},
        {"Grammar Point": "~ことができる (~koto ga dekiru)", "Category": "Expression", "Function": "Can do / Capable of", "Example": "日本語を話すことができます", "Romaji": "Nihongo wo hanasu koto ga dekiru", "Meaning": "I can speak Japanese"},

        # --- TIME & SEQUENCING ---
        {"Grammar Point": "~まえに (~mae ni)", "Category": "Time Pattern", "Function": "Before doing...", "Example": "寝る前に本を読みます", "Romaji": "Neru mae ni hon wo yomimasu", "Meaning": "I read a book before sleeping"},
        {"Grammar Point": "~あとで (~ato de)", "Category": "Time Pattern", "Function": "After doing...", "Example": "食べたあとで散歩します", "Romaji": "Tabeta ato de sanpo shimasu", "Meaning": "I take a walk after eating"},
        {"Grammar Point": "~とき (~toki)", "Category": "Time Pattern", "Function": "When / At the time of", "Example": "暇なとき映画を見ます", "Romaji": "Hima na toki eiga wo mimasu", "Meaning": "When I have free time, I watch movies"},

        # --- COMPARISONS & QUESTIONS ---
        {"Grammar Point": "~でしょう / ~だろう (~deshou / ~darou)", "Category": "Expression", "Function": "Probably / Right?", "Example": "明日は雨が降るでしょう", "Romaji": "Ashita wa ame ga furu deshou", "Meaning": "It will probably rain tomorrow"},
        {"Grammar Point": "~たり ~たりする (~tari ~tari suru)", "Category": "Expression", "Function": "Do things like X and Y", "Example": "本を読んだり音楽を聞いたりします", "Romaji": "Hon wo yondari ongaku wo kiitari shimasu", "Meaning": "I do things like read books and listen to music"},
        {"Grammar Point": "~ながら (~nagara)", "Category": "Expression", "Function": "While doing X, do Y", "Example": "音楽を聞きながら勉強します", "Romaji": "Ongaku wo kikinagara benkyou shimasu", "Meaning": "I study while listening to music"},
        {"Grammar Point": "~すぎる (~sugiru)", "Category": "Suffix", "Function": "Too much / Excessively", "Example": "食べすぎました", "Romaji": "Tabesugimashita", "Meaning": "I ate too much"},
        {"Grammar Point": "どちら / どっち (dochira / docchi)", "Category": "Question", "Function": "Which one (of two)", "Example": "どちらが美味しいですか？", "Romaji": "Dochira ga oishii desu ka?", "Meaning": "Which one is more delicious?"},
        {"Grammar Point": "一番 (ichiban)", "Category": "Adverb", "Function": "The most / Number one", "Example": "これが一番好きです", "Romaji": "Kore ga ichiban suki desu", "Meaning": "I like this one the best"},
        {"Grammar Point": "まだ (~mada)", "Category": "Adverb", "Function": "Still / Not yet", "Example": "まだ食べていません", "Romaji": "Mada tabete imasen", "Meaning": "I haven't eaten yet"},
        {"Grammar Point": "もう (~mou)", "Category": "Adverb", "Function": "Already / Anymore", "Example": "もう宿題をしました", "Romaji": "Mou shukudai wo shimashita", "Meaning": "I already did my homework"},
        {"Grammar Point": "どうして / なぜ (doushite / naze)", "Category": "Question", "Function": "Why / For what reason", "Example": "どうして遅れましたか？", "Romaji": "Doushite okuremashita ka?", "Meaning": "Why were you late?"},
        {"Grammar Point": "どんな (donna)", "Category": "Question", "Function": "What kind of...", "Example": "どんな料理が好きですか？", "Romaji": "Donna ryouri ga suki desu ka?", "Meaning": "What kind of food do you like?"}
    ]

    st.dataframe(pd.DataFrame(n5_grammar_data), use_container_width=True)
    
