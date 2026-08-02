# Dərs 14 — ساعت و زمان (Saat və vaxt)
# Mənbə: کتاب دوم, səh. 171-182

LESSON = {
    "number": 14,
    "title_fa": "ساعت و زمان",
    "title_az": "Saat və vaxt",
    "available": True,
    "vocabulary": [
        {"fa": "ساعت مچی", "reading": "saəte moçi", "az": "Qol saatı"},
        {"fa": "ساعت دیواری", "reading": "saəte divari", "az": "Divar saatı"},
        {"fa": "عقربه", "reading": "əqrəbe", "az": "Əqrəb (saat əqrəbi)"},
        {"fa": "دقیقه", "reading": "dəqiqe", "az": "Dəqiqə"},
        {"fa": "باتری", "reading": "batəri", "az": "Batareya"},
        {"fa": "بند ساعت", "reading": "bənde saət", "az": "Saat qayışı"},
        {"fa": "سالم", "reading": "salem", "az": "Sağlam, işlək"},
        {"fa": "خراب", "reading": "xərab", "az": "Xarab"},
        {"fa": "ساعت‌ساز", "reading": "saətsaz", "az": "Saatsaz"},
        {"fa": "ساعت‌سازی", "reading": "saətsazi", "az": "Saat təmiri emalatxanası"},
        {"fa": "ساعت‌فروش", "reading": "saətforuş", "az": "Saat satan"},
        {"fa": "ساعت‌فروشی", "reading": "saətforuşi", "az": "Saat mağazası"},
        {"fa": "روز", "reading": "ruz", "az": "Gün"},
        {"fa": "صبح", "reading": "sobh", "az": "Səhər"},
        {"fa": "ظهر", "reading": "zohr", "az": "Günorta"},
        {"fa": "بعدازظهر (عصر)", "reading": "bədəzzohr (əsr)", "az": "Günortadan sonra (əsr)"},
        {"fa": "سحر", "reading": "səhər", "az": "Dan yeri, sübh"},
        {"fa": "سرشب", "reading": "sərşəb", "az": "Axşamüstü (gecənin əvvəli)"},
        {"fa": "شب", "reading": "şəb", "az": "Gecə"},
        {"fa": "نیمه‌شب", "reading": "nimeşəb", "az": "Gecəyarısı"},
        {"fa": "شبانه‌روز", "reading": "şəbaneruz", "az": "Sutka"},
        {"fa": "خواب", "reading": "xab", "az": "Yuxu"},
        {"fa": "بیدار", "reading": "bidar", "az": "Ayıq, oyaq"},
        {"fa": "تعمیر می‌کند (درست می‌کند)", "reading": "təmir mikonəd (dorost mikonəd)", "az": "təmir edir"},
        {"fa": "طلوع می‌کند", "reading": "toluu mikonəd", "az": "doğur (günəş)"},
        {"fa": "غروب می‌کند", "reading": "qorub mikonəd", "az": "batır (günəş)"},
        {"fa": "می‌خوابد", "reading": "mixabəd", "az": "yatır"},
        {"fa": "بیدار می‌شود", "reading": "bidar mişəvəd", "az": "oyanır"},
        {"fa": "نام خانوادگی", "reading": "name xanevadegi", "az": "Soyad"},
        {"fa": "خوش‌اخلاق", "reading": "xoşəxlaq", "az": "Xoşrəftar"},
        {"fa": "سرِ چهارراه", "reading": "səre çəharrah", "az": "Dördyol ayrıcının başında"},
        {"fa": "فاصله", "reading": "fasele", "az": "Məsafə"},
        {"fa": "سرِ ساعت", "reading": "səre saət", "az": "Vaxtında, dəqiq saatında"},
        {"fa": "دوباره", "reading": "dobare", "az": "Yenidən"},
        {"fa": "شاگرد", "reading": "şagerd", "az": "Şagird, çırağ"},
        {"fa": "همه", "reading": "həme", "az": "Hamısı"},
        {"fa": "وضو می‌گیرد", "reading": "vozu migirəd", "az": "dəstamaz alır"},
        {"fa": "استراحت می‌کند", "reading": "esterahət mikonəd", "az": "istirahət edir"},
    ],
    "grammar_notes": [
        {
            "title_az": "Saatların öyrədilməsi",
            "title_fa": "آموزش ساعت",
            "explanation_az": (
                "Saat soruşulanda cavab «ساعت، … است» qəlibi ilə verilir.\n"
                "Dəqiqə sıfırdırsa yalnız saat deyilir: ساعت شش است (saat altıdır).\n"
                "Günün hissəsi əlavə oluna bilər: صبح (səhər), ظهر (günorta), بعدازظهر (günortadan sonra), عصر (axşamüstü), شب (gecə), نیمه‌شب (gecə yarısı).\n"
                "Nümunələr: ساعت، هشت صبح است / ساعت، دوازده ظهر است / ساعت، پنج بعدازظهر است / ساعت، نه شب است.\n"
                "Dərsliyin qeydi: «عصر» günortadan sonra günəş batana qədərki vaxta deyilir — «پنج بعدازظهر» = «پنج عصر».\n"
                "«نصف شب» = «نیمه‌شب» (gecə yarısı): ساعت، سه بعد از نصف شب است.\n"
                "Dəqiq olmayan vaxt üçün «حدود» işlənir: ساعت، حدود دوازده است (təxminən on iki).\n"
                "24 saatlıq sistem: günortadan sonrakı saatlar həm «بعدازظهر» ilə, həm də 13-24 kimi deyilə bilər.\n"
                "Dərsliyin cədvəli: یک بعدازظهر = سیزده، دو بعدازظهر = چهارده … ده شب = بیست و دو."
            ),
            "note_fa": (
                "۱. ساعت «یک» بعدازظهر تا «دوازده» شب را، به این شکل هم می‌گوییم:\n"
                "یک بعدازظهر = سیزده / دو بعدازظهر = چهارده / سه بعدازظهر = پانزده / چهار بعدازظهر = شانزده / پنج عصر = هفده / شش عصر = هجده / هفت عصر = نوزده / هشت شب = بیست / نه شب = بیست و یک / ده شب = بیست و دو / یازده شب = بیست و سه / دوازده شب = بیست و چهار\n"
                "۲. عصر: از اواسط بعدازظهر تا غروب آفتاب را «عصر» هم می‌گویند.\n"
                "۳. نصف شب: نیمه شب"
            ),            "note_reading_az": (
                "1. Saəte «yek» bə'dəzzohr ta «dəvazdəh» şəb ra, be in şekl həm miguyim:\n"
                "yek bə'dəzzohr = sizdəh / do bə'dəzzohr = çəhardəh / … / dəvazdəh şəb = bistO-çəhar\n"
                "2. Əsr: əz əvaset bə'dəzzohr ta qorube aftab ra «əsr» həm miguyənd.\n"
                "3. Nesfe şəb: nime şəb"
            ),            "note_az": (
                "1. Günortadan sonrakı saatlar iki cür deyilir (12-lik və 24-lük sistem):\n"
                "یک بعدازظهر = سیزده (13) | دو بعدازظهر = چهارده (14) | سه بعدازظهر = پانزده (15)\n"
                "چهار بعدازظهر = شانزده (16) | پنج عصر = هفده (17) | شش عصر = هجده (18)\n"
                "هفت عصر = نوزده (19) | هشت شب = بیست (20) | نه شب = بیست و یک (21)\n"
                "ده شب = بیست و دو (22) | یازده شب = بیست و سه (23) | دوازده شب = بیست و چهار (24)\n"
                "2. «عصر» — günortadan sonranın ortasından gün batımına qədərki vaxtdır.\n"
                "3. «نصف شب» = «نیمه شب» — gecə yarısı."
            ),
            "conjugations": [
                {"pronoun_fa": "ساعت شش است.", "form_fa": "Saat altıdır."},
                {"pronoun_fa": "ساعت، هشت صبح است.", "form_fa": "Saat səhər səkkizdir."},
                {"pronoun_fa": "ساعت، دوازدهِ ظهر است.", "form_fa": "Saat günorta on ikidir."},
                {"pronoun_fa": "ساعت، پنجِ بعدازظهر (عصر) است.", "form_fa": "Saat günortadan sonra beşdir (əsr beşdir)."},
                {"pronoun_fa": "ساعت، نه شب است.", "form_fa": "Saat gecə doqquzdur."},
                {"pronoun_fa": "ساعت، دوازده نیمه‌شب است.", "form_fa": "Saat gecəyarısı on ikidir."},
            ],
            "examples": [
                {"fa": "ساعت «یک» بعدازظهر تا «دوازده» شب را، به این شکل هم می‌گوییم: یک بعدازظهر = سیزده؛ دو بعدازظهر = چهارده؛ … دوازده شب = بیست و چهار.", "reading_az": "Saəte «yek» bədəzzohr ta «davazdəh» şəb ra, be in şekl həm miguyim: yek bədəzzohr = sizdəh; do bədəzzohr = çəhardəh; ... davazdəh şəb = bist o çəhar.", "az": "24 saatlıq sistemdə: günortadan sonra saat bir = 13, iki = 14 və s., gecə saat on iki = 24."},
                {"fa": "«عصر»: از اواسط بعدازظهر تا غروب آفتاب را «عصر» هم می‌گویند.", "reading_az": "«Əsr»: əz əvasete bədəzzohr ta qorube aftab ra «əsr» həm miguyənd.", "az": "«عصر» (əsr) — günortadan sonranın ortasından günəş batana qədər olan vaxt."},
                {"fa": "«نصف شب»: نیمه‌شب.", "reading_az": "«Nesfe şəb»: nimeşəb.", "az": "«نصف شب» = gecəyarısı."},
                {"fa": "ساعت، شش است. ساعت، هشتِ صبح است. ساعت، دوازدهِ ظهر است.", "reading_az": "Saət, şeş əst. Saət, həşte sobh əst. Saət, davazdəhe zohr əst.", "az": "Saat altıdır. Saat səhər səkkizdir. Saat günorta on ikidir."},
                {"fa": "ساعت، سه بعد از نصفِ شب است. ساعت، حدود دوازده است.", "reading_az": "Saət, se bəd əz nesfe şəb əst. Saət, hodude davazdəh əst.", "az": "Saat gecəyarısından sonra üçdür. Saat təxminən on ikidir."},
            ],
        },
        {
            "title_az": "Dəqiqələrin bildirilməsi: «ربع» və «نیم»",
            "title_fa": "ساعت با «دقیقه»؛ «ربع» و «نیم»",
            "explanation_az": (
                "Dəqiqə saatdan sonra «و» ilə əlavə olunur: ساعت، دوازده و پنج دقیقه است.\n"
                "Quruluş: ساعت + SAAT + و + DƏQİQƏ + دقیقه + است.\n"
                "Nümunələr: چهار و ده دقیقه / هفت و پانزده دقیقه / ده و چهل و هفت دقیقه.\n"
                "15 dəqiqə üçün «ربع» (rüb) da işlənir: ساعت، چهار و ربع است = چهار و پانزده دقیقه.\n"
                "30 dəqiqə üçün «نیم» (yarım) işlənir: ساعت، هشت و نیم است = هشت و سی دقیقه.\n"
                "«ربع» və «نیم» ilə «دقیقه» sözü DEYİLMİR: هشت و نیم ✓ — هشت و نیم دقیقه ✗\n"
                "Saat tama yaxın olanda «حدود» ilə yuvarlaqlaşdırıla bilər: دوازده و پنجاه و هفت دقیقه = حدود یک.\n"
                "Fars dilində dəqiqə həmişə ƏLAVƏ olunur — Azərbaycan dilindəki «bir dəqiqə qalıb» quruluşu işlənmir."
            ),
            "conjugations": [
                {"pronoun_fa": "ساعت، دوازده و پنج دقیقه است.", "form_fa": "Saat on iki və beş dəqiqədir."},
                {"pronoun_fa": "ساعت، دوازده و پانزده دقیقه است.", "form_fa": "= ساعت، دوازده و ربع است."},
                {"pronoun_fa": "ساعت، دوازده و سی دقیقه است.", "form_fa": "= ساعت، دوازده و نیم است."},
                {"pronoun_fa": "ساعت، دوازده و چهل و پنج دقیقه است.", "form_fa": "= ساعت، یک، ربع کم است (istifadə olunmur — 45 dəqiqə kimi deyilir)."},
            ],
            "examples": [
                {"fa": "«ربع» ilə «دقیقه» eyni cümlədə bir yerdə işlənmir: ساعت دوازده و ربع و نیم دقیقه است. ✗", "reading_az": "Vajeye «dəqiqe» ba kəlmehaye «rob» va «nim» estefade nemişəvəd.", "az": "«ربع» və «نیم» sözləri «دقیقه» sözü ilə birlikdə işlənmir."},
                {"fa": "ساعت، چهار و ده دقیقه است.", "reading_az": "Saət, çəhar va dəh dəqiqe əst.", "az": "Saat dörd və on dəqiqədir."},
                {"fa": "ساعت، هفت و پانزده دقیقه است.", "reading_az": "Saət, həft va panzdəh dəqiqe əst.", "az": "Saat yeddi və on beş dəqiqədir."},
                {"fa": "ساعت، شش و بیست و پنج دقیقه است.", "reading_az": "Saət, şeş va bist o pənc dəqiqe əst.", "az": "Saat altı və iyirmi beş dəqiqədir."},
                {"fa": "ساعت، هشت و سی دقیقه است.", "reading_az": "Saət, həşt va si dəqiqe əst.", "az": "Saat səkkiz və otuz dəqiqədir."},
                {"fa": "ساعت، ده و چهل و هفت دقیقه است.", "reading_az": "Saət, dəh va çəhel o həft dəqiqe əst.", "az": "Saat on və qırx yeddi dəqiqədir."},
                {"fa": "ساعت، دوازده و پنجاه و هفت دقیقه است. (ساعت، حدود یک است.)", "reading_az": "Saət, davazdəh va pənca o həft dəqiqe əst. (Saət, hodude yek əst.)", "az": "Saat on iki və əlli yeddi dəqiqədir. (Saat təxminən birdir.)"},
                {"fa": "حسین هر شب از ساعت ده و نیم تا ساعت یازده و ربع، قرآن می‌خواند.", "reading_az": "Hoseyn hər şəb əz saəte dəh o nim ta saəte yazdəh o rob, Qorən mixanəd.", "az": "Hüseyn hər gecə saat on yarımdan on bir rübə qədər Quran oxuyur."},
                {"fa": "دکتر حسینی هر روز از ساعت هشت و سی دقیقه تا یازده و نیم، بیماران را معاینه می‌کند.", "reading_az": "Doktor Hoseyni hər ruz əz saəte həşt o si dəqiqe ta yazdəh o nim, bimaran ra moayene mikonəd.", "az": "Doktor Hüseyni hər gün saat səkkiz otuzdan on bir yarıma qədər xəstələri müayinə edir."},
                {"fa": "پدرم امروز صبح، ساعت شش و نیم به اداره رفت. او ساعت سه و ربع به خانه می‌آید.", "reading_az": "Pedərəm emruz sobh, saəte şeş o nim be edare rəft. U saəte se o rob be xane miayəd.", "az": "Atam bu gün səhər saat altı yarımda idarəyə getdi. O, saat üç rübdə evə gəlir."},
                {"fa": "من دیشب ساعت یازده و ربع خوابیدم و ساعت چهار و نیم صبح بیدار شدم.", "reading_az": "Mən dişəb saəte yazdəh o rob xabidəm va saəte çəhar o nim sobh bidar şodəm.", "az": "Mən dünən gecə saat on bir rübdə yatdım və səhər saat dörd yarımda oyandım."},
                {"fa": "آفتاب امروز ساعت شش و ربع طلوع می‌کند و ساعت هفت و نیم عصر غروب می‌کند.", "reading_az": "Aftab emruz saəte şeş o rob toluu mikonəd va saəte həft o nim əsr qorub mikonəd.", "az": "Günəş bu gün saat altı rübdə doğur və axşam saat yeddi yarımda batır."},
            ],
        },
        {
            "title_az": "Sual sözü «ساعت، چند است؟» (saat neçədir?)",
            "title_fa": "واژه‌ی پرسشی «ساعت، چند است؟»",
            "explanation_az": (
                "Saat soruşmaq üçün «ساعت، چند است؟» işlənir — hərfi mənada «saat neçədir?».\n"
                "Cavab: «ساعت، … است» — sual sözünün yerinə vaxt qoyulur.\n"
                "Dərsliyin qeydi: danışıq dilində «ساعت، چند است؟» əvəzinə «ساعت، چندِ؟» deyilir.\n"
                "Cavab formaları: ساعت، یازده است / ساعت، پنج و ده دقیقه است / ساعت، هفت و نیم است.\n"
                "Günün hissəsi ilə: ساعت، چهارِ بعدازظهر است.\n"
                "Diqqət: burada «چند» MİQDAR sual sözüdür — «چندم» (sıra) ilə qarışdırmayın.\n"
                "Konkret bir işin vaxtını soruşmaq üçün «ساعت چند» işlənir: شما ساعت چند به کلاس می‌روید؟\n"
                "Cavabda «ساعت» sözü təkrarlanır: من ساعت هشت به کلاس می‌روم."
            ),
            "note_fa": (
                "در زبان گفتار «ساعت، چند است؟» را «ساعت، چندِ؟» می‌گوییم."
            ),            "note_reading_az": (
                "Dər zəbane goftar «saət, çənd əst?» ra «saət, çəndE?» miguyim."
            ),            "note_az": (
                "Danışıq dilində «ساعت، چند است؟» qısaldılıb «ساعت، چندِ؟» deyilir.\n"
                "Yazıda və rəsmi danışıqda tam forma işlənir.\n"
                "Cavab həmişə «ساعت، … است» qəlibi ilə verilir."
            ),
            "conjugations": [
                {"pronoun_fa": "ساعت، چند است؟", "form_fa": "ساعت، هفت و بیست دقیقه است."},
            ],
            "examples": [
                {"fa": "ساعت، چند است؟ ساعت، یازده است.", "reading_az": "Saət, çənd əst? Saət, yazdəh əst.", "az": "Saat neçədir? Saat on birdir."},
                {"fa": "ساعت، چند است؟ ساعت، پنج و ده دقیقه است.", "reading_az": "Saət, çənd əst? Saət, pənc va dəh dəqiqe əst.", "az": "Saat neçədir? Saat beş və on dəqiqədir."},
                {"fa": "ساعت، چند است؟ ساعت، چهار بعدازظهر است.", "reading_az": "Saət, çənd əst? Saət, çəhar bədəzzohr əst.", "az": "Saat neçədir? Saat günortadan sonra dörddür."},
                {"fa": "ساعت، چند است؟ ساعت، سه و چهل و دو دقیقه است.", "reading_az": "Saət, çənd əst? Saət, se va çəhel o do dəqiqe əst.", "az": "Saat neçədir? Saat üç və qırx iki dəqiqədir."},
                {"fa": "در گفتار فارسی «ساعت، چند است؟» را «ساعت، چنده؟» هم می‌گویند.", "reading_az": "Dər goftare farsi «saət, çənd əst?» ra «saət, çənde?» həm miguyənd.", "az": "Danışıqda «ساعت، چند است؟» sözü «ساعت، چنده؟» kimi deyilir."},
            ],
        },
        {
            "title_az": "Sual sözü «چه وقت» (nə vaxt?)",
            "title_fa": "واژه‌ی پرسشی «چه وقت»",
            "explanation_az": (
                "«چه وقت» = «nə vaxt?» — hərəkətin zamanını soruşur.\n"
                "Danışıq dilində qısaca «کی» deyilir: جشن تولّد کی است؟ = جشن تولّد چه وقت است؟\n"
                "Cavab müxtəlif zaman ifadələri ilə verilə bilər: ساعat, gün, tarix və ya təxmini vaxt.\n"
                "Nümunə: چه وقت فیلم تماشا می‌کنیم؟ ← ما ساعت نه شب فیلم تماشا می‌کنیم.\n"
                "Nümunə: چه وقت کتاب اوّل را خواندی؟ ← حدود بیست روز قبل.\n"
                "«چه وقت» cümlənin əvvəlində və ya felin önündə gələ bilər.\n"
                "Fərq: «ساعت چند» dəqiq saatı, «چه وقت» isə ümumi vaxtı soruşur.\n"
                "Yaxın sual sözləri: «کی» (nə vaxt), «چند شنبه» (hansı gün), «چه ماهی» (hansı ay)."
            ),
            "conjugations": [
                {"pronoun_fa": "چه وقت به کلاس آمدی؟", "form_fa": "من ساعت هشت به کلاس آمدم."},
                {"pronoun_fa": "چه وقت به مسافرت می‌روی؟", "form_fa": "من آخر تابستان به مسافرت می‌روم."},
                {"pronoun_fa": "چه وقت ناهار می‌خوری؟", "form_fa": "من بعد از خواندن نماز ظهر، ناهار می‌خورم."},
            ],
            "examples": [
                {"fa": "دیشب چه وقت خوابیدی؟ من دیشب ساعت ده و نیم خوابیدم.", "reading_az": "Dişəb çe vaqt xabidi? Mən dişəb saəte dəh o nim xabidəm.", "az": "Dünən gecə nə vaxt yatdın? Mən dünən gecə saat on yarımda yatdım."},
                {"fa": "آقا! ساعتم را چه وقت تعمیر می‌کنی؟ ساعتت را فردا تعمیر می‌کنم.", "reading_az": "Ağa! Saətəm ra çe vaqt təmir mikoni? Saətət ra fərda təmir mikonəm.", "az": "Ağa, saatımı nə vaxt təmir edəcəksən? Saatını sabah təmir edəcəyəm."},
                {"fa": "شما چه وقت‌هایی مطالعه می‌کنی؟ من هر روز صبح زود مطالعه می‌کنم.", "reading_az": "Şoma çe vaqthayi motaleə mikoni? Mən hər ruz sobh zud motaleə mikonəm.", "az": "Sən hansı vaxtlarda mütaliə edirsən? Mən hər gün səhər tezdən mütaliə edirəm."},
                {"fa": "چه وقت در موزه‌ها را می‌بندند؟ سرِ شب در موزه‌ها را می‌بندند.", "reading_az": "Çe vaqt dəre muzeha ra mibəndənd? Səre şəb dəre muzeha ra mibəndənd.", "az": "Muzeylərin qapılarını nə vaxt bağlayırlar? Axşamüstü muzeylərin qapılarını bağlayırlar."},
                {"fa": "در زبان گفتار «چه وقت» را «کی» هم می‌گویند: کی به کلاس آمدی؟", "reading_az": "Dər zəbane goftar «çe vaqt» ra «key» həm miguyənd: key be kelas amədi?", "az": "Danışıqda «چه وقت» sözü «کی» kimi işlənir: sinfə nə vaxt gəldin?"},
            ],
        },
    ],
    "exercises": [
        {
            # Çalışma 1 — səh. 178 «مانند مثال بپرسید و پاسخ دهید» (saat oxumaq).
            # Dərslikdə hər bəndin öz saat şəkli var; şəkillər admin paneldən yüklənir.
            "kind": "picture_sentences",
            "title_fa": "مانند مثال بپرسید و پاسخ دهید — ساعت",
            "instruction_az": "Nümunə kimi soruşun və cavab verin (saatı oxuyun)",
            "example_fa": "ساعت، چند است؟",
            "example_reading_az": "Saət, çənd əst?",
            "example_az": "Saat neçədir? (danışıqda «ساعت، چندِ؟» deyilir)",
            "example_answer_fa": "ساعت، ده و بیست دقیقه است.",
            "example_answer_reading_az": "Saət, dəh o bist dəqiqe əst.",
            "example_answer_az": "Saat onu iyirmi dəqiqə keçib.",
            "items": [
                {
                    "image": "",
                    "sentences": [
                        {"fa": "ساعت، چند است؟", "reading_az": "Saət, çənd əst?", "az": "Saat neçədir? (۱۱:۰۰)"},
                        {"fa": "ساعت، یازده است.", "reading_az": "Saət, yazdəh əst.", "az": "Saat on birdir. — dəqiqə sıfırdırsa yalnız saat deyilir."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "ساعت، چند است؟", "reading_az": "Saət, çənd əst?", "az": "Saat neçədir? (۵:۱۰)"},
                        {"fa": "ساعت، پنج و ده دقیقه است.", "reading_az": "Saət, pənc o dəh dəqiqe əst.", "az": "Saat beşi on dəqiqə keçib."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "ساعت، چند است؟", "reading_az": "Saət, çənd əst?", "az": "Saat neçədir? (۴:۱۵)"},
                        {"fa": "ساعت، چهار و ربع است.", "reading_az": "Saət, çəhar o rob' əst.", "az": "Saat dördün rübüdür. — 15 dəqiqə üçün «ربع»."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "ساعت، چند است؟", "reading_az": "Saət, çənd əst?", "az": "Saat neçədir? (۸:۳۰)"},
                        {"fa": "ساعت، هشت و نیم است.", "reading_az": "Saət, həşt o nim əst.", "az": "Saat səkkizin yarısıdır. — 30 dəqiqə üçün «نیم»."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "ساعت، چند است؟", "reading_az": "Saət, çənd əst?", "az": "Saat neçədir? (۱۰:۴۷)"},
                        {"fa": "ساعت، ده و چهل و هفت دقیقه است.", "reading_az": "Saət, dəh o çehelO-həft dəqiqe əst.", "az": "Saat onu qırx yeddi dəqiqə keçib."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "ساعت، چند است؟", "reading_az": "Saət, çənd əst?", "az": "Saat neçədir? (۷:۲۵)"},
                        {"fa": "ساعت، هفت و بیست و پنج دقیقه است.", "reading_az": "Saət, həft o bistO-pənc dəqiqe əst.", "az": "Saat yeddini iyirmi beş dəqiqə keçib."},
                    ],
                },
            ],
        },
        {
            # Çalışma 2 — səh. 182 «مانند مثال بگویید» (saatları oxumaq — təkrar).
            "kind": "picture_sentences",
            "title_fa": "مانند مثال بگویید — ساعت",
            "instruction_az": "Nümunə kimi saatları deyin",
            "example_fa": "ساعت، سه و بیست و پنج دقیقه است.",
            "example_reading_az": "Saət, se o bistO-pənc dəqiqe əst.",
            "example_az": "Saat üçü iyirmi beş dəqiqə keçib.",
            "items": [
                {"image": "", "sentences": [{"fa": "ساعت، شش و ده دقیقه است.", "reading_az": "Saət, şeş o dəh dəqiqe əst.", "az": "Saat altını on dəqiqə keçib. (۶:۱۰)"}]},
                {"image": "", "sentences": [{"fa": "ساعت، نه و ربع است.", "reading_az": "Saət, noh o rob' əst.", "az": "Saat doqquzun rübüdür. (۹:۱۵)"}]},
                {"image": "", "sentences": [{"fa": "ساعت، دوازده و نیم است.", "reading_az": "Saət, dəvazdəh o nim əst.", "az": "Saat on ikinin yarısıdır. (۱۲:۳۰)"}]},
                {"image": "", "sentences": [{"fa": "ساعت، دو و چهل دقیقه است.", "reading_az": "Saət, do o çehel dəqiqe əst.", "az": "Saat ikini qırx dəqiqə keçib. (۲:۴۰)"}]},
                {"image": "", "sentences": [{"fa": "ساعت، پنج و پنجاه و پنج دقیقه است.", "reading_az": "Saət, pənc o pəncahO-pənc dəqiqe əst.", "az": "Saat beşi əlli beş dəqiqə keçib — «حدود شش» də demək olar. (۵:۵۵)"}]},
                {"image": "", "sentences": [{"fa": "ساعت، هشت است.", "reading_az": "Saət, həşt əst.", "az": "Saat səkkizdir. (۸:۰۰)"}]},
            ],
        },
        {
            # Çalışma 3 — «چه وقت» sual sözü ilə tamamlama.
            "kind": "fill_blank",
            "instruction_az": "«چه وقت» və «کی» sual sözləri ilə tamamlayın.",
            "word_bank": ["چه وقت", "کی", "چه وقت", "چه وقت"],
            "items": [
                {
                    "fa_with_blank": "___ فیلم تماشا می‌کنیم؟ ما ساعت نه شب فیلم تماشا می‌کنیم.",
                    "correct_answer": "چه وقت", "reading_az": "çe vəqt", "az": "nə vaxt",
                    "full_reading_az": "Çe vəqt film təmaşa mikonim? Ma saəte noh şəb film təmaşa mikonim.",
                    "full_translation_az": "Nə vaxt film baxırıq? Biz axşam saat doqquzda film baxırıq.",
                },
                {
                    "fa_with_blank": "___ به مادرم هدیه می‌دهی؟ من امروز عصر به مادرم هدیه می‌دهم.",
                    "correct_answer": "چه وقت", "reading_az": "çe vəqt", "az": "nə vaxt",
                    "full_reading_az": "Çe vəqt be madərəm hedye midəhi? Mən emruz əsr be madərəm hedye midəhəm.",
                    "full_translation_az": "Anama nə vaxt hədiyyə verirsən? Mən bu gün axşamüstü anama hədiyyə verirəm.",
                },
                {
                    "fa_with_blank": "جشن تولّد فرزندم ___ است؟ پس‌فردا است.",
                    "correct_answer": "کی", "reading_az": "key", "az": "nə vaxt",
                    "full_reading_az": "Cəşne təvəllode fərzəndəm key əst? Pəsfærda əst.",
                    "full_translation_az": "Övladımın ad günü nə vaxtdır? Birisi gündür. — «کی» = «چه وقت»in qısa formasıdır.",
                },
                {
                    "fa_with_blank": "___ کتاب اوّل را خواندی؟ حدود بیست روز قبل.",
                    "correct_answer": "چه وقت", "reading_az": "çe vəqt", "az": "nə vaxt",
                    "full_reading_az": "Çe vəqt ketabe əvvəl ra xandi? Hodude bist ruz qəbl.",
                    "full_translation_az": "Birinci kitabı nə vaxt oxudun? Təxminən iyirmi gün əvvəl.",
                },
            ],
        },
        {
            # Çalışma 4 — səh. 182 «لطفاً جایگزین کنید» («سرِ ساعت»).
            # Əvvəllər sadə practice_reveal idi.
            "kind": "answer_question",
            "title_fa": "لطفاً جایگزین کنید — «سرِ ساعت»",
            "instruction_az": "Nümunə kimi əvəz edin («سرِ ساعت …» — düz saatda)",
            # Yaşıl «سرِ ساعت» — dəqiq vaxt, qırmızı — keçmiş zaman feli.
            "example_fa": (
                "استاد / هشت / کلاس / آمدن\n"
                "استاد *سرِ ساعت* هشت به کلاس **آمد**."
            ),
            "example_reading_az": (
                "Ostad / həşt / kelas / amədən\n"
                "Ostad səre saəte həşt be kelas aməd."
            ),
            "example_az": (
                "Verilən sözlər: SUBYEKT / SAAT / YER / MƏSDƏR.\n"
                "Quruluş: SUBYEKT + سرِ ساعت + SAAT + به + YER + KEÇMİŞ FEL.\n"
                "Yaşıl «سرِ ساعت» — «düz saatda, dəqiq saatda» mənasını verir və izafətlə oxunur.\n"
                "Qırmızı fel KEÇMİŞ zamandadır: آمد، رفت، خوابید.\n"
                "Tərcümə: Müəllim düz saat səkkizdə sinfə gəldi."
            ),
            "items": [
                {"fa": "هواپیما / ده / مشهد / رفتن", "reading_az": "Həvapeyma / dəh / Məşhəd / rəftən", "az": "təyyarə / saat 10 / Məşhəd / getmək",
                 "sample_answer_fa": "هواپیما سرِ ساعت ده به مشهد رفت.", "sample_answer_reading_az": "Həvapeyma səre saəte dəh be Məşhəd rəft.",
                 "sample_answer_az": "Təyyarə düz saat onda Məşhədə getdi."},
                {"fa": "مادربزرگمان / نه / دارو / خوردن", "reading_az": "Madərbozorgeman / noh / daru / xordən", "az": "nənəmiz / saat 9 / dərman / içmək",
                 "sample_answer_fa": "مادربزرگمان سرِ ساعت نه دارو خورد.", "sample_answer_reading_az": "Madərbozorgeman səre saəte noh daru xord.",
                 "sample_answer_az": "Nənəmiz düz saat doqquzda dərman içdi."},
                {"fa": "ما / یازده / اتاقمان / خوابیدن", "reading_az": "Ma / yazdəh / otaqeman / xabidən", "az": "biz / saat 11 / otağımız / yatmaq",
                 "sample_answer_fa": "ما سرِ ساعت یازده در اتاقمان خوابیدیم.", "sample_answer_reading_az": "Ma səre saəte yazdəh dər otaqeman xabidim.",
                 "sample_answer_az": "Biz düz saat on birdə otağımızda yatdıq."},
                {"fa": "کارمندها / هفت و نیم / محل کار / آمدن", "reading_az": "Karməndha / həft o nim / məhəlle kar / amədən", "az": "işçilər / 7:30 / iş yeri / gəlmək",
                 "sample_answer_fa": "کارمندها سرِ ساعت هفت و نیم به محل کار آمدند.", "sample_answer_reading_az": "Karməndha səre saəte həft o nim be məhəlle kar amədənd.",
                 "sample_answer_az": "İşçilər düz saat yeddi otuzda iş yerinə gəldilər."},
            ],
        },
        {
            # Çalışma 5 — səh. 182 «لطفاً جایگزین کنید» («فاصله‌ی … تا …»).
            # Əvvəllər sadə practice_reveal idi.
            "kind": "answer_question",
            "title_fa": "لطفاً جایگزین کنید — «فاصله‌ی … تا …»",
            "instruction_az": "Nümunə kimi məsafəni deyin («فاصله‌ی … تا … حدود … است»)",
            # Yaşıl «فاصله‌ی … تا …» — məsafə, qırmızı «حدود» — təxmini.
            "example_fa": (
                "خانه‌ی ناصر / مغازه‌اش / پانصد متر\n"
                "*فاصله‌ی* خانه‌ی ناصر *تا* مغازه‌اش **حدود** پانصد متر است."
            ),
            "example_reading_az": (
                "Xane-ye Naser / məğazeəş / pansəd metr\n"
                "Fasele-ye xane-ye Naser ta məğazeəş hodude pansəd metr əst."
            ),
            "example_az": (
                "Verilən sözlər: BAŞLANĞIC YER / SON YER / MƏSAFƏ.\n"
                "Quruluş: فاصله‌ی + YER1 + تا + YER2 + (حدود) + MƏSAFƏ + است.\n"
                "Yaşıl «فاصله‌ی … تا …» — «…-dan …-a qədər olan məsafə»; izafətlə bağlanır.\n"
                "Qırmızı «حدود» («təxminən») dəqiq olmayan məsafələrdə işlənir, məcburi deyil.\n"
                "Ölçü vahidi: qısa məsafə → متر, uzun məsafə → کیلومتر.\n"
                "Tərcümə: Nasirin evindən mağazasına qədər təxminən beş yüz metrdir."
            ),
            "items": [
                {"fa": "تهران / قم / صد و سی کیلومتر", "reading_az": "Tehran / Qom / sədO-si kilumetr", "az": "Tehran / Qum / 130 km",
                 "sample_answer_fa": "فاصله‌ی تهران تا قم صد و سی کیلومتر است.", "sample_answer_reading_az": "Fasele-ye Tehran ta Qom sədO-si kilumetr əst.",
                 "sample_answer_az": "Tehrandan Quma qədər yüz otuz kilometrdir."},
                {"fa": "روستای ما / شهر / بیست کیلومتر", "reading_az": "Rustaye ma / şəhr / bist kilumetr", "az": "kəndimiz / şəhər / 20 km",
                 "sample_answer_fa": "فاصله‌ی روستای ما تا شهر بیست کیلومتر است.", "sample_answer_reading_az": "Fasele-ye rustaye ma ta şəhr bist kilumetr əst.",
                 "sample_answer_az": "Kəndimizdən şəhərə qədər iyirmi kilometrdir."},
                {"fa": "کشور من / ایران / … کیلومتر", "reading_az": "Kəşvəre mən / Iran / … kilumetr", "az": "ölkəm / İran / … km",
                 "sample_answer_fa": "فاصله‌ی کشور من تا ایران حدود هزار کیلومتر است.", "sample_answer_reading_az": "Fasele-ye kəşvəre mən ta Iran hodude hezar kilumetr əst.",
                 "sample_answer_az": "Ölkəmdən İrana qədər təxminən min kilometrdir. (öz ölkənizə görə cavab verin)"},
                {"fa": "خانه‌ام / دانش‌گاه / سه کیلومتر", "reading_az": "Xaneəm / daneşgah / se kilumetr", "az": "evim / universitet / 3 km",
                 "sample_answer_fa": "فاصله‌ی خانه‌ام تا دانش‌گاه سه کیلومتر است.", "sample_answer_reading_az": "Fasele-ye xaneəm ta daneşgah se kilumetr əst.",
                 "sample_answer_az": "Evimdən universitetə qədər üç kilometrdir."},
            ],
        },
        {
            # Çalışma 6 — «تعمیر کردن» ilə peşə cümlələri.
            # Əvvəllər sadə practice_reveal idi.
            "kind": "answer_question",
            "title_fa": "مانند مثال بگویید — «تعمیر کردن»",
            "instruction_az": "Nümunə kimi cümlə qurun (peşə + təmir etdiyi əşya)",
            "example_fa": (
                "پدربزرگم / ساعت‌ساز / ساعت\n"
                "پدربزرگم ساعت‌ساز است. او ساعت‌های *خراب* را **تعمیر می‌کند**."
            ),
            "example_reading_az": (
                "Pedərbozorgəm / saətsaz / saət\n"
                "Pedərbozorgəm saətsaz əst. U saəthaye xərab ra təmir mikonəd."
            ),
            "example_az": (
                "Verilən sözlər: SUBYEKT / PEŞƏ / TƏMİR ETDİYİ ƏŞYA.\n"
                "Quruluş: SUBYEKT + PEŞƏ + است. + او + ƏŞYA(cəm) + یِ خراب + را + تعمیر می‌کند.\n"
                "Yaşıl «خراب» — xarab, sınıq; qarşılığı «سالم» — saz, bütöv.\n"
                "Qırmızı «تعمیر کردن» — təmir etmək.\n"
                "Peşə adları «-ساز» (düzəldən) və «تعمیرکار» (təmirçi) ilə düzəlir: ساعت‌ساز، تعمیرکار ماشین.\n"
                "Tərcümə: Babam saatsazdır. O, xarab saatları təmir edir."
            ),
            "items": [
                {"fa": "برادرمان / نجّار / صندلی", "reading_az": "Bəradəreman / nəccar / səndəli", "az": "qardaşımız / dülgər / stul",
                 "sample_answer_fa": "برادرمان نجّار است. او صندلی‌های خراب را تعمیر می‌کند.",
                 "sample_answer_reading_az": "Bəradəreman nəccar əst. U səndəlihaye xərab ra təmir mikonəd.",
                 "sample_answer_az": "Qardaşımız dülgərdir. O, xarab stulları təmir edir."},
                {"fa": "خواهرزاده‌ام / مهندس رایانه / رایانه", "reading_az": "Xahərzadeəm / mohəndese rayane / rayane", "az": "bacım oğlu / kompüter mühəndisi / kompüter",
                 "sample_answer_fa": "خواهرزاده‌ام مهندس رایانه است. او رایانه‌های خراب را تعمیر می‌کند.",
                 "sample_answer_reading_az": "Xahərzadeəm mohəndese rayane əst. U rayanehaye xərab ra təmir mikonəd.",
                 "sample_answer_az": "Bacımın oğlu kompüter mühəndisidir. O, xarab kompüterləri təmir edir."},
                {"fa": "دوستم / آهنگر / در و پنجره", "reading_az": "Dustəm / ahəngər / dər o pəncəre", "az": "dostum / dəmirçi / qapı-pəncərə",
                 "sample_answer_fa": "دوستم آهنگر است. او در و پنجره‌های خراب را تعمیر می‌کند.",
                 "sample_answer_reading_az": "Dustəm ahəngər əst. U dər o pəncərehaye xərab ra təmir mikonəd.",
                 "sample_answer_az": "Dostum dəmirçidir. O, xarab qapı-pəncərələri təmir edir."},
                {"fa": "عموی سعید / تعمیرکار ماشین / ماشین", "reading_az": "Əmuye Səid / təmirkare maşin / maşin", "az": "Səidin əmisi / maşın təmirçisi / maşın",
                 "sample_answer_fa": "عموی سعید تعمیرکار ماشین است. او ماشین‌های خراب را تعمیر می‌کند.",
                 "sample_answer_reading_az": "Əmuye Səid təmirkare maşin əst. U maşinhaye xərab ra təmir mikonəd.",
                 "sample_answer_az": "Səidin əmisi maşın təmirçisidir. O, xarab maşınları təmir edir."},
                {"fa": "حامد / تعمیرکار تلفن / تلفن", "reading_az": "Hamed / təmirkare telefon / telefon", "az": "Hamid / telefon təmirçisi / telefon",
                 "sample_answer_fa": "حامد تعمیرکار تلفن است. او تلفن‌های خراب را تعمیر می‌کند.",
                 "sample_answer_reading_az": "Hamed təmirkare telefon əst. U telefonhaye xərab ra təmir mikonəd.",
                 "sample_answer_az": "Hamid telefon təmirçisidir. O, xarab telefonları təmir edir."},
                {"fa": "هادی / دوچرخه‌ساز / دوچرخه", "reading_az": "Hadi / doçərxesaz / doçərxe", "az": "Hadi / velosiped ustası / velosiped",
                 "sample_answer_fa": "هادی دوچرخه‌ساز است. او دوچرخه‌های خراب را تعمیر می‌کند.",
                 "sample_answer_reading_az": "Hadi doçərxesaz əst. U doçərxehaye xərab ra təmir mikonəd.",
                 "sample_answer_az": "Hadi velosiped ustasıdır. O, xarab velosipedləri təmir edir."},
            ],
        },
        {
            # Çalışma 7 — səh. 182 «کامل کنید» (saat lüğəti).
            # Dərslikdə bəzi cümlələrdə iki boşluq var, ona görə multi_blank.
            "kind": "multi_blank",
            "title_fa": "کامل کنید",
            "instruction_az": "Söz bankından uyğun sözlərlə tamamlayın (bəzi cümlələrdə iki boşluq var)",
            "example_fa": "آن ساعت دیواری ___ نیست، ___ است.\nآن ساعت دیواری *سالم* نیست، **خراب** است.",
            "example_reading_az": "An saəte divari salem nist, xərab əst.",
            "example_az": (
                "O divar saatı saz deyil, xarabdır.\n"
                "Yaşıl «سالم» — saz, işlək; qırmızı «خراب» — xarab, sınıq. Bu iki söz antonimdir.\n"
                "Peşə və yer adları: ساعت‌ساز (usta) — ساعت‌سازی (emalatxana) — ساعت‌فروشی (mağaza)."
            ),
            # 8 boşluq = 8 çip.
            "word_bank": [
                "سالم", "خراب", "ساعت‌ساز", "تعمیر",
                "ساعت‌فروشی", "مچی", "تعمیر", "ساعت‌سازی",
            ],
            "items": [
                {
                    "fa_with_blanks": "آن ساعت دیواری ___ نیست، ___ است.",
                    "correct_answers": ["سالم", "خراب"],
                    "full_reading_az": "An saəte divari salem nist, xərab əst.",
                    "full_translation_az": "O divar saatı saz deyil, xarabdır.",
                },
                {
                    "fa_with_blanks": "برادرم ___ است. او ساعت‌های خراب را ___ می‌کند.",
                    "correct_answers": ["ساعت‌ساز", "تعمیر"],
                    "full_reading_az": "Bəradərəm saətsaz əst. U saəthaye xərab ra təmir mikonəd.",
                    "full_translation_az": "Qardaşım saatsazdır. O, xarab saatları təmir edir.",
                },
                {
                    "fa_with_blanks": "من پریروز به ___ رفتم و برای فرزندم یک ساعتِ ___ خریدم.",
                    "correct_answers": ["ساعت‌فروشی", "مچی"],
                    "full_reading_az": "Mən pəriruz be saətforuşi rəftəm va bəraye fərzəndəm yek saəte moçi xəridəm.",
                    "full_translation_az": "Mən srağagün saat mağazasına getdim və övladım üçün bir qol saatı aldım.",
                },
                {
                    "fa_with_blanks": "ساعت پدرم، خراب است. من امروز ساعت ایشان را برای ___ به ___ می‌برم.",
                    "correct_answers": ["تعمیر", "ساعت‌سازی"],
                    "full_reading_az": "Saəte pedərəm, xərab əst. Mən emruz saəte işan ra bəraye təmir be saətsazi mibərəm.",
                    "full_translation_az": "Atamın saatı xarabdır. Mən bu gün onun saatını təmir üçün saat emalatxanasına aparıram.",
                },
            ],
        },
    ],
    "sentence_practice": {
        "listen_exercises": [
            {
                "items": [
                    {
                        "fa": "محسن ساعت‌فروش است. در ساعت‌فروشی او ساعت‌های گوناگونی وجود دارد.",
                        "reading_az": "Mohsen saətforuş əst. Dər saətforuşiye u saəthaye gunaguni vocud darəd.",
                        "az": "Möhsün saat satandır. Onun saat mağazasında müxtəlif saatlar var.",
                    },
                    {
                        "fa": "جواد ساعت‌ساز است. او در ساعت‌سازی عمویش، ساعت‌های خراب را تعمیر می‌کند.",
                        "reading_az": "Cəvad saətsaz əst. U dər saətsaziye əmuyəş, saəthaye xərab ra təmir mikonəd.",
                        "az": "Cavad saatsazdır. O, əmisinin saat təmiri emalatxanasında xarab saatları təmir edir.",
                    },
                    {
                        "fa": "در کلاس ما یک ساعت دیواری هست. ساعتِ کلاس ما سالم است، خراب نیست.",
                        "reading_az": "Dər kelase ma yek saəte divari həst. Saəte kelase ma salem əst, xərab nist.",
                        "az": "Bizim sinifdə bir divar saatı var. Sinfimizin saatı sağlamdır, xarab deyil.",
                    },
                    {
                        "fa": "در فصل زمستان، آفتاب حدود هفت صبح طلوع می‌کند و پنج بعدازظهر غروب می‌کند.",
                        "reading_az": "Dər fəsle zemestan, aftab hodude həft sobh toluu mikonəd va pənc bədəzzohr qorub mikonəd.",
                        "az": "Qış fəslində günəş təxminən səhər saat yeddidə doğur və günortadan sonra saat beşdə batır.",
                    },
                    {
                        "fa": "حمید هر شب ده می‌خوابد و ساعت پنج صبح بیدار می‌شود.",
                        "reading_az": "Həmid hər şəb dəh mixabəd va saəte pənc sobh bidar mişəvəd.",
                        "az": "Həmid hər gecə saat onda yatır və səhər saat beşdə oyanır.",
                    },
                    {
                        "fa": "فاطمه و نرگس در شبانه‌روز، چهارده ساعت درس می‌خوانند و شش ساعت می‌خوابند.",
                        "reading_az": "Fateme va Nərges dər şəbaneruz, çəhardəh saət dərs mixanənd va şeş saət mixabənd.",
                        "az": "Fatimə və Nərgiz sutkada on dörd saat dərs oxuyur və altı saat yatırlar.",
                    },
                    {
                        "fa": "من دیروز به ساعت‌فروشی پدرم رفتم. دو ساعت آن‌جا ماندم و به ایشان کمک کردم.",
                        "reading_az": "Mən diruz be saətforuşiye pedərəm rəftəm. Do saət anja mandəm va be işan komək kərdəm.",
                        "az": "Mən dünən atamın saat mağazasına getdim. Orada iki saat qaldım və ona kömək etdim.",
                    },
                    {
                        "fa": "پسرم علی، یک ساعت مچی دارد. عقربه‌ی دقیقه‌ی ساعتش و بند آن خراب است.",
                        "reading_az": "Pesərəm Əli, yek saəte moçi darəd. Əqrəbeye dəqiqeye saətəş va bənde an xərab əst.",
                        "az": "Oğlum Əlinin bir qol saatı var. Saatının dəqiqə əqrəbi və qayışı xarabdır.",
                    },
                    {
                        "fa": "برادرم هادی، تعمیرکار یخچال است. او یخچال‌های خراب را تعمیر می‌کند.",
                        "reading_az": "Bəradərəm Hadi, təmirkare yəxçal əst. U yəxçalhaye xərab ra təmir mikonəd.",
                        "az": "Qardaşım Hadi soyuducu təmirçisidir. O, xarab soyuducuları təmir edir.",
                    },
                    {
                        "fa": "ما دیشب سرشب خوابیدیم و سحر بیدار شدیم.",
                        "reading_az": "Ma dişəb sərşəb xabidim va səhər bidar şodim.",
                        "az": "Biz dünən gecə axşamüstü yatdıq və dan yerində oyandıq.",
                    },
                ],
            },
        ],
        "answer_items": [],
    },
    "reading_text": {
        "title_fa": "ساعت‌سازی ناصر",
        "title_az": "Nasirin saat təmiri emalatxanası",
        "paragraphs_fa": [
            "اسم این آقا، ناصر است و نام خانوادگی او مهدوی است. او ساعت‌ساز است و یک مغازه‌ی ساعت‌سازی‌اش دارد. او در ساعت‌سازی‌اش، ساعت هم می‌فروشد. ساعت‌سازی او در خیابان هفده شهریور، بین میدان امام حسین (ع) و میدان شهدا، سرِ چهارراه امین، کنار بانک ملّی، پلاک ۱۱۴ است.",
            "فاصله‌ی خانه‌ی آقای مهدوی تا مغازه‌اش حدود پانصد متر است. او هر روز ساعت هفت و نیم صبح پیاده به مغازه‌اش می‌رود و تا حدود ظهر در ساعت‌سازی می‌ماند و ساعت‌های خراب را تعمیر می‌کند. ایشان هنگام ظهر، مغازه‌اش را تعطیل می‌کند؛ وضو می‌گیرد و برای خواندن نماز به مسجد می‌رود. او پس از نماز، خوردن ناهار و استراحت‌کردن به خانه برمی‌گردد و ساعت چهار بعدازظهر دوباره به مغازه می‌آید و تا ساعت نه شب کار می‌کند.",
            "آقا ناصر بسیار خوش‌اخلاق است؛ به این سبب مشتری‌های او زیاد هستند و همه او را دوست دارند.",
            "او یک شاگرد هم دارد. اسم شاگردش رضا است. رضا از صبح تا ظهر در دانش‌گاه درس می‌خواند و بعدازظهرها سرِ ساعت پنج به ساعت‌سازی آقا ناصر می‌رود و در تعمیر ساعت‌ها به ایشان کمک می‌کند. دیروز دوست رضا ساعتش را برای تعمیر به او داد. رضا ساعت دوستش را به ساعت‌سازی برد و برایش تعمیر کرد.",
        ],
        "footnotes": [
            {"fa": "نام خانوادگی", "az": "soyad"},
            {"fa": "فاصله", "az": "məsafə"},
            {"fa": "سرِ ساعت", "az": "vaxtında (dəqiq saatında)"},
            {"fa": "خوش‌اخلاق", "az": "xoşrəftar"},
        ],
        "full_translation_az": (
            "Bu kişinin adı Nasirdir və soyadı Mehdəvidir. O, saatsazdır və özünün saat təmiri emalatxanası var. "
            "O, emalatxanasında saat da satır. Onun emalatxanası On yeddi Şəhrivər küçəsində, İmam Hüseyn (ə) "
            "meydanı ilə Şühəda meydanı arasında, Əmin dördyol ayrıcının başında, Milli Bankın yanında, 114 "
            "nömrəli binadadır.\n\n"
            "Cənab Mehdəvinin evindən emalatxanasına qədər olan məsafə təxminən beş yüz metrdir. O, hər gün "
            "səhər saat yeddi yarımda piyada emalatxanasına gedir və günortaya qədər orada qalıb xarab saatları "
            "təmir edir. O, günorta vaxtı dükanını bağlayır, dəstamaz alır və namaz qılmaq üçün məscidə gedir. "
            "Namazdan, nahar yeməkdən və istirahət etməkdən sonra evinə qayıdır və günortadan sonra saat dörddə "
            "yenidən dükana gəlib gecə saat doqquza qədər işləyir.\n\n"
            "Ağa Nasir çox xoşrəftardır; buna görə müştəriləri çoxdur və hamı onu sevir.\n\n"
            "Onun bir şagirdi də var. Şagirdinin adı Rzadır. Rza səhərdən günortaya qədər universitetdə oxuyur "
            "və günortadan sonra saat beşdə dəqiq Ağa Nasirin emalatxanasına gedib saatların təmirində ona kömək "
            "edir. Dünən Rzanın dostu saatını təmir üçün ona verdi. Rza dostunun saatını emalatxanaya apardı və "
            "onun üçün təmir etdi."
        ),
        "sentences": [
            {
                "fa": "اسم این آقا، ناصر است و نام خانوادگی او مهدوی است.",
                "reading_az": "Esme in ağa, Naser əst va name xanevadegiye u Mehdəvi əst.",
                "az": "Bu kişinin adı Nasirdir və soyadı Mehdəvidir.",
                "new_paragraph": True,
            },
            {"fa": "او ساعت‌ساز است و یک مغازه‌ی ساعت‌سازی‌اش دارد.", "reading_az": "U saətsaz əst va yek məğazeye saətsaziəş darəd.", "az": "O, saatsazdır və özünün saat təmiri emalatxanası var."},
            {"fa": "او در ساعت‌سازی‌اش، ساعت هم می‌فروشد.", "reading_az": "U dər saətsaziəş, saət həm miforuşəd.", "az": "O, emalatxanasında saat da satır."},
            {
                "fa": "ساعت‌سازی او در خیابان هفده شهریور، بین میدان امام حسین (ع) و میدان شهدا، سرِ چهارراه امین، کنار بانک ملّی، پلاک ۱۱۴ است.",
                "reading_az": "Saətsaziye u dər xiyabane hefdəh Şəhrivər, beyne meydane Emam Hoseyn va meydane Şohəda, səre çəharrahe Əmin, kənare banke Melli, pelake sədo çəhardəh əst.",
                "az": "Onun emalatxanası On yeddi Şəhrivər küçəsində, İmam Hüseyn (ə) meydanı ilə Şühəda meydanı arasında, Əmin dördyol ayrıcının başında, Milli Bankın yanında, 114 nömrəli binadadır.",
            },
            {
                "fa": "فاصله‌ی خانه‌ی آقای مهدوی تا مغازه‌اش حدود پانصد متر است.",
                "reading_az": "Faseleye xaneye ağaye Mehdəvi ta məğazeəş hodude pansəd metr əst.",
                "az": "Cənab Mehdəvinin evindən emalatxanasına qədər olan məsafə təxminən beş yüz metrdir.",
                "new_paragraph": True,
            },
            {
                "fa": "او هر روز ساعت هفت و نیم صبح پیاده به مغازه‌اش می‌رود و تا حدود ظهر در ساعت‌سازی می‌ماند و ساعت‌های خراب را تعمیر می‌کند.",
                "reading_az": "U hər ruz saəte həft o nim sobh piyade be məğazeəş mirəvəd va ta hodude zohr dər saətsazi mimanəd va saəthaye xərab ra təmir mikonəd.",
                "az": "O, hər gün səhər saat yeddi yarımda piyada emalatxanasına gedir və günortaya qədər orada qalıb xarab saatları təmir edir.",
            },
            {
                "fa": "ایشان هنگام ظهر، مغازه‌اش را تعطیل می‌کند؛ وضو می‌گیرد و برای خواندن نماز به مسجد می‌رود.",
                "reading_az": "İşan hengame zohr, məğazeəş ra tətil mikonəd; vozu migirəd va bəraye xandəne nəmaz be məsced mirəvəd.",
                "az": "O, günorta vaxtı dükanını bağlayır, dəstamaz alır və namaz qılmaq üçün məscidə gedir.",
            },
            {
                "fa": "او پس از نماز، خوردن ناهار و استراحت‌کردن به خانه برمی‌گردد و ساعت چهار بعدازظهر دوباره به مغازه می‌آید و تا ساعت نه شب کار می‌کند.",
                "reading_az": "U pəs əz nəmaz, xordəne nahar va esterahət-kərdən be xane bərmigərdəd va saəte çəhar bədəzzohr dobare be məğaze miayəd va ta saəte noh şəb kar mikonəd.",
                "az": "Namazdan, nahar yeməkdən və istirahət etməkdən sonra evinə qayıdır və günortadan sonra saat dörddə yenidən dükana gəlib gecə saat doqquza qədər işləyir.",
            },
            {
                "fa": "آقا ناصر بسیار خوش‌اخلاق است؛ به این سبب مشتری‌های او زیاد هستند و همه او را دوست دارند.",
                "reading_az": "Ağa Naser besyar xoşəxlaq əst; be in səbəb moştərihaye u ziyad həstənd va həme u ra dust darənd.",
                "az": "Ağa Nasir çox xoşrəftardır; buna görə müştəriləri çoxdur və hamı onu sevir.",
                "new_paragraph": True,
            },
            {
                "fa": "او یک شاگرد هم دارد.",
                "reading_az": "U yek şagerd həm darəd.",
                "az": "Onun bir şagirdi də var.",
                "new_paragraph": True,
            },
            {"fa": "اسم شاگردش رضا است.", "reading_az": "Esme şagerdəş Reza əst.", "az": "Şagirdinin adı Rzadır."},
            {
                "fa": "رضا از صبح تا ظهر در دانش‌گاه درس می‌خواند و بعدازظهرها سرِ ساعت پنج به ساعت‌سازی آقا ناصر می‌رود و در تعمیر ساعت‌ها به ایشان کمک می‌کند.",
                "reading_az": "Reza əz sobh ta zohr dər daneşgah dərs mixanəd va bədəzzohrha səre saəte pənc be saətsaziye ağa Naser mirəvəd va dər təmire saətha be işan komək mikonəd.",
                "az": "Rza səhərdən günortaya qədər universitetdə oxuyur və günortadan sonra saat beşdə dəqiq Ağa Nasirin emalatxanasına gedib saatların təmirində ona kömək edir.",
            },
            {"fa": "دیروز دوست رضا ساعتش را برای تعمیر به او داد.", "reading_az": "Diruz duste Reza saətəş ra bəraye təmir be u dad.", "az": "Dünən Rzanın dostu saatını təmir üçün ona verdi."},
            {"fa": "رضا ساعت دوستش را به ساعت‌سازی برد و برایش تعمیر کرد.", "reading_az": "Reza saəte dustəş ra be saətsazi bord va bərayəş təmir kərd.", "az": "Rza dostunun saatını emalatxanaya apardı və onun üçün təmir etdi."},
        ],
        "comprehension_questions": [
            {
                "question_fa": "نام خانوادگی ناصر چیست؟",
                "reading_az": "Name xanevadegiye Naser çist?",
                "az": "Nasirin soyadı nədir?",
                "sample_answer_fa": "نام خانوادگی ناصر، مهدوی است.",
                "sample_answer_reading_az": "Name xanevadegiye Naser, Mehdəvi əst.",
                "sample_answer_az": "Nasirin soyadı Mehdəvidir.",
            },
            {
                "question_fa": "ناصر چه‌کاره است و کجا کار می‌کند؟",
                "reading_az": "Naser çekare əst va koca kar mikonəd?",
                "az": "Nasir nə iş görür və harada işləyir?",
                "sample_answer_fa": "ناصر ساعت‌ساز است و در مغازه‌ی ساعت‌سازی خودش کار می‌کند.",
                "sample_answer_reading_az": "Naser saətsaz əst va dər məğazeye saətsaziye xodəş kar mikonəd.",
                "sample_answer_az": "Nasir saatsazdır və öz saat təmiri emalatxanasında işləyir.",
            },
            {
                "question_fa": "به چه سبب مشتری‌های آقا ناصر زیاد هستند؟",
                "reading_az": "Be çe səbəb moştərihaye ağa Naser ziyad həstənd?",
                "az": "Ağa Nasirin nə üçün çoxlu müştərisi var?",
                "sample_answer_fa": "چون آقا ناصر بسیار خوش‌اخلاق است، مشتری‌های او زیاد هستند.",
                "sample_answer_reading_az": "Çon ağa Naser besyar xoşəxlaq əst, moştərihaye u ziyad həstənd.",
                "sample_answer_az": "Çünki Ağa Nasir çox xoşrəftardır, ona görə çoxlu müştərisi var.",
            },
            {
                "question_fa": "آقای مهدوی صبح‌ها با چه چیزی به مغازه‌اش می‌رود؟",
                "reading_az": "Ağaye Mehdəvi sobhha ba çe çizi be məğazeəş mirəvəd?",
                "az": "Cənab Mehdəvi səhərlər mağazasına necə gedir?",
                "sample_answer_fa": "آقای مهدوی صبح‌ها پیاده به مغازه‌اش می‌رود.",
                "sample_answer_reading_az": "Ağaye Mehdəvi sobhha piyade be məğazeəş mirəvəd.",
                "sample_answer_az": "Cənab Mehdəvi səhərlər mağazasına piyada gedir.",
            },
            {
                "question_fa": "رضا ساعت چه‌کسی را برای تعمیر به ساعت‌سازی برد؟",
                "reading_az": "Reza saəte çekəsi ra bəraye təmir be saətsazi bord?",
                "az": "Rza kimin saatını təmir üçün emalatxanaya apardı?",
                "sample_answer_fa": "رضا ساعت دوستش را برای تعمیر به ساعت‌سازی برد.",
                "sample_answer_reading_az": "Reza saəte dustəş ra bəraye təmir be saətsazi bord.",
                "sample_answer_az": "Rza dostunun saatını təmir üçün emalatxanaya apardı.",
            },
            {
                "question_fa": "آقا ناصر چه وقت برای استراحت‌کردن به خانه برمی‌گردد؟",
                "reading_az": "Ağa Naser çe vaqt bəraye esterahət-kərdən be xane bərmigərdəd?",
                "az": "Ağa Nasir istirahət etmək üçün nə vaxt evə qayıdır?",
                "sample_answer_fa": "او پس از نماز و خوردن ناهار، هنگام ظهر برای استراحت‌کردن به خانه برمی‌گردد.",
                "sample_answer_reading_az": "U pəs əz nəmaz va xordəne nahar, hengame zohr bəraye esterahət-kərdən be xane bərmigərdəd.",
                "sample_answer_az": "O, namazdan və nahar yeməkdən sonra, günorta vaxtı istirahət etmək üçün evə qayıdır.",
            },
        ],
    },
}
