# Dərs 16 — میوه‌ها و سبزی‌ها (Meyvə və tərəvəzlər)
# Mənbə: کتاب دوم, səh. 195-206

LESSON = {
    "number": 16,
    "title_fa": "میوه‌ها و سبزی‌ها",
    "title_az": "Meyvə və tərəvəzlər",
    "available": True,
    "vocabulary": [
        {"fa": "انگور", "reading": "əngur", "az": "Üzüm"},
        {"fa": "گلابی", "reading": "goləbi", "az": "Armud"},
        {"fa": "انجیر", "reading": "ənjir", "az": "Əncir"},
        {"fa": "موز", "reading": "mouz", "az": "Banan"},
        {"fa": "آناناس", "reading": "ananas", "az": "Ananas"},
        {"fa": "توت‌فرنگی", "reading": "tute fərəngi", "az": "Çiyələk"},
        {"fa": "زیتون", "reading": "zeytun", "az": "Zeytun"},
        {"fa": "آلو", "reading": "alu", "az": "Gavalı"},
        {"fa": "زردآلو", "reading": "zərdalu", "az": "Ərik"},
        {"fa": "کمپوت", "reading": "kompot", "az": "Kompot"},
        {"fa": "سبزی", "reading": "səbzi", "az": "Göyərti"},
        {"fa": "جعفری", "reading": "cəfəri", "az": "Cəfəri"},
        {"fa": "ریحان", "reading": "reyhan", "az": "Reyhan"},
        {"fa": "نعنا", "reading": "nəna", "az": "Nanə"},
        {"fa": "تربچه", "reading": "torbəçe", "az": "Turp"},
        {"fa": "پیازچه", "reading": "piyazçe", "az": "Cavan soğan"},
        {"fa": "گوجه", "reading": "goce", "az": "Pomidor"},
        {"fa": "بادمجان", "reading": "badenjan", "az": "Badımcan"},
        {"fa": "کدو", "reading": "kədu", "az": "Balqabaq"},
        {"fa": "اسفناج", "reading": "esfənac", "az": "İspanaq"},
        {"fa": "می‌کارد", "reading": "mikarəd", "az": "əkir"},
        {"fa": "می‌چیند", "reading": "miçinəd", "az": "yığır (dərir)"},
        {"fa": "پاک می‌کند", "reading": "pak mikonəd", "az": "təmizləyir"},
        {"fa": "خرد می‌کند", "reading": "xord mikonəd", "az": "xırdalayır"},
        {"fa": "چشم", "reading": "çeşm", "az": "Baş üstə! (razılıq bildirən söz)"},
        {"fa": "تعدادی", "reading": "teədadi", "az": "Bir neçə, bir qədər"},
        {"fa": "مقداری", "reading": "meqdari", "az": "Bir miqdar"},
        {"fa": "درحالِ", "reading": "dərhale", "az": "…etməkdə olarkən"},
        {"fa": "به همراهِ", "reading": "be həmrahe", "az": "…ilə birlikdə"},
        {"fa": "صدا زد", "reading": "seda zəd", "az": "səslədi"},
        {"fa": "حرکت کرد", "reading": "hərəkət kərd", "az": "hərəkət etdi"},
        {"fa": "لطفاً", "reading": "lotfən", "az": "zəhmət olmasa"},
        {"fa": "خواهش می‌کنم", "reading": "xaheş mikonəm", "az": "xahiş edirəm"},
    ],
    "grammar_notes": [
        {
            "title_az": "Əmr (buyruq) feli",
            "title_fa": "فعل امر",
            "explanation_az": (
                "Əmr feli məsdərin indiki zaman kökünə «بـ» artırmaqla düzəlir: خوردن → بخور.\n"
                "Cəm və nəzakətli formada «ید» əlavə olunur: بخورید.\n"
                "Mürəkkəb fellərdə «بـ» ikinci hissəyə qoşulur: پاک کن، مسواک بزن.\n"
                "Bəzi fellər qaydasızdır: رفتن → برو، آمدن → بیا."
            ),
            "conjugations": [
                {"pronoun_fa": "خوردن (məsdər)", "form_fa": "بخور (tək) / بخورید (cəm)"},
                {"pronoun_fa": "پاک کردن", "form_fa": "پاک کن / پاک کنید"},
                {"pronoun_fa": "مسواک زدن", "form_fa": "مسواک بزن / مسواک بزنید"},
                {"pronoun_fa": "رفتن", "form_fa": "برو / بروید"},
                {"pronoun_fa": "آمدن", "form_fa": "بیا / بیایید"},
                {"pronoun_fa": "بردن", "form_fa": "ببر / ببرید"},
                {"pronoun_fa": "آوردن", "form_fa": "بیاور / بیاورید"},
            ],
            "examples": [
                {"fa": "مادرم گفت: مریم! سبزی‌ها روی میز است، آن‌ها را پاک کن.", "reading_az": "Madərəm goft: Məryəm! Səbziha ruye miz əst, anha ra pak kon.", "az": "Anam dedi: Məryəm, göyərtilər masanın üstündədir, onları təmizlə."},
                {"fa": "بعد از غذاخوردن و قبل از خوابیدن مسواک بزنید.", "reading_az": "Bəd əz qəzaxordən va qəbl əz xabidən mesvak bezənid.", "az": "Yemək yedikdən sonra və yatmazdan əvvəl dişlərinizi fırçalayın."},
                {"fa": "بعد از نوشتن روی تابلو، آن را پاک کنید.", "reading_az": "Bəd əz neveştən ruye tablo, an ra pak konid.", "az": "Lövhəyə yazdıqdan sonra onu silin."},
                {"fa": "سارا، با این دستمال سفره را پاک کن.", "reading_az": "Sara, ba in dəstmal sofre ra pak kon.", "az": "Sara, bu salfetlə süfrəni sil."},
                {"fa": "به رنگ‌کار گفتم: امروز اتاق پذیرایی را رنگ بزن و فردا اتاق مطالعه را.", "reading_az": "Be rəngkar goftəm: emruz otaqe pəzirayi ra rəng bezən va fərda otaqe motaleə ra.", "az": "Rəngsaxa dedim: bu gün qonaq otağını, sabah isə mütaliə otağını rəngə."},
                {"fa": "مادرم گفت: قبل از رفتن به جشن تولّد دوستت، لباس‌هایت را اتو بزن.", "reading_az": "Madərəm goft: qəbl əz rəftən be cəşne touləde dustet, lebashayət ra otu bezən.", "az": "Anam dedi: dostunun ad gününə getməzdən əvvəl paltarlarını ütülə."},
                {"fa": "مادرم گفت: به آشپزخانه برو و غذایت را بخور.", "reading_az": "Madərəm goft: be aşpəzxane boro va qəzayət ra boxor.", "az": "Anam dedi: mətbəxə get və yeməyini ye."},
                {"fa": "احمد! امروز بعدازظهر برای درس خواندن به خانه‌ی ما بیا.", "reading_az": "Əhməd! Emruz bədəzzohr bəraye dərsxandən be xaneye ma bia.", "az": "Əhməd! Bu gün günortadan sonra dərs oxumaq üçün bizim evə gəl."},
                {"fa": "پدرم گفت: علی! این ساعت خراب است؛ آن را به ساعت‌سازی ببر.", "reading_az": "Pedərəm goft: Əli! In saət xərab əst; an ra be saətsazi bebər.", "az": "Atam dedi: Əli, bu saat xarabdır; onu saatsaz dükanına apar."},
                {"fa": "به تعمیرگاه برو و ماشین را بیاور.", "reading_az": "Be təmirgah boro va maşin ra biyavər.", "az": "Təmirxanaya get və maşını gətir."},
                {"fa": "میوه‌ها را بیاور و از مهمان‌ها پذیرایی کن.", "reading_az": "Miveha ra biyavər va əz mehmanha pəzirayi kon.", "az": "Meyvələri gətir və qonaqlara ikram et."},
                {"fa": "سبزی‌ها را بیاورید و پاک کنید.", "reading_az": "Səbziha ra biyavərid va pak konid.", "az": "Göyərtiləri gətirin və təmizləyin."},
                {"fa": "سرساعت هشت به کلاس بیایید.", "reading_az": "Sərsaəte həşt be kelas biyayid.", "az": "Saat düz səkkizdə sinfə gəlin."},
                {"fa": "معمولاً در گفت‌وگوی مؤدّبانه به جای امر مفرد، از امر جمع استفاده می‌کنیم: حسین آقا، غذایتان را بخورید.", "reading_az": "Məmulən dər goftoguye moəddəbane be caye əmre mofrəd, əz əmre cəm estefade mikonim: Hoseyn aqa, qəzayetan ra boxorid.", "az": "Adətən nəzakətli danışıqda tək əmr əvəzinə cəm əmr işlədirik: Hüseyn bəy, yeməyinizi yeyin."},
            ],
        },
        {
            "title_az": "«لطفاً» və «خواهش می‌کنم» quruluşları",
            "title_fa": "«لطفاً» ؛ «خواهش می‌کنم»",
            "explanation_az": (
                "Əmri nəzakətli etmək üçün cümlənin əvvəlinə «لطفاً» və ya «خواهش می‌کنم» qoyulur.\n"
                "Fel yenə də əmr formasında qalır: لطفاً بنویسید.\n"
                "«لطفاً» — zəhmət olmasa; «خواهش می‌کنم» — xahiş edirəm."
            ),
            "conjugations": [
                {"pronoun_fa": "نوشتن", "form_fa": "لطفاً بنویسید (بنویس)"},
                {"pronoun_fa": "بازکردن", "form_fa": "خواهش می‌کنم پنجره را باز کن (باز کنید)"},
                {"pronoun_fa": "بستن", "form_fa": "خواهش می‌کنم در را ببندید (ببند)"},
            ],
            "examples": [
                {"fa": "خواهش می‌کنم درس‌هایتان را خوب بخوان و تکلیف‌هایتان را بنویس.", "reading_az": "Xaheş mikonəm dərshayetan ra xub boxan va təklifhayetan ra benevis.", "az": "Xahiş edirəm dərslərini yaxşı oxu və tapşırıqlarını yaz."},
                {"fa": "لطفاً پس از بیرون رفتن از اتاق، در را ببندید.", "reading_az": "Lotfən pəs əz birun rəftən əz otaq, dər ra bebəndid.", "az": "Zəhmət olmasa otaqdan çıxdıqdan sonra qapını bağlayın."},
                {"fa": "لطفاً کتاب را باز کنید و درس پانزدهم را بخوانید.", "reading_az": "Lotfən ketab ra baz konid va dərse panzdəhom ra bexanid.", "az": "Zəhmət olmasa kitabı açın və on beşinci dərsi oxuyun."},
                {"fa": "حسین! هوا سرد است؛ لطفاً پنجره‌ها را ببند.", "reading_az": "Hoseyn! Həva sərd əst; lotfən pəncereha ra bebənd.", "az": "Hüseyn, hava soyuqdur; zəhmət olmasa pəncərələri bağla."},
                {"fa": "خواهش می‌کنم تکلیف‌هایتان را با خط زیبا بنویسید.", "reading_az": "Xaheş mikonəm təklifhayetan ra ba xətte ziba benevisid.", "az": "Xahiş edirəm tapşırıqlarınızı gözəl xətlə yazın."},
                {"fa": "لطفاً درِ کمپوت را باز کن.", "reading_az": "Lotfən dəre kompot ra baz kon.", "az": "Zəhmət olmasa kompotun qapağını aç."},
            ],
        },
        {
            "title_az": "«در حالِ» quruluşu (…etməkdə olarkən) — keçmişdə davam edən iş",
            "title_fa": "«در حالِ ........ بودم که ........»",
            "explanation_az": (
                "Bu quruluş keçmişdə DAVAM EDƏN işi bildirir: «… etməkdə idim ki, …».\n"
                "Quruluş: در حالِ + məsdər + بودم/بودی/بود… + که + ikinci iş.\n"
                "İkinci iş birinci davam edərkən baş verir və keçmiş zamanda deyilir."
            ),
            "conjugations": [
                {"pronoun_fa": "استراحت‌کردن + مادرم صدا زدن", "form_fa": "در حال استراحت کردن بودم که مادرم مرا صدا زد."},
                {"pronoun_fa": "دیدن فیلم + تلویزیون خراب‌شدن", "form_fa": "در حال دیدن فیلم بودیم که تلویزیون خراب شد."},
            ],
            "examples": [
                {"fa": "من درس خواندن بودم که دوستم آمد.", "reading_az": "Mən dərsxandən budəm ke dustəm aməd.", "az": "Mən dərs oxumaqda idim ki, dostum gəldi."},
                {"fa": "پدرم در حال غرق‌شدن بود که برادرم او را نجات داد.", "reading_az": "Pedərəm dər hale qərqşodən bud ke bəradərəm u ra necat dad.", "az": "Atam batmaqda idi ki, qardaşım onu xilas etdi."},
                {"fa": "ما در حال پاک‌کردن سبزی بودیم که مهمان‌ها آمدند.", "reading_az": "Ma dər hale pakkərdəne səbzi budim ke mehmanha amədənd.", "az": "Biz göyərti təmizləməkdə idik ki, qonaqlar gəldi."},
                {"fa": "مجید در حال تماشای باران بود که پدربزرگ او را صدا زد.", "reading_az": "Mocid dər hale təmaşaye baran bud ke pedərbozorg u ra seda zəd.", "az": "Məcid yağışa tamaşa etməkdə idi ki, babası onu səslədi."},
            ],
        },
    ],
    "exercises": [
        {
            "kind": "fill_blank",
            "instruction_az": "Uyğun əmr felini yazın.",
            "word_bank": ["بخوانید", "بزنید", "بخر", "خرد کنید", "ببند"],
            "items": [
                {
                    "fa_with_blank": "خواهش می‌کنم درس‌هایتان را خوب ___ .",
                    "correct_answer": "بخوانید",
                    "reading_az": "bexanid",
                    "az": "oxuyun",
                    "full_reading_az": "Xaheş mikonəm dərshayetan ra xub bexanid.",
                    "full_translation_az": "Xahiş edirəm dərslərinizi yaxşı oxuyun.",
                },
                {
                    "fa_with_blank": "پس از غذا و قبل از خوابیدن، مسواک ___ .",
                    "correct_answer": "بزنید",
                    "reading_az": "bezənid",
                    "az": "vurun (fırçalayın)",
                    "full_reading_az": "Pəs əz qəza va qəbl əz xabidən, mesvak bezənid.",
                    "full_translation_az": "Yeməkdən sonra və yatmazdan əvvəl dişlərinizi fırçalayın.",
                },
                {
                    "fa_with_blank": "لطفاً کتاب را باز کنید و درس پانزدهم را ___ .",
                    "correct_answer": "بخوانید",
                    "reading_az": "bexanid",
                    "az": "oxuyun",
                    "full_reading_az": "Lotfən ketab ra baz konid va dərse panzdəhom ra bexanid.",
                    "full_translation_az": "Zəhmət olmasa kitabı açın və on beşinci dərsi oxuyun.",
                },
                {
                    "fa_with_blank": "دیروز مادربزرگم گفت: حسین! به مغازه برو و سبزی ___ .",
                    "correct_answer": "بخر",
                    "reading_az": "bexər",
                    "az": "al",
                    "full_reading_az": "Diruz madərbozorgəm goft: Hoseyn! Be məğaze boro va səbzi bexər.",
                    "full_translation_az": "Dünən nənəm dedi: Hüseyn, mağazaya get və göyərti al.",
                },
                {
                    "fa_with_blank": "مادرم پس از پاک‌کردن سبزی‌ها گفت: نرگس! سبزی‌ها را ___ .",
                    "correct_answer": "خرد کنید",
                    "reading_az": "xord konid",
                    "az": "xırdalayın",
                    "full_reading_az": "Madərəm pəs əz pakkərdəne səbziha goft: Nərges! Səbziha ra xord konid.",
                    "full_translation_az": "Anam göyərtiləri təmizlədikdən sonra dedi: Nərgiz, göyərtiləri xırdala.",
                },
                {
                    "fa_with_blank": "هوا سرد است؛ لطفاً پنجره را ___ .",
                    "correct_answer": "ببند",
                    "reading_az": "bebənd",
                    "az": "bağla",
                    "full_reading_az": "Həva sərd əst; lotfən pəncere ra bebənd.",
                    "full_translation_az": "Hava soyuqdur; zəhmət olmasa pəncərəni bağla.",
                },
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Cümləni əmr felinə çevirin: «من فردا به تهران می‌روم. → شما (تو) فردا به تهران برو.»",
            "items": [
                {"prompt_fa": "ما از بازار سبزی می‌خریم و آن را پاک می‌کنیم.", "answer_fa": "شما از بازار سبزی بخرید و آن را پاک کنید.", "reading_az": "Şoma əz bazar səbzi bexərid va an ra pak konid.", "az": "Siz bazardan göyərti alın və onu təmizləyin."},
                {"prompt_fa": "شما دیروز به باغ رفتید و میوه خوردید.", "answer_fa": "شما به باغ بروید و میوه بخورید.", "reading_az": "Şoma be bağ boravid va mive bexorid.", "az": "Siz bağa gedin və meyvə yeyin."},
                {"prompt_fa": "من دیشب برای پدر و مادرم نامه نوشتم.", "answer_fa": "شما برای پدر و مادرتان نامه بنویسید.", "reading_az": "Şoma bəraye pedər va madəretan name benevisid.", "az": "Siz ata-ananız üçün məktub yazın."},
                {"prompt_fa": "آیا شما هر شب درها و پنجره‌ها را می‌بندید؟", "answer_fa": "شما هر شب درها و پنجره‌ها را ببندید.", "reading_az": "Şoma hər şəb dərha va pəncereha ra bebəndid.", "az": "Siz hər gecə qapıları və pəncərələri bağlayın."},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Nümunə kimi cümlə qurun: «استراحت‌کردن / مادرم / صدا زدن → در حال استراحت‌کردن بودم که مادرم مرا صدا زد.»",
            "items": [
                {"prompt_fa": "درس خواندن / دوستم / آمدن", "answer_fa": "در حال درس خواندن بودم که دوستم آمد.", "reading_az": "Dər hale dərsxandən budəm ke dustəm aməd.", "az": "Dərs oxumaqda idim ki, dostum gəldi."},
                {"prompt_fa": "دیدن فیلم / تلویزیون / خراب شدن", "answer_fa": "در حال دیدن فیلم بودیم که تلویزیون خراب شد.", "reading_az": "Dər hale didəne film budim ke televizion xərab şod.", "az": "Film baxmaqda idik ki, televizor xarab oldu."},
                {"prompt_fa": "غرق‌شدن / پدرم / نجات دادن", "answer_fa": "در حال غرق‌شدن بودم که پدرم مرا نجات داد.", "reading_az": "Dər hale qərqşodən budəm ke pedərəm mə ra necat dad.", "az": "Batmaqda idim ki, atam məni xilas etdi."},
                {"prompt_fa": "پاک‌کردن سبزی / مهمان‌ها / آمدن", "answer_fa": "در حال پاک‌کردن سبزی بودیم که مهمان‌ها آمدند.", "reading_az": "Dər hale pakkərdəne səbzi budim ke mehmanha amədənd.", "az": "Göyərti təmizləməkdə idik ki, qonaqlar gəldi."},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Nümunə kimi cümlə düzəldin: «من میوه پوست می‌کنم و می‌خورم. — ما / سبزی پاک‌کردن / شستن → ما سبزی را پاک می‌کنیم و می‌شوییم.»",
            "items": [
                {"prompt_fa": "ما / سبزی پاک‌کردن / شستن", "answer_fa": "ما سبزی را پاک می‌کنیم و می‌شوییم.", "reading_az": "Ma səbzi ra pak mikonim va mişuyim.", "az": "Biz göyərtini təmizləyirik və yuyuruq."},
                {"prompt_fa": "پدر بزرگم / میوه چیدن / فروختن", "answer_fa": "پدر بزرگم میوه را می‌چیند و می‌فروشد.", "reading_az": "Pedərbozorgəm mive ra miçinəd va mifəruşəd.", "az": "Babam meyvəni yığır və satır."},
                {"prompt_fa": "باغبان / درخت کاشتن / آب دادن", "answer_fa": "باغبان درخت را می‌کارد و آب می‌دهد.", "reading_az": "Bağban dərəxt ra mikarəd va ab midəhəd.", "az": "Bağban ağacı əkir və suvarır."},
                {"prompt_fa": "مادرم / کدو خرد کردن / پختن", "answer_fa": "مادرم کدو را خرد می‌کند و می‌پزد.", "reading_az": "Madərəm kədu ra xord mikonəd va mipəzəd.", "az": "Anam balqabağı xırdalayır və bişirir."},
            ],
        },
    ],
    "sentence_practice": {
        "listen_exercises": [
            {
                "items": [
                    {"fa": "باغبان‌ها در فصل تابستان و پاییز میوه‌ها را می‌چینند و می‌فروشند.", "reading_az": "Bağbanha dər fəsle tabestan va payiz miveha ra miçinənd va mifəruşənd.", "az": "Bağbanlar yay və payız fəslində meyvələri yığıb satırlar."},
                    {"fa": "سمیّه و مادرش سبزی‌ها را پاک کردند؛ سپس آن‌ها را شستند و در یخچال گذاشتند.", "reading_az": "Somayye va madərəş səbziha ra pak kərdənd; səpəs anha ra şostənd va dər yəxçal gozaştənd.", "az": "Səmiyyə və anası göyərtiləri təmizlədilər; sonra onları yudular və soyuducuya qoydular."},
                    {"fa": "ما بعضی از میوه‌ها را پوست می‌کنیم و می‌خوریم و بعضی را با پوست می‌خوریم.", "reading_az": "Ma bəzi əz miveha ra pust mikonim va mixorim va bəzi ra ba pust mixorim.", "az": "Biz meyvələrin bəzisini soyub yeyirik, bəzisini isə qabığı ilə yeyirik."},
                    {"fa": "دیشب زهرا و مادرش سبزی‌ها را خرد کردند و خورش سبزی درست کردند.", "reading_az": "Dişəb Zəhra va madərəş səbziha ra xord kərdənd va xoreşe səbzi dorost kərdənd.", "az": "Dünən gecə Zəhra və anası göyərtiləri xırdaladılar və göyərti xörəşti hazırladılar."},
                    {"fa": "در میوه‌فروشی‌ها، میوه‌های گوناگونی، مانندِ انگور، انجیر، زردآلو، موز و ... وجود دارد.", "reading_az": "Dər mivefəruşiha, mivehaye gunaguni, manənde əngur, ənjir, zərdalu, mouz va ... vocud darəd.", "az": "Meyvə mağazalarında üzüm, əncir, ərik, banan və s. kimi müxtəlif meyvələr var."},
                    {"fa": "دوستم مریض است. من دیروز دو عدد کمپوت گلابی و آناناس خریدم و برای او بردم.", "reading_az": "Dustəm məriz əst. Mən diruz do ədəd kompote goləbi va ananas xəridəm va bəraye u bordəm.", "az": "Dostum xəstədir. Mən dünən iki ədəd armud və ananas kompotu aldım və ona apardım."},
                    {"fa": "من امروز در باغچه‌ی خانه‌مان یک درخت زیتون و یک درخت انار می‌کارم.", "reading_az": "Mən emruz dər bağçeye xanemean yek dərəxte zeytun va yek dərəxte anar mikaram.", "az": "Mən bu gün evimizin bağçasında bir zeytun ağacı və bir nar ağacı əkirəm."},
                    {"fa": "امروز جشن تولّدِ برادرزاده‌ام است؛ دو شاخه گل از باغچه می‌چینم و به او هدیه می‌دهم.", "reading_az": "Emruz cəşne touləde bəradərzadeəm əst; do şaxe gol əz bağçe miçinəm va be u hedye midəham.", "az": "Bu gün qardaşımın oğlunun ad günüdür; bağçadan iki gül sapı dərib ona hədiyyə edirəm."},
                    {"fa": "پدرم یک کیلو سبزی خوردن (جعفری، ریحان، پیازچه، نعنا و تربچه) خرید و به خانه آورد.", "reading_az": "Pedərəm yek kilo səbzi xordən (cəfəri, reyhan, piyazçe, nəna va torbəçe) xərid va be xane avərd.", "az": "Atam bir kilo yaşıllıq (cəfəri, reyhan, cavan soğan, nanə və turp) aldı və evə gətirdi."},
                    {"fa": "در کارخانه‌ی کمپوت‌سازی با میوه‌های مختلف، کمپوت درست می‌کنند.", "reading_az": "Dər karxaneye kompotsazi ba mivehaye moxtəlef, kompot dorost mikonənd.", "az": "Kompot zavodunda müxtəlif meyvələrdən kompot hazırlayırlar."},
                ],
            },
        ],
        "answer_items": [],
    },
    "reading_text": {
        "title_fa": "کمک به پدربزرگ",
        "title_az": "Babaya kömək",
        "paragraphs_fa": [
            "فصل تابستان بود. حدود ساعت هشت با پدر و مادرم به طرف روستای پدربزرگم حرکت کردیم و ساعت ده و نیم صبح به خانه‌ی پدربزرگ رسیدیم. هوای روستا بسیار خنک و لذّت‌بخش بود.",
            "بعدازظهر برای تفریح و کمک به پدربزرگم به باغ رفتم. حدود ساعت پنج، هوا بارانی شد. در حال تماشای باران بودم که پدربزرگم صدا زد: مجید! جعبه‌ها را بیاور و میوه‌ها را در آن‌ها بگذار. زود به طرف جعبه‌ها رفتم و تعدادی جعبه آوردم. با کمک پدربزرگ سیب‌ها و زردآلوها را در جعبه‌ها ریختیم و مقداری از آن‌ها را برداشتیم و به خانه برگشتیم.",
            "در بین راه، پدربزرگم مقداری پول به من داد و گفت: مجید! امشب دو نفر مهمان داریم؛ دو نفر از دوستان به همراه خانواده‌شان به منزل ما می‌آیند. برو، یک کیلو سیب‌زمینی، یک کیلو تخم‌مرغ و دو تا کاهو بخر و زود بیا. گفتم: چشم! سپس به مغازه رفتم و آن چیزها را خریدم.",
            "هنگام برگشتن به خانه، پدرم را دیدم. ایشان سیب‌زمینی‌ها را از من گرفت و با هم به خانه برگشتیم. چیزهایی که خریدم به آشپزخانه بردم و روی میز گذاشتم. مادربزرگم که در حال پختن غذا بود، از من تشکّر کرد و به مادرم گفت: لطفاً سیب‌زمینی‌ها را بشوی. آن‌ها را پوست بکن و در ماهی‌تابه بریز و سرخ کن.",
            "آن شب مادربزرگ با کمک مادرم غذای خوش‌مزه‌ای پختند و از مهمان‌ها پذیرایی کردند.",
        ],
        "footnotes": [
            {"fa": "تعدادی / مقداری", "az": "bir neçə / bir miqdar"},
            {"fa": "درحالِ", "az": "…etməkdə olarkən"},
            {"fa": "به همراهِ", "az": "…ilə birlikdə"},
            {"fa": "چشم", "az": "baş üstə"},
        ],
        "full_translation_az": (
            "Yay fəsli idi. Saat təxminən səkkizdə ata-anamla babamın kəndinə tərəf yola düşdük və səhər saat "
            "on yarımda babamın evinə çatdıq. Kəndin havası çox sərin və ləzzətli idi.\n\n"
            "Günortadan sonra əyləncə üçün və babama kömək etmək üçün bağa getdim. Saat təxminən beşdə hava "
            "yağışlı oldu. Yağışa tamaşa etməkdə idim ki, babam məni səslədi: Məcid! Qutuları gətir və meyvələri "
            "onların içinə qoy. Tez qutulara tərəf getdim və bir neçə qutu gətirdim. Babamın köməyi ilə almaları "
            "və ərikləri qutulara tökdük və onların bir qismini götürüb evə qayıtdıq.\n\n"
            "Yolda babam mənə bir qədər pul verdi və dedi: Məcid! Bu gecə iki nəfər qonağımız var; dostlardan "
            "ikisi ailələri ilə birlikdə bizə gəlir. Get, bir kilo kartof, bir kilo yumurta və iki dənə kahı al "
            "və tez gəl. Dedim: Baş üstə! Sonra mağazaya getdim və o şeyləri aldım.\n\n"
            "Evə qayıdarkən atamı gördüm. O, kartofları məndən aldı və birlikdə evə qayıtdıq. Aldığım şeyləri "
            "mətbəxə apardım və masanın üstünə qoydum. Yemək bişirməkdə olan nənəm mənə təşəkkür etdi və anama "
            "dedi: Zəhmət olmasa kartofları yu. Onları soy və tavaya töküb qızart.\n\n"
            "O gecə nənəm anamın köməyi ilə dadlı bir yemək bişirdi və qonaqlara ikram etdilər."
        ),
        "sentences": [
            {
                "fa": "فصل تابستان بود.",
                "reading_az": "Fəsle tabestan bud.",
                "az": "Yay fəsli idi.",
                "new_paragraph": True,
            },
            {
                "fa": "حدود ساعت هشت با پدر و مادرم به طرف روستای پدربزرگم حرکت کردیم و ساعت ده و نیم صبح به خانه‌ی پدربزرگ رسیدیم.",
                "reading_az": "Hodude saəte həşt ba pedər va madərəm be tərəfe rustaye pedərbozorgəm hərəkət kərdim va saəte dəh-o-nim sobh be xaneye pedərbozorg residim.",
                "az": "Saat təxminən səkkizdə ata-anamla babamın kəndinə tərəf yola düşdük və səhər saat on yarımda babamın evinə çatdıq.",
            },
            {
                "fa": "هوای روستا بسیار خنک و لذّت‌بخش بود.",
                "reading_az": "Həvaye rusta besyar xonok va ləzzətbəxş bud.",
                "az": "Kəndin havası çox sərin və ləzzətli idi.",
            },
            {
                "fa": "بعدازظهر برای تفریح و کمک به پدربزرگم به باغ رفتم.",
                "reading_az": "Bədəzzohr bəraye təfrih va komək be pedərbozorgəm be bağ rəftəm.",
                "az": "Günortadan sonra əyləncə üçün və babama kömək etmək üçün bağa getdim.",
                "new_paragraph": True,
            },
            {
                "fa": "حدود ساعت پنج، هوا بارانی شد.",
                "reading_az": "Hodude saəte pənc, həva barani şod.",
                "az": "Saat təxminən beşdə hava yağışlı oldu.",
            },
            {
                "fa": "در حال تماشای باران بودم که پدربزرگم صدا زد: مجید! جعبه‌ها را بیاور و میوه‌ها را در آن‌ها بگذار.",
                "reading_az": "Dər hale təmaşaye baran budəm ke pedərbozorgəm seda zəd: Mocid! Coebeha ra biyavər va miveha ra dər anha begozar.",
                "az": "Yağışa tamaşa etməkdə idim ki, babam məni səslədi: Məcid! Qutuları gətir və meyvələri onların içinə qoy.",
            },
            {
                "fa": "زود به طرف جعبه‌ها رفتم و تعدادی جعبه آوردم.",
                "reading_az": "Zud be tərəfe coebeha rəftəm va teədadi coebe avərdəm.",
                "az": "Tez qutulara tərəf getdim və bir neçə qutu gətirdim.",
            },
            {
                "fa": "با کمک پدربزرگ سیب‌ها و زردآلوها را در جعبه‌ها ریختیم و مقداری از آن‌ها را برداشتیم و به خانه برگشتیم.",
                "reading_az": "Ba komək pedərbozorg sibha va zərdaluha ra dər coebeha rixtim va meqdari əz anha ra bərdaştim va be xane bərgəştim.",
                "az": "Babamın köməyi ilə almaları və ərikləri qutulara tökdük və onların bir qismini götürüb evə qayıtdıq.",
            },
            {
                "fa": "در بین راه، پدربزرگم مقداری پول به من داد و گفت: مجید! امشب دو نفر مهمان داریم؛ دو نفر از دوستان به همراه خانواده‌شان به منزل ما می‌آیند.",
                "reading_az": "Dər beyne rah, pedərbozorgəm meqdari pul be mən dad va goft: Mocid! Əmşəb do nəfər mehman darim; do nəfər əz dustan be həmrahe xanevadeşan be mənzele ma miayənd.",
                "az": "Yolda babam mənə bir qədər pul verdi və dedi: Məcid! Bu gecə iki nəfər qonağımız var; dostlardan ikisi ailələri ilə birlikdə bizə gəlir.",
                "new_paragraph": True,
            },
            {
                "fa": "برو، یک کیلو سیب‌زمینی، یک کیلو تخم‌مرغ و دو تا کاهو بخر و زود بیا.",
                "reading_az": "Boro, yek kilo sibzəmini, yek kilo toxme-morğ va do ta kahu bexər va zud bia.",
                "az": "Get, bir kilo kartof, bir kilo yumurta və iki dənə kahı al və tez gəl.",
            },
            {
                "fa": "گفتم: چشم! سپس به مغازه رفتم و آن چیزها را خریدم.",
                "reading_az": "Goftəm: çeşm! Səpəs be məğaze rəftəm va an çizha ra xəridəm.",
                "az": "Dedim: Baş üstə! Sonra mağazaya getdim və o şeyləri aldım.",
            },
            {
                "fa": "هنگام برگشتن به خانه، پدرم را دیدم.",
                "reading_az": "Hengame bərgəştən be xane, pedərəm ra didəm.",
                "az": "Evə qayıdarkən atamı gördüm.",
                "new_paragraph": True,
            },
            {
                "fa": "ایشان سیب‌زمینی‌ها را از من گرفت و با هم به خانه برگشتیم.",
                "reading_az": "İşan sibzəminiha ra əz mən gereft va ba həm be xane bərgəştim.",
                "az": "O, kartofları məndən aldı və birlikdə evə qayıtdıq.",
            },
            {
                "fa": "چیزهایی که خریدم به آشپزخانه بردم و روی میز گذاشتم.",
                "reading_az": "Çizhayi ke xəridəm be aşpəzxane bordəm va ruye miz gozaştəm.",
                "az": "Aldığım şeyləri mətbəxə apardım və masanın üstünə qoydum.",
            },
            {
                "fa": "مادربزرگم که در حال پختن غذا بود، از من تشکّر کرد و به مادرم گفت: لطفاً سیب‌زمینی‌ها را بشوی.",
                "reading_az": "Madərbozorgəm ke dər hale poxtəne qəza bud, əz mən təşəkkor kərd va be madərəm goft: lotfən sibzəminiha ra bešuy.",
                "az": "Yemək bişirməkdə olan nənəm mənə təşəkkür etdi və anama dedi: Zəhmət olmasa kartofları yu.",
            },
            {
                "fa": "آن‌ها را پوست بکن و در ماهی‌تابه بریز و سرخ کن.",
                "reading_az": "Anha ra pust bekon va dər mahitabe beriz va sorx kon.",
                "az": "Onları soy və tavaya töküb qızart.",
            },
            {
                "fa": "آن شب مادربزرگ با کمک مادرم غذای خوش‌مزه‌ای پختند و از مهمان‌ها پذیرایی کردند.",
                "reading_az": "An šəb madərbozorg ba komək madərəm qəzaye xošmazei poxtənd va əz mehmanha pəzirayi kərdənd.",
                "az": "O gecə nənəm anamın köməyi ilə dadlı bir yemək bişirdi və qonaqlara ikram etdilər.",
                "new_paragraph": True,
            },
        ],
        "comprehension_questions": [
            {
                "question_fa": "مجید و خانواده‌اش ساعت چند به طرف روستا حرکت کردند؟",
                "reading_az": "Mocid va xanevadeəş saəte çənd be tərəfe rusta hərəkət kərdənd?",
                "az": "Məcid və ailəsi saat neçədə kəndə tərəf yola düşdülər?",
                "sample_answer_fa": "مجید و خانواده‌اش حدود ساعت هشت به طرف روستای پدربزرگ حرکت کردند.",
                "sample_answer_reading_az": "Mocid va xanevadeəş hodude saəte həşt be tərəfe rustaye pedərbozorg hərəkət kərdənd.",
                "sample_answer_az": "Məcid və ailəsi saat təxminən səkkizdə babasının kəndinə tərəf yola düşdülər.",
            },
            {
                "question_fa": "آن‌ها ساعت چند به خانه‌ی پدربزرگ رسیدند؟",
                "reading_az": "Anha saəte çənd be xaneye pedərbozorg residənd?",
                "az": "Onlar babasının evinə saat neçədə çatdılar?",
                "sample_answer_fa": "آن‌ها ساعت ده و نیم صبح به خانه‌ی پدربزرگ رسیدند.",
                "sample_answer_reading_az": "Anha saəte dəh-o-nim sobh be xaneye pedərbozorg residənd.",
                "sample_answer_az": "Onlar səhər saat on yarımda babasının evinə çatdılar.",
            },
            {
                "question_fa": "مجید برای چه کاری به باغ پدربزرگش رفت؟",
                "reading_az": "Mocid bəraye çe kari be bağe pedərbozorgəş rəft?",
                "az": "Məcid nə üçün babasının bağına getdi?",
                "sample_answer_fa": "مجید برای تفریح و کمک به پدربزرگش به باغ رفت.",
                "sample_answer_reading_az": "Mocid bəraye təfrih va komək be pedərbozorgəş be bağ rəft.",
                "sample_answer_az": "Məcid əyləncə üçün və babasına kömək etmək üçün bağa getdi.",
            },
            {
                "question_fa": "مجید درحال چه کاری بود که پدربزرگ او را صدا زد؟",
                "reading_az": "Mocid dərhale çe kari bud ke pedərbozorg u ra seda zəd?",
                "az": "Babası onu səslədiyi zaman Məcid nə etməkdə idi?",
                "sample_answer_fa": "مجید در حال تماشای باران بود که پدربزرگ او را صدا زد.",
                "sample_answer_reading_az": "Mocid dər hale təmaşaye baran bud ke pedərbozorg u ra seda zəd.",
                "sample_answer_az": "Məcid yağışa tamaşa etməkdə idi ki, babası onu səslədi.",
            },
            {
                "question_fa": "پدربزرگ، وقتی مجید را صدا زد، چه گفت؟",
                "reading_az": "Pedərbozorg, vəqti Mocid ra seda zəd, çe goft?",
                "az": "Babası Məcidi səslədiyi zaman nə dedi?",
                "sample_answer_fa": "پدربزرگ گفت: مجید! جعبه‌ها را بیاور و میوه‌ها را در آن‌ها بگذار.",
                "sample_answer_reading_az": "Pedərbozorg goft: Mocid! Coebeha ra biyavər va miveha ra dər anha begozar.",
                "sample_answer_az": "Babası dedi: Məcid! Qutuları gətir və meyvələri onların içinə qoy.",
            },
            {
                "question_fa": "مجید برای چه کاری به مغازه رفت؟",
                "reading_az": "Mocid bəraye çe kari be məğaze rəft?",
                "az": "Məcid nə üçün mağazaya getdi?",
                "sample_answer_fa": "مجید برای خریدن سیب‌زمینی، تخم‌مرغ و کاهو به مغازه رفت.",
                "sample_answer_reading_az": "Mocid bəraye xəridəne sibzəmini, toxme-morğ va kahu be məğaze rəft.",
                "sample_answer_az": "Məcid kartof, yumurta və kahı almaq üçün mağazaya getdi.",
            },
            {
                "question_fa": "مادربزرگ به مادر مجید چه گفت؟",
                "reading_az": "Madərbozorg be madəre Mocid çe goft?",
                "az": "Nənəsi Məcidin anasına nə dedi?",
                "sample_answer_fa": "مادربزرگ گفت: لطفاً سیب‌زمینی‌ها را بشوی. آن‌ها را پوست بکن و در ماهی‌تابه بریز و سرخ کن.",
                "sample_answer_reading_az": "Madərbozorg goft: lotfən sibzəminiha ra bešuy. Anha ra pust bekon va dər mahitabe beriz va sorx kon.",
                "sample_answer_az": "Nənəsi dedi: Zəhmət olmasa kartofları yu. Onları soy və tavaya töküb qızart.",
            },
        ],
    },
}
