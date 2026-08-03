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
        # səh. 204-206 — mətndə və çalışmalarda işlənən əlavə sözlər
        {"fa": "جعبه", "reading": "coebe", "az": "Qutu, yeşik"},
        {"fa": "سبد", "reading": "səbəd", "az": "Səbət"},
        {"fa": "برداشت", "reading": "bərdaşt", "az": "götürdü"},
        {"fa": "گذاشت", "reading": "gozaşt", "az": "qoydu"},
        {"fa": "ریخت", "reading": "rixt", "az": "tökdü"},
        {"fa": "نجات داد", "reading": "necat dad", "az": "xilas etdi"},
        {"fa": "غرق شد", "reading": "qərq şod", "az": "batdı, suya qərq oldu"},
        {"fa": "اتو زدن", "reading": "otu zədən", "az": "ütüləmək"},
        {"fa": "انتخاب کردن", "reading": "entexab kərdən", "az": "seçmək"},
        {"fa": "نماز خواندن", "reading": "nəmaz xandən", "az": "namaz qılmaq"},
        {"fa": "مسواک زدن", "reading": "mesvak zədən", "az": "diş fırçalamaq"},
        {"fa": "خورش سبزی", "reading": "xoreşe səbzi", "az": "Göyərti xörəşti"},
        {"fa": "میوه‌فروشی", "reading": "mivefəruşi", "az": "Meyvə mağazası"},
        {"fa": "کارخانه‌ی کمپوت‌سازی", "reading": "karxaneye kompotsazi", "az": "Kompot zavodu"},
        {"fa": "گوناگون", "reading": "gunagun", "az": "müxtəlif, rəngarəng"},
        {"fa": "خنک", "reading": "xonok", "az": "sərin"},
        {"fa": "لذّت‌بخش", "reading": "ləzzətbəxş", "az": "ləzzətli, xoş"},
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
            # səh. 201 və 203 — dərslikdəki nömrələnmiş qeydlər
            "note_fa": (
                "۱. واژه‌های «بخر» و «بخرید» فعل امر از مصدر «خریدن» هستند.\n"
                "۲. فعل امر فقط در دو صیغه‌ی «تو» و «شما» به کار می‌رود؛ پس ابتدا ضمیر «من» را به ضمیر «تو» "
                "تبدیل می‌کنیم و سپس «فعل مضارع» را تبدیل به «فعل امر» می‌کنیم:\n"
                "من فردا به تهران می‌روم. ← شما (تو) فردا به تهران برو.\n"
                "● «قید زمان گذشته» و «واژه‌ی پرسشی» در جمله‌های امری حذف می‌شوند:\n"
                "آیا شما دیروز بعد از غذا مسواک زدید؟ ← شما بعد از غذا مسواک بزنید.\n"
                "● معمولاً در گفت‌وگوی مؤدّبانه به جای امر مفرد، از امر جمع استفاده می‌کنیم: "
                "حسین آقا، غذایتان را بخورید."
            ),
            "note_reading_az": (
                "1. «Bexər» va «bexərid» fele əmr əz məsdəre «xəridən» həstənd.\n"
                "2. Fele əmr fəqət dər do siğeye «to» va «şoma» be kar mirəvəd; pəs ebteda zəmire «mən» ra "
                "be zəmire «to» təbdil mikonim va səpəs «fele mozare» ra təbdil be «fele əmr» mikonim:\n"
                "Mən fərda be Tehran mirəvəm. ← Şoma (to) fərda be Tehran boro.\n"
                "Qeyde zəmane gozəşte va vaceye porseşi dər comlehaye əmri həzf mişəvənd."
            ),
            "note_az": (
                "1. «بخر» və «بخرید» sözləri «خریدن» (almaq) məsdərindən düzələn əmr felləridir.\n"
                "2. Əmr feli YALNIZ iki şəxsdə işlənir — «تو» (sən) və «شما» (siz).\n"
                "Ona görə cümləni əmrə çevirəndə əvvəlcə «من» əvəzliyini «تو/شما» ilə əvəz edirik, "
                "sonra indiki zaman felini əmr felinə çeviririk:\n"
                "من فردا به تهران می‌روم → شما (تو) فردا به تهران برو.\n"
                "● Əmr cümləsində KEÇMİŞ ZAMAN zərfi (دیروز، دیشب) və SUAL sözü (آیا، چه) ATILIR:\n"
                "آیا شما دیروز بعد از غذا مسواک زدید؟ → شما بعد از غذا مسواک بزنید.\n"
                "● Nəzakətli danışıqda tək əmr əvəzinə cəm əmr işlədilir."
            ),
            "drills": [
                {
                    "title_fa": "مانند مثال بگویید",
                    "instruction_az": "Məsdərdən dörd formanı deyin: «مسواک زدن: مسواک زدم / مسواک می‌زنم / مسواک بزن / مسواک بزنید»",
                    "items": [
                        {"prompt_fa": "خوردن", "answer_fa": "خوردم؛ می‌خورم؛ بخور؛ بخورید", "reading_az": "Xordəm; mixorəm; boxor; boxorid.", "az": "yedim; yeyirəm; ye; yeyin"},
                        {"prompt_fa": "نوشتن", "answer_fa": "نوشتم؛ می‌نویسم؛ بنویس؛ بنویسید", "reading_az": "Neveştəm; minevisəm; benevis; benevisid.", "az": "yazdım; yazıram; yaz; yazın"},
                        {"prompt_fa": "رفتن", "answer_fa": "رفتم؛ می‌روم؛ برو؛ بروید", "reading_az": "Rəftəm; mirəvəm; boro; bərəvid.", "az": "getdim; gedirəm; get; gedin — qaydasızdır"},
                        {"prompt_fa": "آمدن", "answer_fa": "آمدم؛ می‌آیم؛ بیا؛ بیایید", "reading_az": "Amədəm; miayəm; bia; biyayid.", "az": "gəldim; gəlirəm; gəl; gəlin — qaydasızdır"},
                    ],
                },
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
            # səh. 202 — «لطفاً توجّه کنید» qutusundakı dörd nümunə
            "note_fa": (
                "نوشتن ← لطفاً بنویس (بنویسید).\n"
                "خواندن ← خواهش می‌کنم بخوان (بخوانید).\n"
                "بستن ← خواهش می‌کنم در را ببند (ببندید).\n"
                "بازکردن ← لطفاً پنجره را باز کن (باز کنید)."
            ),
            "note_reading_az": (
                "Neveştən ← lotfən benevis (benevisid).\n"
                "Xandən ← xaheş mikonəm bexan (bexanid).\n"
                "Bəstən ← xaheş mikonəm dər ra bebənd (bebəndid).\n"
                "Baz kərdən ← lotfən pəncere ra baz kon (baz konid)."
            ),
            "note_az": (
                "Dərslikdəki dörd nümunə:\n"
                "yazmaq → zəhmət olmasa yaz (yazın).\n"
                "oxumaq → xahiş edirəm oxu (oxuyun).\n"
                "bağlamaq → xahiş edirəm qapını bağla (bağlayın).\n"
                "açmaq → zəhmət olmasa pəncərəni aç (açın).\n"
                "Mötərizədəki forma NƏZAKƏTLİ (cəm) formadır."
            ),
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
            # səh. 206 — dərslikdəki nümunə və alt qeyd «۱. مرا: من را»
            "note_fa": (
                "استراحت‌کردن / مادرم / صدا زدن\n"
                "← در حال استراحت کردن بودم که مادرم مرا صدا زد.\n"
                "۱. مرا = من را"
            ),
            "note_reading_az": (
                "Esterahət kərdən / madərəm / seda zədən\n"
                "← Dər hale esterahət kərdən budəm ke madərəm mə ra seda zəd.\n"
                "1. Mə ra = mən ra"
            ),
            "note_az": (
                "Verilən sözlər: MƏSDƏR / İKİNCİ ŞƏXS / İKİNCİ İŞ.\n"
                "Quruluş: در حالِ + MƏSDƏR + بودم که + İKİNCİ İŞ (keçmiş zamanda).\n"
                "«مرا» sözü «من را»nın qısaldılmış formasıdır — «məni» deməkdir.\n"
                "Tərcümə: İstirahət etməkdə idim ki, anam məni səslədi."
            ),
        },
        {
            # səh. 205 — dərslikdəki alt qeyd: mürəkkəb və qaydasız fellərin əmr forması
            "title_az": "Qaydasız və mürəkkəb fellərin əmr forması",
            "title_fa": "فعل امرِ فعل‌های بی‌قاعده و مرکّب",
            "explanation_az": (
                "Bəzi fellərin əmr forması qaydaya uyğun deyil — onları əzbərləmək lazımdır.\n"
                "Mürəkkəb fellərdə «بـ» ADƏTƏN atılır: پاک کن، سرخ کن، انتخاب کن.\n"
                "Ancaq dərslikdə «پوست بکن» və «سرخ بکن» kimi «بـ»-li formalar da göstərilib — hər ikisi düzgündür.\n"
                "Danışıq dilində «بشوی» əvəzinə «بشور» deyilir."
            ),
            "conjugations": [
                {"pronoun_fa": "گذاشتن", "form_fa": "بگذار / بگذارید"},
                {"pronoun_fa": "شستن", "form_fa": "بشوی / بشویید (گفتاری: بشور)"},
                {"pronoun_fa": "پوست کندن", "form_fa": "پوست بکن / پوست بکنید"},
                {"pronoun_fa": "سرخ کردن", "form_fa": "سرخ بکن / سرخ بکنید"},
                {"pronoun_fa": "ریختن", "form_fa": "بریز / بریزید"},
                {"pronoun_fa": "خریدن", "form_fa": "بخر / بخرید"},
                {"pronoun_fa": "بستن", "form_fa": "ببند / ببندید"},
                {"pronoun_fa": "نوشتن", "form_fa": "بنویس / بنویسید"},
                {"pronoun_fa": "خواندن", "form_fa": "بخوان / بخوانید"},
                {"pronoun_fa": "دیدن", "form_fa": "ببین / ببینید"},
            ],
            "examples": [
                {"fa": "لطفاً سیب‌زمینی‌ها را بشوی.", "reading_az": "Lotfən sibzəminiha ra bəşuy.", "az": "Zəhmət olmasa kartofları yu."},
                {"fa": "آن‌ها را پوست بکن و در ماهی‌تابه بریز و سرخ کن.", "reading_az": "Anha ra pust bekon va dər mahitabe beriz va sorx kon.", "az": "Onları soy, tavaya tök və qızart."},
                {"fa": "میوه‌ها را در سبد بگذار.", "reading_az": "Miveha ra dər səbəd begozar.", "az": "Meyvələri səbətə qoy."},
                {"fa": "میوه‌ها را در سبد بگذارید.", "reading_az": "Miveha ra dər səbəd begozarid.", "az": "Meyvələri səbətə qoyun. — nəzakətli (cəm) forma."},
                {"fa": "جعبه‌ها را بیاور و میوه‌ها را در آن بگذار.", "reading_az": "Coebeha ra biyavər va miveha ra dər an begozar.", "az": "Qutuları gətir və meyvələri onun içinə qoy."},
            ],
            "drills": [
                {
                    "title_fa": "فعل امر بگویید",
                    "instruction_az": "Məsdəri əmr felinə çevirin (tək və cəm)",
                    "items": [
                        {"prompt_fa": "گذاشتن", "answer_fa": "بگذار / بگذارید", "reading_az": "Begozar / begozarid.", "az": "qoy / qoyun"},
                        {"prompt_fa": "شستن", "answer_fa": "بشوی / بشویید", "reading_az": "Bəşuy / bəşuyid.", "az": "yu / yuyun (danışıqda: بشور)"},
                        {"prompt_fa": "پوست کندن", "answer_fa": "پوست بکن / پوست بکنید", "reading_az": "Pust bekon / pust bekonid.", "az": "soy / soyun"},
                        {"prompt_fa": "سرخ کردن", "answer_fa": "سرخ بکن / سرخ بکنید", "reading_az": "Sorx bekon / sorx bekonid.", "az": "qızart / qızardın"},
                    ],
                },
            ],
        },
        {
            # səh. 198 — «کاشتن» və «چیدن» fellərinin indiki zaman cədvəli
            "title_az": "«کاشتن» (əkmək) və «چیدن» (dərmək) fellərinin indiki zamanı",
            "title_fa": "«کاشتن» ؛ «چیدن» — فعل مضارع",
            "explanation_az": (
                "Bu iki felin indiki zaman kökü məsdərdən fərqlidir və onu yadda saxlamaq lazımdır:\n"
                "کاشتن → کار (می‌کارم)، چیدن → چین (می‌چینم).\n"
                "Əmr forması da həmin kökdən düzəlir: بکار / بچین."
            ),
            "conjugations": [
                {"pronoun_fa": "کاشتن", "form_fa": "می‌کارم؛ می‌کاری؛ می‌کارد؛ می‌کاریم؛ می‌کارید؛ می‌کارند"},
                {"pronoun_fa": "چیدن", "form_fa": "می‌چینم؛ می‌چینی؛ می‌چیند؛ می‌چینیم؛ می‌چینید؛ می‌چینند"},
                {"pronoun_fa": "امر", "form_fa": "بکار / بکارید — بچین / بچینید"},
            ],
            "examples": [
                {"fa": "من امروز در باغچه‌ی خانه‌مان یک درخت زیتون می‌کارم.", "reading_az": "Mən emruz dər bağçeye xaneman yek dərəxte zeytun mikarəm.", "az": "Mən bu gün evimizin bağçasında bir zeytun ağacı əkirəm."},
                {"fa": "باغبان‌ها در فصل تابستان و پاییز میوه‌ها را می‌چینند.", "reading_az": "Bağbanha dər fəsle tabestan va payiz miveha ra miçinənd.", "az": "Bağbanlar yay və payız fəslində meyvələri dərirlər."},
                {"fa": "دو شاخه گل از باغچه می‌چینم و به او هدیه می‌دهم.", "reading_az": "Do şaxe gol əz bağçe miçinəm va be u hedye midəhəm.", "az": "Bağçadan iki gül sapı dərib ona hədiyyə edirəm."},
                {"fa": "کشاورز، بذر را در زمین می‌کارد.", "reading_az": "Keşavərz, bəzr ra dər zəmin mikarəd.", "az": "Əkinçi toxumu torpağa əkir."},
            ],
        },
        {
            # səh. 205 — dərslikdəki keçmiş zaman cədvəli
            "title_az": "Mətndəki fellərin keçmiş zamanı (təsrif cədvəli)",
            "title_fa": "فعل ماضی — رسیدن؛ آوردن؛ صدا زدن؛ برداشتن؛ گذاشتن؛ پختن؛ دیدن؛ گرفتن",
            "explanation_az": (
                "Keçmiş zaman məsdərdən «ـن» atılmaqla düzəlir: رسیدن → رسید.\n"
                "Sonra şəxs şəkilçiləri artırılır: ـم، ـی، (—)، ـیم، ـید، ـند.\n"
                "III şəxs təkdə HEÇ BİR şəkilçi əlavə olunmur: او رسید."
            ),
            "conjugations": [
                {"pronoun_fa": "رسیدن", "form_fa": "رسیدم؛ رسیدی؛ رسید؛ رسیدیم؛ رسیدید؛ رسیدند"},
                {"pronoun_fa": "آوردن", "form_fa": "آوردم؛ آوردی؛ آورد؛ آوردیم؛ آوردید؛ آوردند"},
                {"pronoun_fa": "صدا زدن", "form_fa": "صدا زدم؛ صدا زدی؛ صدا زد؛ صدا زدیم؛ صدا زدید؛ صدا زدند"},
                {"pronoun_fa": "برداشتن", "form_fa": "برداشتم؛ برداشتی؛ برداشت؛ برداشتیم؛ برداشتید؛ برداشتند"},
                {"pronoun_fa": "گذاشتن", "form_fa": "گذاشتم؛ گذاشتی؛ گذاشت؛ گذاشتیم؛ گذاشتید؛ گذاشتند"},
                {"pronoun_fa": "پختن", "form_fa": "پختم؛ پختی؛ پخت؛ پختیم؛ پختید؛ پختند"},
                {"pronoun_fa": "دیدن", "form_fa": "دیدم؛ دیدی؛ دید؛ دیدیم؛ دیدید؛ دیدند"},
                {"pronoun_fa": "گرفتن", "form_fa": "گرفتم؛ گرفتی؛ گرفت؛ گرفتیم؛ گرفتید؛ گرفتند"},
            ],
            "examples": [
                {"fa": "ساعت ده و نیم صبح به خانه‌ی پدربزرگ رسیدیم.", "reading_az": "Saəte dəh-o-nim sobh be xaneye pedərbozorg residim.", "az": "Səhər saat on yarımda babamın evinə çatdıq."},
                {"fa": "تعدادی جعبه آوردم.", "reading_az": "Teədadi coebe avərdəm.", "az": "Bir neçə qutu gətirdim."},
                {"fa": "پدربزرگم صدا زد: مجید!", "reading_az": "Pedərbozorgəm seda zəd: Mocid!", "az": "Babam səslədi: Məcid!"},
                {"fa": "مقداری از آن‌ها را برداشتیم.", "reading_az": "Meqdari əz anha ra bərdaştim.", "az": "Onların bir qismini götürdük."},
                {"fa": "چیزها را روی میز گذاشتم.", "reading_az": "Çizha ra ruye miz gozaştəm.", "az": "Şeyləri masanın üstünə qoydum."},
                {"fa": "مادربزرگ غذای خوش‌مزه‌ای پخت.", "reading_az": "Madərbozorg qəzaye xoşməzei poxt.", "az": "Nənəm dadlı bir yemək bişirdi."},
                {"fa": "هنگام برگشتن به خانه، پدرم را دیدم.", "reading_az": "Hengame bərgəştən be xane, pedərəm ra didəm.", "az": "Evə qayıdarkən atamı gördüm."},
                {"fa": "ایشان سیب‌زمینی‌ها را از من گرفت.", "reading_az": "İşan sibzəminiha ra əz mən gereft.", "az": "O, kartofları məndən aldı."},
            ],
        },
    ],
    "exercises": [
        {
            # Çalışma 1 — səh. 198 «برای هر تصویر، جمله بگویید».
            # Dərslikdə 8 şəkil var; aşağıda «کاشتن / چیدن» cədvəli və dörd cümlə qəlibi verilib:
            # «..... را در ..... می‌کارد.» / «..... را از ..... می‌چیند.» /
            # «..... را پاک می‌کند.» / «..... را خرد می‌کند.»
            "kind": "picture_sentences",
            "title_fa": "برای هر تصویر، جمله بگویید",
            "instruction_az": "Hər şəkil üçün cümlə deyin («می‌کارد / می‌چیند / پاک می‌کند / خرد می‌کند»)",
            "example_fa": "کاشتن: می‌کارم؛ می‌کاری؛ می‌کارد؛ می‌کاریم؛ می‌کارید؛ می‌کارند\nچیدن: می‌چینم؛ می‌چینی؛ می‌چیند؛ می‌چینیم؛ می‌چینید؛ می‌چینند",
            "example_reading_az": "Kaştən: mikarəm; mikari; mikarəd; mikarim; mikarid; mikarənd.\nÇidən: miçinəm; miçini; miçinəd; miçinim; miçinid; miçinənd.",
            "example_az": (
                "Dörd cümlə qəlibi:\n"
                "«… را در … می‌کارد.» — …-i …-də əkir.\n"
                "«… را از … می‌چیند.» — …-i …-dən dərir.\n"
                "«… را پاک می‌کند.» — …-i təmizləyir.\n"
                "«… را خرد می‌کند.» — …-i xırdalayır."
            ),
            "example_answer_fa": "باغبان، درخت را در باغ می‌کارد.",
            "example_answer_reading_az": "Bağban, dərəxt ra dər bağ mikarəd.",
            "example_answer_az": "Bağban ağacı bağda əkir.",
            "items": [
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این سبزی است.", "reading_az": "İn səbzi əst.", "az": "Bu göyərtidir."},
                        {"fa": "مادرم سبزی را پاک می‌کند و خرد می‌کند.", "reading_az": "Madərəm səbzi ra pak mikonəd va xord mikonəd.", "az": "Anam göyərtini təmizləyir və xırdalayır."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این توت‌فرنگی است.", "reading_az": "İn tute-fərəngi əst.", "az": "Bu çiyələkdir."},
                        {"fa": "کشاورز، توت‌فرنگی را در مزرعه می‌کارد و می‌چیند.", "reading_az": "Keşavərz, tute-fərəngi ra dər məzrəe mikarəd va miçinəd.", "az": "Əkinçi çiyələyi tarlada əkir və dərir."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این اسفناج است.", "reading_az": "İn esfənac əst.", "az": "Bu ispanaqdır."},
                        {"fa": "مادربزرگم اسفناج را پاک می‌کند و می‌شوید.", "reading_az": "Madərbozorgəm esfənac ra pak mikonəd va mişuyəd.", "az": "Nənəm ispanağı təmizləyir və yuyur."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این‌ها آلو و زردآلو هستند.", "reading_az": "İnha alu va zərdalu həstənd.", "az": "Bunlar gavalı və ərikdir."},
                        {"fa": "پدربزرگم آلو و زردآلو را از درخت می‌چیند.", "reading_az": "Pedərbozorgəm alu va zərdalu ra əz dərəxt miçinəd.", "az": "Babam gavalını və əriyi ağacdan dərir."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "او سبزی‌ها و قارچ را خرد می‌کند.", "reading_az": "U səbziha va qarç ra xord mikonəd.", "az": "O, göyərtiləri və göbələyi xırdalayır."},
                        {"fa": "مادرم سبزی‌ها را با چاقو خرد می‌کند.", "reading_az": "Madərəm səbziha ra ba çaqu xord mikonəd.", "az": "Anam göyərtiləri bıçaqla xırdalayır."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "پسر، سیب‌ها را از درخت می‌چیند.", "reading_az": "Pesər, sibha ra əz dərəxt miçinəd.", "az": "Oğlan almaları ağacdan dərir."},
                        {"fa": "او میوه‌ها را در سبد می‌گذارد.", "reading_az": "U miveha ra dər səbəd migozarəd.", "az": "O, meyvələri səbətə qoyur."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "باغبان، نهال را در زمین می‌کارد.", "reading_az": "Bağban, nəhal ra dər zəmin mikarəd.", "az": "Bağban tinginin şitilini torpağa əkir."},
                        {"fa": "او پس از کاشتن، به نهال آب می‌دهد.", "reading_az": "U pəs əz kaştən, be nəhal ab midəhəd.", "az": "O, əkdikdən sonra tingi suvarır."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "او تربچه‌ها را پاک می‌کند.", "reading_az": "U torbəçeha ra pak mikonəd.", "az": "O, turpları təmizləyir."},
                        {"fa": "سپس تربچه‌ها را می‌شوید و در بشقاب می‌گذارد.", "reading_az": "Səpəs torbəçeha ra mişuyəd va dər boşqab migozarəd.", "az": "Sonra turpları yuyur və boşqaba qoyur."},
                    ],
                },
            ],
        },
        {
            # Çalışma 2 — səh. 203 «کامل کنید» (sadələşdirilmiş, bir boşluqlu variant).
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
            # Çalışma 3 — səh. 203 «کامل کنید» (dərslikdəki ORİJİNAL şəkil).
            # Hər bənddə iki boşluq var (4-cü bənddə bir boşluq), ona görə multi_blank.
            "kind": "multi_blank",
            "title_fa": "کامل کنید",
            "instruction_az": "Söz bankından uyğun əmr felini (və məsdəri) seçib boşluqları doldurun",
            "example_fa": "لطفاً غذایتان را ___ و درس‌هایتان را ___ .\nلطفاً غذایتان را *بخورید* و درس‌هایتان را *بخوانید*.",
            "example_reading_az": "Lotfən qəzayetan ra boxorid va dərshayetan ra bexanid.",
            "example_az": (
                "Zəhmət olmasa yeməyinizi yeyin və dərslərinizi oxuyun.\n"
                "Diqqət: «لطفاً» və «خواهش می‌کنم» cümlədə olsa da, fel ƏMR formasında qalır.\n"
                "«پس از» və «قبل از» ön qoşmalarından sonra fel MƏSDƏR olur (خوردنِ، پاک کردنِ), əmr yox."
            ),
            # 9 boşluq = 9 çip.
            "word_bank": [
                "کن", "بنویس", "خوردنِ", "بزنید",
                "بخورید", "بخوانید", "برو", "کردنِ", "کن",
            ],
            "items": [
                {
                    "fa_with_blanks": "خواهش می‌کنم مطالعه ___ و تکلیف‌ها را ___ .",
                    "correct_answers": ["کن", "بنویس"],
                    "full_reading_az": "Xaheş mikonəm motaleə kon va təklifha ra benevis.",
                    "full_translation_az": "Xahiş edirəm mütaliə et və tapşırıqları yaz. — «مطالعه کردن» mürəkkəb feldir, əmri «مطالعه کن».",
                },
                {
                    "fa_with_blanks": "پس از ___ غذا و قبل از خوابیدن، مسواک ___ .",
                    "correct_answers": ["خوردنِ", "بزنید"],
                    "full_reading_az": "Pəs əz xordəne qəza va qəbl əz xabidən, mesvak bezənid.",
                    "full_translation_az": "Yemək yedikdən sonra və yatmazdan əvvəl dişlərinizi fırçalayın. — «پس از» sonra MƏSDƏR gəlir: خوردنِ غذا.",
                },
                {
                    "fa_with_blanks": "لطفاً غذایتان را ___ و درس‌هایتان را ___ .",
                    "correct_answers": ["بخورید", "بخوانید"],
                    "full_reading_az": "Lotfən qəzayetan ra boxorid va dərshayetan ra bexanid.",
                    "full_translation_az": "Zəhmət olmasa yeməyinizi yeyin və dərslərinizi oxuyun. — «ـتان» şəkilçisi cəm/nəzakətli formanı tələb edir.",
                },
                {
                    "fa_with_blanks": "دیروز مادربزرگم گفت: حسین! به مغازه ___ و سبزی بخر.",
                    "correct_answers": ["برو"],
                    "full_reading_az": "Diruz madərbozorgəm goft: Hoseyn! Be məğaze boro va səbzi bexər.",
                    "full_translation_az": "Dünən nənəm dedi: Hüseyn, mağazaya get və göyərti al. — «رفتن» qaydasızdır: برو.",
                },
                {
                    "fa_with_blanks": "مادرم پس از پاک ___ سبزی‌ها گفت: نرگس! سبزی‌ها را خرد ___ .",
                    "correct_answers": ["کردنِ", "کن"],
                    "full_reading_az": "Madərəm pəs əz pak kərdəne səbziha goft: Nərges! Səbziha ra xord kon.",
                    "full_translation_az": "Anam göyərtiləri təmizlədikdən sonra dedi: Nərgiz, göyərtiləri xırdala. — birinci boşluq MƏSDƏR (پاک کردنِ), ikinci ƏMR (خرد کن).",
                },
            ],
        },
        {
            # Çalışma 4 — səh. 203 «مانند مثال بگویید».
            # Nümunə: مسواک زدن → مسواک زدم / مسواک می‌زنم / مسواک بزن / مسواک بزنید
            "kind": "answer_question",
            "title_fa": "مانند مثال بگویید",
            "instruction_az": "Hər məsdərin dörd formasını deyin: keçmiş / indiki / əmr (tək) / əmr (cəm)",
            "example_fa": "مسواک زدن: مسواک *زدم* — مسواک *می‌زنم* — مسواک *بزن* — مسواک *بزنید*",
            "example_reading_az": "Mesvak zədən: mesvak zədəm — mesvak mizənəm — mesvak bezən — mesvak bezənid.",
            "example_az": (
                "Dörd sütun bunlardır:\n"
                "1) KEÇMİŞ (من … زدم) — «diş fırçaladım»\n"
                "2) İNDİKİ (من … می‌زنم) — «diş fırçalayıram»\n"
                "3) ƏMR TƏK (تو … بزن) — «fırçala»\n"
                "4) ƏMR CƏM/NƏZAKƏTLİ (شما … بزنید) — «fırçalayın»\n"
                "Mürəkkəb fellərdə yalnız ikinci hissə dəyişir: مسواک + زدن."
            ),
            "items": [
                {"fa": "اتو زدن", "reading_az": "Otu zədən", "az": "ütüləmək",
                 "sample_answer_fa": "اتو زدم — اتو می‌زنم — اتو بزن — اتو بزنید",
                 "sample_answer_reading_az": "Otu zədəm — otu mizənəm — otu bezən — otu bezənid.",
                 "sample_answer_az": "ütülədim — ütüləyirəm — ütülə — ütüləyin"},
                {"fa": "انتخاب کردن", "reading_az": "Entexab kərdən", "az": "seçmək",
                 "sample_answer_fa": "انتخاب کردم — انتخاب می‌کنم — انتخاب کن — انتخاب کنید",
                 "sample_answer_reading_az": "Entexab kərdəm — entexab mikonəm — entexab kon — entexab konid.",
                 "sample_answer_az": "seçdim — seçirəm — seç — seçin"},
                {"fa": "آمدن", "reading_az": "Amədən", "az": "gəlmək",
                 "sample_answer_fa": "آمدم — می‌آیم — بیا — بیایید",
                 "sample_answer_reading_az": "Amədəm — miayəm — bia — biyayid.",
                 "sample_answer_az": "gəldim — gəlirəm — gəl — gəlin (QAYDASIZ: بیا)"},
                {"fa": "بستن", "reading_az": "Bəstən", "az": "bağlamaq",
                 "sample_answer_fa": "بستم — می‌بندم — ببند — ببندید",
                 "sample_answer_reading_az": "Bəstəm — mibəndəm — bebənd — bebəndid.",
                 "sample_answer_az": "bağladım — bağlayıram — bağla — bağlayın (kök: بند)"},
                {"fa": "رفتن", "reading_az": "Rəftən", "az": "getmək",
                 "sample_answer_fa": "رفتم — می‌روم — برو — بروید",
                 "sample_answer_reading_az": "Rəftəm — mirəvəm — boro — bərəvid.",
                 "sample_answer_az": "getdim — gedirəm — get — gedin (QAYDASIZ: برو)"},
                {"fa": "باز کردن", "reading_az": "Baz kərdən", "az": "açmaq",
                 "sample_answer_fa": "باز کردم — باز می‌کنم — باز کن — باز کنید",
                 "sample_answer_reading_az": "Baz kərdəm — baz mikonəm — baz kon — baz konid.",
                 "sample_answer_az": "açdım — açıram — aç — açın"},
                {"fa": "نماز خواندن", "reading_az": "Nəmaz xandən", "az": "namaz qılmaq",
                 "sample_answer_fa": "نماز خواندم — نماز می‌خوانم — نماز بخوان — نماز بخوانید",
                 "sample_answer_reading_az": "Nəmaz xandəm — nəmaz mixanəm — nəmaz bexan — nəmaz bexanid.",
                 "sample_answer_az": "namaz qıldım — namaz qılıram — namaz qıl — namaz qılın"},
                {"fa": "آوردن", "reading_az": "Avərdən", "az": "gətirmək",
                 "sample_answer_fa": "آوردم — می‌آورم — بیاور — بیاورید",
                 "sample_answer_reading_az": "Avərdəm — miavərəm — biyavər — biyavərid.",
                 "sample_answer_az": "gətirdim — gətirirəm — gətir — gətirin (QAYDASIZ: بیاور)"},
                {"fa": "خوردن", "reading_az": "Xordən", "az": "yemək",
                 "sample_answer_fa": "خوردم — می‌خورم — بخور — بخورید",
                 "sample_answer_reading_az": "Xordəm — mixorəm — boxor — boxorid.",
                 "sample_answer_az": "yedim — yeyirəm — ye — yeyin"},
                {"fa": "نوشتن", "reading_az": "Neveştən", "az": "yazmaq",
                 "sample_answer_fa": "نوشتم — می‌نویسم — بنویس — بنویسید",
                 "sample_answer_reading_az": "Neveştəm — minevisəm — benevis — benevisid.",
                 "sample_answer_az": "yazdım — yazıram — yaz — yazın (kök: نویس)"},
            ],
        },
        {
            # Çalışma 5 — səh. 203 «مانند مثال، جمله‌ی امری بگویید».
            # Əvvəllər sadə practice_reveal idi.
            "kind": "answer_question",
            "title_fa": "مانند مثال، جمله‌ی امری بگویید",
            "instruction_az": "Nümunə kimi cümləni əmr cümləsinə çevirin",
            "example_fa": "من فردا به تهران می‌روم.\n← شما (تو) فردا به تهران *برو*.",
            "example_reading_az": "Mən fərda be Tehran mirəvəm.\n← Şoma (to) fərda be Tehran boro.",
            "example_az": (
                "Əmr feli yalnız «تو» və «شما» şəxslərində olur.\n"
                "Addımlar:\n"
                "1) Subyekti «شما (تو)» ilə əvəz et;\n"
                "2) İndiki/keçmiş feli ƏMR felinə çevir (می‌روم → برو);\n"
                "3) KEÇMİŞ ZAMAN zərfini (دیروز، دیشب) və SUAL sözünü (آیا) AT;\n"
                "4) Yiyəlik şəkilçisini uyğunlaşdır: پدر و مادرم → پدر و مادرتان.\n"
                "Tərcümə: Sabah Tehrana get."
            ),
            "items": [
                {"fa": "ما از بازار سبزی می‌خریم و آن‌ها را پاک می‌کنیم.", "reading_az": "Ma əz bazar səbzi mixərim va anha ra pak mikonim.", "az": "Biz bazardan göyərti alırıq və onları təmizləyirik.",
                 "sample_answer_fa": "شما از بازار سبزی بخرید و آن‌ها را پاک کنید.",
                 "sample_answer_reading_az": "Şoma əz bazar səbzi bexərid va anha ra pak konid.",
                 "sample_answer_az": "Siz bazardan göyərti alın və onları təmizləyin."},
                {"fa": "شما دیروز به باغ رفتید و میوه خوردید.", "reading_az": "Şoma diruz be bağ rəftid va mive xordid.", "az": "Siz dünən bağa getdiniz və meyvə yediniz.",
                 "sample_answer_fa": "شما به باغ بروید و میوه بخورید.",
                 "sample_answer_reading_az": "Şoma be bağ bərəvid va mive boxorid.",
                 "sample_answer_az": "Siz bağa gedin və meyvə yeyin. — «دیروز» keçmiş zərfi ATILIR."},
                {"fa": "من دیشب برای پدر و مادرم نامه نوشتم.", "reading_az": "Mən dişəb bəraye pedər va madərəm name neveştəm.", "az": "Mən dünən gecə ata-anama məktub yazdım.",
                 "sample_answer_fa": "شما برای پدر و مادرتان نامه بنویسید.",
                 "sample_answer_reading_az": "Şoma bəraye pedər va madəretan name benevisid.",
                 "sample_answer_az": "Siz ata-ananıza məktub yazın. — «ـم» → «ـتان» dəyişir."},
                {"fa": "آیا شما هر شب درها و پنجره‌ها را می‌بندید؟", "reading_az": "Aya şoma hər şəb dərha va pəncereha ra mibəndid?", "az": "Siz hər gecə qapıları və pəncərələri bağlayırsınız?",
                 "sample_answer_fa": "شما هر شب درها و پنجره‌ها را ببندید.",
                 "sample_answer_reading_az": "Şoma hər şəb dərha va pəncereha ra bebəndid.",
                 "sample_answer_az": "Siz hər gecə qapıları və pəncərələri bağlayın. — «آیا» sual sözü ATILIR."},
            ],
        },
        {
            # Çalışma 6 — səh. 202 «لطفاً توجّه کنید» + «لطفاً بخوانید» əsasında.
            # Vəziyyətə uyğun NƏZAKƏTLİ əmr cümləsi qurmaq.
            "kind": "answer_question",
            "title_fa": "با «لطفاً» و «خواهش می‌کنم» جمله بگویید",
            "instruction_az": "Vəziyyətə uyğun nəzakətli xahiş cümləsi qurun",
            "example_fa": "نوشتن ← لطفاً *بنویس* (*بنویسید*).\nخواندن ← خواهش می‌کنم *بخوان* (*بخوانید*).",
            "example_reading_az": "Neveştən ← lotfən benevis (benevisid).\nXandən ← xaheş mikonəm bexan (bexanid).",
            "example_az": (
                "«لطفاً» = zəhmət olmasa; «خواهش می‌کنم» = xahiş edirəm.\n"
                "Hər ikisi cümlənin ƏVVƏLİNƏ gəlir və feli DƏYİŞMİR — fel yenə əmr formasındadır.\n"
                "Yaxın adama «تو» formasını (بنویس), böyüyə və ya birdən çox adama «شما» formasını (بنویسید) deyirik.\n"
                "Bu iki söz cümləni əmrdən XAHİŞƏ çevirir."
            ),
            "items": [
                {"fa": "هوا سرد است؛ می‌خواهید حسین پنجره‌ها را ببندد.", "reading_az": "Həva sərd əst; mixahid Hoseyn pəncereha ra bebəndəd.", "az": "Hava soyuqdur; Hüseynin pəncərələri bağlamasını istəyirsiniz.",
                 "sample_answer_fa": "حسین! هوا سرد است؛ لطفاً پنجره‌ها را ببند.",
                 "sample_answer_reading_az": "Hoseyn! Həva sərd əst; lotfən pəncereha ra bebənd.",
                 "sample_answer_az": "Hüseyn! Hava soyuqdur; zəhmət olmasa pəncərələri bağla."},
                {"fa": "می‌خواهید دانش‌آموزان کتاب را باز کنند و درس پانزدهم را بخوانند.", "reading_az": "Mixahid daneşamuzan ketab ra baz konənd va dərse panzdəhom ra bexanənd.", "az": "Şagirdlərin kitabı açıb on beşinci dərsi oxumasını istəyirsiniz.",
                 "sample_answer_fa": "لطفاً کتاب را باز کنید و درس پانزدهم را بخوانید.",
                 "sample_answer_reading_az": "Lotfən ketab ra baz konid va dərse panzdəhom ra bexanid.",
                 "sample_answer_az": "Zəhmət olmasa kitabı açın və on beşinci dərsi oxuyun."},
                {"fa": "می‌خواهید مهمان پس از بیرون رفتن از اتاق، در را ببندد.", "reading_az": "Mixahid mehman pəs əz birun rəftən əz otaq, dər ra bebəndəd.", "az": "Qonağın otaqdan çıxdıqdan sonra qapını bağlamasını istəyirsiniz.",
                 "sample_answer_fa": "لطفاً پس از بیرون رفتن از اتاق، در را ببندید.",
                 "sample_answer_reading_az": "Lotfən pəs əz birun rəftən əz otaq, dər ra bebəndid.",
                 "sample_answer_az": "Zəhmət olmasa otaqdan çıxdıqdan sonra qapını bağlayın."},
                {"fa": "می‌خواهید فرزندتان درس‌هایش را خوب بخواند و تکلیف‌هایش را بنویسد.", "reading_az": "Mixahid fərzəndetan dərshayəş ra xub bexanəd va təklifhayəş ra benevisəd.", "az": "Övladınızın dərslərini yaxşı oxumasını və tapşırıqlarını yazmasını istəyirsiniz.",
                 "sample_answer_fa": "خواهش می‌کنم درس‌هایت را خوب بخوان و تکلیف‌هایت را بنویس.",
                 "sample_answer_reading_az": "Xaheş mikonəm dərshayət ra xub bexan va təklifhayət ra benevis.",
                 "sample_answer_az": "Xahiş edirəm dərslərini yaxşı oxu və tapşırıqlarını yaz. — yaxın adama «تو» forması."},
                {"fa": "می‌خواهید دانش‌آموزان تکلیف‌هایشان را با خط زیبا بنویسند.", "reading_az": "Mixahid daneşamuzan təklifhayeşan ra ba xətte ziba benevisənd.", "az": "Şagirdlərin tapşırıqlarını gözəl xətlə yazmasını istəyirsiniz.",
                 "sample_answer_fa": "خواهش می‌کنم تکلیف‌هایتان را با خط زیبا بنویسید.",
                 "sample_answer_reading_az": "Xaheş mikonəm təklifhayetan ra ba xətte ziba benevisid.",
                 "sample_answer_az": "Xahiş edirəm tapşırıqlarınızı gözəl xətlə yazın."},
                {"fa": "می‌خواهید برادرتان درِ کمپوت را باز کند.", "reading_az": "Mixahid bəradəretan dəre kompot ra baz konəd.", "az": "Qardaşınızın kompotun qapağını açmasını istəyirsiniz.",
                 "sample_answer_fa": "لطفاً درِ کمپوت را باز کن.",
                 "sample_answer_reading_az": "Lotfən dəre kompot ra baz kon.",
                 "sample_answer_az": "Zəhmət olmasa kompotun qapağını aç."},
            ],
        },
        {
            # Çalışma 7 — səh. 206 «مانند مثال بگویید» («در حالِ ... بودم که ...»).
            "kind": "practice_reveal",
            "title_fa": "مانند مثال بگویید — «در حالِ … بودم که …»",
            "instruction_az": "Nümunə kimi cümlə qurun: «استراحت‌کردن / مادرم / صدا زدن → در حال استراحت کردن بودم که مادرم مرا صدا زد.»",
            "example_prompt_fa": "استراحت‌کردن / مادرم / صدا زدن",
            "example_answer_fa": "در حال استراحت کردن بودم که مادرم مرا صدا زد.",
            "items": [
                {"prompt_fa": "درس خواندن / دوستم / آمدن", "answer_fa": "در حال درس خواندن بودم که دوستم آمد.", "reading_az": "Dər hale dərsxandən budəm ke dustəm aməd.", "az": "Dərs oxumaqda idim ki, dostum gəldi."},
                {"prompt_fa": "دیدن فیلم / تلویزیون / خراب شدن", "answer_fa": "در حال دیدن فیلم بودیم که تلویزیون خراب شد.", "reading_az": "Dər hale didəne film budim ke televizion xərab şod.", "az": "Film baxmaqda idik ki, televizor xarab oldu."},
                {"prompt_fa": "غرق‌شدن / پدرم / نجات دادن", "answer_fa": "در حال غرق‌شدن بودم که پدرم مرا نجات داد.", "reading_az": "Dər hale qərqşodən budəm ke pedərəm mə ra necat dad.", "az": "Batmaqda idim ki, atam məni xilas etdi."},
                {"prompt_fa": "پاک‌کردن سبزی / مهمان‌ها / آمدن", "answer_fa": "در حال پاک‌کردن سبزی بودیم که مهمان‌ها آمدند.", "reading_az": "Dər hale pakkərdəne səbzi budim ke mehmanha amədənd.", "az": "Göyərti təmizləməkdə idik ki, qonaqlar gəldi."},
            ],
        },
        {
            # Çalışma 8 — səh. 206 «لطفاً جایگزین کنید».
            "kind": "practice_reveal",
            "title_fa": "لطفاً جایگزین کنید",
            "instruction_az": "Verilən sözlərlə nümunədəki cümləni yenidən qurun (SUBYEKT / ƏŞYA / 1-ci MƏSDƏR / 2-ci MƏSDƏR)",
            "example_prompt_fa": "من / میوه / پوست کندن / خوردن",
            "example_answer_fa": "من میوه‌ها را پوست می‌کنم و می‌خورم.",
            "example_fa": "من / میوه / پوست کندن / خوردن → من میوه‌ها را پوست *می‌کنم* و *می‌خورم*.",
            "items": [
                {"prompt_fa": "ما / سبزی / پاک کردن / شستن", "answer_fa": "ما سبزی را پاک می‌کنیم و می‌شوییم.", "reading_az": "Ma səbzi ra pak mikonim va mişuyim.", "az": "Biz göyərtini təmizləyirik və yuyuruq."},
                {"prompt_fa": "پدر بزرگم / میوه / چیدن / فروختن", "answer_fa": "پدر بزرگم میوه را می‌چیند و می‌فروشد.", "reading_az": "Pedərbozorgəm mive ra miçinəd va mifəruşəd.", "az": "Babam meyvəni dərir və satır."},
                {"prompt_fa": "باغبان / درخت / کاشتن / آب دادن", "answer_fa": "باغبان درخت را می‌کارد و آب می‌دهد.", "reading_az": "Bağban dərəxt ra mikarəd va ab midəhəd.", "az": "Bağban ağacı əkir və suvarır."},
                {"prompt_fa": "مادرم / کدو / خرد کردن / پختن", "answer_fa": "مادرم کدو را خرد می‌کند و می‌پزد.", "reading_az": "Madərəm kədu ra xord mikonəd va mipəzəd.", "az": "Anam balqabağı xırdalayır və bişirir."},
            ],
        },
        {
            # Çalışma 9 — səh. 206 «مانند مثال با فعل امر جمله بسازید».
            # Dərslikdə hər məsdərin yanında şəkil var; cavab İKİ cürdür (tək və cəm əmr).
            "kind": "picture_sentences",
            "title_fa": "مانند مثال با فعل امر جمله بسازید",
            "instruction_az": "Nümunə kimi əmr feli ilə cümlə qurun (tək «تو» və cəm «شما» formasında)",
            "example_fa": "گذاشتن (میوه / سبد)",
            "example_reading_az": "Gozaştən (mive / səbəd)",
            "example_az": "qoymaq (meyvə / səbət) — hər şəkil üçün İKİ cümlə deyilir: tək əmr və cəm (nəzakətli) əmr.",
            "example_answer_fa": "میوه را در سبد بگذار. / میوه را در سبد بگذارید.",
            "example_answer_reading_az": "Mive ra dər səbəd begozar. / Mive ra dər səbəd begozarid.",
            "example_answer_az": "Meyvəni səbətə qoy. / Meyvəni səbətə qoyun.",
            "items": [
                {
                    "image": "",
                    "sentences": [
                        {"fa": "خوردن (توت‌فرنگی)", "reading_az": "Xordən (tute-fərəngi)", "az": "yemək (çiyələk)"},
                        {"fa": "توت‌فرنگی را بخور.", "reading_az": "Tute-fərəngi ra boxor.", "az": "Çiyələyi ye."},
                        {"fa": "توت‌فرنگی را بخورید.", "reading_az": "Tute-fərəngi ra boxorid.", "az": "Çiyələyi yeyin. — nəzakətli (cəm) forma."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "شستن (سیب)", "reading_az": "Şostən (sib)", "az": "yumaq (alma)"},
                        {"fa": "سیب را بشوی.", "reading_az": "Sib ra bəşuy.", "az": "Almanı yu. — danışıqda «بشور» deyilir."},
                        {"fa": "سیب را بشویید.", "reading_az": "Sib ra bəşuyid.", "az": "Almanı yuyun."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "خریدن (خودکار)", "reading_az": "Xəridən (xodkar)", "az": "almaq (qələm)"},
                        {"fa": "خودکار را بخر.", "reading_az": "Xodkar ra bexər.", "az": "Qələmi al."},
                        {"fa": "خودکار را بخرید.", "reading_az": "Xodkar ra bexərid.", "az": "Qələmi alın."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "بستن (پنجره)", "reading_az": "Bəstən (pəncere)", "az": "bağlamaq (pəncərə)"},
                        {"fa": "پنجره را ببند.", "reading_az": "Pəncere ra bebənd.", "az": "Pəncərəni bağla."},
                        {"fa": "پنجره را ببندید.", "reading_az": "Pəncere ra bebəndid.", "az": "Pəncərəni bağlayın."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "ریختن (آب / لیوان)", "reading_az": "Rixtən (ab / livan)", "az": "tökmək (su / stəkan)"},
                        {"fa": "آب را در لیوان بریز.", "reading_az": "Ab ra dər livan beriz.", "az": "Suyu stəkana tök."},
                        {"fa": "آب را در لیوان بریزید.", "reading_az": "Ab ra dər livan berizid.", "az": "Suyu stəkana tökün."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "سرخ کردن (سیب‌زمینی)", "reading_az": "Sorx kərdən (sibzəmini)", "az": "qızartmaq (kartof)"},
                        {"fa": "سیب‌زمینی را سرخ بکن.", "reading_az": "Sibzəmini ra sorx bekon.", "az": "Kartofu qızart."},
                        {"fa": "سیب‌زمینی را سرخ بکنید.", "reading_az": "Sibzəmini ra sorx bekonid.", "az": "Kartofu qızardın."},
                    ],
                },
            ],
        },
        {
            # Çalışma 10 — səh. 205 alt qeyd: mətndəki qaydasız/mürəkkəb fellərin əmr forması.
            "kind": "practice_reveal",
            "title_fa": "فعل امر بگویید",
            "instruction_az": "Məsdərin əmr formasını deyin (tək / cəm): «گذاشتن → بگذار؛ بگذارید»",
            "example_prompt_fa": "گذاشتن",
            "example_answer_fa": "بگذار؛ بگذارید",
            "items": [
                {"prompt_fa": "شستن", "answer_fa": "بشوی؛ بشویید", "reading_az": "Bəşuy; bəşuyid.", "az": "yu; yuyun — danışıq dilində «بشور» deyilir."},
                {"prompt_fa": "پوست کندن", "answer_fa": "پوست بکن؛ پوست بکنید", "reading_az": "Pust bekon; pust bekonid.", "az": "soy; soyun"},
                {"prompt_fa": "سرخ کردن", "answer_fa": "سرخ بکن؛ سرخ بکنید", "reading_az": "Sorx bekon; sorx bekonid.", "az": "qızart; qızardın"},
                {"prompt_fa": "ریختن", "answer_fa": "بریز؛ بریزید", "reading_az": "Beriz; berizid.", "az": "tök; tökün"},
                {"prompt_fa": "بردن", "answer_fa": "ببر؛ ببرید", "reading_az": "Bebər; bebərid.", "az": "apar; aparın"},
                {"prompt_fa": "آوردن", "answer_fa": "بیاور؛ بیاورید", "reading_az": "Biyavər; biyavərid.", "az": "gətir; gətirin"},
                {"prompt_fa": "دیدن", "answer_fa": "ببین؛ ببینید", "reading_az": "Bebin; bebinid.", "az": "bax (gör); baxın"},
                {"prompt_fa": "پذیرایی کردن", "answer_fa": "پذیرایی کن؛ پذیرایی کنید", "reading_az": "Pəzirayi kon; pəzirayi konid.", "az": "ikram et; ikram edin"},
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
        # səh. 205 «لطفاً پاسخ دهید» — mətnə aid 7 sual.
        "answer_items": [
            {"fa": "مجید و خانواده‌اش ساعت چند به طرف روستا حرکت کردند؟", "reading_az": "Mocid va xanevadeəş saəte çənd be tərəfe rusta hərəkət kərdənd?", "az": "Məcid və ailəsi saat neçədə kəndə tərəf yola düşdülər?"},
            {"fa": "آن‌ها ساعت چند به خانه‌ی پدربزرگ رسیدند؟", "reading_az": "Anha saəte çənd be xaneye pedərbozorg residənd?", "az": "Onlar babasının evinə saat neçədə çatdılar?"},
            {"fa": "مجید برای چه کاری به باغ پدربزرگش رفت؟", "reading_az": "Mocid bəraye çe kari be bağe pedərbozorgəş rəft?", "az": "Məcid nə üçün babasının bağına getdi?"},
            {"fa": "مجید درحال چه کاری بود که پدربزرگ او را صدا زد؟", "reading_az": "Mocid dərhale çe kari bud ke pedərbozorg u ra seda zəd?", "az": "Babası onu səslədiyi zaman Məcid nə etməkdə idi?"},
            {"fa": "پدربزرگ، وقتی مجید را صدا زد، چه گفت؟", "reading_az": "Pedərbozorg, vəqti Mocid ra seda zəd, çe goft?", "az": "Baba Məcidi səslədiyi zaman nə dedi?"},
            {"fa": "مجید برای چه کاری به مغازه رفت؟", "reading_az": "Mocid bəraye çe kari be məğaze rəft?", "az": "Məcid nə üçün mağazaya getdi?"},
            {"fa": "مادربزرگ به مادر مجید چه گفت؟", "reading_az": "Madərbozorg be madəre Mocid çe goft?", "az": "Nənə Məcidin anasına nə dedi?"},
        ],
    },
    "reading_text": {
        "title_fa": "کمک به پدربزرگ",
        "title_az": "Babaya kömək",
        "paragraphs_fa": [
            "فصل تابستان بود. حدود ساعت هشت با پدر و مادرم به طرف روستای پدربزرگم حرکت کردیم و ساعت ده و نیم صبح به خانه‌ی پدربزرگ رسیدیم. هوای روستا بسیار خنک و لذّت‌بخش بود.",
            "بعدازظهر برای تفریح و کمک به پدربزرگم به باغ رفتم. حدود ساعت پنج، هوا بارانی شد. در حال تماشای باران بودم که پدربزرگم صدا زد: مجید! جعبه‌ها را بیاور و میوه‌ها را در آن بگذار. زود به طرف جعبه‌ها رفتم و تعدادی جعبه آوردم. با کمک پدربزرگ سیب‌ها و زردآلوها را در جعبه‌ها ریختیم و مقداری از آن‌ها را برداشتیم و به خانه برگشتیم.",
            "در بین راه، پدربزرگ مقداری پول به من داد و گفت: مجید! امشب مهمان داریم؛ دو نفر از دوستان به همراه خانواده‌شان به منزل ما می‌آیند. برو، دو کیلو سیب‌زمینی، یک کیلو تخم‌مرغ و دو تا کاهو بخر و زود بیا. گفتم: چَشم؛ سپس به مغازه رفتم و آن چیزها را خریدم.",
            "هنگام برگشتن به خانه، پدرم را دیدم. ایشان سیب‌زمینی‌ها را از من گرفت و با هم به خانه برگشتیم.",
            "چیزهایی را که خریدم به آشپزخانه بردم و روی میز گذاشتم. مادربزرگم که در حال پختن غذا بود، از من تشکّر کرد و به مادرم گفت: لطفاً سیب‌زمینی‌ها را بشوی. آن‌ها را پوست بکن و در ماهی‌تابه بریز و سرخ کن.",
            "آن شب مادربزرگ با کمک مادرم غذای خوش‌مزه‌ای پختند و از مهمان‌ها پذیرایی کردند.",
        ],
        "footnotes": [
            {"fa": "تعدادی / مقداری", "az": "bir neçə / bir miqdar"},
            {"fa": "درحالِ", "az": "…etməkdə olarkən"},
            {"fa": "به همراهِ", "az": "…ilə birlikdə"},
            {"fa": "چَشم", "az": "baş üstə (razılıq bildirir)"},
            {"fa": "…… را صدا زد.", "az": "…-i səslədi (səh. 204 alt qeyd)"},
            {"fa": "در گفت‌وگو فعل امر «بشوی» را «بشور» می‌گوییم.", "az": "Danışıq dilində «بشوی» əvəzinə «بشور» deyilir (səh. 205 alt qeyd)."},
            {"fa": "گذاشتن: فعل امر ← بگذار؛ بگذارید", "az": "qoymaq → qoy; qoyun"},
            {"fa": "شستن: فعل امر ← بشوی؛ بشویید", "az": "yumaq → yu; yuyun"},
            {"fa": "پوست کندن: فعل امر ← پوست بکن؛ پوست بکنید", "az": "soymaq → soy; soyun"},
            {"fa": "سرخ کردن: فعل امر ← سرخ بکن؛ سرخ بکنید", "az": "qızartmaq → qızart; qızardın"},
            {"fa": "مرا: من را", "az": "«مرا» = «من را» (məni) — səh. 206 alt qeyd"},
        ],
        "full_translation_az": (
            "Yay fəsli idi. Saat təxminən səkkizdə ata-anamla babamın kəndinə tərəf yola düşdük və səhər saat "
            "on yarımda babamın evinə çatdıq. Kəndin havası çox sərin və ləzzətli idi.\n\n"
            "Günortadan sonra əyləncə üçün və babama kömək etmək üçün bağa getdim. Saat təxminən beşdə hava "
            "yağışlı oldu. Yağışa tamaşa etməkdə idim ki, babam məni səslədi: Məcid! Qutuları gətir və meyvələri "
            "onların içinə qoy. Tez qutulara tərəf getdim və bir neçə qutu gətirdim. Babamın köməyi ilə almaları "
            "və ərikləri qutulara tökdük və onların bir qismini götürüb evə qayıtdıq.\n\n"
            "Yolda babam mənə bir qədər pul verdi və dedi: Məcid! Bu gecə iki nəfər qonağımız var; dostlardan "
            "ikisi ailələri ilə birlikdə bizə gəlir. Get, iki kilo kartof, bir kilo yumurta və iki dənə kahı al "
            "və tez gəl. Dedim: Baş üstə! Sonra mağazaya getdim və o şeyləri aldım.\n\n"
            "Evə qayıdarkən atamı gördüm. O, kartofları məndən aldı və birlikdə evə qayıtdıq.\n\n"
            "Aldığım şeyləri "
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
                "fa": "در حال تماشای باران بودم که پدربزرگم صدا زد: مجید! جعبه‌ها را بیاور و میوه‌ها را در آن بگذار.",
                "reading_az": "Dər hale təmaşaye baran budəm ke pedərbozorgəm seda zəd: Mocid! Coebeha ra biyavər va miveha ra dər an begozar.",
                "az": "Yağışa tamaşa etməkdə idim ki, babam səslədi: Məcid! Qutuları gətir və meyvələri onun içinə qoy.",
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
                "fa": "در بین راه، پدربزرگ مقداری پول به من داد و گفت: مجید! امشب مهمان داریم؛ دو نفر از دوستان به همراه خانواده‌شان به منزل ما می‌آیند.",
                "reading_az": "Dər beyne rah, pedərbozorg meqdari pul be mən dad va goft: Mocid! Əmşəb mehman darim; do nəfər əz dustan be həmrahe xanevadeşan be mənzele ma miayənd.",
                "az": "Yolda babam mənə bir qədər pul verdi və dedi: Məcid! Bu gecə qonağımız var; dostlardan iki nəfəri ailələri ilə birlikdə bizə gəlir.",
                "new_paragraph": True,
            },
            {
                "fa": "برو، دو کیلو سیب‌زمینی، یک کیلو تخم‌مرغ و دو تا کاهو بخر و زود بیا.",
                "reading_az": "Boro, do kilo sibzəmini, yek kilo toxme-morğ va do ta kahu bexər va zud bia.",
                "az": "Get, iki kilo kartof, bir kilo yumurta və iki dənə kahı al və tez gəl.",
            },
            {
                "fa": "گفتم: چَشم؛ سپس به مغازه رفتم و آن چیزها را خریدم.",
                "reading_az": "Goftəm: çəşm; səpəs be məğaze rəftəm va an çizha ra xəridəm.",
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
                "fa": "چیزهایی را که خریدم به آشپزخانه بردم و روی میز گذاشتم.",
                "reading_az": "Çizhayi ra ke xəridəm be aşpəzxane bordəm va ruye miz gozaştəm.",
                "az": "Aldığım şeyləri mətbəxə apardım və masanın üstünə qoydum.",
                "new_paragraph": True,
            },
            {
                "fa": "مادربزرگم که در حال پختن غذا بود، از من تشکّر کرد و به مادرم گفت: لطفاً سیب‌زمینی‌ها را بشوی.",
                "reading_az": "Madərbozorgəm ke dər hale poxtəne qəza bud, əz mən təşəkkor kərd va be madərəm goft: lotfən sibzəminiha ra bəşuy.",
                "az": "Yemək bişirməkdə olan nənəm mənə təşəkkür etdi və anama dedi: Zəhmət olmasa kartofları yu.",
            },
            {
                "fa": "آن‌ها را پوست بکن و در ماهی‌تابه بریز و سرخ کن.",
                "reading_az": "Anha ra pust bekon va dər mahitabe beriz va sorx kon.",
                "az": "Onları soy və tavaya töküb qızart.",
            },
            {
                "fa": "آن شب مادربزرگ با کمک مادرم غذای خوش‌مزه‌ای پختند و از مهمان‌ها پذیرایی کردند.",
                "reading_az": "An şəb madərbozorg ba komək madərəm qəzaye xoşməzei poxtənd va əz mehmanha pəzirayi kərdənd.",
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
                "sample_answer_fa": "پدربزرگ گفت: مجید! جعبه‌ها را بیاور و میوه‌ها را در آن بگذار.",
                "sample_answer_reading_az": "Pedərbozorg goft: Mocid! Coebeha ra biyavər va miveha ra dər an begozar.",
                "sample_answer_az": "Babası dedi: Məcid! Qutuları gətir və meyvələri onun içinə qoy.",
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
                "sample_answer_reading_az": "Madərbozorg goft: lotfən sibzəminiha ra bəşuy. Anha ra pust bekon va dər mahitabe beriz va sorx kon.",
                "sample_answer_az": "Nənəsi dedi: Zəhmət olmasa kartofları yu. Onları soy və tavaya töküb qızart.",
            },
        ],
    },
}
