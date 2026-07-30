# Dərs 4 — شغل ۱ (Peşə 1)
# Mənbə: کتاب دوم, səh. 51-62

LESSON = {
    "number": 4,
    "title_fa": "شغل ۱",
    "title_az": "Peşə 1",
    "available": True,
    "vocabulary": [
        {"fa": "رئیس‌جمهور", "reading": "rəis-comhur", "az": "Prezident"},
        {"fa": "پادشاه (شاه)", "reading": "padeşah (şah)", "az": "Padşah (şah)"},
        {"fa": "مدیر", "reading": "modir", "az": "Müdir (direktor)"},
        {"fa": "معلّم (استاد)", "reading": "moəllem (ostad)", "az": "Müəllim"},
        {"fa": "دانش‌آموز", "reading": "daneşamuz", "az": "Şagird"},
        {"fa": "دانش‌جو", "reading": "daneşcu", "az": "Tələbə"},
        {"fa": "پزشک (دکتر)", "reading": "pezeşk (doktor)", "az": "Həkim"},
        {"fa": "دندان‌پزشک", "reading": "dəndanpezeşk", "az": "Diş həkimi"},
        {"fa": "مهندس", "reading": "mohəndes", "az": "Mühəndis"},
        {"fa": "بنّا", "reading": "bənna", "az": "Bənna"},
        {"fa": "کارگر", "reading": "kargər", "az": "Fəhlə"},
        {"fa": "آهنگر", "reading": "ahəngər", "az": "Dəmirçi"},
        {"fa": "نجّار", "reading": "nəccar", "az": "Dülgər"},
        {"fa": "خیّاط", "reading": "xəyyat", "az": "Dərzi"},
        {"fa": "کفّاش", "reading": "kəffaş", "az": "Çəkməçi"},
        {"fa": "عکّاس", "reading": "əkkas", "az": "Fotoqraf"},
        {"fa": "قصّاب", "reading": "qəssab", "az": "Qəssab"},
        {"fa": "معاینه می‌کند", "reading": "moayene mikonəd", "az": "müayinə edir"},
        {"fa": "نسخه می‌نویسد", "reading": "nosxe minevisəd", "az": "resept yazır"},
        {"fa": "می‌سازد", "reading": "misazəd", "az": "tikir, düzəldir"},
        {"fa": "می‌دوزد", "reading": "miduzəd", "az": "tikir (paltar)"},
        {"fa": "درس می‌دهد", "reading": "dərs midəhəd", "az": "dərs deyir"},
        {"fa": "کار می‌کند", "reading": "kar mikonəd", "az": "işləyir"},
        {"fa": "گاهی", "reading": "gahi", "az": "bəzən"},
        {"fa": "امّا", "reading": "əmma", "az": "amma"},
        {"fa": "بیمارستان", "reading": "bimarestan", "az": "Xəstəxana"},
        {"fa": "بازنشسته", "reading": "bazneşəste", "az": "Təqaüdçü"},
        {"fa": "خانه‌دار", "reading": "xanedar", "az": "Evdar"},
        {"fa": "شصت", "reading": "şəst", "az": "Altmış"},
        {"fa": "شش‌نفره", "reading": "şeş-nəfəre", "az": "Altı nəfərlik"},
        # Materiallar (dərslikdəki şəkilli sıra: آهن / چوب / پلاستیک / شیشه)
        {"fa": "آهن", "reading": "ahən", "az": "Dəmir"},
        {"fa": "چوب", "reading": "çub", "az": "Ağac (taxta)"},
        {"fa": "پلاستیک", "reading": "plastik", "az": "Plastik"},
        {"fa": "شیشه", "reading": "şişe", "az": "Şüşə"},
        # Təşdidli sözlər (dərslikdəki şəkilli sıra: مکّه / بچّه / مجلّه / سکّه / ارّه / غوّاص)
        {"fa": "مکّه", "reading": "Məkkə", "az": "Məkkə"},
        {"fa": "بچّه", "reading": "bəççe", "az": "Uşaq"},
        {"fa": "مجلّه", "reading": "məcəlle", "az": "Jurnal"},
        {"fa": "سکّه", "reading": "sekke", "az": "Sikkə"},
        {"fa": "ارّه", "reading": "ərre", "az": "Mişar"},
        {"fa": "غوّاص", "reading": "ğəvvas", "az": "Dalğıc"},
    ],
    "grammar_notes": [
        {
            "title_az": "Mənfi fel «نیستم؛ نیستی؛ ...» (deyiləm, deyilsən...)",
            "title_fa": "فعل منفی «نیستم؛ نیستی؛ ...»",
            "explanation_az": (
                "«هستن» köməkçi feldir və təsdiq cümlələrində işlənir: هستم / هستی / هست (است) / هستیم / هستید / هستند.\n"
                "İnkar «ن» ilə düzəlir və forma qısalır: هستم → نیستم (deyiləm), هست → نیست (deyil).\n"
                "3-cü şəxs təkdə «هست» və «است» eyni mənadadır; «است» yazıda daha çox işlənir.\n"
                "Fel cümlənin sonunda gəlir və mübtədanın şəxsi ilə uzlaşır."
            ),
            # Dərslikdəki diaqramın eynisi: hər şəxs üçün نجّار + təsdiq forması
            # və آهنگر + inkar forması bir sətirdə qarşı-qarşıya verilir.
            "conjugations": [
                {"pronoun_fa": "من", "form_fa": "نجّار هستم؛ آهنگر نیستم"},
                {"pronoun_fa": "تو", "form_fa": "نجّار هستی؛ آهنگر نیستی"},
                {"pronoun_fa": "او", "form_fa": "نجّار هست (است)؛ آهنگر نیست"},
                {"pronoun_fa": "ما", "form_fa": "نجّار هستیم؛ آهنگر نیستیم"},
                {"pronoun_fa": "شما", "form_fa": "نجّار هستید؛ آهنگر نیستید"},
                {"pronoun_fa": "آن‌ها", "form_fa": "نجّار هستند؛ آهنگر نیستند"},
            ],
            "note_fa": (
                "۱. «هستن» فعلِ ربطی است و در جملهٔ مثبت به‌کار می‌رود: "
                "هستم / هستی / هست (است) / هستیم / هستید / هستند.\n"
                "۲. برای منفی‌کردن، «ن» به اوّلِ فعل اضافه می‌شود و شکلِ آن کوتاه می‌گردد: "
                "هستم ← نیستم، هستی ← نیستی، هست ← نیست، هستیم ← نیستیم، "
                "هستید ← نیستید، هستند ← نیستند.\n"
                "۳. در سوّم‌شخصِ مفرد دو شکل داریم: «هست» و «است». معنایشان یکی است، "
                "امّا «است» بیشتر در نوشتار به‌کار می‌رود: او نجّار است. = او نجّار هست.\n"
                "۴. فعل همیشه در آخرِ جمله می‌آید و با شخصِ جمله هماهنگ است: "
                "من نجّار هستم. ✓ / من نجّار هستید. ✗"
            ),
            "note_reading_az": (
                "1. «Həstən» fe'le rəbti əst va dər comleye mosbət be-kar mirəvəd: "
                "hastəm / hasti / həst (əst) / hastim / hastid / həstənd.\n"
                "2. Bəraye mənfi-kərdən, «n» be əvvəle fe'l ezafe mişəvəd va şekle an kutah migərdəd: "
                "hastəm ← nistəm, hasti ← nisti, həst ← nist, hastim ← nistim, "
                "hastid ← nistid, həstənd ← nistənd.\n"
                "3. Dər sevvom-şəxse mofrəd do şekl darim: «həst» va «əst». Mə'nayeşan yeki əst, "
                "əmma «əst» biştər dər neveştar be-kar mirəvəd: U nəccar əst. = U nəccar həst.\n"
                "4. Fe'l həmişe dər axəre comle miayəd va ba şəxse comle həmahəng əst: "
                "Mən nəccar hastəm. / Mən nəccar hastid."
            ),
            "note_az": (
                "1. «هستن» köməkçi feldir və təsdiq cümlələrində işlənir: "
                "هستم (-am/-əm) / هستی (-san/-sən) / هست، است (-dır) / هستیم (-ıq/-ik) / "
                "هستید (-sınız/-siniz) / هستند (-dırlar).\n"
                "2. İnkar üçün felin əvvəlinə «ن» əlavə olunur və forma qısalır: "
                "هستم → نیستم (deyiləm), هستی → نیستی (deyilsən), هست → نیست (deyil), "
                "هستیم → نیستیم (deyilik), هستید → نیستید (deyilsiniz), هستند → نیستند (deyillər).\n"
                "3. Üçüncü şəxs təkdə iki forma var: «هست» və «است». Mənaları eynidir, "
                "lakin «است» daha çox yazıda işlənir: او نجّار است. = او نجّار هست. (O, dülgərdir.)\n"
                "4. Fel həmişə cümlənin sonunda gəlir və şəxsə uyğun olmalıdır: "
                "من نجّار هستم. ✓ / من نجّار هستید. ✗"
            ),
            # Dərslikdəki «لطفاً بخوانید» siyahısı (5 cümlə) — نجّار/آهنگر baza
            # cümləsi burada təkrarlanmır, o, yuxarıdakı birləşmə cədvəlindədir.
            "examples": [
                {"fa": "من خیّاط هستم؛ کفّاش نیستم.", "reading_az": "Mən xəyyat hastəm; kəffaş nistəm.", "az": "Mən dərziyəm; çəkməçi deyiləm."},
                {"fa": "شما (تو) معلّم هستی؛ مدیر نیستی.", "reading_az": "Şoma (to) moəllem hasti; modir nisti.", "az": "Sən müəllimsən; müdir deyilsən."},
                {"fa": "او پلیس نیست؛ قاضی است.", "reading_az": "U polis nist; qazi əst.", "az": "O, polis deyil; hakimdir."},
                {"fa": "ما دانش‌آموز نیستیم؛ دانش‌جو هستیم.", "reading_az": "Ma daneşamuz nistim; daneşcu hastim.", "az": "Biz şagird deyilik; tələbəyik."},
                {"fa": "آن‌ها کارگر هستند؛ بنّا نیستند.", "reading_az": "Anha kargər həstənd; bənna nistənd.", "az": "Onlar fəhlədirlər; bənna deyillər."},
            ],
        },
        {
            "title_az": "Sual sözü «چه‌کاره» (nəçidir?)",
            "title_fa": "واژه‌ی پرسشی «چه‌کاره»",
            "explanation_az": (
                "«چه‌کاره است؟» peşəni soruşur — «nəçidir?»; «شغل او چیست؟» ilə eyni mənadadır.\n"
                "Fel şəxsə görə dəyişir: چه‌کاره هستی؟ / چه‌کاره هستید؟ / چه‌کاره هستند؟\n"
                "Görülən işi soruşmaq üçün isə «چه‌کار می‌کند؟» işlənir — cavabda peşənin adı yox, hərəkəti deyilir."
            ),
            "conjugations": [],
            # Dərslikdəki «لطفاً بخوانید» siyahısı (10 bənd). 7-10-cu bəndlərdə
            # bir neçə sual-cavab cütü var — dərslikdəki kimi hər bənd bir
            # nümunə kartı olaraq saxlanılır, sətirlər \n ilə ayrılır.
            "examples": [
                {
                    "fa": "فاطمه خانم چه‌کاره است؟ ایشان پزشک هستند.",
                    "reading_az": "Fateme xanom çekare əst? İşan pezeşk həstənd.",
                    "az": "Fatimə xanım nəçidir? O (hörmətlə), həkimdir.",
                },
                {
                    "fa": "شغل آن آقا چیست؟ او خیّاط است.",
                    "reading_az": "Şoğle an ağa çist? U xəyyat əst.",
                    "az": "O kişinin peşəsi nədir? O, dərzidir.",
                },
                {
                    "fa": "شغل شما چیست؟ من عکّاس هستم.",
                    "reading_az": "Şoğle şoma çist? Mən əkkas hastəm.",
                    "az": "Sizin peşəniz nədir? Mən fotoqrafam.",
                },
                {
                    "fa": "علی و زینب چه‌کاره هستند؟ آن‌ها دانش‌جو هستند.",
                    "reading_az": "Əli va Zeynəb çekare həstənd? Anha daneşcu həstənd.",
                    "az": "Əli və Zeynəb nəçidirlər? Onlar tələbədirlər.",
                },
                {
                    "fa": "من مدیر هستم. شما چه‌کاره هستی؟ من معلّم هستم.",
                    "reading_az": "Mən modir hastəm. Şoma çekare həsti? Mən moəllem hastəm.",
                    "az": "Mən müdirəm. Sən nəçisən? Mən müəlliməm.",
                },
                {
                    "fa": "برادر من مهندس است. برادر شما چه‌کاره است؟ برادر من قاضی است.",
                    "reading_az": "Bəradəre mən mohəndes əst. Bəradəre şoma çekare əst? Bəradəre mən qazi əst.",
                    "az": "Mənim qardaşım mühəndisdir. Sizin qardaşınız nəçidir? Mənim qardaşım hakimdir.",
                },
                {
                    "fa": "شما چه‌کاره هستید؟ ما خیّاط هستیم.\nخیّاط‌ها چه‌کار می‌کنند؟ خیّاط‌ها لباس می‌دوزند.",
                    "reading_az": "Şoma çekare hastid? Ma xəyyat hastim.\nXəyyatha çekar mikonənd? Xəyyatha lebas miduzənd.",
                    "az": "Siz nəçisiniz? Biz dərziyik.\nDərzilər nə edirlər? Dərzilər paltar tikirlər.",
                },
                {
                    "fa": "سعید چه‌کاره است؟ سعید بنّا است.\nبنّا چه‌کار می‌کند؟ بنّا خانه می‌سازد.",
                    "reading_az": "Səid çekare əst? Səid bənna əst.\nBənna çekar mikonəd? Bənna xane misazəd.",
                    "az": "Səid nəçidir? Səid bənnadır.\nBənna nə edir? Bənna ev tikir.",
                },
                {
                    "fa": (
                        "خدیجه چه‌کاره است؟ خدیجه، معلّم است.\n"
                        "معلّم‌ها چه‌کار می‌کنند؟ آن‌ها به دانش‌آموزان درس می‌دهند.\n"
                        "خدیجه خانم الآن چه‌کار می‌کند؟ ایشان الآن خانه را تمیز می‌کند."
                    ),
                    "reading_az": (
                        "Xədice çekare əst? Xədice, moəllem əst.\n"
                        "Moəllemha çekar mikonənd? Anha be daneşamuzan dərs midəhənd.\n"
                        "Xədice xanom əl-an çekar mikonəd? İşan əl-an xane ra təmiz mikonəd."
                    ),
                    "az": (
                        "Xədicə nəçidir? Xədicə müəllimdir.\n"
                        "Müəllimlər nə edirlər? Onlar şagirdlərə dərs deyirlər.\n"
                        "Xədicə xanım indi nə edir? O, indi evi təmizləyir."
                    ),
                },
                {
                    "fa": (
                        "محمّد چه‌کاره است؟ محمّد دندان‌پزشک است.\n"
                        "دندان‌پزشک چه‌کار می‌کند؟ دندان بیماران را معاینه می‌کند.\n"
                        "آقا محمّد الآن چه‌کار می‌کند؟ او الآن چای می‌خورد."
                    ),
                    "reading_az": (
                        "Mohəmməd çekare əst? Mohəmməd dəndanpezeşk əst.\n"
                        "Dəndanpezeşk çekar mikonəd? Dəndane bimaran ra moayene mikonəd.\n"
                        "Ağa Mohəmməd əl-an çekar mikonəd? U əl-an çay mixorəd."
                    ),
                    "az": (
                        "Məhəmməd nəçidir? Məhəmməd diş həkimidir.\n"
                        "Diş həkimi nə edir? Xəstələrin dişlərini müayinə edir.\n"
                        "Ağa Məhəmməd indi nə edir? O, indi çay içir."
                    ),
                },
            ],
            # Qeyd: «مانند مثال بپرسید و پاسخ دهید» çalışması bu mövzudan
            # çıxarılıb — indi lessonun öz «Çalışmalar» siyahısındadır
            # (Çalışma 3, answer_question quruluşu).
        },
        {
            "title_az": "Təşdid « ـّ » (qoşa oxunan samit)",
            "title_fa": "تشدید « ـّ »",
            "explanation_az": (
                "« ـّ » (təşdid) işarəsi samitin QOŞA oxunduğunu göstərir.\n"
                "Yazıda hərf bir dəfə yazılır, oxunuşda iki dəfə səslənir: بنّا — bən-na, عکّاس — əkkas.\n"
                "Təşdid xüsusilə peşə adlarında çox görünür: نجّار، خیّاط، قصّاب، کفّاش، معلّم."
            ),
            "conjugations": [
                {"pronoun_fa": "می‌نویسیم:", "form_fa": "بنّا؛ کفّاش؛ عکّاس؛ قصّاب"},
                {"pronoun_fa": "می‌خوانیم:", "form_fa": "بننا؛ کففاش؛ عککاس؛ قصصاب"},
            ],
            "examples": [
                {"fa": "عکّاس؛ کفّاش؛ نجّار؛ بنّا؛ قصّاب؛ خیّاط", "reading_az": "Əkkas; kəffaş; nəccar; bənna; qəssab; xəyyat.", "az": "əkkas; kəffaş; nəccar; bənna; qəssab; xəyyat — təşdidli samit qoşa oxunur."},
                {"fa": "معلّم؛ محمّد؛ ذرّت؛ پلّه؛ ذرّه‌بین؛ زرّافه", "reading_az": "Moəllem; Mohəmməd; zorrət; pelle; zərrebin; zərrafe.", "az": "moəllem; Mohəmməd; zorrət; pelle; zərrebin; zərrafe"},
                {"fa": "مکّه؛ بچّه؛ مجلّه؛ سکّه؛ ارّه؛ غوّاص", "reading_az": "Məkkə; bəççe; məcəlle; sekke; ərre; ğəvvas.", "az": "Məkkə; bəççe; məcəlle; sekke; ərre; ğəvvas"},
                {"fa": "این آقا عکّاس است. عکّاس، دوربین دارد.", "reading_az": "İn ağa əkkas əst. Əkkas, durbin darəd.", "az": "Bu kişi fotoqrafdır. Fotoqrafın fotoaparatı var."},
                {"fa": "آن‌ها کفّاش هستند. کفّاش‌ها کفش می‌دوزند.", "reading_az": "Anha kəffaş həstənd. Kəffaşha kəfş miduzənd.", "az": "Onlar çəkməçidirlər. Çəkməçilər ayaqqabı tikirlər."},
                {"fa": "محمّد نجّار است. نجّارها چوب و ارّه دارند.", "reading_az": "Mohəmməd nəccar əst. Nəccarha çub va ərre darənd.", "az": "Məhəmməd dülgərdir. Dülgərlərin taxtası və mişarı var."},
            ],
        },
    ],
    "exercises": [
        {
            # Dərslikdəki «مانند مثال کامل کنید» — hər cümlədə İKİ boşluq var
            # (biri təsdiq, biri inkar forması), ona görə çoxboşluqlu tip.
            "kind": "multi_blank",
            "title_fa": "مانند مثال کامل کنید",
            "instruction_az": "Nümunə kimi hər cümlədəki iki boşluğu doldurun",
            "example_fa": "من و حامد بنّا ___ ؛ مهندس ___ .\nمن و حامد بنّا **نیستیم**؛ مهندس *هستیم*.",
            "example_reading_az": "Mən va Hamed bənna nistim; mohəndes hastim.",
            "example_az": (
                "Mən və Hamid bənna deyilik; mühəndisik.\n"
                "Qırmızı — inkar forması (نیستیم), yaşıl — təsdiq forması (هستیم). "
                "Hər ikisi cümlənin şəxsinə uyğun seçilir."
            ),
            # 12 boşluq = 12 çip. Eyni söz bir neçə dəfə lazım olduqda sadəcə
            # təkrarlanır — hər çip ayrı indeksdir, uyğunluq mətnə görə yoxlanır.
            "word_bank": [
                "است", "است", "است", "نیست", "نیست", "نیست",
                "هستیم", "نیستیم", "هستید", "نیستید", "هستند", "نیستند",
            ],
            "items": [
                {
                    "fa_with_blanks": "مریم معلّم ___ ؛ مدیر ___ .",
                    "correct_answers": ["است", "نیست"],
                    "full_reading_az": "Məryəm moəllem əst; modir nist.",
                    "full_translation_az": "Məryəm müəllimdir; müdir deyil.",
                },
                {
                    "fa_with_blanks": "من و زینب خیّاط ___ ؛ عکّاس ___ .",
                    "correct_answers": ["هستیم", "نیستیم"],
                    "full_reading_az": "Mən va Zeynəb xəyyat hastim; əkkas nistim.",
                    "full_translation_az": "Mən və Zeynəb dərziyik; fotoqraf deyilik.",
                },
                {
                    "fa_with_blanks": "تو و فاطمه پرستار ___ ؛ پزشک ___ .",
                    "correct_answers": ["هستید", "نیستید"],
                    "full_reading_az": "To va Fateme pərəstar hastid; pezeşk nistid.",
                    "full_translation_az": "Sən və Fatimə tibb bacısısınız; həkim deyilsiniz.",
                },
                {
                    "fa_with_blanks": "آن خانم دندان‌پزشک ___ ؛ پرستار ___ .",
                    "correct_answers": ["است", "نیست"],
                    "full_reading_az": "An xanom dəndanpezeşk əst; pərəstar nist.",
                    "full_translation_az": "O xanım diş həkimidir; tibb bacısı deyil.",
                },
                {
                    "fa_with_blanks": "آن آقا چوپان ___ ؛ او قصّاب ___ .",
                    "correct_answers": ["است", "نیست"],
                    "full_reading_az": "An ağa çupan əst; u qəssab nist.",
                    "full_translation_az": "O kişi çobandır; o, qəssab deyil.",
                },
                {
                    "fa_with_blanks": "علی و احمد پلیس ___ ؛ قاضی ___ .",
                    "correct_answers": ["هستند", "نیستند"],
                    "full_reading_az": "Əli va Əhməd polis həstənd; qazi nistənd.",
                    "full_translation_az": "Əli və Əhməd polisdir; hakim deyillər.",
                },
            ],
        },
        {
            # Dərs 3-ün Çalışma 5 quruluşu: answer_question + çoxrəngli NÜMUNƏ
            # qutusu. Dərslikdə iki işlənmiş nümunə var — biri fərqli peşələr
            # (نه ilə), biri eyni peşə (بله ilə); hər ikisi qutuda verilir.
            "kind": "answer_question",
            "title_fa": "مانند مثال بپرسید و پاسخ دهید",
            "instruction_az": "Nümunə kimi soruşun və cavab verin",
            # Üç sətrin üç rolu üç rənglə ayrılır (dərslikdəki kimi):
            # 1) verilən sözlər — adi, 2) SUAL — yaşıl, 3) cavabın نه/بله-si —
            # qırmızı / mavi.
            "example_fa": (
                "آن‌ها / پرستار / پزشک\n"
                "*آیا آن‌ها پرستار هستند؟*\n"
                "**نه**، آن‌ها پرستار نیستند؛ پزشک هستند.\n"
                "شما / عکّاس / عکّاس\n"
                "*آیا شما عکّاس هستید؟*\n"
                "***بله***، ما عکّاس هستیم."
            ),
            "example_reading_az": (
                "Anha / pərəstar / pezeşk\n"
                "Aya anha pərəstar həstənd?\n"
                "Nə, anha pərəstar nistənd; pezeşk həstənd.\n"
                "Şoma / əkkas / əkkas\n"
                "Aya şoma əkkas hastid?\n"
                "Bəle, ma əkkas hastim."
            ),
            "example_az": (
                "Verilən üç söz: SUBYEKT / 1-ci peşə / 2-ci peşə.\n"
                "Yaşıl sətir — SUAL; həmişə 1-ci peşə ilə qurulur: "
                "آیا + SUBYEKT + 1-ci peşə + هستند/است؟\n"
                "Qırmızı «نه» — peşələr FƏRQLİ olanda: «نه، ... 1-ci peşə نیستند؛ 2-ci peşə هستند.»\n"
                "Mavi «بله» — hər iki peşə EYNİ olanda: «بله، ... هستند.»\n"
                "Diqqət: «شما» ilə soruşulanda cavab «ما ... هستیم» olur."
            ),
            "items": [
                {
                    "fa": "شما / چوپان / شکارچی",
                    "reading_az": "Şoma / çupan / şekarçi",
                    "az": "siz / çoban / ovçu",
                    "sample_answer_fa": "آیا شما چوپان هستید؟ نه، ما چوپان نیستیم؛ شکارچی هستیم.",
                    "sample_answer_reading_az": "Aya şoma çupan hastid? Nə, ma çupan nistim; şekarçi hastim.",
                    "sample_answer_az": "Siz çobansınızmı? Xeyr, biz çoban deyilik; ovçuyuq.",
                },
                {
                    "fa": "مریم / خیّاط / خیّاط",
                    "reading_az": "Məryəm / xəyyat / xəyyat",
                    "az": "Məryəm / dərzi / dərzi",
                    "sample_answer_fa": "آیا مریم خیّاط است؟ بله، مریم خیّاط است.",
                    "sample_answer_reading_az": "Aya Məryəm xəyyat əst? Bəle, Məryəm xəyyat əst.",
                    "sample_answer_az": "Məryəm dərzidirmi? Bəli, Məryəm dərzidir.",
                },
                {
                    "fa": "آن‌ها / نجّار / نجّار",
                    "reading_az": "Anha / nəccar / nəccar",
                    "az": "onlar / dülgər / dülgər",
                    "sample_answer_fa": "آیا آن‌ها نجّار هستند؟ بله، آن‌ها نجّار هستند.",
                    "sample_answer_reading_az": "Aya anha nəccar həstənd? Bəle, anha nəccar həstənd.",
                    "sample_answer_az": "Onlar dülgərdirmi? Bəli, onlar dülgərdir.",
                },
                {
                    "fa": "این خانم / مهندس / دکتر",
                    "reading_az": "İn xanom / mohəndes / doktor",
                    "az": "bu xanım / mühəndis / həkim",
                    "sample_answer_fa": "آیا این خانم مهندس است؟ نه، او مهندس نیست؛ دکتر است.",
                    "sample_answer_reading_az": "Aya in xanom mohəndes əst? Nə, u mohəndes nist; doktor əst.",
                    "sample_answer_az": "Bu xanım mühəndisdirmi? Xeyr, o, mühəndis deyil; həkimdir.",
                },
                {
                    "fa": "شما / قاضی / قاضی",
                    "reading_az": "Şoma / qazi / qazi",
                    "az": "siz / hakim / hakim",
                    # Nümunədəki «شما → ما ... هستیم» qaydasına uyğun.
                    "sample_answer_fa": "آیا شما قاضی هستید؟ بله، ما قاضی هستیم.",
                    "sample_answer_reading_az": "Aya şoma qazi hastid? Bəle, ma qazi hastim.",
                    "sample_answer_az": "Siz hakimsinizmi? Bəli, biz hakimik.",
                },
                {
                    "fa": "من و علی / دانش‌آموز / دانش‌جو",
                    "reading_az": "Mən va Əli / daneşamuz / daneşcu",
                    "az": "mən və Əli / şagird / tələbə",
                    "sample_answer_fa": "آیا شما دانش‌آموز هستید؟ نه، ما دانش‌آموز نیستیم؛ دانش‌جو هستیم.",
                    "sample_answer_reading_az": "Aya şoma daneşamuz hastid? Nə, ma daneşamuz nistim; daneşcu hastim.",
                    "sample_answer_az": "Siz şagirdsinizmi? Xeyr, biz şagird deyilik; tələbəyik.",
                },
                {
                    "fa": "آن آقا / رئیس‌جمهور / پادشاه",
                    "reading_az": "An ağa / rəis-comhur / padeşah",
                    "az": "o kişi / prezident / padşah",
                    "sample_answer_fa": "آیا آن آقا رئیس‌جمهور است؟ نه، او رئیس‌جمهور نیست؛ پادشاه است.",
                    "sample_answer_reading_az": "Aya an ağa rəis-comhur əst? Nə, u rəis-comhur nist; padeşah əst.",
                    "sample_answer_az": "O kişi prezidentdirmi? Xeyr, o, prezident deyil; padşahdır.",
                },
                {
                    "fa": "نرگس و سوسن / مدیر / معلّم",
                    "reading_az": "Nərges va Susən / modir / moəllem",
                    "az": "Nərgiz və Susən / müdir / müəllim",
                    "sample_answer_fa": "آیا نرگس و سوسن مدیر هستند؟ نه، آن‌ها مدیر نیستند؛ معلّم هستند.",
                    "sample_answer_reading_az": "Aya Nərges va Susən modir həstənd? Nə, anha modir nistənd; moəllem həstənd.",
                    "sample_answer_az": "Nərgiz və Susən müdirdirmi? Xeyr, onlar müdir deyil; müəllimdir.",
                },
            ],
        },
        {
            # Əvvəllər Mövzu 2-nin daxili drill-i idi; Çalışma 2 ilə eyni
            # quruluşa (answer_question + çoxrəngli NÜMUNƏ qutusu) keçirilib.
            "kind": "answer_question",
            "title_fa": "مانند مثال بپرسید و پاسخ دهید",
            "instruction_az": "Nümunə kimi soruşun və cavab verin",
            # 1) verilən sözlər — adi, 2) SUAL-lar — yaşıl, 3) peşə cavabı —
            # qırmızı, 4) «nə edir?» cavabı — mavi.
            "example_fa": (
                "برادرت / معلّم\n"
                "*برادرت چه‌کاره است؟* **برادرم معلّم است.**\n"
                "*معلّم چه‌کار می‌کند؟* ***معلّم درس می‌دهد.***"
            ),
            "example_reading_az": (
                "Bəradərət / moəllem\n"
                "Bəradərət çekare əst? Bəradərəm moəllem əst.\n"
                "Moəllem çekar mikonəd? Moəllem dərs midəhəd."
            ),
            "example_az": (
                "Verilən iki söz: ŞƏXS / PEŞƏ.\n"
                "Yaşıl sətirlər — İKİ SUAL: əvvəlcə «چه‌کاره است؟» (nəçidir?), "
                "sonra «چه‌کار می‌کند؟» (nə edir?).\n"
                "Qırmızı — peşə cavabı: «برادرم معلّم است.» (Qardaşım müəllimdir.)\n"
                "Mavi — işin cavabı: «معلّم درس می‌دهد.» (Müəllim dərs deyir.)\n"
                "Diqqət: «شما» ilə soruşulanda cavab «من ... هستم» olur."
            ),
            "items": [
                {
                    "fa": "شما / طلبه",
                    "reading_az": "Şoma / təllabe",
                    "az": "siz / din tələbəsi",
                    "sample_answer_fa": "شما چه‌کاره هستید؟ من طلبه هستم. طلبه چه‌کار می‌کند؟ طلبه درس دین می‌خواند.",
                    "sample_answer_reading_az": "Şoma çekare hastid? Mən təllabe hastəm. Təllabe çekar mikonəd? Təllabe dərse din mixanəd.",
                    "sample_answer_az": "Siz nəçisiniz? Mən din tələbəsiyəm. Din tələbəsi nə edir? Din tələbəsi din dərsi oxuyur.",
                },
                {
                    "fa": "آن‌ها / نجّار",
                    "reading_az": "Anha / nəccar",
                    "az": "onlar / dülgər",
                    "sample_answer_fa": "آن‌ها چه‌کاره هستند؟ آن‌ها نجّار هستند. نجّار چه‌کار می‌کند؟ نجّار میز و صندلی می‌سازد.",
                    "sample_answer_reading_az": "Anha çekare həstənd? Anha nəccar həstənd. Nəccar çekar mikonəd? Nəccar miz va səndəli misazəd.",
                    "sample_answer_az": "Onlar nəçidirlər? Onlar dülgərdirlər. Dülgər nə edir? Dülgər masa və stul düzəldir.",
                },
                {
                    "fa": "هادی / آهنگر",
                    "reading_az": "Hadi / ahəngər",
                    "az": "Hadi / dəmirçi",
                    "sample_answer_fa": "هادی چه‌کاره است؟ هادی آهنگر است. آهنگر چه‌کار می‌کند؟ آهنگر با آهن کار می‌کند.",
                    "sample_answer_reading_az": "Hadi çekare əst? Hadi ahəngər əst. Ahəngər çekar mikonəd? Ahəngər ba ahən kar mikonəd.",
                    "sample_answer_az": "Hadi nəçidir? Hadi dəmirçidir. Dəmirçi nə edir? Dəmirçi dəmirlə işləyir.",
                },
                {
                    "fa": "دوستتان / آشپز",
                    "reading_az": "Dustetan / aşpəz",
                    "az": "dostunuz / aşpaz",
                    "sample_answer_fa": "دوستتان چه‌کاره است؟ دوستم آشپز است. آشپز چه‌کار می‌کند؟ آشپز غذا می‌پزد.",
                    "sample_answer_reading_az": "Dustetan çekare əst? Dustəm aşpəz əst. Aşpəz çekar mikonəd? Aşpəz qəza mipəzəd.",
                    "sample_answer_az": "Dostunuz nəçidir? Dostum aşpazdır. Aşpaz nə edir? Aşpaz yemək bişirir.",
                },
                {
                    "fa": "مادرت / خیّاط",
                    "reading_az": "Madərət / xəyyat",
                    "az": "anan / dərzi",
                    "sample_answer_fa": "مادرت چه‌کاره است؟ مادرم خیّاط است. خیّاط چه‌کار می‌کند؟ خیّاط لباس می‌دوزد.",
                    "sample_answer_reading_az": "Madərət çekare əst? Madərəm xəyyat əst. Xəyyat çekar mikonəd? Xəyyat lebas miduzəd.",
                    "sample_answer_az": "Anan nəçidir? Anam dərzidir. Dərzi nə edir? Dərzi paltar tikir.",
                },
                {
                    "fa": "پدربزرگ علی / پزشک",
                    "reading_az": "Pedərbozorge Əli / pezeşk",
                    "az": "Əlinin babası / həkim",
                    "sample_answer_fa": "پدربزرگ علی چه‌کاره است؟ او پزشک است. پزشک چه‌کار می‌کند؟ پزشک بیمارها را معاینه می‌کند و نسخه می‌نویسد.",
                    "sample_answer_reading_az": "Pedərbozorge Əli çekare əst? U pezeşk əst. Pezeşk çekar mikonəd? Pezeşk bimarha ra moayene mikonəd va nosxe minevisəd.",
                    "sample_answer_az": "Əlinin babası nəçidir? O, həkimdir. Həkim nə edir? Həkim xəstələri müayinə edir və resept yazır.",
                },
            ],
        },
        {
            # Çalışma 4 — dərslikdəki «مانند مثال بگویید» (peşə + iş yeri).
            # Əvvəllər practice_reveal idi; Çalışma 2 quruluşuna (answer_question
            # + çoxrəngli NÜMUNƏ qutusu) keçirilib.
            "kind": "answer_question",
            "title_fa": "مانند مثال بگویید",
            "instruction_az": "Nümunə kimi deyin",
            # Yaşıl — iş yerini bildirən hissə: «در + YER + کار می‌کند».
            "example_fa": (
                "دوستم / مدیر / مدرسه‌ی ابن سینا\n"
                "دوستم مدیر است. او *در مدرسه‌ی ابن سینا کار می‌کند*."
            ),
            "example_reading_az": (
                "Dustəm / modir / mædrese-ye Ebn-e Sina\n"
                "Dustəm modir əst. U dər mædrese-ye Ebn-e Sina kar mikonəd."
            ),
            "example_az": (
                "Verilən üç söz: ŞƏXS / PEŞƏ / İŞ YERİ.\n"
                "Birinci cümlə peşəni bildirir: «دوستم مدیر است.» (Dostum müdirdir.)\n"
                "Yaşıl hissə — iş yeri: «در + YER + کار می‌کند» (… -da/-də işləyir).\n"
                "Diqqət: subyekt cəm olanda fel «کار می‌کنند» formasına düşür; "
                "hörmət bildirilən şəxs üçün də «ایشان … کار می‌کنند» işlənir."
            ),
            "items": [
                {
                    "fa": "عموی نادر / نگهبان / بانک ملّی ایران",
                    "reading_az": "Əmuye Nadər / negəhban / banke melliye Iran",
                    "az": "Nadirin əmisi / keşikçi / İranın Milli Bankı",
                    "sample_answer_fa": "عموی نادر نگهبان است. او در بانک ملّی ایران کار می‌کند.",
                    "sample_answer_reading_az": "Əmuye Nadər negəhban əst. U dər banke melliye Iran kar mikonəd.",
                    "sample_answer_az": "Nadirin əmisi keşikçidir. O, İranın Milli Bankında işləyir.",
                },
                {
                    "fa": "پدربزرگم / استاد / دانش‌گاه تهران",
                    "reading_az": "Pedərbozorgəm / ostad / daneşgahe Tehran",
                    "az": "babam / müəllim / Tehran Universiteti",
                    "sample_answer_fa": "پدربزرگم استاد است. ایشان در دانش‌گاه تهران کار می‌کنند.",
                    "sample_answer_reading_az": "Pedərbozorgəm ostad əst. İşan dər daneşgahe Tehran kar mikonənd.",
                    "sample_answer_az": "Babam müəllimdir. O, Tehran Universitetində işləyir.",
                },
                {
                    "fa": "زهرا و طاهره / پرستار / بیمارستان امام سجّاد",
                    "reading_az": "Zəhra va Tahere / pərəstar / bimarestane Emam Səccad",
                    "az": "Zəhra və Tahirə / tibb bacısı / İmam Səccad xəstəxanası",
                    "sample_answer_fa": "زهرا و طاهره پرستار هستند. آن‌ها در بیمارستان امام سجّاد کار می‌کنند.",
                    "sample_answer_reading_az": "Zəhra va Tahere pərəstar həstənd. Anha dər bimarestane Emam Səccad kar mikonənd.",
                    "sample_answer_az": "Zəhra və Tahirə tibb bacısıdır. Onlar İmam Səccad xəstəxanasında işləyirlər.",
                },
            ],
        },
        {
            # Çalışma 5 — dərslikdəki «مانند مثال بپرسید و پاسخ دهید»
            # (peşə + həmin peşənin aləti). Əvvəllər practice_reveal idi.
            "kind": "answer_question",
            "title_fa": "مانند مثال بپرسید و پاسخ دهید",
            "instruction_az": "Nümunə kimi soruşun və cavab verin",
            # Qırmızı — iki sual sözü: «چه‌کاره» (nəçidir?) və «چه» (nə?).
            "example_fa": (
                "یوسف / عکّاس / دوربین\n"
                "یوسف **چه‌کاره** است؟ او عکّاس است.\n"
                "عکّاس **چه** دارد؟ عکّاس دوربین دارد."
            ),
            "example_reading_az": (
                "Yusef / əkkas / durbin\n"
                "Yusef çekare əst? U əkkas əst.\n"
                "Əkkas çe darəd? Əkkas durbin darəd."
            ),
            "example_az": (
                "Verilən üç söz: ŞƏXS / PEŞƏ / ALƏT.\n"
                "Qırmızı — iki sual sözü: «چه‌کاره» (nəçidir?) və «چه» (nə?).\n"
                "Birinci sual peşəni soruşur, ikinci sual həmin peşənin nəyi "
                "olduğunu (alətini) soruşur.\n"
                "Diqqət: subyekt cəm və ya hörmət formasında olanda "
                "«چه‌کاره هستند؟ … چه دارند؟» şəklinə düşür."
            ),
            "items": [
                {
                    "fa": "محمّد / خیّاط / قیچی، سوزن و اتو",
                    "reading_az": "Mohəmməd / xəyyat / qeyçi, suzən va otu",
                    "az": "Məhəmməd / dərzi / qayçı, iynə və ütü",
                    "sample_answer_fa": "محمّد چه‌کاره است؟ او خیّاط است. خیّاط چه دارد؟ خیّاط قیچی، سوزن و اتو دارد.",
                    "sample_answer_reading_az": "Mohəmməd çekare əst? U xəyyat əst. Xəyyat çe darəd? Xəyyat qeyçi, suzən va otu darəd.",
                    "sample_answer_az": "Məhəmməd nəçidir? O, dərzidir. Dərzinin nəyi var? Dərzinin qayçısı, iynəsi və ütüsü var.",
                },
                {
                    "fa": "زهرا خانم / استاد / رایانه و کتاب",
                    "reading_az": "Zəhra xanom / ostad / rayane va ketab",
                    "az": "Zəhra xanım / müəllim / kompüter və kitab",
                    "sample_answer_fa": "زهرا خانم چه‌کاره است؟ ایشان استاد هستند. استاد چه دارد؟ استاد رایانه و کتاب دارد.",
                    "sample_answer_reading_az": "Zəhra xanom çekare əst? İşan ostad həstənd. Ostad çe darəd? Ostad rayane va ketab darəd.",
                    "sample_answer_az": "Zəhra xanım nəçidir? O, müəllimdir. Müəllimin nəyi var? Müəllimin komputeri və kitabı var.",
                },
                {
                    "fa": "دخترت / دانش‌جو / کیف و نوشت‌افزار",
                    "reading_az": "Doxtərət / daneşcu / kif va neveştəfzar",
                    "az": "qızın / tələbə / çanta və yazı ləvazimatı",
                    "sample_answer_fa": "دخترت چه‌کاره است؟ دخترم دانش‌جو است. دانش‌جو چه دارد؟ دانش‌جو کیف و نوشت‌افزار دارد.",
                    "sample_answer_reading_az": "Doxtərət çekare əst? Doxtərəm daneşcu əst. Daneşcu çe darəd? Daneşcu kif va neveştəfzar darəd.",
                    "sample_answer_az": "Qızın nəçidir? Qızım tələbədir. Tələbənin nəyi var? Tələbənin çantası və yazı ləvazimatı var.",
                },
            ],
        },
        {
            # Çalışma 6 — dərslikdəki «مانند مثال با واژه‌ی «امّا» جمله بسازید».
            # Əvvəllər practice_reveal idi; Çalışma 2 quruluşuna keçirilib.
            "kind": "answer_question",
            "title_fa": "مانند مثال با واژه‌ی «امّا» جمله بسازید",
            "instruction_az": "Nümunə kimi «امّا» sözü ilə cümlə qurun",
            # Yaşıl — iki cümləni qarşılaşdıran bağlayıcı «امّا».
            "example_fa": (
                "من رایانه / دوستم\n"
                "من رایانه دارم؛ *امّا* دوستم رایانه ندارد."
            ),
            "example_reading_az": (
                "Mən rayane / dustəm\n"
                "Mən rayane daram; əmma dustəm rayane nədarəd."
            ),
            "example_az": (
                "Verilən iki tərəf: 1-ci ŞƏXS + ƏŞYA/SİFƏT / 2-ci ŞƏXS.\n"
                "Yaşıl «امّا» (amma) iki cümləni qarşı-qarşıya qoyur: birinci hissə "
                "təsdiq, ikinci hissə inkar olur — «… دارم؛ امّا … ندارد.»\n"
                "Diqqət: sifətlə qurulanda «دارد/ندارد» yox, «است/هستند» işlənir: "
                "«سعید چاق است؛ امّا برادرش لاغر است.»\n"
                "Fel həmişə öz şəxsinə uyğun gəlir: دارم / دارد / داریم / دارند."
            ),
            "items": [
                {
                    "fa": "زهرا عینک / همسرش",
                    "reading_az": "Zəhra eynək / həmsərəş",
                    "az": "Zəhra eynək / həyat yoldaşı",
                    "sample_answer_fa": "زهرا عینک دارد؛ امّا همسرش عینک ندارد.",
                    "sample_answer_reading_az": "Zəhra eynək darəd; əmma həmsərəş eynək nədarəd.",
                    "sample_answer_az": "Zəhranın eynəyi var; amma həyat yoldaşının eynəyi yoxdur.",
                },
                {
                    "fa": "همسرم عمو / من",
                    "reading_az": "Həmsərəm əmu / mən",
                    "az": "həyat yoldaşım əmi / mən",
                    "sample_answer_fa": "همسرم عمو دارد؛ امّا من عمو ندارم.",
                    "sample_answer_reading_az": "Həmsərəm əmu darəd; əmma mən əmu nədaram.",
                    "sample_answer_az": "Həyat yoldaşımın əmisi var; amma mənim əmim yoxdur.",
                },
                {
                    "fa": "سعید چاق / برادرش لاغر",
                    "reading_az": "Səid çaq / bəradərəş lağər",
                    "az": "Səid kök / qardaşı arıq",
                    "sample_answer_fa": "سعید چاق است؛ امّا برادرش لاغر است.",
                    "sample_answer_reading_az": "Səid çaq əst; əmma bəradərəş lağər əst.",
                    "sample_answer_az": "Səid kökdür; amma qardaşı arıqdır.",
                },
                {
                    "fa": "ما مجرّد / آن‌ها متأهل",
                    "reading_az": "Ma mocərrəd / anha motəəhhel",
                    "az": "biz subay / onlar evli",
                    "sample_answer_fa": "ما مجرّد هستیم؛ امّا آن‌ها متأهل هستند.",
                    "sample_answer_reading_az": "Ma mocərrəd hastim; əmma anha motəəhhel həstənd.",
                    "sample_answer_az": "Biz subayıq; amma onlar evlidir.",
                },
            ],
        },
        {
            # Çalışma 7 — dərslikdəki «برای هر تصویر، دو جمله بگویید».
            # Dərs 2-nin Çalışma 8 quruluşu: nümunə qutusu yoxdur, hər şəkil
            # üçün iki cümlə. Şəkillər qəsdən boş buraxılıb — istifadəçi onları
            # admin paneldən yükləyəcək (Dərs 4-də ümumiyyətlə şəkil aktivi yoxdur).
            "kind": "picture_sentences",
            "title_fa": "برای هر تصویر، دو جمله بگویید",
            "instruction_az": "Hər şəkil üçün iki cümlə deyin",
            "items": [
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این آقا نجّار است.", "reading_az": "İn ağa nəccar əst.", "az": "Bu kişi dülgərdir."},
                        {"fa": "نجّار با چوب و ارّه کار می‌کند.", "reading_az": "Nəccar ba çub va ərre kar mikonəd.", "az": "Dülgər taxta və mişarla işləyir."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این آقا خیّاط است.", "reading_az": "İn ağa xəyyat əst.", "az": "Bu kişi dərzidir."},
                        {"fa": "خیّاط با چرخ خیّاطی لباس می‌دوزد.", "reading_az": "Xəyyat ba çərxe xəyyati lebas miduzəd.", "az": "Dərzi tikiş maşını ilə paltar tikir."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این آقا مدیر مدرسه است.", "reading_az": "İn ağa modire mædrese əst.", "az": "Bu kişi məktəb müdiridir."},
                        {"fa": "مدیر در دفتر با دانش‌آموزان صحبت می‌کند.", "reading_az": "Modir dər dəftər ba daneşamuzan sohbət mikonəd.", "az": "Müdir kabinetdə şagirdlərlə söhbət edir."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این آقا مهندس رایانه است.", "reading_az": "İn ağa mohəndese rayane əst.", "az": "Bu kişi kompüter mühəndisidir."},
                        {"fa": "او در دفتر با رایانه کار می‌کند.", "reading_az": "U dər dəftər ba rayane kar mikonəd.", "az": "O, ofisdə kompüterlə işləyir."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این آقا معلّم است.", "reading_az": "İn ağa moəllem əst.", "az": "Bu kişi müəllimdir."},
                        {"fa": "معلّم روی تخته می‌نویسد و درس می‌دهد.", "reading_az": "Moəllem ruye təxte minevisəd va dərs midəhəd.", "az": "Müəllim lövhədə yazır və dərs deyir."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این آقا چوپان است.", "reading_az": "İn ağa çupan əst.", "az": "Bu kişi çobandır."},
                        {"fa": "چوپان گوسفندها را به صحرا می‌برد.", "reading_az": "Çupan gusfəndha ra be səhra mibərəd.", "az": "Çoban qoyunları çölə aparır."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این آقا پزشک است.", "reading_az": "İn ağa pezeşk əst.", "az": "Bu kişi həkimdir."},
                        {"fa": "پزشک بیمار را معاینه می‌کند و نسخه می‌نویسد.", "reading_az": "Pezeşk bimar ra moayene mikonəd va nosxe minevisəd.", "az": "Həkim xəstəni müayinə edir və resept yazır."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این خانم دندان‌پزشک است.", "reading_az": "İn xanom dəndanpezeşk əst.", "az": "Bu xanım diş həkimidir."},
                        {"fa": "دندان‌پزشک دندان بیمار را معاینه می‌کند.", "reading_az": "Dəndanpezeşk dəndane bimar ra moayene mikonəd.", "az": "Diş həkimi xəstənin dişini müayinə edir."},
                    ],
                },
            ],
        },
    ],
    "sentence_practice": {
        "listen_exercises": [
            {
                "items": [
                    {
                        "fa": "پدرم نجّار است. او میز و صندلی می‌سازد.",
                        "reading_az": "Pedərəm nəccar əst. U miz va səndəli misazəd.",
                        "az": "Atam dülgərdir. O, masa və stul düzəldir.",
                    },
                    {
                        "fa": "آن مرد، رفتگر است. او خیابان را جارو می‌کند.",
                        "reading_az": "An mərd, roftegər əst. U xiyaban ra caru mikonəd.",
                        "az": "O kişi zibilyığandır. O, küçəni süpürür.",
                    },
                    {
                        "fa": "نادر و سلیمان کارگر هستند. آن‌ها به بنّا کمک می‌کنند.",
                        "reading_az": "Nadər va Soleyman kargər həstənd. Anha be bənna komək mikonənd.",
                        "az": "Nadir və Süleyman fəhlədir. Onlar bənnaya kömək edirlər.",
                    },
                    {
                        "fa": "آن خانم، استاد ما است؛ ایشان به ما زبان فارسی درس می‌دهد.",
                        "reading_az": "An xanom, ostade ma əst; işan be ma zəbane farsi dərs midəhəd.",
                        "az": "O xanım bizim müəlliməmizdir; o bizə fars dili öyrədir.",
                    },
                    {
                        "fa": "ما مهندسِ رایانه هستیم و در جامعة المصطفی کار می‌کنیم.",
                        "reading_az": "Ma mohəndese rayane hastim va dər Cameətol-Mostəfa kar mikonim.",
                        "az": "Biz kompüter mühəndisiyik və əl-Müstəfa Cəmiyyətində işləyirik.",
                    },
                    {
                        "fa": "برادرم بنّا است و خانه می‌سازد. خواهرم خیّاط است و لباس می‌دوزد.",
                        "reading_az": "Bəradərəm bənna əst va xane misazəd. Xahərəm xəyyat əst va lebas miduzəd.",
                        "az": "Qardaşım bənnadır və ev tikir. Bacım dərzidir və paltar tikir.",
                    },
                    {
                        "fa": "نجّار با چوب، در و پنجره می‌سازد و آهنگر با آهن، در و پنجره می‌سازد.",
                        "reading_az": "Nəccar ba çub, dər va pəncəre misazəd va ahəngər ba ahən, dər va pəncəre misazəd.",
                        "az": "Dülgər taxtadan qapı və pəncərə düzəldir, dəmirçi isə dəmirdən qapı və pəncərə düzəldir.",
                    },
                    {
                        "fa": "احمد و دوستش دانش‌جو هستند. آن‌ها در دانش‌گاه تهران درس می‌خوانند.",
                        "reading_az": "Əhməd va dustəş daneşcu həstənd. Anha dər daneşgahe Tehran dərs mixanənd.",
                        "az": "Əhməd və dostu tələbədir. Onlar Tehran Universitetində oxuyurlar.",
                    },
                    {
                        "fa": "محمّد و فاطمه دانش‌آموز هستند؛ پدرشان معلّم است و مادرشان مدیر مدرسه است.",
                        "reading_az": "Mohəmməd va Fateme daneşamuz həstənd; pedərşan moəllem əst va madərşan modire mædrese əst.",
                        "az": "Məhəmməd və Fatimə şagirddir; ataları müəllim, anaları isə məktəb müdiridir.",
                    },
                    {
                        "fa": "من و همسرم پزشک هستیم. ما بیمارها را معاینه می‌کنیم و برای آن‌ها دارو می‌نویسیم.",
                        "reading_az": "Mən va həmsərəm pezeşk hastim. Ma bimarha ra moayene mikonim va bəraye anha daru minevisim.",
                        "az": "Mən və həyat yoldaşım həkimik. Biz xəstələri müayinə edirik və onlara dərman yazırıq.",
                    },
                ],
            },
        ],
        "answer_items": [
            {
                "fa": "اسم رئیس‌جمهور کشورتان چیست؟",
                "reading_az": "Esme rəis-comhure kəşvəretan çist?",
                "az": "Ölkənizin prezidentinin adı nədir?",
            },
            {
                "fa": "آهنگر و نجّار چه‌کار می‌کنند؟",
                "reading_az": "Ahəngər va nəccar çekar mikonənd?",
                "az": "Dəmirçi və dülgər nə iş görür?",
                "sample_answer_fa": "آهنگر با آهن کار می‌کند و نجّار با چوب کار می‌کند.",
                "sample_answer_reading_az": "Ahəngər ba ahən kar mikonəd va nəccar ba çub kar mikonəd.",
                "sample_answer_az": "Dəmirçi dəmirlə, dülgər isə taxta ilə işləyir.",
            },
            {
                "fa": "آیا برادرتان مهندس رایانه است؟",
                "reading_az": "Aya bəradəretan mohəndese rayane əst?",
                "az": "Qardaşınız kompüter mühəndisidirmi?",
                "sample_answer_fa": "بله، برادرم مهندس رایانه است.",
                "sample_answer_reading_az": "Bəle, bəradərəm mohəndese rayane əst.",
                "sample_answer_az": "Bəli, qardaşım kompüter mühəndisidir.",
            },
            {
                "fa": "آیا خیّاط میز و صندلی نمی‌سازد؟",
                "reading_az": "Aya xəyyat miz va səndəli nemisazəd?",
                "az": "Dərzi masa və stul düzəltmir?",
                "sample_answer_fa": "بله، خیّاط میز و صندلی نمی‌سازد؛ او لباس می‌دوزد.",
                "sample_answer_reading_az": "Bəle, xəyyat miz va səndəli nemisazəd; u lebas miduzəd.",
                "sample_answer_az": "Bəli, dərzi masa və stul düzəltmir; o, paltar tikir.",
            },
            {
                "fa": "پزشک چه‌کار می‌کند؟",
                "reading_az": "Pezeşk çekar mikonəd?",
                "az": "Həkim nə iş görür?",
                "sample_answer_fa": "پزشک بیمارها را معاینه می‌کند و نسخه می‌نویسد.",
                "sample_answer_reading_az": "Pezeşk bimarha ra moayene mikonəd va nosxe minevisəd.",
                "sample_answer_az": "Həkim xəstələri müayinə edir və resept yazır.",
            },
        ],
    },
    "reading_text": {
        "title_fa": "خانواده‌ی من",
        "title_az": "Mənim ailəm",
        "paragraphs_fa": [
            "من در یک خانواده‌ی شش‌نفره زندگی می‌کنم. اسمم نرگس است. من متأهل هستم. نام همسرم، صادق است. من و صادق دانش‌جو هستیم و در دانش‌گاه تهران درس می‌خوانیم.",
            "همسرم، برادر و خواهر ندارد؛ امّا من یک خواهر و دو برادر دارم. خواهرم شهربانو، از من کوچک‌تر است. او دانش‌آموز است و در مدرسه‌ی شهید بهشتی درس می‌خواند.",
            "برادرم سجّاد، مهندس رایانه است. ایشان در فرودگاه امام‌خمینی تهران کار می‌کند و برادرم حسن، دکترِ قلب است. او در بیمارستان ابوعلی سینا کار می‌کند.",
            "مادرم خانه‌دار است و پدرم معلّم بازنشسته است. ایشان شصت سال دارد. او گاهی کتاب مطالعه می‌کند، گاهی روزنامه می‌خواند و گاهی در کارهای خانه به مادرم کمک می‌کند.",
            "من خانواده‌ام را بسیار دوست دارم.",
        ],
        "footnotes": [
            {"fa": "خانه‌دار", "az": "evdar"},
            {"fa": "بازنشسته", "az": "təqaüdçü"},
            {"fa": "شصت", "az": "altmış"},
            {"fa": "گاهی", "az": "bəzən"},
            {"fa": "امّا", "az": "amma"},
        ],
        "full_translation_az": (
            "Mən altı nəfərlik bir ailədə yaşayıram. Adım Nərgizdir. Mən evliyəm. Həyat yoldaşımın adı Sadiqdir. "
            "Mən və Sadiq tələbəyik və Tehran Universitetində oxuyuruq.\n\n"
            "Həyat yoldaşımın qardaşı və bacısı yoxdur; amma mənim bir bacım və iki qardaşım var. Bacım Şəhrbanu "
            "məndən kiçikdir. O, şagirddir və Şəhid Behişti məktəbində oxuyur.\n\n"
            "Qardaşım Səccad kompüter mühəndisidir. O, Tehranın İmam Xomeyni hava limanında işləyir. Qardaşım "
            "Həsən isə ürək həkimidir. O, Əbu Əli Sina xəstəxanasında işləyir.\n\n"
            "Anam evdar qadındır, atam isə təqaüdçü müəllimdir. Onun altmış yaşı var. O, bəzən kitab oxuyur, "
            "bəzən qəzet oxuyur, bəzən də ev işlərində anama kömək edir.\n\n"
            "Mən ailəmi çox sevirəm."
        ),
        "sentences": [
            {"fa": "من در یک خانواده‌ی شش‌نفره زندگی می‌کنم.", "reading_az": "Mən dər yek xanevade-ye şeş-nəfəre zendegi mikonəm.", "az": "Mən altı nəfərlik bir ailədə yaşayıram.", "new_paragraph": True},
            {"fa": "اسمم نرگس است.", "reading_az": "Esməm Nərges əst.", "az": "Adım Nərgizdir."},
            {"fa": "من متأهل هستم.", "reading_az": "Mən motəəhhel hastəm.", "az": "Mən evliyəm."},
            {"fa": "نام همسرم، صادق است.", "reading_az": "Name həmsərəm, Sadeq əst.", "az": "Həyat yoldaşımın adı Sadiqdir."},
            {
                "fa": "من و صادق دانش‌جو هستیم و در دانش‌گاه تهران درس می‌خوانیم.",
                "reading_az": "Mən va Sadeq daneşcu hastim va dər daneşgahe Tehran dərs mixanim.",
                "az": "Mən və Sadiq tələbəyik və Tehran Universitetində oxuyuruq.",
            },
            {
                "fa": "همسرم، برادر و خواهر ندارد؛ امّا من یک خواهر و دو برادر دارم.",
                "reading_az": "Həmsərəm, bəradər va xahər nədarəd; əmma mən yek xahər va do bəradər daram.",
                "az": "Həyat yoldaşımın qardaşı və bacısı yoxdur; amma mənim bir bacım və iki qardaşım var.",
                "new_paragraph": True,
            },
            {"fa": "خواهرم شهربانو، از من کوچک‌تر است.", "reading_az": "Xahərəm Şəhrbanu, əz mən kuçektər əst.", "az": "Bacım Şəhrbanu məndən kiçikdir."},
            {
                "fa": "او دانش‌آموز است و در مدرسه‌ی شهید بهشتی درس می‌خواند.",
                "reading_az": "U daneşamuz əst va dər mædrese-ye Şəhide Beheşti dərs mixanəd.",
                "az": "O, şagirddir və Şəhid Behişti məktəbində oxuyur.",
            },
            {"fa": "برادرم سجّاد، مهندس رایانه است.", "reading_az": "Bəradərəm Səccad, mohəndese rayane əst.", "az": "Qardaşım Səccad kompüter mühəndisidir.", "new_paragraph": True},
            {"fa": "ایشان در فرودگاه امام‌خمینی تهران کار می‌کند.", "reading_az": "İşan dər forudgahe Emam Xomeyniye Tehran kar mikonəd.", "az": "O, Tehranın İmam Xomeyni hava limanında işləyir."},
            {"fa": "برادرم حسن، دکترِ قلب است.", "reading_az": "Bəradərəm Həsən, doktore qəlb əst.", "az": "Qardaşım Həsən ürək həkimidir."},
            {"fa": "او در بیمارستان ابوعلی سینا کار می‌کند.", "reading_az": "U dər bimarestane Əbuəli Sina kar mikonəd.", "az": "O, Əbu Əli Sina xəstəxanasında işləyir."},
            {
                "fa": "مادرم خانه‌دار است و پدرم معلّم بازنشسته است.",
                "reading_az": "Madərəm xanedar əst va pedərəm moəlleme bazneşəste əst.",
                "az": "Anam evdar qadındır, atam isə təqaüdçü müəllimdir.",
                "new_paragraph": True,
            },
            {"fa": "ایشان شصت سال دارد.", "reading_az": "İşan şəst sal darəd.", "az": "Onun altmış yaşı var."},
            {
                "fa": "او گاهی کتاب مطالعه می‌کند، گاهی روزنامه می‌خواند و گاهی در کارهای خانه به مادرم کمک می‌کند.",
                "reading_az": "U gahi ketab motaleə mikonəd, gahi ruzname mixanəd va gahi dər karhaye xane be madərəm komək mikonəd.",
                "az": "O, bəzən kitab oxuyur, bəzən qəzet oxuyur, bəzən də ev işlərində anama kömək edir.",
            },
            {"fa": "من خانواده‌ام را بسیار دوست دارم.", "reading_az": "Mən xanevadeəm ra besyar dust daram.", "az": "Mən ailəmi çox sevirəm.", "new_paragraph": True},
        ],
        "comprehension_questions": [
            {
                "question_fa": "نرگس و همسرش چه‌کاره هستند؟",
                "reading_az": "Nərges va həmsərəş çekare həstənd?",
                "az": "Nərgiz və həyat yoldaşı nəçidir?",
                "sample_answer_fa": "نرگس و همسرش دانش‌جو هستند.",
                "sample_answer_reading_az": "Nərges va həmsərəş daneşcu həstənd.",
                "sample_answer_az": "Nərgiz və həyat yoldaşı tələbədir.",
            },
            {
                "question_fa": "آیا پدر نرگس الآن درس می‌دهد؟",
                "reading_az": "Aya pedəre Nərges əl-an dərs midəhəd?",
                "az": "Nərgizin atası indi dərs deyirmi?",
                "sample_answer_fa": "نه، پدر نرگس بازنشسته است.",
                "sample_answer_reading_az": "Nə, pedəre Nərges bazneşəste əst.",
                "sample_answer_az": "Xeyr, Nərgizin atası təqaüdçüdür.",
            },
            {
                "question_fa": "پدر نرگس هر روز چه‌کار می‌کند؟",
                "reading_az": "Pedəre Nərges hər ruz çekar mikonəd?",
                "az": "Nərgizin atası hər gün nə edir?",
                "sample_answer_fa": "او گاهی کتاب مطالعه می‌کند و گاهی به مادرم کمک می‌کند.",
                "sample_answer_reading_az": "U gahi ketab motaleə mikonəd va gahi be madərəm komək mikonəd.",
                "sample_answer_az": "O, bəzən kitab oxuyur, bəzən anama kömək edir.",
            },
            {
                "question_fa": "صادق در کدام دانش‌گاه درس می‌خواند؟",
                "reading_az": "Sadeq dər kodam daneşgah dərs mixanəd?",
                "az": "Sadiq hansı universitetdə oxuyur?",
                "sample_answer_fa": "صادق در دانش‌گاه تهران درس می‌خواند.",
                "sample_answer_reading_az": "Sadeq dər daneşgahe Tehran dərs mixanəd.",
                "sample_answer_az": "Sadiq Tehran Universitetində oxuyur.",
            },
            {
                "question_fa": "کدام برادر نرگس، دکترِ قلب است؟",
                "reading_az": "Kodam bəradəre Nərges, doktore qəlb əst?",
                "az": "Nərgizin hansı qardaşı ürək həkimidir?",
                "sample_answer_fa": "برادرش حسن، دکترِ قلب است.",
                "sample_answer_reading_az": "Bəradərəş Həsən, doktore qəlb əst.",
                "sample_answer_az": "Qardaşı Həsən ürək həkimidir.",
            },
            {
                "question_fa": "آیا خانواده‌ی نرگس، چهار نفره هستند؟",
                "reading_az": "Aya xanevade-ye Nərges, çahar-nəfəre həstənd?",
                "az": "Nərgizin ailəsi dörd nəfərlikdirmi?",
                "sample_answer_fa": "نه، خانواده‌ی نرگس شش نفره هستند.",
                "sample_answer_reading_az": "Nə, xanevade-ye Nərges şeş-nəfəre həstənd.",
                "sample_answer_az": "Xeyr, Nərgizin ailəsi altı nəfərlikdir.",
            },
            {
                "question_fa": "سجّاد چه‌کاره است و کجا کار می‌کند؟",
                "reading_az": "Səccad çekare əst va koca kar mikonəd?",
                "az": "Səccad nəçidir və harada işləyir?",
                "sample_answer_fa": "سجّاد مهندس رایانه است و در فرودگاه امام‌خمینی کار می‌کند.",
                "sample_answer_reading_az": "Səccad mohəndese rayane əst va dər forudgahe Emam Xomeyni kar mikonəd.",
                "sample_answer_az": "Səccad kompüter mühəndisidir və İmam Xomeyni hava limanında işləyir.",
            },
        ],
    },
}
