# Dərs 12 — مسافرت (Səyahət)
# Mənbə: کتاب دوم, səh. 147-158

LESSON = {
    "number": 12,
    "title_fa": "مسافرت",
    "title_az": "Səyahət",
    "available": True,
    "vocabulary": [
        {"fa": "قارّه", "reading": "qarre", "az": "Qitə"},
        {"fa": "دفتر مسافرتی", "reading": "dəftəre mosaferəti", "az": "Turizm agentliyi"},
        {"fa": "بلیت", "reading": "belit", "az": "Bilet"},
        {"fa": "قطار شهری (مترو)", "reading": "qətare şəhri (metro)", "az": "Metro"},
        {"fa": "اتوبوس", "reading": "otobus", "az": "Avtobus"},
        {"fa": "پایانه‌ی مسافربری (ترمینال)", "reading": "payaneye mosaferbəri (terminal)", "az": "Avtovağzal (terminal)"},
        {"fa": "مسافر", "reading": "mosafer", "az": "Sərnişin, səyyah"},
        {"fa": "ایستگاه راه‌آهن", "reading": "istqahe rah-ahən", "az": "Dəmiryol stansiyası"},
        {"fa": "راه (جادّه)", "reading": "rah (cadde)", "az": "Yol"},
        {"fa": "تصادف", "reading": "təsadof", "az": "Qəza"},
        {"fa": "ترافیک", "reading": "terafik", "az": "Sıxlıq (tıxac)"},
        {"fa": "شلوغ", "reading": "şoluğ", "az": "İzdihamlı"},
        {"fa": "خلوت", "reading": "xəlvət", "az": "Sakit, boş"},
        {"fa": "نشانی (آدرس)", "reading": "neşani (adres)", "az": "Ünvan"},
        {"fa": "میدان", "reading": "meydan", "az": "Meydan"},
        {"fa": "چهارراه", "reading": "çəharrah", "az": "Dördyol ayrıcı"},
        {"fa": "کوچه", "reading": "kuçe", "az": "Döngə (dar küçə)"},
        {"fa": "بن‌بست", "reading": "bonbəst", "az": "Dalan"},
        {"fa": "اوّل، وسط، آخر", "reading": "əvvəl, vəsət, axər", "az": "Əvvəl, orta, son"},
        {"fa": "سمت راست، سمت چپ", "reading": "səmte rast, səmte çəp", "az": "Sağ tərəf, sol tərəf"},
        {"fa": "مستقیم", "reading": "mostəqim", "az": "Düz (istiqamətdə)"},
        {"fa": "کره‌ی زمین", "reading": "koreye zəmin", "az": "Yer kürəsi"},
        {"fa": "پلاک", "reading": "pelak", "az": "Ev nömrəsi (lövhə)"},
        {"fa": "سوار می‌شود", "reading": "səvar mişəvəd", "az": "minir"},
        {"fa": "پیاده می‌شود", "reading": "piyade mişəvəd", "az": "düşür (nəqliyyatdan)"},
        {"fa": "پیاده می‌رود", "reading": "piyade mirəvəd", "az": "piyada gedir"},
        {"fa": "می‌رسد", "reading": "miresəd", "az": "çatır"},
        {"fa": "ماشین شخصی", "reading": "maşine şəxsi", "az": "Şəxsi avtomobil"},
        {"fa": "پرترافیک", "reading": "porterafik", "az": "Sıxlıqlı (tıxaclı)"},
        {"fa": "تعطیلات", "reading": "tətilat", "az": "Tətil, istirahət"},
        {"fa": "بعضی از", "reading": "bəzi əz", "az": "…-dan bəzisi"},
        {"fa": "ابتدا", "reading": "ebteda", "az": "Əvvəlcə"},
        {"fa": "سپس", "reading": "səpəs", "az": "sonra"},
        {"fa": "سفر می‌کند (مسافرت می‌کند)", "reading": "səfər mikonəd (mosaferət mikonəd)", "az": "səyahət edir"},
        {"fa": "آب و هوا", "reading": "abohəva", "az": "İqlim"},
    ],
    "grammar_notes": [
        {
            "title_az": "«بعد؛ بعد از» ↔ «قبل؛ قبل از»",
            "title_fa": "«بعد»؛ «بعد از» — «قبل»؛ «قبل از»",
            "conjugations": [
                {"pronoun_fa": "من دو روز بعد در تهران هستم.", "form_fa": "من دو روز قبل در مشهد بودم."},
                {"pronoun_fa": "دوشنبه، بعد از یک‌شنبه است.", "form_fa": "یک‌شنبه، قبل از دوشنبه است."},
            ],
            "examples": [
                {"fa": "کتاب‌خانه‌ی آیت‌الله مرعشی، بعد از حرم حضرت معصومه (س) و قبل از چهارراه شهدا است.", "az": "Ayətullah Mərəşi kitabxanası Məsumə həzrətlərinin hərəmindən sonra, şəhidlər dördyolundan əvvəldir."},
                {"fa": "یک‌شنبه، بعد از شنبه و قبل از دوشنبه است.", "az": "Bazar günü şənbədən sonra, bazar ertəsindən əvvəldir."},
                {"fa": "ما بعد از کتاب دوم، کتاب سوم را می‌خوانیم.", "az": "Biz ikinci kitabdan sonra üçüncü kitabı oxuyuruq."},
                {"fa": "فرودگاه مهرآباد تهران، بعد از میدان بزرگ آزادی است.", "az": "Tehranın Mehrabad hava limanı böyük Azadi meydanından sonradır."},
                {"fa": "من قبل از خوردن غذا و بعد از آن دست‌هایم را می‌شویم.", "az": "Mən yeməkdən əvvəl və sonra əllərimi yuyuram."},
            ],
        },
        {
            "title_az": "Zaman zərfi «دیشب؛ امشب؛ فردا شب» + keçmiş zaman feli «رفتم؛ رفتی؛ …»",
            "title_fa": "قید زمان «... دیشب؛ امشب؛ فردا شب؛ ...» و فعل گذشته‌ی «رفتم؛ رفتی؛ ...»",
            "conjugations": [
                {"pronoun_fa": "پریشب", "form_fa": "دو شب قبل"},
                {"pronoun_fa": "دیشب", "form_fa": "یک شب قبل"},
                {"pronoun_fa": "امشب", "form_fa": "امروز شب"},
                {"pronoun_fa": "فرداشب", "form_fa": "یک شب بعد"},
                {"pronoun_fa": "پس‌فرداشب", "form_fa": "دو شب بعد"},
            ],
            "examples": [
                {"fa": "من دیشب به خانه‌ی پدرم رفتم. من امشب به خانه‌ی پدرم می‌روم.", "az": "Mən dünən gecə atamın evinə getdim. Mən bu gecə atamın evinə gedirəm."},
                {"fa": "من فرداشب به خانه‌ی برادرم می‌روم.", "az": "Mən sabah gecə qardaşımın evinə gedirəm."},
                {"fa": "طلبه‌ها هفته‌ی قبل به اصفهان رفتند و دو هفته‌ی بعد به مازندران می‌روند.", "az": "Tələbələr keçən həftə İsfahana getdilər və iki həftə sonra Mazandarana gedirlər."},
                {"fa": "برادرت دیشب به مسافرت رفت یا امشب می‌رود؟ او دو شب قبل به مسافرت رفت.", "az": "Qardaşın dünən gecə səyahətə getdi, yoxsa bu gecə gedir? O, iki gecə əvvəl səyahətə getdi."},
                {"fa": "خانواده‌ام دیروز برای زیارت امام رضا (ع) با قطار به مشهد رفتند. آن‌ها سه روز آن‌جا می‌مانند.", "az": "Ailəm dünən İmam Rzanı (ə) ziyarət etmək üçün qatarla Məşhədə getdi. Onlar üç gün orada qalırlar."},
            ],
        },
        {
            "title_az": "Zaman zərfi «پارسال؛ امسال؛ سال بعد» + keçmiş zaman feli «آمدم؛ آمدی؛ …»",
            "title_fa": "قید زمان «... پارسال؛ امسال؛ سال بعد؛ ...» و فعل گذشته‌ی «آمدم؛ آمدی؛ ...»",
            "conjugations": [
                {"pronoun_fa": "دو سال قبل", "form_fa": "پیرارسال"},
                {"pronoun_fa": "پارسال", "form_fa": "سال قبل"},
                {"pronoun_fa": "امسال", "form_fa": "سال جاری"},
                {"pronoun_fa": "یک سال بعد", "form_fa": "سال بعد"},
                {"pronoun_fa": "دو سال بعد", "form_fa": "دو سال بعد"},
            ],
            "examples": [
                {"fa": "من پارسال به ایران آمدم. من امسال به ایران آمدم.", "az": "Mən keçən il İrana gəldim. Mən bu il İrana gəldim."},
                {"fa": "من یک سال بعد به لبنان می‌آیم. من دو سال بعد به لبنان می‌آیم.", "az": "Mən bir il sonra Livana gəlirəm. Mən iki il sonra Livana gəlirəm."},
                {"fa": "مهدی و حسین دو سال قبل برای درس خواندن به ایران آمدند و چهار سال این‌جا می‌مانند.", "az": "Mehdi və Hüseyn iki il əvvəl oxumaq üçün İrana gəldilər və dörd il burada qalırlar."},
                {"fa": "پدر شما امسال به ایران می‌آید یا سال آینده؟ پدرم سال آینده به ایران می‌آید.", "az": "Sizin atanız bu il İrana gəlir, yoxsa gələn il? Atam gələn il İrana gəlir."},
                {"fa": "خانواده‌ام دو سال قبل برای زیارت به ایران آمدند؛ آن‌ها امسال هم می‌آیند.", "az": "Ailəm iki il əvvəl ziyarət üçün İrana gəldi; onlar bu il də gəlirlər."},
            ],
        },
        {
            "title_az": "«بعضی از» quruluşu (…-lərdən bəzisi)",
            "title_fa": "«بعضی از»",
            "conjugations": [
                {"pronoun_fa": "طلبه / شهر مشهد / درس", "form_fa": "بعضی از طلبه‌ها در شهر مشهد درس می‌خوانند."},
            ],
            "examples": [
                {"fa": "بعضی از مردم با ماشین شخصی مسافرت می‌کنند و بعضی هم به دفترهای مسافرتی می‌روند.", "az": "İnsanların bəzisi şəxsi maşınla səyahət edir, bəzisi isə turizm agentliklərinə gedir."},
                {"fa": "بعضی از دانش‌جوها در کتاب‌خانه مطالعه می‌کنند.", "az": "Tələbələrin bəzisi kitabxanada mütaliə edir."},
                {"fa": "دوست من بعضی از روزهای هفته به باشگاه می‌رود.", "az": "Dostum həftənin bəzi günləri idman zalına gedir."},
                {"fa": "بعضی از خانم‌ها در بیمارستان کار می‌کنند.", "az": "Xanımların bəzisi xəstəxanada işləyir."},
                {"fa": "بعضی از انسان‌ها با ماشین شخصی مسافرت می‌کنند.", "az": "İnsanların bəzisi şəxsi avtomobillə səyahət edir."},
                {"fa": "در زبان فارسی پس از واژه‌های «بعضی از»، «بسیاری از» و «بیشتر»، واژه‌ی جمع یا اسم جمع می‌آید.", "az": "Fars dilində «بعضی از», «بسیاری از» və «بیشتر» sözlərindən sonra cəm isim gəlir."},
            ],
        },
    ],
    "exercises": [
        {
            "kind": "fill_blank",
            "instruction_az": "«قبل، قبل از، بعد، بعد از» ilə tamamlayın.",
            "word_bank": ["بعد از", "قبل از", "بعد", "قبل"],
            "items": [
                {"fa_with_blank": "او ده روز ___ به کشورش می‌رود.", "correct_answer": "بعد"},
                {"fa_with_blank": "پدر و مادرم دو هفته ___ در ایران بودند.", "correct_answer": "قبل"},
                {"fa_with_blank": "صندوق‌دار ___ گرفتنِ پول، آن را می‌شمارد.", "correct_answer": "بعد از"},
                {"fa_with_blank": "پنج‌شنبه ___ جمعه و ___ چهارشنبه است.", "correct_answer": "قبل از"},
                {"fa_with_blank": "مسافران ___ مسافرت از دفتر مسافرتی بلیت اتوبوس، قطار یا هواپیما می‌خرند.", "correct_answer": "قبل از"},
            ],
        },
        {
            "kind": "fill_blank",
            "instruction_az": "Uyğun felin keçmiş zaman formasını yazın.",
            "word_bank": ["رفتم", "رفت", "برمی‌گردد", "رفتند", "آمدند"],
            "items": [
                {"fa_with_blank": "من پریشب به خانه‌ی برادرم ___ .", "correct_answer": "رفتم"},
                {"fa_with_blank": "دوستم دیشب به شمال ___ و فرداشب برمی‌گردد.", "correct_answer": "رفت"},
                {"fa_with_blank": "علی سه شب قبل برای زیارت به مشهد رفت؛ برادرش دو شب بعد ___ .", "correct_answer": "رفت"},
                {"fa_with_blank": "محسن و برادرش دیشب به خانه‌ی پدربزرگشان ___ و پس‌فردا شب برمی‌گردند.", "correct_answer": "آمدند"},
                {"fa_with_blank": "طلبه‌ها هفته‌ی قبل به اصفهان ___ .", "correct_answer": "رفتند"},
            ],
        },
        {
            "kind": "multiple_choice",
            "instruction_az": "«مسافرت» mətninə görə düzgün cavabı seçin.",
            "items": [
                {"question_fa": "بیشتر مردم چه روزهایی به مسافرت می‌روند؟", "options": ["روزهای تعطیل", "روزهای کاری", "روزهای امتحان"], "correct_index": 0},
                {"question_fa": "مردم با چه چیزهایی مسافرت می‌کنند؟", "options": ["فقط با هواپیما", "با ماشین شخصی یا با بلیت اتوبوس، قطار و هواپیما", "فقط پیاده"], "correct_index": 1},
                {"question_fa": "احمد و خانواده‌اش هر چند سال یک بار به مسافرت می‌روند؟", "options": ["هر سال یک بار", "هر دو یا سه سال یک بار", "هر ماه یک بار"], "correct_index": 1},
                {"question_fa": "آن‌ها در تعطیلات عید نوروز به کجا مسافرت می‌کنند؟", "options": ["به شهر همدان", "به شهر مشهد", "به شهر شیراز"], "correct_index": 0},
                {"question_fa": "آن‌ها در روزهای اوّل تابستان به کجا می‌روند؟", "options": ["به همدان", "برای زیارت امام رضا (ع) به مشهد", "به تبریز"], "correct_index": 1},
                {"question_fa": "احمد و همسرش پارسال برای مسافرت کدام شهرها را انتخاب کردند؟", "options": ["اصفهان و شیراز", "تبریز و اردبیل", "همدان و مشهد"], "correct_index": 0},
                {"question_fa": "آن‌ها امسال به کدام شهرها می‌روند؟", "options": ["اصفهان و شیراز", "تبریز و اردبیل", "قم و تهران"], "correct_index": 1},
                {"question_fa": "آن‌ها ابتدا به کدام شهر می‌روند و چند روز آن‌جا می‌مانند؟", "options": ["اردبیل؛ دو روز", "تبریز؛ سه روز", "اصفهان؛ یک روز"], "correct_index": 0},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "«بعضی از» ilə cümlə qurun: «طلبه / شهر مشهد / درس → بعضی از طلبه‌ها در شهر مشهد درس می‌خوانند.»",
            "items": [
                {"prompt_fa": "دوست من / قارّه‌ی اروپا / زندگی", "answer_fa": "بعضی از دوستان من در قارّه‌ی اروپا زندگی می‌کنند."},
                {"prompt_fa": "خانم / بیمارستان / کار", "answer_fa": "بعضی از خانم‌ها در بیمارستان کار می‌کنند."},
                {"prompt_fa": "انسان / ماشین شخصی / مسافرت", "answer_fa": "بعضی از انسان‌ها با ماشین شخصی مسافرت می‌کنند."},
                {"prompt_fa": "دانش‌جو / کتاب‌خانه / مطالعه", "answer_fa": "بعضی از دانش‌جوها در کتاب‌خانه مطالعه می‌کنند."},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Nümunə kimi əvəz edin: «دوستم سال بعد برای درس خواندن به این‌جا می‌آید. (پارسال) → دوستم پارسال برای درس خواندن به این‌جا آمد.»",
            "items": [
                {"prompt_fa": "ما سال آینده به کشورتان می‌آییم. (دو سال قبل)", "answer_fa": "ما دو سال قبل به کشورتان آمدیم."},
                {"prompt_fa": "مهندس‌ها امسال برای ساختن پل به این‌جا می‌آیند. (پارسال)", "answer_fa": "مهندس‌ها پارسال برای ساختن پل به این‌جا آمدند."},
                {"prompt_fa": "دوستانم پارسال برای دیدن من به این‌جا می‌آیند. (سال آینده)", "answer_fa": "دوستانم سال آینده برای دیدن من به این‌جا می‌آیند."},
                {"prompt_fa": "حسین و همسرش سال بعد برای زندگی‌کردن به این شهر می‌آیند. (سال قبل)", "answer_fa": "حسین و همسرش سال قبل برای زندگی‌کردن به این شهر آمدند."},
                {"prompt_fa": "من امسال برای زیارت امام علی (ع) با هواپیما به شهر نجف می‌روم. (سال گذشته)", "answer_fa": "من سال گذشته برای زیارت امام علی (ع) با هواپیما به شهر نجف رفتم."},
                {"prompt_fa": "دکتر جوادی دیروز برای معاینه‌ی بیماران به این بیمارستان آمد. (پس‌فردا)", "answer_fa": "دکتر جوادی پس‌فردا برای معاینه‌ی بیماران به این بیمارستان می‌آید."},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Nümunə kimi cümlə qurun: «ما ساعت هفت سوار اتوبوس می‌شویم و ساعت هشت به مدرسه می‌رسیم.»",
            "items": [
                {"prompt_fa": "مسافران / هواپیما / مشهد", "answer_fa": "مسافران سوار هواپیما می‌شوند و به مشهد می‌رسند."},
                {"prompt_fa": "کارگرها / مترو / کارخانه", "answer_fa": "کارگرها سوار مترو می‌شوند و به کارخانه می‌رسند."},
                {"prompt_fa": "آن کشاورز / اسب / مزرعه", "answer_fa": "آن کشاورز سوار اسب می‌شود و به مزرعه می‌رسد."},
                {"prompt_fa": "من / ماشینم / دانش‌گاه", "answer_fa": "من سوار ماشینم می‌شوم و به دانش‌گاه می‌رسم."},
            ],
        },
    ],
    "sentence_practice": {
        "listen_items": [],
        "answer_items": [],
    },
    "reading_text": {
        "title_fa": "مسافرت",
        "title_az": "Səyahət",
        "paragraphs_fa": [
            "بسیاری از مردم جهان در روزهای تعطیل به مسافرت می‌روند. در این روزها بیشتر جادّه‌ها و خیابان‌ها شلوغ و پرترافیک است. بعضی از مردم با ماشین شخصی مسافرت می‌کنند و بعضی هم به دفترهای مسافرتی می‌روند و بلیت هواپیما، قطار یا اتوبوس می‌خرند.",
            "احمد و خانواده‌اش هر سال دو یا سه بار به مسافرت می‌روند. آن‌ها در تعطیلات عید نوروز برای دیدن پدر، مادر و بستگانشان به شهر همدان مسافرت می‌کنند و در روزهای اوّل تابستان، حدود چهار روز، برای زیارت امام رضا (ع) به مشهد می‌روند. آن‌ها هر سال در روزهای آخر تابستان به یکی از شهرهای زیبای ایران سفر می‌کنند.",
            "احمد و همسرش پارسال برای مسافرت، شهرهای اصفهان و شیراز را انتخاب کردند. آن‌ها ابتدا به اصفهان رفتند و سه روز در آن‌جا ماندند و سپس به شیراز مسافرت کردند. این دو شهر از شهرهای بزرگ، قدیمی و زیبای ایران هستند.",
            "آن‌ها امسال به شهرهای تبریز و اردبیل می‌روند. این دو شهر دارای کوه‌های بلند و آب‌وهوای بسیار خوبی است. احمد با خانواده‌اش ابتدا به اردبیل می‌روند و دو روز آن‌جا می‌مانند. آن‌ها سپس به شهر تبریز مسافرت می‌کنند.",
        ],
        "footnotes": [
            {"fa": "بعضی از", "az": "…-dan bəzisi"},
            {"fa": "ابتدا / سپس", "az": "əvvəlcə / sonra"},
            {"fa": "تعطیلات", "az": "tətil, istirahət"},
            {"fa": "آب‌وهوا", "az": "iqlim"},
        ],
        "full_translation_az": (
            "Dünya əhalisinin çoxu istirahət günlərində səyahətə çıxır. Bu günlərdə yolların və küçələrin çoxu "
            "izdihamlı və tıxaclı olur. İnsanların bəzisi şəxsi avtomobillə səyahət edir, bəzisi isə turizm "
            "agentliklərinə gedib təyyarə, qatar və ya avtobus bileti alır.\n\n"
            "Əhməd və ailəsi hər il iki-üç dəfə səyahətə gedir. Onlar Novruz bayramı tətilində ata, ana və "
            "qohumlarını görmək üçün Həmədan şəhərinə, yayın ilk günlərində isə təxminən dörd gün İmam Rzanı (ə) "
            "ziyarət etmək üçün Məşhədə gedirlər. Onlar hər il yayın son günlərində İranın gözəl şəhərlərindən "
            "birinə səyahət edirlər.\n\n"
            "Əhməd və həyat yoldaşı keçən il səyahət üçün İsfahan və Şiraz şəhərlərini seçdilər. Onlar əvvəlcə "
            "İsfahana getdilər və orada üç gün qaldılar, sonra isə Şiraza səyahət etdilər. Bu iki şəhər İranın "
            "böyük, qədim və gözəl şəhərlərindəndir.\n\n"
            "Onlar bu il Təbriz və Ərdəbil şəhərlərinə gedirlər. Bu iki şəhərin uca dağları və çox yaxşı iqlimi "
            "var. Əhməd ailəsi ilə əvvəlcə Ərdəbilə gedir və orada iki gün qalır. Sonra isə Təbriz şəhərinə "
            "səyahət edirlər."
        ),
    },
}
