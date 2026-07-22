# Dərs 18 — انسان و اعضای بدن (İnsan və bədən üzvləri)
# Mənbə: کتاب دوم, səh. 219-230

LESSON = {
    "number": 18,
    "title_fa": "انسان و اعضای بدن",
    "title_az": "İnsan və bədən üzvləri",
    "available": True,
    "vocabulary": [
        {"fa": "مهربان", "reading": "mehrəban", "az": "Mehriban"},
        {"fa": "نامهربان", "reading": "namehrəban", "az": "Mehribansız"},
        {"fa": "متواضع", "reading": "motəvaze", "az": "Təvazökar"},
        {"fa": "متکبّر", "reading": "motəkəbber", "az": "Təkəbbürlü"},
        {"fa": "نابینا (کور)", "reading": "nabina (kur)", "az": "Kor"},
        {"fa": "ناشنوا (کر)", "reading": "naşenəva (kər)", "az": "Kar"},
        {"fa": "معلول", "reading": "məlul", "az": "Əlil"},
        {"fa": "سر، ابرو، بازو", "reading": "sər, əbru, bazu", "az": "Baş, qaş, qol"},
        {"fa": "سینه", "reading": "sine", "az": "Sinə"},
        {"fa": "معده", "reading": "mede", "az": "Mədə"},
        {"fa": "ماهیچه (عضله)", "reading": "mahiçe (əzəle)", "az": "Əzələ"},
        {"fa": "استخوان", "reading": "ostoxan", "az": "Sümük"},
        {"fa": "نوزاد", "reading": "nouzad", "az": "Körpə (yenidoğulmuş)"},
        {"fa": "احترام می‌گذارد", "reading": "ehteram migozarəd", "az": "hörmət edir"},
        {"fa": "بغل می‌کند", "reading": "bəğəl mikonəd", "az": "qucaqlayır"},
        {"fa": "نوازش می‌کند", "reading": "nəvazeş mikonəd", "az": "sığallayır"},
        {"fa": "می‌بوسد", "reading": "mibusəd", "az": "öpür"},
        {"fa": "صحبت می‌کند", "reading": "sohbət mikonəd", "az": "danışır"},
        {"fa": "به دنیا می‌آید", "reading": "be donya miayəd", "az": "dünyaya gəlir"},
        {"fa": "از دنیا می‌رود", "reading": "əz donya mirəvəd", "az": "dünyadan köçür"},
        {"fa": "شانه می‌زند (کوتاه می‌کند)", "reading": "şane mizənəd (kutah mikonəd)", "az": "daramaq / qısaltmaq"},
        {"fa": "قسمت", "reading": "qesmət", "az": "Hissə"},
        {"fa": "محکم", "reading": "mohkəm", "az": "Möhkəm"},
        {"fa": "بهتر", "reading": "behtər", "az": "Daha yaxşı"},
        {"fa": "طعم و مزه", "reading": "tam o məze", "az": "Dad"},
        {"fa": "شور", "reading": "şur", "az": "Şor"},
        {"fa": "تند", "reading": "tond", "az": "Acı (yeməkdə)"},
        {"fa": "احساس می‌کند", "reading": "ehsas mikonəd", "az": "hiss edir"},
        {"fa": "حس می‌کند", "reading": "hes mikonəd", "az": "hiss edir"},
        {"fa": "نفس می‌کشد", "reading": "nəfəs mikeşəd", "az": "nəfəs alır"},
        {"fa": "حرف می‌زند", "reading": "hərf mizənəd", "az": "danışır"},
        {"fa": "راه می‌رود", "reading": "rah mirəvəd", "az": "yeriyir"},
        {"fa": "به وسیله‌یِ", "reading": "be vasileye", "az": "…vasitəsilə"},
        {"fa": "علاوه بر", "reading": "əlave bər", "az": "…dan əlavə"},
    ],
    "grammar_notes": [
        {
            "title_az": "«دست، دسته و…» — bənzər sözlərin fərqi",
            "title_fa": "دست، دسته و ...",
            "conjugations": [
                {"pronoun_fa": "دست (əl)", "form_fa": "انسان دو دست دارد."},
                {"pronoun_fa": "دسته (qulp/dəstə)", "form_fa": "پارچ و سطل دسته دارند."},
                {"pronoun_fa": "پا (ayaq)", "form_fa": "ما دو پا داریم."},
                {"pronoun_fa": "پایه (ayaq/dayaq — mebel üçün)", "form_fa": "این صندلی، چهار پایه دارد."},
                {"pronoun_fa": "چشم (göz)", "form_fa": "انسان‌ها و حیوان‌ها چشم دارند."},
                {"pronoun_fa": "چشمه (bulaq)", "form_fa": "در کوه و جنگل چشمه وجود دارد."},
                {"pronoun_fa": "دندان (diş)", "form_fa": "این دندان است."},
                {"pronoun_fa": "دندانه (dişcik — hərflərdə)", "form_fa": "حرف «س» سه دندانه دارد."},
                {"pronoun_fa": "ریش (saqqal)", "form_fa": "این مرد، ریش دارد."},
                {"pronoun_fa": "ریشه (kök)", "form_fa": "درخت ریشه دارد."},
                {"pronoun_fa": "شاخ (buynuz)", "form_fa": "گاو شاخ دارد."},
                {"pronoun_fa": "شاخه (budaq)", "form_fa": "درخت شاخه دارد."},
            ],
            "examples": [
                {"fa": "بدن انسان، اعضای گوناگونی دارد؛ امّا بعضی از واژه‌ها با اضافه‌شدن یک حرف، معنای دیگری پیدا می‌کنند.", "az": "İnsan bədəninin müxtəlif üzvləri var; amma bəzi sözlər bir hərf artıqla başqa məna qazanır (dəst→dəstə, pa→paye)."},
                {"fa": "پارچ و سطل دسته دارند؛ امّا انسان دست دارد.", "az": "Dolça və vedrənin qulpu (دسته) olur; insanın isə əli (دست) olur."},
                {"fa": "این صندلی چهار پایه دارد؛ ما دو پا داریم.", "az": "Bu stulun dörd ayağı (پایه) var; bizim isə iki ayağımız (پا) var."},
                {"fa": "در کوه و جنگل چشمه وجود دارد؛ انسان‌ها و حیوان‌ها چشم دارند.", "az": "Dağda və meşədə bulaq (چشمه) olur; insanların və heyvanların gözü (چشم) olur."},
                {"fa": "درخت، ریشه و شاخه دارد؛ این مرد ریش دارد و آن گاو شاخ دارد.", "az": "Ağacın kökü (ریشه) və budağı (شاخه) var; bu kişinin saqqalı (ریش), o inəyin isə buynuzu (شاخ) var."},
            ],
        },
        {
            "title_az": "«مالِ …» quruluşu — sahiblik (kimindir?)",
            "title_fa": "مالِ ........",
            "conjugations": [
                {"pronoun_fa": "این دوچرخه‌ی آبی، مالِ کیست؟", "form_fa": "این دوچرخه‌ی آبی، مالِ من است."},
            ],
            "examples": [
                {"fa": "این عینک، مالِ من است و آن عینک، مالِ برادرم صادق است.", "az": "Bu eynək mənimdir, o eynək isə qardaşım Sadiqindir."},
                {"fa": "یکی از این دفترها، مالِ خواهرم پروین است.", "az": "Bu dəftərlərdən biri bacım Pərvinindir."},
                {"fa": "این عصا مالِ کیست؟ این عصا، مالِ پدربزرگم است.", "az": "Bu əl ağacı kimindir? Bu əl ağacı babamındır."},
                {"fa": "آیا آن خانه‌ی زیبا مالِ عبّاس است؟ بله، آن خانه‌ی زیبا، مالِ عبّاس است.", "az": "O gözəl ev Abbasınmıdır? Bəli, o gözəl ev Abbasındır."},
                {"fa": "این انگشتر، مالِ کیست؟ این انگشتر، مالِ دوستم است.", "az": "Bu üzük kimindir? Bu üzük dostumundur."},
            ],
        },
    ],
    "exercises": [
        {
            "kind": "fill_blank",
            "instruction_az": "Uyğun sözlə tamamlayın.",
            "word_bank": ["نوزاد", "مهربان", "معلول", "نابینا", "ناشنوا"],
            "items": [
                {"fa_with_blank": "کسی که دیگران را دوست دارد و به آن‌ها کمک می‌کند، ___ است.", "correct_answer": "مهربان"},
                {"fa_with_blank": "کسی که دست و پایش سالم نیست، ___ است.", "correct_answer": "معلول"},
                {"fa_with_blank": "به بچّه‌ای که دو یا سه هفته سن دارد، ___ می‌گویند.", "correct_answer": "نوزاد"},
                {"fa_with_blank": "کسی که چشمانش نمی‌بیند، ___ است.", "correct_answer": "نابینا"},
                {"fa_with_blank": "کسی که گوش‌هایش نمی‌شنود، ___ است.", "correct_answer": "ناشنوا"},
            ],
        },
        {
            "kind": "fill_blank",
            "instruction_az": "«دست، دسته؛ پا، پایه؛ چشم، چشمه» kimi cüt sözlərdən doğru olanı seçin.",
            "word_bank": ["دسته", "پایه", "چشمه", "دندانه", "ریشه"],
            "items": [
                {"fa_with_blank": "پارچ و سطل ___ دارند.", "correct_answer": "دسته"},
                {"fa_with_blank": "این صندلی، چهار ___ دارد.", "correct_answer": "پایه"},
                {"fa_with_blank": "در کوه و جنگل ___ وجود دارد.", "correct_answer": "چشمه"},
                {"fa_with_blank": "حرف «س» سه ___ دارد.", "correct_answer": "دندانه"},
                {"fa_with_blank": "درخت ___ دارد.", "correct_answer": "ریشه"},
            ],
        },
        {
            "kind": "multiple_choice",
            "instruction_az": "«بدن انسان» mətninə görə düzgün cavabı seçin.",
            "items": [
                {"question_fa": "بدن انسان از چه قسمت‌هایی تشکیل شده است؟", "options": ["پوست، گوشت، خون، استخوان و...", "فقط پوست و استخوان", "فقط گوشت"], "correct_index": 0},
                {"question_fa": "ما با پوستمان چه چیزهایی را احساس می‌کنیم؟", "options": ["گرمی، سردی، زبری و نرمی", "فقط رنگ‌ها", "فقط صداها"], "correct_index": 0},
                {"question_fa": "در بدن انسان چند عدد استخوان وجود دارد؟", "options": ["بیش از دویست عدد", "پنجاه عدد", "هزار عدد"], "correct_index": 0},
                {"question_fa": "محکم‌ترین و بلندترین استخوان بدن انسان کدام است؟", "options": ["استخوان ران", "استخوان دست", "استخوان جمجمه"], "correct_index": 0},
                {"question_fa": "چرا بعضی از مردم از عینک استفاده می‌کنند؟", "options": ["چون چشم‌هایشان ضعیف است و خوب نمی‌بینند", "چون گوش‌هایشان درد می‌کند", "برای زیبایی"], "correct_index": 0},
                {"question_fa": "با زبان چه چیزی را حس می‌کنیم؟", "options": ["طعم و مزه‌ی خوردنی‌ها", "بوی گل‌ها", "صداها"], "correct_index": 0},
                {"question_fa": "قلب در بدن چه‌کار می‌کند؟", "options": ["خون را به همه‌جای بدن می‌رساند", "غذا را هضم می‌کند", "صدا را می‌شنود"], "correct_index": 0},
                {"question_fa": "با دست چه کارهایی می‌کنیم؟", "options": ["می‌نویسیم، غذا می‌خوریم و وسایل را برمی‌داریم", "فقط راه می‌رویم", "فقط می‌شنویم"], "correct_index": 0},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Nümunə kimi cümlə qurun: «گوش: ما به وسیله‌ی گوش می‌شنویم.»",
            "items": [
                {"prompt_fa": "دست", "answer_fa": "ما به وسیله‌ی دست می‌نویسیم."},
                {"prompt_fa": "بینی", "answer_fa": "ما به وسیله‌ی بینی نفس می‌کشیم و بو می‌کنیم."},
                {"prompt_fa": "چشم", "answer_fa": "ما به وسیله‌ی چشم می‌بینیم."},
                {"prompt_fa": "زبان", "answer_fa": "ما به وسیله‌ی زبان حرف می‌زنیم و طعم غذا را حس می‌کنیم."},
                {"prompt_fa": "پا", "answer_fa": "ما به وسیله‌ی پا راه می‌رویم."},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "«مالِ …» ilə soruşub cavab verin: «انگشتر / دوستم → این انگشتر، مالِ کیست؟ این انگشتر، مالِ دوستم است.»",
            "items": [
                {"prompt_fa": "پالتو / برادرِ حسن", "answer_fa": "این پالتو، مالِ کیست؟ این پالتو، مالِ برادرِ حسن است."},
                {"prompt_fa": "آپارتمان / عمویم", "answer_fa": "این آپارتمان، مالِ کیست؟ این آپارتمان، مالِ عمویم است."},
                {"prompt_fa": "مداد رنگی / فرزندِ جواد", "answer_fa": "این مداد رنگی، مالِ کیست؟ این مداد رنگی، مالِ فرزندِ جواد است."},
                {"prompt_fa": "ساعت مچی / پسرِ محمّد", "answer_fa": "این ساعت مچی، مالِ کیست؟ این ساعت مچی، مالِ پسرِ محمّد است."},
            ],
        },
    ],
    "sentence_practice": {
        "listen_items": [],
        "answer_items": [],
    },
    "reading_text": {
        "title_fa": "بدن انسان",
        "title_az": "İnsan bədəni",
        "paragraphs_fa": [
            "بدن انسان قسمت‌های گوناگونی، مانندِ پوست، گوشت، خون، استخوان و... دارد. رنگ پوست انسان‌ها گوناگون است. بعضی از انسان‌ها زردپوست هستند؛ بعضی سیاه‌پوست، برخی سرخ‌پوست و بعضی دیگر سفیدپوست هستند. ما به وسیله‌ی پوست، گرمی، سردی، زبری و نرمی را احساس می‌کنیم.",
            "در بدن انسان، بیش از دویست عدد استخوان وجود دارد. استخوان‌ها بسیار محکم هستند. محکم‌ترین و بلندترین استخوان بدن انسان، استخوان ران است.",
            "در بدن انسان، دو چشم برای دیدن و دو گوش برای شنیدن وجود دارد. بعضی از مردم، چشم‌هایشان ضعیف است و خوب نمی‌بینند. آن‌ها برای بهتر دیدن از عینک استفاده می‌کنند.",
            "ما با بینی علاوه بر نفس کشیدن، بوی غذاها، بوی گل‌ها، عطرها و... را احساس می‌کنیم. به وسیله‌ی زبان حرف می‌زنیم و طعم و مزه‌ی خوردنی‌ها، مانندِ شیرین بودن عسل، شور بودن نمک، تند بودن فلفل و ترش بودن بعضی از میوه‌ها را حس می‌کنیم.",
            "در بدن ما اعضای دیگری هم وجود دارد، مانندِ قلب که به وسیله‌ی آن خون به همه‌جای بدن می‌رسد؛ پا که به وسیله‌ی آن راه می‌رویم و دست که به وسیله‌ی آن غذا می‌خوریم، می‌نویسیم و وسایل را برمی‌داریم.",
        ],
        "footnotes": [
            {"fa": "به وسیله‌یِ", "az": "…vasitəsilə"},
            {"fa": "علاوه بر", "az": "…-dan əlavə"},
            {"fa": "برخی: بعضی", "az": "bəziləri"},
        ],
        "full_translation_az": (
            "İnsan bədəni dəri, ət, qan, sümük və s. kimi müxtəlif hissələrdən ibarətdir. İnsanların dəri rəngi "
            "müxtəlifdir. Bəzi insanlar sarı dərili, bəziləri qara dərili, bəziləri qırmızı dərili, digərləri isə "
            "ağ dərilidirlər. Biz dəri vasitəsilə isti, soyuq, kobud və yumşaq olmağı hiss edirik.\n\n"
            "İnsan bədənində iki yüzdən çox sümük var. Sümüklər çox möhkəmdir. İnsan bədəninin ən möhkəm və ən "
            "uzun sümüyü bud sümüyüdür.\n\n"
            "İnsan bədənində görmək üçün iki göz, eşitmək üçün iki qulaq var. Bəzi insanların gözləri zəifdir və "
            "yaxşı görmürlər. Onlar daha yaxşı görmək üçün eynəkdən istifadə edirlər.\n\n"
            "Biz burunla nəfəs almaqdan əlavə, yeməklərin iyini, güllərin ətrini, ətirləri və s. hiss edirik. Dil "
            "vasitəsilə danışırıq və balın şirin, duzun şor, istiotun acı, bəzi meyvələrin isə turş olmasını hiss "
            "edirik.\n\n"
            "Bədənimizdə başqa üzvlər də var, məsələn ürək ki, onun vasitəsilə qan bədənin hər yerinə çatır; "
            "ayaq ki, onun vasitəsilə yeriyirik; əl isə onun vasitəsilə yemək yeyirik, yazırıq və əşyaları "
            "götürürük."
        ),
    },
}
