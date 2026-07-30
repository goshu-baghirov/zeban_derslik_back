# Dərs 8 — وسایل شخصی (Şəxsi əşyalar)
# Mənbə: کتاب دوم, səh. 99-110

LESSON = {
    "number": 8,
    "title_fa": "وسایل شخصی",
    "title_az": "Şəxsi əşyalar",
    "available": True,
    "vocabulary": [
        {"fa": "تلفن همراه", "reading": "telefone həmrah", "az": "Mobil telefon"},
        {"fa": "کیفِ پول", "reading": "kife pul", "az": "Pul kisəsi"},
        {"fa": "چمدان", "reading": "çəmedan", "az": "Çamadan"},
        {"fa": "سشوار", "reading": "seşvar", "az": "Fen"},
        {"fa": "بُرُس", "reading": "boros", "az": "Saç fırçası"},
        {"fa": "آینه", "reading": "aine", "az": "Güzgü"},
        {"fa": "خمیردندان", "reading": "xəmirdəndan", "az": "Diş pastası"},
        {"fa": "شامپو", "reading": "şampu", "az": "Şampun"},
        {"fa": "حوله", "reading": "houle", "az": "Dəsmal (məhrəba)"},
        {"fa": "خودتراش", "reading": "xodtəraş", "az": "Ülgüc"},
        {"fa": "ناخن‌گیر", "reading": "naxonqir", "az": "Dırnaqtutan"},
        {"fa": "دستمال کاغذی", "reading": "dəstmale kağəzi", "az": "Kağız salfet"},
        {"fa": "عطر", "reading": "ətr", "az": "Ətir"},
        {"fa": "مروارید", "reading": "morvarid", "az": "Mirvari"},
        {"fa": "انگشتر", "reading": "əngoştər", "az": "Üzük"},
        {"fa": "النگو", "reading": "ələngu", "az": "Qolbaq"},
        {"fa": "گردن‌بند", "reading": "gərdənbənd", "az": "Boyunbağı"},
        {"fa": "گوشواره", "reading": "quşvare", "az": "Sırğa"},
        {"fa": "لوازم آرایش", "reading": "ləvazeme arayeş", "az": "Kosmetika"},
        {"fa": "کِرِم", "reading": "kerem", "az": "Krem"},
        {"fa": "عروسک", "reading": "ərusək", "az": "Kukla (gəlincik)"},
        {"fa": "می‌دهد", "reading": "midəhəd", "az": "verir"},
        {"fa": "می‌گیرد", "reading": "migirəd", "az": "götürür, alır"},
        {"fa": "می‌آورد", "reading": "miavərəd", "az": "gətirir"},
        {"fa": "می‌برد", "reading": "mibərəd", "az": "aparır"},
        {"fa": "برمی‌دارد", "reading": "bərmidarəd", "az": "götürür (yerdən/üstündən)"},
        {"fa": "اکنون (الآن)", "reading": "əknun (əlan)", "az": "indi"},
        {"fa": "رشته", "reading": "reşte", "az": "İxtisas, sahə"},
        {"fa": "هتل", "reading": "hotel", "az": "Otel"},
        {"fa": "گران‌قیمت", "reading": "qəranqeymət", "az": "Bahalı"},
        {"fa": "ارزان‌قیمت", "reading": "ərzanqeymət", "az": "Ucuz"},
        {"fa": "هم‌سن", "reading": "həmsen", "az": "Yaşıd, eyni yaşda"},
        {"fa": "بعد", "reading": "bəd", "az": "sonra"},
        {"fa": "زیارت", "reading": "ziyarət", "az": "Ziyarət"},
        {"fa": "ثروتمند", "reading": "servətmənd", "az": "Varlı"},
    ],
    "grammar_notes": [
        {
            "title_az": "«دارای ... است» quruluşu (malikdir)",
            "title_fa": "دارای ........ است.",
            "explanation_az": (
                "«دارای ... است» «دارد» ilə eyni mənanı verən rəsmi (kitab) üslubudur.\n"
                "Quruluş: mübtəda + دارای + sahib olunan şey + است.\n"
                "این خانه چهار اتاق دارد. = این خانه دارای چهار اتاق است."
            ),
            "conjugations": [
                {"pronoun_fa": "این خانه یک آشپزخانه و چهار اتاق دارد.", "form_fa": "این خانه دارای یک آشپزخانه و چهار اتاق است."},
            ],
            "examples": [
                {"fa": "این کلاس دارای یک تابلو، یک میز و یازده صندلی است.", "reading_az": "İn kelas daraye yek təblo, yek miz va yazdəh səndəli əst.", "az": "Bu sinifdə bir lövhə, bir masa və on bir stul var."},
                {"fa": "انسان دارای دو چشم، دو گوش، دو دست، دو پا و... است.", "reading_az": "İnsan daraye do çeşm, do guş, do dəst, do pa va ... əst.", "az": "İnsanın iki gözü, iki qulağı, iki əli, iki ayağı və s. var."},
                {"fa": "این باغ دارای درخت‌های سیب، توت، هلو، لیمو و... است.", "reading_az": "İn bağ daraye dərəxthaye sib, tut, holu, limu va ... əst.", "az": "Bu bağda alma, tut, şaftalı, limon və s. ağacları var."},
                {"fa": "آن مرد، ثروتمند است. او دارای پنج فروش‌گاه و مزرعه‌های زیادی است.", "reading_az": "An mərd, servətmənd əst. U daraye pənc foruşgah va məzrəehaye ziyadi əst.", "az": "O kişi varlıdır. Onun beş mağazası və çoxlu tarlası var."},
            ],
            "drills": [
                {
                    "title_fa": "جمله‌ها را با واژه‌ی داخل کمانک تغییر دهید",
                    "instruction_az": '"دارای" ↔ "دارد" çevirin',
                    "items": [
                        {"prompt_fa": "این گردن‌بند دارای هجده مروارید است. (دارد)", "answer_fa": "این گردن‌بند هجده مروارید دارد.", "reading_az": "İn gərdənbənd hejdəh morvarid darəd.", "az": "Bu boyunbağının on səkkiz mirvarisi var."},
                        {"prompt_fa": "عمویم سه فرزند پسر و دو فرزند دختر دارد. (دارای)", "answer_fa": "عمویم دارای سه فرزند پسر و دو فرزند دختر است.", "reading_az": "Əmuyəm daraye se fərzəde pesər va do fərzəde doxtər əst.", "az": "Əmimin üç oğlu və iki qızı var."},
                        {"prompt_fa": "کشور ما دارای کوه‌های بلند و جنگل‌های زیبا است. (دارد)", "answer_fa": "کشور ما کوه‌های بلند و جنگل‌های زیبا دارد.", "reading_az": "Kəşvəre ma kuhhaye bolənd va cəngəlhaye ziba darəd.", "az": "Bizim ölkəmizin uca dağları və gözəl meşələri var."},
                        {"prompt_fa": "دانش‌گاه امام خمینی دارای یک استخر بزرگ است. (دارد)", "answer_fa": "دانش‌گاه امام خمینی یک استخر بزرگ دارد.", "reading_az": "Daneşgahe Emam Xomeyni yek estəxre bozorg darəd.", "az": "İmam Xomeyni Universitetinin böyük bir hovuzu var."},
                    ],
                },
            ],
        },
        {
            "title_az": "Sual sözü «کیست؟» (kimdir?)",
            "title_fa": "واژه‌ی پرسشی «کیست؟»",
            "explanation_az": (
                "«کیست؟» şəxs haqqında soruşur: این خانم کیست؟ — Bu xanım kimdir?\n"
                "Əşya üçün isə «چیست؟» işlənir: این چیست؟\n"
                "«کیست» = «کی است»in qısa formasıdır; cavabda ad, qohumluq və ya peşə deyilə bilər."
            ),
            "conjugations": [
                {"pronoun_fa": "این چیست؟", "form_fa": "این گردن‌بند است. (əşya üçün)"},
                {"pronoun_fa": "این خانم کیست؟", "form_fa": "این خانم، زینب است. (şəxs üçün)"},
            ],
            "examples": [
                {"fa": "این خانم کیست؟ این خانم، زینب است. این خانم، خواهرم است. این خانم، کارمندِ دانش‌گاه است.", "reading_az": "İn xanom kist? İn xanom, Zeynəb əst. İn xanom, xahərəm əst. İn xanom, karmənde daneşgah əst.", "az": "Bu xanım kimdir? Bu xanım Zeynəbdir. Bu xanım bacımdır. Bu xanım universitet işçisidir."},
                {"fa": "این آقا کیست؟ این آقا برادرم حسین است. این آقا مهندسِ رایانه است.", "reading_az": "İn ağa kist? İn ağa bəradərəm Hoseyn əst. İn ağa mohəndese rayane əst.", "az": "Bu kişi kimdir? Bu kişi qardaşım Hüseyndir. Bu kişi kompüter mühəndisidir."},
                {"fa": "آن خانم کیست؟ او خانمِ رضوی است. آن خانم، همسرِ برادرم است. ایشان معلّمِ دخترم است.", "reading_az": "An xanom kist? U xanome Rəzəvi əst. An xanom, həmsəre bəradərəm əst. İşan moəlleme doxtərəm əst.", "az": "O xanım kimdir? O, xanım Rəzəvidir. O xanım qardaşımın həyat yoldaşıdır. O, qızımın müəllimidir."},
                {"fa": "آن مرد کیست؟ او دکتر محمدی است. ایشان پدربزرگِ دوستم است. آن مرد، رئیس بیمارستان است.", "reading_az": "An mərd kist? U doktore Mohəmmədi əst. İşan pedərbozorge dustəm əst. An mərd, rəise bimarestan əst.", "az": "O kişi kimdir? O, doktor Məhəmmədidir. O, dostumun babasıdır. O kişi xəstəxananın rəisidir."},
            ],
            "drills": [
                {
                    "title_fa": "مانند مثال بپرسید و پاسخ دهید",
                    "instruction_az": '"کیست؟" ilə soruşun və cavab verin: "آن آقا کیست؟ آن آقا دوستم جواد است. او فروشنده‌ی پوشاک است."',
                    "items": [
                        {"prompt_fa": "این خانم کیست؟ (خانم حسینی / معلّم)", "answer_fa": "این خانم، خانم حسینی است. ایشان معلّم است.", "reading_az": "İn xanom, xanome Hoseyni əst. İşan moəllem əst.", "az": "Bu xanım, xanım Hüseynidir. O, müəllimdir."},
                        {"prompt_fa": "آن آقا کیست؟ (برادرم صادق / تعمیرکار یخچال)", "answer_fa": "آن آقا برادرم صادق است. او تعمیرکار یخچال است.", "reading_az": "An ağa bəradərəm Sadeq əst. U təmirkare yəxçal əst.", "az": "O kişi qardaşım Sadiqdir. O, soyuducu təmirçisidir."},
                        {"prompt_fa": "این دختر کیست؟ (نوه‌ام زهرا / دانش‌آموز)", "answer_fa": "این دختر، نوه‌ام زهرا است. او دانش‌آموز است.", "reading_az": "İn doxtər, nəveəm Zəhra əst. U daneşamuz əst.", "az": "Bu qız, nəvəm Zəhradır. O, şagirddir."},
                        {"prompt_fa": "آن مرد کیست؟ (شوهر سارا / پلیس)", "answer_fa": "آن مرد، شوهر سارا است. او پلیس است.", "reading_az": "An mərd, şohəre Sara əst. U polis əst.", "az": "O kişi, Saranın əridir. O, polisdir."},
                        {"prompt_fa": "آن آقا کیست؟ (پدرِ همسرم / کشاورز)", "answer_fa": "آن آقا پدرِ همسرم است. او کشاورز است.", "reading_az": "An ağa pedəre həmsərəm əst. U keşavərz əst.", "az": "O kişi, həyat yoldaşımın atasıdır. O, əkinçidir."},
                        {"prompt_fa": "آن خانم کیست؟ (همسر سعید / خبرنگار)", "answer_fa": "آن خانم، همسر سعید است. او خبرنگار است.", "reading_az": "An xanom, həmsəre Səid əst. U xəbərneqar əst.", "az": "O xanım, Səidin həyat yoldaşıdır. O, jurnalistdir."},
                    ],
                },
            ],
        },
        {
            "title_az": "Sual sözləri «چه چیزی» (nə?) və «چه کسی» (kim?)",
            "title_fa": "واژه‌های پرسشی «چه چیزی» و «چه کسی»",
            "explanation_az": (
                "«چه چیزی (چه)» əşyanı, «چه کسی» isə şəxsi soruşur.\n"
                "Cəm forması: «چه چیزهایی» və «چه کسانی».\n"
                "Sual sözü cümlədə hansı üzvün yerində durursa, cavab da həmin yerdə verilir."
            ),
            "conjugations": [
                {"pronoun_fa": "علی چه چیزی (چه) دارد؟", "form_fa": "علی تلفن همراه دارد."},
                {"pronoun_fa": "چه‌کسی تلفن همراه دارد؟", "form_fa": "علی تلفن همراه دارد."},
                {"pronoun_fa": "سوسن و نرگس چه چیزهایی دارند؟", "form_fa": "آن‌ها عینک و ساعت دارند."},
                {"pronoun_fa": "چه‌کسانی عینک و ساعت دارند؟", "form_fa": "سوسن و نرگس عینک و ساعت دارند."},
            ],
            "examples": [
                {"fa": "این کودک چه چیزی (چه) دارد؟ این کودک عروسک دارد.", "reading_az": "İn kudək çe çizi (çe) darəd? İn kudək ərusək darəd.", "az": "Bu uşağın nəyi var? Bu uşağın kuklası var."},
                {"fa": "چه‌کسی به بیمار کمک می‌کند؟ پرستار به بیمار کمک می‌کند.", "reading_az": "Çekəsi be bimar komək mikonəd? Pərəstar be bimar komək mikonəd.", "az": "Xəstəyə kim kömək edir? Xəstəyə tibb bacısı kömək edir."},
                {"fa": "در کلاس شما چه‌کسانی عینک دارند؟ در کلاس ما زینب، نرگس و ریحانه عینک دارند.", "reading_az": "Dər kelase şoma çekəsani eynək darənd? Dər kelase ma Zeynəb, Nərges va Reyhane eynək darənd.", "az": "Sizin sinifdə kimlərin eynəyi var? Bizim sinifdə Zeynəb, Nərgiz və Reyhanənin eynəyi var."},
                {"fa": "در چمدان شما چه چیزهایی هست؟ در چمدان من لباس، عطر، کرم، مسواک و خمیردندان هست.", "reading_az": "Dər çəmedane şoma çe çizhayi həst? Dər çəmedane mən lebas, ətr, kerem, mesvak va xəmirdəndan həst.", "az": "Sizin çamadanınızda nələr var? Çamadanımda paltar, ətir, krem, diş fırçası və diş pastası var."},
                {"fa": "سلمان از میوه‌فروش چه می‌خرد و کجا می‌برد؟ او پرتقال می‌خرد و به خانه‌ی دوستِ بیمارش می‌برد.", "reading_az": "Səlman əz miveforuş çe mixərəd va koca mibərəd? U porteqal mixərəd va be xane-ye duste bimarəş mibərəd.", "az": "Salman meyvəsatandan nə alır və hara aparır? O, portağal alır və xəstə dostunun evinə aparır."},
            ],
            "drills": [
                {
                    "title_fa": "مانند مثال بپرسید و پاسخ دهید",
                    "instruction_az": '"چه چیزی می‌سازد؟ / چه کسی؟" nümunəsi ilə soruşub cavab verin: "نجّار چه چیزی می‌سازد؟ نجّار در و پنجره می‌سازد."',
                    "items": [
                        {"prompt_fa": "برادرت / نوشتن", "answer_fa": "برادرت چه چیزی می‌نویسد؟ برادرم نامه می‌نویسد.", "reading_az": "Bəradərət çe çizi minevisəd? Bəradərəm name minevisəd.", "az": "Qardaşın nə yazır? Qardaşım məktub yazır."},
                        {"prompt_fa": "میوه‌فروش / فروختن", "answer_fa": "میوه‌فروش چه چیزهایی می‌فروشد؟ میوه‌فروش سیب، پرتقال و انار می‌فروشد.", "reading_az": "Miveforuş çe çizhayi miforuşəd? Miveforuş sib, porteqal va anar miforuşəd.", "az": "Meyvə satan nə satır? Meyvə satan alma, portağal və nar satır."},
                        {"prompt_fa": "استاد شما / درس دادن", "answer_fa": "استاد شما چه درسی می‌دهد؟ استاد ما زبان فارسی درس می‌دهد.", "reading_az": "Ostade şoma çe dərsi midəhəd? Ostade ma zəbane farsi dərs midəhəd.", "az": "Müəlliminiz hansı dərsi deyir? Müəllimimiz fars dili dərsi deyir."},
                        {"prompt_fa": "آشپز / پختن", "answer_fa": "آشپز چه چیزی می‌پزد؟ آشپز غذا می‌پزد.", "reading_az": "Aşpəz çe çizi mipəzəd? Aşpəz qəza mipəzəd.", "az": "Aşpaz nə bişirir? Aşpaz yemək bişirir."},
                        {"prompt_fa": "چه کسی / بیمار / معاینه کردن", "answer_fa": "چه کسی بیمار را معاینه می‌کند؟ پزشک، بیمار را معاینه می‌کند.", "reading_az": "Çekəsi bimar ra moayene mikonəd? Pezeşk, bimar ra moayene mikonəd.", "az": "Xəstəni kim müayinə edir? Xəstəni həkim müayinə edir."},
                        {"prompt_fa": "چه کسانی / کفش / دوختن", "answer_fa": "چه کسانی کفش می‌دوزند؟ کفّاش‌ها کفش می‌دوزند.", "reading_az": "Çekəsani kəfş miduzənd? Kəffaşha kəfş miduzənd.", "az": "Ayaqqabını kimlər tikir? Çəkməçilər ayaqqabı tikir."},
                    ],
                },
            ],
        },
    ],
    "exercises": [
        {
            "kind": "fill_blank",
            "instruction_az": "Uyğun fellə tamamlayın: می‌بریم؛ می‌گیرد؛ می‌گذارد؛ می‌آوریم؛ دارند؛ می‌دهد؛ برمی‌دارد؛ ندارند.",
            "word_bank": ["می‌دهد", "می‌گیرد", "برمی‌دارد", "دارند", "می‌گذارد", "می‌بریم", "می‌آوریم"],
            "items": [
                {
                    "fa_with_blank": "حسین به همسرش زینب گل ___ و زینب از او می‌گیرد.",
                    "correct_answer": "می‌دهد",
                    "reading_az": "midəhəd",
                    "az": "verir",
                    "full_reading_az": "Hoseyn be həmsərəş Zeynəb gol midəhəd va Zeynəb əz u migirəd.",
                    "full_translation_az": "Hüseyn həyat yoldaşı Zeynəbə gül verir, Zeynəb isə ondan alır.",
                },
                {
                    "fa_with_blank": "مریم و سارا گوشواره و النگو ___ ؛ آن‌ها گردن‌بند ندارند.",
                    "correct_answer": "دارند",
                    "reading_az": "darənd",
                    "az": "var",
                    "full_reading_az": "Məryəm va Sara guşvare va ələngu darənd; anha gərdənbənd nədarənd.",
                    "full_translation_az": "Məryəm və Saranın sırğası və qolbağı var; boyunbağıları yoxdur.",
                },
                {
                    "fa_with_blank": "میوه‌فروش، پرتقال‌ها را از جعبه ___ و روی ترازو می‌گذارد.",
                    "correct_answer": "برمی‌دارد",
                    "reading_az": "bərmidarəd",
                    "az": "götürür",
                    "full_reading_az": "Miveforuş, porteqalha ra əz cəbe bərmidarəd va ruye tarazu migozarəd.",
                    "full_translation_az": "Meyvə satan portağalları qutudan götürür və tərəziyə qoyur.",
                },
                {
                    "fa_with_blank": "ما هر روز صبح، کتاب‌هایمان را به کلاس ___ و ظهر به خانه می‌بریم.",
                    "correct_answer": "می‌آوریم",
                    "reading_az": "miavərim",
                    "az": "gətiririk",
                    "full_reading_az": "Ma hər ruz sobh, ketabhayeman ra be kelas miavərim va zohr be xane mibərim.",
                    "full_translation_az": "Biz hər gün səhər kitablarımızı sinfə gətiririk, günorta isə evə aparırıq.",
                },
                {
                    "fa_with_blank": "استاد، ماژیک را از روی میز ___ و واژه‌ها را روی تابلو می‌نویسد.",
                    "correct_answer": "برمی‌دارد",
                    "reading_az": "bərmidarəd",
                    "az": "götürür",
                    "full_reading_az": "Ostad, majik ra əz ruye miz bərmidarəd va vajeha ra ruye təblo minevisəd.",
                    "full_translation_az": "Müəllim markeri masanın üstündən götürür və sözləri lövhəyə yazır.",
                },
                {
                    "fa_with_blank": "حسین از پدرش پول ___ و برای خرید وسایل شخصی به بازار می‌رود.",
                    "correct_answer": "می‌گیرد",
                    "reading_az": "migirəd",
                    "az": "alır",
                    "full_reading_az": "Hoseyn əz pedərəş pul migirəd va bəraye xəride vəsayele şəxsi be bazar mirəvəd.",
                    "full_translation_az": "Hüseyn atasından pul alır və şəxsi əşyalar almaq üçün bazara gedir.",
                },
            ],
        },
        {
            "kind": "fill_blank",
            "instruction_az": "«چه کسی؛ چه چیزی؛ چه چیزهایی؛ چه کسانی» ilə tamamlayın.",
            "word_bank": ["چه کسی", "چه چیزی", "چه چیزهایی", "چه کسانی"],
            "items": [
                {
                    "fa_with_blank": "شما ___ مطالعه می‌کنی؟ من کتاب مطالعه می‌کنم.",
                    "correct_answer": "چه چیزی",
                    "reading_az": "çe çizi",
                    "az": "nəyi",
                    "full_reading_az": "Şoma çe çizi motaleə mikoni? Mən ketab motaleə mikonəm.",
                    "full_translation_az": "Sən nəyi mütaliə edirsən? Mən kitab mütaliə edirəm.",
                },
                {
                    "fa_with_blank": "___ خیابان‌ها را جارو می‌کنند؟ رفتگرها خیابان‌ها را جارو می‌کنند.",
                    "correct_answer": "چه کسانی",
                    "reading_az": "çe kəsani",
                    "az": "kimlər",
                    "full_reading_az": "Çe kəsani xiyabanha ra caru mikonənd? Roftegərha xiyabanha ra caru mikonənd.",
                    "full_translation_az": "Küçələri kimlər süpürür? Zibilyığanlar küçələri süpürür.",
                },
                {
                    "fa_with_blank": "برادرت با ___ به تهران می‌رود؟ برادرم با دوستش به تهران می‌رود.",
                    "correct_answer": "چه کسی",
                    "reading_az": "çe kəsi",
                    "az": "kiminlə",
                    "full_reading_az": "Bəradərət ba çe kəsi be Tehran mirəvəd? Bəradərəm ba dustəş be Tehran mirəvəd.",
                    "full_translation_az": "Qardaşın kiminlə Tehrana gedir? Qardaşım dostu ilə Tehrana gedir.",
                },
                {
                    "fa_with_blank": "در کلاس شما ___ هست؟ در کلاس ما تابلو، میز، صندلی، رایانه و ساعت هست.",
                    "correct_answer": "چه چیزهایی",
                    "reading_az": "çe çizhayi",
                    "az": "hansı şeylər",
                    "full_reading_az": "Dər kelase şoma çe çizhayi həst? Dər kelase ma təblo, miz, səndəli, rayane va saət həst.",
                    "full_translation_az": "Sizin sinfinizdə hansı şeylər var? Bizim sinfimizdə lövhə, masa, stul, komputer və saat var.",
                },
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "«بعد» və «برای» ilə əvəz edin: «احمد دو روز بعد برای دیدن دوستش به تهران می‌رود.»",
            "items": [
                {
                    "prompt_fa": "من و خواهرم / سه روز / دیدنِ ... / کشورمان",
                    "answer_fa": "من و خواهرم سه روز بعد برای دیدن خانواده‌مان به کشورمان می‌رویم.",
                    "reading_az": "Mən va xahərəm se ruz bəd bəraye didəne xanevademan be kəşvəreman mirəvim.",
                    "az": "Mən və bacım üç gün sonra ailəmizi görmək üçün ölkəmizə gedirik.",
                },
                {
                    "prompt_fa": "علی و دوستش / دو ساعت / خریدنِ ... / بازار",
                    "answer_fa": "علی و دوستش دو ساعت بعد برای خریدن وسایل شخصی به بازار می‌روند.",
                    "reading_az": "Əli va dustəş do saət bəd bəraye xəridəne vəsayele şəxsi be bazar mirəvənd.",
                    "az": "Əli və dostu iki saat sonra şəxsi əşyalar almaq üçün bazara gedirlər.",
                },
                {
                    "prompt_fa": "ما / سه ساعت / خوردنِ ... / سالن غذاخوری",
                    "answer_fa": "ما سه ساعت بعد برای خوردن غذا به سالن غذاخوری می‌رویم.",
                    "reading_az": "Ma se saət bəd bəraye xordəne qəza be salone qəzaxori mirəvim.",
                    "az": "Biz üç saat sonra yemək yemək üçün yeməkxanaya gedirik.",
                },
                {
                    "prompt_fa": "خانواده و بستگانم / هفت روز / زیارتِ ... / کشور عراق",
                    "answer_fa": "خانواده و بستگانم هفت روز بعد برای زیارت به کشور عراق می‌روند.",
                    "reading_az": "Xanevade va bəsteganəm həft ruz bəd bəraye ziyarət be kəşvəre Eraq mirəvənd.",
                    "az": "Ailəm və qohumlarım yeddi gün sonra ziyarət üçün İraqa gedirlər.",
                },
            ],
        },
    ],
    "sentence_practice": {
        "listen_exercises": [
            {
                "items": [
                    {
                        "fa": "استاد، ماژیک را از روی میز برمی‌دارد و واژه‌ها را روی تابلو می‌نویسد.",
                        "reading_az": "Ostad, majik ra əz ruye miz bərmidarəd va vajeha ra ruye təblo minevisəd.",
                        "az": "Müəllim markeri masanın üstündən götürür və sözləri lövhəyə yazır.",
                    },
                    {
                        "fa": "حسین از پدرش پول می‌گیرد و برای خرید وسایلِ شخصی به بازار می‌رود.",
                        "reading_az": "Hoseyn əz pedərəş pul migirəd va bəraye xəride vəsayele şəxsi be bazar mirəvəd.",
                        "az": "Hüseyn atasından pul alır və şəxsi əşyalar almaq üçün bazara gedir.",
                    },
                    {
                        "fa": "در حمام صابون، تیغ، حوله، خودتراش، آینه، شانه، سشوار و... وجود دارد.",
                        "reading_az": "Dər həmmam sabun, tiğ, houle, xodtəraş, aine, şane, seşvar va ... vocud darəd.",
                        "az": "Hamamda sabun, dişlə, dəsmal, ülgüc, güzgü, daraq, fen və s. var.",
                    },
                    {
                        "fa": "پدرم میوه می‌خرد و به خانه می‌آورد. مادرم میوه‌ها را می‌شوید و در یخچال می‌گذارد.",
                        "reading_az": "Pedərəm mive mixərəd va be xane miavərəd. Madərəm miveha ra mişuyəd va dər yəxçal migozarəd.",
                        "az": "Atam meyvə alır və evə gətirir. Anam meyvələri yuyur və soyuducuya qoyur.",
                    },
                    {
                        "fa": "من و خواهرم برای مادرمان گل و انگشتر طلا می‌خریم و در «روز مادر» به او می‌دهیم.",
                        "reading_az": "Mən va xahərəm bəraye madəreman gol va əngoştəre təla mixərim va dər ruze madər be u midəhim.",
                        "az": "Mən və bacım anamız üçün gül və qızıl üzük alırıq və Ana günündə ona veririk.",
                    },
                    {
                        "fa": "این خانم از بازار کیف زنانه و لوازم آرایش می‌خرد. او لوازم آرایش را در کیفش می‌گذارد.",
                        "reading_az": "İn xanom əz bazar kife zənane va ləvazeme arayeş mixərəd. U ləvazeme arayeş ra dər kifəş migozarəd.",
                        "az": "Bu xanım bazardan qadın çantası və kosmetika alır. O, kosmetikanı çantasına qoyur.",
                    },
                    {
                        "fa": "آقای محمّدی فرزندش را هر روز صبح با تاکسی به مدرسه می‌برد و ظهر به خانه می‌آورد.",
                        "reading_az": "Ağaye Mohəmmədi fərzəndəş ra hər ruz sobh ba taksi be mædrese mibərəd va zohr be xane miavərəd.",
                        "az": "Cənab Məhəmmədi övladını hər gün səhər taksi ilə məktəbə aparır və günorta evə gətirir.",
                    },
                    {
                        "fa": "مادر لیلا هر روز به او میوه و پسته می‌دهد. لیلا آن‌ها را از مادرش می‌گیرد و به مدرسه می‌برد.",
                        "reading_az": "Madəre Leyla hər ruz be u mive va peste midəhəd. Leyla anha ra əz madərəş migirəd va be mædrese mibərəd.",
                        "az": "Leylanın anası hər gün ona meyvə və püstə verir. Leyla onları anasından alır və məktəbə aparır.",
                    },
                    {
                        "fa": "پدر دوستم، طلافروش است. او در مغازه‌اش طلاهای گوناگون، مانند گوشواره، النگو، گردن‌بند، انگشتر و مروارید‌های زیبا دارد.",
                        "reading_az": "Pedəre dustəm, təlaforuş əst. U dər məğazeəş təlahaye gunagun, manənde guşvare, ələngu, gərdənbənd, əngoştər va morvaridhaye ziba darəd.",
                        "az": "Dostumun atası zərgərdir. Onun mağazasında sırğa, qolbaq, boyunbağı, üzük və gözəl mirvarilər kimi müxtəlif qızıl əşyalar var.",
                    },
                ],
            },
        ],
        "answer_items": [
            {
                "fa": "آیا شما تلفنِ همراهتان را به کلاس می‌آورید؟",
                "reading_az": "Aya şoma telefone həmrahetan ra be kelas miavərid?",
                "az": "Siz mobil telefonunuzu sinfə gətirirsinizmi?",
                "sample_answer_fa": "نه، من تلفن همراهم را به کلاس نمی‌آورم.",
                "sample_answer_reading_az": "Nə, mən telefone həmrahəm ra be kelas nemiavəram.",
                "sample_answer_az": "Xeyr, mən mobil telefonumu sinfə gətirmirəm.",
            },
            {
                "fa": "آیا دوستانتان از برس و شانه‌ی شما استفاده می‌کنند؟",
                "reading_az": "Aya dustanetan əz bores va şane-ye şoma estefade mikonənd?",
                "az": "Dostlarınız sizin fırça və darağınızdan istifadə edirmi?",
                "sample_answer_fa": "بله، دوستانم گاهی از شانه‌ی من استفاده می‌کنند.",
                "sample_answer_reading_az": "Bəle, dustanəm gahi əz şane-ye mən estefade mikonənd.",
                "sample_answer_az": "Bəli, dostlarım bəzən mənim darağımdan istifadə edirlər.",
            },
            {
                "fa": "آیا شما حوله و مسواکتان را به دوستتان می‌دهی؟",
                "reading_az": "Aya şoma houle va mesvaketan ra be dustetan midəhi?",
                "az": "Sən dəsmalını və diş fırçanı dostuna verirsənmi?",
                "sample_answer_fa": "نه، من حوله و مسواکم را به دوستم نمی‌دهم.",
                "sample_answer_reading_az": "Nə, mən houle va mesvakəm ra be dustəm nemidəham.",
                "sample_answer_az": "Xeyr, mən dəsmalımı və diş fırçamı dostuma vermirəm.",
            },
            {
                "fa": "شما برای دوستِ بیمارتان چه می‌برید؟",
                "reading_az": "Şoma bəraye duste bimaretan çe mibərid?",
                "az": "Siz xəstə dostunuz üçün nə aparırsınız?",
                "sample_answer_fa": "من برای دوستِ بیمارم میوه و گل می‌برم.",
                "sample_answer_reading_az": "Mən bəraye duste bimarəm mive va gol mibəram.",
                "sample_answer_az": "Mən xəstə dostum üçün meyvə və gül aparıram.",
            },
            {
                "fa": "تلفن همراه و کیفِ پولتان چه رنگی است؟",
                "reading_az": "Telefone həmrah va kife puletan çe rəngi əst?",
                "az": "Mobil telefonunuz və pul kisəniz nə rəngdədir?",
                "sample_answer_fa": "تلفن همراهم مشکی و کیفِ پولم قهوه‌ای است.",
                "sample_answer_reading_az": "Telefone həmrahəm meşki va kife puləm qəhvei əst.",
                "sample_answer_az": "Mobil telefonum qara, pul kisəm isə qəhvəyidir.",
            },
        ],
    },
    "reading_text": {
        "title_fa": "مریم و دوستانش",
        "title_az": "Məryəm və dostları",
        "paragraphs_fa": [
            "نام این خانم، مریم است. سوسن و نرگس دوستان او هستند. مریم آن‌ها را خیلی دوست دارد. مریم و دوستانش اهل لبنانند.",
            "مریم اکنون در ایران زندگی می‌کند و در شهر قم درس می‌خواند. امّا سوسن و نرگس در کشورشان لبنان زندگی می‌کنند. سوسن برای درس‌خواندن به سوریه می‌رود. او در دانش‌گاه دمشق، رشته‌ی ریاضی می‌خواند و نرگس در شهر بیروت، رشته‌ی پزشکی می‌خواند.",
            "مریم و دوستش سوسن، هم‌سن هستند؛ امّا نرگس یک سال از آن‌ها کوچک‌تر است. او هجده سال دارد. پدر نرگس دارای دو هتلِ بزرگ و سه رستوران است.",
            "آن‌ها یک خانواده‌ی ثروتمند هستند. نرگس گردن‌بند، گوشواره و النگوهای زیادی دارد. او یک ماشین گران‌قیمت هم دارد و هر روز با ماشینش به دانش‌گاه می‌رود.",
            "مریم و دوستانش با اینترنت برای هم نامه می‌نویسند. سوسن و نرگس ده روز بعد برای زیارت امام رضا (ع) و دیدن دوستشان مریم با هواپیما به ایران می‌آیند.",
        ],
        "footnotes": [
            {"fa": "اکنون: الآن", "az": "indi"},
            {"fa": "هتل", "az": "otel"},
            {"fa": "گران‌قیمت / ارزان‌قیمت", "az": "bahalı / ucuz"},
            {"fa": "هم‌سن", "az": "yaşıd"},
            {"fa": "زیارت", "az": "ziyarət"},
        ],
        "full_translation_az": (
            "Bu xanımın adı Məryəmdir. Susən və Nərgiz onun dostlarıdır. Məryəm onları çox sevir. Məryəm və "
            "dostları Livandandırlar.\n\n"
            "Məryəm indi İranda yaşayır və Qum şəhərində oxuyur. Amma Susən və Nərgiz öz ölkələri Livanda "
            "yaşayırlar. Susən oxumaq üçün Suriyaya gedir. O, Dəməşq Universitetində riyaziyyat ixtisasında, "
            "Nərgiz isə Beyrut şəhərində tibb ixtisasında oxuyur.\n\n"
            "Məryəm və dostu Susən yaşıddırlar; amma Nərgiz onlardan bir yaş kiçikdir. Onun on səkkiz yaşı var. "
            "Nərgizin atasının iki böyük oteli və üç restoranı var.\n\n"
            "Onlar varlı bir ailədir. Nərgizin çoxlu boyunbağısı, sırğası və qolbağı var. Onun bahalı bir maşını "
            "da var və hər gün öz maşını ilə universitetə gedir.\n\n"
            "Məryəm və dostları internetlə bir-birinə məktub yazırlar. Susən və Nərgiz on gün sonra İmam Rzanı (ə) "
            "ziyarət etmək və dostları Məryəmi görmək üçün təyyarə ilə İrana gəlirlər."
        ),
        "sentences": [
            {"fa": "نام این خانم، مریم است.", "reading_az": "Name in xanom, Məryəm əst.", "az": "Bu xanımın adı Məryəmdir.", "new_paragraph": True},
            {"fa": "سوسن و نرگس دوستان او هستند.", "reading_az": "Susən va Nərges dustane u həstənd.", "az": "Susən və Nərgiz onun dostlarıdır."},
            {"fa": "مریم آن‌ها را خیلی دوست دارد.", "reading_az": "Məryəm anha ra xeyli dust darəd.", "az": "Məryəm onları çox sevir."},
            {"fa": "مریم و دوستانش اهل لبنانند.", "reading_az": "Məryəm va dustanəş əhle Lobananənd.", "az": "Məryəm və dostları Livandandırlar."},
            {
                "fa": "مریم اکنون در ایران زندگی می‌کند و در شهر قم درس می‌خواند.",
                "reading_az": "Məryəm əknun dər Iran zendegi mikonəd va dər şəhre Qom dərs mixanəd.",
                "az": "Məryəm indi İranda yaşayır və Qum şəhərində oxuyur.",
                "new_paragraph": True,
            },
            {"fa": "امّا سوسن و نرگس در کشورشان لبنان زندگی می‌کنند.", "reading_az": "Əmma Susən va Nərges dər kəşvərşan Lobnan zendegi mikonənd.", "az": "Amma Susən və Nərgiz öz ölkələri Livanda yaşayırlar."},
            {"fa": "سوسن برای درس‌خواندن به سوریه می‌رود.", "reading_az": "Susən bəraye dərs-xandən be Suriye mirəvəd.", "az": "Susən oxumaq üçün Suriyaya gedir."},
            {
                "fa": "او در دانش‌گاه دمشق، رشته‌ی ریاضی می‌خواند و نرگس در شهر بیروت، رشته‌ی پزشکی می‌خواند.",
                "reading_az": "U dər daneşgahe Dəməşq, reşte-ye riyazi mixanəd va Nərges dər şəhre Beyrut, reşte-ye pezeşki mixanəd.",
                "az": "O, Dəməşq Universitetində riyaziyyat ixtisasında, Nərgiz isə Beyrut şəhərində tibb ixtisasında oxuyur.",
            },
            {
                "fa": "مریم و دوستش سوسن، هم‌سن هستند؛ امّا نرگس یک سال از آن‌ها کوچک‌تر است.",
                "reading_az": "Məryəm va dustəş Susən, həmsen həstənd; əmma Nərges yek sal əz anha kuçektər əst.",
                "az": "Məryəm və dostu Susən yaşıddırlar; amma Nərgiz onlardan bir yaş kiçikdir.",
                "new_paragraph": True,
            },
            {"fa": "او هجده سال دارد.", "reading_az": "U hejdəh sal darəd.", "az": "Onun on səkkiz yaşı var."},
            {"fa": "پدر نرگس دارای دو هتلِ بزرگ و سه رستوران است.", "reading_az": "Pedəre Nərges daraye do hotele bozorg va se restoran əst.", "az": "Nərgizin atasının iki böyük oteli və üç restoranı var."},
            {"fa": "آن‌ها یک خانواده‌ی ثروتمند هستند.", "reading_az": "Anha yek xanevade-ye servətmənd həstənd.", "az": "Onlar varlı bir ailədir.", "new_paragraph": True},
            {"fa": "نرگس گردن‌بند، گوشواره و النگوهای زیادی دارد.", "reading_az": "Nərges gərdənbənd, guşvare va ələnguhaye ziyadi darəd.", "az": "Nərgizin çoxlu boyunbağısı, sırğası və qolbağı var."},
            {
                "fa": "او یک ماشین گران‌قیمت هم دارد و هر روز با ماشینش به دانش‌گاه می‌رود.",
                "reading_az": "U yek maşine qəranqeymət həm darəd va hər ruz ba maşinəş be daneşgah mirəvəd.",
                "az": "Onun bahalı bir maşını da var və hər gün öz maşını ilə universitetə gedir.",
            },
            {
                "fa": "مریم و دوستانش با اینترنت برای هم نامه می‌نویسند.",
                "reading_az": "Məryəm va dustanəş ba internet bəraye həm name minevisənd.",
                "az": "Məryəm və dostları internetlə bir-birinə məktub yazırlar.",
                "new_paragraph": True,
            },
            {
                "fa": "سوسن و نرگس ده روز بعد برای زیارت امام رضا (ع) و دیدن دوستشان مریم با هواپیما به ایران می‌آیند.",
                "reading_az": "Susən va Nərges dəh ruz bəd bəraye ziyarəte Emam Reza va didəne dustəşan Məryəm ba həvapeyma be Iran miayənd.",
                "az": "Susən və Nərgiz on gün sonra İmam Rzanı (ə) ziyarət etmək və dostları Məryəmi görmək üçün təyyarə ilə İrana gəlirlər.",
            },
        ],
        "comprehension_questions": [
            {
                "question_fa": "مریم و دوستانش اهل کجا هستند؟",
                "reading_az": "Məryəm va dustanəş əhle koca həstənd?",
                "az": "Məryəm və dostları haralıdır?",
                "sample_answer_fa": "مریم و دوستانش اهل لبنانند.",
                "sample_answer_reading_az": "Məryəm va dustanəş əhle Lobananənd.",
                "sample_answer_az": "Məryəm və dostları Livandandırlar.",
            },
            {
                "question_fa": "مریم و دوستانش کجا درس می‌خوانند؟",
                "reading_az": "Məryəm va dustanəş koca dərs mixanənd?",
                "az": "Məryəm və dostları harada oxuyurlar?",
                "sample_answer_fa": "مریم در قم، سوسن در دمشق و نرگس در بیروت درس می‌خواند.",
                "sample_answer_reading_az": "Məryəm dər Qom, Susən dər Dəməşq va Nərges dər Beyrut dərs mixanəd.",
                "sample_answer_az": "Məryəm Qumda, Susən Dəməşqdə, Nərgiz isə Beyrutda oxuyur.",
            },
            {
                "question_fa": "سوسن با چه کسی هم‌سن است؟",
                "reading_az": "Susən ba çekəsi həmsen əst?",
                "az": "Susən kiminlə yaşıddır?",
                "sample_answer_fa": "سوسن با مریم هم‌سن است.",
                "sample_answer_reading_az": "Susən ba Məryəm həmsen əst.",
                "sample_answer_az": "Susən Məryəmlə yaşıddır.",
            },
            {
                "question_fa": "نرگس چه چیزهایی دارد؟",
                "reading_az": "Nərges çe çizhayi darəd?",
                "az": "Nərgizin nələri var?",
                "sample_answer_fa": "نرگس گردن‌بند، گوشواره، النگو و یک ماشین گران‌قیمت دارد.",
                "sample_answer_reading_az": "Nərges gərdənbənd, guşvare, ələngu va yek maşine qəranqeymət darəd.",
                "sample_answer_az": "Nərgizin boyunbağısı, sırğası, qolbağı və bahalı bir maşını var.",
            },
            {
                "question_fa": "سوسن و نرگس ده روز بعد برای چه به ایران می‌آیند؟",
                "reading_az": "Susən va Nərges dəh ruz bəd bəraye çe be Iran miayənd?",
                "az": "Susən və Nərgiz on gün sonra nə üçün İrana gəlir?",
                "sample_answer_fa": "آن‌ها برای زیارت امام رضا (ع) و دیدن دوستشان مریم به ایران می‌آیند.",
                "sample_answer_reading_az": "Anha bəraye ziyarəte Emam Reza va didəne dustəşan Məryəm be Iran miayənd.",
                "sample_answer_az": "Onlar İmam Rzanı ziyarət etmək və dostları Məryəmi görmək üçün İrana gəlirlər.",
            },
        ],
    },
}
