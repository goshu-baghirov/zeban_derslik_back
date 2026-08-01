# Dərs 6 — رنگ‌ها (Rənglər)
# Mənbə: کتاب دوم, səh. 75-86

LESSON = {
    "number": 6,
    "title_fa": "رنگ‌ها",
    "title_az": "Rənglər",
    "available": True,
    "vocabulary": [
        {"fa": "سبز", "reading": "səbz", "az": "Yaşıl"},
        {"fa": "قرمز (سرخ)", "reading": "qermez (sorx)", "az": "Qırmızı"},
        {"fa": "صورتی", "reading": "surəti", "az": "Çəhrayı"},
        {"fa": "زرد", "reading": "zərd", "az": "Sarı"},
        {"fa": "نارنجی", "reading": "narenci", "az": "Narıncı"},
        {"fa": "کِرِم", "reading": "kerem", "az": "Krem rəngi"},
        {"fa": "آبی", "reading": "abi", "az": "Mavi"},
        {"fa": "بنفش", "reading": "bənəfş", "az": "Bənövşəyi"},
        {"fa": "قهوه‌ای", "reading": "qəhvei", "az": "Qəhvəyi"},
        {"fa": "مشکی (سیاه)", "reading": "meşki (siyah)", "az": "Qara"},
        {"fa": "سرمه‌ای (سورمه‌ای)", "reading": "sormei", "az": "Tünd göy"},
        {"fa": "طوسی (خاکستری)", "reading": "tusi (xakestəri)", "az": "Boz"},
        {"fa": "سفید", "reading": "sefid", "az": "Ağ"},
        {"fa": "نقره‌ای", "reading": "noqrei", "az": "Gümüşü"},
        {"fa": "پررنگ", "reading": "porrəng", "az": "Tünd (rəng)"},
        {"fa": "کم‌رنگ", "reading": "kəmrəng", "az": "Açıq (rəng)"},
        {"fa": "سیاه و سفید", "reading": "siyah o sefid", "az": "Ağ-qara"},
        {"fa": "رنگی", "reading": "rəngi", "az": "Rəngli"},
        {"fa": "رنگین‌کمان", "reading": "rənginkəman", "az": "Göy qurşağı"},
        {"fa": "آبرنگ", "reading": "abrəng", "az": "Akvarel"},
        {"fa": "قلم‌مو", "reading": "qələmmu", "az": "Fırça"},
        {"fa": "اسپریِ رنگ", "reading": "esperiye rəng", "az": "Rəng spreyi"},
        {"fa": "چهارپایه", "reading": "çəharpaye", "az": "Kətil (taburet)"},
        {"fa": "رنگ‌فروش", "reading": "rəngforuş", "az": "Rəng satan"},
        {"fa": "رنگ‌کار (نقّاش)", "reading": "rəngkar (nəqqaş)", "az": "Rəngsaz"},
        {"fa": "کمد", "reading": "komod", "az": "Şkaf"},
        {"fa": "داخل", "reading": "daxel", "az": "İçəri, iç"},
        {"fa": "زیبا", "reading": "ziba", "az": "Gözəl"},
        {"fa": "خوش‌مزه", "reading": "xoşməze", "az": "Dadlı"},
        {"fa": "رنگ می‌زند", "reading": "rəng mizənəd", "az": "rəngləyir"},
        {"fa": "می‌خواهد", "reading": "mixahəd", "az": "istəyir"},
        {"fa": "استفاده می‌کند", "reading": "estefade mikonəd", "az": "istifadə edir"},
        {"fa": "مردم", "reading": "mərdom", "az": "Camaat, insanlar"},
        {"fa": "دامدار", "reading": "damdar", "az": "Heyvandar (maldar)"},
        {"fa": "مزرعه", "reading": "məzrəe", "az": "Tarla, əkin sahəsi"},
        {"fa": "نزدیک", "reading": "nəzdik", "az": "Yaxın"},
        {"fa": "رنگارنگ", "reading": "rəngarəng", "az": "Rəngbərəng"},
        {"fa": "علاوه بر", "reading": "əlave bər", "az": "…-dan əlavə"},
    ],
    "grammar_notes": [
        {
            "title_az": "Sual sözü «چه رنگ» (nə rəngdədir?)",
            "title_fa": "واژه‌ی پرسشی «چه رنگ»",
            # Hər sətir tətbiqdə ayrıca bənd (•) kimi görünür; izah aşağıdakı
            # «Qaydalar / Birləşmələr» cədvəlindəki iki nümunə üzərində qurulub.
            "explanation_az": (
                "Rəngi soruşmaq üçün «چه رنگ است؟» işlədilir — «nə rəngdədir?».\n"
                "Sualın quruluşu: İŞARƏ SÖZÜ + İSİM + چه رنگ + است؟ — məsələn: این رایانه چه رنگ است؟\n"
                "Sual sözü ismin ARDINCA gəlir, əvvəlinə keçmir.\n"
                "Cavab eyni quruluşla verilir: «چه رنگ»-in yerinə rəngin adı qoyulur — این رایانه، مشکی است.\n"
                "İkinci nümunə də eyni qəlibdədir: آن پیراهن چه رنگ است؟ ← آن پیراهن، صورتی است.\n"
                "Cavabda isim təkrarlanır, vergüldən sonra rəngin adı və «است» gəlir.\n"
                "«چه رنگی» forması da işlənir, xüsusən «دوست داری» kimi fellərlə: کفش چه رنگی دوست داری؟"
            ),
            # Dərslikdəki lövhə: sual — cavab cütlükləri.
            "conjugations": [
                {
                    "pronoun_fa": "این رایانه چه رنگ است؟",
                    "form_fa": "این رایانه، مشکی است.",
                    "reading_az": "İn rayane çe rəng əst? — İn rayane, meşki əst.",
                    "az": "Bu kompüter nə rəngdədir? — Bu kompüter qaradır.",
                },
                {
                    "pronoun_fa": "آن پیراهن چه رنگ است؟",
                    "form_fa": "آن پیراهن، صورتی است.",
                    "reading_az": "An pirahən çe rəng əst? — An pirahən, surəti əst.",
                    "az": "O köynək nə rəngdədir? — O köynək çəhrayıdır.",
                },
            ],
            # Dərslikdəki «لطفاً بخوانید» siyahısı ilə eyni ardıcıllıqda; iki
            # sətirdən ibarət olan bəndlər (۴ və ۵) ayrı-ayrı nümunələrə bölünüb.
            "examples": [
                {"fa": "آن کبوتر چه رنگ است؟ آن کبوتر، سفید است.", "reading_az": "An kəbutər çe rəng əst? An kəbutər, sefid əst.", "az": "O göyərçin nə rəngdədir? O göyərçin ağdır."},
                {"fa": "سطل کلاس شما چه رنگ است؟ سطل کلاس ما قرمز است.", "reading_az": "Sətle kelase şoma çe rəng əst? Sətle kelase ma qermez əst.", "az": "Sizin sinfinizin vedrəsi nə rəngdədir? Bizim sinfimizin vedrəsi qırmızıdır."},
                {"fa": "کفش چه رنگی دوست داری؟ من کفش قهوه‌ای دوست دارم.", "reading_az": "Kəfş çe rəngi dust dari? Mən kəfşe qəhvei dust daram.", "az": "Nə rəngdə ayaqqabı xoşlayırsan? Mən qəhvəyi ayaqqabı xoşlayıram."},
                {"fa": "آیا علی ماشینش را می‌فروشد؟ بله، او ماشینش را می‌فروشد.", "reading_az": "Aya Əli maşineş ra miforuşəd? Bəle, u maşineş ra miforuşəd.", "az": "Əli maşınını satırmı? Bəli, o maşınını satır."},
                {"fa": "ماشین علی چه رنگی است؟ ماشین او نقره‌ای است.", "reading_az": "Maşine Əli çe rəngi əst? Maşine u noqrei əst.", "az": "Əlinin maşını nə rəngdədir? Onun maşını gümüşüdür."},
                {"fa": "این پرچم کدام کشور است؟ این پرچم ایران است.", "reading_az": "İn pərçəm kodam keşvər əst? İn pərçəme Iran əst.", "az": "Bu, hansı ölkənin bayrağıdır? Bu, İranın bayrağıdır."},
                {"fa": "پرچم ایران چه رنگ است؟ پرچم ایران، سبز و سفید و قرمز است.", "reading_az": "Pərçəme Iran çe rəng əst? Pərçəme Iran, səbz o sefid o qermez əst.", "az": "İranın bayrağı nə rəngdədir? İran bayrağı yaşıl, ağ və qırmızıdır."},
            ],
            # Dərslikdəki «بگوییم / نگوییم» qutusu.
            "note_fa": (
                "بگوییم:\n"
                "✅ پیراهن او چه رنگ است؟\n"
                "✅ پیراهن او سفید است.\n"
                "نگوییم:\n"
                "❌ او پیراهن چه رنگ است؟\n"
                "❌ او پیراهن سفید است."
            ),
            "note_reading_az": (
                "Beguyim:\n"
                "Pirahəne u çe rəng əst?\n"
                "Pirahəne u sefid əst.\n"
                "Neguyim:\n"
                "U pirahən çe rəng əst?\n"
                "U pirahən sefid əst."
            ),
            "note_az": (
                "Deyək / deməyək:\n"
                "✅ Sahibi bildirən söz (او) izafətlə isimdən SONRA gəlir: پیراهنِ او — «onun köynəyi».\n"
                "❌ Onu cümlənin əvvəlinə çıxarmaq olmaz: «او پیراهن ...» səhvdir.\n"
                "Bu qayda həm sual, həm də nəqli cümlədə eynidir."
            ),
            # QEYD: dərslikdəki «مانند مثال بپرسید و پاسخ دهید» tapşırığı burada
            # drill kimi deyil, aşağıda ÇALIŞMA 5 (picture_sentences, Dərs 4-ün
            # Çalışma 7 quruluşu) kimi verilib — dərslikdəki 7 şəkillə birlikdə.
        },
        {
            "title_az": "İzafət əlaməti (1): «پیراهنِ من» — kəsrə ( ـِ ) ilə bağlama",
            "title_fa": "نشانه‌ی اضافه (۱)",
            # Hər sətir tətbiqdə ayrıca bənd (•) kimi göstərilir — ona görə
            # qısa, bir fikirli sətirlər yazılır (bax _RuleExplanationBox).
            "explanation_az": (
                "İzafət (نشانه‌ی اضافه) iki sözü bir-birinə bağlayan qısa «e» səsidir.\n"
                "Quruluş: ƏSAS SÖZ + ـِ + İKİNCİ SÖZ. Məsələn: پیراهن + ـِ + من = پیراهنِ من.\n"
                "Fars dilində əsas söz həmişə birinci gəlir; Azərbaycancaya tərcümədə söz sırası tərsinə çevrilir: پیراهنِ من = mənim köynəyim.\n"
                "1) Sahiblik bildirir: پیراهنِ من (mənim köynəyim), ماشینِ استادمان (müəllimimizin maşını).\n"
                "2) Əlamət — rəng, növ — bildirir: پیراهنِ آبی (mavi köynək), ساعتِ نقره‌ای (gümüşü saat).\n"
                "Kəsrə ( ـِ ) yazıda göstərilmir, yalnız oxunuşda eşidilir: «پیراهن من» → pirahən-e mən.\n"
                "İkinci söz dəyişsə də, əsas söz olduğu kimi qalır: پیراهنِ من ← پیراهن → پیراهنِ آبی."
            ),
            # Dərslikdəki lövhə: mərkəzdə kəsrə, sağda əsas söz (پیراهن),
            # solda ona bağlanan sözlər (من / آبی).
            "conjugations": [
                {"pronoun_fa": "پیراهن + ـِ + من", "form_fa": "پیراهنِ من"},
                {"pronoun_fa": "پیراهن + ـِ + آبی", "form_fa": "پیراهنِ آبی"},
            ],
            # Dərslikdəki «لطفاً بخوانید» siyahısının 9 bəndi, eyni ardıcıllıqla.
            "examples": [
                {"fa": "فاطمه، ساعتِ نقره‌ای دارد.", "reading_az": "Fateme, saəte noqrei darəd.", "az": "Fatimənin gümüşü saatı var."},
                {"fa": "ماشینِ استادمان، سفید است.", "reading_az": "Maşine ostademan, sefid əst.", "az": "Müəllimimizin maşını ağdır."},
                {"fa": "مادرم، ظرفِ غذا را در ظرف‌شویی می‌گذارد.", "reading_az": "Madərəm, zərfe qəza ra dər zərfşuyi migozarəd.", "az": "Anam yemək qabını qabyuyana qoyur."},
                {"fa": "همسرِ یوسف در دانش‌گاهِ قم درس می‌خواند.", "reading_az": "Həmsəre Yusef dər daneşgahe Qom dərs mixanəd.", "az": "Yusifin həyat yoldaşı Qum universitetində oxuyur."},
                {"fa": "پدرم از فروش‌گاه برای من یک تشک صورتی و یک بالش آبی می‌خرد.", "reading_az": "Pedərəm əz foruşgah bəraye mən yek toşəke surəti va yek baleşe abi mixərəd.", "az": "Atam mağazadan mənə bir çəhrayı döşək və bir mavi yastıq alır."},
                {"fa": "استادِ ما برای نوشتن روی تابلو از ماژیکِ آبی و مشکی استفاده می‌کند.", "reading_az": "Ostade ma bəraye neveştən ruye təblo əz majike abi va meşki estefade mikonəd.", "az": "Müəllimimiz lövhədə yazmaq üçün mavi və qara markerdən istifadə edir."},
                {"fa": "فرزندت چه رنگی را دوست دارد؟ او رنگِ کرم و قهوه‌ای را دوست دارد.", "reading_az": "Fərzendət çe rəngi ra dust darəd? U rənge kerem va qəhvei ra dust darəd.", "az": "Övladın hansı rəngi xoşlayır? O, krem və qəhvəyi rəngi xoşlayır."},
                {"fa": "آن مردِ جوان چه‌کار می‌کند؟ او اتاقِ پذیرایی را رنگ می‌زند.", "reading_az": "An mərde cəvan çekar mikonəd? U otağe pəzirayi ra rəng mizənəd.", "az": "O cavan kişi nə edir? O, qonaq otağını rəngləyir."},
                {"fa": "شما چه می‌خواهید؟ من آبرنگ و کاغذِ رنگی می‌خواهم.", "reading_az": "Şoma çe mixahid? Mən abrəng va kağəze rəngi mixahəm.", "az": "Siz nə istəyirsiniz? Mən akvarel və rəngli kağız istəyirəm."},
            ],
            # Siyahının altındakı ulduzlu qeyd.
            "note_fa": "در ترکیب‌ها نشانه‌ی اضافه‌ی کسره ( ـِ ) نوشته نمی‌شود، امّا خوانده می‌شود.",
            "note_reading_az": "Dər tərkibha neşane-ye ezafe-ye kəsre neveşte nemişəvəd, əmma xande mişəvəd.",
            "note_az": (
                "Söz birləşmələrində izafət əlaməti — kəsrə ( ـِ ) — yazılmır, ancaq oxunur.\n"
                "Yazılışı: پیراهن من — oxunuşu: pirahən-e mən.\n"
                "Yəni hərfi görmədən də iki söz arasında qısa «e» səsini tələffüz etmək lazımdır."
            ),
        },
        {
            "title_az": "İzafət əlaməti (2): «ه» ilə bitən sözlərdə «ی» (خانه‌ی پدرم)",
            "title_fa": "نشانه‌ی اضافه (۲)",
            # Hər sətir tətbiqdə ayrıca bənd (•) kimi görünür.
            "explanation_az": (
                "Sözün sonundakı «ه / ـه» OXUNMURSA (bəyan-e hərəkət), izafət kəsrə ilə yox, «ی» ilə göstərilir.\n"
                "Quruluş: SÖZ + ی + İKİNCİ SÖZ. Məsələn: خانه + ی + پدرم = خانه‌ی پدرم؛ راننده + ی + تاکسی = راننده‌ی تاکسی.\n"
                "«ی»-dən əvvəl yarımboşluq (nim-fasilə) qoyulur və bu «ی» yazıda mütləq görünür.\n"
                "Sözün sonundakı «ه» OXUNURSA, adi kəsrə qalır: کلاه + ـِ + صورتی = کلاهِ صورتی؛ ته + ـِ + چاه = تهِ چاه.\n"
                "«ه»-si oxunan sözlər: کلاه، دانش‌گاه، فرودگاه، پادشاه، کوه، ته və s.\n"
                "Yoxlama üsulu: sözü tək oxu — sonda «h» səsi eşidilirsə kəsrə, eşidilmirsə «ی» işlədilir."
            ),
            # Dərslikdəki lövhə: yuxarı cütlük «ی» ilə, aşağı cütlük kəsrə ilə.
            "conjugations": [
                {"pronoun_fa": "خانه + ی + پدرم", "form_fa": "خانه‌ی پدرم"},
                {"pronoun_fa": "راننده + ی + تاکسی", "form_fa": "راننده‌ی تاکسی"},
                {"pronoun_fa": "کلاه + ـِ + صورتی", "form_fa": "کلاهِ صورتی"},
                {"pronoun_fa": "ته + ـِ + چاه", "form_fa": "تهِ چاه"},
            ],
            "examples": [
                {"fa": "خانه‌ی پدرم بزرگ است.", "reading_az": "Xane-ye pedərəm bozorg əst.", "az": "Atamın evi böyükdür."},
                {"fa": "پدرم، راننده‌ی تاکسی است.", "reading_az": "Pedərəm, ranənde-ye taksi əst.", "az": "Atam taksi sürücüsüdür."},
                {"fa": "مریم کلاهِ صورتی دارد.", "reading_az": "Məryəm kolahe surəti darəd.", "az": "Məryəmin çəhrayı papağı var."},
                {"fa": "در تهِ چاه آب وجود دارد.", "reading_az": "Dər tehe çah ab vocud darəd.", "az": "Quyunun dibində su var."},
                {"fa": "رایانه‌ی من در اتاق مطالعه است.", "reading_az": "Rayane-ye mən dər otağe motaleə əst.", "az": "Mənim kompüterim iş otağındadır."},
                {"fa": "من یک پرده‌ی زیبا برای اتاق پذیرایی می‌خرم.", "reading_az": "Mən yek pərde-ye ziba bəraye otağe pəziraei mixərəm.", "az": "Mən qonaq otağı üçün gözəl bir pərdə alıram."},
                {"fa": "در باغچه‌ی خانه‌ی ما دو درخت سیب و یک درخت پرتقال وجود دارد.", "reading_az": "Dər bağçe-ye xane-ye ma do dərəxte sib va yek dərəxte porteqal vocud darəd.", "az": "Bizim evin bağçasında iki alma ağacı və bir portağal ağacı var."},
            ],
            # Dərslikdəki iki ulduzlu qeyd — hərəsi Qeyd kartının öz qutusunda.
            "note_fa": (
                "نشانه‌ی اضافه در واژه‌هایی که آخرشان «ه ، ـه»ی بیان حرکت (ناخوانا) دارد، «ی» می‌باشد؛ "
                "امّا برخی از «ء» به عنوان نشانه‌ی اضافه استفاده می‌کنند، مانند: خانه‌ی پدرم (خانۀ پدرم)؛ "
                "راننده‌ی تاکسی (رانندۀ تاکسی)"
            ),
            "note_reading_az": (
                "Neşane-ye ezafe dər vajehayi ke axərəşan «he»-ye bəyane hərəkət (naxana) darəd, «ye» "
                "mibaşəd; əmma bərxi əz «həmze» be onvane neşane-ye ezafe estefade mikonənd, manənd: "
                "xane-ye pedərəm (xaneye pedərəm); ranənde-ye taksi (ranəndeye taksi)"
            ),
            "note_az": (
                "Sonu oxunmayan «ه» ilə bitən sözlərdə izafət əlaməti «ی»-dir: خانه‌ی پدرم، راننده‌ی تاکسی.\n"
                "Bəzi mətnlərdə eyni əlamət «ء» (həmzə) ilə yazılır: خانۀ پدرم = خانه‌ی پدرم؛ رانندۀ تاکسی = راننده‌ی تاکسی.\n"
                "Hər iki yazılış eyni oxunur, mənası dəyişmir."
            ),
            "note2_fa": (
                "در واژه‌هایی مانند «کلاه»، «دانش‌گاه»، «فرودگاه»، «پادشاه»، «کوه»، «ته» و ... «ه ، ـه» "
                "بیان حرکت نیست و خوانده می‌شود. در واژه‌هایی که «ه ، ـه» خوانده می‌شود، نشانه‌ی اضافه "
                "کسره ( ـِ ) می‌باشد، مانند: کلاهِ من؛ دانش‌گاهِ قم؛ تهِ چاه"
            ),
            "note2_reading_az": (
                "Dər vajehayi manənd «kolah», «daneşgah», «forudgah», «padeşah», «kuh», «te» va ... «he» "
                "bəyane hərəkət nist va xande mişəvəd. Dər vajehayi ke «he» xande mişəvəd, neşane-ye "
                "ezafe kəsre mibaşəd, manənd: kolahe mən; daneşgahe Qom; tehe çah"
            ),
            "note2_az": (
                "«کلاه» (papaq), «دانش‌گاه» (universitet), «فرودگاه» (hava limanı), «پادشاه» (padşah), "
                "«کوه» (dağ), «ته» (dib) kimi sözlərdə «ه» oxunur — o, bəyan-e hərəkət deyil.\n"
                "Belə sözlərdə izafət əlaməti kəsrədir ( ـِ ): کلاهِ من, دانش‌گاهِ قم, تهِ چاه.\n"
                "Yəni «ی» yalnız «ه»-si OXUNMAYAN sözlərə əlavə olunur."
            ),
        },
        {
            "title_az": "İzafət əlaməti (3): «ی/ا/و» ilə bitən sözlərdə «ی» (موی بلند)",
            "title_fa": "نشانه‌ی اضافه (۳)",
            # Hər sətir tətbiqdə ayrıca bənd (•) kimi görünür; izah aşağıdakı
            # dörd birləşmə üzərində qurulub.
            "explanation_az": (
                "Söz «ا» və ya «و» saiti ilə bitirsə, izafət «ی» hərfi ilə YAZILIR və oxunur.\n"
                "Quruluş: SÖZ + ی + İKİNCİ SÖZ. Məsələn: مو + ی + بلند = موی بلند («uzun saç»).\n"
                "Eyni qayda «ا» üçün: عصا + ی + پدربزرگ = عصای پدربزرگ («babamın əsası»). «ی» sözə bitişik yazılır.\n"
                "Söz onsuz da «ی» ilə bitib «i» səsi verirsə, izafətin «ی»-si YAZILMIR, ancaq OXUNUR: صندلی کوچک → «səndəli-ye kuçek».\n"
                "Belə sözlərdə yazıda heç bir əlamət görünmür: بخاری اتاق yazılır, «boxari-ye otaq» oxunur.\n"
                "Yekun: izafət həmişə eşidilir, yalnız yazılışı sözün son hərfindən asılıdır — samitdən sonra kəsrə, «ا/و»-dan sonra «ی», «ی»-dən sonra isə heç nə."
            ),
            # Dərslikdəki lövhə: yuxarı cütlük «ی» yazılan hal, aşağı cütlük
            # «(ی)» — yazılmayıb yalnız oxunan hal.
            "conjugations": [
                {
                    "pronoun_fa": "مو + ی + بلند",
                    "form_fa": "موی بلند",
                    "reading_az": "muye bolənd",
                    "az": "uzun saç",
                },
                {
                    "pronoun_fa": "عصا + ی + پدربزرگ",
                    "form_fa": "عصای پدربزرگ",
                    "reading_az": "əsaye pedərbozorg",
                    "az": "babanın əsası",
                },
                {
                    "pronoun_fa": "صندلی + (ی) + کوچک",
                    "form_fa": "صندلی کوچک",
                    "reading_az": "səndəli-ye kuçek",
                    "az": "kiçik stul — «ی» yazılmır, oxunur",
                },
                {
                    "pronoun_fa": "بخاری + (ی) + اتاق",
                    "form_fa": "بخاری اتاق",
                    "reading_az": "boxari-ye otaq",
                    "az": "otağın sobası — «ی» yazılmır, oxunur",
                },
            ],
            # Yalnız dərslikdəki «لطفاً بخوانید» tapşırığının 7 cümləsi.
            "examples": [
                {"fa": "اسم عموی من، حسین و اسم عمّه‌ام فاطمه است.", "reading_az": "Esme əmuye mən, Hoseyn va esme əmməam Fateme əst.", "az": "Əmimin adı Hüseyn, bibimin adı Fatimədir."},
                {"fa": "پزشک، پای دوستم را معاینه می‌کند.", "reading_az": "Pezeşk, paye dustəm ra moayene mikonəd.", "az": "Həkim dostumun ayağını müayinə edir."},
                {"fa": "ما کتاب فارسی دوم را می‌خوانیم.", "reading_az": "Ma ketabe farsiye dovvom ra mixanim.", "az": "Biz ikinci fars dili kitabını oxuyuruq."},
                {"fa": "مادرم غذاهای لذیذ و خوش‌مزه می‌پزد.", "reading_az": "Madərəm qəzahaye ləziz va xoşməze mipəzəd.", "az": "Anam ləzzətli və dadlı yeməklər bişirir."},
                {"fa": "جواد یک زیردستی کوچک و دو مقوّای رنگی می‌خواهد.", "reading_az": "Cavad yek zirdəstiye kuçek va do moqəvvaye rəngi mixahəd.", "az": "Cavad kiçik bir altlıq və iki rəngli mopqa (karton) istəyir."},
                {"fa": "شما روی تابلوی کلاس چه می‌نویسید؟ من روی تابلو، املا می‌نویسم.", "reading_az": "Şoma ruye tabluye kelas çe minevisid? Mən ruye tablo, emla minevisəm.", "az": "Siz sinfin lövhəsinə nə yazırsınız? Mən lövhəyə imla yazıram."},
                {"fa": "جواد، دانش‌جوی دانش‌گاه تهران است و خواهرش ریحانه، طلبه‌ی جامعة المصطفی است.", "reading_az": "Cavad, daneşcuye daneşgahe Tehran əst va xahərəş Reyhane, təlbeye Cameətol-Mostəfa əst.", "az": "Cavad Tehran Universitetinin tələbəsidir, bacısı Reyhanə isə Came'ətül-Mustafanın dini tələbəsidir."},
            ],
            # Səhifənin altındakı ulduzlu qeyd və «می‌نویسیم / می‌خوانیم» qutusu.
            "note_fa": (
                "در ترکیب واژه‌هایی که آخرشان «ی» می‌باشد و صدای «ای» دارند، "
                "نشانه‌ی اضافه «ی» را نمی‌نویسیم، امّا می‌خوانیم."
            ),
            "note_reading_az": (
                "Dər tərkibe vajehayi ke axərəşan «ye» mibaşəd va sədaye «i» darənd, "
                "neşane-ye ezafe «ye» ra neminevisim, əmma mixanim."
            ),
            "note_az": (
                "Sonu «ی» ilə bitən və «i» səsi verən sözlərin birləşməsində izafətin «ی»-si yazılmır, ancaq oxunur.\n"
                "Yəni yazıda əlamət görünmür, tələffüzdə isə mütləq eşidilir."
            ),
            "note2_fa": (
                "می‌نویسیم: صندلی کوچک؛ آبی کم‌رنگ\n"
                "می‌خوانیم: صندلی(ی) کوچک؛ آبی(ی) کم‌رنگ"
            ),
            "note2_reading_az": (
                "Minevisim: səndəli kuçek; abi kəmrəng\n"
                "Mixanim: səndəli-ye kuçek; abi-ye kəmrəng"
            ),
            "note2_az": (
                "Yazırıq: صندلی کوچک، آبی کم‌رنگ — heç bir əlamət yazılmır.\n"
                "Oxuyuruq: səndəli-ye kuçek, abi-ye kəmrəng — iki sözün arasında «ye» səsi eşidilir."
            ),
            # QEYD: bu mövzunun dərslikdəki iki tapşırığı — «با نشانه‌ی اضافه
            # بخوانید» və «مانند مثال جایگزین کنید» — burada drill kimi deyil,
            # aşağıda ÇALIŞMA 3 (multi_blank, Dərs 4-ün Çalışma 1 quruluşu) və
            # ÇALIŞMA 4 (answer_question, Dərs 5-in Çalışma 2 quruluşu) kimi verilib.
        },
    ],
    "exercises": [
        {
            # Çalışma 1 — dərslikdəki «لطفاً جایگزین کنید» (استفاده کردن + از).
            # Əvvəllər sadə practice_reveal idi (Çalışma 2); Dərs 3-ün Çalışma 3
            # quruluşuna (answer_question + çoxrəngli NÜMUNƏ qutusu) keçirilib,
            # bəndlər dərslikdəki sıra ilə düzülüb.
            "kind": "answer_question",
            "title_fa": "لطفاً جایگزین کنید",
            "instruction_az": "Nümunə kimi əvəz edin",
            # Qırmızı — inkar hissə (işlətmədiyi əşya), yaşıl — müsbət hissə.
            "example_fa": (
                "فرزندم / مدادرنگی / آبرنگ\n"
                "فرزندم **از** مدادرنگی **استفاده نمی‌کند**؛ او *از* آبرنگ *استفاده می‌کند*."
            ),
            "example_reading_az": (
                "Fərzendəm / medadrəngi / abrəng\n"
                "Fərzendəm əz medadrəngi estefade nemikonəd; u əz abrəng estefade mikonəd."
            ),
            "example_az": (
                "Verilən sözlər: SUBYEKT / İŞLƏTMƏDİYİ ƏŞYA / İŞLƏTDİYİ ƏŞYA.\n"
                "Quruluş: SUBYEKT + از + 1-ci əşya + استفاده نمی‌کند؛ او + از + 2-ci əşya + استفاده می‌کند.\n"
                "Qırmızı — inkar hissə (birinci əşya), yaşıl — müsbət hissə (ikinci əşya).\n"
                "«استفاده کردن» feli həmişə «از» ön qoşması ilə işlənir.\n"
                "Tərcümə: Övladım rəngli karandaşdan istifadə etmir; o, akvareldən istifadə edir."
            ),
            "items": [
                {
                    "fa": "پدرم / خودکار سبز / خودکار آبی",
                    "reading_az": "Pedərəm / xodkare səbz / xodkare abi",
                    "az": "atam / yaşıl tükənməz qələm / mavi tükənməz qələm",
                    "sample_answer_fa": "پدرم از خودکار سبز استفاده نمی‌کند؛ او از خودکار آبی استفاده می‌کند.",
                    "sample_answer_reading_az": "Pedərəm əz xodkare səbz estefade nemikonəd; u əz xodkare abi estefade mikonəd.",
                    "sample_answer_az": "Atam yaşıl tükənməz qələmdən istifadə etmir; o, mavi tükənməz qələmdən istifadə edir.",
                },
                {
                    "fa": "استادمان / ماژیک قرمز / ماژیک مشکی",
                    "reading_az": "Ostademan / majike qermez / majike meşki",
                    "az": "müəllimimiz / qırmızı marker / qara marker",
                    "sample_answer_fa": "استادمان از ماژیک قرمز استفاده نمی‌کند؛ او از ماژیک مشکی استفاده می‌کند.",
                    "sample_answer_reading_az": "Ostademan əz majike qermez estefade nemikonəd; u əz majike meşki estefade mikonəd.",
                    "sample_answer_az": "Müəllimimiz qırmızı markerdən istifadə etmir; o, qara markerdən istifadə edir.",
                },
                {
                    "fa": "محمّدرضا / پاک‌کن / غلط‌گیر",
                    "reading_az": "Mohəmmədreza / pakkon / qələtgir",
                    "az": "Məhəmmədrza / pozan / korrektor",
                    "sample_answer_fa": "محمّدرضا از پاک‌کن استفاده نمی‌کند؛ او از غلط‌گیر استفاده می‌کند.",
                    "sample_answer_reading_az": "Mohəmmədreza əz pakkon estefade nemikonəd; u əz qələtgir estefade mikonəd.",
                    "sample_answer_az": "Məhəmmədrza pozandan istifadə etmir; o, korrektordan istifadə edir.",
                },
                {
                    "fa": "نرگس / جارودستی / جاروبرقی",
                    "reading_az": "Nərges / caruye dəsti / caruye bərqi",
                    "az": "Nərgiz / əl süpürgəsi / tozsoran",
                    "sample_answer_fa": "نرگس از جارودستی استفاده نمی‌کند؛ او از جاروبرقی استفاده می‌کند.",
                    "sample_answer_reading_az": "Nərges əz caruye dəsti estefade nemikonəd; u əz caruye bərqi estefade mikonəd.",
                    "sample_answer_az": "Nərgiz əl süpürgəsindən istifadə etmir; o, tozsorandan istifadə edir.",
                },
                {
                    "fa": "بنّا / نردبان / چهارپایه",
                    "reading_az": "Bənna / nərdeban / çəharpaye",
                    "az": "bənna / nərdivan / kətil",
                    "sample_answer_fa": "بنّا از نردبان استفاده نمی‌کند؛ او از چهارپایه استفاده می‌کند.",
                    "sample_answer_reading_az": "Bənna əz nərdeban estefade nemikonəd; u əz çəharpaye estefade mikonəd.",
                    "sample_answer_az": "Bənna nərdivandan istifadə etmir; o, kətildən istifadə edir.",
                },
                {
                    "fa": "نجّار / آهن / چوب",
                    "reading_az": "Nəccar / ahən / çub",
                    "az": "dülgər / dəmir / taxta",
                    "sample_answer_fa": "نجّار از آهن استفاده نمی‌کند؛ او از چوب استفاده می‌کند.",
                    "sample_answer_reading_az": "Nəccar əz ahən estefade nemikonəd; u əz çub estefade mikonəd.",
                    "sample_answer_az": "Dülgər dəmirdən istifadə etmir; o, taxtadan istifadə edir.",
                },
            ],
        },
        {
            "kind": "fill_blank",
            "instruction_az": "Boşluğu uyğun sözlə doldurun (rəng və «می‌خواهد / استفاده می‌کند» felləri).",
            "word_bank": ["مشکی", "صورتی", "نارنجی", "می‌خواهد", "استفاده می‌کند", "رنگ می‌زند"],
            "items": [
                {
                    "fa_with_blank": "من برای دخترکوچکم، جوراب ___ می‌خرم.",
                    "correct_answer": "صورتی",
                    "reading_az": "surəti",
                    "az": "çəhrayı",
                    "full_reading_az": "Mən bəraye doxtəre kuçekəm, curabe surəti mixərəm.",
                    "full_translation_az": "Mən balaca qızım üçün çəhrayı corab alıram.",
                },
                {
                    "fa_with_blank": "دوستم رضا خودکار ___ دارد؛ او خودکار آبی و قرمز می‌خواهد.",
                    "correct_answer": "مشکی",
                    "reading_az": "meşki",
                    "az": "qara",
                    "full_reading_az": "Dustəm Reza xodkare meşki darəd; u xodkare abi va qermez mixahəd.",
                    "full_translation_az": "Dostum Rza qara tükənməz qələmə malikdir; o, mavi və qırmızı tükənməz qələm istəyir.",
                },
                {
                    "fa_with_blank": "آن مرد، رنگ‌فروش نیست؛ او رنگ‌کار است. او الآن خانه‌ی ما را ___ .",
                    "correct_answer": "رنگ می‌زند",
                    "reading_az": "rəng mizənəd",
                    "az": "rəngləyir",
                    "full_reading_az": "An mərd, rəngforuş nist; u rəngkar əst. U əl-an xane-ye ma ra rəng mizənəd.",
                    "full_translation_az": "O kişi rəng satan deyil; o, rəngsazdır. O, indi bizim evimizi rəngləyir.",
                },
                {
                    "fa_with_blank": "شما کدام جامدادی را می‌خواهید؟ من جامدادی ___ را می‌خواهم.",
                    "correct_answer": "نارنجی",
                    "reading_az": "narenci",
                    "az": "narıncı",
                    "full_reading_az": "Şoma kodam camedadi ra mixahid? Mən camedadiye narenci ra mixahəm.",
                    "full_translation_az": "Siz hansı qələmqabını istəyirsiniz? Mən narıncı qələmqabını istəyirəm.",
                },
                {
                    "fa_with_blank": "ایشان برای نوشتن از ماژیک قرمز ___ یا آبی؟ او از ماژیک آبی استفاده می‌کند.",
                    "correct_answer": "استفاده می‌کند",
                    "reading_az": "estefade mikonəd",
                    "az": "istifadə edir",
                    "full_reading_az": "İşan bəraye neveştən əz majike qermez estefade mikonəd ya abi? U əz majike abi estefade mikonəd.",
                    "full_translation_az": "O, yazmaq üçün qırmızı markerdən istifadə edir, yoxsa mavi? O, mavi markerdən istifadə edir.",
                },
            ],
        },
        {
            # Çalışma 3 — dərslikdəki «با نشانه‌ی اضافه بخوانید». Hər cümlədə
            # bir neçə izafət yeri var, ona görə Dərs 4-ün Çalışma 1 quruluşu
            # (multi_blank: söz bankı + çoxboşluqlu sürüklə-burax) götürülüb.
            "kind": "multi_blank",
            "title_fa": "با نشانه‌ی اضافه بخوانید",
            "instruction_az": "İzafət əlamətini yerinə qoyun: samitdən sonra kəsrə (ـِ), «ه/ا/و»-dan sonra «ی»",
            "example_fa": "خانه ___ پدربزرگ ___ من بزرگ است.\n**خانه‌ی** *پدربزرگِ* من بزرگ است.",
            "example_reading_az": "Xane-ye pedərbozorge mən bozorg əst.",
            "example_az": (
                "Babamın evi böyükdür.\n"
                "Qırmızı — «ه» ilə bitən sözdə izafət «ی» hərfi ilə yazılır (خانه‌ی).\n"
                "Yaşıl — samitlə bitən sözdə izafət kəsrə (ـِ) ilə göstərilir (پدربزرگِ).\n"
                "Söz «ا» və ya «و» ilə bitirsə də «ی» yazılır: روستای ما، ترازوی مدرسه.\n"
                "Söz «ی» ilə bitib «i» səsi verirsə, yeni «ی» yazılmır — kəsrə qoyulur, «-ye» oxunur: جامدادیِ صورتی."
            ),
            # 10 boşluq = 10 çip: 7 dəfə «ی», 3 dəfə kəsrə. Eyni əlamət bir neçə
            # dəfə lazım olduğu üçün sadəcə təkrarlanır (Dərs 4-dəki kimi).
            "word_bank": [
                "ی", "ی", "ی", "ی", "ی", "ی", "ی",
                "ـِ", "ـِ", "ـِ",
            ],
            "items": [
                {
                    "fa_with_blanks": "پرده ___ خانه ___ ما قهوه‌ای ___ کم‌رنگ است.",
                    "correct_answers": ["ی", "ی", "ـِ"],
                    "full_reading_az": "Pərde-ye xane-ye ma qəhveiye kəmrəng əst.",
                    "full_translation_az": "Bizim evimizin pərdəsi açıq qəhvəyidir.",
                },
                {
                    "fa_with_blanks": "دکتر، چشم‌ها ___ نوه ___ او را معاینه می‌کند.",
                    "correct_answers": ["ی", "ی"],
                    "full_reading_az": "Doktor, çeşmhaye nəve-ye u ra moayene mikonəd.",
                    "full_translation_az": "Həkim onun nəvəsinin gözlərini müayinə edir.",
                },
                {
                    "fa_with_blanks": "در روستا ___ ما یک مدرسه ___ بزرگ هست.",
                    "correct_answers": ["ی", "ی"],
                    "full_reading_az": "Dər rustaye ma yek mədrese-ye bozorg həst.",
                    "full_translation_az": "Bizim kəndimizdə bir böyük məktəb var.",
                },
                {
                    "fa_with_blanks": "ترازو ___ فروشگاه ___ مدرسه، نقره‌ای است.",
                    "correct_answers": ["ی", "ـِ"],
                    "full_reading_az": "Tarazuye foruşgahe mədrese, noqrei əst.",
                    "full_translation_az": "Məktəb mağazasının tərəzisi gümüşüdür.",
                },
                {
                    "fa_with_blanks": "من برای دخترم، یک کیف بنفش و یک جامدادی ___ صورتی می‌خرم.",
                    "correct_answers": ["ـِ"],
                    "full_reading_az": "Mən bəraye doxtərəm, yek kife bənəfş va yek camedadiye surəti mixərəm.",
                    "full_translation_az": "Mən qızım üçün bənövşəyi çanta və çəhrayı qələmqabı alıram.",
                },
            ],
        },
        {
            # Çalışma 4 — dərslikdəki «مانند مثال جایگزین کنید» (izafət zənciri
            # ilə əvəzləmə). Dərs 5-in Çalışma 2 quruluşu: answer_question +
            # çoxrəngli NÜMUNƏ qutusu; mötərizədəki sözlər cümlədəki uyğun
            # birləşmənin yerinə qoyulur.
            "kind": "answer_question",
            "title_fa": "مانند مثال جایگزین کنید",
            "instruction_az": "Nümunə kimi əvəz edin",
            # Qırmızı — mötərizədəki BİRİNCİ söz, yaşıl — İKİNCİ söz;
            # hər ikisi izafət əlaməti ilə bağlanır.
            "example_fa": (
                "من دیوارهای اتاق دوستم را رنگ می‌زنم. (پنجره ـ خانه)\n"
                "من **پنجره‌ی** *خانه‌ی* دوستم را رنگ می‌زنم."
            ),
            "example_reading_az": (
                "Mən divarhaye otağe dustəm ra rəng mizənəm. (Pəncəre - xane)\n"
                "Mən pəncəre-ye xane-ye dustəm ra rəng mizənəm."
            ),
            "example_az": (
                "Verilən: CÜMLƏ + mötərizədə iki söz (BİRİNCİ ـ İKİNCİ).\n"
                "Cümlədəki izafət birləşməsi (دیوارهای اتاق) mötərizədəki sözlərlə əvəz olunur: "
                "qırmızı — birinci söz, yaşıl — ikinci söz.\n"
                "Quruluş: SÖZ1 + izafət + SÖZ2 + izafət + cümlənin qalan hissəsi.\n"
                "İzafət əlaməti sonuncu hərfə görə seçilir: «ه»-dan sonra «ی» (پنجره‌ی، خانه‌ی), "
                "samitdən sonra kəsrə (باغِ), «ا/و»-dan sonra «ی» (زانوی).\n"
                "Cümlənin qalan hissəsi və fel dəyişmir.\n"
                "Tərcümə: Mən dostumun evinin pəncərəsini rəngləyirəm."
            ),
            "items": [
                {
                    "fa": "فرزندم آن جامدادی صورتی را می‌خواهد. (صندلی ـ سفید)",
                    "reading_az": "Fərzendəm an camedadiye surəti ra mixahəd. (Səndəli - sefid)",
                    "az": "Övladım o çəhrayı qələmqabını istəyir. (stul - ağ)",
                    "sample_answer_fa": "فرزندم آن صندلیِ سفید را می‌خواهد.",
                    "sample_answer_reading_az": "Fərzendəm an səndəliye sefid ra mixahəd.",
                    "sample_answer_az": "Övladım o ağ stulu istəyir.",
                },
                {
                    "fa": "اتاق مطالعه‌ی ما در طبقه‌ی دوم است. (آشپزخانه ـ اوّل)",
                    "reading_az": "Otağe motaleə-ye ma dər təbəqe-ye dovvom əst. (Aşpəzxane - əvvəl)",
                    "az": "Bizim mütaliə otağımız ikinci mərtəbədədir. (mətbəx - birinci)",
                    "sample_answer_fa": "آشپزخانه‌ی ما در طبقه‌ی اوّل است.",
                    "sample_answer_reading_az": "Aşpəzxane-ye ma dər təbəqe-ye əvvəl əst.",
                    "sample_answer_az": "Bizim mətbəximiz birinci mərtəbədədir.",
                },
                {
                    "fa": "من غذاهای مادرم را دوست دارم. (میوه‌ها ـ باغ پدربزرگم)",
                    "reading_az": "Mən qəzahaye madərəm ra dust daram. (Miveha - bağe pedərbozorgəm)",
                    "az": "Mən anamın yeməklərini xoşlayıram. (meyvələr - babamın bağı)",
                    "sample_answer_fa": "من میوه‌های باغ پدربزرگم را دوست دارم.",
                    "sample_answer_reading_az": "Mən mivehaye bağe pedərbozorgəm ra dust daram.",
                    "sample_answer_az": "Mən babamın bağının meyvələrini xoşlayıram.",
                },
                {
                    "fa": "ما در مدرسه‌ی شهید مطهّری درس می‌خوانیم. (دانش‌گاه ـ امام خمینی)",
                    "reading_az": "Ma dər mədrese-ye Şəhid Motəhhəri dərs mixanim. (Daneşgah - Emam Xomeyni)",
                    "az": "Biz Şəhid Mütəhhəri məktəbində oxuyuruq. (universitet - İmam Xomeyni)",
                    "sample_answer_fa": "ما در دانش‌گاه امام خمینی درس می‌خوانیم.",
                    "sample_answer_reading_az": "Ma dər daneşgahe Emam Xomeyni dərs mixanim.",
                    "sample_answer_az": "Biz İmam Xomeyni Universitetində oxuyuruq.",
                },
                {
                    "fa": "پزشک دندان و لثه‌ی بیمار را معاینه می‌کند. (دست و زانو)",
                    "reading_az": "Pezeşk dəndan va lese-ye bimar ra moayene mikonəd. (Dəst va zanu)",
                    "az": "Həkim xəstənin dişini və diş ətini müayinə edir. (əl və diz)",
                    "sample_answer_fa": "پزشک دست و زانوی بیمار را معاینه می‌کند.",
                    "sample_answer_reading_az": "Pezeşk dəst va zanuye bimar ra moayene mikonəd.",
                    "sample_answer_az": "Həkim xəstənin əl və dizini müayinə edir.",
                },
            ],
        },
        {
            # Çalışma 5 — dərslikdəki «مانند مثال بپرسید و پاسخ دهید» (چه رنگ؟).
            # Dərs 4-ün Çalışma 7 quruluşu: picture_sentences — nömrələnmiş
            # şəkillər, hər şəkil üçün iki cümlə (burada sual + cavab).
            # Nümunə qutusu dərslikdəki sarı çərçivədir (dovşan şəkli).
            # Şəkillər dərslikdən real foto olduğu üçün boş qalır — admin
            # panelindən yüklənir (Dərs 5-in Çalışma 7-si ilə eyni prinsip).
            "kind": "picture_sentences",
            "title_fa": "مانند مثال بپرسید و پاسخ دهید",
            "instruction_az": "Nümunə kimi soruşun və cavab verin",
            "example_fa": "این خرگوش چه رنگ است؟",
            "example_reading_az": "İn xərguş çe rəng əst?",
            "example_az": "Bu dovşan nə rəngdədir?",
            "example_answer_fa": "این خرگوش، سفید است.",
            "example_answer_reading_az": "İn xərguş, sefid əst.",
            "example_answer_az": "Bu dovşan ağdır.",
            "items": [
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این فلفل چه رنگ است؟", "reading_az": "İn felfel çe rəng əst?", "az": "Bu bibər nə rəngdədir?"},
                        {"fa": "این فلفل، قرمز است.", "reading_az": "İn felfel, qermez əst.", "az": "Bu bibər qırmızıdır."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این بستنی چه رنگ است؟", "reading_az": "İn bəstəni çe rəng əst?", "az": "Bu dondurma nə rəngdədir?"},
                        {"fa": "این بستنی، زرد و قهوه‌ای است.", "reading_az": "İn bəstəni, zərd o qəhvei əst.", "az": "Bu dondurma sarı və qəhvəyidir."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این کلاه چه رنگ است؟", "reading_az": "İn kolah çe rəng əst?", "az": "Bu papaq nə rəngdədir?"},
                        {"fa": "این کلاه، قهوه‌ای است.", "reading_az": "İn kolah, qəhvei əst.", "az": "Bu papaq qəhvəyidir."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این صندلی چه رنگ است؟", "reading_az": "İn səndəli çe rəng əst?", "az": "Bu stul nə rəngdədir?"},
                        {"fa": "این صندلی، مشکی است.", "reading_az": "İn səndəli, meşki əst.", "az": "Bu stul qaradır."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این چشم چه رنگ است؟", "reading_az": "İn çeşm çe rəng əst?", "az": "Bu göz nə rəngdədir?"},
                        {"fa": "این چشم، سبز است.", "reading_az": "İn çeşm, səbz əst.", "az": "Bu göz yaşıldır."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این شانه چه رنگ است؟", "reading_az": "İn şane çe rəng əst?", "az": "Bu daraq nə rəngdədir?"},
                        {"fa": "این شانه، زرد است.", "reading_az": "İn şane, zərd əst.", "az": "Bu daraq sarıdır."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این گل چه رنگ است؟", "reading_az": "İn gol çe rəng əst?", "az": "Bu gül nə rəngdədir?"},
                        {"fa": "این گل، صورتی است.", "reading_az": "İn gol, surəti əst.", "az": "Bu gül çəhrayıdır."},
                    ],
                },
            ],
        },
        {
            # Çalışma 6 — dərslikdəki «اسم رنگ‌های زیر را بگویید» (səh. 86-nın
            # yuxarısındakı 7 rəngli dairə). Dərs 4-ün Çalışma 7 quruluşu
            # (picture_sentences): hər dairə bir şəkil bəndidir, altında rəngin
            # adını deyən bir cümlə açılır. Dairələr sadə rəngli şəkil olduğu
            # üçün admin panelindən yüklənəcək; sıra dərslikdəki kimi SAĞDAN
            # SOLA-dır (açıq yaşıl → tünd göy → narıncı → boz → krem → bənövşəyi → sarı).
            "kind": "picture_sentences",
            "title_fa": "اسم رنگ‌های زیر را بگویید",
            "instruction_az": "Aşağıdakı rənglərin adını deyin",
            "items": [
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این رنگ، سبز کم‌رنگ است.", "reading_az": "İn rəng, səbze kəmrəng əst.", "az": "Bu rəng açıq yaşıldır."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این رنگ، سرمه‌ای است.", "reading_az": "İn rəng, sormei əst.", "az": "Bu rəng tünd göydür."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این رنگ، نارنجی است.", "reading_az": "İn rəng, narenci əst.", "az": "Bu rəng narıncıdır."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این رنگ، طوسی (خاکستری) است.", "reading_az": "İn rəng, tusi (xakestəri) əst.", "az": "Bu rəng bozdur."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این رنگ، کِرِم است.", "reading_az": "İn rəng, kerem əst.", "az": "Bu rəng krem rəngidir."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این رنگ، بنفش است.", "reading_az": "İn rəng, bənəfş əst.", "az": "Bu rəng bənövşəyidir."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این رنگ، زرد است.", "reading_az": "İn rəng, zərd əst.", "az": "Bu rəng sarıdır."},
                    ],
                },
            ],
        },
        {
            # Çalışma 7 — dərslikdəki «لطفاً جایگزین کنید»-in 1-ci hissəsi
            # («علاوه بر»). Əvvəllər sadə practice_reveal idi; Dərs 5-in
            # Çalışma 6 quruluşuna (answer_question + çoxrəngli NÜMUNƏ qutusu)
            # keçirilib.
            "kind": "answer_question",
            "title_fa": "لطفاً جایگزین کنید",
            "instruction_az": "Nümunə kimi əvəz edin («علاوه بر»)",
            # Qırmızı «علاوه بر» — birinci iş, yaşıl — ikinci (əsas) iş.
            "example_fa": (
                "دوستم / تمیز کردن اتاق / غذا پختن\n"
                "دوستم **علاوه بر** تمیز کردن اتاق *غذا می‌پزد*."
            ),
            "example_reading_az": (
                "Dustəm / təmiz kərdəne otaq / qəza poxtən\n"
                "Dustəm əlave bər təmiz kərdəne otaq qəza mipəzəd."
            ),
            "example_az": (
                "Verilən sözlər: SUBYEKT / BİRİNCİ İŞ / İKİNCİ İŞ.\n"
                "Quruluş: SUBYEKT + علاوه بر + BİRİNCİ İŞ (məsdər) + İKİNCİ İŞ (şəxsə görə hallanmış fel).\n"
                "Qırmızı «علاوه بر» birinci işin qarşısına qoyulur və o iş MƏSDƏR formasında qalır.\n"
                "Yaşıl hissə — ikinci iş; yalnız bu fel subyektə görə dəyişir (می‌پزد / می‌کنیم / می‌کشند).\n"
                "Tərcümə: Dostum otağı təmizləməkdən əlavə yemək bişirir."
            ),
            "items": [
                {
                    "fa": "ما / درس خواندن / کار کردن",
                    "reading_az": "Ma / dərs xandən / kar kərdən",
                    "az": "biz / dərs oxumaq / işləmək",
                    "sample_answer_fa": "ما علاوه بر درس خواندن، کار می‌کنیم.",
                    "sample_answer_reading_az": "Ma əlave bər dərs-xandən, kar mikonim.",
                    "sample_answer_az": "Biz dərs oxumaqdan əlavə işləyirik.",
                },
                {
                    "fa": "دانش‌آموزها / نوشتن تکلیف / نقّاشی کشیدن",
                    "reading_az": "Daneşamuzha / neveştəne təklif / nəqqaşi keşidən",
                    "az": "şagirdlər / tapşırıq yazmaq / rəsm çəkmək",
                    "sample_answer_fa": "دانش‌آموزها علاوه بر نوشتن تکلیف، نقّاشی می‌کشند.",
                    "sample_answer_reading_az": "Daneşamuzha əlave bər neveştəne təklif, nəqqaşi mikeşənd.",
                    "sample_answer_az": "Şagirdlər tapşırıq yazmaqdan əlavə rəsm çəkirlər.",
                },
                {
                    "fa": "خواهرم / لباس دوختن / مطالعه کردن",
                    "reading_az": "Xahərəm / lebas duxtən / motaleə kərdən",
                    "az": "bacım / paltar tikmək / mütaliə etmək",
                    "sample_answer_fa": "خواهرم علاوه بر لباس دوختن، مطالعه می‌کند.",
                    "sample_answer_reading_az": "Xahərəm əlave bər lebas-duxtən, motaleə mikonəd.",
                    "sample_answer_az": "Bacım paltar tikməkdən əlavə mütaliə edir.",
                },
                {
                    "fa": "نجّارها / ساختن در و پنجره / میز ساختن",
                    "reading_az": "Nəccarha / saxtəne dər va pəncəre / miz saxtən",
                    "az": "dülgərlər / qapı və pəncərə düzəltmək / masa düzəltmək",
                    "sample_answer_fa": "نجّارها علاوه بر ساختن در و پنجره، میز می‌سازند.",
                    "sample_answer_reading_az": "Nəccarha əlave bər saxtəne dər va pəncəre, miz misazənd.",
                    "sample_answer_az": "Dülgərlər qapı-pəncərə düzəltməkdən əlavə masa da düzəldirlər.",
                },
            ],
        },
        {
            # Çalışma 8 — «لطفاً جایگزین کنید»-in 2-ci hissəsi («بیشتر»).
            # Dərs 5-in Çalışma 6 quruluşu.
            "kind": "answer_question",
            "title_fa": "لطفاً جایگزین کنید",
            "instruction_az": "Nümunə kimi əvəz edin («بیشتر»)",
            # Qırmızı «بیشتر» — cümlənin əvvəlində, yaşıl «ها» — cəm şəkilçisi.
            "example_fa": (
                "طلبه / این کلاس / اهل آفریقا\n"
                "**بیشتر** *طلبه‌های* این کلاس اهل آفریقا هستند."
            ),
            "example_reading_az": (
                "Təlbe / in kelas / əhle Afriqa\n"
                "Biştəre təlbehaye in kelas əhle Afriqa həstənd."
            ),
            "example_az": (
                "Verilən sözlər: İSİM / YER (sahib) / ƏLAMƏT.\n"
                "Quruluş: بیشتر + İSİM + ها + izafət + YER + ƏLAMƏT + هستند.\n"
                "Qırmızı «بیشتر» (çoxu) cümlənin əvvəlində gəlir.\n"
                "Yaşıl «ها» — isim mütləq CƏM olur, sonra izafətlə sahibə bağlanır (طلبه‌های این کلاس).\n"
                "Cəm mübtəda ilə fel də cəm olur: هستند.\n"
                "Tərcümə: Bu sinfin dini tələbələrinin çoxu afrikalıdır."
            ),
            "items": [
                {
                    "fa": "دانش‌جو / آن کلاس / لاغر",
                    "reading_az": "Daneşcu / an kelas / lağər",
                    "az": "tələbə / o sinif / arıq",
                    "sample_answer_fa": "بیشتر دانش‌جوهای آن کلاس لاغر هستند.",
                    "sample_answer_reading_az": "Biştəre daneşcuhaye an kelas lağər həstənd.",
                    "sample_answer_az": "O sinifin tələbələrinin çoxu arıqdır.",
                },
                {
                    "fa": "پیراهن / من / رنگی",
                    "reading_az": "Pirahən / mən / rəngi",
                    "az": "köynək / mən / rəngli",
                    "sample_answer_fa": "بیشتر پیراهن‌های من رنگی هستند.",
                    "sample_answer_reading_az": "Biştəre pirahənhaye mən rəngi həstənd.",
                    "sample_answer_az": "Köynəklərimin çoxu rənglidir.",
                },
                {
                    "fa": "خانم / روستا / خانه‌دار",
                    "reading_az": "Xanom / rusta / xanedar",
                    "az": "xanım / kənd / evdar",
                    "sample_answer_fa": "بیشتر خانم‌های روستا خانه‌دار هستند.",
                    "sample_answer_reading_az": "Biştəre xanomhaye rusta xanedar həstənd.",
                    "sample_answer_az": "Kənd xanımlarının çoxu evdardır.",
                },
                {
                    "fa": "مردم / ایران / جوان",
                    "reading_az": "Mərdom / Iran / cavan",
                    "az": "camaat / İran / cavan",
                    "sample_answer_fa": "بیشتر مردم ایران جوان هستند.",
                    "sample_answer_reading_az": "Biştəre mərdome Iran cavan həstənd.",
                    "sample_answer_az": "İran əhalisinin çoxu cavandır.",
                },
            ],
        },
        {
            # Çalışma 9 — «لطفاً جایگزین کنید»-in 3-cü hissəsi (izafət + inkar/
            # təsdiq rəng cümləsi). Dərs 5-in Çalışma 6 quruluşu.
            "kind": "answer_question",
            "title_fa": "لطفاً جایگزین کنید",
            "instruction_az": "Nümunə kimi əvəz edin (izafət + «نیست؛ ... است»)",
            # Qırmızı — izafətlə bağlanmış mübtəda, yaşıl — düzgün əlamət.
            "example_fa": (
                "پرده / کلاس / سفید / آبی\n"
                "**پرده‌ی کلاس ما** سفید نیست؛ *آبی است*."
            ),
            "example_reading_az": (
                "Pərde / kelas / sefid / abi\n"
                "Pərde-ye kelase ma sefid nist; abi əst."
            ),
            "example_az": (
                "Verilən sözlər: İSİM / SAHİB / SƏHV ƏLAMƏT / DÜZGÜN ƏLAMƏT.\n"
                "Quruluş: İSİM + izafət + SAHİB + 1-ci əlamət + نیست؛ + 2-ci əlamət + است.\n"
                "Qırmızı — iki söz izafətlə bağlanır (پرده‌ی کلاس); izafət əlaməti sonuncu hərfə görə "
                "seçilir: «ه»-dan sonra «ی», samitdən sonra kəsrə.\n"
                "Yaşıl — düzgün əlamət «است» ilə təsdiq edilir; birinci əlamət isə «نیست» ilə inkar olunur.\n"
                "Tərcümə: Bizim sinfimizin pərdəsi ağ deyil; mavidir."
            ),
            "items": [
                {
                    "fa": "مو / برادرم / سفید / سیاه",
                    "reading_az": "Mu / bəradərəm / sefid / siyah",
                    "az": "saç / qardaşım / ağ / qara",
                    "sample_answer_fa": "موی برادرم سفید نیست؛ سیاه است.",
                    "sample_answer_reading_az": "Muye bəradərəm sefid nist; siyah əst.",
                    "sample_answer_az": "Qardaşımın saçı ağ deyil; qaradır.",
                },
                {
                    "fa": "غذا / پدربزرگم / کم / زیاد",
                    "reading_az": "Qəza / pedərbozorgəm / kəm / ziyad",
                    "az": "yemək / babam / az / çox",
                    "sample_answer_fa": "غذای پدربزرگم کم نیست؛ زیاد است.",
                    "sample_answer_reading_az": "Qəzaye pedərbozorgəm kəm nist; ziyad əst.",
                    "sample_answer_az": "Babamın yeməyi az deyil; çoxdur.",
                },
                {
                    "fa": "لامپ / اتاق من / زرد / سفید",
                    "reading_az": "Lamp / otağe mən / zərd / sefid",
                    "az": "lampa / mənim otağım / sarı / ağ",
                    "sample_answer_fa": "لامپِ اتاق من زرد نیست؛ سفید است.",
                    "sample_answer_reading_az": "Lampe otağe mən zərd nist; sefid əst.",
                    "sample_answer_az": "Otağımın lampası sarı deyil; ağdır.",
                },
                {
                    "fa": "گاو / آن‌ها / قهوه‌ای / مشکی",
                    "reading_az": "Gav / anha / qəhvei / meşki",
                    "az": "inək / onlar / qəhvəyi / qara",
                    "sample_answer_fa": "گاوِ آن‌ها قهوه‌ای نیست؛ مشکی است.",
                    "sample_answer_reading_az": "Gave anha qəhvei nist; meşki əst.",
                    "sample_answer_az": "Onların inəyi qəhvəyi deyil; qaradır.",
                },
                {
                    "fa": "پنجره / فروش‌گاه / کثیف / تمیز",
                    "reading_az": "Pəncəre / foruşgah / kəsif / təmiz",
                    "az": "pəncərə / mağaza / çirkli / təmiz",
                    "sample_answer_fa": "پنجره‌ی فروش‌گاه کثیف نیست؛ تمیز است.",
                    "sample_answer_reading_az": "Pəncəre-ye foruşgah kəsif nist; təmiz əst.",
                    "sample_answer_az": "Mağazanın pəncərəsi çirkli deyil; təmizdir.",
                },
                {
                    "fa": "فروش‌گاه / دوستم / بزرگ / کوچک",
                    "reading_az": "Foruşgah / dustəm / bozorg / kuçek",
                    "az": "mağaza / dostum / böyük / kiçik",
                    "sample_answer_fa": "فروش‌گاهِ دوستم بزرگ نیست؛ کوچک است.",
                    "sample_answer_reading_az": "Foruşgahe dustəm bozorg nist; kuçek əst.",
                    "sample_answer_az": "Dostumun mağazası böyük deyil; kiçikdir.",
                },
            ],
        },
    ],
    "sentence_practice": {
        "listen_exercises": [
            {
                "items": [
                    {
                        "fa": "در خانه‌ی ما یک چهارپایه‌ی قهوه‌ای وجود دارد.",
                        "reading_az": "Dər xane-ye ma yek çəharpaye-ye qəhvei vocud darəd.",
                        "az": "Bizim evimizdə bir qəhvəyi kətil var.",
                    },
                    {
                        "fa": "من برای دختر کوچکم، جوراب صورتی می‌خرم.",
                        "reading_az": "Mən bəraye doxtəre kuçekəm, curabe surəti mixərəm.",
                        "az": "Mən balaca qızım üçün çəhrayı corab alıram.",
                    },
                    {
                        "fa": "پسرم جواد، یک خط‌کش کوچک دارد؛ خط‌کش او بنفش است.",
                        "reading_az": "Pesərəm Cavad, yek xətkeşe kuçek darəd; xətkeşe u bənəfş əst.",
                        "az": "Oğlum Cavadın kiçik bir xətkeşi var; onun xətkeşi bənövşəyidir.",
                    },
                    {
                        "fa": "دوستم رضا خودکار مشکی دارد؛ او خودکار آبی و قرمز می‌خواهد.",
                        "reading_az": "Dustəm Reza xodkare meşki darəd; u xodkare abi va qermez mixahəd.",
                        "az": "Dostum Rza qara tükənməz qələm var; o, mavi və qırmızı tükənməz qələm istəyir.",
                    },
                    {
                        "fa": "آن مرد، رنگ‌فروش نیست؛ او رنگ‌کار است. او الآن خانه‌ی ما را رنگ می‌زند.",
                        "reading_az": "An mərd, rəngforuş nist; u rəngkar əst. U əl-an xane-ye ma ra rəng mizənəd.",
                        "az": "O kişi rəng satan deyil; o, rəngsazdır. O, indi bizim evimizi rəngləyir.",
                    },
                    {
                        "fa": "آیا این عکس، رنگی نیست؟ نه این عکس نیست؛ سیاه و سفید است.",
                        "reading_az": "Aya in əks, rəngi nist? Nə in əks nist; siyah o sefid əst.",
                        "az": "Bu şəkil rəngli deyilmi? Xeyr, bu şəkil rəngli deyil; ağ-qaradır.",
                    },
                    {
                        "fa": "شما کدام جامدادی را می‌خواهید؟ من جامدادی نارنجی را می‌خواهم.",
                        "reading_az": "Şoma kodam camedadi ra mixahid? Mən camedadiye narenci ra mixahəm.",
                        "az": "Siz hansı qələmqabını istəyirsiniz? Mən narıncı qələmqabını istəyirəm.",
                    },
                    {
                        "fa": "ایشان برای نوشتن از ماژیک قرمز استفاده می‌کند یا آبی؟ او از ماژیک آبی استفاده می‌کند.",
                        "reading_az": "İşan bəraye neveştən əz majike qermez estefade mikonəd ya abi? U əz majike abi estefade mikonəd.",
                        "az": "O, yazmaq üçün qırmızı markerdən istifadə edir, yoxsa mavi? O, mavi markerdən istifadə edir.",
                    },
                ],
            },
        ],
        "answer_items": [],
    },
    "reading_text": {
        "title_fa": "زندگی در روستا",
        "title_az": "Kənddə həyat",
        "paragraphs_fa": [
            "محمّد و خانواده‌اش در روستا زندگی می‌کنند. آن‌ها زندگی‌کردن در روستا را دوست دارند. روستای آن‌ها نزدیک جنگل است.",
            "محمّد دو برادر و یک خواهر دارد. او و برادر کوچکش مهدی هر روز با دوچرخه به مدرسه می‌روند و ساعت دوازده ظهر با هم به خانه می‌آیند.",
            "خانه‌ی آن‌ها بزرگ است. در حیاط خانه‌شان درخت‌های میوه، گل‌های رنگارنگ، بوقلمون، اردک، مرغ، خروس و ده جوجه‌ی زیبا وجود دارد.",
            "بیشتر مردم روستا کشاورز و دامدارند. پدر محمّد هم کشاورز است. او یک باغ کوچک و یک مزرعه‌ی بزرگ گندم و ذرّت دارد. او هر روز صبح برای کارکردن به مزرعه و باغش می‌رود و غروب به خانه می‌آید.",
            "مادر محمّد خانه‌دار است و خواهرش زهرا خیّاط است. او برای خانم‌های روستا لباس‌های زیبا می‌دوزد. محمّد یک برادر بزرگ هم دارد. برادر بزرگش، جواد در شهر زندگی می‌کند. او نقّاش است و در و دیوار خانه‌ها، اداره‌ها، مدرسه‌ها و... را رنگ می‌زند.",
            "محمّد و مهدی علاوه بر درس خواندن، گاهی به مزرعه و باغ می‌روند و به پدرشان کمک می‌کنند.",
        ],
        "footnotes": [
            {"fa": "رنگارنگ", "az": "rəngbərəng"},
            {"fa": "دامدار", "az": "heyvandar (maldar)"},
            {"fa": "مزرعه", "az": "tarla"},
            {"fa": "نزدیک / دور", "az": "yaxın / uzaq"},
            {"fa": "علاوه بر", "az": "…-dan əlavə"},
        ],
        "full_translation_az": (
            "Məhəmməd və ailəsi kənddə yaşayırlar. Onlar kənddə yaşamağı sevirlər. Onların kəndi meşəyə yaxındır.\n\n"
            "Məhəmmədin iki qardaşı və bir bacısı var. O və kiçik qardaşı Mehdi hər gün velosipedlə məktəbə gedir "
            "və günorta saat on ikidə birlikdə evə gəlirlər.\n\n"
            "Onların evi böyükdür. Evlərinin həyətində meyvə ağacları, rəngbərəng güllər, hindtoyuğu, ördək, "
            "toyuq, xoruz və on gözəl cücə var.\n\n"
            "Kənd camaatının çoxu əkinçi və heyvandardır. Məhəmmədin atası da əkinçidir. Onun kiçik bir bağı və "
            "böyük bir buğda-qarğıdalı tarlası var. O, hər gün səhər işləmək üçün tarlasına və bağına gedir, "
            "axşamüstü evə qayıdır.\n\n"
            "Məhəmmədin anası evdar qadındır, bacısı Zəhra isə dərzidir. O, kənd xanımları üçün gözəl paltarlar "
            "tikir. Məhəmmədin bir böyük qardaşı da var. Böyük qardaşı Cavad şəhərdə yaşayır. O, rəngsazdır; "
            "evlərin, idarələrin, məktəblərin qapı-divarlarını rəngləyir.\n\n"
            "Məhəmməd və Mehdi dərs oxumaqdan əlavə, bəzən tarlaya və bağa gedib atalarına kömək edirlər."
        ),
        "sentences": [
            {"fa": "محمّد و خانواده‌اش در روستا زندگی می‌کنند.", "reading_az": "Mohəmməd va xanevadeəş dər rusta zendegi mikonənd.", "az": "Məhəmməd və ailəsi kənddə yaşayırlar.", "new_paragraph": True},
            {"fa": "آن‌ها زندگی‌کردن در روستا را دوست دارند.", "reading_az": "Anha zendegi-kərdən dər rusta ra dust darənd.", "az": "Onlar kənddə yaşamağı sevirlər."},
            {"fa": "روستای آن‌ها نزدیک جنگل است.", "reading_az": "Rustaye anha nəzdike cəngəl əst.", "az": "Onların kəndi meşəyə yaxındır."},
            {"fa": "محمّد دو برادر و یک خواهر دارد.", "reading_az": "Mohəmməd do bəradər va yek xahər darəd.", "az": "Məhəmmədin iki qardaşı və bir bacısı var.", "new_paragraph": True},
            {
                "fa": "او و برادر کوچکش مهدی هر روز با دوچرخه به مدرسه می‌روند و ساعت دوازده ظهر با هم به خانه می‌آیند.",
                "reading_az": "U va bəradəre kuçekəş Mehdi hər ruz ba doçərxe be mædrese mirəvənd va saəte davazdə zohr ba həm be xane miayənd.",
                "az": "O və kiçik qardaşı Mehdi hər gün velosipedlə məktəbə gedir və günorta saat on ikidə birlikdə evə gəlirlər.",
            },
            {"fa": "خانه‌ی آن‌ها بزرگ است.", "reading_az": "Xane-ye anha bozorg əst.", "az": "Onların evi böyükdür.", "new_paragraph": True},
            {
                "fa": "در حیاط خانه‌شان درخت‌های میوه، گل‌های رنگارنگ، بوقلمون، اردک، مرغ، خروس و ده جوجه‌ی زیبا وجود دارد.",
                "reading_az": "Dər həyate xaneşan dərəxthaye mive, golhaye rəngarəng, buqələmun, ordək, morğ, xorus va dəh cuce-ye ziba vocud darəd.",
                "az": "Evlərinin həyətində meyvə ağacları, rəngbərəng güllər, hindtoyuğu, ördək, toyuq, xoruz və on gözəl cücə var.",
            },
            {"fa": "بیشتر مردم روستا کشاورز و دامدارند.", "reading_az": "Biştəre mərdome rusta keşavərz va damdarand.", "az": "Kənd camaatının çoxu əkinçi və heyvandardır.", "new_paragraph": True},
            {"fa": "پدر محمّد هم کشاورز است.", "reading_az": "Pedəre Mohəmməd həm keşavərz əst.", "az": "Məhəmmədin atası da əkinçidir."},
            {
                "fa": "او یک باغ کوچک و یک مزرعه‌ی بزرگ گندم و ذرّت دارد.",
                "reading_az": "U yek bağe kuçek va yek məzrəe-ye bozorge gəndom va zorrət darəd.",
                "az": "Onun kiçik bir bağı və böyük bir buğda-qarğıdalı tarlası var.",
            },
            {
                "fa": "او هر روز صبح برای کارکردن به مزرعه و باغش می‌رود و غروب به خانه می‌آید.",
                "reading_az": "U hər ruz sobh bəraye kar-kərdən be məzrəe va bağəş mirəvəd va ğorub be xane miayəd.",
                "az": "O, hər gün səhər işləmək üçün tarlasına və bağına gedir, axşamüstü evə qayıdır.",
            },
            {
                "fa": "مادر محمّد خانه‌دار است و خواهرش زهرا خیّاط است.",
                "reading_az": "Madəre Mohəmməd xanedar əst va xahərəş Zəhra xəyyat əst.",
                "az": "Məhəmmədin anası evdar qadındır, bacısı Zəhra isə dərzidir.",
                "new_paragraph": True,
            },
            {"fa": "او برای خانم‌های روستا لباس‌های زیبا می‌دوزد.", "reading_az": "U bəraye xanomhaye rusta lebashaye ziba miduzəd.", "az": "O, kənd xanımları üçün gözəl paltarlar tikir."},
            {"fa": "محمّد یک برادر بزرگ هم دارد.", "reading_az": "Mohəmməd yek bəradəre bozorg həm darəd.", "az": "Məhəmmədin bir böyük qardaşı da var."},
            {"fa": "برادر بزرگش، جواد در شهر زندگی می‌کند.", "reading_az": "Bəradəre bozorgəş, Cəvad dər şəhr zendegi mikonəd.", "az": "Böyük qardaşı Cavad şəhərdə yaşayır."},
            {
                "fa": "او نقّاش است و در و دیوار خانه‌ها، اداره‌ها، مدرسه‌ها و... را رنگ می‌زند.",
                "reading_az": "U nəqqaş əst va dər va divare xaneha, edareha, mædreseha va ... ra rəng mizənəd.",
                "az": "O, rəngsazdır; evlərin, idarələrin, məktəblərin qapı-divarlarını rəngləyir.",
            },
            {
                "fa": "محمّد و مهدی علاوه بر درس خواندن، گاهی به مزرعه و باغ می‌روند و به پدرشان کمک می‌کنند.",
                "reading_az": "Mohəmməd va Mehdi əlave bər dərs-xandən, gahi be məzrəe va bağ mirəvənd va be pedərşan komək mikonənd.",
                "az": "Məhəmməd və Mehdi dərs oxumaqdan əlavə, bəzən tarlaya və bağa gedib atalarına kömək edirlər.",
                "new_paragraph": True,
            },
        ],
        "comprehension_questions": [
            {
                "question_fa": "بیشتر مردم روستا چه‌کاره‌اند؟",
                "reading_az": "Biştəre mərdome rusta çekareand?",
                "az": "Kənd əhalisinin çoxu nəçidir?",
                "sample_answer_fa": "بیشتر مردم روستا کشاورز و دامدارند.",
                "sample_answer_reading_az": "Biştəre mərdome rusta keşavərz va damdarand.",
                "sample_answer_az": "Kənd əhalisinin çoxu əkinçi və heyvandardır.",
            },
            {
                "question_fa": "پدر محمّد هر روز چه‌کار می‌کند؟",
                "reading_az": "Pedəre Mohəmməd hər ruz çekar mikonəd?",
                "az": "Məhəmmədin atası hər gün nə edir?",
                "sample_answer_fa": "او هر روز صبح به مزرعه و باغش می‌رود.",
                "sample_answer_reading_az": "U hər ruz sobh be məzrəe va bağəş mirəvəd.",
                "sample_answer_az": "O, hər gün səhər tarlasına və bağına gedir.",
            },
            {
                "question_fa": "محمّد و مهدی علاوه بر درس‌خواندن چه‌کار می‌کنند؟",
                "reading_az": "Mohəmməd va Mehdi əlave bər dərs-xandən çekar mikonənd?",
                "az": "Məhəmməd və Mehdi oxumaqdan əlavə nə edirlər?",
                "sample_answer_fa": "آن‌ها گاهی به مزرعه و باغ می‌روند و به پدرشان کمک می‌کنند.",
                "sample_answer_reading_az": "Anha gahi be məzrəe va bağ mirəvənd va be pedərşan komək mikonənd.",
                "sample_answer_az": "Onlar bəzən tarlaya və bağa gedib atalarına kömək edirlər.",
            },
            {
                "question_fa": "در حیاط خانه‌ی آن‌ها چه حیوان‌هایی وجود دارد؟",
                "reading_az": "Dər həyate xane-ye anha çe heyvanhayi vocud darəd?",
                "az": "Onların evinin həyətində hansı heyvanlar var?",
                "sample_answer_fa": "در حیاط آن‌ها بوقلمون، اردک، مرغ، خروس و جوجه وجود دارد.",
                "sample_answer_reading_az": "Dər həyate anha buqələmun, ordək, morğ, xorus va cuce vocud darəd.",
                "sample_answer_az": "Onların həyətində hindtoyuğu, ördək, toyuq, xoruz və cücə var.",
            },
            {
                "question_fa": "برادرِ بزرگ محمّد چه‌کار می‌کند؟",
                "reading_az": "Bəradəre bozorge Mohəmməd çekar mikonəd?",
                "az": "Məhəmmədin böyük qardaşı nə iş görür?",
                "sample_answer_fa": "برادر بزرگش نقّاش است؛ او در و دیوارها را رنگ می‌زند.",
                "sample_answer_reading_az": "Bəradəre bozorgəş nəqqaş əst; u dər va divarha ra rəng mizənəd.",
                "sample_answer_az": "Böyük qardaşı rəngsazdır; o, qapı-divarları rəngləyir.",
            },
        ],
    },
}
