# Dərs 14 — ساعت و زمان (Saat və vaxt)
# Mənbə: کتاب دوم, səh. 171-182

LESSON = {
    "number": 14,
    "title_fa": "ساعت و زمان",
    "title_az": "Saat və vaxt",
    "available": True,
    "vocabulary": [
        {"fa": "ساعت مچی", "reading": "saəte moçi", "az": "Qol saatı"},
        {"fa": "ساعت دیواری", "reading": "saəte divari", "az": "Divar saatı"},
        {"fa": "عقربه", "reading": "əqrəbe", "az": "Əqrəb (saat əqrəbi)"},
        {"fa": "دقیقه", "reading": "dəqiqe", "az": "Dəqiqə"},
        {"fa": "باتری", "reading": "batəri", "az": "Batareya"},
        {"fa": "بند ساعت", "reading": "bənde saət", "az": "Saat qayışı"},
        {"fa": "سالم", "reading": "salem", "az": "Sağlam, işlək"},
        {"fa": "خراب", "reading": "xərab", "az": "Xarab"},
        {"fa": "ساعت‌ساز", "reading": "saətsaz", "az": "Saatsaz"},
        {"fa": "ساعت‌سازی", "reading": "saətsazi", "az": "Saat təmiri emalatxanası"},
        {"fa": "ساعت‌فروش", "reading": "saətforuş", "az": "Saat satan"},
        {"fa": "ساعت‌فروشی", "reading": "saətforuşi", "az": "Saat mağazası"},
        {"fa": "روز", "reading": "ruz", "az": "Gün"},
        {"fa": "صبح", "reading": "sobh", "az": "Səhər"},
        {"fa": "ظهر", "reading": "zohr", "az": "Günorta"},
        {"fa": "بعدازظهر (عصر)", "reading": "bədəzzohr (əsr)", "az": "Günortadan sonra (əsr)"},
        {"fa": "سحر", "reading": "səhər", "az": "Dan yeri, sübh"},
        {"fa": "سرشب", "reading": "sərşəb", "az": "Axşamüstü (gecənin əvvəli)"},
        {"fa": "شب", "reading": "şəb", "az": "Gecə"},
        {"fa": "نیمه‌شب", "reading": "nimeşəb", "az": "Gecəyarısı"},
        {"fa": "شبانه‌روز", "reading": "şəbaneruz", "az": "Sutka"},
        {"fa": "خواب", "reading": "xab", "az": "Yuxu"},
        {"fa": "بیدار", "reading": "bidar", "az": "Ayıq, oyaq"},
        {"fa": "تعمیر می‌کند (درست می‌کند)", "reading": "təmir mikonəd (dorost mikonəd)", "az": "təmir edir"},
        {"fa": "طلوع می‌کند", "reading": "toluu mikonəd", "az": "doğur (günəş)"},
        {"fa": "غروب می‌کند", "reading": "qorub mikonəd", "az": "batır (günəş)"},
        {"fa": "می‌خوابد", "reading": "mixabəd", "az": "yatır"},
        {"fa": "بیدار می‌شود", "reading": "bidar mişəvəd", "az": "oyanır"},
        {"fa": "نام خانوادگی", "reading": "name xanevadegi", "az": "Soyad"},
        {"fa": "خوش‌اخلاق", "reading": "xoşəxlaq", "az": "Xoşrəftar"},
        {"fa": "سرِ چهارراه", "reading": "səre çəharrah", "az": "Dördyol ayrıcının başında"},
        {"fa": "فاصله", "reading": "fasele", "az": "Məsafə"},
        {"fa": "سرِ ساعت", "reading": "səre saət", "az": "Vaxtında, dəqiq saatında"},
        {"fa": "دوباره", "reading": "dobare", "az": "Yenidən"},
        {"fa": "شاگرد", "reading": "şagerd", "az": "Şagird, çırağ"},
        {"fa": "همه", "reading": "həme", "az": "Hamısı"},
        {"fa": "وضو می‌گیرد", "reading": "vozu migirəd", "az": "dəstamaz alır"},
        {"fa": "استراحت می‌کند", "reading": "esterahət mikonəd", "az": "istirahət edir"},
    ],
    "grammar_notes": [
        {
            "title_az": "Saatların öyrədilməsi",
            "title_fa": "آموزش ساعت",
            "conjugations": [
                {"pronoun_fa": "ساعت شش است.", "form_fa": "Saat altıdır."},
                {"pronoun_fa": "ساعت، هشت صبح است.", "form_fa": "Saat səhər səkkizdir."},
                {"pronoun_fa": "ساعت، دوازدهِ ظهر است.", "form_fa": "Saat günorta on ikidir."},
                {"pronoun_fa": "ساعت، پنجِ بعدازظهر (عصر) است.", "form_fa": "Saat günortadan sonra beşdir (əsr beşdir)."},
                {"pronoun_fa": "ساعت، نه شب است.", "form_fa": "Saat gecə doqquzdur."},
                {"pronoun_fa": "ساعت، دوازده نیمه‌شب است.", "form_fa": "Saat gecəyarısı on ikidir."},
            ],
            "examples": [
                {"fa": "ساعت «یک» بعدازظهر تا «دوازده» شب را، به این شکل هم می‌گوییم: یک بعدازظهر = سیزده؛ دو بعدازظهر = چهارده؛ … دوازده شب = بیست و چهار.", "az": "24 saatlıq sistemdə: günortadan sonra saat bir = 13, iki = 14 və s., gecə saat on iki = 24."},
                {"fa": "«عصر»: از اواسط بعدازظهر تا غروب آفتاب را «عصر» هم می‌گویند.", "az": "«عصر» (əsr) — günortadan sonranın ortasından günəş batana qədər olan vaxt."},
                {"fa": "«نصف شب»: نیمه‌شب.", "az": "«نصف شب» = gecəyarısı."},
                {"fa": "ساعت، شش است. ساعت، هشتِ صبح است. ساعت، دوازدهِ ظهر است.", "az": "Saat altıdır. Saat səhər səkkizdir. Saat günorta on ikidir."},
                {"fa": "ساعت، سه بعد از نصفِ شب است. ساعت، حدود دوازده است.", "az": "Saat gecəyarısından sonra üçdür. Saat təxminən on ikidir."},
            ],
        },
        {
            "title_az": "Dəqiqələrin bildirilməsi: «ربع» və «نیم»",
            "title_fa": "ساعت با «دقیقه»؛ «ربع» و «نیم»",
            "conjugations": [
                {"pronoun_fa": "ساعت، دوازده و پنج دقیقه است.", "form_fa": "Saat on iki və beş dəqiqədir."},
                {"pronoun_fa": "ساعت، دوازده و پانزده دقیقه است.", "form_fa": "= ساعت، دوازده و ربع است."},
                {"pronoun_fa": "ساعت، دوازده و سی دقیقه است.", "form_fa": "= ساعت، دوازده و نیم است."},
                {"pronoun_fa": "ساعت، دوازده و چهل و پنج دقیقه است.", "form_fa": "= ساعت، یک، ربع کم است (istifadə olunmur — 45 dəqiqə kimi deyilir)."},
            ],
            "examples": [
                {"fa": "«ربع» ilə «دقیقه» eyni cümlədə bir yerdə işlənmir: ساعت دوازده و ربع و نیم دقیقه است. ✗", "az": "«ربع» və «نیم» sözləri «دقیقه» sözü ilə birlikdə işlənmir."},
                {"fa": "ساعت، چهار و ده دقیقه است.", "az": "Saat dörd və on dəqiqədir."},
                {"fa": "ساعت، هفت و پانزده دقیقه است.", "az": "Saat yeddi və on beş dəqiqədir."},
                {"fa": "ساعت، شش و بیست و پنج دقیقه است.", "az": "Saat altı və iyirmi beş dəqiqədir."},
                {"fa": "ساعت، هشت و سی دقیقه است.", "az": "Saat səkkiz və otuz dəqiqədir."},
                {"fa": "ساعت، ده و چهل و هفت دقیقه است.", "az": "Saat on və qırx yeddi dəqiqədir."},
            ],
        },
        {
            "title_az": "Sual sözü «ساعت، چند است؟» (saat neçədir?)",
            "title_fa": "واژه‌ی پرسشی «ساعت، چند است؟»",
            "conjugations": [
                {"pronoun_fa": "ساعت، چند است؟", "form_fa": "ساعت، هفت و بیست دقیقه است."},
            ],
            "examples": [
                {"fa": "ساعت، چند است؟ ساعت، یازده است.", "az": "Saat neçədir? Saat on birdir."},
                {"fa": "ساعت، چند است؟ ساعت، پنج و ده دقیقه است.", "az": "Saat neçədir? Saat beş və on dəqiqədir."},
                {"fa": "ساعت، چند است؟ ساعت، چهار بعدازظهر است.", "az": "Saat neçədir? Saat günortadan sonra dörddür."},
                {"fa": "ساعت، چند است؟ ساعت، سه و چهل و دو دقیقه است.", "az": "Saat neçədir? Saat üç və qırx iki dəqiqədir."},
                {"fa": "در گفتار فارسی «ساعت، چند است؟» را «ساعت، چنده؟» هم می‌گویند.", "az": "Danışıqda «ساعت، چند است؟» sözü «ساعت، چنده؟» kimi deyilir."},
            ],
        },
        {
            "title_az": "Sual sözü «چه وقت» (nə vaxt?)",
            "title_fa": "واژه‌ی پرسشی «چه وقت»",
            "conjugations": [
                {"pronoun_fa": "چه وقت به کلاس آمدی؟", "form_fa": "من ساعت هشت به کلاس آمدم."},
                {"pronoun_fa": "چه وقت به مسافرت می‌روی؟", "form_fa": "من آخر تابستان به مسافرت می‌روم."},
                {"pronoun_fa": "چه وقت ناهار می‌خوری؟", "form_fa": "من بعد از خواندن نماز ظهر، ناهار می‌خورم."},
            ],
            "examples": [
                {"fa": "دیشب چه وقت خوابیدی؟ من دیشب ساعت ده و نیم خوابیدم.", "az": "Dünən gecə nə vaxt yatdın? Mən dünən gecə saat on yarımda yatdım."},
                {"fa": "آقا! ساعتم را چه وقت تعمیر می‌کنی؟ ساعتت را فردا تعمیر می‌کنم.", "az": "Ağa, saatımı nə vaxt təmir edəcəksən? Saatını sabah təmir edəcəyəm."},
                {"fa": "شما چه وقت‌هایی مطالعه می‌کنی؟ من هر روز صبح زود مطالعه می‌کنم.", "az": "Sən hansı vaxtlarda mütaliə edirsən? Mən hər gün səhər tezdən mütaliə edirəm."},
                {"fa": "چه وقت در موزه‌ها را می‌بندند؟ سرِ شب در موزه‌ها را می‌بندند.", "az": "Muzeylərin qapılarını nə vaxt bağlayırlar? Axşamüstü muzeylərin qapılarını bağlayırlar."},
                {"fa": "در زبان گفتار «چه وقت» را «کی» هم می‌گویند: کی به کلاس آمدی؟", "az": "Danışıqda «چه وقت» sözü «کی» kimi işlənir: sinfə nə vaxt gəldin?"},
            ],
        },
    ],
    "exercises": [
        {
            "kind": "fill_blank",
            "instruction_az": "«چه وقت» sualını uyğun cümlə ilə tamamlayın.",
            "word_bank": ["چه وقت", "کی"],
            "items": [
                {"fa_with_blank": "___ فیلم تماشا می‌کنیم؟ ما ساعت نه شب فیلم تماشا می‌کنیم.", "correct_answer": "چه وقت"},
                {"fa_with_blank": "___ به مادرم هدیه می‌دهی؟ من امروز عصر به مادرم هدیه می‌دهم.", "correct_answer": "چه وقت"},
                {"fa_with_blank": "جشن تولّد فرزندم ___ است؟ پس‌فردا است.", "correct_answer": "کی"},
                {"fa_with_blank": "___ کتاب اوّل را خواندی؟ حدود بیست روز قبل.", "correct_answer": "چه وقت"},
            ],
        },
        {
            "kind": "fill_blank",
            "instruction_az": "Uyğun sözlə tamamlayın.",
            "word_bank": ["مچی", "ساعت‌سازی", "تعمیر", "سالم", "ساعت‌ساز", "خراب"],
            "items": [
                {"fa_with_blank": "آن ساعت دیواری ___ نیست؛ خراب است.", "correct_answer": "سالم"},
                {"fa_with_blank": "برادرم ___ است. او ساعت‌های خراب را تعمیر می‌کند.", "correct_answer": "ساعت‌ساز"},
                {"fa_with_blank": "من پریروز رفتم و برای فرزندم یک ساعتِ ___ خریدم.", "correct_answer": "مچی"},
                {"fa_with_blank": "ساعت پدرم خراب است. من امروز ساعت او را برای ___ به ایشان می‌برم.", "correct_answer": "تعمیر"},
                {"fa_with_blank": "پدرم هر روز صبح به ___ آقا ناصر می‌رود.", "correct_answer": "ساعت‌سازی"},
            ],
        },
        {
            "kind": "multiple_choice",
            "instruction_az": "«ساعت‌سازی ناصر» mətninə görə düzgün cavabı seçin.",
            "items": [
                {"question_fa": "نام خانوادگی ناصر چیست؟", "options": ["مهدوی", "رضوی", "احمدی"], "correct_index": 0},
                {"question_fa": "ناصر چه‌کاره است و کجا کار می‌کند؟", "options": ["ساعت‌ساز است؛ در مغازه‌ی خودش", "معلّم است؛ در مدرسه", "پزشک است؛ در بیمارستان"], "correct_index": 0},
                {"question_fa": "مغازه‌ی ناصر کجاست؟", "options": ["خیابان هفده شهریور، پلاک ۱۱۴", "میدان آزادی", "خیابان انقلاب"], "correct_index": 0},
                {"question_fa": "فاصله‌ی خانه‌ی ناصر تا مغازه‌اش چقدر است؟", "options": ["حدود پانصد متر", "حدود پنج کیلومتر", "حدود صد متر"], "correct_index": 0},
                {"question_fa": "ناصر هنگام ظهر چه‌کار می‌کند؟", "options": ["مغازه‌اش را تعطیل می‌کند و برای نماز به مسجد می‌رود", "به خانه می‌رود و می‌خوابد", "درس می‌خواند"], "correct_index": 0},
                {"question_fa": "شاگرد ناصر کیست و از صبح تا ظهر چه‌کار می‌کند؟", "options": ["رضا؛ در دانش‌گاه درس می‌خواند", "رضا؛ در مغازه کار می‌کند", "علی؛ در خانه است"], "correct_index": 0},
                {"question_fa": "رضا هر روز چه ساعتی به ساعت‌سازی می‌رود؟", "options": ["سرِ ساعت پنج", "سرِ ساعت هشت", "سرِ ساعت دو"], "correct_index": 0},
                {"question_fa": "دوست رضا ساعتش را برای چه به او داد؟", "options": ["برای تعمیر", "برای هدیه", "برای فروش"], "correct_index": 0},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Saatı deyin: «ساعت، چند است؟»",
            "items": [
                {"prompt_fa": "۱۱:۰۰", "answer_fa": "ساعت، یازده است."},
                {"prompt_fa": "۵:۱۰", "answer_fa": "ساعت، پنج و ده دقیقه است."},
                {"prompt_fa": "۴:۱۵", "answer_fa": "ساعت، چهار و ربع است."},
                {"prompt_fa": "۸:۳۰", "answer_fa": "ساعت، هشت و نیم است."},
                {"prompt_fa": "۱۰:۴۷", "answer_fa": "ساعت، ده و چهل و هفت دقیقه است."},
                {"prompt_fa": "۱۲:۰۰ (شب)", "answer_fa": "ساعت، دوازده نیمه‌شب است."},
                {"prompt_fa": "۷:۲۵", "answer_fa": "ساعت، هفت و بیست و پنج دقیقه است."},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Nümunə kimi əvəz edin: «استاد سرِ ساعت هشت به کلاس آمد. — مادربزرگم / نه / دارو خوردن → مادربزرگم سرِ ساعت نه دارو خورد.»",
            "items": [
                {"prompt_fa": "کارمندها / هفت و نیم / محل کار آمدن", "answer_fa": "کارمندها سرِ ساعت هفت و نیم به محل کار آمدند."},
                {"prompt_fa": "ما / یازده / اتاقمان خوابیدن", "answer_fa": "ما سرِ ساعت یازده در اتاقمان خوابیدیم."},
                {"prompt_fa": "هواپیما / ده / مشهد رفتن", "answer_fa": "هواپیما سرِ ساعت ده به مشهد رفت."},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Nümunə kimi məsafəni deyin: «فاصله‌ی خانه‌ی ناصر تا مغازه‌اش حدود پانصد متر است. — تهران / قم / صد و سی کیلومتر»",
            "items": [
                {"prompt_fa": "روستای ما / شهر / بیست کیلومتر", "answer_fa": "فاصله‌ی روستای ما تا شهر بیست کیلومتر است."},
                {"prompt_fa": "کشور من / ایران / … کیلومتر", "answer_fa": "فاصله‌ی کشور من تا ایران هزار کیلومتر است."},
                {"prompt_fa": "خانه‌ام / دانش‌گاه / سه کیلومتر", "answer_fa": "فاصله‌ی خانه‌ام تا دانش‌گاه سه کیلومتر است."},
            ],
        },
    ],
    "sentence_practice": {
        "listen_items": [],
        "answer_items": [],
    },
    "reading_text": {
        "title_fa": "ساعت‌سازی ناصر",
        "title_az": "Nasirin saat təmiri emalatxanası",
        "paragraphs_fa": [
            "اسم این آقا، ناصر است و نام خانوادگی او مهدوی است. او ساعت‌ساز است و یک مغازه‌ی ساعت‌سازی‌اش دارد. او در ساعت‌سازی‌اش، ساعت هم می‌فروشد. ساعت‌سازی او در خیابان هفده شهریور، بین میدان امام حسین (ع) و میدان شهدا، سرِ چهارراه امین، کنار بانک ملّی، پلاک ۱۱۴ است.",
            "فاصله‌ی خانه‌ی آقای مهدوی تا مغازه‌اش حدود پانصد متر است. او هر روز ساعت هفت و نیم صبح پیاده به مغازه‌اش می‌رود و تا حدود ظهر در ساعت‌سازی می‌ماند و ساعت‌های خراب را تعمیر می‌کند. ایشان هنگام ظهر، مغازه‌اش را تعطیل می‌کند؛ وضو می‌گیرد و برای خواندن نماز به مسجد می‌رود. او پس از نماز، خوردن ناهار و استراحت‌کردن به خانه برمی‌گردد و ساعت چهار بعدازظهر دوباره به مغازه می‌آید و تا ساعت نه شب کار می‌کند.",
            "آقا ناصر بسیار خوش‌اخلاق است؛ به این سبب مشتری‌های او زیاد هستند و همه او را دوست دارند.",
            "او یک شاگرد هم دارد. اسم شاگردش رضا است. رضا از صبح تا ظهر در دانش‌گاه درس می‌خواند و بعدازظهرها سرِ ساعت پنج به ساعت‌سازی آقا ناصر می‌رود و در تعمیر ساعت‌ها به ایشان کمک می‌کند. دیروز دوست رضا ساعتش را برای تعمیر به او داد. رضا ساعت دوستش را به ساعت‌سازی برد و برایش تعمیر کرد.",
        ],
        "footnotes": [
            {"fa": "نام خانوادگی", "az": "soyad"},
            {"fa": "فاصله", "az": "məsafə"},
            {"fa": "سرِ ساعت", "az": "vaxtında (dəqiq saatında)"},
            {"fa": "خوش‌اخلاق", "az": "xoşrəftar"},
        ],
        "full_translation_az": (
            "Bu kişinin adı Nasirdir və soyadı Mehdəvidir. O, saatsazdır və özünün saat təmiri emalatxanası var. "
            "O, emalatxanasında saat da satır. Onun emalatxanası On yeddi Şəhrivər küçəsində, İmam Hüseyn (ə) "
            "meydanı ilə Şühəda meydanı arasında, Əmin dördyol ayrıcının başında, Milli Bankın yanında, 114 "
            "nömrəli binadadır.\n\n"
            "Cənab Mehdəvinin evindən emalatxanasına qədər olan məsafə təxminən beş yüz metrdir. O, hər gün "
            "səhər saat yeddi yarımda piyada emalatxanasına gedir və günortaya qədər orada qalıb xarab saatları "
            "təmir edir. O, günorta vaxtı dükanını bağlayır, dəstamaz alır və namaz qılmaq üçün məscidə gedir. "
            "Namazdan, nahar yeməkdən və istirahət etməkdən sonra evinə qayıdır və günortadan sonra saat dörddə "
            "yenidən dükana gəlib gecə saat doqquza qədər işləyir.\n\n"
            "Ağa Nasir çox xoşrəftardır; buna görə müştəriləri çoxdur və hamı onu sevir.\n\n"
            "Onun bir şagirdi də var. Şagirdinin adı Rzadır. Rza səhərdən günortaya qədər universitetdə oxuyur "
            "və günortadan sonra saat beşdə dəqiq Ağa Nasirin emalatxanasına gedib saatların təmirində ona kömək "
            "edir. Dünən Rzanın dostu saatını təmir üçün ona verdi. Rza dostunun saatını emalatxanaya apardı və "
            "onun üçün təmir etdi."
        ),
    },
}
