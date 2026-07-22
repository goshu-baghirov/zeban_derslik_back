# Dərs 20 — ورزش (İdman)
# Mənbə: کتاب دوم, səh. 243-254

LESSON = {
    "number": 20,
    "title_fa": "ورزش",
    "title_az": "İdman",
    "available": True,
    "vocabulary": [
        {"fa": "ورزش‌گاه", "reading": "vərzeşgah", "az": "Stadion"},
        {"fa": "سالن ورزشی", "reading": "salone vərzeşi", "az": "İdman zalı"},
        {"fa": "ورزش‌کار", "reading": "vərzeşkar", "az": "İdmançı"},
        {"fa": "مربّی", "reading": "morəbbi", "az": "Məşqçi"},
        {"fa": "داور", "reading": "davər", "az": "Hakim (idman)"},
        {"fa": "کشتی", "reading": "koşti", "az": "Güləş"},
        {"fa": "شنا", "reading": "şena", "az": "Üzgüçülük"},
        {"fa": "تیراندازی", "reading": "tirandazi", "az": "Atıcılıq"},
        {"fa": "اسب‌سواری", "reading": "əsbsəvari", "az": "At çapma"},
        {"fa": "والیبال", "reading": "valeybal", "az": "Voleybol"},
        {"fa": "بسکتبال", "reading": "basketbal", "az": "Basketbol"},
        {"fa": "تنیس روی میز (پینگ‌پونگ)", "reading": "tenise ruye miz (ping-pong)", "az": "Stolüstü tennis"},
        {"fa": "ورزش رزمی", "reading": "vərzeşe rəzmi", "az": "Döyüş idmanı"},
        {"fa": "شمشیربازی", "reading": "şəmşirbazi", "az": "Qılıncoynatma"},
        {"fa": "بدن‌سازی", "reading": "bədənsazi", "az": "Bədənqurma"},
        {"fa": "دوچرخه‌سواری", "reading": "douçərxesəvari", "az": "Velosiped sürmə"},
        {"fa": "اسکی", "reading": "eski", "az": "Xizəksürmə"},
        {"fa": "کوه‌نوردی", "reading": "kuhnəvərdi", "az": "Dağa dırmaşma"},
        {"fa": "پیاده‌روی", "reading": "piyaderəvi", "az": "Piyada gəzinti"},
        {"fa": "دو و میدانی", "reading": "dəvo miydani", "az": "Yüngül atletika"},
        {"fa": "قهرمان", "reading": "qəhrəman", "az": "Çempion"},
        {"fa": "لباس ورزشی", "reading": "lebase vərzeşi", "az": "İdman geyimi"},
        {"fa": "مسابقه می‌دهد", "reading": "mosabeqe midəhəd", "az": "yarışa çıxır"},
        {"fa": "پیروز می‌شود", "reading": "piruz mişəvəd", "az": "qalib gəlir"},
        {"fa": "شکست می‌خورد", "reading": "şekəst mixorəd", "az": "məğlub olur"},
        {"fa": "دعوا می‌کند", "reading": "dəva mikonəd", "az": "dava edir"},
        {"fa": "برنامه‌ی هفتگی", "reading": "bərnameye həftegi", "az": "Həftəlik proqram"},
        {"fa": "اخبار", "reading": "əxbar", "az": "Xəbərlər"},
        {"fa": "سریال", "reading": "seryal", "az": "Serial"},
        {"fa": "گوش می‌دهد", "reading": "guş midəhəd", "az": "qulaq asır"},
        {"fa": "یاد می‌گیرد", "reading": "yad migirəd", "az": "öyrənir"},
        {"fa": "تقسیم می‌کند", "reading": "təqsim mikonəd", "az": "bölür"},
        {"fa": "عبادت می‌کند", "reading": "ebadət mikonəd", "az": "ibadət edir"},
        {"fa": "آماده می‌شود", "reading": "amade mişəvəd", "az": "hazırlaşır"},
    ],
    "grammar_notes": [
        {
            "title_az": "«… خوردن» quruluşu — «yemək» felinin geniş mənaları",
            "title_fa": "«....... خوردن»",
            "conjugations": [
                {"pronoun_fa": "شکست خوردن", "form_fa": "məğlub olmaq"},
                {"pronoun_fa": "سرما خوردن", "form_fa": "soyuqlamaq"},
                {"pronoun_fa": "قسم خوردن", "form_fa": "and içmək"},
                {"pronoun_fa": "سُر خوردن", "form_fa": "sürüşmək"},
                {"pronoun_fa": "کتک خوردن", "form_fa": "döyülmək"},
                {"pronoun_fa": "گل خوردن", "form_fa": "qol yemək (futbolda)"},
                {"pronoun_fa": "زمین خوردن", "form_fa": "yıxılmaq"},
            ],
            "examples": [
                {"fa": "«خوردن» feli özündən əvvəlki sözlə birləşərək fərqli mənalar bildirir — yalnız yemək mənasında deyil.", "az": "«خوردن» (yemək) feli müxtəlif isimlərlə birləşərək tamam fərqli mənalar yaradır."},
                {"fa": "نادر پارسال در مسابقه‌ی پینگ‌پونگ از حسن شکست خورد.", "az": "Nadir keçən il stolüstü tennis yarışında Həsəndən məğlub oldu."},
                {"fa": "بچّه‌ها در هوای برفی بازی کردند و سرما خوردند.", "az": "Uşaqlar qarlı havada oynadılar və soyuqladılar."},
                {"fa": "هادی در دادگاه به قاضی گفت: من قسم می‌خورم که از صادق پولی نگرفتم.", "az": "Hadi məhkəmədə hakimə dedi: and içirəm ki, Sadiqdən pul almamışam."},
                {"fa": "دیروز ماشینم روی برف سُر خورد و با یک ماشین دیگر تصادف کرد.", "az": "Dünən maşınım qarın üstündə sürüşdü və başqa maşınla toqquşdu."},
                {"fa": "جمشید دیروز با سه نفر دعوا کرد و از آن‌ها کتک خورد.", "az": "Cəmşid dünən üç nəfərlə dava etdi və onlardan döyüldü."},
                {"fa": "مریم هنگام دویدن زمین خورد و دست و پایش زخمی شد.", "az": "Məryəm qaçarkən yıxıldı və əl-ayağı yaralandı."},
            ],
        },
        {
            "title_az": "Fellər və onlarla işlənən ön qoşmalar (حروف اضافه)",
            "title_fa": "فعل‌ها و حروف اضافه",
            "conjugations": [
                {"pronoun_fa": "از … استفاده کردن", "form_fa": "استاد از ماژیک استفاده می‌کند."},
                {"pronoun_fa": "از … پذیرایی کردن", "form_fa": "ما از مهمان‌ها پذیرایی کردیم."},
                {"pronoun_fa": "از … پرسیدن", "form_fa": "محمّد از راننده آدرس را پرسید."},
                {"pronoun_fa": "از … ترسیدن", "form_fa": "بعضی از مردم از موش می‌ترسند."},
                {"pronoun_fa": "از … تشکّر کردن", "form_fa": "طلبه‌ها از استادهایشان تشکّر می‌کنند."},
                {"pronoun_fa": "از … حرکت کردن", "form_fa": "ابراهیم ساعت دوازده از تهران حرکت می‌کند."},
                {"pronoun_fa": "از … خواستن", "form_fa": "پدرم از من یک لیوان آب خواست."},
                {"pronoun_fa": "از … شکست خوردن", "form_fa": "یاسر از حسین شکست خورد."},
                {"pronoun_fa": "از … گرفتن", "form_fa": "فاطمه و برادرش از پدرشان پول می‌گیرند."},
                {"pronoun_fa": "از … پیاده شدن", "form_fa": "سلمان از اتوبوس پیاده شد."},
                {"pronoun_fa": "از … خریدن", "form_fa": "پدر و مادرم از فروش‌گاه کوثر لباس می‌خرند."},
                {"pronoun_fa": "به … دادن", "form_fa": "من دوچرخه‌ام را به دوستم دادم."},
                {"pronoun_fa": "به … کمک کردن", "form_fa": "دخترم به آن پیرزن کمک کرد."},
                {"pronoun_fa": "به … تلفن زدن", "form_fa": "من هر هفته به مادرم تلفن می‌زنم."},
                {"pronoun_fa": "به … گفتن", "form_fa": "استاد به ما گفت تکلیف‌هایتان را بنویسید."},
                {"pronoun_fa": "به … علاقه داشتن", "form_fa": "ما به درس خواندن علاقه داریم."},
                {"pronoun_fa": "با … ازدواج کردن", "form_fa": "حضرت خدیجه (س) با حضرت محمّد (ص) ازدواج کرد."},
                {"pronoun_fa": "با … بازی کردن", "form_fa": "بچّه‌ها در حیاط با توپ بازی می‌کنند."},
                {"pronoun_fa": "با … صحبت کردن", "form_fa": "زهرا با دوستش سوسن صحبت می‌کند."},
                {"pronoun_fa": "در … زندگی کردن", "form_fa": "پدربزرگ کمیل در تهران زندگی می‌کند."},
                {"pronoun_fa": "در … غرق شدن", "form_fa": "تعدادی از مردم هرسال در دریا غرق می‌شوند."},
                {"pronoun_fa": "در … ماندن", "form_fa": "ما برای درس خواندن پنج سال در ایران می‌مانیم."},
                {"pronoun_fa": "در/روی … نشستن", "form_fa": "مهمان‌ها در اتاق پذیرایی، روی مبل نشستند."},
                {"pronoun_fa": "از/به … رفتن", "form_fa": "دانش‌آموزان ساعت هفت از خانه به مدرسه می‌روند."},
                {"pronoun_fa": "از/به … آمدن", "form_fa": "پدرم ساعت دو از اداره به خانه می‌آید."},
                {"pronoun_fa": "از/به … برگشتن", "form_fa": "همسرم ساعت دوازده از دانش‌گاه به خانه برمی‌گردد."},
                {"pronoun_fa": "از/به … بردن", "form_fa": "حسین هر روز دخترش را از خانه به مدرسه می‌برد."},
            ],
            "examples": [
                {"fa": "Bəzi fars felləri (sadə və mürəkkəb) həmişə müəyyən bir ön qoşma ilə işlənir — hansı qoşma işlənəcəyini əzbərləmək lazımdır.", "az": "Hər fel öz sabit ön qoşması ilə yadda saxlanmalıdır: کمک کردن → به, استفاده کردن → از, صحبت کردن → با və s."},
            ],
        },
    ],
    "exercises": [
        {
            "kind": "fill_blank",
            "instruction_az": "Uyğun ön qoşma ilə tamamlayın: از، به، با، در.",
            "word_bank": ["از", "به", "با", "در"],
            "items": [
                {"fa_with_blank": "دانش‌جوها برای نوشتن ___ خودکار استفاده می‌کنند.", "correct_answer": "از"},
                {"fa_with_blank": "من ___ پدرم پول گرفتم و ___ فقیر دادم.", "correct_answer": "از"},
                {"fa_with_blank": "سجّاد هر هفته فرزندانش را ___ پارک می‌برد و ___ آن‌ها بازی می‌کند.", "correct_answer": "با"},
                {"fa_with_blank": "ما ___ دانش‌جوهای آن دانش‌گاه مسابقه دادیم و ___ آن‌ها شکست خوردیم.", "correct_answer": "از"},
                {"fa_with_blank": "فاطمه ___ پیرزن کمک کرد؛ او هم ___ فاطمه تشکّر کرد.", "correct_answer": "به"},
            ],
        },
        {
            "kind": "fill_blank",
            "instruction_az": "«…خوردن» birləşməsi ilə tamamlayın.",
            "word_bank": ["شکست خورد", "سرما خوردند", "قسم می‌خورم", "سُر خورد", "کتک خورد", "زمین خورد"],
            "items": [
                {"fa_with_blank": "نادر پارسال در مسابقه‌ی پینگ‌پونگ از حسن ___ .", "correct_answer": "شکست خورد"},
                {"fa_with_blank": "بچّه‌ها در هوای برفی بازی کردند و ___ .", "correct_answer": "سرما خوردند"},
                {"fa_with_blank": "هادی در دادگاه گفت: من ___ که از صادق پولی نگرفتم.", "correct_answer": "قسم می‌خورم"},
                {"fa_with_blank": "دیروز ماشینم روی برف ___ و با یک ماشین دیگر تصادف کرد.", "correct_answer": "سُر خورد"},
                {"fa_with_blank": "جمشید دیروز با سه نفر دعوا کرد و از آن‌ها ___ .", "correct_answer": "کتک خورد"},
                {"fa_with_blank": "مریم هنگام دویدن ___ و دست و پایش زخمی شد.", "correct_answer": "زمین خورد"},
            ],
        },
        {
            "kind": "multiple_choice",
            "instruction_az": "«برنامه‌ی هفتگی من» mətninə görə düzgün cavabı seçin.",
            "items": [
                {"question_fa": "مهدی به همراه چه کسانی به ایران آمد؟", "options": ["همسر و فرزندش", "پدر و مادرش", "تنها"], "correct_index": 0},
                {"question_fa": "مهدی برای یادگرفتن زبان فارسی به کجا رفت؟", "options": ["مرکز آموزش زبان فارسی و معارف اسلامی", "دانش‌گاه تهران", "مدرسه‌ی شهید بهشتی"], "correct_index": 0},
                {"question_fa": "مهدی برنامه‌ی هفتگی‌اش را به چند بخش تقسیم کرد؟", "options": ["سه بخش: درس خواندن، عبادت کردن، تفریح و استراحت", "دو بخش", "چهار بخش"], "correct_index": 0},
                {"question_fa": "مهدی هر روز صبح پس از خواندن نماز چه‌کار می‌کند؟", "options": ["حدود یک ربع قرآن می‌خواند", "می‌خوابد", "ورزش می‌کند"], "correct_index": 0},
                {"question_fa": "مهدی چرا ساعت هشت به مدرسه می‌رود؟", "options": ["چون استادشان سرِ ساعت هشت به کلاس می‌آید", "چون کلاس دور است", "چون دوست دارد زود برود"], "correct_index": 0},
                {"question_fa": "مهدی برای بهتر یادگرفتن زبان فارسی چه‌کار می‌کند؟", "options": ["فیلم‌ها و سریال‌های ایرانی تماشا می‌کند", "فقط کتاب می‌خواند", "فقط با دوستانش صحبت می‌کند"], "correct_index": 0},
                {"question_fa": "مهدی و دوستانش عصرهای چه روزهایی ورزش می‌کنند؟", "options": ["شنبه، دوشنبه و چهارشنبه", "یک‌شنبه و سه‌شنبه", "جمعه و شنبه"], "correct_index": 0},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Nümunə kimi cümlə qurun: «پدرم / دو ساعت / کتاب / مطالعه → پدرم هر روز دو ساعت، کتاب مطالعه می‌کند.»",
            "items": [
                {"prompt_fa": "من و جعفر / یک ساعت و نیم / فیلم / تماشا", "answer_fa": "من و جعفر هر روز یک ساعت و نیم، فیلم تماشا می‌کنیم."},
                {"prompt_fa": "دوستم / پنج صبح / از خواب / بیدار", "answer_fa": "دوستم هر روز پنج صبح، از خواب بیدار می‌شود."},
                {"prompt_fa": "احمد و علی / بیست دقیقه / اخبار / گوش", "answer_fa": "احمد و علی هر روز بیست دقیقه، اخبار گوش می‌دهند."},
                {"prompt_fa": "محمّد صادق / هفت ساعت / خانه / استراحت", "answer_fa": "محمّد صادق هر روز هفت ساعت، خانه استراحت می‌کند."},
                {"prompt_fa": "پزشک مدرسه / از ساعت یک تا سه / بیماران / معاینه", "answer_fa": "پزشک مدرسه هر روز از ساعت یک تا سه، بیماران را معاینه می‌کند."},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Cümləni uyğun ön qoşma ilə tamamlayın: «آیا زهرا فردا تیراندازی، پیروز می‌شود؟»",
            "items": [
                {"prompt_fa": "مهدی / پارسال / کشتی / قهرمان شدن", "answer_fa": "آیا مهدی پارسال کشتی، قهرمان شد؟"},
                {"prompt_fa": "ما / هفته‌ی قبل / والیبال / شکست", "answer_fa": "آیا ما هفته‌ی قبل والیبال، شکست خوردیم؟"},
                {"prompt_fa": "محسن / امسال / دوچرخه سواری / پیروز", "answer_fa": "آیا محسن امسال دوچرخه سواری، پیروز شد؟"},
            ],
        },
    ],
    "sentence_practice": {
        "listen_items": [],
        "answer_items": [],
    },
    "reading_text": {
        "title_fa": "برنامه‌ی هفتگی من",
        "title_az": "Mənim həftəlik proqramım",
        "paragraphs_fa": [
            "من مهدی هستم. دو ماه و نیم قبل به همراه همسر و فرزندم برای درس‌خواندن به ایران آمدم. پس از آمدن به ایران برای یادگرفتن زبان فارسی به «مرکزآموزش زبان فارسی و معارف اسلامی» رفتم. ابتدا برنامه‌ی درسی آن مرکز را مطالعه کردم. سپس با کمک همسر و دوستانم یک برنامه‌ی هفتگی نوشتم و شبانه‌روزم را به سه بخش درس خواندن، عبادت کردن، تفریح و استراحت تقسیم کردم.",
            "من هر روز پس از خواندن نماز صبح، حدود یک ربع قرآن می‌خوانم. ساعت هفت صبح با خانواده‌ام صبحانه می‌خورم و ساعت هفت و نیم با آن‌ها خداحافظی می‌کنم و به مدرسه می‌روم. حدود ساعت هشت به مدرسه می‌رسم و زود به کلاس می‌روم؛ چون استاد ما سرِ ساعت هشت به کلاس می‌آید.",
            "پس از تعطیل شدن کلاس‌ها هنگام ظهر به خانه برمی‌گردم. معمولاً اوّل اذان به خانه می‌رسم. سپس پس از خواندن نماز ظهر و عصر با همسر و فرزندم ناهار می‌خورم. سپس یک ربع اخبار فارسی گوش می‌دهم و نیم‌ساعت می‌خوابم؛ تا ساعت دو و نیم از خواب بیدار شوم. تا ساعت سه و نیم درس‌هایم را می‌خوانم و بعد برای رفتن به کلاس‌های بعدازظهر آماده می‌شوم.",
            "من شب‌ها مقداری مطالعه می‌کنم و حدود یک ساعت هم برای بهتر یاد گرفتن زبان فارسی، فیلم‌ها و سریال‌های ایرانی را تماشا می‌کنم. سپس شش ساعت می‌خوابم.",
            "در مدرسه‌ی ما یک سالن ورزشی هست که در آن وسایل گوناگون ورزشی وجود دارد. من و بعضی از دوستانم، عصرِ روزهای شنبه، دوشنبه و چهارشنبه یک ساعت در این سالن ورزش می‌کنیم.",
        ],
        "footnotes": [
            {"fa": "برنامه‌ی هفتگی", "az": "həftəlik proqram"},
            {"fa": "تقسیم می‌کند", "az": "bölür"},
            {"fa": "آماده می‌شود", "az": "hazırlaşır"},
        ],
        "full_translation_az": (
            "Mən Mehdiyəm. İki yarım ay əvvəl həyat yoldaşım və övladımla birlikdə oxumaq üçün İrana gəldim. "
            "İrana gəldikdən sonra fars dilini öyrənmək üçün «Fars dili və İslam maarifi tədris mərkəzi»nə "
            "getdim. Əvvəlcə o mərkəzin dərs proqramını araşdırdım. Sonra həyat yoldaşımın və dostlarımın "
            "köməyi ilə həftəlik bir proqram yazdım və sutkamı dərs oxumaq, ibadət etmək, əylənmək və istirahət "
            "etmək olmaqla üç hissəyə böldüm.\n\n"
            "Mən hər gün səhər namazını qıldıqdan sonra təxminən on beş dəqiqə Quran oxuyuram. Səhər saat "
            "yeddidə ailəmlə səhər yeməyi yeyirəm və saat yeddi yarımda onlarla sağollaşıb məktəbə gedirəm. "
            "Təxminən saat səkkizdə məktəbə çatıram və tez sinfə gedirəm; çünki müəllimimiz dəqiq saat "
            "səkkizdə sinfə gəlir.\n\n"
            "Dərslər bitdikdən sonra günorta evə qayıdıram. Adətən ilk azanda evə çatıram. Sonra günorta və "
            "əsr namazlarını qıldıqdan sonra həyat yoldaşım və övladımla nahar yeyirəm. Sonra on beş dəqiqə "
            "fars dilində xəbərlərə qulaq asıram və yarım saat yatıram; saat iki yarımda oyanıram. Saat üç "
            "yarıma qədər dərslərimi oxuyuram və sonra günortadan sonrakı dərslərə getmək üçün hazırlaşıram.\n\n"
            "Mən gecələr bir qədər mütaliə edirəm və fars dilini daha yaxşı öyrənmək üçün təxminən bir saat "
            "İran filmlərinə və seriallarına baxıram. Sonra altı saat yatıram.\n\n"
            "Məktəbimizdə müxtəlif idman avadanlıqları olan bir idman zalı var. Mən və dostlarımdan bəzisi "
            "şənbə, bazar ertəsi və çərşənbə günləri günortadan sonra bir saat bu zalda idman edirik."
        ),
    },
}
