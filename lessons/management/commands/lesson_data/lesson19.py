# Dərs 19 — پزشکی (Tibb)
# Mənbə: کتاب دوم, səh. 231-242

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
        # Səh. 232-də şəkilli lövhədə olan, əvvəl faylda çatışmayan sözlər.
        {"fa": "درد می‌کند", "reading": "dərd mikonəd", "az": "ağrıyır"},
        {"fa": "عمل می‌کند", "reading": "əməl mikonəd", "az": "əməliyyat edir"},
        # Səh. 236 «... زدن» birləşmələri.
        {"fa": "لبخند می‌زند", "reading": "ləbxənd mizənəd", "az": "gülümsəyir"},
        {"fa": "شانه می‌زند", "reading": "şane mizənəd", "az": "(saçını) darayır"},
        {"fa": "کِرِم می‌زند", "reading": "kerem mizənəd", "az": "krem sürtür"},
        {"fa": "اتو می‌زند", "reading": "otu mizənəd", "az": "ütüləyir"},
        {"fa": "در می‌زند", "reading": "dər mizənəd", "az": "qapını döyür"},
        {"fa": "زنگ می‌زند", "reading": "zəng mizənəd", "az": "zəng vurur"},
        {"fa": "تلفن می‌زند", "reading": "telefon mizənəd", "az": "telefon edir"},
        {"fa": "حرف می‌زند", "reading": "hərf mizənəd", "az": "danışır"},
        {"fa": "دست می‌زند", "reading": "dəst mizənəd", "az": "əl çalır / əl vurur"},
        {"fa": "به‌هم می‌زند", "reading": "be həm mizənəd", "az": "qarışdırır"},
        {"fa": "رنگ می‌زند", "reading": "rəng mizənəd", "az": "rəngləyir"},
        {"fa": "دور می‌زند", "reading": "dor mizənəd", "az": "geri dönür (maşınla)"},
        {"fa": "سوت می‌زند", "reading": "sut mizənəd", "az": "fit çalır"},
        # Səh. 240-242 mətn və çalışmalarındakı sözlər.
        {"fa": "نوازش می‌کند", "reading": "nəvazeş mikonəd", "az": "sığallayır, əzizləyir"},
        {"fa": "شبانه‌روزی", "reading": "şəbaneruzi", "az": "Sutkalıq (gecə-gündüz açıq)"},
        {"fa": "خمیردندان", "reading": "xəmirdəndan", "az": "Diş pastası"},
        {"fa": "گوش و حلق و بینی", "reading": "quş-o-həlq-o-bini", "az": "Qulaq-boğaz-burun (LOR)"},
        {"fa": "شلوغ", "reading": "şoluğ", "az": "İzdihamlı, sıx"},
        {"fa": "فقیر", "reading": "fəqir", "az": "Kasıb"},
        {"fa": "به خاطرِ", "reading": "be xatere", "az": "…-a görə, səbəbindən"},
        {"fa": "درمان‌گاه", "reading": "dərmangah", "az": "Poliklinika"},
        {"fa": "تقویم", "reading": "təqvim", "az": "Təqvim"},
        {"fa": "سررسید", "reading": "sərresid", "az": "Gündəlik (tarixli dəftər)"},
        # Səh. 233-dəki «واژه‌های خوانده شده» bölməsi.
        {"fa": "بیمارستان", "reading": "bimarestan", "az": "Xəstəxana"},
        {"fa": "بیمار", "reading": "bimar", "az": "Xəstə"},
        {"fa": "مریض", "reading": "mariz", "az": "Xəstə"},
        {"fa": "پزشک", "reading": "pezeşk", "az": "Həkim"},
        {"fa": "دندان‌پزشک", "reading": "dandanpezeşk", "az": "Diş həkimi"},
        {"fa": "پرستار", "reading": "pərəstar", "az": "Tibb bacısı"},
        {"fa": "امدادگر", "reading": "əmdadgər", "az": "Təcili yardım əməkdaşı"},
        {"fa": "دارو", "reading": "daru", "az": "Dərman"},
        {"fa": "واکسن", "reading": "vaksən", "az": "Peyvənd"},
        {"fa": "خون", "reading": "xun", "az": "Qan"},
        {"fa": "معاینه می‌کند", "reading": "moayene mikonəd", "az": "Müayinə edir"},
        {"fa": "نسخه می‌نویسد", "reading": "nosxe minevisəd", "az": "Resept yazır"},
        {"fa": "اورژانس", "reading": "orjans", "az": "Təcili yardım şöbəsi"},
        {"fa": "فوریت‌های پزشکی", "reading": "foriyyathaye pezeşki", "az": "Təcili tibbi yardım"},
    ],
    "grammar_notes": [
        {
            "title_az": "«بفرمایید» sözü — nəzakət ifadəsi",
            "title_fa": "«بفرمایید»",
            "explanation_az": (
                "«بفرمایید» nəzakət sözüdür və mənası vəziyyətə görə dəyişir: buyurun, alın, keçin, oturun.\n"
                "Yemək təklif edəndə, hədiyyə verəndə, yer göstərəndə və içəri dəvət edəndə işlənir.\n"
                "Samimi (tək) forması «بفرما», nəzakətli forması «بفرمایید»dir."
            ),
            "conjugations": [
                {"pronoun_fa": "qonağa yer göstərəndə", "form_fa": "بفرمایید (buyurun)"},
                {"pronoun_fa": "hədiyyə verəndə", "form_fa": "بفرمایید (buyurun, alın)"},
                {"pronoun_fa": "avtobusda yer göstərəndə", "form_fa": "بفرمایید (buyurun oturun)"},
                {"pronoun_fa": "kimisə içəri dəvət edəndə", "form_fa": "بفرمایید (buyurun)"},
            ],
            "examples": [
                {
                    "fa": "«بفرمایید» sözü fars dilində bir çox nəzakət vəziyyətində işlənir: yemək təklif edəndə, hədiyyə verəndə, yer göstərəndə, kimisə otağa dəvət edəndə, taksidə sərnişinə yer göstərəndə, lifdə keçməyə icazə verəndə.",
                    "az": "«بفرمایید» sözünün tərcüməsi kontekstdən asılı olaraq dəyişir: buyurun, alın, keçin, oturun.",
                },
                {
                    "fa": "مهمان‌ها سرِ سفره نشستند و میزبان گفت: بفرمایید.",
                    "reading_az": "Mehmanha səre səfre nesəstənd va mizban goft: bəfərmayid.",
                    "az": "Qonaqlar süfrə başına oturdular və ev sahibi dedi: buyurun.",
                },
                {
                    "fa": "منشی گفت: سلام، بفرمایید. — بیمار وارد مطب دکتر شد.",
                    "reading_az": "Mənşi goft: səlam, bəfərmayid. — Bimar varede mətəbe doktor şod.",
                    "az": "Katibə dedi: salam, buyurun. — Xəstə həkimin kabinetinə girdi.",
                },
                {
                    "fa": "راننده‌ی تاکسی گفت: بفرمایید. — مسافر گفت: قابلی ندارد.",
                    "reading_az": "Ranəndeye taksi goft: bəfərmayid. — Mosafer goft: qabeli nədarəd.",
                    "az": "Taksi sürücüsü dedi: buyurun (pulu alın). Sərnişin dedi: dəyməz (təvazökarlıq).",
                },
            ],
            "drills": [
                {
                    "title_fa": "مانند مثال بگویید",
                    "instruction_az": '«بفرمایید» ilə uyğun cümlə deyin (bütün bu vəziyyətlərdə eyni söz işlənir):',
                    "items": [
                        {
                            "prompt_fa": "میزبان یک لیوان چای به مهمان می‌دهد.",
                            "answer_fa": "بفرمایید.",
                            "reading_az": "Bəfərmayid.",
                            "az": "Buyurun.",
                        },
                        {
                            "prompt_fa": "منشی به بیمار اجازه‌ی ورود به مطب می‌دهد.",
                            "answer_fa": "سلام، بفرمایید.",
                            "reading_az": "Səlam, bəfərmayid.",
                            "az": "Salam, buyurun.",
                        },
                        {
                            "prompt_fa": "راننده‌ی تاکسی پول را از مسافر می‌گیرد و به او می‌دهد.",
                            "answer_fa": "بفرمایید.",
                            "reading_az": "Bəfərmayid.",
                            "az": "Buyurun.",
                        },
                        {
                            "prompt_fa": "شما در آسانسور به فرد مسن‌تر جا می‌دهید.",
                            "answer_fa": "بفرمایید.",
                            "reading_az": "Bəfərmayid.",
                            "az": "Buyurun.",
                        },
                    ],
                },
            ],
        },
        {
            "title_az": "«… زدن» quruluşu — geniş mənalı «vurmaq/etmək» feli",
            "title_fa": "«....... زدن»",
            "explanation_az": (
                "«زدن» (vurmaq) feli isimlə birləşib tamamilə yeni məna verir.\n"
                "لبخند زدن (gülümsəmək), حرف زدن (danışmaq), زنگ زدن (zəng etmək), اتو زدن (ütüləmək).\n"
                "Mənanı sözbəsöz yox, birləşmə kimi bütöv öyrənmək lazımdır.\n"
                "Səh. 236-dakı sxemdə «زدن» ilə birləşən 14 söz var: لبخند، شانه، کِرِم، اتو، در، زنگ،\n"
                "تلفن، حرف، دست، به‌هم، رنگ، آمپول، دور، سوت."
            ),
            # Səh. 237, 1-ci haşiyə qeydi.
            "note_fa": "در زبان گفتار به جای مصدر «تلفن زدن»، از «زنگ زدن» هم استفاده می‌شود: از خانه به محل کار دوستم زنگ زدم.",
            "note_reading_az": "Dər zəbane goftar be caye məsdəre «telefon zədən», əz «zəng zədən» həm estefade mişəvəd: əz xane be məhəlle kare dustəm zəng zadəm.",
            "note_az": (
                "Danışıq dilində «تلفن زدن» (telefon etmək) əvəzinə «زنگ زدن» də işlədilir:\n"
                "«Evdən dostumun iş yerinə zəng vurdum.»"
            ),
            # Səh. 237, 2-ci haşiyə qeydi.
            "note2_fa": "در زبان گفتار «به هم زدن» را «هم زدن» می‌گوییم: من با قاشق، چای را هم زدم.",
            "note2_reading_az": "Dər zəbane goftar «be həm zədən» ra «həm zədən» miguyim: mən ba qaşoq, çay ra həm zadəm.",
            "note2_az": (
                "Danışıq dilində «به هم زدن» (qarışdırmaq) qısaldılıb «هم زدن» deyilir:\n"
                "«Mən qaşıqla çayı qarışdırdım.»"
            ),
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
                {
                    "fa": "«زدن» feli fərqli isimlərlə birləşərək çoxlu müxtəlif mənalar yaradır — mənanı isimlə birlikdə öyrənmək lazımdır.",
                    "az": "«زدن» (vurmaq) feli özündən əvvəlki isimlə birləşərək tamamilə fərqli mənalar bildirir.",
                },
                {
                    "fa": "پدربزرگ و مادربزرگ هنگام دیدن ما خوش‌حال می‌شوند و لبخند می‌زنند.",
                    "reading_az": "Pedərbozorg va madərbozorg hengame didəne ma xoşhal mişəvənd va ləbxənd mizənənd.",
                    "az": "Baba və nənə bizi görəndə şad olur və gülümsəyirlər.",
                },
                {
                    "fa": "قبل از رفتن به خانه‌ی دوستم، به او تلفن زدم؛ سپس به آن‌جا رفتم.",
                    "reading_az": "Qəbl əz rəftən be xane-ye dustəm, be u telefon zadəm; səpəs be anja rəftəm.",
                    "az": "Dostumun evinə getməzdən əvvəl ona telefon etdim; sonra oraya getdim.",
                },
                {
                    "fa": "وقتی به خانه‌ی حسین رسیدم، زنگ زدم و پدرش در را باز کرد.",
                    "reading_az": "Vəqti be xane-ye Hoseyn residəm, zəng zadəm va pedərəş dər ra baz kərd.",
                    "az": "Hüseynin evinə çatanda zəng vurdum və atası qapını açdı.",
                },
                {
                    "fa": "آیا شما قبل از رفتن به کلاس، موهایتان را شانه می‌زنید؟",
                    "reading_az": "Aya şoma qəbl əz rəftən be kelas, muhayetan ra şane mizənid?",
                    "az": "Siz sinfə getməzdən əvvəl saçınızı darayırsınızmı?",
                },
                {
                    "fa": "هفته‌ی قبل مریض بودم و سه تا آمپول زدم.",
                    "reading_az": "Həfteye qəbl mariz budəm va se ta ampul zadəm.",
                    "az": "Keçən həftə xəstə idim və üç dəfə iynə vurdurdum.",
                },
                {
                    "fa": "ما قبل از وارد شدن به اتاق مدیر، در می‌زنیم؛ سپس وارد می‌شویم.",
                    "reading_az": "Ma qəbl əz vared-şodən be otaqe modir, dər mizənim; səpəs vared mişəvim.",
                    "az": "Biz müdirin otağına girməzdən əvvəl qapını döyürük; sonra giririk.",
                },
                {
                    "fa": "یکی از دوستانم زیاد حرف می‌زند. من زیاد حرف زدن را دوست ندارم.",
                    "reading_az": "Yeki əz dustanəm ziyad hərf mizənəd. Mən ziyad hərf-zadən ra dust nədaram.",
                    "az": "Dostlarımdan biri çox danışır. Mən çox danışmağı sevmirəm.",
                },
                {
                    "fa": "پلیس گفت: این خیابان، ورود ممنوع است؛ دور بزنید و از آن خیابان بروید.",
                    "reading_az": "Polis goft: in xiyaban, vorud məmnu əst; dor bezənid va əz an xiyaban bəravid.",
                    "az": "Polis dedi: bu küçəyə giriş qadağandır; geri dönün və o küçədən gedin.",
                },
                {
                    "fa": "در هوای آفتابی، هنگام بیرون رفتن از خانه به دست‌ها و صورتم کِرِم می‌زنم.",
                    "reading_az": "Dər havaye aftabi, hengame birun-rəftən əz xane be dəstha va suratəm kerem mizənəm.",
                    "az": "Günəşli havada evdən çıxarkən əllərimə və üzümə krem sürtürəm.",
                },
                {
                    "fa": "هر روز هنگام خوردن صبحانه، شکر را در چای می‌ریزم و با قاشق آن را به هم می‌زنم.",
                    "reading_az": "Hər ruz hengame xordəne səbhane, şekər ra dər çay mirizəm va ba qaşoq an ra be həm mizənəm.",
                    "az": "Hər gün səhər yeməyi zamanı şəkəri çaya tökürəm və qaşıqla qarışdırıram.",
                },
            ],
        },
        {
            "title_az": "Şəmsi tarixin yazılışı və oxunuşu",
            "title_fa": "نوشتن و خواندن «تاریخ»",
            "explanation_az": (
                "Tarix belə oxunur: gün (sıra sayı) + ay + il.\n"
                "۱۳۹۱/۷/۴ — «چهارمِ مهرِ هزار و سیصد و نود و یک».\n"
                "Yazıda ardıcıllıq il/ay/gün olur, oxunuş isə gündən başlayır; sözlər izafə (kəsrə) ilə bağlanır.\n"
                "Səh. 238-dəki üç variantdan ikisi də doğrudur:\n"
                "«چهارِ مهرِ …» və «چهارمِ مهرِ …»; amma ayı RƏQƏMLƏ demək («چهارِ هفتِ …») YANLIŞdır.\n"
                "Şəmsi ayların sırası: ۱ فروردین، ۲ اردیبهشت، ۳ خرداد، ۴ تیر، ۵ مرداد، ۶ شهریور،\n"
                "۷ مهر، ۸ آبان، ۹ آذر، ۱۰ دی، ۱۱ بهمن، ۱۲ اسفند."
            ),
            # Səh. 238 haşiyə qeydi (səhv variant).
            "note_fa": "«چهارم هفتِ هزار و سیصد و نود و یک» ✗",
            "note_reading_az": "«Çəharome həfte hezar va sisəd va nəvad va yek» ✗",
            "note_az": (
                "Ayı rəqəm adı ilə demək olmaz: «چهارم هفتِ …» YANLIŞdır.\n"
                "Düzgünü ay adı ilədir: «چهارمِ مهرِ …»."
            ),
            # Səh. 239 haşiyə qeydi (danışıq dilində qısaltma).
            "note2_fa": "در زبان گفتار «سالِ هزار و سیصد و نود و یک» را برای اختصار «سالِ نود و یک» هم می‌گوییم.",
            "note2_reading_az": "Dər zəbane goftar «sale hezar va sisəd va nəvad va yek» ra bəraye extesar «sale nəvad va yek» həm miguyim.",
            "note2_az": (
                "Danışıqda il qısaldılır: «سالِ هزار و سیصد و نود و یک» əvəzinə\n"
                "sadəcə «سالِ نود و یک» (91-ci il) deyilir."
            ),
            "conjugations": [
                {"pronoun_fa": "۱۳۹۱/۷/۴", "form_fa": "چهارمِ مهر، هزار و سیصد و نود و یک"},
                {"pronoun_fa": "گün + Ay + İl", "form_fa": "روز + مِ/ + ماه + ِ + هزار و ..."},
            ],
            "examples": [
                {
                    "fa": "تاریخ به این شکل خوانده می‌شود: روزِ عدد + ماه + سال. مثلاً ۱۳۹۲/۵/۱۲ = دوازدهِ مردادِ هزار و سیصد و نود و دو.",
                    "reading_az": "Tarix be in şekl xandə mişəvəd: ruze ədəd + mah + sal. Məsələn 1392/5/12 = dəvazdəhe mordade hezar va sisəd va nəvad va do.",
                    "az": "Tarix belə oxunur: gün + ay + il, məsələn 12 Mordad 1392.",
                },
                {
                    "fa": "امام خمینی (ره) در چهاردهم خردادِ هزار و سیصد و شصت و هشت از دنیا رفت.",
                    "reading_az": "Emam Xomeyni dər çəhardəhome xordade hezar va sisəd va şəst va həşt əz donya rəft.",
                    "az": "İmam Xomeyni 1368-ci il Xordad ayının 14-də (1989) vəfat etdi.",
                },
                {
                    "fa": "من در دوازدهم فروردینِ هزار و سیصد و پنجاه و هشت به دنیا آمدم.",
                    "reading_az": "Mən dər dəvazdəhome fərvərdine hezar va sisəd va pənjah va həşt be donya amədəm.",
                    "az": "Mən 1358-ci il Fərvərdin ayının 12-də anadan olmuşam.",
                },
                {
                    "fa": "تاریخ تولّد شما چیست؟ تاریخ تولّد من، بیست و دوم بهمنِ هزار و سیصد و پنجاه و هفت است.",
                    "reading_az": "Tarixe touləde şoma çist? Tarixe touləde mən, bist o dovvome bəhməne hezar va sisəd va pənjah va həft əst.",
                    "az": "Doğum tarixiniz nədir? Mənim doğum tarixim 1357-ci il Bəhmən ayının 22-sidir.",
                },
                {
                    "fa": "دومِ خردادِ هزار و سیصد و پنجاه و شش.",
                    "reading_az": "Dovome xordade hezar va sisəd va pənjah va şeş.",
                    "az": "1356-cı il Xordad ayının 2-si.",
                },
                {
                    "fa": "هشتمِ تیرِ هزار و سیصد و هفتاد و هشت.",
                    "reading_az": "Həştome tire hezar va sisəd va həftad va həşt.",
                    "az": "1378-ci il Tir ayının 8-i.",
                },
                {
                    "fa": "پانزدهمِ شهریورِ هزار و سیصد و هشتاد.",
                    "reading_az": "Panzdəhome şəhrivare hezar va sisəd va həştad.",
                    "az": "1380-ci il Şəhrivər ayının 15-i.",
                },
                {
                    "fa": "سی و یکمِ مردادِ هزار و سیصد و هشتاد و هشت.",
                    "reading_az": "Si-yo yekome mordade hezar va sisəd va həştad va həşt.",
                    "az": "1388-ci il Mordad ayının 31-i.",
                },
                {
                    "fa": "هفدهمِ آبانِ هزار و سیصد و نود و دو.",
                    "reading_az": "Hefdahome abane hezar va sisəd va nəvad va do.",
                    "az": "1392-ci il Aban ayının 17-si.",
                },
            ],
            "drills": [
                {
                    "title_fa": "مانند مثال بخوانید",
                    "instruction_az": 'Nümunə kimi tarixi tam formada oxuyun: "۱۳۹۲/۵/۱۲ → تاریخ تولّد من، دوازدهمِ مردادِ هزار و سیصد و نود و دو است."',
                    "items": [
                        {
                            "prompt_fa": "۱۳۷۶/۵/۸",
                            "answer_fa": "تاریخ تولّد من، هشتمِ مردادِ هزار و سیصد و هفتاد و شش است.",
                            "reading_az": "Tarixe touləde mən, həştome mordade hezar va sisəd va həftad va şeş əst.",
                            "az": "Mənim doğum tarixim 1376-cı il Mordad ayının 8-idir.",
                        },
                        {
                            "prompt_fa": "۱۳۸۵/۱۲/۲۹",
                            "answer_fa": "تاریخ تولّد من، بیست و نهمِ اسفندِ هزار و سیصد و هشتاد و پنج است.",
                            "reading_az": "Tarixe touləde mən, bist o nohome esfənde hezar va sisəd va həştad va pənc əst.",
                            "az": "Mənim doğum tarixim 1385-ci il Esfənd ayının 29-udur.",
                        },
                        {
                            "prompt_fa": "۱۳۶۱/۴/۷",
                            "answer_fa": "تاریخ تولّد من، هفتمِ تیرِ هزار و سیصد و شصت و یک است.",
                            "reading_az": "Tarixe touləde mən, həftome tire hezar va sisəd va şəst va yek əst.",
                            "az": "Mənim doğum tarixim 1361-ci il Tir ayının 7-sidir.",
                        },
                        {
                            "prompt_fa": "۱۳۹۲/۷/۱۳",
                            "answer_fa": "تاریخ تولّد من، سیزدهمِ مهرِ هزار و سیصد و نود و دو است.",
                            "reading_az": "Tarixe touləde mən, sizdəhome mehre hezar va sisəd va nəvad va do əst.",
                            "az": "Mənim doğum tarixim 1392-ci il Mehr ayının 13-üdür.",
                        },
                        {
                            "prompt_fa": "۱۳۴۴/۲/۳۰",
                            "answer_fa": "تاریخ تولّد من، سی‌امِ اردیبهشتِ هزار و سیصد و چهل و چهار است.",
                            "reading_az": "Tarixe touləde mən, siome ordibeheşte hezar va sisəd va çehel va çəhar əst.",
                            "az": "Mənim doğum tarixim 1344-cü il Ordibeheşt ayının 30-udur.",
                        },
                        {
                            "prompt_fa": "۱۳۸۹/۹/۲۷",
                            "answer_fa": "تاریخ تولّد من، بیست و هفتمِ آذرِ هزار و سیصد و هشتاد و نه است.",
                            "reading_az": "Tarixe touləde mən, bist o həftome azare hezar va sisəd va həştad va noh əst.",
                            "az": "Mənim doğum tarixim 1389-cu il Azər ayının 27-sidir.",
                        },
                    ],
                },
            ],
        },
        {
            # Səh. 234 «لطفاً جایگزین کنید» qəlibi + səhifə altındakı sərlövhəli cədvəl.
            "title_az": "«MÜDDƏT + است + … درد دارم» — nə vaxtdan bəri ağrıyır",
            "title_fa": "«... است ... درد دارم»",
            "explanation_az": (
                "Bir ağrının nə vaxtdan davam etdiyini iki cür demək olar:\n"
                "1) Uzun forma: «من دو روز است دندانم درد می‌کند» — «İki gündür dişim ağrıyır».\n"
                "2) Qısa forma: «من دو روز است دندان‌درد دارم» — orqan adı + درد birləşib İSİM olur.\n"
                "Qəlib: SUBYEKT + MÜDDƏT + است + ORQAN-درد + دارم/دارد/داریم.\n"
                "Diqqət: «است» müddətdən sonra gəlir və şəxsə görə dəyişmir.\n"
                "Orqan adları birləşəndə: سر → سردرد، دندان → دندان‌درد، دل → دل‌درد،\n"
                "کمر → کمردرد، پا → پادرد، چشم → چشم‌درد، گوش → گوش‌درد."
            ),
            "conjugations": [
                {"pronoun_fa": "من دو روز است دندانم درد می‌کند.", "form_fa": "= من دو روز است دندان‌درد دارم."},
                {"pronoun_fa": "او یک هفته است سرش درد می‌کند.", "form_fa": "= او یک هفته است سردرد دارد."},
                {"pronoun_fa": "ما یک سال است چشممان درد می‌کند.", "form_fa": "= ما یک سال است چشم‌درد داریم."},
                # Səh. 234 altındakı fel cədvəli: «سرما خوردن».
                {"pronoun_fa": "سرما خوردن", "form_fa": "سرما می‌خورم / می‌خوری / می‌خورد / می‌خوریم / می‌خورید / می‌خورند"},
                # Səh. 234 altındakı fel cədvəli: «آمپول زدن».
                {"pronoun_fa": "آمپول زدن", "form_fa": "آمپول می‌زنم / می‌زنی / می‌زند / می‌زنیم / می‌زنید / می‌زنند"},
            ],
            "examples": [
                {
                    "fa": "من دو روز است دندانم درد می‌کند. = من دو روز است دندان‌درد دارم.",
                    "reading_az": "Mən do ruz əst dəndanəm dərd mikonəd. = Mən do ruz əst dəndandərd darəm.",
                    "az": "İki gündür dişim ağrıyır. = İki gündür diş ağrım var.",
                },
                {
                    "fa": "فرزندم چهار ساعت است سرش درد می‌کند.",
                    "reading_az": "Fərzəndəm çəhar saət əst sərəş dərd mikonəd.",
                    "az": "Övladımın dörd saatdır ki, başı ağrıyır.",
                },
                {
                    "fa": "من دیروز سرما خوردم و امروز تب دارم.",
                    "reading_az": "Mən diruz sərma xordəm va əmruz təb darəm.",
                    "az": "Mən dünən soyuqladım və bu gün qızdırmam var.",
                },
                {
                    "fa": "پرستار زخم بیمار را پانسمان می‌کند و پزشک بیمار را جرّاحی می‌کند.",
                    "reading_az": "Pərəstar zəxme bimar ra pansman mikonəd va pezeşk bimar ra cərrahi mikonəd.",
                    "az": "Tibb bacısı xəstənin yarasına sarğı qoyur, həkim isə xəstəni əməliyyat edir.",
                },
            ],
            # Səh. 234 haşiyə qeydi.
            "note_fa": "به خاطرِ = به سببِ",
            "note_reading_az": "Be xatere = be səbəbe",
            "note_az": (
                "«به خاطرِ» səbəb bildirir və «به سببِ» ilə eyni mənadadır: «…-a görə».\n"
                "Nümunə: من به خاطرِ چشم‌درد به بیمارستان می‌روم — «Mən göz ağrısına görə xəstəxanaya gedirəm.»"
            ),
            "drills": [
                {
                    # Səh. 234 «لطفاً جایگزین کنید» — dərslikdəki 4 bənd.
                    "title_fa": "لطفاً جایگزین کنید",
                    "instruction_az": "Nümunə kimi qısa formaya çevirin: «من / دو روز / دندان → من دو روز است دندان‌درد دارم.»",
                    "example_prompt_fa": "من / دو روز / دندان",
                    "example_answer_fa": "من دو روز است دندانم درد می‌کند : من دو روز است دندان‌درد دارم.",
                    "example_reading_az": "Mən do ruz əst dəndanəm dərd mikonəd : Mən do ruz əst dəndandərd darəm.",
                    "example_az": "İki gündür dişim ağrıyır : İki gündür diş ağrım var.",
                    "items": [
                        {
                            "prompt_fa": "فرزندم / چهار ساعت / سر",
                            "answer_fa": "فرزندم چهار ساعت است سردرد دارد.",
                            "reading_az": "Fərzəndəm çəhar saət əst sərdərd darəd.",
                            "az": "Övladımın dörd saatdır ki, başı ağrıyır.",
                        },
                        {
                            "prompt_fa": "پدربزرگمان / یک ماه / پا",
                            "answer_fa": "پدربزرگمان یک ماه است پادرد دارد.",
                            "reading_az": "Pedərbozorgeman yek mah əst padərd darəd.",
                            "az": "Babamızın bir aydır ki, ayağı ağrıyır.",
                        },
                        {
                            "prompt_fa": "ابراهیم / یک هفته / کمر",
                            "answer_fa": "ابراهیم یک هفته است کمردرد دارد.",
                            "reading_az": "Ebrahim yek həfte əst kəmərdərd darəd.",
                            "az": "İbrahimin bir həftədir ki, beli ağrıyır.",
                        },
                        {
                            "prompt_fa": "ما / یک سال / چشم",
                            "answer_fa": "ما یک سال است چشم‌درد داریم.",
                            "reading_az": "Ma yek sal əst çeşmdərd darim.",
                            "az": "Bizim bir ildir ki, gözümüz ağrıyır.",
                        },
                    ],
                },
            ],
        },
        {
            # Səh. 240-242 haşiyə qeydləri: hansı fel hansı ön qoşmanı istəyir.
            "title_az": "«را دوست دارد» / «به … علاقه دارد» / «به … تخفیف می‌دهد»",
            "title_fa": "«... را دوست دارد» ؛ «به ... علاقه دارد»",
            "explanation_az": (
                "Bu üç ifadə eyni mənaya yaxındır, amma FƏRQLİ qoşma tələb edir — qarışdırmaq olmaz:\n"
                "• «… را دوست دارد» — obyekt «را» ilə: او بچّه‌ها را دوست دارد.\n"
                "• «به … علاقه دارد» — obyekt «به» ilə: کودکان به او علاقه دارند.\n"
                "• «به … تخفیف می‌دهد» — kimə endirim verilirsə «به» ilə: به خانواده‌های فقیر تخفیف می‌دهد.\n"
                "• «از … پول نمی‌گیرد» — kimdən pul alınırsa «از» ilə: از خانواده‌های فقیر پول نمی‌گیرد.\n"
                "Yadda saxla: دوست داشتن → را ; علاقه داشتن → به ; تخفیف دادن → به ; گرفتن → از."
            ),
            "conjugations": [
                {"pronoun_fa": "دوست داشتن", "form_fa": "... را دوست دارد"},
                {"pronoun_fa": "علاقه داشتن", "form_fa": "به ... علاقه دارد"},
                {"pronoun_fa": "تخفیف دادن", "form_fa": "به ... تخفیف می‌دهد"},
                {"pronoun_fa": "پول گرفتن", "form_fa": "از ... پول می‌گیرد"},
            ],
            "examples": [
                {
                    "fa": "او بچّه‌ها را مانند فرزندانش دوست دارد.",
                    "reading_az": "U bəççeha ra manənde fərzəndanəş dust darəd.",
                    "az": "O, uşaqları öz övladları kimi sevir. — «دوست داشتن» «را» istəyir.",
                },
                {
                    "fa": "کودکان هم به او بسیار علاقه دارند.",
                    "reading_az": "Kudəkan həm be u besyar əlaqe darənd.",
                    "az": "Uşaqlar da onu çox sevirlər. — «علاقه داشتن» «به» istəyir.",
                },
                {
                    "fa": "ایشان به خانواده‌های فقیر بسیار تخفیف می‌دهد.",
                    "reading_az": "İşan be xanevadehaye fəqir besyar təxfif midəhəd.",
                    "az": "O, kasıb ailələrə çox endirim edir. — «تخفیف دادن» «به» istəyir.",
                },
                {
                    "fa": "ایشان از خانواده‌های فقیر، پول ویزیت و جرّاحی نمی‌گیرد.",
                    "reading_az": "İşan əz xanevadehaye fəqir, pule vizit va cərrahi nemigirəd.",
                    "az": "O, kasıb ailələrdən müayinə və əməliyyat pulu almır. — «گرفتن» «از» istəyir.",
                },
                {
                    "fa": "فروشنده‌ی پوشاک به خانواده‌های فقیر تخفیف می‌دهد.",
                    "reading_az": "Foruşəndeye puşak be xanevadehaye fəqir təxfif midəhəd.",
                    "az": "Geyim satıcısı kasıb ailələrə endirim edir.",
                },
            ],
            "note_fa": "......... را دوست دارد. — به ......... علاقه دارد. — به ......... تخفیف می‌دهد.",
            "note_reading_az": "… ra dust darəd. — Be … əlaqe darəd. — Be … təxfif midəhəd.",
            "note_az": (
                "Dərslikdəki üç qəlib qutusu (səh. 240 və 241):\n"
                "«… را دوست دارد» / «به … علاقه دارد» / «به … تخفیف می‌دهد»."
            ),
            "drills": [
                {
                    "title_fa": "قسمت خالی را کامل کنید",
                    "instruction_az": "Uyğun qoşmanı («را» / «به» / «از») seçib deyin.",
                    "items": [
                        {
                            "prompt_fa": "بچّه‌ها پدر و مادرشان ......... بسیار دوست دارند.",
                            "answer_fa": "بچّه‌ها پدر و مادرشان را بسیار دوست دارند.",
                            "reading_az": "Bəççeha pedər va madərəşan ra besyar dust darənd.",
                            "az": "Uşaqlar ata-analarını çox sevirlər. — دوست داشتن → را",
                        },
                        {
                            "prompt_fa": "کودکان بیمار ......... سمیّه‌خانم بسیار علاقه دارند.",
                            "answer_fa": "کودکان بیمار به سمیّه‌خانم بسیار علاقه دارند.",
                            "reading_az": "Kudəkane bimar be Səmiyye-xanom besyar əlaqe darənd.",
                            "az": "Xəstə uşaqlar Səmiyyə xanımı çox sevirlər. — علاقه داشتن → به",
                        },
                        {
                            "prompt_fa": "پدر سمیّه ......... خانواده‌های فقیر تخفیف می‌دهد.",
                            "answer_fa": "پدر سمیّه به خانواده‌های فقیر تخفیف می‌دهد.",
                            "reading_az": "Pedəre Səmiyye be xanevadehaye fəqir təxfif midəhəd.",
                            "az": "Səmiyyənin atası kasıb ailələrə endirim edir. — تخفیف دادن → به",
                        },
                        {
                            "prompt_fa": "او ......... خانواده‌های فقیر پول ویزیت نمی‌گیرد.",
                            "answer_fa": "او از خانواده‌های فقیر پول ویزیت نمی‌گیرد.",
                            "reading_az": "U əz xanevadehaye fəqir pule vizit nemigirəd.",
                            "az": "O, kasıb ailələrdən müayinə pulu almır. — گرفتن → از",
                        },
                    ],
                },
            ],
        },
    ],
    "exercises": [
        {
            # Çalışma 1 — səh. 237 «لطفاً بخوانید» cümlələri əsasında hazırlanmış boşluq doldurma.
            "kind": "fill_blank",
            "instruction_az": "«… زدن» birləşmələrindən uyğun olanı yazın.",
            "word_bank": ["لبخند می‌زنند", "تلفن زدم", "زنگ زدم", "آمپول زدم", "دور بزنید"],
            "items": [
                {
                    "fa_with_blank": "پدربزرگ و مادربزرگ هنگام دیدن ما خوش‌حال می‌شوند و ___ .",
                    "correct_answer": "لبخند می‌زنند",
                    "reading_az": "ləbxənd mizənənd",
                    "az": "gülümsəyirlər",
                    "full_reading_az": "Pedərbozorg va madərbozorg hengame didəne ma xoşhal mişəvənd va ləbxənd mizənənd.",
                    "full_translation_az": "Baba və nənə bizi görəndə şad olur və gülümsəyirlər.",
                },
                {
                    "fa_with_blank": "قبل از رفتن به خانه‌ی دوستم، به او ___ ؛ سپس به آن‌جا رفتم.",
                    "correct_answer": "تلفن زدم",
                    "reading_az": "telefon zadəm",
                    "az": "telefon etdim",
                    "full_reading_az": "Qəbl əz rəftən be xane-ye dustəm, be u telefon zadəm; səpəs be anja rəftəm.",
                    "full_translation_az": "Dostumun evinə getməzdən əvvəl ona telefon etdim; sonra oraya getdim.",
                },
                {
                    "fa_with_blank": "وقتی به خانه‌ی حسین رسیدم، ___ و پدرش در را باز کرد.",
                    "correct_answer": "زنگ زدم",
                    "reading_az": "zəng zadəm",
                    "az": "zəng vurdum",
                    "full_reading_az": "Vəqti be xane-ye Hoseyn residəm, zəng zadəm va pedərəş dər ra baz kərd.",
                    "full_translation_az": "Hüseynin evinə çatanda zəng vurdum və atası qapını açdı.",
                },
                {
                    "fa_with_blank": "هفته‌ی قبل مریض بودم و سه تا ___ .",
                    "correct_answer": "آمپول زدم",
                    "reading_az": "ampul zadəm",
                    "az": "iynə vurdurdum",
                    "full_reading_az": "Həfteye qəbl mariz budəm va se ta ampul zadəm.",
                    "full_translation_az": "Keçən həftə xəstə idim və üç dəfə iynə vurdurdum.",
                },
                {
                    "fa_with_blank": "پلیس گفت: این خیابان، ورود ممنوع است؛ ___ و از آن خیابان بروید.",
                    "correct_answer": "دور بزنید",
                    "reading_az": "dor bezənid",
                    "az": "geri dönün",
                    "full_reading_az": "Polis goft: in xiyaban, vorud məmnu əst; dor bezənid va əz an xiyaban bəravid.",
                    "full_translation_az": "Polis dedi: bu küçəyə giriş qadağandır; geri dönün və o küçədən gedin.",
                },
            ],
        },
        {
            # Çalışma 2 — səh. 238 «نوشتن و خواندن تاریخ» qutusu əsasında boşluq doldurma.
            "kind": "fill_blank",
            "instruction_az": "Tarixi düzgün oxuyaraq yazın (nümunə əsasında).",
            "word_bank": ["دوازدهِ", "چهاردهِ", "بیست و دوم", "چهارمِ"],
            "items": [
                {
                    "fa_with_blank": "۱۳۹۱/۷/۴ = ___ مهرِ هزار و سیصد و نود و یک",
                    "correct_answer": "چهارمِ",
                    "reading_az": "çəharome",
                    "az": "dördüncü",
                    "full_reading_az": "Çəharome mehre hezar va sisəd va nəvad va yek.",
                    "full_translation_az": "1391-ci il Mehr ayının 4-ü.",
                },
                {
                    "fa_with_blank": "۱۳۹۲/۵/۱۲ = ___ مردادِ هزار و سیصد و نود و دو",
                    "correct_answer": "دوازدهِ",
                    "reading_az": "dəvazdəhe",
                    "az": "on iki",
                    "full_reading_az": "Dəvazdəhe mordade hezar va sisəd va nəvad va do.",
                    "full_translation_az": "1392-ci il Mordad ayının 12-si.",
                },
                {
                    "fa_with_blank": "۱۳۶۸/۳/۱۴ = ___ خردادِ هزار و سیصد و شصت و هشت",
                    "correct_answer": "چهاردهِ",
                    "reading_az": "çəhardəhe",
                    "az": "on dörd",
                    "full_reading_az": "Çəhardəhe xordade hezar va sisəd va şəst va həşt.",
                    "full_translation_az": "1368-ci il Xordad ayının 14-ü.",
                },
                {
                    "fa_with_blank": "۱۳۵۷/۱۱/۲۲ = ___ بهمنِ هزار و سیصد و پنجاه و هفت",
                    "correct_answer": "بیست و دوم",
                    "reading_az": "bist o dovvom",
                    "az": "iyirmi ikinci",
                    "full_reading_az": "Bist o dovvome bəhməne hezar va sisəd va pənjah va həft.",
                    "full_translation_az": "1357-ci il Bəhmən ayının 22-si.",
                },
            ],
        },
        {
            # Çalışma 3 — səh. 234 «لطفاً جایگزین کنید»; dərslikdə 4 bənd var.
            "kind": "practice_reveal",
            "title_fa": "لطفاً جایگزین کنید",
            "instruction_az": "Nümunə kimi əvəz edin: «من دو روز است دندانم درد می‌کند = من دو روز است دندان‌درد دارم.»",
            "example_prompt_fa": "من / دو روز / دندان",
            "example_answer_fa": "من دو روز است دندانم درد می‌کند : من دو روز است دندان‌درد دارم.",
            "example_reading_az": "Mən do ruz əst dəndanəm dərd mikonəd : Mən do ruz əst dəndandərd darəm.",
            "example_az": (
                "Verilən sözlər: SUBYEKT / MÜDDƏT / ORQAN.\n"
                "Qəlib: SUBYEKT + MÜDDƏT + است + ORQAN-درد + دارم/دارد/داریم.\n"
                "Tərcümə: İki gündür diş ağrım var."
            ),
            "items": [
                {
                    "prompt_fa": "فرزندم / چهار ساعت / سر",
                    "answer_fa": "فرزندم چهار ساعت است سردرد دارد.",
                    "reading_az": "Fərzəndəm çəhar saət əst sərdərd darəd.",
                    "az": "Övladımın dörd saatdır ki, başı ağrıyır. (سر + درد = سردرد)",
                },
                {
                    "prompt_fa": "پدربزرگمان / یک ماه / پا",
                    "answer_fa": "پدربزرگمان یک ماه است پادرد دارد.",
                    "reading_az": "Pedərbozorgeman yek mah əst padərd darəd.",
                    "az": "Babamızın bir aydır ki, ayağı ağrıyır. (پا + درد = پادرد)",
                },
                {
                    "prompt_fa": "ابراهیم / یک هفته / کمر",
                    "answer_fa": "ابراهیم یک هفته است کمردرد دارد.",
                    "reading_az": "Ebrahim yek həfte əst kəmərdərd darəd.",
                    "az": "İbrahimin bir həftədir ki, beli ağrıyır. (کمر + درد = کمردرد)",
                },
                {
                    "prompt_fa": "ما / یک سال / چشم",
                    "answer_fa": "ما یک سال است چشم‌درد داریم.",
                    "reading_az": "Ma yek sal əst çeşmdərd darim.",
                    "az": "Bizim bir ildir ki, gözümüz ağrıyır. (چشم + درد = چشم‌درد)",
                },
            ],
        },
        {
            # Çalışma 4 — səh. 235 «لطفاً توجّه کنید — بفرمایید»; dərslikdə 8 şəkilli vəziyyət var.
            "kind": "answer_question",
            "title_fa": "بفرمایید",
            "instruction_az": "Vəziyyətə uyğun «بفرمایید» ilə qısa cavab deyin (dərslikdəki 8 şəkil).",
            "example_fa": "میزبان چای را به مهمان می‌دهد. ← بفرمایید.",
            "example_reading_az": "Mizban çay ra be mehman midəhəd. — Bəfərmayid.",
            "example_az": (
                "Ev sahibi qonağa çay verir. — Buyurun.\n"
                "«بفرمایید» bütün bu vəziyyətlərdə eynidir, amma Azərbaycan dilinə\n"
                "hər dəfə başqa cür tərcümə olunur: buyurun, alın, keçin, oturun."
            ),
            "note_fa": "بفرما (خودمانی) — بفرمایید (محترمانه)",
            "note_reading_az": "Bəfərma (xodəmani) — bəfərmayid (mohtərəmane)",
            "note_az": "Samimi (sən) forması «بفرما», nəzakətli (siz) forması «بفرمایید»dir.",
            "items": [
                {"fa": "کودکان به خانمِ میزبان هدیه می‌دهند.", "reading_az": "Kudəkan be xanome mizban hədiye midəhənd.", "az": "Uşaqlar ev sahibi xanıma hədiyyə verirlər.", "sample_answer_fa": "بفرمایید. — دستِ شما درد نکنه.", "sample_answer_reading_az": "Bəfərmayid. — Dəste şoma dərd nəkone.", "sample_answer_az": "Buyurun, alın. — Əliniz ağrımasın (təşəkkür)."},
                {"fa": "میزبان سرِ سفره از مهمان‌ها پذیرایی می‌کند.", "reading_az": "Mizban səre sofre əz mehmanha pəzirayi mikonəd.", "az": "Ev sahibi süfrə başında qonaqları ağırlayır.", "sample_answer_fa": "بفرمایید. — چشم، خیلی ممنون.", "sample_answer_reading_az": "Bəfərmayid. — Çeşm, xeyli məmnun.", "sample_answer_az": "Buyurun (yeyin). — Baş üstə, çox sağ olun."},
                {"fa": "استاد به دانشجویان می‌گوید وارد کلاس شوند و بنشینند.", "reading_az": "Ostad be daneşcuyan miguyəd varede kelas şəvənd va beneşinənd.", "az": "Müəllim tələbələrə sinfə girib oturmağı deyir.", "sample_answer_fa": "بفرمایید.", "sample_answer_reading_az": "Bəfərmayid.", "sample_answer_az": "Buyurun, keçin (oturun)."},
                {"fa": "مسافر در اتوبوس جای خود را به فرد دیگری می‌دهد.", "reading_az": "Mosafer dər otobus caye xod ra be fərde digəri midəhəd.", "az": "Avtobusda sərnişin öz yerini başqasına verir.", "sample_answer_fa": "بفرمایید.", "sample_answer_reading_az": "Bəfərmayid.", "sample_answer_az": "Buyurun, oturun."},
                {"fa": "منشی تلفن را جواب می‌دهد.", "reading_az": "Mənşi telefon ra cəvab midəhəd.", "az": "Katibə telefona cavab verir.", "sample_answer_fa": "سلام، بفرمایید.", "sample_answer_reading_az": "Səlam, bəfərmayid.", "sample_answer_az": "Salam, buyurun (eşidirəm)."},
                {"fa": "منشیِ مطب به بیمار می‌گوید وارد اتاق دکتر شود.", "reading_az": "Mənşiye mətəb be bimar miguyəd varede otaqe doktor şəvəd.", "az": "Kabinetin katibəsi xəstəyə həkimin otağına girməsini deyir.", "sample_answer_fa": "بفرمایید. — متشکّرم.", "sample_answer_reading_az": "Bəfərmayid. — Motəşəkkerəm.", "sample_answer_az": "Buyurun, keçin. — Təşəkkür edirəm."},
                {"fa": "دو نفر جلوی درِ آسانسور به هم تعارف می‌کنند.", "reading_az": "Do nəfər celove dəre asansor be həm təarof mikonənd.", "az": "İki nəfər lift qapısının qabağında bir-birinə təklif edir.", "sample_answer_fa": "بفرمایید. — شما بفرمایید.", "sample_answer_reading_az": "Bəfərmayid. — Şoma bəfərmayid.", "sample_answer_az": "Buyurun (siz keçin). — Yox, siz buyurun."},
                {"fa": "مسافر پولِ تاکسی را به راننده می‌دهد.", "reading_az": "Mosafer pule taksi ra be ranənde midəhəd.", "az": "Sərnişin taksi pulunu sürücüyə verir.", "sample_answer_fa": "بفرمایید. — قابلی نداره.", "sample_answer_reading_az": "Bəfərmayid. — Qabeli nədare.", "sample_answer_az": "Buyurun (alın). — Dəyməz (təvazökarlıq — «قابل نیست»)."},
            ],
        },
        {
            # Çalışma 5 — səh. 237 «لطفاً کامل کنید»; dərslikdə 6 bənd var,
            # 5-ci bənddə İKİ boşluq olduğuna görə multi_blank quruluşu seçilib.
            "kind": "multi_blank",
            "title_fa": "لطفاً کامل کنید",
            "instruction_az": "«... زدن» birləşmələrinin çatışmayan hissəsini söz bankından seçin.",
            "example_fa": "من قبل از رفتن به کلاس، موهایم را ___ می‌زنم.\nمن قبل از رفتن به کلاس، موهایم را *شانه* می‌زنم.",
            "example_reading_az": "Mən qəbl əz rəftən be kelas, muhayəm ra şane mizənəm.",
            "example_az": (
                "Mən sinfə getməzdən əvvəl saçımı darayıram.\n"
                "«زدن» feli sabit qalır, dəyişən İSİM hissəsidir: شانه، رنگ، اتو، آمپول، زنگ، حرف، به هم."
            ),
            # 6 bənddə cəmi 7 boşluq → 7 çip.
            "word_bank": ["رنگ", "اتو", "آمپول", "زنگ", "زدم", "حرف", "به هم"],
            "items": [
                {
                    "fa_with_blanks": "رنگ‌کارها فردا دیوارهای مدرسه را ___ می‌زنند.",
                    "correct_answers": ["رنگ"],
                    "full_reading_az": "Rəngkarha fərda divarhaye mədrəse ra rəng mizənənd.",
                    "full_translation_az": "Rəngsazlar sabah məktəbin divarlarını rəngləyəcəklər. — رنگ زدن = rəngləmək.",
                },
                {
                    "fa_with_blanks": "پس از شستن لباس‌ها، پیراهنم را ___ می‌زنم.",
                    "correct_answers": ["اتو"],
                    "full_reading_az": "Pəs əz şostəne lebasha, pirahənəm ra otu mizənəm.",
                    "full_translation_az": "Paltarları yuduqdan sonra köynəyimi ütüləyirəm. — اتو زدن = ütüləmək.",
                },
                {
                    "fa_with_blanks": "دوستم علاوه‌بر خوردن کپسول و شربت، یک سرم و دو تا ___ زد.",
                    "correct_answers": ["آمپول"],
                    "full_reading_az": "Dustəm əlave bər xordəne kapsul va şərbət, yek serom va do ta ampul zad.",
                    "full_translation_az": "Dostum kapsul və şərbət içməklə yanaşı, bir serum və iki iynə də vurdurdu.",
                },
                {
                    "fa_with_blanks": "دیروز مریض بودم؛ دوستانم به من ___ زدند و حالم را پرسیدند.",
                    "correct_answers": ["زنگ"],
                    "full_reading_az": "Diruz mariz budəm; dustanəm be mən zəng zadənd va haləm ra porsidənd.",
                    "full_translation_az": "Dünən xəstə idim; dostlarım mənə zəng vurub halımı soruşdular. — «تلفن زدند» də olar.",
                },
                {
                    "fa_with_blanks": "دیشب به مادرم تلفن ___ و حدود نیم‌ساعت با او ___ زدم.",
                    "correct_answers": ["زدم", "حرف"],
                    "full_reading_az": "Dişəb be madərəm telefon zadəm va hodude nim-saət ba u hərf zadəm.",
                    "full_translation_az": "Dünən gecə anama telefon etdim və təxminən yarım saat onunla danışdım. — İki boşluq: تلفن زدن + حرف زدن.",
                },
                {
                    "fa_with_blanks": "امروز صبحانه، مقداری شکر در شیر ریختم و با قاشق آن را ___ زدم.",
                    "correct_answers": ["به هم"],
                    "full_reading_az": "Əmruz sobhane, məqdari şəkər dər şir rixtəm va ba qaşoq an ra be həm zadəm.",
                    "full_translation_az": "Bu gün səhər yeməyində südə bir az şəkər tökdüm və qaşıqla qarışdırdım. — به هم زدن = qarışdırmaq.",
                },
            ],
        },
        {
            # Çalışma 6 — səh. 238 «لطفاً بخوانید»; dərslikdəki 8 tarixin tam oxunuşu.
            "kind": "practice_reveal",
            "title_fa": "لطفاً بخوانید",
            "instruction_az": "Tarixləri tam formada (gün + ay adı + il) oxuyun.",
            "example_prompt_fa": "۱۳۹۱/۷/۴",
            "example_answer_fa": "چهارمِ مهرِ هزار و سیصد و نود و یک",
            "example_reading_az": "Çəharome mehre hezar va sisəd va nəvad va yek.",
            "example_az": "1391-ci il Mehr ayının 4-ü. — Ayı rəqəmlə demirik, ay ADI ilə deyirik.",
            "items": [
                {
                    "prompt_fa": "۱۳۶۸/۳/۱۴",
                    "answer_fa": "چهاردهِ خردادِ هزار و سیصد و شصت و هشت",
                    "reading_az": "Çəhardəhe xordade hezar va sisəd va şəst va həşt.",
                    "az": "1368-ci il Xordad ayının 14-ü. (3-cü ay = خرداد)",
                },
                {
                    "prompt_fa": "۱۳۵۶/۳/۲",
                    "answer_fa": "دومِ خردادِ هزار و سیصد و پنجاه و شش",
                    "reading_az": "Dovvome xordade hezar va sisəd va pəncah va şeş.",
                    "az": "1356-cı il Xordad ayının 2-si.",
                },
                {
                    "prompt_fa": "۱۳۷۸/۴/۸",
                    "answer_fa": "هشتمِ تیرِ هزار و سیصد و هفتاد و هشت",
                    "reading_az": "Həştome tire hezar va sisəd va həftad va həşt.",
                    "az": "1378-ci il Tir ayının 8-i. (4-cü ay = تیر)",
                },
                {
                    "prompt_fa": "۱۳۸۰/۶/۱۵",
                    "answer_fa": "پانزدهمِ شهریورِ هزار و سیصد و هشتاد",
                    "reading_az": "Panzdəhome şəhrivare hezar va sisəd va həştad.",
                    "az": "1380-ci il Şəhrivər ayının 15-i. (6-cı ay = شهریور)",
                },
                {
                    "prompt_fa": "۱۳۸۸/۵/۳۱",
                    "answer_fa": "سی و یکمِ مردادِ هزار و سیصد و هشتاد و هشت",
                    "reading_az": "Si-o-yekome mordade hezar va sisəd va həştad va həşt.",
                    "az": "1388-ci il Mordad ayının 31-i. (5-ci ay = مرداد)",
                },
                {
                    "prompt_fa": "۱۳۵۸/۱/۱۲",
                    "answer_fa": "دوازدهِ فروردینِ هزار و سیصد و پنجاه و هشت",
                    "reading_az": "Dəvazdəhe fərvərdine hezar va sisəd va pəncah va həşt.",
                    "az": "1358-ci il Fərvərdin ayının 12-si. (1-ci ay = فروردین)",
                },
                {
                    "prompt_fa": "۱۳۵۷/۱۱/۲۲",
                    "answer_fa": "بیست و دومِ بهمنِ هزار و سیصد و پنجاه و هفت",
                    "reading_az": "Bist-o-dovvome bəhməne hezar va sisəd va pəncah va həft.",
                    "az": "1357-ci il Bəhmən ayının 22-si — İran İnqilabının qələbə günü. (11-ci ay = بهمن)",
                },
                {
                    "prompt_fa": "۱۳۹۲/۸/۱۷",
                    "answer_fa": "هفدهمِ آبانِ هزار و سیصد و نود و دو",
                    "reading_az": "Hefdəhome abane hezar va sisəd va nəvad va do.",
                    "az": "1392-ci il Aban ayının 17-si. (8-ci ay = آبان)",
                },
            ],
        },
        {
            # Çalışma 7 — səh. 239 «جایگزین کنید»; dərslikdə 4 bənd var.
            "kind": "answer_question",
            "title_fa": "جایگزین کنید",
            "instruction_az": "Verilən sözlərdən tarixlə birlikdə tam cümlə qurun.",
            "example_fa": "آیت ا... خامنه‌ای / ۱۳۱۸/۴/۲۴ / مشهد / به دنیا آمدن ← آیت ا... خامنه‌ای *بیست‌وچهارم تیرِ* هزار و سیصد و هجده در مشهد به دنیا آمد.",
            "example_reading_az": "Ayətollah Xameneyi bist-o-çəharome tire hezar va sisəd va hicdəh dər Məşhəd be donya aməd.",
            "example_az": (
                "Verilən sözlər: ŞƏXS / TARİX / YER / MƏSDƏR.\n"
                "Qəlib: ŞƏXS + (در) TARİX + در YER + FEL (keçmiş zaman).\n"
                "Tarix mütləq sözlə oxunur: ۴ تیر → «بیست‌وچهارمِ تیرِ …».\n"
                "Tərcümə: Ayətullah Xameneyi 1318-ci il Tir ayının 24-də Məşhəddə anadan olub."
            ),
            "items": [
                {"fa": "آیت ا... بهجت / ۱۳۸۸/۳/۲۷ / قم / از دنیا رفتن", "reading_az": "Ayətollah Behcət / 1388/3/27 / Qom / əz donya rəftən", "az": "Ayətullah Behcət / 1388/3/27 / Qum / vəfat etmək",
                 "sample_answer_fa": "آیت ا... بهجت در بیست‌وهفتمِ خردادِ هزار و سیصد و هشتاد و هشت در قم از دنیا رفت.",
                 "sample_answer_reading_az": "Ayətollah Behcət dər bist-o-həftome xordade hezar va sisəd va həştad va həşt dər Qom əz donya rəft.",
                 "sample_answer_az": "Ayətullah Behcət 1388-ci il Xordad ayının 27-də Qumda vəfat etdi. — 3-cü ay خرداد-dır."},
                {"fa": "پدرم / ۱۳۹۰/۴/۱۶ / بیمارستان / بستری شدن", "reading_az": "Pedərəm / 1390/4/16 / bimarestan / bəstəri şodən", "az": "atam / 1390/4/16 / xəstəxana / yatırılmaq",
                 "sample_answer_fa": "پدرم در شانزدهمِ تیرِ هزار و سیصد و نود در بیمارستان بستری شد.",
                 "sample_answer_reading_az": "Pedərəm dər şanzdəhome tire hezar va sisəd va nəvad dər bimarestan bəstəri şod.",
                 "sample_answer_az": "Atam 1390-cı il Tir ayının 16-da xəstəxanaya yatırıldı. — 4-cü ay تیر-dir."},
                {"fa": "حسن / در تاریخ / ۱۳۹۰/۱۲/۴ / تهران / عمل کردن", "reading_az": "Həsən / dər tarix / 1390/12/4 / Tehran / əməl kərdən", "az": "Həsən / tarixdə / 1390/12/4 / Tehran / əməliyyat olunmaq",
                 "sample_answer_fa": "حسن در تاریخِ چهارمِ اسفندِ هزار و سیصد و نود در تهران عمل کرد.",
                 "sample_answer_reading_az": "Həsən dər tarixe çəharome esfənde hezar va sisəd va nəvad dər Tehran əməl kərd.",
                 "sample_answer_az": "Həsən 1390-cı il Esfənd ayının 4-də Tehranda əməliyyat oldu. — 12-ci ay اسفند-dir."},
                {"fa": "من و دوستم / در تاریخ / ۱۳۹۱/۲/۱۹ / آزمایش‌گاه / رفتن", "reading_az": "Mən va dustəm / dər tarix / 1391/2/19 / azmayeşgah / rəftən", "az": "mən və dostum / tarixdə / 1391/2/19 / laboratoriya / getmək",
                 "sample_answer_fa": "من و دوستم در تاریخِ نوزدهمِ اردیبهشتِ هزار و سیصد و نود و یک به آزمایش‌گاه رفتیم.",
                 "sample_answer_reading_az": "Mən va dustəm dər tarixe nozdəhome ordibeheşte hezar va sisəd va nəvad va yek be azmayeşgah rəftim.",
                 "sample_answer_az": "Mən və dostum 1391-ci il Ordibeheşt ayının 19-da laboratoriyaya getdik. — 2-ci ay اردیبهشت-dir."},
            ],
        },
        {
            # Çalışma 8 — səh. 242 «با گزینه‌ی درست کامل کنید»; dərslikdə 6 bənd var.
            "kind": "fill_blank",
            "instruction_az": "Mötərizədəki variantlardan düzgün olanını seçib boşluğu doldurun.",
            "word_bank": ["را", "به", "به", "می‌زنند", "می‌کند", "وجود دارد"],
            "items": [
                {"fa_with_blank": "بچّه‌ها پدر و مادرشان ___ بسیار دوست دارند. (را ؛ به ؛ از ؛ با)", "correct_answer": "را", "reading_az": "ra", "az": "təsirlik hal göstəricisi",
                 "full_reading_az": "Bəççeha pedər va madərəşan ra besyar dust darənd.",
                 "full_translation_az": "Uşaqlar ata-analarını çox sevirlər. — «دوست داشتن» «را» tələb edir."},
                {"fa_with_blank": "کودکان بیمار ___ سمیّه‌خانم، بسیار علاقه دارند. (را ؛ به ؛ از ؛ با)", "correct_answer": "به", "reading_az": "be", "az": "-a/-ə",
                 "full_reading_az": "Kudəkane bimar be Səmiyye-xanom, besyar əlaqe darənd.",
                 "full_translation_az": "Xəstə uşaqlar Səmiyyə xanımı çox sevirlər. — «علاقه داشتن» «به» tələb edir."},
                {"fa_with_blank": "فروشنده‌ی پوشاک ___ خانواده‌های فقیر تخفیف می‌دهد. (را ؛ به ؛ از ؛ با)", "correct_answer": "به", "reading_az": "be", "az": "-a/-ə",
                 "full_reading_az": "Foruşəndeye puşak be xanevadehaye fəqir təxfif midəhəd.",
                 "full_translation_az": "Geyim satıcısı kasıb ailələrə endirim edir. — «تخفیف دادن» «به» tələb edir."},
                {"fa_with_blank": "پرستارها با مهربانی زخم بیماران را می‌شویند و پماد ___ . (می‌کنند ؛ می‌کشند ؛ می‌زنند)", "correct_answer": "می‌زنند", "reading_az": "mizənənd", "az": "sürtürlər",
                 "full_reading_az": "Pərəstarha ba mehrəbani zəxme bimaran ra mişuyənd va pəmad mizənənd.",
                 "full_translation_az": "Tibb bacıları xəstələrin yarasını mehribanlıqla yuyur və məlhəm sürtürlər. — «پماد زدن» düzgün birləşmədir."},
                {"fa_with_blank": "سمیّه هنگام پانسمان زخم‌ها، کودکان را نوازش ___ . (می‌کند ؛ می‌زند ؛ می‌گیرد)", "correct_answer": "می‌کند", "reading_az": "mikonəd", "az": "sığallayır",
                 "full_reading_az": "Səmiyye hengame pansmane zəxmha, kudəkan ra nəvazeş mikonəd.",
                 "full_translation_az": "Səmiyyə yaraları sarıyarkən uşaqları sığallayır. — «نوازش کردن» düzgün birləşmədir."},
                {"fa_with_blank": "در داروخانه‌ی کوثر، انواع داروها، مانند قرص و کپسول ___ . (دارد ؛ وجود دارد)", "correct_answer": "وجود دارد", "reading_az": "vocud darəd", "az": "var (mövcuddur)",
                 "full_reading_az": "Dər daruxaneye Kousər, ənvae daruha, manənde qors va kapsul vocud darəd.",
                 "full_translation_az": "Kovsər aptekində həb və kapsul kimi müxtəlif dərmanlar var. — Yer bildirən cümlədə «وجود دارد» işlənir."},
            ],
        },
        {
            # Çalışma 9 — səh. 242 «لطفاً جایگزین کنید»; dərslikdə 3 bənd var.
            "kind": "answer_question",
            "title_fa": "لطفاً جایگزین کنید",
            "instruction_az": "Nümunə kimi «به خاطرِ … در تاریخِ … به …» qəlibi ilə cümlə qurun.",
            "example_fa": "من / چشم‌درد / ۱۳۹۱/۱۲/۲۵ / بیمارستان ← من *به خاطر* چشم‌درد *در تاریخِ* ۱۳۹۱/۱۲/۲۵ به بیمارستان می‌روم.",
            "example_reading_az": "Mən be xatere çeşmdərd dər tarixe bist-o-pəncome esfənde hezar va sisəd va nəvad va yek be bimarestan mirəvəm.",
            "example_az": (
                "Verilən sözlər: ŞƏXS / DƏRD (səbəb) / TARİX / YER.\n"
                "Qəlib: ŞƏXS + به خاطرِ SƏBƏB + در تاریخِ TARİX + به YER + می‌روم/می‌رود.\n"
                "«به خاطرِ» = «به سببِ» — «…-a görə».\n"
                "Tərcümə: Mən göz ağrısına görə 1391/12/25 tarixində xəstəxanaya gedirəm."
            ),
            "items": [
                {"fa": "هادی / دندان‌درد / ۱۳۹۱/۹/۱۷ / دندان‌پزشکی", "reading_az": "Hadi / dəndandərd / 1391/9/17 / dəndanpezeşki", "az": "Hadi / diş ağrısı / 1391/9/17 / diş klinikası",
                 "sample_answer_fa": "هادی به خاطر دندان‌درد در تاریخِ هفدهمِ آذرِ هزار و سیصد و نود و یک به دندان‌پزشکی می‌رود.",
                 "sample_answer_reading_az": "Hadi be xatere dəndandərd dər tarixe hefdəhome azare hezar va sisəd va nəvad va yek be dəndanpezeşki mirəvəd.",
                 "sample_answer_az": "Hadi diş ağrısına görə 1391-ci il Azər ayının 17-də diş həkiminə gedir. — 9-cu ay آذر-dir."},
                {"fa": "مادربزرگم / معاینه‌ی گوش / ۱۳۹۲/۱/۲۴ / درمان‌گاه", "reading_az": "Madərbozorgəm / moayeneye quş / 1392/1/24 / dərmangah", "az": "nənəm / qulaq müayinəsi / 1392/1/24 / poliklinika",
                 "sample_answer_fa": "مادربزرگم به خاطر معاینه‌ی گوش در تاریخِ بیست‌وچهارمِ فروردینِ هزار و سیصد و نود و دو به درمان‌گاه می‌رود.",
                 "sample_answer_reading_az": "Madərbozorgəm be xatere moayeneye quş dər tarixe bist-o-çəharome fərvərdine hezar va sisəd va nəvad va do be dərmangah mirəvəd.",
                 "sample_answer_az": "Nənəm qulaq müayinəsi üçün 1392-ci il Fərvərdin ayının 24-də poliklinikaya gedir. — 1-ci ay فروردین-dir."},
                {"fa": "زهرا و دوستش / دل‌درد / الآن / مطب", "reading_az": "Zəhra va dusteş / deldərd / əl'an / mətəb", "az": "Zəhra və rəfiqəsi / qarın ağrısı / indi / həkim kabineti",
                 "sample_answer_fa": "زهرا و دوستش به خاطر دل‌درد الآن به مطب می‌روند.",
                 "sample_answer_reading_az": "Zəhra va dusteş be xatere deldərd əl'an be mətəb mirəvənd.",
                 "sample_answer_az": "Zəhra və rəfiqəsi qarın ağrısına görə indi həkim kabinetinə gedirlər. — «الآن» tarix deyil, ona görə «در تاریخِ» işlənmir."},
            ],
        },
        {
            # Çalışma 10 — səh. 242 «اسم تصویرهای زیر را بگویید»; 8 cüt şəkil.
            "kind": "picture_sentences",
            "title_fa": "اسم تصویرهای زیر را بگویید",
            "instruction_az": "Aşağıdakı şəkillərin adını deyin (hər şəkil üçün bir cümlə də qurun).",
            "example_fa": "این چیست؟",
            "example_reading_az": "İn çist?",
            "example_az": "Bu nədir? — əvvəlcə sözü deyin, sonra onunla cümlə qurun.",
            "example_answer_fa": "این، قرص است. دکتر گفت: هر هشت ساعت یک قرص بخور.",
            "example_answer_reading_az": "İn, qors əst. Doktor goft: hər həşt saət yek qors boxor.",
            "example_answer_az": "Bu, həbdir. Həkim dedi: hər səkkiz saatdan bir həb iç.",
            "items": [
                {
                    "image": "",
                    "sentences": [
                        {"fa": "شانه می‌زند.", "reading_az": "Şane mizənəd.", "az": "(Saçını) darayır."},
                        {"fa": "رنگ می‌زند.", "reading_az": "Rəng mizənəd.", "az": "Rəngləyir (divarı boyayır)."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "تب دارد.", "reading_az": "Təb darəd.", "az": "Qızdırması var."},
                        {"fa": "قرص و کپسول", "reading_az": "Qors va kapsul", "az": "Həb və kapsul"},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "سِرُم", "reading_az": "Serom", "az": "Serum (damcı sistemi)"},
                        {"fa": "آمپول", "reading_az": "Ampul", "az": "İynə (ampula)"},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "دارو (شیشه‌ی دارو)", "reading_az": "Daru (şişeye daru)", "az": "Dərman (dərman şüşəsi)"},
                        {"fa": "شربت و قطره", "reading_az": "Şərbət va qətre", "az": "Şərbət və damcı"},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "چسبِ زخم", "reading_az": "Çəsbe zəxm", "az": "Yara plastırı"},
                        {"fa": "آمپول می‌زند.", "reading_az": "Ampul mizənəd.", "az": "İynə vurur."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "صندلی چرخ‌دار", "reading_az": "Səndəliye çərxdar", "az": "Əlil arabası (velosiped-kreslo)"},
                        {"fa": "عیادت می‌کند؛ بیمار بستری است.", "reading_az": "Eyadət mikonəd; bimar bəstəri əst.", "az": "Baş çəkir; xəstə xəstəxanaya yatırılıb."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "آزمایش‌گاه", "reading_az": "Azmayeşgah", "az": "Laboratoriya"},
                        {"fa": "داروخانه؛ داروساز", "reading_az": "Daruxane; darusaz", "az": "Aptek; əczaçı"},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "امدادگر، بیمار را معاینه می‌کند.", "reading_az": "Əmdadgər, bimar ra moayene mikonəd.", "az": "Təcili yardım işçisi xəstəni müayinə edir."},
                        {"fa": "پزشک، نسخه می‌نویسد.", "reading_az": "Pezeşk, nosxe minevisəd.", "az": "Həkim resept yazır."},
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
                        "fa": "پدرم پزشک متخصّص قلب است. او رئیس بیمارستان ابن سینا است.",
                        "reading_az": "Pedərəm pezeşke motəxəsese qəlb əst. U rəise bimarestane Ebn-e Sina əst.",
                        "az": "Atam ürək üzrə mütəxəssis həkimdir. O, İbn Sina xəstəxanasının rəisidir.",
                    },
                    {
                        "fa": "دوستم در خیابان تصادف کرد؛ او را زود به بخش اورژانس بردند.",
                        "reading_az": "Dustəm dər xiyaban təsadof kərd; u ra zud be bəxşe orjans bordənd.",
                        "az": "Dostum küçədə qəza keçirdi; onu tez təcili yardım şöbəsinə apardılar.",
                    },
                    {
                        "fa": "برادرم مریض است؛ او امروز علاوه بر خوردن قرص و کپسول، آمپول هم زد.",
                        "reading_az": "Bəradərəm mariz əst; u əmruz əlave bər xordəne qors va kapsul, ampul həm zad.",
                        "az": "Qardaşım xəstədir; o, bu gün həb və kapsul içməkdən əlavə, iynə də vurdurdu.",
                    },
                    {
                        "fa": "دکتر گفت: هر هشت ساعت، یک قرص و یک قاشق غذاخوری شربت بخور.",
                        "reading_az": "Doktor goft: hər həşt saət, yek qors va yek qaşoqe qəzaxori şərbət boxor.",
                        "az": "Həkim dedi: hər səkkiz saatdan bir, bir həb və bir xörək qaşığı şərbət iç.",
                    },
                    {
                        "fa": "دختر کوچکم به خاطر سرماخوردن تب دارد و زیاد سرفه و عطسه می‌کند.",
                        "reading_az": "Doxtəre kuçekəm be xatere sərma-xordən təb darəd va ziyad sorfe va ətse mikonəd.",
                        "az": "Kiçik qızım soyuqladığı üçün qızdırması var və çox öskürüb asqırır.",
                    },
                    {
                        "fa": "دندان علی درد می‌کند. او امروز برای درمان دندان‌هایش به دندان‌پزشکی می‌رود.",
                        "reading_az": "Dəndane Əli dərd mikonəd. U əmruz bəraye dərmane dəndanhayəş be dəndanpezeşki mirəvəd.",
                        "az": "Əlinin dişi ağrıyır. O, bu gün dişlərinin müalicəsi üçün diş həkiminə gedir.",
                    },
                    {
                        "fa": "در بیمارستان‌ها اتاق تزریقات، بخش اورژانس، آزمایش‌گاه، داروخانه و اتاق عمل وجود دارد.",
                        "reading_az": "Dər bimarestanha otaqe təzriqat, bəxşe orjans, azmayeşgah, daruxane va otaqe əməl vocud darəd.",
                        "az": "Xəstəxanalarda inyeksiya otağı, təcili yardım şöbəsi, laboratoriya, aptek və əməliyyat otağı olur.",
                    },
                    {
                        "fa": "در اتاق تزریقات، زخم بیمار را با سرم و بتادین می‌شویند و به وسیله‌ی باند پانسمان می‌کنند.",
                        "reading_az": "Dər otaqe təzriqat, zəxme bimar ra ba serom va betadin mişuyənd va be vasileye band pansman mikonənd.",
                        "az": "İnyeksiya otağında xəstənin yarasını serum və betadinlə yuyur, bintlə sarğı qoyurlar.",
                    },
                    {
                        "fa": "پدربزرگم در بیمارستان بستری است. ما هر روز به عیادت ایشان می‌رویم.",
                        "reading_az": "Pedərbozorgəm dər bimarestan bəstəri əst. Ma hər ruz be eyadəte işan mirəvim.",
                        "az": "Babam xəstəxanaya yatırılıb. Biz hər gün ona baş çəkməyə gedirik.",
                    },
                    {
                        "fa": "فاطمه متخصّص و جرّاح چشم است. ایشان چشم بیماران را معاینه و جرّاحی می‌کند.",
                        "reading_az": "Fateme motəxəses va cərrahe çeşm əst. İşan çeşme bimaran ra moayene va cərrahi mikonəd.",
                        "az": "Fatimə göz həkimi-cərrahdır. O, xəstələrin gözünü müayinə edir və əməliyyat edir.",
                    },
                ],
            },
            {
                # Səh. 237 «لطفاً بخوانید» — «... زدن» birləşmələri ilə 10 cümlə.
                "items": [
                    {
                        "fa": "پدربزرگ و مادربزرگم هنگام دیدن ما خوش‌حال می‌شوند و لبخند می‌زنند.",
                        "reading_az": "Pedərbozorg va madərbozorgəm hengame didəne ma xoşhal mişəvənd va ləbxənd mizənənd.",
                        "az": "Babam və nənəm bizi görəndə sevinir və gülümsəyirlər.",
                    },
                    {
                        "fa": "قبل از رفتن به خانه‌ی دوستم، به او تلفن زدم؛ سپس به آن‌جا رفتم.",
                        "reading_az": "Qəbl əz rəftən be xaneye dustəm, be u telefon zadəm; səpəs be anca rəftəm.",
                        "az": "Dostumun evinə getməzdən əvvəl ona telefon etdim; sonra oraya getdim.",
                    },
                    {
                        "fa": "وقتی به خانه‌ی حسین رسیدم، زنگ زدم و پدرش در را باز کرد.",
                        "reading_az": "Vəqti be xaneye Hoseyn residəm, zəng zadəm va pedərəş dər ra baz kərd.",
                        "az": "Hüseynin evinə çatanda zəng vurdum və atası qapını açdı.",
                    },
                    {
                        "fa": "آیا شما قبل از رفتن به کلاس، موهایتان را شانه می‌زنید؟",
                        "reading_az": "Aya şoma qəbl əz rəftən be kelas, muhayetan ra şane mizənid?",
                        "az": "Siz sinfə getməzdən əvvəl saçınızı darayırsınızmı?",
                    },
                    {
                        "fa": "هفته‌ی قبل مریض بودم و سه تا آمپول زدم.",
                        "reading_az": "Həfteye qəbl mariz budəm va se ta ampul zadəm.",
                        "az": "Keçən həftə xəstə idim və üç iynə vurdurdum.",
                    },
                    {
                        "fa": "ما قبل از وارد شدن به اتاق مدیر، در می‌زنیم؛ سپس وارد می‌شویم.",
                        "reading_az": "Ma qəbl əz vared şodən be otaqe modir, dər mizənim; səpəs vared mişəvim.",
                        "az": "Biz müdirin otağına girməzdən əvvəl qapını döyürük; sonra giririk.",
                    },
                    {
                        "fa": "یکی از دوستانم زیاد حرف می‌زند. من زیاد حرف زدن را دوست ندارم.",
                        "reading_az": "Yeki əz dustanəm ziyad hərf mizənəd. Mən ziyad hərf zədən ra dust nədarəm.",
                        "az": "Dostlarımdan biri çox danışır. Mən çox danışmağı sevmirəm.",
                    },
                    {
                        "fa": "پلیس گفت: این خیابان، ورود ممنوع است؛ دور بزنید و از آن خیابان بروید.",
                        "reading_az": "Polis goft: in xiyaban, vorud məmnu əst; dor bezənid va əz an xiyaban bəravid.",
                        "az": "Polis dedi: bu küçəyə giriş qadağandır; geri dönün və o küçədən gedin.",
                    },
                    {
                        "fa": "در هوای آفتابی، هنگام بیرون رفتن از خانه به دست‌ها و صورتم کِرِم می‌زنم.",
                        "reading_az": "Dər havaye aftabi, hengame birun rəftən əz xane be dəstha va suratəm kerem mizənəm.",
                        "az": "Günəşli havada evdən çıxarkən əllərimə və üzümə krem sürtürəm.",
                    },
                    {
                        "fa": "هر روز هنگام خوردن صبحانه، شکر را در چای می‌ریزم و با قاشق آن را به هم می‌زنم.",
                        "reading_az": "Hər ruz hengame xordəne sobhane, şekər ra dər çay mirizəm va ba qaşoq an ra be həm mizənəm.",
                        "az": "Hər gün səhər yeməyi zamanı şəkəri çaya tökürəm və qaşıqla qarışdırıram.",
                    },
                ],
            },
        ],
        # Səh. 239 «لطفاً پاسخ دهید» — dərslikdəki 5 sual.
        "answer_items": [
            {
                "fa": "امروز چندمِ ماه است؟",
                "reading_az": "Əmruz çəndome mah əst?",
                "az": "Bu gün ayın neçəsidir?",
                "sample_answer_fa": "امروز، دوازدهمِ مهر است.",
                "sample_answer_reading_az": "Əmruz, dəvazdəhome mehr əst.",
                "sample_answer_az": "Bu gün Mehr ayının 12-sidir. — «چندمِ ماه» sıra sayı ilə cavab istəyir.",
            },
            {
                "fa": "تاریخ تولّدتان را بگویید؟",
                "reading_az": "Tarixe touledetan ra begoyid?",
                "az": "Doğum tarixinizi deyin?",
                "sample_answer_fa": "تاریخ تولّد من، بیست و دومِ بهمنِ هزار و سیصد و شصت و پنج است.",
                "sample_answer_reading_az": "Tarixe touləde mən, bist-o-dovvome bəhməne hezar va sisəd va şəst va pənc əst.",
                "sample_answer_az": "Mənim doğum tarixim 1365-ci il Bəhmən ayının 22-sidir.",
            },
            {
                "fa": "شما چه وقت به ایران آمدید؟",
                "reading_az": "Şoma çe vaqt be Iran amədid?",
                "az": "Siz İrana nə vaxt gəldiniz?",
                "sample_answer_fa": "من در پانزدهمِ شهریورِ هزار و سیصد و نود به ایران آمدم.",
                "sample_answer_reading_az": "Mən dər panzdəhome şəhrivare hezar va sisəd va nəvad be Iran amədəm.",
                "sample_answer_az": "Mən 1390-cı il Şəhrivər ayının 15-də İrana gəldim.",
            },
            {
                "fa": "دیروز هفدهم فروردین بود یا هجدهم فروردین؟",
                "reading_az": "Diruz hefdəhome fərvərdin bud ya hejdəhome fərvərdin?",
                "az": "Dünən Fərvərdin ayının 17-si idi, yoxsa 18-i?",
                "sample_answer_fa": "دیروز هفدهمِ فروردین بود.",
                "sample_answer_reading_az": "Diruz hefdəhome fərvərdin bud.",
                "sample_answer_az": "Dünən Fərvərdin ayının 17-si idi.",
            },
            {
                "fa": "آیا امام خمینی (ره) در چهاردهمِ خردادِ شصت و هشت از دنیا رفت؟",
                "reading_az": "Aya Emam Xomeyni dər çəhardəhome xordade şəst o həşt əz donya rəft?",
                "az": "İmam Xomeyni 68-ci ilin Xordad ayının 14-də dünyadan köçdümü?",
                "sample_answer_fa": "بله، امام خمینی (ره) در چهاردهم خردادِ هزار و سیصد و شصت و هشت از دنیا رفت.",
                "sample_answer_reading_az": "Bəle, Emam Xomeyni dər çəhardəhome xordade hezar va sisəd va şəst va həşt əz donya rəft.",
                "sample_answer_az": "Bəli, İmam Xomeyni 1368-ci il Xordad ayının 14-də dünyadan köçdü.",
            },
        ],
    },
    "reading_text": {
        "title_fa": "پرستار مهربان",
        "title_az": "Mehriban tibb bacısı",
        "paragraphs_fa": [
            "سمیّه، پرستاری خوش‌اخلاق و مهربان است. او در بخش کودکانِ بیمارستانِ امام خمینی (ره) کار می‌کند. سمیّه به کودکان بیمار در خوردن داروها کمک می‌کند. هنگام پانسمانِ زخمشان، آن‌ها را نوازش می‌کند و با مهربانی زخمشان را می‌شوید، پماد می‌زند و سپس به وسیله‌ی باند می‌بندد. او بچّه‌ها را مانند فرزندانش دوست دارد و کودکان هم به او بسیار علاقه دارند.",
            "خانم کاظمی، مادر سمیّه است. او پزشک داروساز و صاحبِ داروخانه‌ی بزرگِ کوثر است. این داروخانه شبانه‌روزی است. داروخانه‌ی دکتر کاظمی در خیابان سعدی، کنار بیمارستان امام‌خمینی (ره) قرار دارد.",
            "در داروخانه‌ی کوثر انواع داروها مانندِ قرص، کپسول، سرم، آمپول، شربت و پماد وجود دارد. آن‌جا علاوه بر دارو، وسایل پزشکی و بهداشتی، مانندِ صندلی چرخ‌دار، پنبه، باند، چسب زخم، بتادین، انواع کِرِم و خمیردندان و... می‌فروشند.",
            # Səh. 241 — mətnin dördüncü (son) abzası.
            "پدر سمیّه، پزشک متخصّصِ گوش و حلق و بینی است. مطب او بیشتر وقت‌ها شلوغ است. ایشان از خانواده‌های فقیر، پول ویزیت و جرّاحی نمی‌گیرد یا به آن‌ها بسیار تخفیف می‌دهد.",
        ],
        "footnotes": [
            {"fa": "بستری", "az": "yatırılmış (xəstəxanaya)"},
            {"fa": "درمان / بخش / تزریقات", "az": "müalicə / şöbə / iynə otağı"},
            {"fa": "علاقه دارد", "az": "maraq göstərir, sevir"},
            # Səh. 240 haşiyəsi.
            {"fa": "صندلی چرخ‌دار (ویلچر)", "az": "Əlil arabası (velçer)"},
            {"fa": "......... را دوست دارد.", "az": "«دوست داشتن» obyekti «را» ilə alır."},
            {"fa": "به ......... علاقه دارد.", "az": "«علاقه داشتن» obyekti «به» ilə alır."},
            # Səh. 241 haşiyəsi.
            {"fa": "به ......... تخفیف می‌دهد.", "az": "«تخفیف دادن» — kimə endirim verilirsə «به» ilə."},
            {"fa": "مطب / ویزیت", "az": "həkim kabineti / müayinə haqqı"},
        ],
        "full_translation_az": (
            "Səmiyyə xoşrəftar və mehriban bir tibb bacısıdır. O, İmam Xomeyni xəstəxanasının uşaq şöbəsində "
            "işləyir. Səmiyyə xəstə uşaqlara dərman qəbul etməkdə kömək edir. Yaralarının sarğısını dəyişərkən "
            "onları sığallayır, mehribanlıqla yaralarını yuyur, məlhəm sürtür və sonra bintlə sarıyır. O, uşaqları "
            "öz övladları kimi sevir və uşaqlar da onu çox sevirlər.\n\n"
            "Xanım Kazımi Səmiyyənin anasıdır. O, əczaçı-həkimdir və böyük Kovsər aptekinin sahibidir. Bu aptek "
            "sutkalıq (gecə-gündüz açıq) işləyir. Doktor Kazıminin apteki Sədi küçəsində, İmam Xomeyni "
            "xəstəxanasının yanında yerləşir.\n\n"
            "Kovsər aptekində həb, kapsul, serum, iynə, şərbət və məlhəm kimi müxtəlif dərmanlar var. Orada "
            "dərmandan əlavə, əlil arabası, pambıq, bint, yara plastırı, yod məhlulu, müxtəlif kremlər və diş "
            "pastası kimi tibbi və gigiyena vasitələri də satılır.\n\n"
            "Səmiyyənin atası qulaq-boğaz-burun üzrə mütəxəssis həkimdir. Onun kabineti çox vaxt izdihamlı olur. "
            "O, kasıb ailələrdən müayinə və əməliyyat pulu almır, yaxud onlara çox böyük endirim edir."
        ),
        "sentences": [
            {
                "fa": "سمیّه، پرستاری خوش‌اخلاق و مهربان است.",
                "reading_az": "Səmiyye, pərəstariye xoş-əxlaq va mehrəban əst.",
                "az": "Səmiyyə xoşrəftar və mehriban bir tibb bacısıdır.",
                "new_paragraph": True,
            },
            {
                "fa": "او در بخش کودکانِ بیمارستانِ امام خمینی (ره) کار می‌کند.",
                "reading_az": "U dər bəxşe kudəkane bimarestane Emam Xomeyni kar mikonəd.",
                "az": "O, İmam Xomeyni xəstəxanasının uşaq şöbəsində işləyir.",
            },
            {
                "fa": "سمیّه به کودکان بیمار در خوردن داروها کمک می‌کند.",
                "reading_az": "Səmiyye be kudəkane bimar dər xordəne daruha komək mikonəd.",
                "az": "Səmiyyə xəstə uşaqlara dərman qəbul etməkdə kömək edir.",
            },
            {
                "fa": "هنگام پانسمانِ زخمشان، آن‌ها را نوازش می‌کند و با مهربانی زخمشان را می‌شوید، پماد می‌زند و سپس به وسیله‌ی باند می‌بندد.",
                "reading_az": "Hengame pansmane zəxmeşan, anha ra nəvazeş mikonəd va ba mehrəbani zəxmeşan ra mişuyəd, pəmad mizənəd va səpəs be vasileye band mibəndəd.",
                "az": "Yaralarını sarıyarkən onları sığallayır, mehribanlıqla yaralarını yuyur, məlhəm sürtür və sonra bintlə sarıyır.",
            },
            {
                "fa": "او بچّه‌ها را مانند فرزندانش دوست دارد و کودکان هم به او بسیار علاقه دارند.",
                "reading_az": "U bəççeha ra manənde fərzəndanəş dust darəd va kudəkan həm be u besyar əlaqe darənd.",
                "az": "O, uşaqları öz övladları kimi sevir və uşaqlar da onu çox sevirlər.",
            },
            {
                "fa": "خانم کاظمی، مادر سمیّه است.",
                "reading_az": "Xanome Kazemi, madəre Səmiyye əst.",
                "az": "Xanım Kazımi Səmiyyənin anasıdır.",
                "new_paragraph": True,
            },
            {
                "fa": "او پزشک داروساز و صاحبِ داروخانه‌ی بزرگِ کوثر است.",
                "reading_az": "U pezeşke darusaz va sahebe daruxaneye bozorge Kousər əst.",
                "az": "O, əczaçı-həkimdir və böyük Kovsər aptekinin sahibidir.",
            },
            {
                "fa": "این داروخانه شبانه‌روزی است.",
                "reading_az": "İn daruxane, şəbaneruzi əst.",
                "az": "Bu aptek sutkalıq (gecə-gündüz açıq) işləyir.",
            },
            {
                "fa": "داروخانه‌ی دکتر کاظمی در خیابان سعدی، کنار بیمارستان امام‌خمینی (ره) قرار دارد.",
                "reading_az": "Daruxaneye doktore Kazemi dər xiyabane Sədi, kənare bimarestane Emam Xomeyni qərar darəd.",
                "az": "Doktor Kazıminin apteki Sədi küçəsində, İmam Xomeyni xəstəxanasının yanında yerləşir.",
            },
            {
                "fa": "در داروخانه‌ی کوثر انواع داروها مانندِ قرص، کپسول، سرم، آمپول، شربت و پماد وجود دارد.",
                "reading_az": "Dər daruxaneye Kousər ənvae daruha manənde qors, kapsul, serom, ampul, şərbət va pəmad vocud darəd.",
                "az": "Kovsər aptekində həb, kapsul, serum, iynə, şərbət və məlhəm kimi müxtəlif dərmanlar var.",
                "new_paragraph": True,
            },
            {
                "fa": "آن‌جا علاوه بر دارو، وسایل پزشکی و بهداشتی، مانندِ صندلی چرخ‌دار، پنبه، باند، چسب زخم، بتادین، انواع کِرِم و خمیردندان و... می‌فروشند.",
                "reading_az": "Anja əlave bər daru, vəsayele pezeşki va behdaşti, manənde səndəliye çərxdar, pənbe, band, çəsbe zəxm, betadin, ənvae kerem va xəmirdəndan va ... miforuşənd.",
                "az": "Orada dərmandan əlavə, əlil arabası, pambıq, bint, yara plastırı, yod məhlulu, müxtəlif kremlər və diş pastası kimi tibbi və gigiyena vasitələri də satılır.",
            },
            {
                "fa": "پدر سمیّه، پزشک متخصّصِ گوش و حلق و بینی است.",
                "reading_az": "Pedəre Səmiyye, pezeşke motəxəssese quş-o-həlq-o-bini əst.",
                "az": "Səmiyyənin atası qulaq-boğaz-burun üzrə mütəxəssis həkimdir.",
                "new_paragraph": True,
            },
            {
                "fa": "مطب او بیشتر وقت‌ها شلوغ است.",
                "reading_az": "Mətəbe u biştəre vəqtha şoluğ əst.",
                "az": "Onun həkim kabineti çox vaxt izdihamlı olur.",
            },
            {
                "fa": "ایشان از خانواده‌های فقیر، پول ویزیت و جرّاحی نمی‌گیرد یا به آن‌ها بسیار تخفیف می‌دهد.",
                "reading_az": "İşan əz xanevadehaye fəqir, pule vizit va cərrahi nemigirəd ya be anha besyar təxfif midəhəd.",
                "az": "O, kasıb ailələrdən müayinə və əməliyyat pulu almır, yaxud onlara çox böyük endirim edir.",
            },
        ],
        "comprehension_questions": [
            {
                "question_fa": "سمیّه چه‌کاره است و کجا کار می‌کند؟",
                "reading_az": "Səmiyye çekare əst va koca kar mikonəd?",
                "az": "Səmiyyə nəçidir və harada işləyir?",
                "sample_answer_fa": "سمیّه پرستار است و در بخش کودکان بیمارستان امام‌خمینی (ره) کار می‌کند.",
                "sample_answer_reading_az": "Səmiyye pərəstar əst va dər bəxşe kudəkane bimarestane Emam Xomeyni kar mikonəd.",
                "sample_answer_az": "Səmiyyə tibb bacısıdır və İmam Xomeyni xəstəxanasının uşaq şöbəsində işləyir.",
            },
            {
                # Səh. 241, sual 2.
                "question_fa": "چرا کودکان، سمیّه را دوست دارند؟",
                "reading_az": "Çera kudəkan, Səmiyye ra dust darənd?",
                "az": "Uşaqlar niyə Səmiyyəni sevirlər?",
                "sample_answer_fa": "چون سمیّه با آن‌ها مهربان است؛ آن‌ها را نوازش می‌کند و مانند فرزندانش دوست دارد.",
                "sample_answer_reading_az": "Çon Səmiyye ba anha mehrəban əst; anha ra nəvazeş mikonəd va manənde fərzəndanəş dust darəd.",
                "sample_answer_az": "Çünki Səmiyyə onlarla mehribandır; onları sığallayır və öz övladları kimi sevir.",
            },
            {
                # Səh. 241, sual 3.
                "question_fa": "داروخانه‌ی شبانه‌روزی کوثر کجا قرار دارد؟",
                "reading_az": "Daruxaneye şəbaneruziye Kousər koca qərar darəd?",
                "az": "Sutkalıq Kovsər apteki harada yerləşir?",
                "sample_answer_fa": "داروخانه‌ی کوثر در خیابان سعدی، کنار بیمارستان امام‌خمینی (ره) قرار دارد.",
                "sample_answer_reading_az": "Daruxaneye Kousər dər xiyabane Sədi, kənare bimarestane Emam Xomeyni qərar darəd.",
                "sample_answer_az": "Kovsər apteki Sədi küçəsində, İmam Xomeyni xəstəxanasının yanında yerləşir.",
            },
            {
                # Səh. 241, sual 4.
                "question_fa": "در داروخانه‌ی خانم کاظمی چه چیزهایی وجود دارد؟",
                "reading_az": "Dər daruxaneye xanome Kazemi çe çizhayi vocud darəd?",
                "az": "Xanım Kazıminin aptekində nələr var?",
                "sample_answer_fa": "در آن‌جا قرص، کپسول، سرم، آمپول، شربت، پماد و وسایل پزشکی و بهداشتی مانند صندلی چرخ‌دار، پنبه، باند و بتادین وجود دارد.",
                "sample_answer_reading_az": "Dər anca qors, kapsul, serom, ampul, şərbət, pəmad va vəsayele pezeşki va behdaşti manənde səndəliye çərxdar, pənbe, band va betadin vocud darəd.",
                "sample_answer_az": "Orada həb, kapsul, serum, iynə, şərbət, məlhəm və əlil arabası, pambıq, bint, betadin kimi tibbi-gigiyena vasitələri var.",
            },
            {
                # Səh. 241, sual 5.
                "question_fa": "پدر و مادر سمیّه چه‌کاره هستند؟",
                "reading_az": "Pedər va madəre Səmiyye çekare hastənd?",
                "az": "Səmiyyənin ata-anası nəçidirlər?",
                "sample_answer_fa": "مادرش، خانم کاظمی، پزشکِ داروساز و صاحبِ داروخانه‌ی کوثر است و پدرش پزشک متخصّص است.",
                "sample_answer_reading_az": "Madərəş, xanome Kazemi, pezeşke darusaz va sahebe daruxaneye Kousər əst va pedərəş pezeşke motəxəsses əst.",
                "sample_answer_az": "Anası, xanım Kazımi, əczaçı-həkimdir və Kovsər aptekinin sahibidir; atası isə mütəxəssis həkimdir.",
            },
            {
                # Səh. 241, sual 6.
                "question_fa": "پدر سمیّه متخصّصِ چه چیزی است؟",
                "reading_az": "Pedəre Səmiyye motəxəssese çe çizi əst?",
                "az": "Səmiyyənin atası nə üzrə mütəxəssisdir?",
                "sample_answer_fa": "پدر سمیّه، پزشک متخصّصِ گوش و حلق و بینی است.",
                "sample_answer_reading_az": "Pedəre Səmiyye, pezeşke motəxəssese quş-o-həlq-o-bini əst.",
                "sample_answer_az": "Səmiyyənin atası qulaq-boğaz-burun (LOR) üzrə mütəxəssis həkimdir.",
            },
            {
                # Səh. 241, sual 7.
                "question_fa": "پدر سمیّه به چه کسانی تخفیف می‌دهد؟",
                "reading_az": "Pedəre Səmiyye be çe kəsani təxfif midəhəd?",
                "az": "Səmiyyənin atası kimlərə endirim edir?",
                "sample_answer_fa": "او به خانواده‌های فقیر بسیار تخفیف می‌دهد یا از آن‌ها پول ویزیت و جرّاحی نمی‌گیرد.",
                "sample_answer_reading_az": "U be xanevadehaye fəqir besyar təxfif midəhəd ya əz anha pule vizit va cərrahi nemigirəd.",
                "sample_answer_az": "O, kasıb ailələrə çox endirim edir, yaxud onlardan müayinə və əməliyyat pulu almır.",
            },
        ],
    },
}
