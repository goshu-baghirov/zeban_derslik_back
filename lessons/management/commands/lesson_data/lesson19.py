# Dərs 19 — پزشکی (Tibb)
# Mənbə: کتاب دوم, səh. 231-240

LESSON = {
    "number": 19,
    "title_fa": "پزشکی",
    "title_az": "Tibb",
    "available": True,
    "vocabulary": [
        {"fa": "سردرد", "reading": "sərdərd", "az": "Baş ağrısı"},
        {"fa": "دل‌درد", "reading": "deldərd", "az": "Qarın ağrısı"},
        {"fa": "دندان‌درد", "reading": "dəndandərd", "az": "Diş ağrısı"},
        {"fa": "تب", "reading": "təb", "az": "Qızdırma"},
        {"fa": "زخم", "reading": "zəxm", "az": "Yara"},
        {"fa": "چسبِ زخم", "reading": "çəsbe zəxm", "az": "Yara plastırı"},
        {"fa": "باند", "reading": "band", "az": "Bint"},
        {"fa": "پنبه", "reading": "pənbe", "az": "Pambıq"},
        {"fa": "بتادین", "reading": "betadin", "az": "Yod məhlulu (betadin)"},
        {"fa": "داروخانه", "reading": "daruxane", "az": "Aptek"},
        {"fa": "کپسول", "reading": "kapsul", "az": "Kapsul"},
        {"fa": "قرص", "reading": "qors", "az": "Həb"},
        {"fa": "شربت", "reading": "şərbət", "az": "Şərbət (dərman)"},
        {"fa": "قطره", "reading": "qətre", "az": "Damcı"},
        {"fa": "سِرُم", "reading": "serom", "az": "Serum (damcı sistemi)"},
        {"fa": "پماد", "reading": "pəmad", "az": "Məlhəm"},
        {"fa": "آزمایش‌گاه", "reading": "azmayeşgah", "az": "Laboratoriya"},
        {"fa": "پزشکِ متخصّص", "reading": "pezeşke motəxəses", "az": "Mütəxəssis həkim"},
        {"fa": "عیادت", "reading": "eyadət", "az": "Xəstə baş çəkmə"},
        {"fa": "بستری", "reading": "bəstəri", "az": "Yatırılmış (xəstəxanaya)"},
        {"fa": "درمان", "reading": "dərman", "az": "Müalicə"},
        {"fa": "بخش", "reading": "bəxş", "az": "Şöbə"},
        {"fa": "تزریقات", "reading": "təzriqat", "az": "İnyeksiyalar"},
        {"fa": "سرما می‌خورد", "reading": "sərma mixorəd", "az": "soyuqlayır"},
        {"fa": "سرفه می‌کند", "reading": "sorfe mikonəd", "az": "öskürür"},
        {"fa": "عطسه می‌کند", "reading": "ətse mikonəd", "az": "asqırır"},
        {"fa": "پانسمان می‌زند", "reading": "pansman mizənəd", "az": "sarğı qoyur"},
        {"fa": "آمپول می‌زند", "reading": "ampul mizənəd", "az": "iynə vurur"},
        {"fa": "جرّاحی می‌کند (عمل می‌کند)", "reading": "cərrahi mikonəd (əməl mikonəd)", "az": "əməliyyat edir"},
        {"fa": "داروساز", "reading": "darusaz", "az": "Əczaçı"},
        {"fa": "صاحب", "reading": "saheb", "az": "Sahib"},
        {"fa": "صندلی چرخ‌دار", "reading": "səndəliye çərxdar", "az": "Əlil arabası"},
        {"fa": "انواع", "reading": "ənva", "az": "Növlər, cürlər"},
        {"fa": "وسایل بهداشتی", "reading": "vəsayele behdaşti", "az": "Gigiyena vasitələri"},
        {"fa": "مطب", "reading": "mətəb", "az": "Həkim kabineti"},
        {"fa": "ویزیت", "reading": "vizit", "az": "Həkim müayinə haqqı"},
        {"fa": "تخفیف می‌دهد", "reading": "təxfif midəhəd", "az": "endirim edir"},
        {"fa": "علاقه دارد", "reading": "əlaqe darəd", "az": "maraq göstərir, sevir"},
    ],
    "grammar_notes": [
        {
            "title_az": "«بفرمایید» sözü — nəzakət ifadəsi",
            "title_fa": "«بفرمایید»",
            "conjugations": [
                {"pronoun_fa": "qonağa yer göstərəndə", "form_fa": "بفرمایید (buyurun)"},
                {"pronoun_fa": "hədiyyə verəndə", "form_fa": "بفرمایید (buyurun, alın)"},
                {"pronoun_fa": "avtobusda yer göstərəndə", "form_fa": "بفرمایید (buyurun oturun)"},
                {"pronoun_fa": "kimisə içəri dəvət edəndə", "form_fa": "بفرمایید (buyurun)"},
            ],
            "examples": [
                {"fa": "«بفرمایید» sözü fars dilində bir çox nəzakət vəziyyətində işlənir: yemək təklif edəndə, hədiyyə verəndə, yer göstərəndə, kimisə otağa dəvət edəndə, taksidə sərnişinə yer göstərəndə, lifdə keçməyə icazə verəndə.", "az": "«بفرمایید» sözünün tərcüməsi kontekstdən asılı olaraq dəyişir: buyurun, alın, keçin, oturun."},
                {"fa": "مهمان‌ها سرِ سفره نشستند و میزبان گفت: بفرمایید.", "az": "Qonaqlar süfrə başına oturdular və ev sahibi dedi: buyurun."},
                {"fa": "منشی گفت: سلام، بفرمایید. — بیمار وارد مطب دکتر شد.", "az": "Katibə dedi: salam, buyurun. — Xəstə həkimin kabinetinə girdi."},
                {"fa": "راننده‌ی تاکسی گفت: بفرمایید. — مسافر گفت: قابلی ندارد.", "az": "Taksi sürücüsü dedi: buyurun (pulu alın). Sərnişin dedi: dəyməz (təvazökarlıq)."},
            ],
        },
        {
            "title_az": "«… زدن» quruluşu — geniş mənalı «vurmaq/etmək» feli",
            "title_fa": "«....... زدن»",
            "conjugations": [
                {"pronoun_fa": "لبخند زدن", "form_fa": "gülümsəmək"},
                {"pronoun_fa": "شانه زدن", "form_fa": "daramaq"},
                {"pronoun_fa": "کِرِم زدن", "form_fa": "krem sürtmək"},
                {"pronoun_fa": "اتو زدن", "form_fa": "ütüləmək"},
                {"pronoun_fa": "در زدن", "form_fa": "qapını döymək"},
                {"pronoun_fa": "زنگ زدن", "form_fa": "zəng vurmaq"},
                {"pronoun_fa": "تلفن زدن", "form_fa": "telefon etmək"},
                {"pronoun_fa": "حرف زدن", "form_fa": "danışmaq"},
                {"pronoun_fa": "دست زدن", "form_fa": "əl vurmaq/toxunmaq"},
                {"pronoun_fa": "به‌هم زدن", "form_fa": "qarışdırmaq"},
                {"pronoun_fa": "رنگ زدن", "form_fa": "rəngləmək"},
                {"pronoun_fa": "آمپول زدن", "form_fa": "iynə vurmaq"},
                {"pronoun_fa": "دور زدن", "form_fa": "dönmək (maşınla)"},
                {"pronoun_fa": "سوت زدن", "form_fa": "fit çalmaq"},
            ],
            "examples": [
                {"fa": "«زدن» feli fərqli isimlərlə birləşərək çoxlu müxtəlif mənalar yaradır — mənanı isimlə birlikdə öyrənmək lazımdır.", "az": "«زدن» (vurmaq) feli özündən əvvəlki isimlə birləşərək tamamilə fərqli mənalar bildirir."},
                {"fa": "پدربزرگ و مادربزرگ هنگام دیدن ما خوش‌حال می‌شوند و لبخند می‌زنند.", "az": "Baba və nənə bizi görəndə şad olur və gülümsəyirlər."},
                {"fa": "قبل از رفتن به خانه‌ی دوستم، به او تلفن زدم؛ سپس به آن‌جا رفتم.", "az": "Dostumun evinə getməzdən əvvəl ona telefon etdim; sonra oraya getdim."},
                {"fa": "وقتی به خانه‌ی حسین رسیدم، زنگ زدم و پدرش در را باز کرد.", "az": "Hüseynin evinə çatanda zəng vurdum və atası qapını açdı."},
                {"fa": "هفته‌ی قبل مریض بودم و سه تا آمپول زدم.", "az": "Keçən həftə xəstə idim və üç dəfə iynə vurdurdum."},
                {"fa": "پلیس گفت: این خیابان، ورود ممنوع است؛ دور بزنید و از آن خیابان بروید.", "az": "Polis dedi: bu küçəyə giriş qadağandır; geri dönün və o küçədən gedin."},
            ],
        },
        {
            "title_az": "Şəmsi tarixin yazılışı və oxunuşu",
            "title_fa": "نوشتن و خواندن «تاریخ»",
            "conjugations": [
                {"pronoun_fa": "۱۳۹۱/۷/۴", "form_fa": "چهارمِ مهر، هزار و سیصد و نود و یک"},
                {"pronoun_fa": "گün + Ay + İl", "form_fa": "روز + مِ/ + ماه + ِ + هزار و ..."},
            ],
            "examples": [
                {"fa": "تاریخ به این شکل خوانده می‌شود: روزِ عدد + ماه + سال. مثلاً ۱۳۹۲/۵/۱۲ = دوازدهِ مردادِ هزار و سیصد و نود و دو.", "az": "Tarix belə oxunur: gün + ay + il, məsələn 12 Mordad 1392."},
                {"fa": "امام خمینی (ره) در چهاردهم خردادِ هزار و سیصد و شصت و هشت از دنیا رفت.", "az": "İmam Xomeyni 1368-ci il Xordad ayının 14-də (1989) vəfat etdi."},
                {"fa": "من در دوازدهم فروردینِ هزار و سیصد و پنجاه و هشت به دنیا آمدم.", "az": "Mən 1358-ci il Fərvərdin ayının 12-də anadan olmuşam."},
                {"fa": "تاریخ تولّد شما چیست؟ تاریخ تولّد من، بیست و دوم بهمنِ هزار و سیصد و پنجاه و هفت است.", "az": "Doğum tarixiniz nədir? Mənim doğum tarixim 1357-ci il Bəhmən ayının 22-sidir."},
            ],
        },
    ],
    "exercises": [
        {
            "kind": "fill_blank",
            "instruction_az": "«… زدن» birləşmələrindən uyğun olanı yazın.",
            "word_bank": ["لبخند می‌زنند", "تلفن زدم", "زنگ زدم", "آمپول زدم", "دور بزنید"],
            "items": [
                {"fa_with_blank": "پدربزرگ و مادربزرگ هنگام دیدن ما خوش‌حال می‌شوند و ___ .", "correct_answer": "لبخند می‌زنند"},
                {"fa_with_blank": "قبل از رفتن به خانه‌ی دوستم، به او ___ ؛ سپس به آن‌جا رفتم.", "correct_answer": "تلفن زدم"},
                {"fa_with_blank": "وقتی به خانه‌ی حسین رسیدم، ___ و پدرش در را باز کرد.", "correct_answer": "زنگ زدم"},
                {"fa_with_blank": "هفته‌ی قبل مریض بودم و سه تا ___ .", "correct_answer": "آمپول زدم"},
                {"fa_with_blank": "پلیس گفت: این خیابان، ورود ممنوع است؛ ___ و از آن خیابان بروید.", "correct_answer": "دور بزنید"},
            ],
        },
        {
            "kind": "fill_blank",
            "instruction_az": "Tarixi düzgün oxuyaraq yazın (nümunə əsasında).",
            "word_bank": ["دوازدهِ", "چهاردهِ", "بیست و دوم", "چهارمِ"],
            "items": [
                {"fa_with_blank": "۱۳۹۱/۷/۴ = ___ مهرِ هزار و سیصد و نود و یک", "correct_answer": "چهارمِ"},
                {"fa_with_blank": "۱۳۹۲/۵/۱۲ = ___ مردادِ هزار و سیصد و نود و دو", "correct_answer": "دوازدهِ"},
                {"fa_with_blank": "۱۳۶۸/۳/۱۴ = ___ خردادِ هزار و سیصد و شصت و هشت", "correct_answer": "چهاردهِ"},
                {"fa_with_blank": "۱۳۵۷/۱۱/۲۲ = ___ بهمنِ هزار و سیصد و پنجاه و هفت", "correct_answer": "بیست و دوم"},
            ],
        },
        {
            "kind": "multiple_choice",
            "instruction_az": "«پرستار مهربان» mətninə görə düzgün cavabı seçin.",
            "items": [
                {"question_fa": "سمیّه چگونه شخصیّتی دارد؟", "options": ["خوش‌اخلاق و مهربان", "بی‌ادب و بداخلاق", "ساکت و خجالتی"], "correct_index": 0},
                {"question_fa": "سمیّه در کدام بخش بیمارستان کار می‌کند؟", "options": ["بخش کودکان بیمارستان امام خمینی", "بخش قلب بیمارستان ابن سینا", "بخش تزریقات"], "correct_index": 0},
                {"question_fa": "سمیّه هنگام پانسمان‌زدن چه‌کار می‌کند؟", "options": ["زخم را می‌شوید، نوازش می‌کند، پماد می‌زند و باند می‌بندد", "فقط پول می‌گیرد", "کودکان را می‌ترساند"], "correct_index": 0},
                {"question_fa": "مادر سمیّه چه‌کاره است؟", "options": ["پزشک داروساز و صاحب داروخانه‌ی بزرگ کوثر", "معلّم مدرسه", "پرستار بیمارستان"], "correct_index": 0},
                {"question_fa": "داروخانه‌ی دکتر کاظمی کجاست؟", "options": ["در خیابان سعدی، کنار بیمارستان امام‌خمینی", "در خیابان انقلاب", "در میدان آزادی"], "correct_index": 0},
                {"question_fa": "داروخانه‌ی کوثر چه ساعاتی باز است؟", "options": ["شبانه‌روزی است", "فقط صبح‌ها باز است", "فقط شب‌ها باز است"], "correct_index": 0},
                {"question_fa": "در داروخانه‌ی کوثر علاوه بر دارو چه چیزهایی می‌فروشند؟", "options": ["وسایل پزشکی و بهداشتی، مانند صندلی چرخ‌دار، پنبه، باند و...", "فقط لباس", "فقط کتاب"], "correct_index": 0},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Nümunə kimi əvəz edin: «من دو روز، دندانم درد می‌کند = من دو روز است دندان‌درد دارم.»",
            "items": [
                {"prompt_fa": "فرزندم / چهار ساعت / سرش", "answer_fa": "فرزندم چهار ساعت است سردرد دارد."},
                {"prompt_fa": "ابراهیم / یک هفته / کمرش", "answer_fa": "ابراهیم یک هفته است کمردرد دارد."},
                {"prompt_fa": "پدربزرگمان / یک ماه / پایش", "answer_fa": "پدربزرگمان یک ماه است پادرد دارد."},
                {"prompt_fa": "ما / یک سال / چشممان", "answer_fa": "ما یک سال است چشم‌درد داریم."},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "«بفرمایید» ilə uyğun cümlə deyin.",
            "items": [
                {"prompt_fa": "میزبان یک لیوان چای به مهمان می‌دهد.", "answer_fa": "بفرمایید."},
                {"prompt_fa": "منشی به بیمار اجازه‌ی ورود به مطب می‌دهد.", "answer_fa": "سلام، بفرمایید."},
                {"prompt_fa": "راننده‌ی تاکسی پول را از مسافر می‌گیرد و به او می‌دهد.", "answer_fa": "بفرمایید."},
                {"prompt_fa": "شما در آسانسور به فرد مسن‌تر جا می‌دهید.", "answer_fa": "بفرمایید."},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Öz doğum tarixini nümunə kimi tam formada deyin: «تاریخ تولّد من، دوازدهِ فروردینِ هزار و سیصد و نود است.»",
            "items": [
                {"prompt_fa": "۱۳۸۵/۱۲/۲۹", "answer_fa": "تاریخ تولّد من، بیست و نهمِ اسفندِ هزار و سیصد و هشتاد و پنج است."},
                {"prompt_fa": "۱۳۶۱/۴/۷", "answer_fa": "تاریخ تولّد من، هفتمِ تیرِ هزار و سیصد و شصت و یک است."},
                {"prompt_fa": "۱۳۸۹/۹/۲۷", "answer_fa": "تاریخ تولّد من، بیست و هفتمِ آذرِ هزار و سیصد و هشتاد و نه است."},
            ],
        },
    ],
    "sentence_practice": {
        "listen_items": [],
        "answer_items": [],
    },
    "reading_text": {
        "title_fa": "پرستار مهربان",
        "title_az": "Mehriban tibb bacısı",
        "paragraphs_fa": [
            "سمیّه، پرستاری خوش‌اخلاق و مهربان است. او در بخش کودکان بیمارستان امام خمینی (ره) کار می‌کند. سمیّه به کودکان بیمار در خوردن داروها کمک می‌کند. هنگام پانسمانِ زخمشان، آن‌ها را با مهربانی زخمشان را می‌شوید و با نوازش می‌کند و سپس پماد می‌زند و به وسیله‌ی باند می‌بندد. او بچّه‌ها را مانند فرزندانش دوست دارد و کودکان هم به او بسیار علاقه دارند.",
            "خانم کاظمی، مادر سمیّه است. او پزشک داروساز و صاحب داروخانه‌ی بزرگ کوثر است. این داروخانه، شبانه‌روزی است. داروخانه‌ی دکتر کاظمی در خیابان سعدی، کنار بیمارستان امام‌خمینی (ره) قرار دارد.",
            "در داروخانه‌ی کوثر انواع داروها، مانندِ قرص، کپسول، سرم، آمپول، شربت و پماد وجود دارد. آن‌جا علاوه بر دارو، وسایل پزشکی و بهداشتی، مانندِ صندلی چرخ‌دار، پنبه، باند، چسب زخم، بتادین، انواع کِرِم و خمیردندان و... می‌فروشند.",
        ],
        "footnotes": [
            {"fa": "بستری", "az": "yatırılmış (xəstəxanaya)"},
            {"fa": "درمان / بخش / تزریقات", "az": "müalicə / şöbə / iynə otağı"},
            {"fa": "علاقه دارد", "az": "maraq göstərir, sevir"},
        ],
        "full_translation_az": (
            "Səmiyyə xoşrəftar və mehriban bir tibb bacısıdır. O, İmam Xomeyni xəstəxanasının uşaq şöbəsində "
            "işləyir. Səmiyyə xəstə uşaqlara dərman qəbul etməkdə kömək edir. Yaralarının sarğısını dəyişərkən "
            "onları mehribanlıqla yuyur, sığallayır, sonra məlhəm sürtür və bintlə sarıyır. O, uşaqları öz "
            "övladları kimi sevir və uşaqlar da onu çox sevirlər.\n\n"
            "Xanım Kazımi Səmiyyənin anasıdır. O, əczaçı-həkimdir və böyük Kovsər aptekinin sahibidir. Bu aptek "
            "sutkalıq (gecə-gündüz açıq) işləyir. Doktor Kazıminin apteki Sədi küçəsində, İmam Xomeyni "
            "xəstəxanasının yanında yerləşir.\n\n"
            "Kovsər aptekində həb, kapsul, serum, iynə, şərbət və məlhəm kimi müxtəlif dərmanlar var. Orada "
            "dərmandan əlavə, əlil arabası, pambıq, bint, yara plastırı, yod məhlulu, müxtəlif kremlər və diş "
            "pastası kimi tibbi və gigiyena vasitələri də satılır."
        ),
    },
}
