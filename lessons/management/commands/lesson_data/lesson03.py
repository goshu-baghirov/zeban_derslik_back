# Dərs 3 — انسان؛ خانواده و بستگان (İnsan; ailə və qohumlar)
# Mənbə: کتاب دوم, səh. 39-50

LESSON = {
    "number": 3,
    "title_fa": "انسان؛ خانواده و بستگان",
    "title_az": "İnsan; ailə və qohumlar",
    "available": True,
    "vocabulary": [
        {"fa": "دختر", "reading": "doxtər", "az": "Qız"},
        {"fa": "پسر", "reading": "pesər", "az": "Oğlan"},
        {"fa": "زن", "reading": "zən", "az": "Qadın"},
        {"fa": "مرد", "reading": "mərd", "az": "Kişi"},
        {"fa": "نوجوان", "reading": "nocavan", "az": "Yeniyetmə"},
        {"fa": "جوان", "reading": "cavan", "az": "Gənc"},
        {"fa": "میان‌سال", "reading": "miyansal", "az": "Orta yaşlı"},
        {"fa": "پیر", "reading": "pir", "az": "Qoca"},
        {"fa": "مجرّد", "reading": "mocərrəd", "az": "Subay"},
        {"fa": "متأهل", "reading": "motəəhhel", "az": "Evli"},
        {"fa": "پدربزرگ", "reading": "pedərbozorg", "az": "Baba"},
        {"fa": "مادربزرگ", "reading": "madərbozorg", "az": "Nənə"},
        {"fa": "پدر", "reading": "pedər", "az": "Ata"},
        {"fa": "مادر", "reading": "madər", "az": "Ana"},
        {"fa": "خواهر", "reading": "xahər", "az": "Bacı"},
        {"fa": "برادر", "reading": "bəradər", "az": "Qardaş"},
        {"fa": "همسر", "reading": "həmsər", "az": "Həyat yoldaşı"},
        {"fa": "شوهر", "reading": "şohər", "az": "Ər"},
        {"fa": "خانم (زن)", "reading": "xanom (zən)", "az": "Xanım (arvad)"},
        {"fa": "فرزند", "reading": "fərzənd", "az": "Övlad"},
        {"fa": "نوه", "reading": "nəve", "az": "Nəvə"},
        {"fa": "عروس", "reading": "ərus", "az": "Gəlin"},
        {"fa": "داماد", "reading": "damad", "az": "Kürəkən"},
        {"fa": "پدرخانم", "reading": "pedərxanom", "az": "Qayınata (arvadın atası)"},
        {"fa": "مادرخانم", "reading": "madərxanom", "az": "Qayınana (arvadın anası)"},
        {"fa": "پدرشوهر", "reading": "pedərşohər", "az": "Qayınata (ərin atası)"},
        {"fa": "مادرشوهر", "reading": "madərşohər", "az": "Qayınana (ərin anası)"},
        {"fa": "عمو", "reading": "əmu", "az": "Əmi"},
        {"fa": "عمّه", "reading": "əmme", "az": "Bibi"},
        {"fa": "دایی", "reading": "dayi", "az": "Dayı"},
        {"fa": "خاله", "reading": "xale", "az": "Xala"},
        {"fa": "برادرزاده", "reading": "bəradərzade", "az": "Qardaş uşağı"},
        {"fa": "خواهرزاده", "reading": "xahərzade", "az": "Bacı uşağı"},
        {"fa": "کمک می‌کند", "reading": "komək mikonəd", "az": "kömək edir"},
        {"fa": "مطالعه می‌کند", "reading": "motaleə mikonəd", "az": "mütaliə edir"},
        {"fa": "ازدواج می‌کند", "reading": "ezdevac mikonəd", "az": "evlənir"},
        {"fa": "زندگی می‌کند", "reading": "zendegi mikonəd", "az": "yaşayır"},
        {"fa": "جارو می‌کند", "reading": "caru mikonəd", "az": "süpürür"},
        {"fa": "تمیز می‌کند", "reading": "təmiz mikonəd", "az": "təmizləyir"},
        {"fa": "هم‌کلاس", "reading": "həmkelas", "az": "Sinif yoldaşı"},
        {"fa": "بسیار؛ خیلی", "reading": "besyar; xeyli", "az": "çox"},
        {"fa": "دوست دارد", "reading": "dust darəd", "az": "sevir, xoşlayır"},
    ],
    "grammar_notes": [
        {
            "title_az": "Ayrı və bitişik əvəzliklər (کتابِ من → کتابم)",
            "title_fa": "ضمیرهای گسسته و پیوسته",
            "explanation_az": (
                "Mənsubiyyət iki cür bildirilir: ayrı (کتابِ من) və bitişik (کتابم) — mənaları eynidir.\n"
                "Bitişik əvəzliklər isimin sonuna qoşulur: ـَم، ـَت، ـَش، ـِمان، ـِتان، ـِشان.\n"
                "Danışıqda qısa (bitişik) forma daha çox işlənir."
            ),
            "conjugations": [
                {"pronoun_fa": "کتاب من", "form_fa": "کتاب + ـَم → کتابم"},
                {"pronoun_fa": "کتاب تو", "form_fa": "کتاب + ـَت → کتابت"},
                {"pronoun_fa": "کتاب او", "form_fa": "کتاب + ـَش → کتابش"},
                {"pronoun_fa": "کتاب ما", "form_fa": "کتاب + ـِمان → کتابمان"},
                {"pronoun_fa": "کتاب شما", "form_fa": "کتاب + ـِتان → کتابتان"},
                {"pronoun_fa": "کتاب آن‌ها", "form_fa": "کتاب + ـِشان → کتابشان"},
            ],
            "note_fa": (
                "۱. «ضمیرِ گسسته» (جدا)، اسم را با «ِ» اضافه به ضمیر وصل می‌کند: کتابِ من، کتابِ تو، کتابِ او...\n"
                "۲. «ضمیرِ پیوسته» (چسبیده) مستقیماً به آخرِ اسم می‌چسبد و «ِ» اضافه حذف می‌شود: کتاب + َم ← کتابم. "
                "هر دو یک معنا دارند، ولی ضمیرِ پیوسته در فارسیِ روزمره بیشتر به‌کار می‌رود.\n"
                "۳. همان‌طور که در ضمیرهای گسسته برای احترام «تو» و «او» را به «شما» و «ایشان» تبدیل می‌کنیم، "
                "در ضمیرهای پیوسته هم برای احترام «ت» و «ش» را به «تان» و «شان» تبدیل می‌کنیم: "
                "فرزندت (تو) → فرزندتان (شما)، فرزندش (او) → فرزندشان (ایشان).\n"
                "۴. توجّه: «شان» هم برای احترام (ایشان) و هم برای جمع (آن‌ها) به‌کار می‌رود: "
                "فرزندشان = هم «فرزندِ ایشان» و هم «فرزندِ آن‌ها»."
            ),
            "note_reading_az": (
                "1. «Zamire gosaste» (cəda), esmi «e» ezafe ilə zamirə vəsl mikonəd: ketabe mən, ketabe to, ketabe u...\n"
                "2. «Zamire peyvəste» (çəsbide) mostəqiman be axəre esm miçəsbəd va «e» ezafe hazf mişəvəd: "
                "ketab + əm ← ketabəm. Hər do yek mə'na darənd, vəli zamire peyvəste dər farsiye ruzəmərre "
                "biştər be-kar mirəvəd.\n"
                "3. Həman-tor ke dər zamirhaye gosaste bəraye ehteram «to» va «u» ra be «şoma» va «işan» "
                "təbdil mikonim, dər zamirhaye peyvəste həm bəraye ehteram «t» va «ş» ra be «tan» va «şan» "
                "təbdil mikonim: fərzəndət (to) → fərzəndetan (şoma), fərzəndəş (u) → fərzəndeşan (işan).\n"
                "4. Toəccoh: «şan» həm bəraye ehteram (işan) va həm bəraye cəm (anha) be-kar mirəvəd: "
                "fərzəndeşan = həm «fərzəndé işan» va həm «fərzəndé anha»."
            ),
            "note_az": (
                "1. «Ayrı (gəsəstə) əvəzlik» isimlə əvəzlik arasında izafə «e» səsi ilə bağlanır: "
                "کتابِ من (mənim kitabım), کتابِ تو (sənin kitabın)...\n"
                "2. «Bitişik (peyvəstə) əvəzlik» isə isim + şəkilçi kimi birbaşa sözün sonuna qoşulur, "
                "izafə «e» səsi düşür: کتاب + َم → کتابم (kitabım). Hər ikisi eyni mənanı verir, lakin "
                "gündəlik danışıqda bitişik forma daha çox işlənir.\n"
                "3. Necə ki ayrı əvəzliklərdə hörmət üçün «تو» (sən) və «او» (o) yerinə «شما» (siz) və "
                "«ایشان» (hörmətli o) işlədirik, bitişik əvəzliklərdə də hörmət üçün «ت» və «ش» şəkilçilərini "
                "«تان» və «شان»-a çeviririk: فرزندت (sənin övladın) → فرزندتان (hörmətlə: sizin övladınız), "
                "فرزندش (onun övladı) → فرزندشان (hörmətlə).\n"
                "4. Diqqət: «شان» həm hörmət (ایشان) məqsədilə, həm də cəm (آن‌ها/onlar) mənasında işlənir: "
                "فرزندشان = ya hörmətli şəxsin övladı, ya da onların övladı ola bilər — məna kontekstdən "
                "müəyyən olunur."
            ),
            "examples": [
                {
                    "fa": "کتابِ من، روی میز است. = کتابم، روی میز است.",
                    "reading_az": "Ketabe mən, ruye miz əst. = Ketabəm, ruye miz əst.",
                    "az": "Mənim kitabım masanın üstündədir. = Kitabım masanın üstündədir.",
                },
                {
                    "fa": "برادرت چه دارد؟ برادرم تاکسی دارد.",
                    "reading_az": "Bəradərət çe darəd? Bəradərəm taksi darəd.",
                    "az": "Sənin qardaşının nəyi var? Mənim qardaşımın taksisi var.",
                },
                {
                    "fa": "پدرت کجاست؟ پدرم در فروشگاه است.",
                    "reading_az": "Pedərət kocast? Pedərəm dər foruşgah əst.",
                    "az": "Sənin atan haradadır? Mənim atam mağazadadır.",
                },
                {
                    "fa": "آیا همسر علی، معلّم است؟ نه، همسرش معلّم نیست؛ پرستار است.",
                    "reading_az": "Aya həmsəre Əli, moəllem əst? Nə, həmsərəş moəllem nist; pərəstar əst.",
                    "az": "Əlinin həyat yoldaşı müəllimdirmi? Xeyr, onun həyat yoldaşı müəllim deyil; tibb bacısıdır.",
                },
                {
                    "fa": "آیا فرزندت هر روز مطالعه می‌کند؟ بله، فرزندم هر روز مطالعه می‌کند.",
                    "reading_az": "Aya fərzəndət hər ruz motaleə mikonəd? Bəle, fərzəndəm hər ruz motaleə mikonəd.",
                    "az": "Sənin övladın hər gün mütaliə edirmi? Bəli, mənim övladım hər gün mütaliə edir.",
                },
                {
                    "fa": "آیا پدربزرگ و مادربزرگتان در ایران زندگی می‌کنند؟ نه، پدربزرگ و مادربزرگمان در سوریه زندگی می‌کنند.",
                    "reading_az": "Aya pedərbozorg va madərbozorgetan dər Iran zendegi mikonənd? Nə, pedərbozorg va madərbozorgeman dər Suriye zendegi mikonənd.",
                    "az": "Sizin baba-nənəniz İranda yaşayırmı? Xeyr, bizim baba-nənəmiz Suriyada yaşayır.",
                },
                {
                    "fa": "آیا آن‌ها به پدر و مادرشان کمک می‌کنند؟ بله، آن‌ها به پدر و مادرشان کمک می‌کنند.",
                    "reading_az": "Aya anha be pedər va madərşan komək mikonənd? Bəle, anha be pedər va madərşan komək mikonənd.",
                    "az": "Onlar ata-analarına kömək edirlərmi? Bəli, onlar ata-analarına kömək edirlər.",
                },
                {
                    "fa": "آیا فرزندتان اتاق‌ها را تمیز نمی‌کند؟ چرا، فرزندم اتاق‌ها را تمیز می‌کند.",
                    "reading_az": "Aya fərzəndetan otaqha ra təmiz nemikonəd? Çera, fərzəndəm otaqha ra təmiz mikonəd.",
                    "az": "Sizin övladınız otaqları təmizləmir? Əksinə, mənim övladım otaqları təmizləyir.",
                },
                {
                    "fa": "آیا عمو و عمّه‌ات پرستار هستند؟ نه، عمویم استاد دانش‌گاه و عمّه‌ام پزشک است.",
                    "reading_az": "Aya əmu va əmmeət pərəstar həstənd? Nə, əmuyəm ostade daneşgah va əmməəm pezeşk əst.",
                    "az": "Sənin əmin və bibin tibb bacısıdır? Xeyr, mənim əmim universitet müəllimi, bibim isə həkimdir.",
                },
            ],
        },
        {
            "title_az": "Deyək — deməyək (بگوییم – نگوییم)",
            "title_fa": "بگوییم – نگوییم",
            "explanation_az": (
                "Cümlənin mübtədası ilə sahib eyni şəxsdirsə, bitişik əvəzlik işlədilir.\n"
                "من اتاقم را تمیز می‌کنم. ✓ — من اتاق من را تمیز می‌کنم. ✗\n"
                "Yəni «mənim otağım» yox, sadəcə «otağım» deyilir; qayda bütün şəxslərə aiddir."
            ),
            "conjugations": [
                {"pronoun_fa": "من اتاقم را تمیز می‌کنم. ✓", "form_fa": "من اتاق من را تمیز می‌کنم. ✗"},
                {"pronoun_fa": "ما اتاق شما را تمیز می‌کنیم. ✓", "form_fa": "ما اتاق ما را تمیز می‌کنیم. ✗"},
            ],
            "examples": [
                {
                    "fa": "او هر روز درسش را مطالعه می‌کند. ✓ / او هر روز درس او را مطالعه می‌کند. ✗",
                    "reading_az": "U hər ruz dərseş ra motaleə mikonəd. / U hər ruz dərse u ra motaleə mikonəd.",
                    "az": "Öz əşyandan danışanda bitişik əvəzlik işlənir: “dərsini” (درسش), “dərs onun” yox.",
                },
                {
                    "fa": "آن‌ها در خانه‌ی پدرشان زندگی می‌کنند. ✓ / آن‌ها در خانه‌ی پدر آن‌ها زندگی می‌کنند. ✗",
                    "reading_az": "Anha dər xane-ye pedərşan zendegi mikonənd. / Anha dər xane-ye pedər anha zendegi mikonənd.",
                    "az": "Onlar atalarının evində yaşayırlar — “پدرشان” düzgün formadır.",
                },
                {
                    "fa": "ما در شستن ظرف‌ها به مادرمان کمک می‌کنیم. ✓ / ما در شستن ظرف‌ها به مادر ما کمک می‌کنیم. ✗",
                    "reading_az": "Ma dər şostəne zərfha be madərəman komək mikonim. / Ma dər şostəne zərfha be madəre ma komək mikonim.",
                    "az": "Biz qabları yumaqda anamıza kömək edirik — “مادرمان” düzgün formadır.",
                },
                {
                    "fa": "من و مادربزرگم حیاط خانه را جارو می‌کنیم. ✓ / من و مادربزرگ من، حیاط خانه را جارو می‌کنیم. ✗",
                    "reading_az": "Mən va madərbozorgəm həyate xane ra caru mikonim. / Mən va madərbozorge mən, həyate xane ra caru mikonim.",
                    "az": "Mən və nənəm evin həyətini süpürürük — “مادربزرگم” düzgün formadır.",
                },
            ],
        },
    ],
    "exercises": [
        {
            # 'Ev' dərsinin (Dərs 2) Çalışma 1-i ilə eyni quruluş: sualın üzərinə
            # toxunanda yalnız ONUN oxunuşu açılır, «nümunə» düyməsi cavabı
            # (və toxunanda onun da öz oxunuşunu), tərcümə düyməsi isə
            # tərcümələri göstərir — hər üçü bir-birindən asılı olmadan.
            "kind": "answer_question",
            "title_fa": "مانند مثال تبدیل کنید",
            "instruction_az": "Nümunə kimi əvəzliyi dəyişin (ayrı ↔ bitişik)",
            # Yaşıl = ayrı (gəsəstə) əvəzlik, qırmızı = bitişik (peyvəstə) şəkilçi.
            "example_fa": "برادر *من* : برادر**م**\nکیف**شان** : کیف *آن‌ها*",
            "example_reading_az": "Bəradəre mən : bəradərəm.\nKifeşan : kife anha.",
            "example_az": "Mənim qardaşım : qardaşım.\nOnların çantası : onların çantası.",
            "items": [
                {
                    "fa": "پدر آن‌ها",
                    "reading_az": "pedəre anha",
                    "az": "onların atası",
                    "sample_answer_fa": "پدرشان",
                    "sample_answer_reading_az": "pedərşan",
                    "sample_answer_az": "onların atası",
                },
                {
                    "fa": "خودکار او",
                    "reading_az": "xodkare u",
                    "az": "onun tükənməz qələmi",
                    "sample_answer_fa": "خودکارش",
                    "sample_answer_reading_az": "xodkarəş",
                    "sample_answer_az": "onun tükənməz qələmi",
                },
                {
                    "fa": "مادربزرگ ما",
                    "reading_az": "madərbozorge ma",
                    "az": "bizim nənəmiz",
                    "sample_answer_fa": "مادربزرگمان",
                    "sample_answer_reading_az": "madərbozorgəman",
                    "sample_answer_az": "bizim nənəmiz",
                },
                {
                    "fa": "چتر شما",
                    "reading_az": "çətre şoma",
                    "az": "sizin çətriniz",
                    "sample_answer_fa": "چترتان",
                    "sample_answer_reading_az": "çətretan",
                    "sample_answer_az": "sizin çətriniz",
                },
                {
                    "fa": "فرزند بزرگ شما",
                    "reading_az": "fərzənde bozorge şoma",
                    "az": "sizin böyük övladınız",
                    "sample_answer_fa": "فرزند بزرگتان",
                    "sample_answer_reading_az": "fərzəde bozorgetan",
                    "sample_answer_az": "sizin böyük övladınız",
                },
                {
                    "fa": "چشمم",
                    "reading_az": "çeşməm",
                    "az": "mənim gözüm",
                    "sample_answer_fa": "چشم من",
                    "sample_answer_reading_az": "çeşme mən",
                    "sample_answer_az": "mənim gözüm",
                },
                {
                    "fa": "پولتان",
                    "reading_az": "puletan",
                    "az": "sizin pulunuz",
                    "sample_answer_fa": "پول شما",
                    "sample_answer_reading_az": "pule şoma",
                    "sample_answer_az": "sizin pulunuz",
                },
                {
                    "fa": "جانمازشان",
                    "reading_az": "canəmazeşan",
                    "az": "onların namazlığı",
                    "sample_answer_fa": "جانماز آن‌ها",
                    "sample_answer_reading_az": "canəmaze anha",
                    "sample_answer_az": "onların namazlığı",
                },
                {
                    "fa": "دامادش",
                    "reading_az": "damadəş",
                    "az": "onun kürəkəni",
                    "sample_answer_fa": "داماد او",
                    "sample_answer_reading_az": "damade u",
                    "sample_answer_az": "onun kürəkəni",
                },
                {
                    "fa": "اتاق‌خوابم",
                    "reading_az": "otağ-xabəm",
                    "az": "mənim yataq otağım",
                    "sample_answer_fa": "اتاق‌خواب من",
                    "sample_answer_reading_az": "otağe xabe mən",
                    "sample_answer_az": "mənim yataq otağım",
                },
                {
                    "fa": "پرچم کشورمان",
                    "reading_az": "pərçəme kəşvəreman",
                    "az": "bizim ölkəmizin bayrağı",
                    "sample_answer_fa": "پرچم کشور ما",
                    "sample_answer_reading_az": "pərçəme kəşvəre ma",
                    "sample_answer_az": "bizim ölkəmizin bayrağı",
                },
            ],
        },
        {
            # Çalışma 1 ilə eyni quruluş: səhv cümləyə toxunanda onun oxunuşu,
            # «nümunə» düyməsi düzəldilmiş cümləni (və onun öz oxunuşunu),
            # tərcümə düyməsi isə tərcüməni açır.
            "kind": "answer_question",
            "title_fa": "لطفاً تصحیح کنید",
            "instruction_az": "Cümlələri düzəldin (bitişik əvəzlik işlədin)",
            "items": [
                {
                    "fa": "شما در دفتر شما نقّاشی می‌کشید.",
                    "reading_az": "Şoma dər dəftəre şoma nəqqaşi mikeşid.",
                    "az": "Siz dəftərinizdə rəsm çəkirsiniz.",
                    "sample_answer_fa": "شما در دفترتان نقّاشی می‌کشید.",
                    "sample_answer_reading_az": "Şoma dər dəftəretan nəqqaşi mikeşid.",
                    "sample_answer_az": "Siz dəftərinizdə rəsm çəkirsiniz.",
                },
                {
                    "fa": "من و مادر من در آشپزخانه غذا می‌پزیم.",
                    "reading_az": "Mən va madəre mən dər aşpəzxane qəza mipəzim.",
                    "az": "Mən və anam mətbəxdə yemək bişiririk.",
                    "sample_answer_fa": "من و مادرم در آشپزخانه غذا می‌پزیم.",
                    "sample_answer_reading_az": "Mən va madərəm dər aşpəzxane qəza mipəzim.",
                    "sample_answer_az": "Mən və anam mətbəxdə yemək bişiririk.",
                },
                {
                    "fa": "ما روزهای جمعه، اتاق ما را تمیز می‌کنیم.",
                    "reading_az": "Ma ruzhaye come, otağe ma ra təmiz mikonim.",
                    "az": "Biz cümə günləri otağımızı təmizləyirik.",
                    "sample_answer_fa": "ما روزهای جمعه، اتاقمان را تمیز می‌کنیم.",
                    "sample_answer_reading_az": "Ma ruzhaye come, otağeman ra təmiz mikonim.",
                    "sample_answer_az": "Biz cümə günləri otağımızı təmizləyirik.",
                },
                {
                    "fa": "آن‌ها کتاب‌های آن‌ها را در کیف می‌گذارند.",
                    "reading_az": "Anha ketabhaye anha ra dər kif migozarənd.",
                    "az": "Onlar kitablarını çantaya qoyurlar.",
                    "sample_answer_fa": "آن‌ها کتاب‌هایشان را در کیف می‌گذارند.",
                    "sample_answer_reading_az": "Anha ketabhayeşan ra dər kif migozarənd.",
                    "sample_answer_az": "Onlar kitablarını çantaya qoyurlar.",
                },
            ],
        },
        {
            # Çalışma 2 ilə eyni quruluş (answer_question). NÜMUNƏ qutusunda
            # iki sətir var: verilən söz dəsti, sonra ondan qurulan tam cümlə.
            # Qırmızı «را» = təsirlik hal əlaməti, yaşıl «دوست دارد» = şəxsə
            # görə dəyişən fel — izahı example_az-dadır.
            "kind": "answer_question",
            "title_fa": "مانند مثال بگویید",
            "instruction_az": "Nümunə kimi cümlə qurun",
            "example_fa": "پدربزرگم / نوه‌هایش\nپدربزرگم نوه‌هایش **را** بسیار *دوست دارد*.",
            "example_reading_az": "Pedərbozorgəm / nəvehayeş\nPedərbozorgəm nəvehayeş ra besyar dust darəd.",
            "example_az": (
                "Verilən sözlər: «پدربزرگم» (babam) + «نوه‌هایش» (onun nəvələri).\n"
                "Quruluş: SUBYEKT + OBYEKT + را + بسیار + دوست دارد.\n"
                "Qırmızı «را» — təsirlik hal əlamətidir, obyektdən sonra gəlir.\n"
                "Yaşıl «دوست دارد» — fel subyektə görə dəyişir: "
                "دارم / داری / دارد / داریم / دارید / دارند.\n"
                "Tərcümə: Babam nəvələrini çox sevir."
            ),
            "items": [
                {
                    "fa": "محمّدعلی / پدر و مادرش",
                    "reading_az": "Mohəmmədəli / pedər va madərəş",
                    "az": "Məhəmmədəli / onun ata-anası",
                    "sample_answer_fa": "محمّدعلی پدر و مادرش را بسیار دوست دارد.",
                    "sample_answer_reading_az": "Mohəmmədəli pedər va madərəş ra besyar dust darəd.",
                    "sample_answer_az": "Məhəmmədəli ata-anasını çox sevir.",
                },
                {
                    "fa": "ما / قرآن خواندن",
                    "reading_az": "Ma / Qoran xandən",
                    "az": "biz / Quran oxumaq",
                    "sample_answer_fa": "ما قرآن خواندن را بسیار دوست داریم.",
                    "sample_answer_reading_az": "Ma Qoran xandən ra besyar dust darim.",
                    "sample_answer_az": "Biz Quran oxumağı çox sevirik.",
                },
                {
                    "fa": "آن کودک / نقّاشی کشیدن",
                    "reading_az": "An kudək / nəqqaşi keşidən",
                    "az": "o uşaq / rəsm çəkmək",
                    "sample_answer_fa": "آن کودک نقّاشی کشیدن را بسیار دوست دارد.",
                    "sample_answer_reading_az": "An kudək nəqqaşi keşidən ra besyar dust darəd.",
                    "sample_answer_az": "O uşaq rəsm çəkməyi çox sevir.",
                },
                {
                    "fa": "من و خواهرم / عمّه و خاله‌مان",
                    "reading_az": "Mən va xahərəm / əmme va xaleman",
                    "az": "mən və bacım / bibimiz və xalamız",
                    "sample_answer_fa": "من و خواهرم عمّه و خاله‌مان را بسیار دوست داریم.",
                    "sample_answer_reading_az": "Mən va xahərəm əmme va xaleman ra besyar dust darim.",
                    "sample_answer_az": "Mən və bacım bibimizi və xalamızı çox sevirik.",
                },
                {
                    "fa": "فاطمه و زینب / مطالعه کردن",
                    "reading_az": "Fateme va Zeynəb / motaleə kərdən",
                    "az": "Fatimə və Zeynəb / mütaliə etmək",
                    "sample_answer_fa": "فاطمه و زینب مطالعه کردن را بسیار دوست دارند.",
                    "sample_answer_reading_az": "Fateme va Zeynəb motaleə kərdən ra besyar dust darənd.",
                    "sample_answer_az": "Fatimə və Zeynəb mütaliə etməyi çox sevirlər.",
                },
                {
                    "fa": "پدرم / برادرزاده و خواهرزاده‌اش",
                    "reading_az": "Pedərəm / bəradərzade va xahərzadeəş",
                    "az": "atam / onun qardaşı və bacısı uşaqları",
                    "sample_answer_fa": "پدرم برادرزاده و خواهرزاده‌اش را بسیار دوست دارد.",
                    "sample_answer_reading_az": "Pedərəm bəradərzade va xahərzadeəş ra besyar dust darəd.",
                    "sample_answer_az": "Atam qardaşı və bacısının uşaqlarını çox sevir.",
                },
            ],
        },
        {
            "kind": "fill_blank",
            "instruction_az": "Bitişik əvəzliklərdən istifadə edərək cavabları tamamlayın.",
            "word_bank": ["برادرم", "مادرش", "پدربزرگمان", "عمه‌ام"],
            "items": [
                {
                    "fa_with_blank": "خانه‌ی برادرت باغچه ندارد؟ چرا، خانه‌ی ___ باغچه دارد.",
                    "correct_answer": "برادرم",
                    "reading_az": "bəradərəm",
                    "az": "qardaşımın",
                    "full_reading_az": "Xane-ye bəradərət bağçe nədarəd? Çera, xane-ye bəradərəm bağçe darəd.",
                    "full_translation_az": "Qardaşının evinin bağçası yoxdurmu? Xeyr (əksinə), qardaşımın evinin bağçası var.",
                },
                {
                    "fa_with_blank": "مادر مریم چه کار می‌کند؟ ___ خانه را تمیز می‌کند و غذا می‌پزد.",
                    "correct_answer": "مادرش",
                    "reading_az": "madərəş",
                    "az": "onun anası",
                    "full_reading_az": "Madəre Məryəm çekar mikonəd? Madərəş xane ra təmiz mikonəd va qəza mipəzəd.",
                    "full_translation_az": "Məryəmin anası nə edir? Onun anası evi təmizləyir və yemək bişirir.",
                },
                {
                    "fa_with_blank": "آیا پدربزرگتان در ایران زندگی می‌کند؟ نه، ___ در پاکستان زندگی می‌کند.",
                    "correct_answer": "پدربزرگمان",
                    "reading_az": "pedərbozorgeman",
                    "az": "bizim babamız",
                    "full_reading_az": "Aya pedərbozorgetan dər Iran zendegi mikonəd? Nə, pedərbozorgeman dər Pakestan zendegi mikonəd.",
                    "full_translation_az": "Babanız İranda yaşayır? Xeyr, bizim babamız Pakistanda yaşayır.",
                },
                {
                    "fa_with_blank": "آیا عمه‌ی شما به مادربزرگت کمک می‌کند؟ بله، ___ به مادربزرگم کمک می‌کند.",
                    "correct_answer": "عمه‌ام",
                    "reading_az": "əmməəm",
                    "az": "mənim bibim",
                    "full_reading_az": "Aya əmme-ye şoma be madərbozorgət komək mikonəd? Bəle, əmməəm be madərbozorgəm komək mikonəd.",
                    "full_translation_az": "Sizin bibiniz nənənizə kömək edir? Bəli, mənim bibim nənəmə kömək edir.",
                },
            ],
        },
        {
            # Çalışma 3 ilə eyni quruluş. NÜMUNƏ qutusunda üç rəng işlənir:
            # qırmızı = subyekt, mavi = kömək edilən şəxs (subyektə uyğun
            # bitişik əvəzlik alır), yaşıl = subyektə görə dəyişən fel.
            "kind": "answer_question",
            "title_fa": "لطفاً جایگزین کنید",
            "instruction_az": "Sözləri nümunədəki kimi əvəz edin",
            "example_fa": (
                "**من** در تمیز کردن اتاق به ***دوستانم*** *کمک می‌کنم*.\n"
                "زینب / شستن ظرف‌ها / مادر ← "
                "**زینب** در شستن ظرف‌ها به ***مادرش*** *کمک می‌کند*."
            ),
            "example_reading_az": (
                "Mən dər təmiz kərdəne otaq be dustanəm komək mikonəm.\n"
                "Zeynəb / şostəne zərfha / madər ← "
                "Zeynəb dər şostəne zərfha be madərəş komək mikonəd."
            ),
            "example_az": (
                "Nümunə: «Mən otağı təmizləməkdə dostlarıma kömək edirəm.»\n"
                "Quruluş: SUBYEKT + در + İŞ + به + ŞƏXS + کمک می‌کند.\n"
                "Qırmızı — subyekt.\n"
                "Mavi — kömək edilən şəxs; subyektə uyğun bitişik əvəzlik alır "
                "(مادر → مادرش).\n"
                "Yaşıl — fel; subyektə görə dəyişir (می‌کنم / می‌کند / می‌کنیم / می‌کنند).\n"
                "Tərcümə: Zeynəb qabları yumaqda anasına kömək edir."
            ),
            "items": [
                {
                    "fa": "ما / پاک‌کردن تابلو / استاد",
                    "reading_az": "Ma / pak-kərdəne təblo / ostad",
                    "az": "biz / lövhəni təmizləmək / müəllim",
                    "sample_answer_fa": "ما در پاک‌کردن تابلو به استادمان کمک می‌کنیم.",
                    "sample_answer_reading_az": "Ma dər pak-kərdəne təblo be ostademan komək mikonim.",
                    "sample_answer_az": "Biz lövhəni təmizləməkdə müəllimimizə kömək edirik.",
                },
                {
                    "fa": "ابراهیم / نقّاشی‌کشیدن / فرزند",
                    "reading_az": "Ebrahim / nəqqaşi-keşidən / fərzənd",
                    "az": "İbrahim / rəsm çəkmək / övlad",
                    "sample_answer_fa": "ابراهیم در نقّاشی‌کشیدن به فرزندش کمک می‌کند.",
                    "sample_answer_reading_az": "Ebrahim dər nəqqaşi-keşidən be fərzendeş komək mikonəd.",
                    "sample_answer_az": "İbrahim rəsm çəkməkdə övladına kömək edir.",
                },
                {
                    "fa": "دایی‌ام / تمیزکردن خانه / همسر",
                    "reading_az": "Dayiəm / təmiz-kərdəne xane / həmsər",
                    "az": "dayım / evi təmizləmək / həyat yoldaşı",
                    "sample_answer_fa": "دایی‌ام در تمیزکردن خانه به همسرش کمک می‌کند.",
                    "sample_answer_reading_az": "Dayiəm dər təmiz-kərdəne xane be həmsərəş komək mikonəd.",
                    "sample_answer_az": "Dayım evi təmizləməkdə həyat yoldaşına kömək edir.",
                },
                {
                    "fa": "پدربزرگ / خواندن درس / نوه",
                    "reading_az": "Pedərbozorg / xandəne dərs / nəve",
                    "az": "baba / dərs oxumaq / nəvə",
                    "sample_answer_fa": "پدربزرگ در خواندن درس به نوه‌اش کمک می‌کند.",
                    "sample_answer_reading_az": "Pedərbozorg dər xandəne dərs be nəveəş komək mikonəd.",
                    "sample_answer_az": "Baba dərs oxumaqda nəvəsinə kömək edir.",
                },
                {
                    "fa": "نرگس و سوسن / جارو کردن حیاط / مادر",
                    "reading_az": "Nərges va Susən / caru kərdəne həyat / madər",
                    "az": "Nərgiz və Susən / həyəti süpürmək / ana",
                    "sample_answer_fa": "نرگس و سوسن در جارو کردن حیاط به مادرشان کمک می‌کنند.",
                    "sample_answer_reading_az": "Nərges va Susən dər caru kərdəne həyat be madərşan komək mikonənd.",
                    "sample_answer_az": "Nərgiz və Susən həyəti süpürməkdə analarına kömək edirlər.",
                },
                {
                    "fa": "من و خواهرم / پختن غذا / مادربزرگ",
                    "reading_az": "Mən va xahərəm / poxtəne qəza / madərbozorg",
                    "az": "mən və bacım / yemək bişirmək / nənə",
                    "sample_answer_fa": "من و خواهرم در پختن غذا به مادربزرگمان کمک می‌کنیم.",
                    "sample_answer_reading_az": "Mən va xahərəm dər poxtəne qəza be madərbozorgeman komək mikonim.",
                    "sample_answer_az": "Mən və bacım yemək bişirməkdə nənəmizə kömək edirik.",
                },
            ],
        },
        {
            # Çalışma 3/4 ilə eyni quruluş. NÜMUNƏ qutusunda: yaşıl = qohumluq
            # adı (sualdakı ipucu və cavabda açılmış forması), qırmızı = əlavə
            # olunan bitişik əvəzlik (پدر → پدرم).
            "kind": "answer_question",
            "title_fa": "مانند مثال بگویید",
            "instruction_az": "Nümunə kimi qohumluq adını deyin",
            "example_fa": "برادرِ پدر (*عمو*)\nبرادر **پدرم**، *عموی من* است.",
            "example_reading_az": "Bəradəre pedər (əmu)\nBəradəre pedərəm, əmuye mən əst.",
            "example_az": (
                "Sual: «برادرِ پدر» — atanın qardaşı; mötərizədəki «عمو» ipucudur (əmi).\n"
                "Cavab: برادر پدرم، عموی من است. = «Atamın qardaşı mənim əmimdir.»\n"
                "Qırmızı — «پدر» sözünə bitişik əvəzlik «ـم» əlavə olunur (پدر → پدرم).\n"
                "Yaşıl — qohumluq adı; cavabda «عموی من» şəklində açılır."
            ),
            "items": [
                {
                    "fa": "برادرِ مادر",
                    "reading_az": "Bəradəre madər",
                    "az": "ananın qardaşı",
                    "sample_answer_fa": "برادر مادرم، دایی من است.",
                    "sample_answer_reading_az": "Bəradəre madərəm, dayiye mən əst.",
                    "sample_answer_az": "Anamın qardaşı mənim dayımdır.",
                },
                {
                    "fa": "مادرِ پدر",
                    "reading_az": "Madəre pedər",
                    "az": "atanın anası",
                    "sample_answer_fa": "مادر پدرم، مادربزرگ من است.",
                    "sample_answer_reading_az": "Madəre pedərəm, madərbozorge mən əst.",
                    "sample_answer_az": "Atamın anası mənim nənəmdir.",
                },
                {
                    "fa": "خواهرِ پدر",
                    "reading_az": "Xahəre pedər",
                    "az": "atanın bacısı",
                    "sample_answer_fa": "خواهر پدرم، عمّه‌ی من است.",
                    "sample_answer_reading_az": "Xahəre pedərəm, əmme-ye mən əst.",
                    "sample_answer_az": "Atamın bacısı mənim bibimdir.",
                },
                {
                    "fa": "دختر و پسرِ فرزند",
                    "reading_az": "Doxtər va pesəre fərzənd",
                    "az": "övladın qızı və oğlu",
                    "sample_answer_fa": "دختر و پسر فرزندم، نوه‌های من هستند.",
                    "sample_answer_reading_az": "Doxtər va pesəre fərzendəm, nəvehaye mən həstənd.",
                    "sample_answer_az": "Övladımın qızı və oğlu mənim nəvələrimdir.",
                },
                {
                    "fa": "همسرِ پسر",
                    "reading_az": "Həmsəre pesər",
                    "az": "oğlun həyat yoldaşı",
                    "sample_answer_fa": "همسر پسرم، عروس من است.",
                    "sample_answer_reading_az": "Həmsəre pesərəm, əruse mən əst.",
                    "sample_answer_az": "Oğlumun həyat yoldaşı mənim gəlinimdir.",
                },
                {
                    "fa": "خواهرِ مادر",
                    "reading_az": "Xahəre madər",
                    "az": "ananın bacısı",
                    "sample_answer_fa": "خواهر مادرم، خاله‌ی من است.",
                    "sample_answer_reading_az": "Xahəre madərəm, xale-ye mən əst.",
                    "sample_answer_az": "Anamın bacısı mənim xalamdır.",
                },
            ],
        },
    ],
    "sentence_practice": {
        "listen_exercises": [
            {
                "items": [
                    {
                        "fa": "پدربزرگ و مادربزرگم پیر هستند؛ آن‌ها در دِه زندگی می‌کنند.",
                        "reading_az": "Pedərbozorg va madərbozorgəm pir həstənd; anha dər deh zendegi mikonənd.",
                        "az": "Babam və nənəm qocadırlar; onlar kənddə yaşayırlar.",
                    },
                    {
                        "fa": "ما هر روز، سه ساعت مطالعه می‌کنیم و یک ساعت تکلیف می‌نویسیم.",
                        "reading_az": "Ma hər ruz, se saət motaleə mikonim va yek saət təklif minevisim.",
                        "az": "Biz hər gün üç saat mütaliə edirik və bir saat tapşırıq yazırıq.",
                    },
                    {
                        "fa": "مادرم هر روز خانه را جارو می‌کند؛ غذا می‌پزد و دو ساعت مطالعه می‌کند.",
                        "reading_az": "Madərəm hər ruz xane ra caru mikonəd; qəza mipəzəd va do saət motaleə mikonəd.",
                        "az": "Anam hər gün evi süpürür, yemək bişirir və iki saat mütaliə edir.",
                    },
                    {
                        "fa": "این مرد اهل ایران است. او در شهر اصفهان زندگی می‌کند.",
                        "reading_az": "İn mərd əhle Iran əst. U dər şəhre Esfəhan zendegi mikonəd.",
                        "az": "Bu kişi İranlıdır. O, İsfahan şəhərində yaşayır.",
                    },
                    {
                        "fa": "من هر روز به مادرم کمک می‌کنم؛ اتاق‌ها را تمیز می‌کنم و ظرف‌ها را می‌شویم.",
                        "reading_az": "Mən hər ruz be madərəm komək mikonəm; otaqha ra təmiz mikonəm va zərfha ra mişuyəm.",
                        "az": "Mən hər gün anama kömək edirəm; otaqları təmizləyirəm və qabları yuyuram.",
                    },
                    {
                        "fa": "صادق، همسرِ دخترم زهرا است. دختر و دامادم در شهر بیروت زندگی می‌کنند.",
                        "reading_az": "Sadeq, həmsəre doxtərəm Zəhra əst. Doxtər va damadəm dər şəhre Beyrut zendegi mikonənd.",
                        "az": "Sadiq qızım Zəhranın həyat yoldaşıdır. Qızım və kürəkənim Beyrut şəhərində yaşayırlar.",
                    },
                    {
                        "fa": "من مجرّد هستم. دوستم سجّاد، متأهل است. او دو فرزند دختر دارد و فرزند پسر ندارد.",
                        "reading_az": "Mən mocərrəd hastəm. Dustəm Səccad, motəəhhel əst. U do fərzəde doxtər darəd va fərzəde pesər nədarəd.",
                        "az": "Mən subayam. Dostum Səccad evlidir. Onun iki qız övladı var, oğlu yoxdur.",
                    },
                    {
                        "fa": "فرزندم متأهل است. او یک پسر به نام مهدی و یک دختر به نام ریحانه دارد.",
                        "reading_az": "Fərzendəm motəəhhel əst. U yek pesər be name Mehdi va yek doxtər be name Reyhane darəd.",
                        "az": "Övladım evlidir. Onun Mehdi adında bir oğlu və Reyhanə adında bir qızı var.",
                    },
                    {
                        "fa": "جواد و سمیّه نوه‌های حسین آقا هستند و حسین آقا پدربزرگ آن‌هاست.",
                        "reading_az": "Cəvad va Sommeyye nəvehaye Hoseyn Ağa həstənd va Hoseyn Ağa pedərbozorge anhast.",
                        "az": "Cavad və Sümeyyə Hüseyn ağanın nəvələridir, Hüseyn ağa isə onların babasıdır.",
                    },
                    {
                        "fa": "من هر روز درس می‌خوانم و در تمیز کردن اتاق به دوستم کمک می‌کنم.",
                        "reading_az": "Mən hər ruz dərs mixanəm va dər təmiz kərdəne otaq be dustəm komək mikonəm.",
                        "az": "Mən hər gün dərs oxuyuram və otağı təmizləməkdə dostuma kömək edirəm.",
                    },
                    {
                        "fa": "پدرم نه پیر است نه جوان؛ ایشان میان‌سال است و چهل و هفت سال دارد.",
                        "reading_az": "Pedərəm nə pir əst nə cavan; işan miyansal əst va çehel va həft sal darəd.",
                        "az": "Atam nə qocadır, nə cavan; o, orta yaşlıdır və qırx yeddi yaşındadır.",
                    },
                ],
            },
            {
                "items": [
                    {
                        "fa": "حسین، شوهرِ لیلا و لیلا، خانمِ حسین است. آن‌ها همسر هم هستند.",
                        "reading_az": "Hoseyn, şohəre Leyla va Leyla, xanome Hoseyn əst. Anha həmsəre həm həstənd.",
                        "az": "Hüseyn Leylanın əridir, Leyla isə Hüseynin xanımıdır (arvadıdır). Onlar bir-birinin həyat yoldaşlarıdır.",
                    },
                    {
                        "fa": "احمد، پدرشوهرِ لیلا و سکینه، مادرشوهرِ لیلا است. لیلا عروسِ آن‌ها است.",
                        "reading_az": "Əhməd, pedərşohəre Leyla va Səkine, madərşohəre Leyla əst. Leyla əruse anha əst.",
                        "az": "Əhməd Leylanın qayınatası, Səkinə isə Leylanın qayınanasıdır. Leyla onların gəlinidir.",
                    },
                    {
                        "fa": "صادق، پدرخانمِ حسین، و خدیجه، مادرخانمِ حسین است. حسین دامادِ خدیجه و صادق است.",
                        "reading_az": "Sadeq, pedərxanome Hoseyn, va Xədice, madərxanome Hoseyn əst. Hoseyn damade Xədice va Sadeq əst.",
                        "az": "Sadiq Hüseynin qayınatası (arvadının atası), Xədicə isə Hüseynin qayınanasıdır (arvadının anası). Hüseyn Xədicə və Sadiqin kürəkənidir.",
                    },
                    {
                        "fa": "پدرشوهرِ لیلا یک خانه‌ی سه طبقه دارد. لیلا و حسین در خانه‌ی او زندگی می‌کنند.",
                        "reading_az": "Pedərşohəre Leyla yek xane-ye se təbəqe darəd. Leyla va Hoseyn dər xane-ye u zendegi mikonənd.",
                        "az": "Leylanın qayınatasının üç mərtəbəli bir evi var. Leyla və Hüseyn onun evində yaşayırlar.",
                    },
                ],
                "note_fa": "۱. بستگان: فامیل‌ها\n۲. لیلا خانم حسین است: لیلا زن حسین است.\n۳. (پدرخانم: پدرزن)؛ (مادرخانم: مادرزن)",
                "note_reading_az": "1. Bəstegan: familiha.\n2. Leyla xanome Hoseyn əst: Leyla zəne Hoseyn əst.\n3. (Pedərxanom: pedərzən); (Madərxanom: madərzən)",
                "note_az": "1. «بستگان» (bəstegan) sözü «فامیل‌ها» (qohumlar) mənasındadır.\n2. «لیلا خانم حسین است» = «لیلا زن حسین است» — yəni Leyla, Hüseynin arvadıdır.\n3. (پدرخانم = qayınata); (مادرخانم = qayınana)",
            },
            {
                "items": [
                    {
                        "fa": "اسم من مهدی است و اسم خواهرم ریحانه است. حسین آقا و لیلا خانم پدر و مادرم هستند.",
                        "reading_az": "Esme mən Mehdi əst va esme xahərəm Reyhane əst. Hoseyn ağa va Leyla xanom pedər va madərəm həstənd.",
                        "az": "Mənim adım Mehdidir, bacımın adı isə Reyhanədir. Hüseyn ağa və Leyla xanım mənim ata-anamdır.",
                    },
                    {
                        "fa": "پدرم یک برادر به نام محمّد و یک خواهر به نام زهرا خانم دارد. محمّد آقا، عموی من و زهرا خانم، عمّه‌ی من است. من و خواهرم ریحانه، برادرزاده‌های آن‌ها هستیم.",
                        "reading_az": "Pedərəm yek bəradər be name Mohəmməd va yek xahər be name Zəhra xanom darəd. Mohəmməd ağa əmuye mən va Zəhra xanom, əmmeye mən əst. Mən va xahərəm Reyhane, bəradərzadehaye anha hastim.",
                        "az": "Atamın Məhəmməd adında bir qardaşı və Zəhra xanım adında bir bacısı var. Məhəmməd ağa mənim əmim, Zəhra xanım isə bibimdir. Mən və bacım Reyhanə onların qardaş uşaqlarıyıq.",
                    },
                    {
                        "fa": "مادرم هم یک برادر و یک خواهر دارد. اسم آن‌ها یوسف و فاطمه است. آقا یوسف، دایی من و فاطمه خانم، خاله‌ی من است. من و ریحانه، خواهرزاده‌های آن‌ها هستیم.",
                        "reading_az": "Madərəm həm yek bəradər va yek xahər darəd. Esme anha Yusof va Fateme əst. Ağa Yusof, dayiye mən va Fateme xanom, xaleye mən əst. Mən va Reyhane, xahərzadehaye anha hastim.",
                        "az": "Anamın da bir qardaşı və bir bacısı var. Onların adı Yusif və Fatimədir. Yusif ağa mənim dayım, Fatimə xanım isə xalamdır. Mən və Reyhanə onların bacı uşaqlarıyıq.",
                    },
                    {
                        "fa": "احمد آقا و آقا صادق، پدربزرگ‌های من هستند و سکینه خانم و خدیجه خانم، مادربزرگ‌های من هستند. من و خواهرم ریحانه، نوه‌های آن‌ها هستیم.",
                        "reading_az": "Əhməd ağa va ağa Sadeq, pedərbozorghaye mən həstənd va Səkine xanom va Xədice xanom, madərbozorghaye mən həstənd. Mən va xahərəm Reyhane, nəvehaye anha hastim.",
                        "az": "Əhməd ağa və Sadiq ağa mənim babalarımdır, Səkinə xanım və Xədicə xanım isə nənələrimdir. Mən və bacım Reyhanə onların nəvələriyik.",
                    },
                ],
            },
        ],
        "answer_items": [
            {
                "fa": "شما مجرّد هستی یا متأهل؟",
                "reading_az": "Şoma mocərrəd hasti ya motəəhhel?",
                "az": "Sən subaysan, yoxsa evli?",
                "sample_answer_fa": "من مجرّد هستم.",
                "sample_answer_reading_az": "Mən mocərrəd hastəm.",
                "sample_answer_az": "Mən subayam.",
            },
            {
                "fa": "شما الآن کجا زندگی می‌کنید؟",
                "reading_az": "Şoma əl-an koca zendegi mikonid?",
                "az": "Siz indi harada yaşayırsınız?",
                "sample_answer_fa": "من الآن در باکو زندگی می‌کنم.",
                "sample_answer_reading_az": "Mən əl-an dər Baku zendegi mikonəm.",
                "sample_answer_az": "Mən indi Bakıda yaşayıram.",
            },
            {
                "fa": "خانواده‌ی شما کجا زندگی می‌کنند؟",
                "reading_az": "Xanevade-ye şoma koca zendegi mikonənd?",
                "az": "Ailəniz harada yaşayır?",
                "sample_answer_fa": "خانواده‌ی من در آذربایجان زندگی می‌کنند.",
                "sample_answer_reading_az": "Xanevade-ye mən dər Azərbaycan zendegi mikonənd.",
                "sample_answer_az": "Mənim ailəm Azərbaycanda yaşayır.",
            },
            {
                "fa": "پدر و مادر شما پیر هستند یا جوان؟",
                "reading_az": "Pedər va madəre şoma pir həstənd ya cavan?",
                "az": "Ata-ananız qocadır, yoxsa cavan?",
                "sample_answer_fa": "پدر و مادرم میان‌سال هستند.",
                "sample_answer_reading_az": "Pedər va madərəm miyansal həstənd.",
                "sample_answer_az": "Ata-anam orta yaşlıdır.",
            },
            {
                "fa": "آیا شما به پیرمردها و پیرزن‌ها کمک می‌کنید؟",
                "reading_az": "Aya şoma be pirmərdha va pirzənha komək mikonid?",
                "az": "Siz qocalara kömək edirsinizmi?",
                "sample_answer_fa": "بله، من به پیرمردها و پیرزن‌ها کمک می‌کنم.",
                "sample_answer_reading_az": "Bəle, mən be pirmərdha va pirzənha komək mikonəm.",
                "sample_answer_az": "Bəli, mən qocalara kömək edirəm.",
            },
            {
                "fa": "آیا پدربزرگ شما هر روز کتاب مطالعه می‌کند؟",
                "reading_az": "Aya pedərbozorge şoma hər ruz ketab motaleə mikonəd?",
                "az": "Babanız hər gün kitab oxuyurmu?",
                "sample_answer_fa": "بله، پدربزرگم هر روز کتاب مطالعه می‌کند.",
                "sample_answer_reading_az": "Bəle, pedərbozorgəm hər ruz ketab motaleə mikonəd.",
                "sample_answer_az": "Bəli, babam hər gün kitab oxuyur.",
            },
        ],
    },
    "reading_text": {
        "title_fa": "دوستم سعید",
        "title_az": "Dostum Səid",
        "paragraphs_fa": [
            "اسم من محمّد است. من اهل استرالیا هستم. پدر و مادرم در آن‌جا زندگی می‌کنند. من در کشور ایران درس می‌خوانم و طلبه‌ی جامعة المصطفی هستم.",
            "ایشان دوستم سعید است. من و سعید هم‌کلاس هستیم. او اهل روسیه است. پدرش استاد دانشگاه و مادرش پرستار است.",
            "سعید یک خواهر و یک برادر دارد. برادرش هفت سال از سعید بزرگ‌تر است. او متأهل است و دو فرزند دختر دارد. پدر و مادر سعید نوه‌هایشان را بسیار دوست دارند.",
            "پدربزرگ و مادربزرگ سعید پیر هستند و در خانه‌ی فرزندشان زندگی می‌کنند. سعید و خانواده‌اش، مادربزرگ و پدربزرگ را خیلی دوست دارند و در کارها به آن‌ها کمک می‌کنند.",
            "سعید یک عمو و دو عمّه دارد. عمو و عمّه‌های سعید از پدرش کوچک‌تر هستند. عموی سعید در کشور لبنان درس می‌خواند. سعید یک خاله هم دارد؛ او دایی ندارد. خاله‌ی او پرستار است و در روسیه زندگی می‌کند.",
        ],
        "footnotes": [
            {"fa": "هم‌کلاس: هم‌کلاسی", "az": "sinif yoldaşı"},
            {"fa": "بسیار: خیلی؛ زیاد", "az": "çox"},
        ],
        "full_translation_az": (
            "Mənim adım Məhəmməddir. Mən Avstraliyadanam. Ata-anam orada yaşayır. Mən İranda oxuyuram və "
            "əl-Müstəfa Cəmiyyətinin tələbəsiyəm.\n\n"
            "Bu, dostum Səiddir. Mən və Səid sinif yoldaşıyıq. O, Rusiyadandır. Atası universitet müəllimi, "
            "anası isə tibb bacısıdır.\n\n"
            "Səidin bir bacısı və bir qardaşı var. Qardaşı Səiddən yeddi yaş böyükdür. O, evlidir və iki qız "
            "övladı var. Səidin ata-anası nəvələrini çox sevirlər.\n\n"
            "Səidin baba və nənəsi qocadırlar və övladlarının evində yaşayırlar. Səid və ailəsi nənə ilə babanı "
            "çox sevir və işlərdə onlara kömək edirlər.\n\n"
            "Səidin bir əmisi və iki bibisi var. Səidin əmisi və bibiləri atasından kiçikdirlər. Səidin əmisi "
            "Livanda oxuyur. Səidin bir xalası da var; dayısı yoxdur. Xalası tibb bacısıdır və Rusiyada yaşayır."
        ),
        "sentences": [
            {"fa": "اسم من محمّد است.", "reading_az": "Esme mən Mohəmməd əst.", "az": "Mənim adım Məhəmməddir.", "new_paragraph": True},
            {"fa": "من اهل استرالیا هستم.", "reading_az": "Mən əhle Ostralia hastəm.", "az": "Mən Avstraliyadanam."},
            {"fa": "پدر و مادرم در آن‌جا زندگی می‌کنند.", "reading_az": "Pedər va madərəm dər anja zendegi mikonənd.", "az": "Ata-anam orada yaşayır."},
            {
                "fa": "من در کشور ایران درس می‌خوانم و طلبه‌ی جامعة المصطفی هستم.",
                "reading_az": "Mən dər kəşvəre Iran dərs mixanəm va təllabe-ye Cameətol-Mostəfa hastəm.",
                "az": "Mən İranda oxuyuram və əl-Müstəfa Cəmiyyətinin tələbəsiyəm.",
            },
            {"fa": "ایشان دوستم سعید است.", "reading_az": "İşan dustəm Səid əst.", "az": "Bu, dostum Səiddir.", "new_paragraph": True},
            {"fa": "من و سعید هم‌کلاس هستیم.", "reading_az": "Mən va Səid həmkelas hastim.", "az": "Mən və Səid sinif yoldaşıyıq."},
            {"fa": "او اهل روسیه است.", "reading_az": "U əhle Rusiye əst.", "az": "O, Rusiyadandır."},
            {
                "fa": "پدرش استاد دانشگاه و مادرش پرستار است.",
                "reading_az": "Pedərəş ostade daneşgah va madərəş pərəstar əst.",
                "az": "Atası universitet müəllimi, anası isə tibb bacısıdır.",
            },
            {"fa": "سعید یک خواهر و یک برادر دارد.", "reading_az": "Səid yek xahər va yek bəradər darəd.", "az": "Səidin bir bacısı və bir qardaşı var.", "new_paragraph": True},
            {"fa": "برادرش هفت سال از سعید بزرگ‌تر است.", "reading_az": "Bəradərəş həft sal əz Səid bozorgtər əst.", "az": "Qardaşı Səiddən yeddi yaş böyükdür."},
            {"fa": "او متأهل است و دو فرزند دختر دارد.", "reading_az": "U motəəhhel əst va do fərzəde doxtər darəd.", "az": "O, evlidir və iki qız övladı var."},
            {
                "fa": "پدر و مادر سعید نوه‌هایشان را بسیار دوست دارند.",
                "reading_az": "Pedər va madəre Səid nəvehayeşan ra besyar dust darənd.",
                "az": "Səidin ata-anası nəvələrini çox sevirlər.",
            },
            {
                "fa": "پدربزرگ و مادربزرگ سعید پیر هستند و در خانه‌ی فرزندشان زندگی می‌کنند.",
                "reading_az": "Pedərbozorg va madərbozorge Səid pir həstənd va dər xane-ye fərzəndeşan zendegi mikonənd.",
                "az": "Səidin baba və nənəsi qocadırlar və övladlarının evində yaşayırlar.",
                "new_paragraph": True,
            },
            {
                "fa": "سعید و خانواده‌اش، مادربزرگ و پدربزرگ را خیلی دوست دارند و در کارها به آن‌ها کمک می‌کنند.",
                "reading_az": "Səid va xanevadeəş, madərbozorg va pedərbozorg ra xeyli dust darənd va dər karha be anha komək mikonənd.",
                "az": "Səid və ailəsi nənə ilə babanı çox sevir və işlərdə onlara kömək edirlər.",
            },
            {"fa": "سعید یک عمو و دو عمّه دارد.", "reading_az": "Səid yek əmu va do əmme darəd.", "az": "Səidin bir əmisi və iki bibisi var.", "new_paragraph": True},
            {
                "fa": "عمو و عمّه‌های سعید از پدرش کوچک‌تر هستند.",
                "reading_az": "Əmu va əmmehaye Səid əz pedərəş kuçektər həstənd.",
                "az": "Səidin əmisi və bibiləri atasından kiçikdirlər.",
            },
            {"fa": "عموی سعید در کشور لبنان درس می‌خواند.", "reading_az": "Əmuye Səid dər kəşvəre Lobnan dərs mixanəd.", "az": "Səidin əmisi Livanda oxuyur."},
            {"fa": "سعید یک خاله هم دارد؛ او دایی ندارد.", "reading_az": "Səid yek xale həm darəd; u dayi nədarəd.", "az": "Səidin bir xalası da var; dayısı yoxdur."},
            {"fa": "خاله‌ی او پرستار است و در روسیه زندگی می‌کند.", "reading_az": "Xale-ye u pərəstar əst va dər Rusiye zendegi mikonəd.", "az": "Xalası tibb bacısıdır və Rusiyada yaşayır."},
        ],
        "comprehension_questions": [
            {
                "question_fa": "محمّد اهل کجاست و الآن کجا زندگی می‌کند؟",
                "reading_az": "Mohəmməd əhle kocast va əl-an koca zendegi mikonəd?",
                "az": "Məhəmməd haralıdır və indi harada yaşayır?",
                "sample_answer_fa": "محمّد اهل استرالیاست و الآن در ایران زندگی می‌کند.",
                "sample_answer_reading_az": "Mohəmməd əhle Ostraliast va əl-an dər Iran zendegi mikonəd.",
                "sample_answer_az": "Məhəmməd Avstraliyalıdır və indi İranda yaşayır.",
            },
            {
                "question_fa": "پدر و مادر محمّد کجا زندگی می‌کنند؟",
                "reading_az": "Pedər va madəre Mohəmməd koca zendegi mikonənd?",
                "az": "Məhəmmədin ata-anası harada yaşayır?",
                "sample_answer_fa": "پدر و مادر محمّد در استرالیا زندگی می‌کنند.",
                "sample_answer_reading_az": "Pedər va madəre Mohəmməd dər Ostralia zendegi mikonənd.",
                "sample_answer_az": "Məhəmmədin ata-anası Avstraliyada yaşayır.",
            },
            {
                "question_fa": "محمّد و سعید کجا درس می‌خوانند؟",
                "reading_az": "Mohəmməd va Səid koca dərs mixanənd?",
                "az": "Məhəmməd və Səid harada oxuyurlar?",
                "sample_answer_fa": "محمّد و سعید در ایران، در جامعة المصطفی درس می‌خوانند.",
                "sample_answer_reading_az": "Mohəmməd va Səid dər Iran, dər Cameətol-Mostəfa dərs mixanənd.",
                "sample_answer_az": "Məhəmməd və Səid İranda, əl-Müstəfa Cəmiyyətində oxuyurlar.",
            },
            {
                "question_fa": "آیا پدر سعید پرستار است؟",
                "reading_az": "Aya pedəre Səid pərəstar əst?",
                "az": "Səidin atası tibb bacısıdırmı?",
                "sample_answer_fa": "نه، پدر سعید پرستار نیست؛ او استاد دانشگاه است.",
                "sample_answer_reading_az": "Nə, pedəre Səid pərəstar nist; u ostade daneşgah əst.",
                "sample_answer_az": "Xeyr, Səidin atası tibb bacısı deyil; o, universitet müəllimidir.",
            },
            {
                "question_fa": "عمو و خاله‌ی سعید چه‌کار می‌کنند؟",
                "reading_az": "Əmu va xale-ye Səid çekar mikonənd?",
                "az": "Səidin əmisi və xalası nə iş görür?",
                "sample_answer_fa": "عموی سعید در لبنان درس می‌خواند و خاله‌اش پرستار است.",
                "sample_answer_reading_az": "Əmuye Səid dər Lobnan dərs mixanəd va xaleəş pərəstar əst.",
                "sample_answer_az": "Səidin əmisi Livanda oxuyur, xalası isə tibb bacısıdır.",
            },
            {
                "question_fa": "آیا پدر و مادر سعید نوه‌هایشان را دوست دارند؟",
                "reading_az": "Aya pedər va madəre Səid nəvehayeşan ra dust darənd?",
                "az": "Səidin ata-anası nəvələrini sevirmi?",
                "sample_answer_fa": "بله، پدر و مادر سعید نوه‌هایشان را بسیار دوست دارند.",
                "sample_answer_reading_az": "Bəle, pedər va madəre Səid nəvehayeşan ra besyar dust darənd.",
                "sample_answer_az": "Bəli, Səidin ata-anası nəvələrini çox sevir.",
            },
            {
                "question_fa": "پدربزرگ و مادربزرگ سعید کجا زندگی می‌کنند؟",
                "reading_az": "Pedərbozorg va madərbozorge Səid koca zendegi mikonənd?",
                "az": "Səidin baba-nənəsi harada yaşayır?",
                "sample_answer_fa": "پدربزرگ و مادربزرگ سعید در خانه‌ی فرزندشان زندگی می‌کنند.",
                "sample_answer_reading_az": "Pedərbozorg va madərbozorge Səid dər xane-ye fərzəndeşan zendegi mikonənd.",
                "sample_answer_az": "Səidin baba-nənəsi övladlarının evində yaşayır.",
            },
        ],
    },
}
