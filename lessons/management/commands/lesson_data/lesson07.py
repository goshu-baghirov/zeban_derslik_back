# Dərs 7 — پوشاک (لباس) (Geyim)
# Mənbə: کتاب دوم, səh. 87-98

LESSON = {
    "number": 7,
    "title_fa": "پوشاک (لباس)",
    "title_az": "Geyim",
    "available": True,
    "vocabulary": [
        {"fa": "پوشاک مردانه", "reading": "puşake mərdane", "az": "Kişi geyimi"},
        {"fa": "پوشاک زنانه", "reading": "puşake zənane", "az": "Qadın geyimi"},
        {"fa": "پوشاک بچّگانه", "reading": "puşake bəççeqane", "az": "Uşaq geyimi"},
        {"fa": "چادر", "reading": "çador", "az": "Çadra"},
        {"fa": "روسری", "reading": "rusəri", "az": "Baş örtüyü (yaylıq)"},
        {"fa": "مقنعه", "reading": "məqnəe", "az": "Hicab (məqnəə)"},
        {"fa": "مانتو", "reading": "manto", "az": "Manto"},
        {"fa": "پالتو", "reading": "palto", "az": "Palto"},
        {"fa": "کاپشن", "reading": "kapşen", "az": "Gödəkcə (kurtka)"},
        {"fa": "بلوز", "reading": "boluz", "az": "Bluz (sviter)"},
        {"fa": "زیرپوش", "reading": "zirpuş", "az": "Alt köynəyi (mayka)"},
        {"fa": "شورت", "reading": "şort", "az": "Alt paltarı (şort)"},
        {"fa": "چکمه", "reading": "çəkme", "az": "Çəkmə"},
        {"fa": "دمپایی", "reading": "dəmpayi", "az": "Şəpşəp (ev ayaqqabısı)"},
        {"fa": "کفش", "reading": "kəfş", "az": "Ayaqqabı"},
        {"fa": "کمربند", "reading": "kəmərbənd", "az": "Kəmər"},
        {"fa": "دست‌کش", "reading": "dəstkeş", "az": "Əlcək"},
        {"fa": "ضخیم", "reading": "zəxim", "az": "Qalın"},
        {"fa": "نازک", "reading": "nazok", "az": "Nazik"},
        {"fa": "شال", "reading": "şal", "az": "Şal"},
        {"fa": "آستین", "reading": "astin", "az": "Qol (paltarın qolu)"},
        {"fa": "یقه", "reading": "yəqe", "az": "Yaxa"},
        {"fa": "دکمه", "reading": "dokme", "az": "Düymə"},
        {"fa": "زیپ", "reading": "zip", "az": "Zəncirbənd"},
        {"fa": "انتخاب می‌کند", "reading": "entexab mikonəd", "az": "seçir"},
        {"fa": "اتو می‌زند", "reading": "otu mizənəd", "az": "ütüləyir"},
        {"fa": "می‌پوشد", "reading": "mipuşəd", "az": "geyinir"},
        {"fa": "درمی‌آورد", "reading": "dərmiavərəd", "az": "çıxarır (əynindən)"},
        {"fa": "شلوغ", "reading": "şoluğ", "az": "İzdihamlı, qələbəlik"},
        {"fa": "خلوت", "reading": "xəlvət", "az": "Sakit, boş"},
        {"fa": "هنگام", "reading": "hengam", "az": "…zamanı, vaxtı"},
        {"fa": "نو", "reading": "nou", "az": "Təzə"},
        {"fa": "قدیمی", "reading": "qədimi", "az": "Köhnə, qədim"},
        {"fa": "چوب‌لباسی", "reading": "çublebasi", "az": "Paltarasan"},
        {"fa": "آویزان می‌کند", "reading": "avizan mikonəd", "az": "asır"},
    ],
    "grammar_notes": [
        {
            "title_az": "Cəm şəkilçiləri «ها» və «ان»",
            "title_fa": "نشانه‌های جمع «ها» و «ان»",
            # Hər sətir tətbiqdə ayrıca bənd (•) kimi görünür; izah dərslikdəki
            # diaqramın (پسر / شتر / درخت / لباس) məntiqini addım-addım açır.
            "explanation_az": (
                "Fars dilində cəm iki şəkilçi ilə düzəlir: «ها» və «ان». Türk dilindəki «-lar/-lər»in qarşılığıdır.\n"
                "Diaqramın oxunuşu: SÖZ + ها → bir cəm forması, SÖZ + ان → ikinci cəm forması; hər iki forma eyni mənanı verir.\n"
                "«ها» UNİVERSALDIR — istənilən ismə qoşula bilər: canlı da (پسرها، شترها), cansız da (لباس‌ها، کتاب‌ها).\n"
                "«ان» isə YALNIZ CANLILARA qoşulur: پسران، شتران، دختران، کودکان.\n"
                "Diqqət: fars dilində AĞAC və bitkilər də canlı sayılır — ona görə درختان düzgündür.\n"
                "Cansız sözlərdə «ان» İŞLƏNMİR: لباس‌ها ✓ — لباسان ✗ (dərslikdə bu forma qırmızı ilə pozulub).\n"
                "Yazılış fərqi: «ها» sözdən yarımboşluqla ayrıla bilər (درخت‌ها، لباس‌ها), «ان» isə həmişə bitişik yazılır (درختان).\n"
                "Üslub fərqi: «ان» kitab və rəsmi dildə çox işlənir; gündəlik danışıqda «ها» üstünlük təşkil edir.\n"
                "Yəni پسرها və پسران eyni mənadadır — biri danışıq, digəri kitab üslubudur."
            ),
            # Dərslikdəki dörd sətirlik lövhə: SÖZ + (ها / ان) → alınan cəm formaları.
            # Sonuncu sətir qəsdən «xəttli» nümunədir: cansız sözdə «ان» olmur.
            "conjugations": [
                {
                    "pronoun_fa": "پسر + ها / ان",
                    "form_fa": "پسرها = پسران",
                    "reading_az": "pesərha = pesəran",
                    "az": "oğlanlar — canlı, ona görə hər iki şəkilçi olar",
                },
                {
                    "pronoun_fa": "شتر + ها / ان",
                    "form_fa": "شترها = شتران",
                    "reading_az": "şotorha = şotoran",
                    "az": "dəvələr — heyvanlar da canlı sayılır",
                },
                {
                    "pronoun_fa": "درخت + ها / ان",
                    "form_fa": "درخت‌ها = درختان",
                    "reading_az": "dəraxtha = dərəxtan",
                    "az": "ağaclar — farscada bitkilər canlı sayılır",
                },
                {
                    "pronoun_fa": "لباس + ها / ان ✗",
                    "form_fa": "لباس‌ها ✓ — لباسان ✗",
                    "reading_az": "lebasha ✓ — lebasan ✗",
                    "az": "paltarlar — cansız olduğu üçün yalnız «ها» olur",
                },
            ],
            # Dərslikdəki «لطفاً بخوانید» cümlələri (səhifənin alt qeydləri
            # nümunə deyil, aşağıdakı «Qeyd» kartına köçürülüb).
            "examples": [
                {"fa": "آن‌آقا هر روز پلّه‌های مدرسه را تمیز و جارو می‌کند.", "reading_az": "An ağa hər ruz pellehaye mædrese ra təmiz va caru mikonəd.", "az": "O kişi hər gün məktəbin pillələrini təmizləyir və süpürür."},
                {"fa": "چادر، روسری، مقنعه و مانتو لباس‌های زنانه هستند.", "reading_az": "Çador, rusəri, məqnəe va manto lebashaye zənane həstənd.", "az": "Çadra, yaylıq, məqnəə və manto qadın geyimləridir."},
                {"fa": "صادق به بازار می‌رود و برای فرزندانش لباس‌های زیبا انتخاب می‌کند و می‌خرد.", "reading_az": "Sadeq be bazar mirəvəd va bəraye fərzəndanəş lebashaye ziba entexab mikonəd va mixərəd.", "az": "Sadiq bazara gedir və övladları üçün gözəl paltarlar seçib alır."},
                {"fa": "آن‌ها دانش‌آموزان این مدرسه هستند. آن دانش‌آموزها در کلاس اوّل درس می‌خوانند.", "reading_az": "Anha daneşamuzane in mædrese həstənd. An daneşamuzha dər kelase əvvəl dərs mixanənd.", "az": "Onlar bu məktəbin şagirdləridir. O şagirdlər birinci sinifdə oxuyurlar."},
                {"fa": "رستورانِ سعید در خیابان فلسطین است. دوستان من در آن رستوران کار می‌کنند.", "reading_az": "Restorane Səid dər xiyabane Fələstin əst. Dustane mən dər an restoran kar mikonənd.", "az": "Səidin restoranı Fələstin küçəsindədir. Mənim dostlarım o restoranda işləyirlər."},
                {"fa": "آن خانم‌ها پزشک هستند. آن پزشکان در بیمارستان امام خمینی تهران کار می‌کنند.", "reading_az": "An xanomha pezeşk həstənd. An pezeşkan dər bimarestane Emam Xomeyniye Tehran kar mikonənd.", "az": "O xanımlar həkimdir. O həkimlər Tehranın İmam Xomeyni xəstəxanasında işləyirlər."},
                {"fa": "در جنگل، درختان و حیوان‌های زیادی وجود دارد.", "reading_az": "Dər cəngəl, dərəxtan va heyvanhaye ziyadi vocud darəd.", "az": "Meşədə çoxlu ağac və heyvan var."},
                {"fa": "فرزندان شما پسرند یا دختر؟ من یک فرزند پسر به نام علی و دو فرزند دختر به نام‌های فاطمه و زینب دارم.", "reading_az": "Fərzəndane şoma pesərand ya doxtər? Mən yek fərzəde pesər be name Əli va do fərzəde doxtər be namhaye Fateme va Zeynəb daram.", "az": "Sizin övladlarınız oğlandır, yoxsa qız? Mənim Əli adında bir oğlum, Fatimə və Zeynəb adında iki qızım var."},
            ],
            # Səhifənin altındakı iki nömrəli qeyd (dərslikdəki mətnin özü).
            "note_fa": (
                "۱. «ها» و «ان» علامت‌های جمع در فارسی هستند.\n"
                "«ها» برای جمع همه‌ی اسم‌ها استفاده می‌شود، مانند: استادها، دفترها، اسب‌ها و ...\n"
                "۲. «ان» معمولاً برای جمع‌بستن اسم جان‌داران استفاده می‌شود، مانند: زنان، مردان، "
                "دختران، پسران، کودکان، اسبان، شتران، مرغان، شیران، درختان و ..."
            ),
            "note_reading_az": (
                "1. «Ha» va «an» əlaməthaye cəm' dər farsi həstənd.\n"
                "«Ha» bəraye cəm'e həme-ye esmha estefade mişəvəd, manənde: ostadha, dəftərha, əsbha va ...\n"
                "2. «An» mə'mulən bəraye cəm'-bəstəne esme candaran estefade mişəvəd, manənde: zənan, mərdan, "
                "doxtəran, pesəran, kudəkan, əsban, şotoran, morğan, şiran, dərəxtan va ..."
            ),
            "note_az": (
                "1. «ها» və «ان» fars dilində cəm əlamətləridir.\n"
                "«ها» BÜTÜN isimlərin cəmində işlənir: استادها (müəllimlər), دفترها (dəftərlər), اسب‌ها (atlar) və s.\n"
                "2. «ان» adətən CANLI varlıqların cəmində işlənir: زنان (qadınlar), مردان (kişilər), "
                "دختران (qızlar), پسران (oğlanlar), کودکان (uşaqlar), اسبان (atlar), شتران (dəvələr), "
                "مرغان (quşlar), شیران (aslanlar), درختان (ağaclar) və s.\n"
                "Göründüyü kimi اسب sözünün hər iki cəmi var — اسب‌ها və اسبان — çünki at canlıdır."
            ),
            "note2_fa": (
                "می‌گوییم: لباس‌ها ✓ / نمی‌گوییم: لباسان ✗\n"
                "اسم‌های بی‌جان فقط با «ها» جمع بسته می‌شوند: کتاب‌ها، میزها، پیراهن‌ها، کفش‌ها.\n"
                "توجّه: در برخی واژه‌ها «ان» جزء کلمه است و نشانه‌ی جمع نیست، مانند: "
                "رستوران، بیمارستان، خیابان، تهران، دندان، زبان، نگهبان، لیوان، حیوان، عریان و ...\n"
                "این واژه‌ها هم با «ها» جمع بسته می‌شوند: خیابان‌ها، دندان‌ها، لیوان‌ها."
            ),
            "note2_reading_az": (
                "Miguyim: lebasha / Nemiguyim: lebasan\n"
                "Esmhaye bican fəqət ba «ha» cəm' bəste mişəvənd: ketabha, mizha, pirahənha, kəfşha.\n"
                "Təvəccoh: dər bərxi vajeha «an» cozve kəlame əst va neşane-ye cəm' nist, manənde: "
                "restoran, bimarestan, xiyaban, Tehran, dəndan, zəban, negəhban, livan, heyvan, əryan va ...\n"
                "İn vajeha həm ba «ha» cəm' bəste mişəvənd: xiyabanha, dəndanha, livanha."
            ),
            "note2_az": (
                "Deyirik: لباس‌ها ✓ — Demirik: لباسان ✗\n"
                "Cansız isimlər yalnız «ها» ilə cəmlənir: کتاب‌ها (kitablar), میزها (masalar), "
                "پیراهن‌ها (köynəklər), کفش‌ها (ayaqqabılar).\n"
                "Dərslikdə də məhz bu səbəbdən «لباسان» formasının üstündən qırmızı xətt çəkilib.\n"
                "DİQQƏT (dərslikdəki ayrıca qeyd): bəzi sözlərin sonundakı «ان» cəm əlaməti DEYİL, "
                "sözün öz hissəsidir — رستوران (restoran), بیمارستان (xəstəxana), خیابان (küçə), "
                "تهران (Tehran), دندان (diş), زبان (dil), نگهبان (gözətçi), لیوان (stəkan), "
                "حیوان (heyvan), عریان (çılpaq).\n"
                "Bu sözlər onsuz da cəm deyil — cəmlənəndə «ها» alırlar: خیابان‌ها، دندان‌ها، لیوان‌ها."
            ),
            # QEYD: dərslikdəki «مانند مثال، جمله بسازید» tapşırığı burada drill
            # kimi deyil, aşağıda ÇALIŞMA 2 (answer_question) kimi verilib.
        },
        {
            "title_az": "Cəm mübtəda və feli (نهادِ جمع و فعل آن)",
            "title_fa": "نهادِ جمع و فعل آن",
            # Hər sətir tətbiqdə ayrıca bənd (•) kimi görünür; izahın açarı —
            # mübtədanın CANLI, yoxsa CANSIZ olması.
            "explanation_az": (
                "Mübtəda (نهاد) cəm olanda felin də cəm olub-olmaması mübtədanın CANLI, yoxsa CANSIZ olmasından asılıdır.\n"
                "CANLI cəm mübtəda (insan, heyvan) → fel MÜTLƏQ cəm olur: دانش‌آموزها در کلاس هستند. ✓ / ... در کلاس است. ✗\n"
                "CANSIZ cəm mübtəda (əşya) → fel həm cəm, həm TƏK ola bilər; hər iki forma düzgündür: این صندلی‌ها تمیز هستند. ✓ = این صندلی‌ها تمیز است. ✓\n"
                "Səbəb: farscada cansız əşyaların cəmi çox vaxt bir bütöv, bir yığın kimi qəbul edilir, ona görə tək fel də qəbul olunur.\n"
                "Qayda yalnız «هستند/است»-ə yox, BÜTÜN fellərə aiddir: می‌پوشند، دارند، معاینه می‌کنند.\n"
                "Cəm şəkilçisinin «ها», yoxsa «ان» olması fərq etmir: دانش‌آموزها və دانش‌آموزان eyni qaydaya tabedir.\n"
                "Yazılı dildə cansız mübtəda üçün daha çox TƏK fel işlədilir: این کاغذها سفید است.\n"
                "Praktik məsləhət: canlıda həmişə CƏM fel işlədin; cansızda seçim sərbəstdir — şübhə edəndə cəm fel həmişə düzgündür."
            ),
            # Dərslikdəki mavi lövhə: solda düzgün (cəm) forma, sağda tək forma —
            # birincidə ✗ (canlı), ikincidə ✓ (cansız).
            "conjugations": [
                {
                    "pronoun_fa": "دانش‌آموزها در کلاس هستند. ✓",
                    "form_fa": "دانش‌آموزها در کلاس است. ✗",
                    "reading_az": "Daneşamuzha dər kelas həstənd. / ... dər kelas əst. ✗",
                    "az": "Şagirdlər sinifdədir — CANLI mübtəda, ona görə yalnız cəm fel olar",
                },
                {
                    "pronoun_fa": "این صندلی‌ها تمیز هستند. ✓",
                    "form_fa": "این صندلی‌ها تمیز است. ✓",
                    "reading_az": "İn səndəliha təmiz həstənd. = İn səndəliha təmiz əst.",
                    "az": "Bu stullar təmizdir — CANSIZ mübtəda, hər iki forma düzgündür",
                },
            ],
            # Dərslikdəki «لطفاً بخوانید» siyahısı: hər bənddə eyni cümlənin
            # cəm və tək variantı yan-yana verilir — ikincinin ✓/✗ olması
            # mübtədanın canlı/cansız olmasından asılıdır.
            "examples": [
                {"fa": "این کاغذها سفید هستند. ✓ ⟵ این کاغذها سفید است. ✓", "reading_az": "İn kağəzha sefid həstənd. = İn kağəzha sefid əst.", "az": "Bu kağızlar ağdır. — کاغذ CANSIZdır, ona görə hər iki fel forması düzgündür."},
                {"fa": "این دخترها مانتو می‌پوشند. ✓ ⟵ این دخترها مانتو می‌پوشد. ✗", "reading_az": "İn doxtərha manto mipuşənd. (mipuşəd ✗)", "az": "Bu qızlar manto geyinirlər. — دختر CANLIdır, tək fel («می‌پوشد») SƏHVdir."},
                {"fa": "پیراهن‌های مردانه، جیب دارند. ✓ ⟵ پیراهن‌های مردانه، جیب دارد. ✓", "reading_az": "Pirahənhaye mərdane, cib darənd. = ... cib darəd.", "az": "Kişi köynəklərinin cibi var. — پیراهن CANSIZdır, hər iki forma düzgündür."},
                {"fa": "پزشکان، بیماران را معاینه می‌کنند. ✓ ⟵ پزشکان، بیماران را معاینه می‌کند. ✗", "reading_az": "Pezeşkan, bimaran ra moayene mikonənd. (mikonəd ✗)", "az": "Həkimlər xəstələri müayinə edirlər. — پزشک CANLIdır, tək fel SƏHVdir."},
            ],
            # Mavi lövhədəki qaydanın öz sözləri ilə yekunu.
            "note_fa": (
                "۱. اگر نهاد، جمع و جان‌دار باشد، فعل حتماً جمع می‌آید:\n"
                "دانش‌آموزها در کلاس هستند. ✓ / دانش‌آموزها در کلاس است. ✗\n"
                "۲. اگر نهاد، جمع و بی‌جان باشد، فعل هم جمع و هم مفرد می‌تواند بیاید:\n"
                "این صندلی‌ها تمیز هستند. ✓ = این صندلی‌ها تمیز است. ✓"
            ),
            "note_reading_az": (
                "1. Əgər nəhad, cəm' va candar başəd, fe'l hətmən cəm' miayəd:\n"
                "Daneşamuzha dər kelas həstənd. / Daneşamuzha dər kelas əst. (ğələt)\n"
                "2. Əgər nəhad, cəm' va bican başəd, fe'l həm cəm' va həm mofrəd mitəvanəd biayəd:\n"
                "İn səndəliha təmiz həstənd. = İn səndəliha təmiz əst."
            ),
            "note_az": (
                "1. Mübtəda cəm və CANLI olarsa, fel mütləq cəm gəlir:\n"
                "دانش‌آموزها در کلاس هستند. ✓ (Şagirdlər sinifdədirlər.) / دانش‌آموزها در کلاس است. ✗\n"
                "2. Mübtəda cəm və CANSIZ olarsa, fel həm cəm, həm tək gələ bilər:\n"
                "این صندلی‌ها تمیز هستند. ✓ = این صندلی‌ها تمیز است. ✓ (Bu stullar təmizdir.)\n"
                "Yəni səhv etmək yalnız birinci halda mümkündür — canlı mübtədada tək fel işlətmək olmaz."
            ),
            # QEYD: dərslikdəki bu tapşırıq artıq ÇALIŞMALAR siyahısındadır.
        },
        {
            "title_az": "Deyək — deməyək: برادرِ من (mənim qardaşım) fel uzlaşması",
            "title_fa": "بگوییم – نگوییم",
            "explanation_az": (
                "Fel danışanla yox, cümlənin ÖZ mübtədası ilə uzlaşır.\n"
                "برادر من درس می‌خواند. ✓ — برادر من درس می‌خوانم. ✗\n"
                "«من ... هستم. برادرم ... است.» — hər cümlənin öz mübtədası və öz feli var."
            ),
            "conjugations": [
                {"pronoun_fa": "برادر من درس فارسی می‌خواند. ✓", "form_fa": "برادر من درس فارسی می‌خوانم. ✗"},
                {"pronoun_fa": "برادرهای ما درس فارسی می‌خوانند. ✓", "form_fa": "برادرهای ما درس فارسی می‌خوانیم. ✗"},
            ],
            "examples": [
                {"fa": "من عکّاس هستم. برادر من خیّاط است.", "reading_az": "Mən əkkas hastəm. Bəradəre mən xəyyat əst.", "az": "Mən fotoqrafam. Mənim qardaşım dərzidir — fel «brat»la uzlaşır, «mən»lə yox."},
                {"fa": "شما مهندس هستی. خواهرت دانش‌آموز است و برادرانت دانش‌جو هستند.", "reading_az": "Şoma mohəndes hasti. Xahərət daneşamuz əst va bəradəranət daneşcu həstənd.", "az": "Sən mühəndissən. Bacın şagirddir, qardaşların isə tələbədirlər."},
                {"fa": "دوستان شما پالتو می‌پوشند یا کاپشن؟ دوستان ما گاهی پالتو و گاهی کاپشن می‌پوشند.", "reading_az": "Dustane şoma palto mipuşənd ya kapşen? Dustane ma gahi palto va gahi kapşen mipuşənd.", "az": "Sizin dostlarınız palto geyinirlər, yoxsa gödəkcə? Dostlarımız bəzən palto, bəzən gödəkcə geyinirlər."},
            ],
            # QEYD: dərslikdəki bu tapşırıq artıq ÇALIŞMALAR siyahısındadır.
        },
    ],
    "exercises": [
        {
            # Çalışma 1 — dərslikdəki «لطفاً جایگزین کنید» (درآوردن / پوشیدن).
            # Dərs 6-nın Çalışma 8 quruluşu: answer_question + çoxrəngli
            # NÜMUNƏ qutusu (verilən sözlər → hazır cavab).
            "kind": "answer_question",
            "title_fa": "لطفاً جایگزین کنید",
            "instruction_az": "Nümunə kimi əvəz edin",
            # Qırmızı — «درآوردن» (çıxarmaq), yaşıl — «پوشیدن» (geyinmək);
            # hər iki fel subyektə görə hallanır.
            "example_fa": (
                "علی پیراهنش را **درمی‌آورد** و ژاکت *می‌پوشد*.\n"
                "من / کاپشن / پالتو\n"
                "من کاپشنم را **درمی‌آورم** و پالتو *می‌پوشم*."
            ),
            "example_reading_az": (
                "Əli pirahənəş ra dər-miavərəd va jaket mipuşəd.\n"
                "Mən / kapşen / palto\n"
                "Mən kapşenəm ra dər-miavərəm va palto mipuşəm."
            ),
            "example_az": (
                "Verilən sözlər: SUBYEKT / ÇIXARILAN GEYİM / GEYİLƏN GEYİM.\n"
                "Quruluş: SUBYEKT + 1-ci geyim + mənsubiyyət şəkilçisi + را درمی‌آورد و + 2-ci geyim + می‌پوشد.\n"
                "Qırmızı «درمی‌آورد» — çıxarır, yaşıl «می‌پوشد» — geyinir.\n"
                "Birinci geyim şəkilçi alır (کاپشنم، پیراهنش، کفشمان) və «را» ilə işlənir; ikincisi şəkilçisiz qalır.\n"
                "Hər iki fel şəxsə görə dəyişir: درمی‌آورم / می‌پوشم — درمی‌آوریم / می‌پوشیم.\n"
                "Tərcümə: Əli köynəyini çıxarır və jaket geyinir."
            ),
            "items": [
                {
                    "fa": "ما / کفش / دمپایی",
                    "reading_az": "Ma / kəfş / dəmpayi",
                    "az": "biz / ayaqqabı / ev başmağı (terlik)",
                    "sample_answer_fa": "ما کفشمان را درمی‌آوریم و دمپایی می‌پوشیم.",
                    "sample_answer_reading_az": "Ma kəfşeman ra dər-miavərim va dəmpayi mipuşim.",
                    "sample_answer_az": "Biz ayaqqabımızı çıxarırıq və ev başmağı geyinirik.",
                },
                {
                    "fa": "من / جوراب نازک / جوراب ضخیم",
                    "reading_az": "Mən / curabe nazok / curabe zəxim",
                    "az": "mən / nazik corab / qalın corab",
                    "sample_answer_fa": "من جوراب نازکم را درمی‌آورم و جوراب ضخیم می‌پوشم.",
                    "sample_answer_reading_az": "Mən curabe nazokəm ra dər-miavərəm va curabe zəxim mipuşəm.",
                    "sample_answer_az": "Mən nazik corabımı çıxarıram və qalın corab geyinirəm.",
                },
                {
                    "fa": "شما / پیراهن / بلوز",
                    "reading_az": "Şoma / pirahən / boluz",
                    "az": "siz / köynək / bluz",
                    "sample_answer_fa": "شما پیراهنتان را درمی‌آورید و بلوز می‌پوشید.",
                    "sample_answer_reading_az": "Şoma pirahənetan ra dər-miavərid va boluz mipuşid.",
                    "sample_answer_az": "Siz köynəyinizi çıxarırsınız və bluz geyinirsiniz.",
                },
                {
                    "fa": "او / پیراهن آستین‌کوتاه / پیراهن آستین‌بلند",
                    "reading_az": "U / pirahəne astin-kutah / pirahəne astin-bolənd",
                    "az": "o / qısaqol köynək / uzunqol köynək",
                    "sample_answer_fa": "او پیراهن آستین‌کوتاهش را درمی‌آورد و پیراهن آستین‌بلند می‌پوشد.",
                    "sample_answer_reading_az": "U pirahəne astin-kutaheş ra dər-miavərəd va pirahəne astin-bolənd mipuşəd.",
                    "sample_answer_az": "O, qısaqol köynəyini çıxarır və uzunqol köynək geyinir.",
                },
            ],
        },
        {
            # Çalışma 2 — dərslikdəki «مانند مثال، جمله بسازید» (cəm «ها» + «را»).
            # Əvvəllər Mövzu 1-in daxili drill-i idi; Çalışma 1 ilə eyni
            # quruluşa (answer_question + çoxrəngli NÜMUNƏ qutusu) keçirilib.
            "kind": "answer_question",
            "title_fa": "مانند مثال، جمله بسازید",
            "instruction_az": "Nümunə kimi cümlə qurun",
            # Yaşıl «ها» — cəm şəkilçisi (hər iki isimdə), qırmızı «را» — obyekt əlaməti.
            "example_fa": (
                "خیّاط / لباس / اتو زدن\n"
                "*خیّاط‌ها*، *لباس‌ها* **را** اتو می‌زنند."
            ),
            "example_reading_az": (
                "Xəyyat / lebas / otu zədən\n"
                "Xəyyatha, lebasha ra otu mizənənd."
            ),
            "example_az": (
                "Verilən sözlər: SUBYEKT / OBYEKT / MƏSDƏR.\n"
                "Quruluş: SUBYEKT + ها، OBYEKT + ها + را + FEL (cəm).\n"
                "Yaşıl «ها» — hər iki isim CƏM olur; qırmızı «را» — müəyyən obyektin əlamətidir.\n"
                "Məsdər cəm mübtədaya görə hallanır: اتو زدن → اتو می‌زنند.\n"
                "«درس دادن» və «کمک کردن» kimi fellərdə «را» yox, «به» işlənir: به دانش‌جوها درس می‌دهند.\n"
                "Tərcümə: Dərzilər paltarları ütüləyirlər."
            ),
            "items": [
                {
                    "fa": "آن پسر / کفش / پوشیدن",
                    "reading_az": "An pesər / kəfş / puşidən",
                    "az": "o oğlan / ayaqqabı / geyinmək",
                    "sample_answer_fa": "آن پسرها، کفش‌ها را می‌پوشند.",
                    "sample_answer_reading_az": "An pesərha, kəfşha ra mipuşənd.",
                    "sample_answer_az": "O oğlanlar ayaqqabıları geyinirlər.",
                },
                {
                    "fa": "استاد / دانش‌جو / درس دادن",
                    "reading_az": "Ostad / daneşcu / dərs dadən",
                    "az": "müəllim / tələbə / dərs demək",
                    "sample_answer_fa": "استادها، به دانش‌جوها درس می‌دهند.",
                    "sample_answer_reading_az": "Ostadha, be daneşcuha dərs midəhənd.",
                    "sample_answer_az": "Müəllimlər tələbələrə dərs deyirlər.",
                },
                {
                    "fa": "جوان / پیر / کمک کردن",
                    "reading_az": "Cavan / pir / komək kərdən",
                    "az": "cavan / qoca / kömək etmək",
                    "sample_answer_fa": "جوان‌ها، به پیرها کمک می‌کنند.",
                    "sample_answer_reading_az": "Cavanha, be pirha komək mikonənd.",
                    "sample_answer_az": "Cavanlar qocalara kömək edirlər.",
                },
                {
                    "fa": "رنگ‌کار / دیوار / رنگ زدن",
                    "reading_az": "Rəngkar / divar / rəng zədən",
                    "az": "rəngsaz / divar / rəngləmək",
                    "sample_answer_fa": "رنگ‌کارها، دیوارها را رنگ می‌زنند.",
                    "sample_answer_reading_az": "Rəngkarha, divarha ra rəng mizənənd.",
                    "sample_answer_az": "Rəngsazlar divarları rəngləyirlər.",
                },
                {
                    "fa": "پزشک / بیمار / معاینه کردن",
                    "reading_az": "Pezeşk / bimar / moayene kərdən",
                    "az": "həkim / xəstə / müayinə etmək",
                    "sample_answer_fa": "پزشک‌ها، بیمارها را معاینه می‌کنند.",
                    "sample_answer_reading_az": "Pezeşkha, bimarha ra moayene mikonənd.",
                    "sample_answer_az": "Həkimlər xəstələri müayinə edirlər.",
                },
                {
                    "fa": "مادر / فرزند / دوست داشتن",
                    "reading_az": "Madər / fərzənd / dust daştən",
                    "az": "ana / övlad / sevmək",
                    "sample_answer_fa": "مادرها، فرزندانشان را دوست دارند.",
                    "sample_answer_reading_az": "Madərha, fərzəndanəşan ra dust darənd.",
                    "sample_answer_az": "Analar övladlarını sevirlər.",
                },
            ],
        },
        {
            # Çalışma 3 — səh. 93 «جمله‌های اشتباه را تصحیح کنید» (5 bənd).
            # Əvvəllər Mövzu 2-nin drill-i idi və yalnız 3 bəndi vardı;
            # dərslikdəki 5 bəndlə tam şəkildə çalışmaya çevrilib.
            "kind": "answer_question",
            "title_fa": "جمله‌های اشتباه را تصحیح کنید",
            "instruction_az": "Səhv cümlələri düzəldin",
            # Qırmızı — səhv (tək) fel, yaşıl — düzgün (cəm) fel.
            "example_fa": (
                "دانش‌آموزها در کلاس **است**.\n"
                "دانش‌آموزها در کلاس *هستند*."
            ),
            "example_reading_az": (
                "Daneşamuzha dər kelas əst. (ğələt)\n"
                "Daneşamuzha dər kelas həstənd."
            ),
            "example_az": (
                "Mübtəda cəm və CANLI olanda fel mütləq cəm olmalıdır.\n"
                "Qırmızı — səhv tək fel, yaşıl — düzgün cəm fel.\n"
                "Mübtəda CANSIZ olanda tək fel də düzgündür, amma bu tapşırıqda hamısı cəm formaya çevrilir.\n"
                "Tərcümə: Şagirdlər sinifdədirlər."
            ),
            "items": [
                {
                    "fa": "کارگران بیل و تیشه دارد.",
                    "reading_az": "Kargəran bil va tişe darəd. (səhv)",
                    "az": "Fəhlələrin beli və külüngü var. — کارگران canlı və cəmdir",
                    "sample_answer_fa": "کارگران بیل و تیشه دارند.",
                    "sample_answer_reading_az": "Kargəran bil va tişe darənd.",
                    "sample_answer_az": "Fəhlələrin beli və külüngü var. (canlı cəm → fel mütləq cəm)",
                },
                {
                    "fa": "این کلاه‌ها آبی و صورتی است.",
                    "reading_az": "İn kolahha abi va surəti əst.",
                    "az": "Bu papaqlar mavi və çəhrayıdır. — کلاه cansızdır",
                    "sample_answer_fa": "این کلاه‌ها آبی و صورتی هستند.",
                    "sample_answer_reading_az": "İn kolahha abi va surəti həstənd.",
                    "sample_answer_az": "Bu papaqlar mavi və çəhrayıdır. (cansız olduğu üçün «است» də düzgündür, amma burada cəm forma istənir)",
                },
                {
                    "fa": "جوانان به پیرمردها کمک می‌کند.",
                    "reading_az": "Cəvanan be pirmərdha komək mikonəd. (səhv)",
                    "az": "Gənclər qocalara kömək edirlər. — جوانان canlı və cəmdir",
                    "sample_answer_fa": "جوانان به پیرمردها کمک می‌کنند.",
                    "sample_answer_reading_az": "Cəvanan be pirmərdha komək mikonənd.",
                    "sample_answer_az": "Gənclər qocalara kömək edirlər. (canlı cəm → fel mütləq cəm)",
                },
                {
                    "fa": "سرویس‌های بهداشتی، شیر آب دارد.",
                    "reading_az": "Servishaye behdaşti, şire ab darəd.",
                    "az": "Sanitar qovşaqlarının su kranı var. — سرویس cansızdır",
                    "sample_answer_fa": "سرویس‌های بهداشتی، شیر آب دارند.",
                    "sample_answer_reading_az": "Servishaye behdaşti, şire ab darənd.",
                    "sample_answer_az": "Sanitar qovşaqlarının su kranı var. (cansız olduğu üçün «دارد» da düzgündür)",
                },
                {
                    "fa": "آن کودکان درس می‌خواند و تکلیف می‌نویسد.",
                    "reading_az": "An kudəkan dərs mixanəd va təklif minevisəd. (səhv)",
                    "az": "O uşaqlar dərs oxuyur və tapşırıq yazırlar. — کودکان canlı və cəmdir",
                    "sample_answer_fa": "آن کودکان درس می‌خوانند و تکلیف می‌نویسند.",
                    "sample_answer_reading_az": "An kudəkan dərs mixanənd va təklif minevisənd.",
                    "sample_answer_az": "O uşaqlar dərs oxuyur və tapşırıq yazırlar. (hər iki fel cəm olmalıdır)",
                },
            ],
        },
        {
            # Çalışma 4 — səh. 94 «با واژه یا واژه‌های درست کامل کنید».
            # Dərslikdə hər bənd üçün İKİ variant verilir və biri seçilir, ona
            # görə söz bankında 12 çip var (6 düzgün + 6 çeldirici).
            "kind": "fill_blank",
            "instruction_az": "با واژه یا واژه‌های درست کامل کنید — düzgün söz və ya sözlərlə tamamlayın (hər cümlə üçün iki variantdan biri düzgündür).",
            "word_bank": [
                "کتاب", "کتاب‌ها", "خانم", "خانم‌ها", "است", "هستند",
                "کودک", "کودکان", "می‌پزد", "می‌پزند", "دارد", "دارند",
            ],
            "items": [
                {
                    "fa_with_blank": "این ___ رنگی است.",
                    "correct_answer": "کتاب",
                    "reading_az": "ketab",
                    "az": "kitab",
                    "full_reading_az": "İn ketab rəngi əst.",
                    "full_translation_az": "Bu kitab rənglidir. — «است» tək olduğu üçün mübtəda da tək olur.",
                },
                {
                    "fa_with_blank": "آن ___ ، لباس می‌دوزد.",
                    "correct_answer": "خانم",
                    "reading_az": "xanom",
                    "az": "xanım",
                    "full_reading_az": "An xanom, lebas miduzəd.",
                    "full_translation_az": "O xanım paltar tikir. — fel tək və mübtəda canlıdır, ona görə «خانم‌ها» olmaz.",
                },
                {
                    "fa_with_blank": "آن کفش‌ها زنانه ___ .",
                    "correct_answer": "هستند",
                    "reading_az": "həstənd",
                    "az": "-dır (cəm)",
                    "full_reading_az": "An kəfşha zənane həstənd.",
                    "full_translation_az": "O ayaqqabılar qadın ayaqqabısıdır. — کفش cansızdır, ona görə «است» də düzgün sayılır.",
                },
                {
                    "fa_with_blank": "این ___ ، آبرنگ می‌خواهند.",
                    "correct_answer": "کودکان",
                    "reading_az": "kudəkan",
                    "az": "uşaqlar",
                    "full_reading_az": "İn kudəkan, abrəng mixahənd.",
                    "full_translation_az": "Bu uşaqlar akvarel istəyirlər. — fel cəmdir («می‌خواهند»), ona görə mübtəda da cəm olmalıdır.",
                },
                {
                    "fa_with_blank": "آشپزها در آشپزخانه غذا ___ .",
                    "correct_answer": "می‌پزند",
                    "reading_az": "mipəzənd",
                    "az": "bişirirlər",
                    "full_reading_az": "Aşpəzha dər aşpəzxane qəza mipəzənd.",
                    "full_translation_az": "Aşpazlar mətbəxdə yemək bişirirlər. — آشپزها canlı və cəmdir, fel mütləq cəm olur.",
                },
                {
                    "fa_with_blank": "آن پیراهن‌ها آستین و یقه ___ .",
                    "correct_answer": "دارند",
                    "reading_az": "darənd",
                    "az": "var (cəm)",
                    "full_reading_az": "An pirahənha astin va yəqe darənd.",
                    "full_translation_az": "O köynəklərin qolu və yaxası var. — پیراهن cansızdır, ona görə «دارد» da düzgündür.",
                },
            ],
        },
        {
            # Çalışma 5 — səh. 94 «جمع کدام واژه‌ها با «ان» درست است.»
            # Dərslikdə 15 söz verilir; hər sözün «ان» ilə cəmlənə bilib-
            # bilməməsi canlı/cansız qaydası ilə yoxlanır.
            "kind": "answer_question",
            "title_fa": "جمع کدام واژه‌ها با «ان» درست است؟",
            "instruction_az": "Hansı sözlərin «ان» ilə cəmi düzgündür? Hər söz üçün cavabı yoxlayın",
            # Yaşıl — «ان» mümkün olan söz, qırmızı — mümkün olmayan.
            "example_fa": (
                "پسر ← *پسران* ✓ (جان‌دار)\n"
                "پیراهن ← **پیراهنان** ✗ — پیراهن‌ها ✓ (بی‌جان)"
            ),
            "example_reading_az": (
                "pesər → pesəran ✓ (candar)\n"
                "pirahən → pirahənan ✗ — pirahənha ✓ (bican)"
            ),
            "example_az": (
                "Qayda: «ان» yalnız CANLI varlıqlara qoşulur (insan, heyvan, bitki).\n"
                "Cansız sözlərdə yalnız «ها» işlənir.\n"
                "Diqqət: bəzi sözlərin sonundakı «ان» cəm əlaməti deyil, sözün öz hissəsidir — "
                "خیابان، خلبان، بیمارستان kimi. Onlar da «ها» ilə cəmlənir: خیابان‌ها، خلبان‌ها.\n"
                "Yaşıl — «ان» düzgündür, qırmızı — düzgün deyil."
            ),
            "items": [
                {
                    "fa": "پسر", "reading_az": "pesər", "az": "oğlan",
                    "sample_answer_fa": "پسران ✓ (پسرها هم درست است)",
                    "sample_answer_reading_az": "pesəran ✓ / pesərha ✓",
                    "sample_answer_az": "Düzgündür — insandır, canlıdır.",
                },
                {
                    "fa": "پیراهن", "reading_az": "pirahən", "az": "köynək",
                    "sample_answer_fa": "پیراهنان ✗ — پیراهن‌ها ✓",
                    "sample_answer_reading_az": "pirahənan ✗ — pirahənha ✓",
                    "sample_answer_az": "Düzgün deyil — köynək cansızdır.",
                },
                {
                    "fa": "خلبان", "reading_az": "xəlleban", "az": "pilot",
                    "sample_answer_fa": "خلبانان ✓ (خلبان‌ها هم درست است)",
                    "sample_answer_reading_az": "xəllebanan ✓ / xəllebanha ✓",
                    "sample_answer_az": "Düzgündür — pilot canlıdır. Diqqət: sözün öz sonundakı «ان» cəm əlaməti deyil.",
                },
                {
                    "fa": "فرزند", "reading_az": "fərzənd", "az": "övlad",
                    "sample_answer_fa": "فرزندان ✓ (فرزندها هم درست است)",
                    "sample_answer_reading_az": "fərzəndan ✓ / fərzəndha ✓",
                    "sample_answer_az": "Düzgündür — insandır, canlıdır.",
                },
                {
                    "fa": "چسب", "reading_az": "çəsb", "az": "yapışqan",
                    "sample_answer_fa": "چسبان ✗ — چسب‌ها ✓",
                    "sample_answer_reading_az": "çəsban ✗ — çəsbha ✓",
                    "sample_answer_az": "Düzgün deyil — yapışqan cansızdır.",
                },
                {
                    "fa": "همسر", "reading_az": "həmsər", "az": "həyat yoldaşı",
                    "sample_answer_fa": "همسران ✓ (همسرها هم درست است)",
                    "sample_answer_reading_az": "həmsəran ✓ / həmsərha ✓",
                    "sample_answer_az": "Düzgündür — insandır, canlıdır.",
                },
                {
                    "fa": "هواپیما", "reading_az": "həvapeyma", "az": "təyyarə",
                    "sample_answer_fa": "هواپیمایان ✗ — هواپیماها ✓",
                    "sample_answer_reading_az": "həvapeymaha ✓",
                    "sample_answer_az": "Düzgün deyil — təyyarə cansızdır.",
                },
                {
                    "fa": "خیابان", "reading_az": "xiyaban", "az": "küçə",
                    "sample_answer_fa": "خیابان‌ها ✓ (سونداکی «ان» جزء کلمه است)",
                    "sample_answer_reading_az": "xiyabanha ✓",
                    "sample_answer_az": "«ان» ilə cəmlənmir — küçə cansızdır; üstəlik sonundakı «ان» sözün öz hissəsidir.",
                },
                {
                    "fa": "دانش‌آموز", "reading_az": "daneşamuz", "az": "şagird",
                    "sample_answer_fa": "دانش‌آموزان ✓ (دانش‌آموزها هم درست است)",
                    "sample_answer_reading_az": "daneşamuzan ✓ / daneşamuzha ✓",
                    "sample_answer_az": "Düzgündür — insandır, canlıdır.",
                },
                {
                    "fa": "معلّم", "reading_az": "moəllem", "az": "müəllim",
                    "sample_answer_fa": "معلّمان ✓ (معلّم‌ها هم درست است)",
                    "sample_answer_reading_az": "moəlleman ✓ / moəllemha ✓",
                    "sample_answer_az": "Düzgündür — insandır, canlıdır.",
                },
                {
                    "fa": "درخت", "reading_az": "dəraxt", "az": "ağac",
                    "sample_answer_fa": "درختان ✓ (درخت‌ها هم درست است)",
                    "sample_answer_reading_az": "dərəxtan ✓ / dəraxtha ✓",
                    "sample_answer_az": "Düzgündür — farscada bitkilər canlı sayılır.",
                },
                {
                    "fa": "پشت‌بام", "reading_az": "poştbam", "az": "dam",
                    "sample_answer_fa": "پشت‌بامان ✗ — پشت‌بام‌ها ✓",
                    "sample_answer_reading_az": "poştbamha ✓",
                    "sample_answer_az": "Düzgün deyil — dam cansızdır.",
                },
                {
                    "fa": "تکلیف", "reading_az": "təklif", "az": "ev tapşırığı",
                    "sample_answer_fa": "تکلیفان ✗ — تکلیف‌ها ✓",
                    "sample_answer_reading_az": "təklifha ✓",
                    "sample_answer_az": "Düzgün deyil — tapşırıq cansızdır.",
                },
                {
                    "fa": "زیپ", "reading_az": "zip", "az": "zəncirbənd",
                    "sample_answer_fa": "زیپان ✗ — زیپ‌ها ✓",
                    "sample_answer_reading_az": "zipha ✓",
                    "sample_answer_az": "Düzgün deyil — zəncirbənd cansızdır.",
                },
                {
                    "fa": "مادر", "reading_az": "madər", "az": "ana",
                    "sample_answer_fa": "مادران ✓ (مادرها هم درست است)",
                    "sample_answer_reading_az": "madəran ✓ / madərha ✓",
                    "sample_answer_az": "Düzgündür — insandır, canlıdır.",
                },
            ],
        },
        {
            # Çalışma 6 — səh. 94 «لطفاً جایگزین کنید» («برای … انتخاب کردن»).
            # Əvvəllər sadə practice_reveal idi; Dərs 5/6 quruluşuna keçirilib.
            "kind": "answer_question",
            "title_fa": "لطفاً جایگزین کنید",
            "instruction_az": "Nümunə kimi əvəz edin («برای … انتخاب کردن»)",
            # Qırmızı «را» — obyekt əlaməti, yaşıl «برای» — məqsəd.
            "example_fa": (
                "من / پیراهن سفید / پوشیدن\n"
                "من پیراهن سفید **را** *برای* پوشیدن انتخاب می‌کنم."
            ),
            "example_reading_az": (
                "Mən / pirahəne sefid / puşidən\n"
                "Mən pirahəne sefid ra bəraye puşidən entexab mikonəm."
            ),
            "example_az": (
                "Verilən sözlər: SUBYEKT / SEÇİLƏN ŞEY / MƏQSƏD (məsdər).\n"
                "Quruluş: SUBYEKT + SEÇİLƏN ŞEY + را + برای + MƏSDƏR + انتخاب می‌کند.\n"
                "Qırmızı «را» seçilən şeyin, yaşıl «برای» məqsədin qarşısında gəlir.\n"
                "«انتخاب کردن» feli subyektin şəxsinə görə hallanır.\n"
                "Tərcümə: Mən geyinmək üçün ağ köynəyi seçirəm."
            ),
            "items": [
                {
                    "fa": "شما / خودکار آبی / نوشتن",
                    "reading_az": "Şoma / xodkare abi / neveştən",
                    "az": "siz / mavi tükənməz qələm / yazmaq",
                    "sample_answer_fa": "شما خودکار آبی را برای نوشتن انتخاب می‌کنید.",
                    "sample_answer_reading_az": "Şoma xodkare abi ra bəraye neveştən entexab mikonid.",
                    "sample_answer_az": "Siz yazmaq üçün mavi tükənməz qələmi seçirsiniz.",
                },
                {
                    "fa": "آن‌ها / جامعة المصطفی / درس خواندن",
                    "reading_az": "Anha / Cameətol-Mostəfa / dərs xandən",
                    "az": "onlar / əl-Müstəfa Cəmiyyəti / oxumaq",
                    "sample_answer_fa": "آن‌ها جامعة المصطفی را برای درس خواندن انتخاب می‌کنند.",
                    "sample_answer_reading_az": "Anha Cameətol-Mostəfa ra bəraye dərs-xandən entexab mikonənd.",
                    "sample_answer_az": "Onlar oxumaq üçün əl-Müstəfa Cəmiyyətini seçirlər.",
                },
                {
                    "fa": "مادرم / این فروش‌گاه / خریدن پوشاک",
                    "reading_az": "Madərəm / in foruşgah / xəridəne puşak",
                    "az": "anam / bu mağaza / geyim almaq",
                    "sample_answer_fa": "مادرم این فروش‌گاه را برای خریدن پوشاک انتخاب می‌کند.",
                    "sample_answer_reading_az": "Madərəm in foruşgah ra bəraye xəridəne puşak entexab mikonəd.",
                    "sample_answer_az": "Anam geyim almaq üçün bu mağazanı seçir.",
                },
                {
                    "fa": "فرزندان او / مقوّای رنگی / نقّاشی کشیدن",
                    "reading_az": "Fərzəndane u / moqəvvaye rəngi / nəqqaşi keşidən",
                    "az": "onun övladları / rəngli karton / rəsm çəkmək",
                    "sample_answer_fa": "فرزندان او مقوّای رنگی را برای نقّاشی کشیدن انتخاب می‌کنند.",
                    "sample_answer_reading_az": "Fərzəndane u moqəvvaye rəngi ra bəraye nəqqaşi-keşidən entexab mikonənd.",
                    "sample_answer_az": "Onun övladları rəsm çəkmək üçün rəngli kartonu seçirlər.",
                },
                {
                    "fa": "برادرم / اداره‌ی پست / کار کردن",
                    "reading_az": "Bəradərəm / edareye post / kar kərdən",
                    "az": "qardaşım / poçt idarəsi / işləmək",
                    "sample_answer_fa": "برادرم اداره‌ی پست را برای کار کردن انتخاب می‌کند.",
                    "sample_answer_reading_az": "Bəradərəm edareye post ra bəraye kar-kərdən entexab mikonəd.",
                    "sample_answer_az": "Qardaşım işləmək üçün poçt idarəsini seçir.",
                },
                {
                    "fa": "پدرم / آن بنّا / ساختن خانه",
                    "reading_az": "Pedərəm / an bənna / saxtəne xane",
                    "az": "atam / o bənna / ev tikmək",
                    "sample_answer_fa": "پدرم آن بنّا را برای ساختن خانه انتخاب می‌کند.",
                    "sample_answer_reading_az": "Pedərəm an bənna ra bəraye saxtəne xane entexab mikonəd.",
                    "sample_answer_az": "Atam ev tikmək üçün o bənnanı seçir.",
                },
            ],
        },
        {
            # Çalışma 7 — səh. 95 «تصحیح کنید» (بگوییم – نگوییم mövzusu).
            # Əvvəllər Mövzu 3-ün drill-i idi.
            "kind": "answer_question",
            "title_fa": "تصحیح کنید",
            "instruction_az": "Səhv cümlələri düzəldin (fel cümlənin öz mübtədası ilə uzlaşmalıdır)",
            # Qırmızı — səhv fel, yaşıl — düzgün fel.
            "example_fa": (
                "برادر من درس فارسی **می‌خوانم**.\n"
                "برادر من درس فارسی *می‌خواند*."
            ),
            "example_reading_az": (
                "Bəradəre mən dərse farsi mixanəm. (ğələt)\n"
                "Bəradəre mən dərse farsi mixanəd."
            ),
            "example_az": (
                "Fel danışanla («من»/«ما») deyil, cümlənin ÖZ mübtədası ilə uzlaşır.\n"
                "«برادر من» üçüncü şəxs təkdir, ona görə fel «می‌خواند» olur.\n"
                "Mübtədanın tərkibindəki «من/ما/شما» sözü aldadıcıdır — əsas söz onun önündəki isimdir.\n"
                "Tərcümə: Mənim qardaşım fars dili oxuyur."
            ),
            "items": [
                {
                    "fa": "استادِ شما درس می‌دهید.",
                    "reading_az": "Ostade şoma dərs midəhid. (səhv)",
                    "az": "Sizin müəlliminiz dərs deyir. — mübtəda «استاد»dır, «شما» deyil",
                    "sample_answer_fa": "استادِ شما درس می‌دهد.",
                    "sample_answer_reading_az": "Ostade şoma dərs midəhəd.",
                    "sample_answer_az": "Sizin müəlliminiz dərs deyir. (3-cü şəxs tək)",
                },
                {
                    "fa": "فرزندان ما دندان‌پزشک هستیم.",
                    "reading_az": "Fərzəndane ma dəndanpezeşk hastim. (səhv)",
                    "az": "Bizim övladlarımız diş həkimidir. — mübtəda «فرزندان»dır",
                    "sample_answer_fa": "فرزندان ما دندان‌پزشک هستند.",
                    "sample_answer_reading_az": "Fərzəndane ma dəndanpezeşk həstənd.",
                    "sample_answer_az": "Bizim övladlarımız diş həkimidirlər. (3-cü şəxs cəm)",
                },
                {
                    "fa": "دوستان او لباس‌ها را اتو می‌زند.",
                    "reading_az": "Dustane u lebasha ra otu mizənəd. (səhv)",
                    "az": "Onun dostları paltarları ütüləyirlər. — mübtəda «دوستان» cəmdir",
                    "sample_answer_fa": "دوستان او لباس‌ها را اتو می‌زنند.",
                    "sample_answer_reading_az": "Dustane u lebasha ra otu mizənənd.",
                    "sample_answer_az": "Onun dostları paltarları ütüləyirlər. (canlı cəm → fel cəm)",
                },
                {
                    "fa": "هم‌کلاس من این پیراهن را می‌پوشم.",
                    "reading_az": "Həmkelase mən in pirahən ra mipuşəm. (səhv)",
                    "az": "Mənim sinif yoldaşım bu köynəyi geyinir. — mübtəda «هم‌کلاس»dır",
                    "sample_answer_fa": "هم‌کلاس من این پیراهن را می‌پوشد.",
                    "sample_answer_reading_az": "Həmkelase mən in pirahən ra mipuşəd.",
                    "sample_answer_az": "Mənim sinif yoldaşım bu köynəyi geyinir. (3-cü şəxs tək)",
                },
            ],
        },
        {
            # Çalışma 8 — səh. 98 «لطفاً با فعل مناسب کامل کنید».
            "kind": "fill_blank",
            "instruction_az": "لطفاً با فعل مناسب کامل کنید — uyğun fellə tamamlayın.",
            "word_bank": ["اتو می‌زنند", "انتخاب می‌کند", "می‌گذارد", "می‌شوید", "می‌کنند"],
            "items": [
                {
                    "fa_with_blank": "دوستان ما لباس‌ها را اتو ___ .",
                    "correct_answer": "اتو می‌زنند",
                    "reading_az": "otu mizənənd",
                    "az": "ütüləyirlər",
                    "full_reading_az": "Dustane ma lebasha ra otu mizənənd.",
                    "full_translation_az": "Dostlarımız paltarları ütüləyirlər.",
                },
                {
                    "fa_with_blank": "برادرت کدام کلاه را انتخاب ___ ؟",
                    "correct_answer": "انتخاب می‌کند",
                    "reading_az": "entexab mikonəd",
                    "az": "seçir",
                    "full_reading_az": "Bəradərət kodam kolah ra entexab mikonəd?",
                    "full_translation_az": "Qardaşın hansı papağı seçir?",
                },
                {
                    "fa_with_blank": "خواهر من لباس‌ها را در لباس‌شویی ___ .",
                    "correct_answer": "می‌گذارد",
                    "reading_az": "migozarəd",
                    "az": "qoyur",
                    "full_reading_az": "Xahəre mən lebasha ra dər ləbasşuyi migozarəd.",
                    "full_translation_az": "Bacım paltarları paltaryuyana qoyur. — «در لباس‌شویی» (içinə) olduğu üçün «می‌گذارد».",
                },
                {
                    "fa_with_blank": "خواهر من لباس‌ها را با لباس‌شویی ___ .",
                    "correct_answer": "می‌شوید",
                    "reading_az": "mişuyəd",
                    "az": "yuyur",
                    "full_reading_az": "Xahəre mən lebasha ra ba ləbasşuyi mişuyəd.",
                    "full_translation_az": "Bacım paltarları paltaryuyanla yuyur. — «با لباس‌شویی» (vasitə) olduğu üçün «می‌شوید».",
                },
                {
                    "fa_with_blank": "آیا دوستانتان در تمیزکردن اتاق به شما کمک ___ ؟",
                    "correct_answer": "می‌کنند",
                    "reading_az": "mikonənd",
                    "az": "edirlər",
                    "full_reading_az": "Aya dustanetan dər təmiz-kərdəne otaq be şoma komək mikonənd?",
                    "full_translation_az": "Dostlarınız otağı təmizləməkdə sizə kömək edirlərmi?",
                },
            ],
        },
        {
            # Çalışma 9 — səh. 98 «مانند مثال، جمله‌های زیر را تغییر دهید».
            # Əvvəllər sadə practice_reveal idi.
            "kind": "answer_question",
            "title_fa": "مانند مثال، جمله‌های زیر را تغییر دهید",
            "instruction_az": "Nümunə kimi cümlələri dəyişin (mötərizədəki yeni mübtəda ilə)",
            # Qırmızı — köhnə mübtəda, yaşıl — yeni mübtəda (fel ona görə dəyişir).
            "example_fa": (
                "**شما** از خودکار آبی و قرمز استفاده می‌کنید. (استاد شما)\n"
                "*استاد شما* از خودکار آبی و قرمز استفاده می‌کند."
            ),
            "example_reading_az": (
                "Şoma əz xodkare abi va qermez estefade mikonid. (Ostade şoma)\n"
                "Ostade şoma əz xodkare abi va qermez estefade mikonəd."
            ),
            "example_az": (
                "Cümlədəki mübtəda mötərizədə verilən yeni mübtəda ilə əvəz olunur.\n"
                "Qırmızı — köhnə mübtəda, yaşıl — yeni mübtəda.\n"
                "Fel YENİ mübtədanın şəxsinə görə dəyişir: می‌کنید → می‌کند.\n"
                "Cümlənin qalan hissəsi olduğu kimi qalır.\n"
                "Tərcümə: Sizin müəlliminiz mavi və qırmızı qələmdən istifadə edir."
            ),
            "items": [
                {
                    "fa": "آن‌ها اتاق را تمیز می‌کنند. (دوست آن‌ها)",
                    "reading_az": "Anha otaq ra təmiz mikonənd. (Duste anha)",
                    "az": "Onlar otağı təmizləyirlər. (onların dostu)",
                    "sample_answer_fa": "دوست آن‌ها اتاق را تمیز می‌کند.",
                    "sample_answer_reading_az": "Duste anha otaq ra təmiz mikonəd.",
                    "sample_answer_az": "Onların dostu otağı təmizləyir. (yeni mübtəda tək → fel tək)",
                },
                {
                    "fa": "من روسری قهوه‌ای را انتخاب می‌کنم. (مادر من)",
                    "reading_az": "Mən rusəriye qəhvei ra entexab mikonəm. (Madəre mən)",
                    "az": "Mən qəhvəyi baş örtüyünü seçirəm. (mənim anam)",
                    "sample_answer_fa": "مادر من روسری قهوه‌ای را انتخاب می‌کند.",
                    "sample_answer_reading_az": "Madəre mən rusəriye qəhvei ra entexab mikonəd.",
                    "sample_answer_az": "Anam qəhvəyi baş örtüyünü seçir. (3-cü şəxs tək)",
                },
                {
                    "fa": "شما لباس‌ها را می‌شویی و اتو می‌زنی. (همسر شما)",
                    "reading_az": "Şoma lebasha ra mişuyi va otu mizəni. (Həmsəre şoma)",
                    "az": "Sən paltarları yuyub ütüləyirsən. (sizin həyat yoldaşınız)",
                    "sample_answer_fa": "همسر شما لباس‌ها را می‌شوید و اتو می‌زند.",
                    "sample_answer_reading_az": "Həmsəre şoma lebasha ra mişuyəd va otu mizənəd.",
                    "sample_answer_az": "Həyat yoldaşınız paltarları yuyur və ütüləyir. (hər iki fel dəyişir)",
                },
                {
                    "fa": "ما در زمستان لباس‌های نازک را درمی‌آوریم و لباس‌های ضخیم می‌پوشیم. (دوستان ما)",
                    "reading_az": "Ma dər zemestan lebashaye nazok ra dər-miavərim va lebashaye zəxim mipuşim. (Dustane ma)",
                    "az": "Biz qışda nazik paltarları çıxarıb qalın paltar geyinirik. (bizim dostlarımız)",
                    "sample_answer_fa": "دوستان ما در زمستان لباس‌های نازک را درمی‌آورند و لباس‌های ضخیم می‌پوشند.",
                    "sample_answer_reading_az": "Dustane ma dər zemestan lebashaye nazok ra dər-miavərənd va lebashaye zəxim mipuşənd.",
                    "sample_answer_az": "Dostlarımız qışda nazik paltarları çıxarır və qalın paltarlar geyinirlər.",
                },
            ],
        },
        {
            # Çalışma 10 — səh. 98 «با استفاده از واژه‌ی «هنگام» جمله بسازید».
            # Əvvəllər sadə practice_reveal idi.
            "kind": "answer_question",
            "title_fa": "با استفاده از واژه‌ی «هنگام» جمله بسازید",
            "instruction_az": "«هنگام» sözü ilə cümlə qurun",
            # Yaşıl «هنگام» — «…-arkən, … vaxtı» mənasında məsdərin önündə.
            "example_fa": (
                "من / درس خواندن / اتاق مطالعه / رفتن\n"
                "من *هنگام* درس خواندن به اتاق مطالعه می‌روم."
            ),
            "example_reading_az": (
                "Mən / dərs xandən / otaqe motaleə / rəftən\n"
                "Mən hengame dərs-xandən be otaqe motaleə mirəvəm."
            ),
            "example_az": (
                "Verilən sözlər: SUBYEKT / 1-ci İŞ (məsdər) / YER və ya VASİTƏ / 2-ci İŞ (məsdər).\n"
                "Quruluş: SUBYEKT + هنگام + 1-ci MƏSDƏR + ... + 2-ci FEL (hallanmış).\n"
                "Yaşıl «هنگام» məsdərin önündə gəlir və «…-arkən / … vaxtı» mənasını verir; izafətlə oxunur: هنگامِ.\n"
                "Yalnız SONUNCU fel hallanır, «هنگام»dan sonrakı fel məsdər olaraq qalır.\n"
                "Tərcümə: Mən dərs oxuyarkən mütaliə otağına gedirəm."
            ),
            "items": [
                {
                    "fa": "دوستم / ظرف شستن / مادرش / کمک کردن",
                    "reading_az": "Dustəm / zərf şostən / madərəş / komək kərdən",
                    "az": "dostum / qab yumaq / onun anası / kömək etmək",
                    "sample_answer_fa": "دوستم هنگام ظرف شستن به مادرش کمک می‌کند.",
                    "sample_answer_reading_az": "Dustəm hengame zərf-şostən be madərəş komək mikonəd.",
                    "sample_answer_az": "Dostum qab yuyarkən anasına kömək edir.",
                },
                {
                    "fa": "استاد / درس دادن / تابلو و ماژیک / استفاده کردن",
                    "reading_az": "Ostad / dərs dadən / təblo va majik / estefade kərdən",
                    "az": "müəllim / dərs demək / lövhə və marker / istifadə etmək",
                    "sample_answer_fa": "استاد هنگام درس دادن از تابلو و ماژیک استفاده می‌کند.",
                    "sample_answer_reading_az": "Ostad hengame dərs-dadən əz təblo va majik estefade mikonəd.",
                    "sample_answer_az": "Müəllim dərs deyərkən lövhə və markerdən istifadə edir.",
                },
                {
                    "fa": "ما / عید / لباس‌های نو / انتخاب کردن و خریدن",
                    "reading_az": "Ma / eyd / lebashaye nou / entexab kərdən va xəridən",
                    "az": "biz / bayram / təzə paltarlar / seçmək və almaq",
                    "sample_answer_fa": "ما هنگام عید لباس‌های نو انتخاب می‌کنیم و می‌خریم.",
                    "sample_answer_reading_az": "Ma hengame eyd lebashaye nou entexab mikonim va mixərim.",
                    "sample_answer_az": "Biz bayram vaxtı təzə paltarlar seçib alırıq.",
                },
                {
                    "fa": "آن‌ها / زمستان / لباس‌های ضخیم / خریدن و پوشیدن",
                    "reading_az": "Anha / zemestan / lebashaye zəxim / xəridən va puşidən",
                    "az": "onlar / qış / qalın paltarlar / almaq və geyinmək",
                    "sample_answer_fa": "آن‌ها هنگام زمستان لباس‌های ضخیم می‌خرند و می‌پوشند.",
                    "sample_answer_reading_az": "Anha hengame zemestan lebashaye zəxim mixərənd va mipuşənd.",
                    "sample_answer_az": "Onlar qış vaxtı qalın paltarlar alıb geyinirlər.",
                },
            ],
        },
    ],
    "sentence_practice": {
        "listen_exercises": [
            {
                "items": [
                    {
                        "fa": "سارا و یاسر در فروش‌گاه پوشاک کار می‌کنند. آن‌ها لباس‌های زنانه و مردانه می‌فروشند.",
                        "reading_az": "Sara va Yasər dər foruşgahe puşak kar mikonənd. Anha lebashaye zənane va mərdane miforuşənd.",
                        "az": "Sara və Yasər geyim mağazasında işləyirlər. Onlar qadın və kişi geyimləri satırlar.",
                    },
                    {
                        "fa": "پدرم برای من دو پیراهنِ آستین بلند و یک پیراهن آستین کوتاه می‌خرد.",
                        "reading_az": "Pedərəm bəraye mən do pirahəne astin-bolənd va yek pirahəne astin-kutah mixərəd.",
                        "az": "Atam mənə iki uzunqollu köynək və bir qısaqollu köynək alır.",
                    },
                    {
                        "fa": "من در خانه زیرپوش یا پیراهن آستین‌کوتاه و بیرون از خانه پیراهن آستین بلند می‌پوشم.",
                        "reading_az": "Mən dər xane zirpuş ya pirahəne astin-kutah va birun əz xane pirahəne astin-bolənd mipuşəm.",
                        "az": "Mən evdə alt köynəyi və ya qısaqollu köynək, evdən bayırda isə uzunqollu köynək geyinirəm.",
                    },
                    {
                        "fa": "علی و زهرا در روز عید پدر به بازار می‌روند و برای پدرشان یک پیراهن انتخاب می‌کنند و می‌خرند.",
                        "reading_az": "Əli va Zəhra dər ruze eyde pedər be bazar mirəvənd va bəraye pedərşan yek pirahən entexab mikonənd va mixərənd.",
                        "az": "Əli və Zəhra ata günündə bazara gedirlər və ataları üçün bir köynək seçib alırlar.",
                    },
                    {
                        "fa": "همسرم لباس‌های کثیف را با لباس‌شویی می‌شوید و لباس‌های چروک را اتو می‌زند.",
                        "reading_az": "Həmsərəm lebashaye kəsif ra ba ləbasşuyi mişuyəd va lebashaye çoruk ra otu mizənəd.",
                        "az": "Həyat yoldaşım çirkli paltarları paltaryuyanla yuyur və qırışmış paltarları ütüləyir.",
                    },
                    {
                        "fa": "مریم روزهای جمعه در شستن لباس‌ها و تمیزکردن خانه به مادرش کمک می‌کند.",
                        "reading_az": "Məryəm ruzhaye come dər şostəne lebasha va təmiz-kərdəne xane be madərəş komək mikonəd.",
                        "az": "Məryəm cümə günləri paltarları yumaqda və evi təmizləməkdə anasına kömək edir.",
                    },
                    {
                        "fa": "آیا شما در کلاس، کاپشنتان را درمی‌آورید؟ بله، من در کلاسم کاپشنم را درمی‌آورم.",
                        "reading_az": "Aya şoma dər kelas, kapşenetan ra dərmiavərid? Bəle, mən dər kelasəm kapşenəm ra dərmiavəram.",
                        "az": "Siz sinifdə gödəkcənizi çıxarırsınızmı? Bəli, mən sinifdə gödəkcəmi çıxarıram.",
                    },
                    {
                        "fa": "شما کدام روسری را انتخاب می‌کنید؟ من روسری سرمه‌ای را انتخاب می‌کنم.",
                        "reading_az": "Şoma kodam rusəri ra entexab mikonid? Mən rusəriye sormei ra entexab mikonəm.",
                        "az": "Siz hansı baş örtüyünü seçirsiniz? Mən tünd göy baş örtüyünü seçirəm.",
                    },
                    {
                        "fa": "شما در زمستان چه لباس‌هایی می‌پوشید؟ ما در زمستان لباس‌های ضخیم، مانند ژاکت، کاپشن و پالتو می‌پوشیم.",
                        "reading_az": "Şoma dər zemestan çe lebashayi mipuşid? Ma dər zemestan lebashaye zəxim, manənde jaket, kapşen va palto mipuşim.",
                        "az": "Siz qışda hansı paltarları geyinirsiniz? Biz qışda jaket, gödəkcə və palto kimi qalın paltarlar geyinirik.",
                    },
                ],
            },
        ],
        "answer_items": [],
    },
    "reading_text": {
        "title_fa": "بازار",
        "title_az": "Bazar",
        "paragraphs_fa": [
            "در بسیاری از شهرهای ایران، بازار قدیمی و زیبا وجود دارد. در بازار، مغازه‌های زیادی برای فروشِ پوشاک، کفش، فرش، طلا، ظرف، پارچه، پرده و... هست. هر روز مردم زیادی برای خرید به بازار می‌روند. در بازارهای ایران، مسجد هم هست. فروشنده‌ها و خریداران، هنگام اذان برای خواندن نماز به آن‌جا می‌روند.",
            "بازارها نزدیک عید، خیلی شلوغ است. بچّه‌ها در آن روزها با پدر و مادرشان به بازار می‌روند؛ لباس و کفش‌های زیبا انتخاب می‌کنند و می‌خرند. پدر و مادرها هم یا لباس می‌خرند، یا پارچه‌های زیبا انتخاب می‌کنند و خیّاط برای آن‌ها شلوار، پیراهن، چادر و... می‌دوزد.",
            "بچّه‌ها لباس‌های نو را در کمد به چوب‌لباسی آویزان می‌کنند و در روز عید می‌پوشند و به خانه‌ی پدربزرگ‌ها، مادربزرگ‌ها، بستگان و دوستانشان می‌روند.",
        ],
        "footnotes": [
            {"fa": "فروش: فروختن / خرید: خریدن", "az": "satış / alış"},
            {"fa": "قدیمی", "az": "köhnə, qədim"},
            {"fa": "شلوغ / خلوت", "az": "qələbəlik / sakit"},
            {"fa": "هنگام", "az": "…zamanı"},
            {"fa": "چوب‌لباسی", "az": "paltarasan"},
        ],
        "full_translation_az": (
            "İranın bir çox şəhərində köhnə və gözəl bazar var. Bazarda geyim, ayaqqabı, xalça, qızıl, qab-qacaq, "
            "parça, pərdə və s. satışı üçün çoxlu mağaza var. Hər gün çoxlu insan alış-veriş üçün bazara gedir. "
            "İran bazarlarında məscid də var. Satıcılar və alıcılar azan zamanı namaz qılmaq üçün oraya gedirlər.\n\n"
            "Bayrama yaxın bazarlar çox qələbəlik olur. Uşaqlar o günlərdə ata-anaları ilə bazara gedirlər; gözəl "
            "paltar və ayaqqabılar seçib alırlar. Ata-analar da ya paltar alır, ya da gözəl parçalar seçirlər və "
            "dərzi onlar üçün şalvar, köynək, çadra və s. tikir.\n\n"
            "Uşaqlar təzə paltarları şkafda paltarasandan asırlar, bayram günü geyinib babalarının, nənələrinin, "
            "qohumlarının və dostlarının evinə gedirlər."
        ),
        "sentences": [
            {
                "fa": "در بسیاری از شهرهای ایران، بازار قدیمی و زیبا وجود دارد.",
                "reading_az": "Dər besyari əz şəhrhaye Iran, bazare qədimi va ziba vocud darəd.",
                "az": "İranın bir çox şəhərində köhnə və gözəl bazar var.",
                "new_paragraph": True,
            },
            {
                "fa": "در بازار، مغازه‌های زیادی برای فروشِ پوشاک، کفش، فرش، طلا، ظرف، پارچه، پرده و... هست.",
                "reading_az": "Dər bazar, məğazehaye ziyadi bəraye foruşe puşak, kəfş, fərş, təla, zərf, parçe, pərde va ... həst.",
                "az": "Bazarda geyim, ayaqqabı, xalça, qızıl, qab-qacaq, parça, pərdə və s. satışı üçün çoxlu mağaza var.",
            },
            {"fa": "هر روز مردم زیادی برای خرید به بازار می‌روند.", "reading_az": "Hər ruz mərdome ziyadi bəraye xərid be bazar mirəvənd.", "az": "Hər gün çoxlu insan alış-veriş üçün bazara gedir."},
            {"fa": "در بازارهای ایران، مسجد هم هست.", "reading_az": "Dər bazarhaye Iran, məsced həm həst.", "az": "İran bazarlarında məscid də var."},
            {
                "fa": "فروشنده‌ها و خریداران، هنگام اذان برای خواندن نماز به آن‌جا می‌روند.",
                "reading_az": "Foruşendeha va xəridaran, hengame əzan bəraye xandənenəmaz be anja mirəvənd.",
                "az": "Satıcılar və alıcılar azan zamanı namaz qılmaq üçün oraya gedirlər.",
            },
            {
                "fa": "بازارها نزدیک عید، خیلی شلوغ است.",
                "reading_az": "Bazarha nəzdike eyd, xeyli şoluğ əst.",
                "az": "Bayrama yaxın bazarlar çox qələbəlik olur.",
                "new_paragraph": True,
            },
            {
                "fa": "بچّه‌ها در آن روزها با پدر و مادرشان به بازار می‌روند؛ لباس و کفش‌های زیبا انتخاب می‌کنند و می‌خرند.",
                "reading_az": "Bəççeha dər an ruzha ba pedər va madərşan be bazar mirəvənd; lebas va kəfşhaye ziba entexab mikonənd va mixərənd.",
                "az": "Uşaqlar o günlərdə ata-anaları ilə bazara gedirlər; gözəl paltar və ayaqqabılar seçib alırlar.",
            },
            {
                "fa": "پدر و مادرها هم یا لباس می‌خرند، یا پارچه‌های زیبا انتخاب می‌کنند و خیّاط برای آن‌ها شلوار، پیراهن، چادر و... می‌دوزد.",
                "reading_az": "Pedər va madərha həm ya lebas mixərənd, ya parçehaye ziba entexab mikonənd va xəyyat bəraye anha şəlvar, pirahən, çador va ... miduzəd.",
                "az": "Ata-analar da ya paltar alır, ya da gözəl parçalar seçirlər və dərzi onlar üçün şalvar, köynək, çadra və s. tikir.",
            },
            {
                "fa": "بچّه‌ها لباس‌های نو را در کمد به چوب‌لباسی آویزان می‌کنند و در روز عید می‌پوشند و به خانه‌ی پدربزرگ‌ها، مادربزرگ‌ها، بستگان و دوستانشان می‌روند.",
                "reading_az": "Bəççeha lebashaye nou ra dər komod be çublebasi avizan mikonənd va dər ruze eyd mipuşənd va be xane-ye pedərbozorgha, madərbozorgha, bəstegan va dustanəşan mirəvənd.",
                "az": "Uşaqlar təzə paltarları şkafda paltarasandan asırlar, bayram günü geyinib babalarının, nənələrinin, qohumlarının və dostlarının evinə gedirlər.",
                "new_paragraph": True,
            },
        ],
        "comprehension_questions": [
            {
                "question_fa": "در بازار چه مغازه‌هایی وجود دارد؟",
                "reading_az": "Dər bazar çe məğazehayi vocud darəd?",
                "az": "Bazarda hansı mağazalar var?",
                "sample_answer_fa": "در بازار مغازه‌های پوشاک، کفش، فرش، طلا و ظرف وجود دارد.",
                "sample_answer_reading_az": "Dər bazar məğazehaye puşak, kəfş, fərş, təla va zərf vocud darəd.",
                "sample_answer_az": "Bazarda geyim, ayaqqabı, xalça, qızıl və qab-qacaq mağazaları var.",
            },
            {
                "question_fa": "بچّه‌ها هنگام عید چه‌کار می‌کنند؟",
                "reading_az": "Bəççeha hengame eyd çekar mikonənd?",
                "az": "Uşaqlar bayram vaxtı nə edir?",
                "sample_answer_fa": "آن‌ها با پدر و مادرشان به بازار می‌روند و لباس و کفش انتخاب می‌کنند.",
                "sample_answer_reading_az": "Anha ba pedər va madərşan be bazar mirəvənd va lebas va kəfş entexab mikonənd.",
                "sample_answer_az": "Onlar ata-anaları ilə bazara gedir və paltar-ayaqqabı seçirlər.",
            },
            {
                "question_fa": "آیا در بازارهای ایران، مسجد وجود ندارد؟",
                "reading_az": "Aya dər bazarhaye Iran, məsced vocud nədarəd?",
                "az": "İran bazarlarında məscid yoxdurmu?",
                "sample_answer_fa": "چرا، در بازارهای ایران مسجد هم هست.",
                "sample_answer_reading_az": "Çera, dər bazarhaye Iran məsced həm həst.",
                "sample_answer_az": "Xeyr (əksinə), İran bazarlarında məscid də var.",
            },
            {
                "question_fa": "چه وقت بازارهای ایران بسیار شلوغ هستند؟",
                "reading_az": "Çe vaqt bazarhaye Iran besyar şoluğ həstənd?",
                "az": "İran bazarları nə vaxt çox izdihamlı olur?",
                "sample_answer_fa": "بازارهای ایران نزدیک عید، بسیار شلوغ هستند.",
                "sample_answer_reading_az": "Bazarhaye Iran nəzdike eyd, besyar şoluğ həstənd.",
                "sample_answer_az": "İran bazarları bayrama yaxın çox izdihamlı olur.",
            },
            {
                "question_fa": "بچّه‌ها لباس‌های نو را چه‌کار می‌کنند؟",
                "reading_az": "Bəççeha lebashaye nou ra çekar mikonənd?",
                "az": "Uşaqlar təzə paltarları nə edirlər?",
                "sample_answer_fa": "بچّه‌ها لباس‌های نو را در کمد به چوب‌لباسی آویزان می‌کنند.",
                "sample_answer_reading_az": "Bəççeha lebashaye nou ra dər komod be çublebasi avizan mikonənd.",
                "sample_answer_az": "Uşaqlar təzə paltarları şkafda paltarasandan asırlar.",
            },
        ],
    },
}
