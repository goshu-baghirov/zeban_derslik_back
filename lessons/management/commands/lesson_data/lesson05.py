# Dərs 5 — شغل ۲ (Peşə 2)
# Mənbə: کتاب دوم, səh. 63-74

LESSON = {
    "number": 5,
    "title_fa": "شغل ۲",
    "title_az": "Peşə 2",
    "available": True,
    "vocabulary": [
        {"fa": "باغبان", "reading": "bağban", "az": "Bağban"},
        {"fa": "کشاورز", "reading": "keşavərz", "az": "Əkinçi"},
        {"fa": "نانوا", "reading": "nanva", "az": "Çörəkçi"},
        {"fa": "آشپز", "reading": "aşpəz", "az": "Aşpaz"},
        {"fa": "آرایش‌گر", "reading": "arayeşgər", "az": "Bərbər"},
        {"fa": "تعمیرکار", "reading": "təmirkar", "az": "Təmirçi"},
        {"fa": "میوه‌فروش", "reading": "miveforuş", "az": "Meyvə satan"},
        {"fa": "کتاب‌فروش", "reading": "ketabforuş", "az": "Kitab satan"},
        {"fa": "طلافروش", "reading": "təlaforuş", "az": "Qızıl satan (zərgər)"},
        {"fa": "نویسنده", "reading": "nevisənde", "az": "Yazıçı"},
        {"fa": "خبرنگار", "reading": "xəbərneqar", "az": "Jurnalist (müxbir)"},
        {"fa": "امدادگر", "reading": "emdadgər", "az": "Xilasedici"},
        {"fa": "خلبان", "reading": "xələban", "az": "Pilot"},
        {"fa": "مهمان‌دار", "reading": "mehmandar", "az": "Stüardessa (bələdçi)"},
        {"fa": "بازرگان (تاجر)", "reading": "bazərgan (tacer)", "az": "Tacir"},
        {"fa": "کارمند", "reading": "karmənd", "az": "İşçi (məmur)"},
        {"fa": "خریدار", "reading": "xəridar", "az": "Alıcı (müştəri)"},
        {"fa": "فروشنده", "reading": "foruşənde", "az": "Satıcı"},
        {"fa": "می‌رود", "reading": "mirəvəd", "az": "gedir"},
        {"fa": "می‌آید", "reading": "miayəd", "az": "gəlir"},
        {"fa": "می‌خرد", "reading": "mixərəd", "az": "alır"},
        {"fa": "می‌فروشد", "reading": "miforuşəd", "az": "satır"},
        {"fa": "روستا (ده)", "reading": "rusta (deh)", "az": "Kənd"},
        {"fa": "باغ‌دار", "reading": "bağdar", "az": "Bağ sahibi"},
        {"fa": "اداره‌ی پست", "reading": "edareye post", "az": "Poçt idarəsi"},
        {"fa": "باهم", "reading": "bahəm", "az": "birlikdə"},
        {"fa": "تنها", "reading": "tənha", "az": "tək"},
        {"fa": "بیرون", "reading": "birun", "az": "bayır, çöl"},
    ],
    "grammar_notes": [
        {
            "title_az": "«از» (…-dan) və «به» (…-a) ön qoşmaları",
            "title_fa": "حرف اضافه‌ی «از» ؛ «به»",
            "conjugations": [],
            "examples": [
                {"fa": "من ساعت هفتِ صبح از خانه به مدرسه می‌روم.", "az": "Mən səhər saat yeddidə evdən məktəbə gedirəm."},
                {"fa": "من ساعت دوازده از مدرسه به خانه می‌آیم.", "az": "Mən saat on ikidə məktəbdən evə gəlirəm."},
                {"fa": "من با تاکسی از قم به فرودگاه تهران می‌روم.", "az": "Mən taksi ilə Qumdan Tehran hava limanına gedirəm."},
                {"fa": "خانواده‌ام روز یک‌شنبه از پاکستان به ایران می‌آیند.", "az": "Ailəm bazar günü Pakistandan İrana gəlir."},
                {"fa": "شما از این‌جا به کجا می‌روید؟ من از این‌جا به خانه‌ی دوستم می‌روم.", "az": "Siz buradan hara gedirsiniz? Mən buradan dostumun evinə gedirəm."},
            ],
        },
        {
            "title_az": "«هستم؛ هستی؛ ...» felinin əvəzedicisi (1): استادم = استاد هستم",
            "title_fa": "جانشین فعل «هستم؛ هستی؛ ...» (۱)",
            "conjugations": [
                {"pronoun_fa": "من", "form_fa": "استاد + ـَم → استادم"},
                {"pronoun_fa": "تو", "form_fa": "استاد + ی → استادی"},
                {"pronoun_fa": "او", "form_fa": "استاد + است → استاد است"},
                {"pronoun_fa": "ما", "form_fa": "استاد + یم → استادیم"},
                {"pronoun_fa": "شما", "form_fa": "استاد + ید → استادید"},
                {"pronoun_fa": "آن‌ها", "form_fa": "استاد + ـَند → استادند"},
            ],
            "examples": [
                {"fa": "من خلبانم و برادرم مهندس رایانه است.", "az": "Mən pilotam və qardaşım kompüter mühəndisidir."},
                {"fa": "ما تعمیرکار ساعتیم و آن‌ها تعمیرکار یخچالند.", "az": "Biz saat təmirçisiyik, onlar isə soyuducu təmirçisidirlər."},
                {"fa": "پدر و برادرم بازرگانند. آن‌ها چای و برنج می‌خرند و می‌فروشند.", "az": "Atam və qardaşım tacirdirlər. Onlar çay və düyü alıb-satırlar."},
                {"fa": "من فروشنده نیستم، خریدارم. من برای فرزندم میز و چراغ مطالعه می‌خرم.", "az": "Mən satıcı deyiləm, alıcıyam. Övladım üçün masa və masa lampası alıram."},
                {"fa": "شما چوپانی یا شکارچی؟ من چوپانم.", "az": "Sən çobansan, yoxsa ovçu? Mən çobanam."},
                {"fa": "شما پلیسید یا امدادگرید؟ ما پلیس نیستیم؛ ما امدادگریم.", "az": "Siz polissiniz, yoxsa xilasedici? Biz polis deyilik; biz xilasediciyik."},
            ],
        },
        {
            "title_az": "«هستم؛ ...» felinin əvəzedicisi (2): «ه» ilə bitən sözlər (فروشنده‌ام)",
            "title_fa": "جانشین فعل «هستم؛ هستی؛ ...» (۲)",
            "conjugations": [
                {"pronoun_fa": "من", "form_fa": "فروشنده + ام → فروشنده‌ام"},
                {"pronoun_fa": "تو", "form_fa": "فروشنده + ای → فروشنده‌ای"},
                {"pronoun_fa": "او", "form_fa": "فروشنده + است → فروشنده است"},
                {"pronoun_fa": "ما", "form_fa": "فروشنده + ایم → فروشنده‌ایم"},
                {"pronoun_fa": "شما", "form_fa": "فروشنده + اید → فروشنده‌اید"},
                {"pronoun_fa": "آن‌ها", "form_fa": "فروشنده + اند → فروشنده‌اند"},
            ],
            "examples": [
                {"fa": "ما کتاب‌فروشیم؛ آن‌ها نویسنده‌اند.", "az": "Biz kitab satanıq; onlar yazıçıdırlar."},
                {"fa": "آن‌ها خریدار نیستند؛ آن‌ها فروشنده‌اند.", "az": "Onlar alıcı deyillər; onlar satıcıdırlar."},
                {"fa": "آن‌ها دانش‌آموزند؛ ما معلّمیم و ایشان مدیر مدرسه‌اند.", "az": "Onlar şagirddirlər; biz müəllimik, o (hörmətlə) isə məktəb direktorudur."},
                {"fa": "آیا شما پلیسی؟ نه، من نگهبان مدرسه‌ام.", "az": "Sən polissən? Xeyr, mən məktəbin gözətçisiyəm."},
                {"fa": "آیا شما طلبه‌اید؟ بله، ما طلبه‌ایم.", "az": "Siz tələbəsiniz? Bəli, biz tələbəyik."},
                {"fa": "سعید و برادرش چه‌کاره‌اند؟ آن‌ها راننده‌اند.", "az": "Səid və qardaşı nəçidirlər? Onlar sürücüdürlər."},
            ],
        },
    ],
    "exercises": [
        {
            "kind": "fill_blank",
            "instruction_az": "Boşluqları «از» və ya «به» ilə doldurun.",
            "word_bank": ["از", "به"],
            "items": [
                {"fa_with_blank": "ما ___ لبنان به ایران می‌آییم.", "correct_answer": "از"},
                {"fa_with_blank": "آن‌ها ساعت یک از مسجد ___ خانه می‌آیند.", "correct_answer": "به"},
                {"fa_with_blank": "من برای خریدن لباس و کفش ___ فروش‌گاه می‌روم.", "correct_answer": "به"},
                {"fa_with_blank": "شما ___ کجا می‌آیید و به کجا می‌روید؟", "correct_answer": "از"},
                {"fa_with_blank": "من از این‌جا ___ استخر می‌آیم و به رستوران می‌روم.", "correct_answer": "به"},
            ],
        },
        {
            "kind": "fill_blank",
            "instruction_az": "Boşluğu söz bankından uyğun peşə ilə doldurun.",
            "word_bank": ["آشپز", "نویسنده", "خبرنگار", "دانش‌آموز", "تاجر", "پزشک"],
            "items": [
                {"fa_with_blank": "این خانم ___ است. او کتاب‌های زیادی می‌نویسد.", "correct_answer": "نویسنده"},
                {"fa_with_blank": "محمد و مهدی ___ هستند. آن‌ها بیماران را معاینه می‌کنند.", "correct_answer": "پزشک"},
                {"fa_with_blank": "برادرم ___ است. او هر روز چهار ساعت به کلاس می‌رود.", "correct_answer": "دانش‌آموز"},
                {"fa_with_blank": "ما در آن دانش‌گاه ___ هستیم. ما هر روز برای دانش‌جوها غذا می‌پزیم.", "correct_answer": "آشپز"},
                {"fa_with_blank": "پدر زینب ___ است. او از ایران پسته می‌خرد و در آفریقا و اروپا می‌فروشد.", "correct_answer": "تاجر"},
            ],
        },
        {
            "kind": "multiple_choice",
            "instruction_az": "«فرهاد» mətninə görə düzgün cavabı seçin.",
            "items": [
                {"question_fa": "فرهاد چه‌کاره است؟", "options": ["کارمند دانش‌گاه مشهد", "کارمند اداره‌ی پست", "مدیر مدرسه"], "correct_index": 0},
                {"question_fa": "مریم کارمند کدام اداره است؟", "options": ["اداره‌ی بانک", "اداره‌ی پست", "اداره‌ی مدرسه"], "correct_index": 1},
                {"question_fa": "مریم ناهار را کجا می‌خورد؟", "options": ["در دانش‌گاه", "در اداره", "در خانه، تنها"], "correct_index": 2},
                {"question_fa": "پدر مریم چه‌کاره است؟", "options": ["مدیر مدرسه", "باغ‌دار", "معلّم"], "correct_index": 0},
                {"question_fa": "پدر فرهاد چه‌کاره است و کجا زندگی می‌کند؟", "options": ["کشاورز است؛ در شهر", "باغ‌دار است؛ در روستا", "میوه‌فروش است؛ در نیشابور"], "correct_index": 1},
                {"question_fa": "در باغ پدر فرهاد چه درخت‌هایی وجود دارد؟", "options": ["سیب، انار و هلو", "پرتقال و نارگیل", "گیلاس و زردآلو"], "correct_index": 0},
                {"question_fa": "فرهاد و مریم روزهای جمعه به کجا می‌روند؟", "options": ["به مشهد", "گاهی به روستا و گاهی به نیشابور", "به فرودگاه"], "correct_index": 1},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Nümunə kimi «از … به …» ilə deyin: «فاطمه و مریم می‌روند. (دانش‌گاه ـ خانه) → فاطمه و مریم از دانش‌گاه به خانه می‌روند.»",
            "items": [
                {"prompt_fa": "این هواپیما می‌رود. (ایران ـ چین)", "answer_fa": "این هواپیما از ایران به چین می‌رود."},
                {"prompt_fa": "استادمان با قطار می‌رود. (اصفهان ـ شیراز)", "answer_fa": "استادمان با قطار از اصفهان به شیراز می‌رود."},
                {"prompt_fa": "زینب و نرگس هر روز می‌آیند. (مدرسه ـ مسجد)", "answer_fa": "زینب و نرگس هر روز از مدرسه به مسجد می‌آیند."},
                {"prompt_fa": "من برای دیدن دوستم با قطار می‌روم. (پاکستان ـ هند)", "answer_fa": "من برای دیدن دوستم با قطار از پاکستان به هند می‌روم."},
                {"prompt_fa": "من و خواهرم برای درس‌خواندن می‌آییم. (کشورمان ـ ایران)", "answer_fa": "من و خواهرم برای درس‌خواندن از کشورمان به ایران می‌آییم."},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Nümunə kimi çevirin: «من آهنگر هستم = من آهنگرم؛ من راننده هستم = من راننده‌ام»",
            "items": [
                {"prompt_fa": "من معلّم هستم.", "answer_fa": "من معلّمم."},
                {"prompt_fa": "ما مهندس هستیم.", "answer_fa": "ما مهندسیم."},
                {"prompt_fa": "من و دوستم طلبه هستیم.", "answer_fa": "من و دوستم طلبه‌ایم."},
                {"prompt_fa": "آن‌ها نویسنده هستند.", "answer_fa": "آن‌ها نویسنده‌اند."},
                {"prompt_fa": "من پرستار هستم؛ پزشک نیستم.", "answer_fa": "من پرستارم؛ پزشک نیستم."},
                {"prompt_fa": "ما امدادگر هستیم؛ پلیس نیستیم.", "answer_fa": "ما امدادگریم؛ پلیس نیستیم."},
                {"prompt_fa": "آیا شما فروشنده هستی؟", "answer_fa": "آیا شما فروشنده‌ای؟"},
                {"prompt_fa": "آیا شما تاجر فرش هستید؟", "answer_fa": "آیا شما تاجر فرشید؟"},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "İndi əksinə çevirin: «ما خبرنگاریم = ما خبرنگار هستیم»",
            "items": [
                {"prompt_fa": "آن‌ها راننده‌اند.", "answer_fa": "آن‌ها راننده هستند."},
                {"prompt_fa": "من و برادرم کشاورزیم.", "answer_fa": "من و برادرم کشاورز هستیم."},
                {"prompt_fa": "من تعمیرکار یخچالم.", "answer_fa": "من تعمیرکار یخچال هستم."},
                {"prompt_fa": "شما کارمند بانکید.", "answer_fa": "شما کارمند بانک هستید."},
                {"prompt_fa": "شما کارمند کدام اداره‌اید؟", "answer_fa": "شما کارمند کدام اداره هستید؟"},
                {"prompt_fa": "آن‌ها باغبانند یا میوه‌فروشند؟", "answer_fa": "آن‌ها باغبان هستند یا میوه‌فروش هستند؟"},
                {"prompt_fa": "شما فروشنده‌ای یا خریدار؟", "answer_fa": "شما فروشنده هستی یا خریدار هستی؟"},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "«تنها / باهم» ilə nümunə kimi deyin: «من / مدرسه رفتن / دوستم → من تنها به مدرسه نمی‌روم؛ من و دوستم باهم به مدرسه می‌رویم.»",
            "items": [
                {"prompt_fa": "سعید / غذاخوردن / پدربزرگش", "answer_fa": "سعید تنها غذا نمی‌خورد؛ سعید و پدربزرگش باهم غذا می‌خورند."},
                {"prompt_fa": "فرزندم / خانه آمدن / برادرش", "answer_fa": "فرزندم تنها به خانه نمی‌آید؛ فرزندم و برادرش باهم به خانه می‌آیند."},
                {"prompt_fa": "دخترم / فروش‌گاه رفتن / مادرش", "answer_fa": "دخترم تنها به فروش‌گاه نمی‌رود؛ دخترم و مادرش باهم به فروش‌گاه می‌روند."},
                {"prompt_fa": "مادربزرگم / زندگی‌کردن / مادرم", "answer_fa": "مادربزرگم تنها زندگی نمی‌کند؛ مادربزرگم و مادرم باهم زندگی می‌کنند."},
            ],
        },
    ],
    "sentence_practice": {
        "listen_items": [],
        "answer_items": [],
    },
    "reading_text": {
        "title_fa": "فرهاد",
        "title_az": "Fərhad",
        "paragraphs_fa": [
            "فرهاد، کارمندِ دانش‌گاه مشهد است و همسرش مریم، کارمند اداره‌ی پست است. فرهاد و مریم هر روز صبح باهم از خانه بیرون می‌روند. مریم ساعت دو به خانه می‌آید و تنها ناهار می‌خورد؛ امّا همسرش فرهاد تا ساعت چهار در دانش‌گاه است و آن‌جا غذا می‌خورد.",
            "پدر مریم در شهر نیشابور زندگی می‌کند. او مدیر مدرسه است. در مدرسه‌ی او هجده معلّم درس می‌دهند و دانش‌آموزان زیادی درس می‌خوانند.",
            "پدر فرهاد، باغ‌دار است و با خانواده‌اش در روستا زندگی می‌کند. او یک باغ بزرگ و زیبا دارد. در باغ او، درخت‌های سیب، انار، هلو و... وجود دارد.",
            "فرهاد و همسرش روزهای جمعه گاهی به روستا می‌روند و گاهی برای دیدن خانواده‌ی مریم به نیشابور می‌روند.",
        ],
        "footnotes": [
            {"fa": "اداره‌ی پست", "az": "poçt idarəsi"},
            {"fa": "روستا: ده", "az": "kənd"},
            {"fa": "باغ‌دار", "az": "bağ sahibi"},
            {"fa": "تنها / باهم", "az": "tək / birlikdə"},
        ],
        "full_translation_az": (
            "Fərhad Məşhəd Universitetinin işçisidir, həyat yoldaşı Məryəm isə poçt idarəsinin işçisidir. "
            "Fərhad və Məryəm hər gün səhər birlikdə evdən çıxırlar. Məryəm saat ikidə evə gəlir və naharı tək "
            "yeyir; amma həyat yoldaşı Fərhad saat dördə qədər universitetdədir və yeməyini orada yeyir.\n\n"
            "Məryəmin atası Nişapur şəhərində yaşayır. O, məktəb direktorudur. Onun məktəbində on səkkiz müəllim "
            "dərs deyir və çoxlu şagird oxuyur.\n\n"
            "Fərhadın atası bağ sahibidir və ailəsi ilə kənddə yaşayır. Onun böyük və gözəl bir bağı var. Onun "
            "bağında alma, nar, şaftalı və s. ağacları var.\n\n"
            "Fərhad və həyat yoldaşı cümə günləri bəzən kəndə gedir, bəzən də Məryəmin ailəsini görmək üçün "
            "Nişapura gedirlər."
        ),
    },
}
