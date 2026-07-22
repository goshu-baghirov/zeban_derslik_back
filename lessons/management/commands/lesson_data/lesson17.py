# Dərs 17 — صفت‌ها (Sifətlər)
# Mənbə: کتاب دوم, səh. 207-216

LESSON = {
    "number": 17,
    "title_fa": "صفت‌ها",
    "title_az": "Sifətlər",
    "available": True,
    "vocabulary": [
        {"fa": "شیرین", "reading": "şirin", "az": "Şirin"},
        {"fa": "ترش", "reading": "torş", "az": "Turş"},
        {"fa": "بالا", "reading": "bala", "az": "Yuxarı"},
        {"fa": "پایین", "reading": "payin", "az": "Aşağı"},
        {"fa": "نو", "reading": "nou", "az": "Təzə"},
        {"fa": "کهنه", "reading": "kohne", "az": "Köhnə"},
        {"fa": "ارزان", "reading": "ərzan", "az": "Ucuz"},
        {"fa": "گران", "reading": "gəran", "az": "Bahalı"},
        {"fa": "خیس", "reading": "xis", "az": "Yaş, islanmış"},
        {"fa": "خشک", "reading": "xoşk", "az": "Quru"},
        {"fa": "نرم", "reading": "nərm", "az": "Yumşaq"},
        {"fa": "زبر", "reading": "zebr", "az": "Sərt, kobud"},
        {"fa": "باز", "reading": "baz", "az": "Açıq"},
        {"fa": "بسته", "reading": "bəste", "az": "Bağlı"},
        {"fa": "روشن", "reading": "rouşən", "az": "İşıqlı"},
        {"fa": "تاریک", "reading": "tarik", "az": "Qaranlıq"},
        {"fa": "قشنگ (زیبا)", "reading": "qəşəng (ziba)", "az": "Gözəl"},
        {"fa": "زشت", "reading": "zeşt", "az": "Çirkin"},
        {"fa": "خوش‌حال", "reading": "xoşhal", "az": "Şad, xoşbəxt"},
        {"fa": "ناراحت", "reading": "narahat", "az": "Narahat, kədərli"},
        {"fa": "ثروتمند", "reading": "servətmənd", "az": "Varlı"},
        {"fa": "فقیر", "reading": "fəqir", "az": "Kasıb"},
        {"fa": "قوی", "reading": "qəvi", "az": "Güclü"},
        {"fa": "ضعیف", "reading": "zəif", "az": "Zəif"},
        {"fa": "شجاع", "reading": "şoja", "az": "Cəsur"},
        {"fa": "ترسو", "reading": "tərsu", "az": "Qorxaq"},
        {"fa": "می‌ترسد", "reading": "mitərsəd", "az": "qorxur"},
        {"fa": "لبخند می‌زند", "reading": "ləbxənd mizənəd", "az": "gülümsəyir"},
        {"fa": "می‌خندد", "reading": "mixəndəd", "az": "gülür"},
        {"fa": "گریه می‌کند", "reading": "gerye mikonəd", "az": "ağlayır"},
        {"fa": "جالب", "reading": "caleb", "az": "Maraqlı"},
        {"fa": "همه‌جور آدم", "reading": "həmecur adəm", "az": "Hər cür insan"},
        {"fa": "بغل‌دستی", "reading": "bəğəldəsti", "az": "Yan qonşusu (oturuşda)"},
        {"fa": "فرد", "reading": "fərd", "az": "Fərd"},
        {"fa": "به نظر من", "reading": "be nəzəre mən", "az": "mənim fikrimcə"},
        {"fa": "ولی", "reading": "vəli", "az": "amma, lakin"},
        {"fa": "خلاصه", "reading": "xolase", "az": "Xülasə"},
        {"fa": "خنده‌رو", "reading": "xəndero", "az": "Şən, gülərüz"},
        {"fa": "هرچه", "reading": "hərçe", "az": "hər nə"},
        {"fa": "می‌ایستد", "reading": "mi-istəd", "az": "dayanır"},
        {"fa": "شوخی می‌کند", "reading": "şuxi mikonəd", "az": "zarafat edir"},
        {"fa": "بازی می‌کند", "reading": "bazi mikonəd", "az": "oynayır"},
    ],
    "grammar_notes": [
        {
            "title_az": "Deyək — deməyək: sifət isimlə uzlaşmır",
            "title_fa": "بگوییم – نگوییم",
            "conjugations": [
                {"pronoun_fa": "آن مرد یک خانه‌ی بزرگ دارد. ✓", "form_fa": "آن مرد یک بزرگ خانه دارد. ✗"},
                {"pronoun_fa": "ما امروز غذای خوش‌مزه خوردیم. ✓", "form_fa": "ما امروز خوش‌مزه غذا خوردیم. ✗"},
                {"pronoun_fa": "در زمستان، لباس ضخیم بپوشید. ✓", "form_fa": "در زمستان، ضخیم لباس بپوشید. ✗"},
            ],
            "examples": [
                {"fa": "فارsca-da sifət həmişə isimdən SONRA gəlir, əvəzinə isimlə arasında izafət (kəsrə) olur.", "az": "Fars dilində sifət isimdən sonra gəlir: خانه‌ی بزرگ (böyük ev), yəni «böyük» sözünü əvvələ çəkmək olmaz."},
                {"fa": "همسرم خیّاط است. او لباس‌های زیبا می‌دوزد.", "az": "Həyat yoldaşım dərzidir. O, gözəl paltarlar tikir."},
                {"fa": "سارا با آبرنگ، یک رنگین‌کمان زیبا نقّاشی می‌کند.", "az": "Sara akvarellə gözəl bir göy qurşağı çəkir."},
                {"fa": "من برای دخترم یک کیف بنفش و یک جامدادی آبی می‌خرم.", "az": "Mən qızım üçün bənövşəyi bir çanta və mavi bir qələmqabı alıram."},
                {"fa": "رفتگرها خیابان‌های کثیف را تمیز می‌کنند.", "az": "Zibilyığanlar çirkli küçələri təmizləyir."},
            ],
        },
        {
            "title_az": "Deyək — deməyək: cəm halında sifət «ها»sız gəlir",
            "title_fa": "بگوییم – نگوییم (صفتِ جمع)",
            "conjugations": [
                {"pronoun_fa": "من لباس تمیز می‌پوشم. ✓ / لباس‌های تمیز می‌پوشم. ✓", "form_fa": "لباس‌های تمیزها می‌پوشم. ✗"},
            ],
            "examples": [
                {"fa": "من لباس‌های تمیز می‌پوشم. (لباس‌های تمیزها ✗)", "az": "Mən təmiz paltarlar geyinirəm — sifət «تمیز» cəm şəkilçisi almır, isim özü cəmlənir."},
                {"fa": "انسان‌های شجاع نمی‌ترسند.", "az": "Cəsur insanlar qorxmurlar."},
                {"fa": "محسن پیراهن‌های سفید را بیشتر از پیراهن‌های رنگی دوست دارد.", "az": "Möhsün ağ köynəkləri rəngli köynəklərdən daha çox sevir."},
                {"fa": "ریحانه لباس‌های خشک را از روی طناب برمی‌دارد و لباس‌های خیس را پهن می‌کند.", "az": "Reyhanə quru paltarları ipdən götürür və yaş paltarları sərir."},
                {"fa": "پدرم گفت: دخترم! گل‌های قشنگ‌ها را انتخاب کن و بخر.", "az": "Səhv forma: «گل‌های قشنگ‌ها» — düzgünü «گل‌های قشنگ»دır."},
            ],
        },
        {
            "title_az": "Müqayisə (تفضیلی) və üstünlük (عالی) dərəcə şəkilçiləri: تر / ترین",
            "title_fa": "صفتِ برتر (تفضیلی) و برترین (عالی)",
            "conjugations": [
                {"pronoun_fa": "صفت ساده", "form_fa": "این پسر، چاق است."},
                {"pronoun_fa": "صفت برتر (تفضیلی) + از", "form_fa": "این پسر، چاق‌تر از آن پسر است."},
                {"pronoun_fa": "صفت برترین (عالی) + ترین", "form_fa": "این پسر، چاق‌ترین پسر است."},
            ],
            "examples": [
                {"fa": "این صندلی، زیباتر از آن صندلی است. (زیباترین ✗ در این جمله چون مقایسه‌ی دوتایی است)", "az": "Bu stul o stuldan gözəldir — iki şeyin müqayisəsində «-tər», üçdən çoxda «-tərin»."},
                {"fa": "خانه‌ی حسن، بزرگ‌تر از خانه‌ی احمد است.", "az": "Həsənin evi Əhmədin evindən böyükdür."},
                {"fa": "کفش شما نوترین کفش من است.", "az": "Sizin ayaqqabınız mənim ən təzə ayaqqabımdır."},
                {"fa": "خط‌کش لیلا ارزان‌تر از خط‌کش نرگس است.", "az": "Leylanın xətkeşi Nərgizin xətkeşindən ucuzdur."},
                {"fa": "این انگور، خوش‌مزه‌ترین انگور است.", "az": "Bu üzüm ən dadlı üzümdür."},
                {"fa": "محمّد قوی‌تر از سعید و یاسر است.", "az": "Məhəmməd Səid və Yasirdən güclüdür."},
            ],
        },
        {
            "title_az": "«چرا» ؛ «چون» و «برای این‌که» (niyə? çünki, ona görə ki)",
            "title_fa": "«چرا» ؛ «چون» و «برای این‌که»",
            "conjugations": [
                {"pronoun_fa": "چرا امروز خیلی خوش‌حال هستی؟", "form_fa": "چون روز تولّد من است."},
                {"pronoun_fa": "چرا روسری و مانتوی آبی می‌پوشی؟", "form_fa": "برای این‌که رنگ آبی را زیاد دوست دارم."},
            ],
            "examples": [
                {"fa": "چرا غذا نمی‌خوری؟ چون سیر هستم؛ گرسنه نیستم.", "az": "Niyə yemək yemirsən? Çünki toxam; ac deyiləm."},
                {"fa": "چرا تکلیف‌هایت را ننوشتی؟ برای این‌که دیروز مریض بودم.", "az": "Niyə tapşırıqlarını yazmadın? Ona görə ki, dünən xəstə idim."},
                {"fa": "چرا لامپ‌ها را روشن کردند؟ چون هوا تاریک است.", "az": "Niyə lampaları yandırdılar? Çünki hava qaranlıqdır."},
                {"fa": "چرا چلوکباب زیاد دوست داری؟ چون چلوکباب بسیار خوش‌مزه است.", "az": "Niyə plov-kababı çox sevirsən? Çünki plov-kabab çox dadlıdır."},
                {"fa": "چرا لباس‌هایت را روی طناب آویزان کردی؟ چون لباس‌هایم خیس بود.", "az": "Niyə paltarlarını ip üstünə asdın? Çünki paltarlarım yaş idi."},
            ],
        },
    ],
    "exercises": [
        {
            "kind": "fill_blank",
            "instruction_az": "Uyğun sifətlə tamamlayın.",
            "word_bank": ["شجاع", "خوش‌حال", "خوش‌مزه", "زیبا", "ثروتمند"],
            "items": [
                {"fa_with_blank": "حسین ___ ترسو نیست.", "correct_answer": "شجاع"},
                {"fa_with_blank": "روزها هوا گرم است و شب‌ها هوا ___ است.", "correct_answer": "خوش‌مزه"},
                {"fa_with_blank": "آن‌ها هنگام ___ بودن لبخند می‌زنند یا می‌خندند.", "correct_answer": "خوش‌حال"},
                {"fa_with_blank": "ثروتمندان لباس‌های ___ می‌پوشند و انسان‌های فقیر، لباس‌های ساده می‌پوشند.", "correct_answer": "ثروتمند"},
                {"fa_with_blank": "این غذا بسیار ___ است.", "correct_answer": "خوش‌مزه"},
            ],
        },
        {
            "kind": "fill_blank",
            "instruction_az": "Müqayisə/üstünlük dərəcəsi ilə tamamlayın.",
            "word_bank": ["بالاتر", "بزرگ‌ترین", "قوی‌ترین", "ضعیف", "خیس"],
            "items": [
                {"fa_with_blank": "این درخت ___ از آن درخت میوه دارد.", "correct_answer": "بالاتر"},
                {"fa_with_blank": "من لباس‌های ___ را روی طناب آویزان کردم.", "correct_answer": "خیس"},
                {"fa_with_blank": "شیر و فیل ___ حیوان‌های جنگل هستند.", "correct_answer": "قوی‌ترین"},
                {"fa_with_blank": "طبقه‌ی سوم از طبقه‌ی دوم ___ است.", "correct_answer": "بالاتر"},
                {"fa_with_blank": "این ساختمان، ___ ساختمان این خیابان است.", "correct_answer": "بزرگ‌ترین"},
            ],
        },
        {
            "kind": "multiple_choice",
            "instruction_az": "«کلاس جالب ما» mətninə görə düzgün cavabı seçin.",
            "items": [
                {"question_fa": "کلاس نویسنده چگونه توصیف شده است؟", "options": ["یکی از بهترین و جالب‌ترین کلاس‌های مدرسه", "کوچک‌ترین کلاس مدرسه", "خلوت‌ترین کلاس مدرسه"], "correct_index": 0},
                {"question_fa": "لاغرترین فرد کلاس کیست و چند کیلو وزن دارد؟", "options": ["بغل‌دستی نویسنده؛ بیشتر از سی و پنج کیلو نیست", "معلّم کلاس؛ چهل کیلو", "دوست نویسنده؛ سی کیلو"], "correct_index": 0},
                {"question_fa": "قدبلندترین فرد کلاس چند متر قد دارد؟", "options": ["حدود دو متر و ده سانتی‌متر", "یک متر و هشتاد سانتی‌متر", "دو متر و پنجاه سانتی‌متر"], "correct_index": 0},
                {"question_fa": "کوتاه‌ترین دانش‌آموز کلاس چند قد دارد؟", "options": ["یک متر و بیست سانتی‌متر", "یک متر و پنجاه سانتی‌متر", "نود سانتی‌متر"], "correct_index": 0},
                {"question_fa": "دو نفر که قدشان خیلی فرق دارد، به چه چیزی تشبیه شده‌اند؟", "options": ["فیل و فنجان", "شیر و روباه", "کوه و دشت"], "correct_index": 0},
                {"question_fa": "چاق‌ترین فرد کلاس چند کیلو وزن دارد؟", "options": ["حدود صد و بیست کیلو", "حدود هشتاد کیلو", "حدود صد کیلو"], "correct_index": 0},
                {"question_fa": "چاق‌ترین فرد کلاس چگونه شخصیّتی دارد؟", "options": ["بسیار خوش‌اخلاق و شوخ", "بسیار ساکت و جدّی", "ترسو و ناراحت"], "correct_index": 0},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Cümləni düzəldin (sifəti isimdən sonraya, izafətlə köçürün).",
            "items": [
                {"prompt_fa": "آن مرد یک بزرگ خانه دارد.", "answer_fa": "آن مرد یک خانه‌ی بزرگ دارد."},
                {"prompt_fa": "ما امروز خوش‌مزه غذا خوردیم.", "answer_fa": "ما امروز غذای خوش‌مزه خوردیم."},
                {"prompt_fa": "در زمستان، ضخیم لباس بپوشید.", "answer_fa": "در زمستان، لباس ضخیم بپوشید."},
                {"prompt_fa": "رنگ‌کار با صورتی رنگ، اتاق را رنگ می‌زند.", "answer_fa": "رنگ‌کار با رنگ صورتی، اتاق را رنگ می‌زند."},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Müqayisə dərəcəsi ilə cümlə qurun: «من / برنج ارزان / خریدن → من برنج ارزان می‌خرم، برنج گران نمی‌خرم.»",
            "items": [
                {"prompt_fa": "محمّد / لباس سفید / دوست داشتن", "answer_fa": "محمّد لباس سفید دوست دارد، لباس رنگی دوست ندارد."},
                {"prompt_fa": "حسین / طبقه‌ی بالا / زندگی کردن", "answer_fa": "حسین طبقه‌ی بالا زندگی می‌کند، طبقه‌ی پایین زندگی نمی‌کند."},
                {"prompt_fa": "انسان ترسو / حیوان‌ها / ترسیدن", "answer_fa": "انسان ترسو از حیوان‌ها می‌ترسد، انسان شجاع نمی‌ترسد."},
                {"prompt_fa": "ثروتمندها / لباس نو و گران / پوشیدن", "answer_fa": "ثروتمندها لباس نو و گران می‌پوشند، لباس کهنه نمی‌پوشند."},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "«چرا … چون» ilə soruşub cavab verin.",
            "items": [
                {"prompt_fa": "چرا دیروز به کلاس نرفتی؟", "answer_fa": "چون مریض بودم."},
                {"prompt_fa": "چرا در کلاس را می‌بندید؟", "answer_fa": "چون هوا سرد است."},
                {"prompt_fa": "چرا کوه، جنگل و دریا را دوست داری؟", "answer_fa": "چون طبیعت آن‌ها بسیار زیباست."},
                {"prompt_fa": "چرا در زمستان، لباس‌های ضخیم می‌پوشیم؟", "answer_fa": "برای این‌که هوا سرد است."},
            ],
        },
    ],
    "sentence_practice": {
        "listen_items": [],
        "answer_items": [],
    },
    "reading_text": {
        "title_fa": "کلاس جالب ما",
        "title_az": "Bizim maraqlı sinfimiz",
        "paragraphs_fa": [
            "کلاس ما یکی از بهترین و جالب‌ترین کلاس‌های مدرسه است. در کلاس ما همه‌جور آدمی هست؛ از کوتاه قد تا بلند قد، از چاقِ چاق تا لاغرِ لاغر.",
            "بغل‌دستی من لاغرترین فرد کلاس است. به نظرم بیشتر از سی و پنج کیلو وزن ندارد. قدبلندترین فرد کلاس ما حدود دو متر و ده سانتی‌متر است و کوتاه‌ترین دانش‌آموز کلاس ما یک متر و بیست سانتی‌متر قد دارد. این دو نفر وقتی کنار هم می‌ایستند، مانند فیل و فنجان هستند.",
            "یکی دیگر از هم‌کلاسی‌هایم، بسیار چاق است. وزن او حدود صد کیلو است؛ امّا چاق‌تر از او در هم کلاس ما هست: چاق‌ترین فرد کلاس ما صد و بیست کیلو وزن دارد. او بسیار خوش‌اخلاق است و همیشه با دیگران شوخی می‌کند.",
        ],
        "footnotes": [
            {"fa": "جالب", "az": "maraqlı"},
            {"fa": "بغل‌دستی", "az": "yan qonşusu"},
            {"fa": "به نظر من", "az": "mənim fikrimcə"},
            {"fa": "خلاصه", "az": "xülasə"},
        ],
        "full_translation_az": (
            "Bizim sinfimiz məktəbin ən yaxşı və ən maraqlı siniflərindən biridir. Sinfimizdə hər cür insan var; "
            "balacaboydan hündürboya qədər, çox arıqdan çox köküyə qədər.\n\n"
            "Yan qonşum sinfin ən arıq şəxsidir. Fikrimcə, otuz beş kiloqramdan çox çəkisi yoxdur. Sinfimizin ən "
            "hündürboylu şəxsi təxminən iki metr on santimetrdir, ən balacaboylu şagirdimiz isə bir metr iyirmi "
            "santimetr boydadır. Bu iki nəfər yan-yana durduqda fil və fincan kimi görünürlər.\n\n"
            "Sinif yoldaşlarımdan biri də çox kökdür. Onun çəkisi təxminən yüz kiloqramdır; amma sinfimizdə "
            "ondan da kökü var: sinfin ən kök şəxsinin çəkisi yüz iyirmi kiloqramdır. O, çox xoşrəftardır və "
            "həmişə başqaları ilə zarafat edir."
        ),
    },
}
