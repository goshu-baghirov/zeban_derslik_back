# Dərs 15 — غذا (Yemək)
# Mənbə: کتاب دوم, səh. 183-194

LESSON = {
    "number": 15,
    "title_fa": "غذا",
    "title_az": "Yemək",
    "available": True,
    "vocabulary": [
        {"fa": "صبحانه", "reading": "sobhane", "az": "Səhər yeməyi"},
        {"fa": "پنیر", "reading": "pənir", "az": "Pendir"},
        {"fa": "کره", "reading": "kəre", "az": "Kərə yağı"},
        {"fa": "مربّا", "reading": "morəbba", "az": "Mürəbbə"},
        {"fa": "خامه", "reading": "xame", "az": "Qaymaq"},
        {"fa": "تخم‌مرغ آب‌پز", "reading": "toxme-morğe abpəz", "az": "Bişmiş yumurta"},
        {"fa": "نیمرو", "reading": "nimru", "az": "Qayğanaq"},
        {"fa": "ناهار", "reading": "nahar", "az": "Nahar"},
        {"fa": "چلومرغ", "reading": "çelomorğ", "az": "Toyuqlu plov"},
        {"fa": "چلوکباب", "reading": "çelokəbab", "az": "Kabablı plov"},
        {"fa": "سالاد", "reading": "salad", "az": "Salat"},
        {"fa": "ماست", "reading": "mast", "az": "Qatıq"},
        {"fa": "خورش", "reading": "xoreş", "az": "Xörəşt"},
        {"fa": "شام", "reading": "şam", "az": "Şam yeməyi"},
        {"fa": "سوپ", "reading": "sup", "az": "Şorba"},
        {"fa": "ماکارونی", "reading": "makaroni", "az": "Makaron"},
        {"fa": "کنسرو", "reading": "konsərv", "az": "Konserv"},
        {"fa": "سیب‌زمینی سرخ‌کرده", "reading": "sibzəmini sorxkərde", "az": "Qızardılmış kartof (frit)"},
        {"fa": "روغن", "reading": "rouğən", "az": "Yağ"},
        {"fa": "دوغ", "reading": "duğ", "az": "Ayran"},
        {"fa": "نوشابه", "reading": "nuşabe", "az": "Sərinləşdirici içki (qazlı)"},
        {"fa": "سیر", "reading": "sir", "az": "Sarımsaq / tox"},
        {"fa": "گرسنه", "reading": "gorosne", "az": "Ac"},
        {"fa": "ماهی‌تابه (تابه)", "reading": "mahitabe (tabe)", "az": "Qızartma qabı (tava)"},
        {"fa": "پوست می‌کند", "reading": "pust mikonəd", "az": "qabığını soyur"},
        {"fa": "می‌ریزد", "reading": "mirizəd", "az": "tökür"},
        {"fa": "سرخ می‌کند", "reading": "sorx mikonəd", "az": "qızardır"},
        {"fa": "کباب می‌کند", "reading": "kəbab mikonəd", "az": "kabab bişirir"},
        {"fa": "معمولاً", "reading": "məmulən", "az": "adətən"},
        {"fa": "بیشترِ وقت‌ها", "reading": "biştəre vəqtha", "az": "çox vaxt"},
        {"fa": "خوش‌مزه", "reading": "xoşməze", "az": "Dadlı"},
        {"fa": "مهمان", "reading": "mehman", "az": "Qonaq"},
        {"fa": "نشست", "reading": "neşəst", "az": "oturdu"},
        {"fa": "دعوت کرد", "reading": "dəvət kərd", "az": "dəvət etdi"},
        {"fa": "پهن کرد", "reading": "pəhn kərd", "az": "sərdi (süfrəni)"},
        {"fa": "پذیرایی کرد", "reading": "pəzirayi kərd", "az": "qonaqpərvərlik etdi"},
        {"fa": "تشکّر کرد", "reading": "təşəkkor kərd", "az": "təşəkkür etdi"},
    ],
    "grammar_notes": [
        {
            "title_az": "«Saatın yaxınlaşması»: «... به ...» quruluşu",
            "title_fa": "ساعت با «به»",
            "explanation_az": (
                "Yarım saatı keçəndən sonra vaxtı «neçə dəqiqə qalıb» şəklində də demək olar.\n"
                "Quruluş: qalan dəqiqə + «به» + növbəti saat: بیست دقیقه به سه — «üçə iyirmi dəqiqə qalıb».\n"
                "15 dəqiqə qalanda «یک ربع به ...» deyilir."
            ),
            "conjugations": [
                {"pronoun_fa": "ساعت، دو و چهل دقیقه است.", "form_fa": "= ساعت، بیست دقیقه به سه است."},
                {"pronoun_fa": "ساعت، هشت و چهل و پنج دقیقه است.", "form_fa": "= ساعت، پانزده دقیقه به نه است. = ساعت، یک ربع به نه است."},
            ],
            "examples": [
                {"fa": "ساعت، سه و سی و پنج دقیقه است. = ساعت، بیست و پنج دقیقه به چهار است.", "reading_az": "Saət, se va si-o-pənc dəqiqe əst. = Saət, bist-o-pənc dəqiqe be çəhar əst.", "az": "Saat üç otuz beş dəqiqədir. = Saat dördə iyirmi beş dəqiqə qalıb."},
                {"fa": "ما هشت و چهل دقیقه شام می‌خوریم. = ما بیست دقیقه به نه شام می‌خوریم.", "reading_az": "Ma həşt-o-çehel dəqiqe şam mixorim. = Ma bist dəqiqe be no şam mixorim.", "az": "Biz səkkiz qırx dəqiqədə şam yeyirik. = Doqquza iyirmi dəqiqə qalmış şam yeyirik."},
                {"fa": "قطار، یازده و پنجاه و پنج دقیقه به ایستگاه می‌رسد. = قطار، ده دقیقه به دوازده به ایستگاه می‌رسد.", "reading_az": "Qətar, yazdəh-o-pənca-o-pənc dəqiqe be istqah miresəd. = Qətar, dəh dəqiqe be davazdəh be istqah miresəd.", "az": "Qatar on birdə əlli beş dəqiqədə stansiyaya çatır. = On ikiyə on dəqiqə qalmış stansiyaya çatır."},
                {"fa": "ساعت هفت و بیست دقیقه است. ✓ («ساعت چهل دقیقه به هشت است» نمی‌گوییم) ✗", "reading_az": "Saət həft-o-bist dəqiqe əst.", "az": "Saat yeddi iyirmidir. ✓ («Saat səkkizə qırx dəqiqə qalıb» demək YANLIŞDIR.)"},
                {"fa": "ساعت هفت و سی دقیقه است. ✓ («ساعت سی دقیقه به هشت است» نمی‌گوییم) ✗", "reading_az": "Saət həft-o-si dəqiqe əst.", "az": "Saat yeddi otuzdur. ✓ («Saat səkkizə otuz dəqiqə qalıb» demək YANLIŞDIR.)"},
            ],
        },
        {
            "title_az": "Sual sözü «ساعتِ چند» / «چند ساعت» fərqi",
            "title_fa": "«ساعتِ چند» ؛ «چند ساعت»",
            "explanation_az": (
                "«ساعتِ چند» — hansı vaxtda (saat neçədə); cavab: ساعتِ هشت.\n"
                "«چند ساعت» — nə qədər müddət (neçə saat); cavab: دو ساعت.\n"
                "Fərq yalnız söz sırasındadır, mənası isə tamamilə başqadır."
            ),
            "conjugations": [
                {"pronoun_fa": "ساعتِ چند؟", "form_fa": "ساعت، چند است؟ (saat kimin vaxtı → ساعت هشت است)"},
                {"pronoun_fa": "چند ساعت؟", "form_fa": "چند ساعت درس می‌دهد؟ (neçə saat müddət → دو ساعت)"},
            ],
            "examples": [
                {"fa": "استاد ساعتِ چند به کلاس آمد؟ ایشان، ساعتِ هشت به کلاس آمد.", "reading_az": "Ostad saəte çənd be kelas aməd? İşan, saəte həşt be kelas aməd.", "az": "Müəllim saat neçədə sinfə gəldi? O, saat səkkizdə sinfə gəldi."},
                {"fa": "استاد هر روز، چند ساعت درس می‌دهد؟ او هر روز، دو ساعت درس می‌دهد.", "reading_az": "Ostad hər ruz, çənd saət dərs midəhəd? U hər ruz, do saət dərs midəhəd.", "az": "Müəllim hər gün neçə saat dərs deyir? O, hər gün iki saat dərs deyir."},
                {"fa": "شما ساعتِ چند برای مطالعه به کتاب‌خانه می‌روید؟ من ساعتِ چهار بعدازظهر به کتاب‌خانه می‌روم.", "reading_az": "Şoma saəte çənd bəraye motaleə be ketabxane mirəvid? Mən saəte çəhar bədəzzohr be ketabxane mirəvəm.", "az": "Siz mütaliə üçün saat neçədə kitabxanaya gedirsiniz? Mən günortadan sonra saat dörddə kitabxanaya gedirəm."},
                {"fa": "شما ساعتِ چند صبح بیدار شدید؟ من امروز، ساعتِ پنج و نیم صبح بیدار شدم.", "reading_az": "Şoma saəte çənd sobh bidar şodid? Mən emruz, saəte pənc-o-nim sobh bidar şodəm.", "az": "Siz səhər saat neçədə oyandınız? Mən bu gün səhər beş yarımda oyandım."},
                {"fa": "شما هر روز چند ساعت مطالعه می‌کنی؟ من هر روز سه ساعت مطالعه می‌کنم.", "reading_az": "Şoma hər ruz çənd saət motaleə mikoni? Mən hər ruz se saət motaleə mikonəm.", "az": "Sən hər gün neçə saat mütaliə edirsən? Mən hər gün üç saat mütaliə edirəm."},
                {"fa": "دیشب ساعتِ چند خوابیدید؟ دیشب ساعتِ یک ربع به یازده خوابیدم.", "reading_az": "Dişəb saəte çənd xabidid? Dişəb saəte yek robe be yazdəh xabidəm.", "az": "Dünən gecə saat neçədə yatdınız? Dünən gecə saat on birə on beş dəqiqə qalmış yatdım."},
                {"fa": "دیشب چند ساعت خوابیدی؟ دیشب پنج ساعت و نیم خوابیدم.", "reading_az": "Dişəb çənd saət xabidi? Dişəb pənc saət-o-nim xabidəm.", "az": "Dünən gecə neçə saat yatdın? Dünən gecə beş yarım saat yatdım."},
            ],
        },
        {
            "title_az": "«هم؛ هم … هم» (da/də; həm … həm)",
            "title_fa": "«هم» ؛ «هم ... هم»",
            "explanation_az": (
                "Tək «هم» «da/də» mənasını verir və aid olduğu sözdən SONRA gəlir: پسرم هم عسل می‌خورد.\n"
                "«هم … هم» — «həm … həm də»: هم عسل، هم کره می‌خورد.\n"
                "İnkarda isə «نه … نه» işlənir: نه ماکارونی، نه کنسرو."
            ),
            "conjugations": [
                {"pronoun_fa": "من عسل می‌خورم؛ پسرم حسین هم عسل می‌خورد.", "form_fa": "Mən bal yeyirəm; oğlum Hüseyn də bal yeyir."},
                {"pronoun_fa": "پسرم هم عسل می‌خورد، هم کره می‌خورد.", "form_fa": "Oğlum həm bal, həm kərə yağı yeyir."},
            ],
            "examples": [
                {"fa": "علی عینک دارد؛ همسرش سوسن هم عینک دارد.", "reading_az": "Əli eynək darəd; həmsərəş Susən həm eynək darəd.", "az": "Əlinin eynəyi var; həyat yoldaşı Susənin də eynəyi var."},
                {"fa": "آن‌ها شام سوپ هم می‌خورند، هم سیب‌زمینی سرخ‌کرده می‌خورند.", "reading_az": "Anha şam sup həm mixorənd, həm sibzəminiye sorxkərde mixorənd.", "az": "Onlar şam yeməyində həm şorba, həm də qızardılmış kartof yeyirlər."},
                {"fa": "او نه ماکارونی دوست دارد، نه کنسرو؛ او چلوخورش دوست دارد.", "reading_az": "U nə makaroni dust darəd, nə konsərv; u çeloxoreş dust darəd.", "az": "O, nə makaron, nə də konserv sevmir; o, plov-xörəşt sevir."},
                {"fa": "من نه با اتوبوس مسافرت می‌کنم، نه با قطار؛ من با ماشین شخصی مسافرت می‌کنم.", "reading_az": "Mən nə ba otobus mosaferət mikonəm, nə ba qətar; mən ba maşine şəxsi mosaferət mikonəm.", "az": "Mən nə avtobusla, nə də qatarla səyahət edirəm; mən şəxsi maşınla səyahət edirəm."},
                {"fa": "احمد طلبه است؛ آیا شما هم طلبه هستید؟ بله، من هم طلبه هستم.", "reading_az": "Əhməd tələbe əst; aya şoma həm tələbe hastid? Bəle, mən həm tələbe hastəm.", "az": "Əhməd tələbədir; siz də tələbəsiniz? Bəli, mən də tələbəyəm."},
                {"fa": "آن‌ها دیروز پیراهن خریدند؟ آن‌ها هم پیراهن خریدند، هم شلوار.", "reading_az": "Anha diruz pirahən xəridənd? Anha həm pirahən xəridənd, həm şəlvar.", "az": "Onlar dünən köynək aldılar? Onlar həm köynək, həm də şalvar aldılar."},
                {"fa": "در کلاس ما هم میز هست، هم صندلی.", "reading_az": "Dər kelase ma həm miz həst, həm səndəli.", "az": "Sinfimizdə həm masa, həm də stul var."},
                {"fa": "شما زباله‌ها را در کوچه ریختی یا خیابان؟ نه در کوچه ریختم، نه در خیابان؛ در سطل زباله ریختم.", "reading_az": "Şoma zəbaleha ra dər kuçe rixti ya xiyaban? Nə dər kuçe rixtəm, nə dər xiyaban; dər sətle zəbale rixtəm.", "az": "Siz zibilləri döngəyə tökdünüz, yoxsa küçəyə? Nə döngəyə, nə də küçəyə; zibil qutusuna tökdüm."},
            ],
        },
    ],
    "exercises": [
        {
            "kind": "fill_blank",
            "instruction_az": "«ساعتِ چند» yoxsa «چند ساعت» ilə tamamlayın.",
            "word_bank": ["ساعتِ چند", "چند ساعت"],
            "items": [
                {
                    "fa_with_blank": "شما دیشب ___ خوابیدید؟ من دیشب هفت ساعت خوابیدم.",
                    "correct_answer": "چند ساعت",
                    "reading_az": "çənd saət",
                    "az": "neçə saat",
                    "full_reading_az": "Şoma dişəb çənd saət xabidid? Mən dişəb həft saət xabidəm.",
                    "full_translation_az": "Siz dünən gecə neçə saat yatdınız? Mən dünən gecə yeddi saat yatdım.",
                },
                {
                    "fa_with_blank": "قطار ___ به ایستگاه رسید؟ قطار، ساعتِ دوازده رسید.",
                    "correct_answer": "ساعتِ چند",
                    "reading_az": "saəte çənd",
                    "az": "saat neçədə",
                    "full_reading_az": "Qətar saəte çənd be istqah residə? Qətar, saəte davazdəh residə.",
                    "full_translation_az": "Qatar stansiyaya saat neçədə çatdı? Qatar saat on ikidə çatdı.",
                },
                {
                    "fa_with_blank": "استاد هر روز ___ درس می‌دهد؟ او هر روز دو ساعت درس می‌دهد.",
                    "correct_answer": "چند ساعت",
                    "reading_az": "çənd saət",
                    "az": "neçə saat",
                    "full_reading_az": "Ostad hər ruz çənd saət dərs midəhəd? U hər ruz do saət dərs midəhəd.",
                    "full_translation_az": "Müəllim hər gün neçə saat dərs deyir? O, hər gün iki saat dərs deyir.",
                },
                {
                    "fa_with_blank": "پدرت امروز ___ به خانه آمد؟ او امروز ساعت چهار آمد.",
                    "correct_answer": "ساعتِ چند",
                    "reading_az": "saəte çənd",
                    "az": "saat neçədə",
                    "full_reading_az": "Pedərət emruz saəte çənd be xane aməd? U emruz saəte çəhar aməd.",
                    "full_translation_az": "Atan bu gün evə saat neçədə gəldi? O, bu gün saat dörddə gəldi.",
                },
            ],
        },
        {
            "kind": "fill_blank",
            "instruction_az": "«هم» yoxsa «نه … نه» ilə tamamlayın.",
            "word_bank": ["هم", "نه", "هم … هم"],
            "items": [
                {
                    "fa_with_blank": "علی عینک دارد؛ همسرش سوسن ___ عینک دارد.",
                    "correct_answer": "هم",
                    "reading_az": "həm",
                    "az": "da",
                    "full_reading_az": "Əli eynək darəd; həmsərəş Susən həm eynək darəd.",
                    "full_translation_az": "Əlinin eynəyi var; həyat yoldaşı Susənin də eynəyi var.",
                },
                {
                    "fa_with_blank": "او ___ ماکارونی دوست دارد، ___ کنسرو.",
                    "correct_answer": "نه",
                    "reading_az": "nə",
                    "az": "nə",
                    "full_reading_az": "U nə makaroni dust darəd, nə konsərv.",
                    "full_translation_az": "O, nə makaron, nə də konserv sevmir.",
                },
                {
                    "fa_with_blank": "آن‌ها شام ___ سوپ می‌خورند، ___ سیب‌زمینی سرخ‌کرده.",
                    "correct_answer": "هم … هم",
                    "reading_az": "həm … həm",
                    "az": "həm … həm də",
                    "full_reading_az": "Anha şam həm sup mixorənd, həm sibzəminiye sorxkərde.",
                    "full_translation_az": "Onlar şam yeməyində həm şorba, həm də qızardılmış kartof yeyirlər.",
                },
                {
                    "fa_with_blank": "من ___ با اتوبوس مسافرت می‌کنم، ___ با قطار.",
                    "correct_answer": "نه",
                    "reading_az": "nə",
                    "az": "nə",
                    "full_reading_az": "Mən nə ba otobus mosaferət mikonəm, nə ba qətar.",
                    "full_translation_az": "Mən nə avtobusla, nə də qatarla səyahət edirəm.",
                },
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Saatı «به» ilə deyin: «ساعت، دو و چهل دقیقه است. = ساعت، بیست دقیقه به سه است.»",
            "items": [
                {"prompt_fa": "۸:۴۵", "answer_fa": "ساعت، یک ربع به نه است.", "reading_az": "Saət, yek robe be no əst.", "az": "Saat doqquza bir rübə (on beş dəqiqəyə) qalıb."},
                {"prompt_fa": "۱۱:۵۵", "answer_fa": "ساعت، پنج دقیقه به دوازده است.", "reading_az": "Saət, pənc dəqiqe be davazdəh əst.", "az": "Saat on ikiyə beş dəqiqə qalıb."},
                {"prompt_fa": "۳:۵۰", "answer_fa": "ساعت، ده دقیقه به چهار است.", "reading_az": "Saət, dəh dəqiqe be çəhar əst.", "az": "Saat dördə on dəqiqə qalıb."},
                {"prompt_fa": "۶:۴۰", "answer_fa": "ساعت، بیست دقیقه به هفت است.", "reading_az": "Saət, bist dəqiqe be həft əst.", "az": "Saat yeddiyə iyirmi dəqiqə qalıb."},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Nümunə kimi cümlə qurun: «من / چلوکباب / خوردن / برادرم → من چلوکباب می‌خورم؛ برادرم هم چلوکباب می‌خورد.»",
            "items": [
                {"prompt_fa": "آن‌ها / درس فارسی / خواندن / ما", "answer_fa": "آن‌ها درس فارسی می‌خوانند؛ ما هم درس فارسی می‌خوانیم.", "reading_az": "Anha dərse farsi mixanənd; ma həm dərse farsi mixanim.", "az": "Onlar fars dili dərsi oxuyurlar; biz də fars dili dərsi oxuyuruq."},
                {"prompt_fa": "نرگس / سیب‌زمینی سرخ‌کردن / مادرم", "answer_fa": "نرگس سیب‌زمینی سرخ می‌کند؛ مادرم هم سیب‌زمینی سرخ می‌کند.", "reading_az": "Nərges sibzəmini sorx mikonəd; madərəm həm sibzəmini sorx mikonəd.", "az": "Nərgiz kartof qızardır; anam da kartof qızardır."},
                {"prompt_fa": "زهرا / روغن مایع / استفاده کردن / لیلا", "answer_fa": "زهرا روغن مایع استفاده می‌کند؛ لیلا هم روغن مایع استفاده می‌کند.", "reading_az": "Zəhra rouğəne maye estefade mikonəd; Leyla həm rouğəne maye estefade mikonəd.", "az": "Zəhra maye yağ istifadə edir; Leyla da maye yağ istifadə edir."},
                {"prompt_fa": "من / سیب‌زمینی پوست‌کندن / همسرم", "answer_fa": "من سیب‌زمینی پوست می‌کنم؛ همسرم هم سیب‌زمینی پوست می‌کند.", "reading_az": "Mən sibzəmini pust mikonəm; həmsərəm həm sibzəmini pust mikonəd.", "az": "Mən kartof soyuram; həyat yoldaşım da kartof soyur."},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Nümunə kimi cümlə qurun, hər dəfə göstərilən «هم ... هم» və ya «نه ... نه» qəlibini işlədin: «احمد / دیشب / شام و میوه / خوردن (نه...نه) → احمد دیشب نه شام خورد، نه میوه.»",
            "items": [
                {"prompt_fa": "(نه ... نه) آن‌ها / دیروز / پالتو و کاپشن / پوشیدن", "answer_fa": "آن‌ها دیروز نه پالتو پوشیدند، نه کاپشن.", "reading_az": "Anha diruz nə palto pušidənd, nə kapşən.", "az": "Onlar dünən nə palto, nə də kurtka geyindilər."},
                {"prompt_fa": "(هم ... هم) او / امشب / سیب‌زمینی و پیاز / پوست‌کندن", "answer_fa": "او امشب هم سیب‌زمینی پوست می‌کند، هم پیاز.", "reading_az": "U əmşəb həm sibzəmini pust mikonəd, həm piyaz.", "az": "O bu axşam həm kartofu, həm də soğanı soyur."},
                {"prompt_fa": "(هم ... هم) ما / فردا / مرغ و ماهی / پختن", "answer_fa": "ما فردا هم مرغ می‌پزیم، هم ماهی.", "reading_az": "Ma fərda həm morğ mipəzim, həm mahi.", "az": "Biz sabah həm toyuq, həm də balıq bişiririk."},
                {"prompt_fa": "(نه ... نه) مادرم / دیشب / چلومرغ و چلوکباب / درست‌کردن", "answer_fa": "مادرم دیشب نه چلومرغ درست کرد، نه چلوکباب.", "reading_az": "Madərəm dişəb nə çelomorğ dorost kərd, nə çelokəbab.", "az": "Anam dünən gecə nə toyuqlu plov, nə də kabablı plov hazırladı."},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Vaxtı soruşub cavab verin: «شما امشب چند ساعت شام می‌خورید؟ ما امشب، بیست دقیقه به نه شام می‌خوریم.»",
            "items": [
                {"prompt_fa": "آن‌ها / دیشب / میوه خوردن / یازده و ربع", "answer_fa": "آن‌ها دیشب، ساعتِ چند میوه خوردند؟ آن‌ها دیشب، یازده و ربع میوه خوردند.", "reading_az": "Anha dişəb, saəte çənd mive xordənd? Anha dişəb, yazdəh-o-robe mive xordənd.", "az": "Onlar dünən gecə saat neçədə meyvə yedilər? Onlar dünən gecə on birə on beş dəqiqə işləmiş meyvə yedilər."},
                {"prompt_fa": "شما / امروز / ناهار خوردن / یک و نیم", "answer_fa": "شما امروز، ساعتِ چند ناهار می‌خورید؟ ما امروز، یک و نیم ناهار می‌خوریم.", "reading_az": "Şoma emruz, saəte çənd nahar mixorid? Ma emruz, yek-o-nim nahar mixorim.", "az": "Siz bu gün saat neçədə nahar yeyirsiniz? Biz bu gün saat bir yarımda nahar yeyirik."},
                {"prompt_fa": "شما / دیروز / خانه برگشتن / پنج به هفت", "answer_fa": "شما دیروز، ساعتِ چند به خانه برگشتید؟ ما دیروز، پنج دقیقه به هفت برگشتیم.", "reading_az": "Şoma diruz, saəte çənd be xane bərgəştid? Ma diruz, pənc dəqiqe be həft bərgəştim.", "az": "Siz dünən saat neçədə evə qayıtdınız? Biz dünən saat yeddiyə beş dəqiqə qalmış qayıtdıq."},
                {"prompt_fa": "ریحانه / دیشب / پذیرایی‌کردنِ دوستانش / هشت و ده دقیقه", "answer_fa": "ریحانه دیشب، ساعتِ چند دوستانش را پذیرایی کرد؟ او دیشب، هشت و ده دقیقه دوستانش را پذیرایی کرد.", "reading_az": "Reyhane dişəb, saəte çənd dustanəş ra pəzirayi kərd? U dişəb, həşt-o-dəh dəqiqe dustanəş ra pəzirayi kərd.", "az": "Reyhanə dünən gecə dostlarını saat neçədə qarşıladı? O, dünən gecə saat səkkiz on dəqiqədə dostlarını qarşıladı."},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Nümunə kimi cümlə qurun: «مادرم امروز برای ناهار، چلومرغ درست می‌کند.»",
            "items": [
                {"prompt_fa": "خواهرم / امشب / ماکارونی", "answer_fa": "خواهرم امشب ماکارونی درست می‌کند.", "reading_az": "Xahərəm əmşəb makaroni dorost mikonəd.", "az": "Bacım bu axşam makaron hazırlayır."},
                {"prompt_fa": "مادربزرگم / دیروز / چلوخورش", "answer_fa": "مادربزرگم دیروز چلوخورش درست کرد.", "reading_az": "Madərbozorgəm diruz çeloxoreş dorost kərd.", "az": "Nənəm dünən plov-xörəşt hazırladı."},
                {"prompt_fa": "آن‌ها / فردا / تخم‌مرغ آب‌پز", "answer_fa": "آن‌ها فردا تخم‌مرغ آب‌پز درست می‌کنند.", "reading_az": "Anha fərda toxme-morğe abpəz dorost mikonənd.", "az": "Onlar sabah bişmiş yumurta hazırlayacaqlar."},
                {"prompt_fa": "برادرزاده‌ام فاطمه / دیشب / ماهی", "answer_fa": "برادرزاده‌ام فاطمه دیشب ماهی درست کرد.", "reading_az": "Bəradərzadeəm Fateme dişəb mahi dorost kərd.", "az": "Qardaşımın qızı Fatimə dünən gecə balıq hazırladı."},
                {"prompt_fa": "من / فردا شب / سالاد", "answer_fa": "من فردا شب سالاد درست می‌کنم.", "reading_az": "Mən fərdaşəb salad dorost mikonəm.", "az": "Mən sabah gecə salat hazırlayıram."},
                {"prompt_fa": "دوستم / سه ساعت قبل / نیم‌رو", "answer_fa": "دوستم سه ساعت قبل نیم‌رو درست کرد.", "reading_az": "Dustəm se saət qəbl nimru dorost kərd.", "az": "Dostum üç saat əvvəl qayğanaq hazırladı."},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Uyğun sual qurun (verilən cavaba görə).",
            "items": [
                {"prompt_fa": "ساعت، دوازده دقیقه به هفت است.", "answer_fa": "ساعت چند است؟", "reading_az": "Saət çənd əst?", "az": "Saat neçədir?"},
                {"prompt_fa": "امروز، ساعتِ پنج و نیم صبح بیدار شدم.", "answer_fa": "شما ساعتِ چند صبح بیدار شدید؟", "reading_az": "Şoma saəte çənd sobh bidar şodid?", "az": "Siz səhər saat neçədə oyandınız?"},
                {"prompt_fa": "من و دوستانم هر روز یک ساعت قرآن می‌خوانیم.", "answer_fa": "شما هر روز چند ساعت قرآن می‌خوانید؟", "reading_az": "Şoma hər ruz çənd saət Qoran mixanid?", "az": "Siz hər gün neçə saat Quran oxuyursunuz?"},
                {"prompt_fa": "پدرم امروز ساعت چهار و بیست دقیقه به خانه آمد.", "answer_fa": "پدرتان ساعتِ چند به خانه آمد؟", "reading_az": "Pedəretan saəte çənd be xane aməd?", "az": "Atanız saat neçədə evə gəldi?"},
                {"prompt_fa": "آشپزها هر روز نیم‌ساعت سیب‌زمینی پوست می‌کنند.", "answer_fa": "آشپزها هر روز چند ساعت سیب‌زمینی پوست می‌کنند؟", "reading_az": "Aşpəzha hər ruz çənd saət sibzəmini pust mikonənd?", "az": "Aşpazlar hər gün neçə saat kartof təmizləyirlər?"},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Nümunə kimi cümlə qurun: «من / پدر و مادرم / مسافرت → من بیشتر وقت‌ها با پدر و مادرم به مسافرت می‌روم.»",
            "items": [
                {"prompt_fa": "پدر حسین / هواپیما / سفر", "answer_fa": "پدر حسین بیشتر وقت‌ها با هواپیما سفر می‌کند.", "reading_az": "Pedəre Hoseyn bişttəre vəqtha ba həvapeyma səfər mikonəd.", "az": "Hüseynin atası çox vaxt təyyarə ilə səyahət edir."},
                {"prompt_fa": "کشاورزان / مزرعه / کار", "answer_fa": "کشاورزان بیشتر وقت‌ها در مزرعه کار می‌کنند.", "reading_az": "Keşavərzan bişttəre vəqtha dər məzree kar mikonənd.", "az": "Əkinçilər çox vaxt tarlada işləyirlər."},
                {"prompt_fa": "ما / بعدازظهر / استراحت", "answer_fa": "ما بیشتر وقت‌ها بعدازظهر استراحت می‌کنیم.", "reading_az": "Ma bişttəre vəqtha bədəzzohr esterahət mikonim.", "az": "Biz çox vaxt günortadan sonra istirahət edirik."},
                {"prompt_fa": "در زمستان / برف و باران / باریدن", "answer_fa": "در زمستان بیشتر وقت‌ها برف و باران می‌بارد.", "reading_az": "Dər zemestan bişttəre vəqtha bərf-o-baran mibarəd.", "az": "Qışda çox vaxt qar və yağış yağır."},
            ],
        },
    ],
    "sentence_practice": {
        "listen_exercises": [
            {
                "items": [
                    {"fa": "ما هر شب پس از شام چای و میوه می‌خوریم.", "reading_az": "Ma hər şəb pəs əz şam çay-o-mive mixorim.", "az": "Biz hər gecə şam yeməyindən sonra çay və meyvə yeyirik."},
                    {"fa": "خواهرم زهرا بیمار است؛ مادرم امروز برایش تخم‌مرغ آب‌پز و سوپ می‌پزد.", "reading_az": "Xahərəm Zəhra bimar əst; madərəm emruz bərayəş toxme-morğe abpəz-o-sup mipəzəd.", "az": "Bacım Zəhra xəstədir; anam bu gün onun üçün bişmiş yumurta və şorba bişirir."},
                    {"fa": "من سیب را پوست می‌کنم و می‌خورم؛ امّا برادرم سیب را با پوست می‌خورد.", "reading_az": "Mən sib ra pust mikonəm-o-mixorəm; əmma bəradərəm sib ra ba pust mixorəd.", "az": "Mən almanı soyub yeyirəm; amma qardaşım almanı qabığı ilə yeyir."},
                    {"fa": "بعضی‌از مردم، سیب‌زمینی آب‌پز و بعضی سیب‌زمینی سرخ‌کرده دوست دارند.", "reading_az": "Bəzi əz mərdom, sibzəminiye abpəz-o-bəzi sibzəminiye sorxkərde dust darənd.", "az": "İnsanların bəzisi bişmiş kartof, bəzisi isə qızardılmış kartof sevir."},
                    {"fa": "مادرم گاهی گوشت را در روغن سرخ می‌کند و گاهی روی آتش کباب می‌کند.", "reading_az": "Madərəm gahi guşt ra dər rouğən sorx mikonəd va gahi ruye atəş kəbab mikonəd.", "az": "Anam bəzən əti yağda qızardır, bəzən isə odda kabab bişirir."},
                    {"fa": "من ساعت چهار و نیم بعدازظهر ناهار خوردم؛ الآن سیر هستم و شام نمی‌خورم.", "reading_az": "Mən saəte çəhar-o-nim bədəzzohr nahar xordəm; əl-an sir hastəm va şam nemixorəm.", "az": "Mən günortadan sonra saat dörd yarımda nahar yedim; indi toxam və şam yemirəm."},
                    {"fa": "زینب سیب‌زمینی‌ها را پوست می‌کند؛ در ماهی‌تابه می‌ریزد و در روغن سرخ می‌کند.", "reading_az": "Zeynəb sibzəminiha ra pust mikonəd; dər mahitabe mirizəd va dər rouğən sorx mikonəd.", "az": "Zeynəb kartofları soyur; tavaya töküb yağda qızardır."},
                    {"fa": "مادرم برای پختن غذا، از روغن جامد استفاده نمی‌کند؛ ایشان از روغن مایع استفاده می‌کند.", "reading_az": "Madərəm bəraye poxtəne qəza, əz rouğəne camed estefade nemikonəd; işan əz rouğəne maye estefade mikonəd.", "az": "Anam yemək bişirmək üçün bərk yağdan istifadə etmir; o, maye yağdan istifadə edir."},
                    {"fa": "ما صبحانه، گاهی پنیر و گردو، گاهی کره و مربّا، گاهی عسل و خامه و گاهی نیمرو می‌خوریم.", "reading_az": "Ma sobhane, gahi pənir-o-gərdu, gahi kəre-o-morəbba, gahi əsəl-o-xame va gahi nimru mixorim.", "az": "Biz səhər yeməyində bəzən pendir-qoz, bəzən kərə yağı-mürəbbə, bəzən bal-qaymaq, bəzən də qayğanaq yeyirik."},
                    {"fa": "ایرانی‌ها هنگام خوردن ناهار و شام، علاوه بر آب، بر سرِ سفره، از دوغ یا ماست یا سالاد هم استفاده می‌کنند.", "reading_az": "Iraniha hengame xordəne nahar-o-şam, əlave bər ab, bər səre sofre, əz duğ ya mast ya salad həm estefade mikonənd.", "az": "İranlılar nahar və şam yeyərkən sudan əlavə süfrə başında ayran, qatıq və ya salatdan da istifadə edirlər."},
                ],
            },
        ],
        "answer_items": [
            {"fa": "شما کدام غذاها را دوست دارید؟", "reading_az": "Şoma kodam qəzaha ra dust darid?", "az": "Siz hansı yeməkləri sevirsiniz?"},
            {"fa": "هر روز چند ساعت تکلیف می‌نویسید؟", "reading_az": "Hər ruz çənd saət təklif minevisid?", "az": "Siz hər gün neçə saat tapşırıq yazırsınız?"},
            {"fa": "ساعت چند صبحانه، ناهار و شام می‌خورید؟", "reading_az": "Saəte çənd sobhane, nahar-o-şam mixorid?", "az": "Siz səhər, nahar və şam yeməyini saat neçədə yeyirsiniz?"},
            {"fa": "آیا قبل از غذاخوردن دست‌هایتان را می‌شویید؟", "reading_az": "Aya qəbl əz qəzaxordən dəsthayetan ra mişuyid?", "az": "Yeməkdən əvvəl əllərinizi yuyursunuzmu?"},
        ],
    },
    "reading_text": {
        "title_fa": "سفره‌های ایرانی",
        "title_az": "İran süfrələri",
        "paragraphs_fa": [
            "در هر کشور، مردم غذاهای گوناگون می‌خورند. در ایران هم غذاهای مختلف وجود دارد. مردم ایران، مانند مردم کشورهای دیگر، هر روز غذا سه بار می‌خورند: صبح صبحانه، ظهر ناهار و شب‌ها شام می‌خورند.",
            "صبحانه‌ی ایرانی‌ها معمولاً پنیر و گردو، کره و مربّا، عسل و خامه یا نیمرو با چای و شیر است. ایرانی‌ها بیشتر وقت‌ها ناهار، برنج با خورش‌های گوناگون، مانند قیمه، قورمه‌سبزی و... یا چلومرغ و چلوکباب به علاوه‌ی ماست و سالاد می‌خورند و شام آن‌ها سوپ، آش، ماکارونی، الویه یا آب‌گوشت است. آب‌گوشت یک غذای لذیذ و خوش‌مزه‌ی ایرانی است.",
            "خانواده‌های ایرانی معمولاً شب‌ها زیاد غذا نمی‌خورند و از غذاهای رستوران هم کم استفاده می‌کنند. آن‌ها بیشتر وقت‌ها با هم غذا می‌خورند و تنها غذا خوردن را دوست ندارند.",
            "حمید و همسرش ریحانه، ایرانی هستند. آن‌ها یک دوست لبنانی به نام سیّد علی دارند. او و خانواده‌اش در ایران زندگی می‌کنند. حمید دیروز آن‌ها را برای شام به خانه‌اش دعوت کرد.",
            "ریحانه قبل از آمدن مهمان‌ها شام خوش‌مزه‌ای برای آن‌ها درست کرد. مهمان‌ها ساعت هفت‌ونیم شب آمدند. حمید و همسرش آن‌ها را به اتاق پذیرایی بردند و با چای، شیرینی و میوه از آنان پذیرایی کردند. ریحانه حدود ساعت نهِ شب سفره‌ی شام را پهن کرد و همه با هم سرِ سفره نشستند و شام خوردند.",
            "سیّد علی و همسرش پس از خوردن شام از حمید و خانواده‌اش تشکّر کردند و حدود ساعت ده و نیم به خانه‌شان برگشتند.",
        ],
        "footnotes": [
            {"fa": "معمولاً", "az": "adətən"},
            {"fa": "بیشترِ وقت‌ها", "az": "çox vaxt"},
            {"fa": "خوش‌مزه", "az": "dadlı"},
            {"fa": "پذیرایی کرد / تشکّر کرد", "az": "qonaqpərvərlik etdi / təşəkkür etdi"},
        ],
        "full_translation_az": (
            "Hər ölkədə insanlar müxtəlif yeməklər yeyir. İranda da müxtəlif yeməklər var. İran xalqı, digər "
            "ölkələrin xalqları kimi, hər gün üç dəfə yemək yeyir: səhər — səhər yeməyi, günorta — nahar, "
            "axşamlar isə şam yeməyi.\n\n"
            "İranlıların səhər yeməyi adətən pendir və qoz-fındıq, kərə yağı və mürəbbə, bal və qaymaq və ya "
            "qayğanaq, çay və südlə olur. İranlılar çox vaxt naharda düyünü müxtəlif xörəştlərlə, məsələn qeymə, "
            "qormesəbzi və s. və ya toyuqlu-plov və kabablı-plovu qatıq və salatla yeyirlər, şam yeməkləri isə "
            "şorba, aş, makaron, olivye və ya ət şorbasıdır. Ət şorbası ləzzətli və dadlı bir İran yeməyidir.\n\n"
            "İran ailələri adətən axşamlar çox yemək yemir və restoran yeməklərindən də az istifadə edir. Onlar "
            "çox vaxt birlikdə yemək yeyir və tək yemək yeməyi sevmirlər.\n\n"
            "Həmid və həyat yoldaşı Reyhanə iranlıdır. Onların Seyid Əli adında livanlı bir dostu var. O və "
            "ailəsi İranda yaşayır. Həmid dünən onları şam yeməyinə evinə dəvət etdi.\n\n"
            "Reyhanə qonaqlar gəlməmişdən əvvəl onlar üçün dadlı bir şam hazırladı. Qonaqlar axşam saat yeddi "
            "yarımda gəldilər. Həmid və həyat yoldaşı onları qonaq otağına apardı və çay, şirniyyat və meyvə ilə "
            "qonaqpərvərlik etdilər. Reyhanə axşam təxminən saat doqquzda şam süfrəsini sərdi və hamı birlikdə "
            "süfrə başına oturub şam yeməyini yedi.\n\n"
            "Seyid Əli və həyat yoldaşı şam yeməyindən sonra Həmiddən və ailəsindən təşəkkür etdilər və təxminən "
            "saat on yarımda öz evlərinə qayıtdılar."
        ),
        "sentences": [
            {
                "fa": "در هر کشور، مردم غذاهای گوناگون می‌خورند.",
                "reading_az": "Dər hər kəşvər, mərdom qəzahaye gunagun mixorənd.",
                "az": "Hər ölkədə insanlar müxtəlif yeməklər yeyir.",
                "new_paragraph": True,
            },
            {
                "fa": "در ایران هم غذاهای مختلف وجود دارد.",
                "reading_az": "Dər Iran həm qəzahaye moxtəlef vocud darəd.",
                "az": "İranda da müxtəlif yeməklər var.",
            },
            {
                "fa": "مردم ایران، مانند مردم کشورهای دیگر، هر روز غذا سه بار می‌خورند: صبح صبحانه، ظهر ناهار و شب‌ها شام می‌خورند.",
                "reading_az": "Mərdome Iran, manənde mərdome kəşvərhaye digər, hər ruz qəza se bar mixorənd: sobh sobhane, zohr nahar va şəbha şam mixorənd.",
                "az": "İran xalqı, digər ölkələrin xalqları kimi, hər gün üç dəfə yemək yeyir: səhər — səhər yeməyi, günorta — nahar, axşamlar isə şam yeməyi.",
            },
            {
                "fa": "صبحانه‌ی ایرانی‌ها معمولاً پنیر و گردو، کره و مربّا، عسل و خامه یا نیمرو با چای و شیر است.",
                "reading_az": "Sobhaneye Irəniha məmulən pənir-o-gərdu, kəre-o-morəbba, əsəl-o-xame ya nimru ba çay-o-şir əst.",
                "az": "İranlıların səhər yeməyi adətən pendir və qoz-fındıq, kərə yağı və mürəbbə, bal və qaymaq və ya qayğanaq, çay və südlə olur.",
                "new_paragraph": True,
            },
            {
                "fa": "ایرانی‌ها بیشتر وقت‌ها ناهار، برنج با خورش‌های گوناگون، مانند قیمه، قورمه‌سبزی و... یا چلومرغ و چلوکباب به علاوه‌ی ماست و سالاد می‌خورند و شام آن‌ها سوپ، آش، ماکارونی، الویه یا آب‌گوشت است.",
                "reading_az": "Irəniha bişttəre vəqtha nahar, berənc ba xoreşhaye gunagun, manənde qeyme, qormesəbzi va..., ya çelomorğ-o-çelokəbab be əlaveye mast-o-salad mixorənd va şame anha sup, aş, makaroni, olviye ya abguşt əst.",
                "az": "İranlılar çox vaxt naharda düyünü müxtəlif xörəştlərlə, məsələn qeymə, qormesəbzi və s. və ya toyuqlu-plov və kabablı-plovu qatıq və salatla yeyirlər, şam yeməkləri isə şorba, aş, makaron, olivye və ya ət şorbasıdır.",
            },
            {
                "fa": "آب‌گوشت یک غذای لذیذ و خوش‌مزه‌ی ایرانی است.",
                "reading_az": "Abguşt yek qəzaye ləzizo xoşmazeye Irani əst.",
                "az": "Ət şorbası ləzzətli və dadlı bir İran yeməyidir.",
            },
            {
                "fa": "خانواده‌های ایرانی معمولاً شب‌ها زیاد غذا نمی‌خورند و از غذاهای رستوران هم کم استفاده می‌کنند.",
                "reading_az": "Xanevadehaye Irani məmulən şəbha ziyad qəza nemixorənd va əz qəzahaye restoran həm kəm estefade mikonənd.",
                "az": "İran ailələri adətən axşamlar çox yemək yemir və restoran yeməklərindən də az istifadə edir.",
                "new_paragraph": True,
            },
            {
                "fa": "آن‌ها بیشتر وقت‌ها با هم غذا می‌خورند و تنها غذا خوردن را دوست ندارند.",
                "reading_az": "Anha bişttəre vəqtha ba həm qəza mixorənd va tənha qəza xordən ra dust nədarənd.",
                "az": "Onlar çox vaxt birlikdə yemək yeyir və tək yemək yeməyi sevmirlər.",
            },
            {
                "fa": "حمید و همسرش ریحانه، ایرانی هستند.",
                "reading_az": "Həmid va həmsərəş Reyhane, Irani həstənd.",
                "az": "Həmid və həyat yoldaşı Reyhanə iranlıdır.",
                "new_paragraph": True,
            },
            {
                "fa": "آن‌ها یک دوست لبنانی به نام سیّد علی دارند.",
                "reading_az": "Anha yek duste Lobnani be name Seyyed Əli darənd.",
                "az": "Onların Seyid Əli adında livanlı bir dostu var.",
            },
            {
                "fa": "او و خانواده‌اش در ایران زندگی می‌کنند.",
                "reading_az": "U va xanevadeəş dər Iran zendegi mikonənd.",
                "az": "O və ailəsi İranda yaşayır.",
            },
            {
                "fa": "حمید دیروز آن‌ها را برای شام به خانه‌اش دعوت کرد.",
                "reading_az": "Həmid diruz anha ra bəraye şam be xaneəş dəvət kərd.",
                "az": "Həmid dünən onları şam yeməyinə evinə dəvət etdi.",
            },
            {
                "fa": "ریحانه قبل از آمدن مهمان‌ها شام خوش‌مزه‌ای برای آن‌ها درست کرد.",
                "reading_az": "Reyhane qəbl əz aməddəne mehmanha şame xoşmazei bəraye anha dorost kərd.",
                "az": "Reyhanə qonaqlar gəlməmişdən əvvəl onlar üçün dadlı bir şam hazırladı.",
                "new_paragraph": True,
            },
            {
                "fa": "مهمان‌ها ساعت هفت‌ونیم شب آمدند.",
                "reading_az": "Mehmanha saəte həft-o-nim şəb amədənd.",
                "az": "Qonaqlar axşam saat yeddi yarımda gəldilər.",
            },
            {
                "fa": "حمید و همسرش آن‌ها را به اتاق پذیرایی بردند و با چای، شیرینی و میوه از آنان پذیرایی کردند.",
                "reading_az": "Həmid va həmsərəş anha ra be otaqe pəzirayi bordənd va ba çay, şirini va mive əz anan pəzirayi kərdənd.",
                "az": "Həmid və həyat yoldaşı onları qonaq otağına apardı və çay, şirniyyat və meyvə ilə qonaqpərvərlik etdilər.",
            },
            {
                "fa": "ریحانه حدود ساعت نهِ شب سفره‌ی شام را پهن کرد و همه با هم سرِ سفره نشستند و شام خوردند.",
                "reading_az": "Reyhane hodude saəte nohe şəb sofreye şam ra pəhn kərd va həme ba həm səre sofre neşəstənd va şam xordənd.",
                "az": "Reyhanə axşam təxminən saat doqquzda şam süfrəsini sərdi və hamı birlikdə süfrə başına oturub şam yeməyini yedi.",
            },
            {
                "fa": "سیّد علی و همسرش پس از خوردن شام از حمید و خانواده‌اش تشکّر کردند و حدود ساعت ده و نیم به خانه‌شان برگشتند.",
                "reading_az": "Seyyed Əli va həmsərəş pəs əz xordəne şam əz Həmid va xanevadeəş təşəkkor kərdənd va hodude saəte dəh-o-nim be xanehayeşan bərgəştənd.",
                "az": "Seyid Əli və həyat yoldaşı şam yeməyindən sonra Həmiddən və ailəsindən təşəkkür etdilər və təxminən saat on yarımda öz evlərinə qayıtdılar.",
                "new_paragraph": True,
            },
        ],
        "comprehension_questions": [
            {
                "question_fa": "ناهار و شام ایرانی‌ها معمولاً چیست؟",
                "reading_az": "Nahar-o-şame Iraniha məmulən çist?",
                "az": "İranlıların naharı və şamı adətən nədir?",
                "sample_answer_fa": "ناهار ایرانی‌ها معمولاً برنج با خورش‌های گوناگون یا چلومرغ و چلوکباب است و شام آن‌ها سوپ، آش، ماکارونی، الویه یا آب‌گوشت است.",
                "sample_answer_reading_az": "Nahare Iraniha məmulən berənc ba xoreşhaye gunagun ya çelomorğ-o-çelokəbab əst va şame anha sup, aş, makaroni, olviye ya abguşt əst.",
                "sample_answer_az": "İranlıların naharı adətən müxtəlif xörəştlərlə düyü, ya da toyuqlu-plov və kabablı-plovdur; şamları isə şorba, aş, makaron, olivye və ya ət şorbasıdır.",
            },
            {
                "question_fa": "حمید چه کسانی را برای شام به خانه‌اش دعوت کرد؟",
                "reading_az": "Həmid çe kəsani ra bəraye şam be xaneəş dəvət kərd?",
                "az": "Həmid şam yeməyinə evinə kimləri dəvət etdi?",
                "sample_answer_fa": "حمید دوستش سیّد علی و خانواده‌اش را برای شام دعوت کرد.",
                "sample_answer_reading_az": "Həmid dustəş Seyyed Əli va xanevadeəş ra bəraye şam dəvət kərd.",
                "sample_answer_az": "Həmid dostu Seyid Əlini və ailəsini şam yeməyinə dəvət etdi.",
            },
            {
                "question_fa": "مهمان‌ها چه وقت آمدند و ریحانه ساعت چند سفره را پهن کرد؟",
                "reading_az": "Mehmanha çe vəqt amədənd va Reyhane saəte çənd sofre ra pəhn kərd?",
                "az": "Qonaqlar nə vaxt gəldilər və Reyhanə süfrəni saat neçədə sərdi?",
                "sample_answer_fa": "مهمان‌ها ساعت هفت‌ونیم شب آمدند و ریحانه حدود ساعت نهِ شب سفره را پهن کرد.",
                "sample_answer_reading_az": "Mehmanha saəte həft-o-nim şəb amədənd va Reyhane hodude saəte nohe şəb sofre ra pəhn kərd.",
                "sample_answer_az": "Qonaqlar axşam saat yeddi yarımda gəldilər və Reyhanə təxminən saat doqquzda süfrəni sərdi.",
            },
            {
                "question_fa": "حمید و همسرش قبل از شام با چه چیزهایی از مهمانان پذیرایی کردند؟",
                "reading_az": "Həmid va həmsərəş qəbl əz şam ba çe çizhayi əz mehmanan pəzirayi kərdənd?",
                "az": "Həmid və həyat yoldaşı şamdan əvvəl qonaqları nə ilə qarşıladılar?",
                "sample_answer_fa": "آن‌ها با چای، شیرینی و میوه از مهمانان پذیرایی کردند.",
                "sample_answer_reading_az": "Anha ba çay, şirini va mive əz mehmanan pəzirayi kərdənd.",
                "sample_answer_az": "Onlar qonaqları çay, şirniyyat və meyvə ilə qarşıladılar.",
            },
            {
                "question_fa": "سیّد علی و همسرش پس از خوردن شام چه کردند؟",
                "reading_az": "Seyyed Əli va həmsərəş pəs əz xordəne şam çe kərdənd?",
                "az": "Seyid Əli və həyat yoldaşı şam yeməyindən sonra nə etdilər?",
                "sample_answer_fa": "آن‌ها از حمید و خانواده‌اش تشکّر کردند و حدود ساعت ده و نیم به خانه‌شان برگشتند.",
                "sample_answer_reading_az": "Anha əz Həmid va xanevadeəş təşəkkor kərdənd va hodude saəte dəh-o-nim be xanehayeşan bərgəştənd.",
                "sample_answer_az": "Onlar Həmiddən və ailəsindən təşəkkür etdilər və təxminən saat on yarımda evlərinə qayıtdılar.",
            },
        ],
    },
}
