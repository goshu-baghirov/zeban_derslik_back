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
                "Mənanı sözbəsöz yox, birləşmə kimi bütöv öyrənmək lazımdır."
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
                "Yazıda ardıcıllıq il/ay/gün olur, oxunuş isə gündən başlayır; sözlər izafə (kəsrə) ilə bağlanır."
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
    ],
    "exercises": [
        {
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
            "kind": "practice_reveal",
            "instruction_az": "Nümunə kimi əvəz edin: «من دو روز، دندانم درد می‌کند = من دو روز است دندان‌درد دارم.»",
            "items": [
                {
                    "prompt_fa": "فرزندم / چهار ساعت / سرش",
                    "answer_fa": "فرزندم چهار ساعت است سردرد دارد.",
                    "reading_az": "Fərzəndəm çəhar saət əst sərdərd darəd.",
                    "az": "Övladımın dörd saatdır ki, başı ağrıyır.",
                },
                {
                    "prompt_fa": "ابراهیم / یک هفته / کمرش",
                    "answer_fa": "ابراهیم یک هفته است کمردرد دارد.",
                    "reading_az": "Ebrahim yek həfte əst kəmərdərd darəd.",
                    "az": "İbrahimin bir həftədir ki, beli ağrıyır.",
                },
                {
                    "prompt_fa": "پدربزرگمان / یک ماه / پایش",
                    "answer_fa": "پدربزرگمان یک ماه است پادرد دارد.",
                    "reading_az": "Pedərbozorgeman yek mah əst padərd darəd.",
                    "az": "Babamızın bir aydır ki, ayağı ağrıyır.",
                },
                {
                    "prompt_fa": "ما / یک سال / چشممان",
                    "answer_fa": "ما یک سال است چشم‌درد داریم.",
                    "reading_az": "Ma yek sal əst çeşmdərd darim.",
                    "az": "Bizim bir ildir ki, gözümüz ağrıyır.",
                },
            ],
        },
        {
            # Səh. 235: «بفرمایید» sözünün şəkillərdəki müxtəlif nəzakət mənaları.
            "kind": "answer_question",
            "title_fa": "بفرمایید",
            "instruction_az": "Vəziyyətə uyğun «بفرمایید» ilə qısa cavab deyin.",
            "example_fa": "میزبان چای را به مهمان می‌دهد. ← بفرمایید.",
            "example_reading_az": "Mizban çay ra be mehman midəhəd. — Bəfərmayid.",
            "example_az": "Ev sahibi qonağa çay verir. — Buyurun.",
            "items": [
                {"fa": "کودک به مادربزرگش هدیه می‌دهد.", "reading_az": "Kudək be madərbozorgeş hədiye midəhəd.", "az": "Uşaq nənəsinə hədiyyə verir.", "sample_answer_fa": "بفرمایید.", "sample_answer_reading_az": "Bəfərmayid.", "sample_answer_az": "Buyurun, alın."},
                {"fa": "معلم به دانش‌آموز اجازه می‌دهد وارد کلاس شود.", "reading_az": "Moəlləm be daneşamuz ecazeye vorud be kelas midəhəd.", "az": "Müəllim şagirdə sinfə girməyə icazə verir.", "sample_answer_fa": "بفرمایید.", "sample_answer_reading_az": "Bəfərmayid.", "sample_answer_az": "Buyurun, içəri keçin."},
                {"fa": "منشی به بیمار می‌گوید وارد مطب شود.", "reading_az": "Mənşi be bimar miguyəd varede mətəb şəvəd.", "az": "Katibə xəstəyə kabinetə girməsini deyir.", "sample_answer_fa": "سلام، بفرمایید.", "sample_answer_reading_az": "Səlam, bəfərmayid.", "sample_answer_az": "Salam, buyurun."},
                {"fa": "رانندهٔ تاکسی پول را به مسافر می‌دهد.", "reading_az": "Ranəndeye taksi pul ra be mosafer midəhəd.", "az": "Taksi sürücüsü pulu sərnişinə verir.", "sample_answer_fa": "بفرمایید.", "sample_answer_reading_az": "Bəfərmayid.", "sample_answer_az": "Buyurun, alın."},
            ],
        },
        {
            # Səh. 237: «... زدن» birləşmələri ilə boşluqları tamamlamaq.
            "kind": "fill_blank",
            "instruction_az": "Uyğun «... زدن» birləşməsini seçib boşluğu doldurun.",
            "word_bank": ["رنگ می‌زنند", "اتو می‌زنم", "آمپول زد", "تلفن زد", "به هم زدم"],
            "items": [
                {"fa_with_blank": "رنگ‌کارها فردا دیوارهای مدرسه را ___ .", "correct_answer": "رنگ می‌زنند", "reading_az": "rəng mizənənd", "az": "rəngləyirlər", "full_reading_az": "Rəngkarha fərda divarhaye mədrəse ra rəng mizənənd.", "full_translation_az": "Rəngsazlar sabah məktəbin divarlarını rəngləyəcəklər."},
                {"fa_with_blank": "پس از شستن لباس‌ها، پیراهنم را ___ .", "correct_answer": "اتو می‌زنم", "reading_az": "otu mizənəm", "az": "ütüləyirəm", "full_reading_az": "Pəs əz şostəne lebas-ha, pirahənəm ra otu mizənəm.", "full_translation_az": "Paltarları yuduqdan sonra köynəyimi ütüləyirəm."},
                {"fa_with_blank": "دوستم علاوه‌بر خوردن کپسول و شربت، یک سرم و دو تا ___ .", "correct_answer": "آمپول زد", "reading_az": "ampul zad", "az": "iynə vurdurdu", "full_reading_az": "Dustəm əlave bər xordəne kapsul va şərbət, yek serom va do ta ampul zad.", "full_translation_az": "Dostum kapsul və şərbət içməklə yanaşı, serum və iki iynə də vurdurdu."},
                {"fa_with_blank": "دیروز مریض بودم؛ دوستم به من ___ و حالم را پرسید.", "correct_answer": "تلفن زد", "reading_az": "telefon zad", "az": "telefon etdi", "full_reading_az": "Diruz mariz budəm; dustəm be mən telefon zad va haləm ra porsid.", "full_translation_az": "Dünən xəstə idim; dostum mənə telefon edib halımı soruşdu."},
                {"fa_with_blank": "امروز صبحانه، مقداری شکر در شیر ریختم و با قاشق آن را ___ .", "correct_answer": "به هم زدم", "reading_az": "be həm zadəm", "az": "qarışdırdım", "full_reading_az": "Əmruz sobhane, məqdari şəkər dər şir rixtəm va ba qaşoq an ra be həm zadəm.", "full_translation_az": "Bu gün səhər yeməyində südün içinə şəkər tökdüm və qaşıqla qarışdırdım."},
            ],
        },
        {
            # Səh. 239: tarixlə verilən sözlərdən cümlə qurmaq.
            "kind": "answer_question",
            "title_fa": "تاریخ را بگویید",
            "instruction_az": "Verilən sözlərdən tarixlə birlikdə tam cümlə qurun.",
            "example_fa": "من / چشم‌درد / ۱۳۹۱/۱۲/۲۵ / بیمارستان ← من به خاطر چشم‌درد در تاریخ ۱۳۹۱/۱۲/۲۵ به بیمارستان می‌روم.",
            "example_reading_az": "Mən / çeşmdərd / 1391/12/25 / bimarestan. — Mən be xatere çeşmdərd dər tarix 1391/12/25 be bimarestan mirəvəm.",
            "example_az": "Mən göz ağrısına görə 1391/12/25 tarixində xəstəxanaya gedirəm.",
            "items": [
                {"fa": "آیت‌الله بهجت / ۱۳۸۸/۳/۲۷ / قم / از دنیا رفتن", "reading_az": "Ayətollah Behcət / 1388/3/27 / Qom / əz donya rəftən", "az": "Ayətullah Behcət / 1388/3/27 / Qum / vəfat etmək", "sample_answer_fa": "آیت‌الله بهجت در بیست‌وهفتمِ تیرِ هزار و سیصد و هشتاد و هشت در قم از دنیا رفت.", "sample_answer_reading_az": "Ayətollah Behcət dər bist-o-həftome tire hezar va sisəd va həştad va həşt dər Qom əz donya rəft.", "sample_answer_az": "Ayətullah Behcət 1388-ci il Tir ayının 27-də Qumda vəfat etdi."},
                {"fa": "پدرم / ۱۳۹۰/۴/۱۶ / بیمارستان / بستری شدن", "reading_az": "Pedərəm / 1390/4/16 / bimarestan / bəstəri şodən", "az": "atam / 1390/4/16 / xəstəxana / yatızdırılmaq", "sample_answer_fa": "پدرم در شانزدهمِ تیرِ هزار و سیصد و نود در بیمارستان بستری شد.", "sample_answer_reading_az": "Pedərəm dər şanzdəhome tire hezar va sisəd va nəvad dər bimarestan bəstəri şod.", "sample_answer_az": "Atam 1390-cı il Tir ayının 16-da xəstəxanaya yatırıldı."},
                {"fa": "من و دوستم / ۱۳۹۱/۲/۱۹ / آزمایش‌گاه / رفتن", "reading_az": "Mən va dustəm / 1391/2/19 / azmayeşgah / rəftən", "az": "mən və dostum / 1391/2/19 / laboratoriya / getmək", "sample_answer_fa": "من و دوستم در نوزدهمِ اردیبهشتِ هزار و سیصد و نود و یک به آزمایش‌گاه رفتیم.", "sample_answer_reading_az": "Mən va dustəm dər nozdəhome ordibeheşte hezar va sisəd va nəvad va yek be azmayeşgah rəftim.", "sample_answer_az": "Mən və dostum 1391-ci il Ordibeheşt ayının 19-da laboratoriyaya getdik."},
            ],
        },
        {
            # Səh. 242: oxu mətninə aid düzgün cavabı tapmaq.
            "kind": "fill_blank",
            "instruction_az": "Oxu mətninə əsasən uyğun sözü seçin.",
            "word_bank": ["به", "با", "را", "می‌زنند", "می‌گیرد", "وجود دارد"],
            "items": [
                {"fa_with_blank": "بچّه‌ها پدر و مادرشان ___ بسیار دوست دارند.", "correct_answer": "را", "reading_az": "ra", "az": "təsirlik hal şəkilçisi", "full_reading_az": "Bəççeha pedər va madərəşan ra besyar dust darənd.", "full_translation_az": "Uşaqlar ata-analarını çox sevirlər."},
                {"fa_with_blank": "کودکان بیمار ___ سمیّه‌خانم بسیار علاقه دارند.", "correct_answer": "به", "reading_az": "be", "az": "-a/-ə", "full_reading_az": "Kudəkane bimar be Səmiyyexanom besyar əlaqe darənd.", "full_translation_az": "Xəstə uşaqlar xanım Səmiyyəni çox sevirlər."},
                {"fa_with_blank": "پرستارها با مهربانی زخم بیماران را می‌شویند و پماد ___ .", "correct_answer": "می‌زنند", "reading_az": "mizənənd", "az": "sürtürlər", "full_reading_az": "Pərəstarha ba mehrəbani zəxme bimaran ra mişuyənd va pəmad mizənənd.", "full_translation_az": "Tibb bacıları xəstələrin yarasını mehribanlıqla yuyur və məlhəm sürtürlər."},
                {"fa_with_blank": "در داروخانهٔ کوثر، انواع داروها مانند قرص و کپسول ___ .", "correct_answer": "وجود دارد", "reading_az": "vocud darəd", "az": "var", "full_reading_az": "Dər daruxaneye Kousər, ənvaye daruha manənde qors va kapsul vocud darəd.", "full_translation_az": "Kovsər aptekində həb və kapsul kimi müxtəlif dərmanlar var."},
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
        ],
        "answer_items": [
            {
                "fa": "امروز چندمِ ماه است؟",
                "reading_az": "Əmruz çəndome mah əst?",
                "az": "Bu gün ayın neçəsidir?",
            },
            {
                "fa": "تاریخ تولّدتان را بگویید؟",
                "reading_az": "Tarixe touledetan ra begoyid?",
                "az": "Doğum tarixinizi deyin?",
            },
            {
                "fa": "شما چه وقت به ایران آمدید؟",
                "reading_az": "Şoma çe vaqt be Iran amədid?",
                "az": "Siz İrana nə vaxt gəldiniz?",
            },
            {
                "fa": "دیروز هفدهم فروردین بود یا هجدهم فروردین؟",
                "reading_az": "Diruz hefdəhome fərvərdin bud ya hejdəhome fərvərdin?",
                "az": "Dünən Fərvərdin ayının 17-si idi, yoxsa 18-i?",
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
        "sentences": [
            {
                "fa": "سمیّه، پرستاری خوش‌اخلاق و مهربان است.",
                "reading_az": "Səmiyye, pərəstariye xoş-əxlaq va mehrəban əst.",
                "az": "Səmiyyə xoşrəftar və mehriban bir tibb bacısıdır.",
                "new_paragraph": True,
            },
            {
                "fa": "او در بخش کودکان بیمارستان امام خمینی (ره) کار می‌کند.",
                "reading_az": "U dər bəxşe kudəkane bimarestane Emam Xomeyni kar mikonəd.",
                "az": "O, İmam Xomeyni xəstəxanasının uşaq şöbəsində işləyir.",
            },
            {
                "fa": "سمیّه به کودکان بیمار در خوردن داروها کمک می‌کند.",
                "reading_az": "Səmiyye be kudəkane bimar dər xordəne daruha komək mikonəd.",
                "az": "Səmiyyə xəstə uşaqlara dərman qəbul etməkdə kömək edir.",
            },
            {
                "fa": "هنگام پانسمانِ زخمشان، آن‌ها را با مهربانی زخمشان را می‌شوید و با نوازش می‌کند و سپس پماد می‌زند و به وسیله‌ی باند می‌بندد.",
                "reading_az": "Hengame pansmane zəxmeşan, anha ra ba mehrəbani zəxmeşan ra mişuyəd va ba nəvazeş mikonəd va səpəs pəmad mizənəd va be vasileye band mibəndəd.",
                "az": "Yaralarının sarğısını dəyişərkən onları mehribanlıqla yuyur, sığallayır, sonra məlhəm sürtür və bintlə sarıyır.",
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
                "fa": "او پزشک داروساز و صاحب داروخانه‌ی بزرگ کوثر است.",
                "reading_az": "U pezeşke darusaz va saheb daruxaneye bozorge Kousər əst.",
                "az": "O, əczaçı-həkimdir və böyük Kovsər aptekinin sahibidir.",
            },
            {
                "fa": "این داروخانه، شبانه‌روزی است.",
                "reading_az": "İn daruxane, şəbaneruzi əst.",
                "az": "Bu aptek sutkalıq (gecə-gündüz açıq) işləyir.",
            },
            {
                "fa": "داروخانه‌ی دکتر کاظمی در خیابان سعدی، کنار بیمارستان امام‌خمینی (ره) قرار دارد.",
                "reading_az": "Daruxaneye doktore Kazemi dər xiyabane Sədi, kənare bimarestane Emam Xomeyni qərar darəd.",
                "az": "Doktor Kazıminin apteki Sədi küçəsində, İmam Xomeyni xəstəxanasının yanında yerləşir.",
            },
            {
                "fa": "در داروخانه‌ی کوثر انواع داروها، مانندِ قرص، کپسول، سرم، آمپول، شربت و پماد وجود دارد.",
                "reading_az": "Dər daruxaneye Kousər ənvae daruha, manənde qors, kapsul, serom, ampul, şərbət va pəmad vocud darəd.",
                "az": "Kovsər aptekində həb, kapsul, serum, iynə, şərbət və məlhəm kimi müxtəlif dərmanlar var.",
                "new_paragraph": True,
            },
            {
                "fa": "آن‌جا علاوه بر دارو، وسایل پزشکی و بهداشتی، مانندِ صندلی چرخ‌دار، پنبه، باند، چسب زخم، بتادین، انواع کِرِم و خمیردندان و... می‌فروشند.",
                "reading_az": "Anja əlave bər daru, vəsayele pezeşki va behdaşti, manənde səndəliye çərxdar, pənbe, band, çəsbe zəxm, betadin, ənvae kerem va xəmirdəndan va ... miforuşənd.",
                "az": "Orada dərmandan əlavə, əlil arabası, pambıq, bint, yara plastırı, yod məhlulu, müxtəlif kremlər və diş pastası kimi tibbi və gigiyena vasitələri də satılır.",
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
                "question_fa": "سمیّه هنگام پانسمانِ زخمِ بیمارها چه‌کار می‌کند؟",
                "reading_az": "Səmiyye hengame pansmane zəxme bimarha çekar mikonəd?",
                "az": "Səmiyyə xəstələrin yarasını sarıyarkən nə edir?",
                "sample_answer_fa": "او با مهربانی زخمشان را می‌شوید، نوازش می‌کند، پماد می‌زند و با باند می‌بندد.",
                "sample_answer_reading_az": "U ba mehrəbani zəxmeşan ra mişuyəd, nəvazeş mikonəd, pəmad mizənəd va ba band mibəndəd.",
                "sample_answer_az": "O, mehribanlıqla yaralarını yuyur, sığallayır, məlhəm sürtür və bintlə sarıyır.",
            },
            {
                "question_fa": "مادر سمیّه چه‌کاره است؟",
                "reading_az": "Madəre Səmiyye çekare əst?",
                "az": "Səmiyyənin anası nəçidir?",
                "sample_answer_fa": "مادر سمیّه، خانم کاظمی، پزشکِ داروساز و صاحبِ داروخانه‌ی کوثر است.",
                "sample_answer_reading_az": "Madəre Səmiyye, xanome Kazemi, pezeşke darusaz va sahebe daruxaneye Kousər əst.",
                "sample_answer_az": "Səmiyyənin anası, xanım Kazımi, əczaçı-həkimdir və Kovsər aptekinin sahibidir.",
            },
            {
                "question_fa": "داروخانه‌ی کوثر کجاست؟",
                "reading_az": "Daruxaneye Kousər kocast?",
                "az": "Kovsər apteki haradadır?",
                "sample_answer_fa": "داروخانه‌ی کوثر در خیابان سعدی، کنار بیمارستان امام‌خمینی (ره) قرار دارد.",
                "sample_answer_reading_az": "Daruxaneye Kousər dər xiyabane Sədi, kənare bimarestane Emam Xomeyni qərar darəd.",
                "sample_answer_az": "Kovsər apteki Sədi küçəsində, İmam Xomeyni xəstəxanasının yanında yerləşir.",
            },
            {
                "question_fa": "در داروخانه‌ی کوثر چه چیزهایی وجود دارد؟",
                "reading_az": "Dər daruxaneye Kousər çe çizhayi vocud darəd?",
                "az": "Kovsər aptekində nələr var?",
                "sample_answer_fa": "در آن‌جا قرص، کپسول، سرم، آمپول، شربت، پماد و وسایل پزشکی و بهداشتی وجود دارد.",
                "sample_answer_reading_az": "Dər anja qors, kapsul, serom, ampul, şərbət, pəmad va vəsayele pezeşki va behdaşti vocud darəd.",
                "sample_answer_az": "Orada həb, kapsul, serum, iynə, şərbət, məlhəm və tibbi-gigiyena vasitələri var.",
            },
            {
                "question_fa": "آیا داروخانه‌ی کوثر شبانه‌روزی است؟",
                "reading_az": "Aya daruxaneye Kousər şəbaneruzi əst?",
                "az": "Kovsər apteki sutkalıq (gecə-gündüz) işləyirmi?",
                "sample_answer_fa": "بله، داروخانه‌ی کوثر شبانه‌روزی است.",
                "sample_answer_reading_az": "Bəle, daruxaneye Kousər şəbaneruzi əst.",
                "sample_answer_az": "Bəli, Kovsər apteki sutka boyu (gecə-gündüz) işləyir.",
            },
        ],
    },
}
