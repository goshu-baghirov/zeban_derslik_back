# Dərs 18 — انسان و اعضای بدن (İnsan və bədən üzvləri)
# Mənbə: کتاب دوم, səh. 219-230

LESSON = {
    "number": 18,
    "title_fa": "انسان و اعضای بدن",
    "title_az": "İnsan və bədən üzvləri",
    "available": True,
    "vocabulary": [
        {"fa": "مهربان", "reading": "mehrəban", "az": "Mehriban"},
        {"fa": "نامهربان", "reading": "namehrəban", "az": "Namahriban, qəddar"},
        {"fa": "متواضع", "reading": "motəvaze", "az": "Təvazokar"},
        {"fa": "متکبّر", "reading": "motəkəbbər", "az": "Təkəbbürlü, məğrur"},
        {"fa": "احترام می‌گذارد", "reading": "ehteram migəzarəd", "az": "hörmət edir"},
        {"fa": "نابینا (کور)", "reading": "nabina (kur)", "az": "Gözdən əlil (kor)"},
        {"fa": "ناشنوا (کر)", "reading": "naşənva (kor)", "az": "Eşitmə əlili (kar)"},
        {"fa": "معلول", "reading": "mə'lul", "az": "Əlil, fiziki məhdudiyyətli"},
        {"fa": "بغل می‌کند", "reading": "bəğəl mikonəd", "az": "qucaqlayır"},
        {"fa": "نوازش می‌کند", "reading": "nəvazəş mikonəd", "az": "sığallayır, əzizləyir"},
        {"fa": "می‌بوسد", "reading": "mibusəd", "az": "öpür"},
        {"fa": "صحبت می‌کند", "reading": "sohbət mikonəd", "az": "danışır, söhbət edir"},
        {"fa": "به دنیا می‌آید", "reading": "be donya miayəd", "az": "dünyaya gəlir (doğulur)"},
        {"fa": "از دنیا می‌رود", "reading": "əz donya mirəvəd", "az": "dünyasını dəyişir (vəfat edir)"},
        {"fa": "نوزاد", "reading": "nouzad", "az": "Körpə, yeni doğulmuş uşaq"},
        {"fa": "سر", "reading": "sər", "az": "Baş"},
        {"fa": "صورت", "reading": "surət", "az": "Üz, sifət"},
        {"fa": "مغز", "reading": "məğz", "az": "Beyin"},
        {"fa": "مو", "reading": "mu", "az": "Saç"},
        {"fa": "پیشانی", "reading": "pişani", "az": "Alın"},
        {"fa": "چشم", "reading": "çeşm", "az": "Göz"},
        {"fa": "مژه", "reading": "moje", "az": "Kirpik"},
        {"fa": "گوش", "reading": "guş", "az": "Qulaq"},
        {"fa": "بینی (دماغ)", "reading": "bini (dəmağ)", "az": "Burun"},
        {"fa": "ریش", "reading": "riş", "az": "Saqqal"},
        {"fa": "گردن", "reading": "gərdən", "az": "Boğaz, boyun"},
        {"fa": "ابرو", "reading": "əbru", "az": "Qaş"},
        {"fa": "پلک", "reading": "pelk", "az": "Qapaq (göz qapağı)"},
        {"fa": "گونه (لُپ)", "reading": "gune (lop)", "az": "Yanaq"},
        {"fa": "سبیل", "reading": "sebil", "az": "Bığ"},
        {"fa": "چانه", "reading": "çane", "az": "Çənə"},
        {"fa": "دهان", "reading": "dəhan", "az": "Ağız"},
        {"fa": "لثه", "reading": "ləse", "az": "Damaq"},
        {"fa": "دندان", "reading": "dəndan", "az": "Diş"},
        {"fa": "زبان", "reading": "zəban", "az": "Dil"},
        {"fa": "لب", "reading": "ləb", "az": "Dodaq"},
        {"fa": "دست", "reading": "dəst", "az": "Əl"},
        {"fa": "ناخن", "reading": "naxon", "az": "Dırnaq"},
        {"fa": "رگ", "reading": "rəg", "az": "Damar"},
        {"fa": "کف دست", "reading": "kəfe dəst", "az": "Əlin içi (ovuc)"},
        {"fa": "ساعد", "reading": "saed", "az": "Qolun alt hissəsi (biləklə dirsək arası)"},
        {"fa": "شکم", "reading": "şekəm", "az": "Qarın"},
        {"fa": "ناف", "reading": "naf", "az": "Göbək"},
        {"fa": "شانه (کتف)", "reading": "şane (ketf)", "az": "Çiyin"},
        {"fa": "سینه", "reading": "sine", "az": "Sinə"},
        {"fa": "بازو", "reading": "bazu", "az": "Qol (bazu)"},
        {"fa": "آرنج", "reading": "arənc", "az": "Dirsək"},
        {"fa": "مچ", "reading": "moç", "az": "Bilək"},
        {"fa": "انگشت", "reading": "əngoşt", "az": "Barmaq"},
        {"fa": "ماهیچه (عضله)", "reading": "mahiçe (əzəle)", "az": "Əzələ"},
        {"fa": "استخوان", "reading": "ostoxan", "az": "Sümük"},
        {"fa": "قلب", "reading": "qəlb", "az": "Ürək"},
        {"fa": "پوست", "reading": "pust", "az": "Dəri"},
        {"fa": "اسکلت", "reading": "eskelet", "az": "Skelet"},
        {"fa": "کمر", "reading": "kəmər", "az": "Bel"},
        {"fa": "پهلو", "reading": "pəhlu", "az": "Böyür, yan"},
        {"fa": "ران", "reading": "ran", "az": "Bud"},
        {"fa": "باسن", "reading": "basən", "az": "Sağrı, arxa"},
        {"fa": "زانو", "reading": "zanu", "az": "Diz"},
        {"fa": "ساق", "reading": "saq", "az": "Baldır"},
        {"fa": "پاشنه", "reading": "paşne", "az": "Daban"},
        {"fa": "پا", "reading": "pa", "az": "Ayaq"},
        {"fa": "کف پا", "reading": "kəfe pa", "az": "Ayağın altı (daban-ovuc)"},
        {"fa": "مچ پا", "reading": "moçe pa", "az": "Topuq (ayaq biləyi)"},
        {"fa": "قفسه‌ی سینه", "reading": "qəfəseye sine", "az": "Döş qəfəsi"},
        {"fa": "ستون فقرات", "reading": "sotune fəqərat", "az": "Onurğa sütunu"},
        {"fa": "کلیه", "reading": "kolye", "az": "Böyrək"},
        {"fa": "حلق", "reading": "həlq", "az": "Boğaz, udlaq"},
        {"fa": "معده", "reading": "moede", "az": "Mədə"},
        {"fa": "کبد (جگر)", "reading": "kəbed (jegər)", "az": "Qaraciyər"},
        {"fa": "روده‌ی بزرگ", "reading": "rudeye bozorg", "az": "Yoğun bağırsaq"},
        {"fa": "روده‌ی کوچک", "reading": "rudeye kuçək", "az": "Nazik bağırsaq"},
        {"fa": "دست / دسته", "reading": "dəst / dəste", "az": "Əl / Qulp, dəstək"},
        {"fa": "پا / پایه", "reading": "pa / paye", "az": "Ayaq / Dayaq, qıç (stul və s.)"},
        {"fa": "چشم / چشمه", "reading": "çeşm / çeşme", "az": "Göz / Bulaq"},
        {"fa": "دندان / دندانه", "reading": "dəndan / dəndane", "az": "Diş / Dişcik (hərflərdə, daraqda)"},
        {"fa": "ریش / ریشه", "reading": "riş / rişe", "az": "Saqqal / Kök (ağac kökü)"},
        {"fa": "شاخ / شاخه", "reading": "şax / şaxe", "az": "Buynuz / Budaq (ağac budağı)"},
        {"fa": "مالِ", "reading": "male", "az": "...-ın, ...-in (sahiblik ifadəsi)"},
        # Səh. 219 «واژه‌ها» siyahısındakı, əvvəl faylda çatışmayan sözlər.
        {"fa": "قسمت", "reading": "qesmət", "az": "Hissə, bölmə"},
        {"fa": "محکم", "reading": "mohkəm", "az": "Möhkəm"},
        {"fa": "بهتر", "reading": "behtər", "az": "Daha yaxşı"},
        {"fa": "طعم و مزه", "reading": "tə'm-o-məze", "az": "Dad və ləzzət"},
        {"fa": "شور", "reading": "şur", "az": "Şor (duzlu)"},
        {"fa": "تند", "reading": "tond", "az": "Acı (istiotlu) / sürətli"},
        {"fa": "ترش", "reading": "torş", "az": "Turş"},
        {"fa": "شیرین", "reading": "şirin", "az": "Şirin"},
        {"fa": "احساس می‌کند", "reading": "ehsas mikonəd", "az": "hiss edir"},
        {"fa": "حس می‌کند", "reading": "hes mikonəd", "az": "hiss edir (eyni məna)"},
        {"fa": "نفس می‌کشد", "reading": "nəfəs mikeşəd", "az": "nəfəs alır"},
        {"fa": "حرف می‌زند", "reading": "hərf mizənəd", "az": "danışır"},
        {"fa": "راه می‌رود", "reading": "rah mirəvəd", "az": "yeriyir, gəzir"},
        {"fa": "شانه می‌زند (شانه می‌کند)", "reading": "şane mizənəd (şane mikonəd)", "az": "darayır"},
        {"fa": "کوتاه می‌کند", "reading": "kutah mikonəd", "az": "qısaldır"},
        # Səh. 228-229 oxu mətnindəki sözlər.
        {"fa": "گوشت", "reading": "quşt", "az": "Ət"},
        {"fa": "خون", "reading": "xun", "az": "Qan"},
        {"fa": "برخی (بعضی)", "reading": "bərxi (bə'zi)", "az": "Bəzi, bir qismi"},
        {"fa": "به وسیله‌ی (با)", "reading": "be vəsileye (ba)", "az": "…vasitəsilə, ilə"},
        {"fa": "گوناگون", "reading": "qunagun", "az": "Müxtəlif, rəngarəng"},
        {"fa": "زردپوست", "reading": "zərdpust", "az": "Sarıdərili"},
        {"fa": "سیاه‌پوست", "reading": "siyahpust", "az": "Qaradərili"},
        {"fa": "سرخ‌پوست", "reading": "sorxpust", "az": "Qırmızıdərili"},
        {"fa": "سفیدپوست", "reading": "sefidpust", "az": "Ağdərili"},
        {"fa": "زبری", "reading": "zebri", "az": "Kobudluq, sərtlik"},
        {"fa": "نرمی", "reading": "nərmi", "az": "Yumşaqlıq"},
        {"fa": "گرمی / سردی", "reading": "gərmi / sərdi", "az": "İstilik / soyuqluq"},
        {"fa": "ضعیف", "reading": "zəif", "az": "Zəif"},
        {"fa": "عصا", "reading": "əsa", "az": "Əsa (dəyənək)"},
        {"fa": "آرایشگاه", "reading": "arayeşgah", "az": "Bərbərxana, gözəllik salonu"},
        {"fa": "مسواک می‌زند", "reading": "mesvak mizənəd", "az": "diş fırçalayır"},
    ],
    "grammar_notes": [
        {
            "title_az": "İnsan bədən üzvləri və fərqli mənalar: «دست، دسته / پا، پایه / چشم، چشمه...»",
            "title_fa": "دست، دسته و...",
            "explanation_az": (
                "Fars dilində bəzi sözlərin sonuna «ـه» şəkilçisi əlavə etdikdə bədən üzvünün adı əşya və ya təbiət anlayışına çevrilir:\n"
                "1. دست (əl - bədən üzvü) → دسته (qulp, dəstək): پارچ و سطل دسته دارند.\n"
                "2. پا (ayaq - bədən üzvü) → پایه (dayaq, stul qıçı): این صندلی چهار پایه دارد.\n"
                "3. چشم (göz - bədən üzvü) → چشمه (bulaq): در کوه و جنگل چشمه وجود دارد.\n"
                "4. دندان (diş - bədən üzvü) → دندانه (dişcik): حرف «س» سه دندانه دارد.\n"
                "5. ریش (saqqal - bədən üzvü) → ریشه (kök): درخت ریشه دارد.\n"
                "6. شاخ (buynuz - heyvan bədəni) → شاخه (budaq): درخت شاخه دارد."
            ),
            "note_fa": (
                "دست ← انسان دو دست دارد. / دسته ← پارچ و سطل دسته دارند.\n"
                "پا ← ما دو پا داریم. / پایه ← این صندلی چهار پایه دارد.\n"
                "چشم ← انسان چشم دارد. / چشمه ← در کوه چشمه وجود دارد.\n"
                "دندان ← این دندان است. / دندانه ← حرف «س» سه دندانه دارد.\n"
                "ریش ← این مرد ریش دارد. / ریشه ← درخت ریشه دارد.\n"
                "شاخ ← گاو شاخ دارد. / شاخه ← درخت شاخه دارد."
            ),
            "note_reading_az": (
                "Dəst ← Ensan do dəst darəd. / Dəste ← Parç va sətl dəste darənd.\n"
                "Pa ← Ma do pa darim. / Paye ← In səndəli çəhar paye darəd.\n"
                "Çeşm ← Ensan çeşm darəd. / Çeşme ← Dər kuh çeşme vocud darəd.\n"
                "Dəndan ← In dəndan əst. / Dəndane ← Hərfe «se» se dəndane darəd.\n"
                "Riş ← In mərd riş darəd. / Rişe ← Dərəxt rişe darəd.\n"
                "Şax ← Gav şax darəd. / Şaxe ← Dərəxt şaxe darəd."
            ),
            "note_az": (
                "Bədən üzvü adı + «ـه» = Əşya və ya təbiət obyekti:\n"
                "• دست (əl) → دسته (qulp)\n"
                "• پا (ayaq) → پایه (stul ayağı)\n"
                "• چشم (göz) → چشمه (bulaq)\n"
                "• دندان (diş) → دندانه (hərf dişi)\n"
                "• ریش (saqqal) → ریشه (ağac kökü)\n"
                "• شاخ (buynuz) → شاخه (ağac budağı)"
            ),
            "conjugations": [
                {"pronoun_fa": "دست (Əl)", "form_fa": "دسته (Qulp)"},
                {"pronoun_fa": "پا (Ayaq)", "form_fa": "پایه (Dayaq/Stul qıçı)"},
                {"pronoun_fa": "چشم (Göz)", "form_fa": "چشمه (Bulaq)"},
                {"pronoun_fa": "دندان (Diş)", "form_fa": "دندانه (Dişcik)"},
                {"pronoun_fa": "ریش (Saqqal)", "form_fa": "ریشه (Kök)"},
                {"pronoun_fa": "شاخ (Buynuz)", "form_fa": "شاخه (Budaq)"},
            ],
            "examples": [
                {
                    "fa": "انسان دو دست دارد و پارچ و سطل دسته دارند.",
                    "reading_az": "Ensan do dəst darəd va parç va sətl dəste darənd.",
                    "az": "İnsanın iki əli var, dolça və vedrənin isə qulpu var.",
                },
                {
                    "fa": "ما دو پا داریم و این صندلی، چهار پایه دارد.",
                    "reading_az": "Ma do pa darim va in səndəli, çəhar paye darəd.",
                    "az": "Bizim iki ayağımız var, bu stulun isə dörd ayağı (dayağı) var.",
                },
                {
                    "fa": "انسان‌ها و حیوان‌ها چشم دارند و در کوه و جنگل چشمه وجود دارد.",
                    "reading_az": "Ensanha va heyvanha çeşm darənd va dər kuh va cəngəl çeşme vocud darəd.",
                    "az": "İnsanların və heyvanların gözü var, dağda və meşədə isə bulaq var.",
                },
                {
                    "fa": "این دندان است و حرف «س» سه دندانه دارد.",
                    "reading_az": "In dəndan əst va hərfe «se» se dəndane darəd.",
                    "az": "Bu dişdir və «s» hərfinin üç dişi (dəndanəsi) var.",
                },
                {
                    "fa": "این مرد، ریش دارد و درخت، ریشه دارد.",
                    "reading_az": "In mərd, riş darəd va dərəxt, rişe darəd.",
                    "az": "Bu kişinin saqqalı var və ağacın kökü var.",
                },
                {
                    "fa": "گاو، شاخ دارد و درخت، شاخه دارد.",
                    "reading_az": "Gav, şax darəd va dərəxt, şaxe darəd.",
                    "az": "İnəyin buynuzu var, ağacın isə budaqları var.",
                },
            ],
        },
        {
            "title_az": "Sahiblik ifadəsi: «مالِ …» (kimindir? / aidiyyət)",
            "title_fa": "مالِ ........",
            "explanation_az": (
                "Fars dilində əşyanın kiməsə aid olduğunu (mənsubiyyəti) bildirmək üçün «مالِ» sözü işlənir.\n"
                "Quruluş: ƏŞYA + مالِ + SAHİBİ + است.\n"
                "Nümunə: این دوچرخه، مالِ من است (Bu velosiped mənimkidir / mənimdir).\n"
                "Sual vermək üçün «این ... مالِ کیست؟» (Bu ... kimindir?) quruluşundan istifadə olunur.\n"
                "Şifahi dildə (گفتار): «کیست» sözü «کیه» kimi deyilir (این عصا مال کیه؟)."
            ),
            "note_fa": (
                "من یک دوچرخه‌ی آبی دارم. ← این دوچرخه‌ی آبی، مالِ من است.\n"
                "سؤال: این عصا مالِ کیست؟ (گفتاری: این عصا مالِ کیه؟)\n"
                "پاسخ: این عصا مالِ پدربزرگم است."
            ),
            "note_reading_az": (
                "Mən yek doçərxe-ye abi daram. ← In doçərxe-ye abi, male mən əst.\n"
                "Soəl: In əsa male kist? (Goftari: In əsa male kiye?)\n"
                "Pasəx: In əsa male pedərbozorgəm əst."
            ),
            "note_az": (
                "Aidiyyət bildirən «مالِ» quruluşu:\n"
                "• این کتاب مالِ من است (Bu kitab mənimdir).\n"
                "• این عینک مالِ کیست؟ (Bu eynək kimindir?)"
            ),
            "conjugations": [
                {"pronoun_fa": "مالِ من", "form_fa": "Mənim / Mənimki"},
                {"pronoun_fa": "مالِ تو", "form_fa": "Sənin / Səninki"},
                {"pronoun_fa": "مالِ او", "form_fa": "Onun / Onunla"},
                {"pronoun_fa": "مالِ برادرم", "form_fa": "Qardaşımınki"},
            ],
            "examples": [
                {
                    "fa": "این عینک، مالِ من است و آن عینک، مالِ برادرم صادق است.",
                    "reading_az": "In eyneke male mən əst va an eynek male bəradərəm Sadəq əst.",
                    "az": "Bu eynək mənimdir, o eynək isə qardaşım Sadiqingidir.",
                },
                {
                    "fa": "یکی از این دفترها مالِ خواهرم پروین است.",
                    "reading_az": "Yeki əz in dəftərha male xvahərəm Pərvin əst.",
                    "az": "Bu dəftərlərdən biri bacım Pərvininkidir.",
                },
                {
                    "fa": "این عصا مالِ کیست؟ این عصا مالِ پدربزرگم است.",
                    "reading_az": "In əsa male kist? In əsa male pedərbozorgəm əst.",
                    "az": "Bu əsa kimindir? Bu əsa babamındır.",
                },
                {
                    "fa": "آیا آن خانه‌ی زیبا مالِ عبّاس است؟ بله، آن خانه‌ی زیبا مالِ عبّاس است.",
                    "reading_az": "Aya an xaneye ziba male Əbbas əst? Bəle, an xaneye ziba male Əbbas əst.",
                    "az": "O gözəl ev Abbasındır? Bəli, o gözəl ev Abbasındır.",
                },
            ],
        },
        {
            # Səh. 221 səhifə altındakı təsrif cədvəli.
            "title_az": "İndiki zamanda təsrif: «بوسیدن»، «شنیدن»، «احترام گذاشتن»",
            "title_fa": "بوسیدن؛ شنیدن؛ احترام گذاشتن",
            "explanation_az": (
                "Bu dərsdə üç fel indiki zamanda (حال) altı şəxs üzrə təsrif olunur.\n"
                "Quruluş: می‌ + indiki zaman kökü + şəxs sonluğu.\n"
                "1. بوسیدن (öpmək) — kök «بوس»: می‌بوسم، می‌بوسی، می‌بوسد، می‌بوسیم، می‌بوسید، می‌بوسند.\n"
                "2. شنیدن (eşitmək) — kök «شنو»: می‌شنوم، می‌شنوی، می‌شنود، می‌شنویم، می‌شنوید، می‌شنوند.\n"
                "3. احترام گذاشتن (hörmət etmək) — mürəkkəb feldir; yalnız köməkçi hissə (گذاشتن → گذار) təsriflənir, "
                "ad hissəsi (احترام) dəyişmir: احترام می‌گذارم، احترام می‌گذاری، احترام می‌گذارد و s.\n"
                "Diqqət: «احترام گذاشتن» həmişə «به» ilə işlənir — به استادم احترام می‌گذارم.\n"
                "«بوسیدن» felinin əmr forması: ببوس (öp) / ببوسید (öpün)."
            ),
            "note_fa": (
                "بوسیدن: می‌بوسم؛ می‌بوسی؛ می‌بوسد؛ می‌بوسیم؛ می‌بوسید؛ می‌بوسند\n"
                "شنیدن: می‌شنوم؛ می‌شنوی؛ می‌شنود؛ می‌شنویم؛ می‌شنوید؛ می‌شنوند\n"
                "احترام گذاشتن: احترام می‌گذارم؛ احترام می‌گذاری؛ احترام می‌گذارد؛ احترام می‌گذاریم؛ احترام می‌گذارید؛ احترام می‌گذارند\n"
                "بوسیدن ← فعل امر: ببوس؛ ببوسید"
            ),
            "note_reading_az": (
                "Busidən: mibusəm; mibusi; mibusəd; mibusim; mibusid; mibusənd\n"
                "Şənidən: mişənəvəm; mişənəvi; mişənəvəd; mişənəvim; mişənəvid; mişənəvənd\n"
                "Ehteram gozaştən: ehteram migozarəm; ehteram migozari; ehteram migozarəd; "
                "ehteram migozarim; ehteram migozarid; ehteram migozarənd\n"
                "Busidən ← fe'le əmr: bebus; bebusid"
            ),
            "note_az": (
                "Üç felin indiki zaman təsrifi:\n"
                "• بوسیدن — öpmək\n"
                "• شنیدن — eşitmək\n"
                "• احترام گذاشتن — hörmət etmək (mürəkkəb fel)\n"
                "Əmr forması: ببوس (öp) / ببوسید (öpün)."
            ),
            "conjugations": [
                {"pronoun_fa": "من", "form_fa": "می‌بوسم / می‌شنوم / احترام می‌گذارم"},
                {"pronoun_fa": "تو", "form_fa": "می‌بوسی / می‌شنوی / احترام می‌گذاری"},
                {"pronoun_fa": "او", "form_fa": "می‌بوسد / می‌شنود / احترام می‌گذارد"},
                {"pronoun_fa": "ما", "form_fa": "می‌بوسیم / می‌شنویم / احترام می‌گذاریم"},
                {"pronoun_fa": "شما", "form_fa": "می‌بوسید / می‌شنوید / احترام می‌گذارید"},
                {"pronoun_fa": "آن‌ها", "form_fa": "می‌بوسند / می‌شنوند / احترام می‌گذارند"},
            ],
            "examples": [
                {
                    "fa": "من هر روز دست مادرم را می‌بوسم.",
                    "reading_az": "Mən hər ruz dəste madərəm ra mibusəm.",
                    "az": "Mən hər gün anamın əlini öpürəm.",
                },
                {
                    "fa": "ما با گوش‌هایمان صدای پرنده‌ها را می‌شنویم.",
                    "reading_az": "Ma ba guşhayeman sedaye pərəndeha ra mişənvim.",
                    "az": "Biz qulaqlarımızla quşların səsini eşidirik.",
                },
                {
                    "fa": "طلبه‌های این کلاس به استادهایشان احترام می‌گذارند.",
                    "reading_az": "Tələbehaye in kelas be ostadhayeşan ehteram migozarənd.",
                    "az": "Bu sinfin tələbələri müəllimlərinə hörmət edirlər.",
                },
                {
                    "fa": "روز مادر به دیدن مادرتان بروید و دست ایشان را ببوسید.",
                    "reading_az": "Ruze madər be didəne madərətan bərəvid va dəste işan ra bebusid.",
                    "az": "Analar günündə ananızın görüşünə gedin və onun əlini öpün.",
                },
            ],
        },
        {
            # Səh. 229 səhifə altındakı təsrif cədvəli.
            "title_az": "«حرف زدن» (danışmaq) felinin indiki zamanda təsrifi",
            "title_fa": "حرف زدن",
            "explanation_az": (
                "«حرف زدن» — mürəkkəb feldir: ad hissəsi «حرف» (söz) + fel hissəsi «زدن» (vurmaq).\n"
                "Yalnız fel hissəsi təsriflənir, «حرف» sözü dəyişməz qalır:\n"
                "حرف می‌زنم، حرف می‌زنی، حرف می‌زند، حرف می‌زنیم، حرف می‌زنید، حرف می‌زنند.\n"
                "Mənası «صحبت کردن» (söhbət etmək) ilə eynidir: با او حرف می‌زنم = با او صحبت می‌کنم.\n"
                "Kiminləsə danışmaq üçün «با» işlənir: با دوستم حرف می‌زنم.\n"
                "Nə ilə danışdığımızı bildirmək üçün də «با» işlənir: با زبان حرف می‌زنیم."
            ),
            "note_fa": (
                "حرف زدن: حرف می‌زنم؛ حرف می‌زنی؛ حرف می‌زند؛ حرف می‌زنیم؛ حرف می‌زنید؛ حرف می‌زنند\n"
                "به وسیله‌ی زبان حرف می‌زنیم. / با ....... حرف می‌زند."
            ),
            "note_reading_az": (
                "Hərf zədən: hərf mizənəm; hərf mizəni; hərf mizənəd; hərf mizənim; hərf mizənid; hərf mizənənd\n"
                "Be vəsileye zəban hərf mizənim. / Ba ....... hərf mizənəd."
            ),
            "note_az": (
                "«حرف زدن» = «صحبت کردن» (danışmaq).\n"
                "• با کسی حرف زدن — kiminləsə danışmaq\n"
                "• با زبان حرف زدن — dillə danışmaq"
            ),
            "conjugations": [
                {"pronoun_fa": "من", "form_fa": "حرف می‌زنم"},
                {"pronoun_fa": "تو", "form_fa": "حرف می‌زنی"},
                {"pronoun_fa": "او", "form_fa": "حرف می‌زند"},
                {"pronoun_fa": "ما", "form_fa": "حرف می‌زنیم"},
                {"pronoun_fa": "شما", "form_fa": "حرف می‌زنید"},
                {"pronoun_fa": "آن‌ها", "form_fa": "حرف می‌زنند"},
            ],
            "examples": [
                {
                    "fa": "به وسیله‌ی زبان حرف می‌زنیم.",
                    "reading_az": "Be vəsileye zəban hərf mizənim.",
                    "az": "Biz dil vasitəsilə danışırıq.",
                },
                {
                    "fa": "نوزاد هنوز حرف نمی‌زند.",
                    "reading_az": "Nouzad hənuz hərf nemizənəd.",
                    "az": "Körpə hələ danışmır.",
                },
                {
                    "fa": "دیروز با مادربزرگم حرف زدم.",
                    "reading_az": "Diruz ba madərbozorgəm hərf zədəm.",
                    "az": "Dünən nənəmlə danışdım.",
                },
            ],
        },
        {
            # Səh. 228 haşiyəsi (به وسیله‌ی: با) + səh. 229-230 çalışmaları.
            "title_az": "«به وسیله‌ی …» — vasitə bildirən quruluş",
            "title_fa": "به وسیله‌ی ........",
            "explanation_az": (
                "İşin hansı alət və ya üzv vasitəsilə görüldüyünü bildirmək üçün «به وسیله‌ی» işlənir.\n"
                "Quruluş: به وسیله‌ی + VASİTƏ + FEL.\n"
                "Dərslikdəki haşiyə: به وسیله‌ی = با. Yəni «به وسیله‌ی گوش می‌شنویم» ilə «با گوش می‌شنویم» eynidir.\n"
                "«وسیله» sözü izafətlə bağlanır, ona görə sonuna «ـی» əlavə olunur: وسیله + ی = وسیله‌ی.\n"
                "Azərbaycan dilinə «… vasitəsilə», «… ilə» kimi tərcümə edilir.\n"
                "Nümunələr: ما به وسیله‌ی چشم می‌بینیم؛ به وسیله‌ی پا راه می‌رویم؛ به وسیله‌ی دست می‌نویسیم."
            ),
            "note_fa": (
                "به وسیله‌ی = با\n"
                "گوش ← ما به وسیله‌ی گوش می‌شنویم.\n"
                "چشم ← ما به وسیله‌ی چشم می‌بینیم.\n"
                "زبان ← ما به وسیله‌ی زبان حرف می‌زنیم."
            ),
            "note_reading_az": (
                "Be vəsileye = ba\n"
                "Guş ← Ma be vəsileye guş mişənvim.\n"
                "Çeşm ← Ma be vəsileye çeşm mibinim.\n"
                "Zəban ← Ma be vəsileye zəban hərf mizənim."
            ),
            "note_az": (
                "«به وسیله‌ی …» = «با …» (… vasitəsilə):\n"
                "• به وسیله‌ی گوش می‌شنویم — qulaq vasitəsilə eşidirik\n"
                "• به وسیله‌ی بینی نفس می‌کشیم — burun vasitəsilə nəfəs alırıq"
            ),
            "conjugations": [
                {"pronoun_fa": "به وسیله‌ی گوش", "form_fa": "می‌شنویم (eşidirik)"},
                {"pronoun_fa": "به وسیله‌ی چشم", "form_fa": "می‌بینیم (görürük)"},
                {"pronoun_fa": "به وسیله‌ی بینی", "form_fa": "نفس می‌کشیم (nəfəs alırıq)"},
                {"pronoun_fa": "به وسیله‌ی زبان", "form_fa": "حرف می‌زنیم (danışırıq)"},
                {"pronoun_fa": "به وسیله‌ی دست", "form_fa": "می‌نویسیم (yazırıq)"},
                {"pronoun_fa": "به وسیله‌ی پا", "form_fa": "راه می‌رویم (yeriyirik)"},
            ],
            "examples": [
                {
                    "fa": "ما به وسیله‌ی پوست، گرمی، سردی، زبری و نرمی را احساس می‌کنیم.",
                    "reading_az": "Ma be vəsileye pust, gərmi, sərdi, zebri va nərmi ra ehsas mikonim.",
                    "az": "Biz dəri vasitəsilə istini, soyuğu, sərtliyi və yumşaqlığı hiss edirik.",
                },
                {
                    "fa": "قلب عضوی است که به وسیله‌ی آن خون به همه‌جای بدن می‌رسد.",
                    "reading_az": "Qəlb ozvi əst ke be vəsileye an xun be həmecaye bədən mirəsəd.",
                    "az": "Ürək elə bir üzvdür ki, onun vasitəsilə qan bədənin hər yerinə çatır.",
                },
                {
                    "fa": "دست عضوی است که به وسیله‌ی آن می‌نویسیم و وسایل را برمی‌داریم.",
                    "reading_az": "Dəst ozvi əst ke be vəsileye an minəvisim va vəsayel ra bərmidarim.",
                    "az": "Əl elə bir üzvdür ki, onun vasitəsilə yazırıq və əşyaları götürürük.",
                },
            ],
        },
        {
            # Səh. 220, 222, 227, 228 səhifə altı haşiyələri (زیرنویس‌ها).
            "title_az": "Dərslikdəki haşiyələr: eyni mənalı ifadələr",
            "title_fa": "زیرنویس‌های درس",
            "explanation_az": (
                "Dərsin səhifə altı qeydlərində bir neçə ifadənin izahı verilib:\n"
                "1. نوازش کردن = نوازش دادن — «sığallamaq» mənasında hər iki forma işlənir (səh. 220).\n"
                "2. شانه زدن = شانه کردن — «(saçı) daramaq» (səh. 222).\n"
                "3. کوتاه کردن — bir şeyin uzunluğunu və ya hündürlüyünü azaltmaq, yəni «qısaltmaq» (səh. 222).\n"
                "4. کیست؟ → danışıq dilində «کیه؟» deyilir: این عصا مالِ کیست؟ = این عصا مالِ کیه؟ (səh. 227).\n"
                "5. برخی = بعضی — «bəzi, bir qismi» (səh. 228).\n"
                "6. به وسیله‌ی = با — «… vasitəsilə, … ilə» (səh. 228)."
            ),
            "note_fa": (
                "نوازش کردن: نوازش دادن\n"
                "شانه زدن: شانه کردن\n"
                "کم کردن طول یا بلندی چیزی را «کوتاه کردن» می‌گویند.\n"
                "در زبان گفتار «کیست» را «کیه» می‌گوییم: این عصا مالِ کیست؟ = این عصا مالِ کیه؟\n"
                "برخی: بعضی\n"
                "به وسیله‌ی: با"
            ),
            "note_reading_az": (
                "Nəvazəş kərdən: nəvazəş dadən\n"
                "Şane zədən: şane kərdən\n"
                "Kəm kərdəne tul ya boləndiye çizi ra «kutah kərdən» miguyənd.\n"
                "Dər zəbane goftar «kist» ra «kiye» miguyim: In əsa male kist? = In əsa male kiye?\n"
                "Bərxi: bə'zi\n"
                "Be vəsileye: ba"
            ),
            "note_az": (
                "• نوازش کردن / نوازش دادن — sığallamaq\n"
                "• شانه زدن / شانه کردن — daramaq\n"
                "• کوتاه کردن — qısaltmaq\n"
                "• کیست؟ → کیه؟ (danışıq dili)\n"
                "• برخی = بعضی — bəzi\n"
                "• به وسیله‌ی = با — vasitəsilə"
            ),
            "conjugations": [
                {"pronoun_fa": "نوازش کردن", "form_fa": "نوازش دادن (sığallamaq)"},
                {"pronoun_fa": "شانه زدن", "form_fa": "شانه کردن (daramaq)"},
                {"pronoun_fa": "کوتاه کردن", "form_fa": "qısaltmaq"},
                {"pronoun_fa": "کیست؟", "form_fa": "کیه؟ (danışıq dili)"},
                {"pronoun_fa": "برخی", "form_fa": "بعضی (bəzi)"},
                {"pronoun_fa": "به وسیله‌ی", "form_fa": "با (… ilə)"},
            ],
            "examples": [
                {
                    "fa": "من هر روز موهای دخترم را شانه می‌زنم.",
                    "reading_az": "Mən hər ruz muhaye doxtərəm ra şane mizənəm.",
                    "az": "Mən hər gün qızımın saçlarını darayıram.",
                },
                {
                    "fa": "برادرم به آرایشگاه رفت و موهای سر و صورتش را کوتاه کرد.",
                    "reading_az": "Bəradərəm be arayeşgah rəft va muhaye sər va surətəş ra kutah kərd.",
                    "az": "Qardaşım bərbərxanaya getdi və başının, üzünün tüklərini qısaltdı.",
                },
                {
                    "fa": "این عصا مالِ کیه؟ (= این عصا مالِ کیست؟)",
                    "reading_az": "In əsa male kiye? (= In əsa male kist?)",
                    "az": "Bu əsa kimindir? (danışıq dili / yazı dili)",
                },
            ],
        },
    ],
    "exercises": [
        {
            "kind": "answer_question",
            "title_fa": "لطفاً جمله بسازید",
            "instruction_az": "Verilmiş sözlərlə cümlə düzəldin",
            "example_fa": "صحبت ← من با دوستم صحبت کردم.",
            "example_reading_az": "Sohbət ← Mən ba dustəm sohbət kərdəm.",
            "example_az": "Mən dostumla söhbət etdim.",
            "items": [
                {
                    "fa": "متکبّر",
                    "reading_az": "Motəkəbbər",
                    "az": "Təkəbbürlü",
                    "sample_answer_fa": "انسان متکبّر دوست زیاد ندارد.",
                    "sample_answer_reading_az": "Ensane motəkəbbər duste ziyad nədarəd.",
                    "sample_answer_az": "Təkəbbürlü insanın dostu çox olmaz.",
                },
                {
                    "fa": "صحبت",
                    "reading_az": "Sohbət",
                    "az": "Söhbət",
                    "sample_answer_fa": "من دیروز با استادم صحبت کردم.",
                    "sample_answer_reading_az": "Mən diruz ba ostadəm sohbət kərdəm.",
                    "sample_answer_az": "Mən dünən müəllimimlə söhbət etdim.",
                },
                {
                    "fa": "می‌بوسم",
                    "reading_az": "Mibusəm",
                    "az": "Öpürəm",
                    "sample_answer_fa": "من دست مادرم را می‌بوسم.",
                    "sample_answer_reading_az": "Mən dəste madərəm ra mibusəm.",
                    "sample_answer_az": "Mən anamın əlini öpürəm.",
                },
                {
                    "fa": "نوازش",
                    "reading_az": "Nəvazəş",
                    "az": "Sığal, əzizləmə",
                    "sample_answer_fa": "پدربزرگم همیشه نوه‌هایش را نوازش می‌کند.",
                    "sample_answer_reading_az": "Pedərbozorgəm həmişe novehayəş ra nəvazəş mikonəd.",
                    "sample_answer_az": "Babam həmişə nəvələrini sığallayır.",
                },
                {
                    "fa": "نابینا",
                    "reading_az": "Nabina",
                    "az": "Gözdən əlil",
                    "sample_answer_fa": "علی به مرد نابینا کمک کرد.",
                    "sample_answer_reading_az": "Əli be mərde nabina komək kərd.",
                    "sample_answer_az": "Əli gözdən əlil kişiyə kömək etdi.",
                },
                {
                    "fa": "احترام",
                    "reading_az": "Ehteram",
                    "az": "Hörmət",
                    "sample_answer_fa": "دانش‌آموزان به استادان خود احترام می‌گذارند.",
                    "sample_answer_reading_az": "Daneşamuzan be ostadane xod ehteram migəzarənd.",
                    "sample_answer_az": "Şagirdlər öz müəllimlərinə hörmət edirlər.",
                },
                {
                    "fa": "به دنیا آمدم",
                    "reading_az": "Be donya amədəm",
                    "az": "Dünyaya gəldim",
                    "sample_answer_fa": "من در شهر تبریز به دنیا آمدم.",
                    "sample_answer_reading_az": "Mən dər şəhre Təbriz be donya amədəm.",
                    "sample_answer_az": "Mən Təbriz şəhərində dünyaya gəldim.",
                },
                {
                    "fa": "از دنیا رفت",
                    "reading_az": "Əz donya rəft",
                    "az": "Vəfat etdi",
                    "sample_answer_fa": "مادربزرگم پارسال از دنیا رفت.",
                    "sample_answer_reading_az": "Madərbozorgəm parsal əz donya rəft.",
                    "sample_answer_az": "Nənəm keçən il vəfat etdi.",
                },
            ],
        },
        {
            # Səh. 221 və səh. 229 səhifə altındakı danışıq tapşırıqları:
            # «......... را بغل می‌کند.»، «با ....... حرف می‌زند.» və s.
            "kind": "practice_reveal",
            "instruction_az": (
                "Nöqtələrin yerini doldurub cümləni ucadan deyin. Nümunə: "
                "«… را بغل می‌کند.» → «مادر، نوزادش را بغل می‌کند.»"
            ),
            "example_prompt_fa": "… را بغل می‌کند.",
            "example_answer_fa": "مادر، نوزادش را بغل می‌کند.",
            "example_reading_az": "Madər, nouzadəş ra bəğəl mikonəd.",
            "example_az": "Ana körpəsini qucaqlayır.",
            "items": [
                {
                    "prompt_fa": "… را بغل می‌کند.",
                    "answer_fa": "پدر، نوزادش را بغل می‌کند.",
                    "reading_az": "Pedər, nouzadəş ra bəğəl mikonəd.",
                    "az": "Ata körpəsini qucaqlayır.",
                },
                {
                    "prompt_fa": "… را نوازش می‌کند.",
                    "answer_fa": "پدربزرگم نوه‌هایش را نوازش می‌کند.",
                    "reading_az": "Pedərbozorgəm novehayəş ra nəvazəş mikonəd.",
                    "az": "Babam nəvələrini sığallayır.",
                },
                {
                    "prompt_fa": "… را می‌بوسد.",
                    "answer_fa": "مادر، دست فرزندش را می‌بوسد.",
                    "reading_az": "Madər, dəste fərzəndəş ra mibusəd.",
                    "az": "Ana övladının əlini öpür.",
                },
                {
                    "prompt_fa": "با … صحبت می‌کند.",
                    "answer_fa": "او با مادربزرگش صحبت می‌کند.",
                    "reading_az": "U ba madərbozorgəş sohbət mikonəd.",
                    "az": "O, nənəsi ilə söhbət edir.",
                },
                {
                    "prompt_fa": "به … احترام می‌گذارد.",
                    "answer_fa": "طلبه به استادش احترام می‌گذارد.",
                    "reading_az": "Tələbe be ostadəş ehteram migozarəd.",
                    "az": "Tələbə müəlliminə hörmət edir.",
                },
                {
                    "prompt_fa": "… را احساس می‌کند (حس می‌کند).",
                    "answer_fa": "انسان به وسیله‌ی پوست، گرمی و سردی را احساس می‌کند.",
                    "reading_az": "Ensan be vəsileye pust, gərmi va sərdi ra ehsas mikonəd.",
                    "az": "İnsan dəri vasitəsilə istini və soyuğu hiss edir.",
                },
                {
                    "prompt_fa": "با … حرف می‌زند.",
                    "answer_fa": "انسان با زبان حرف می‌زند.",
                    "reading_az": "Ensan ba zəban hərf mizənəd.",
                    "az": "İnsan dillə danışır.",
                },
            ],
        },
        {
            # Səh. 223 «لطفاً کامل کنید» — 6 bənd, cəmi 7 boşluq (4-cü bənddə iki boşluq var),
            # söz qutusunda da 7 söz var. Ona görə fill_blank yox, multi_blank kimi verilir.
            "kind": "multi_blank",
            "title_fa": "لطفاً کامل کنید",
            "instruction_az": "Cümlələri söz qutusundakı sözlərlə tamamlayın (کوتاه؛ دست؛ خون؛ قوی؛ بیست؛ بزرگ؛ پا)",
            "example_fa": "انسان دو ___ دارد.\nانسان دو *گوش* دارد.",
            "example_reading_az": "Ensan do guş darəd.",
            "example_az": (
                "İnsanın iki qulağı var.\n"
                "Hər boşluğa söz qutusundan yalnız BİR söz düşür.\n"
                "Bəzi cümlələrdə iki boşluq var — onlara iki ayrı söz seçilir."
            ),
            # 7 boşluq = 7 çip.
            "word_bank": ["کوتاه", "دست", "خون", "قوی", "بیست", "بزرگ", "پا"],
            "items": [
                {
                    "fa_with_blanks": "شکم انسان‌های چاق، ___ است.",
                    "correct_answers": ["بزرگ"],
                    "full_reading_az": "Şekəme ensanhaye çaq, bozorg əst.",
                    "full_translation_az": "Kök insanların qarnı böyükdür.",
                },
                {
                    "fa_with_blanks": "در رگ‌های انسان ___ وجود دارد.",
                    "correct_answers": ["خون"],
                    "full_reading_az": "Dər rəghaye ensan xun vocud darəd.",
                    "full_translation_az": "İnsanın damarlarında qan var.",
                },
                {
                    "fa_with_blanks": "انسان ___ انگشت دارد.",
                    "correct_answers": ["بیست"],
                    "full_reading_az": "Ensan bist əngoşt darəd.",
                    "full_translation_az": "İnsanın iyirmi barmağı var.",
                },
                {
                    "fa_with_blanks": "انسان دو ___، دو ___ و یک سر دارد.",
                    "correct_answers": ["دست", "پا"],
                    "full_reading_az": "Ensan do dəst, do pa va yek sər darəd.",
                    "full_translation_az": "İnsanın iki əli, iki ayağı və bir başı var.",
                },
                {
                    "fa_with_blanks": "من روزهای جمعه ناخن‌هایم را ___ می‌کنم.",
                    "correct_answers": ["کوتاه"],
                    "full_reading_az": "Mən ruzhaye com'e naxonhayəm ra kutah mikonəm.",
                    "full_translation_az": "Mən cümə günləri dırnaqlarımı qısaldıram (tuturam).",
                },
                {
                    "fa_with_blanks": "بازوها و ماهیچه‌های آن جوان بسیار ___ هستند.",
                    "correct_answers": ["قوی"],
                    "full_reading_az": "Bazuha va mahiçehaye an cəvan besyar qəvi həstənd.",
                    "full_translation_az": "O gəncin qolları və əzələləri çox güclüdür.",
                },
            ],
        },
        {
            # Səh. 225 «نام تصویرهای زیر را بگویید» — 16 şəkil, hər birinin adını demək.
            "kind": "picture_sentences",
            "title_fa": "نام تصویرهای زیر را بگویید.",
            "instruction_az": "Aşağıdakı şəkillərdəki bədən üzvlərinin adını deyin",
            "example_fa": "این گوش است.",
            "example_reading_az": "In guş əst.",
            "example_az": "Bu qulaqdır.",
            "example_answer_fa": "این گوش است؛ ما به وسیله‌ی گوش می‌شنویم.",
            "example_answer_reading_az": "In guş əst; ma be vəsileye guş mişənvim.",
            "example_answer_az": "Bu qulaqdır; biz qulaq vasitəsilə eşidirik.",
            "items": [
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این ماهیچه (عضله) است.", "reading_az": "In mahiçe (əzəle) əst.", "az": "Bu əzələdir."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این‌ها ناخن هستند.", "reading_az": "Inha naxon həstənd.", "az": "Bunlar dırnaqlardır."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این رگ است.", "reading_az": "In rəg əst.", "az": "Bu damardır."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این بازو است.", "reading_az": "In bazu əst.", "az": "Bu qoldur (bazudur)."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این مژه است.", "reading_az": "In moje əst.", "az": "Bu kirpikdir."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این ابرو است.", "reading_az": "In əbru əst.", "az": "Bu qaşdır."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این مغز است.", "reading_az": "In məğz əst.", "az": "Bu beyindir."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این استخوان است.", "reading_az": "In ostoxan əst.", "az": "Bu sümükdür."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این معده است.", "reading_az": "In moede əst.", "az": "Bu mədədir."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این قلب است.", "reading_az": "In qəlb əst.", "az": "Bu ürəkdir."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این کف دست و انگشت‌ها است.", "reading_az": "In kəfe dəst va əngoştha əst.", "az": "Bu ovuc və barmaqlardır."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این آرنج است.", "reading_az": "In arənc əst.", "az": "Bu dirsəkdir."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این روده‌ی بزرگ و روده‌ی کوچک است.", "reading_az": "In rudeye bozorg va rudeye kuçək əst.", "az": "Bu yoğun və nazik bağırsaqdır."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این اسکلت و ستون فقرات است.", "reading_az": "In eskelet va sotune fəqərat əst.", "az": "Bu skelet və onurğa sütunudur."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این کف پا است.", "reading_az": "In kəfe pa əst.", "az": "Bu ayağın altıdır."},
                    ],
                },
                {
                    "image": "",
                    "sentences": [
                        {"fa": "این کمر است.", "reading_az": "In kəmər əst.", "az": "Bu beldir."},
                    ],
                },
            ],
        },
        {
            "kind": "answer_question",
            "title_fa": "لطفاً پاسخ دهید — اعضای بدن",
            "instruction_az": "Bədən üzvləri haqqında suallara cavab verin",
            "example_fa": "یک دست چند انگشت دارد؟ ← یک دست پنج انگشت دارد.",
            "example_reading_az": "Yek dəst çənd əngoşt darəd? ← Yek dəst pənc əngoşt darəd.",
            "example_az": "Bir əldə neçə barmaq var? ← Bir əldə beş barmaq var.",
            "items": [
                {
                    "fa": "در صورت انسان چه چیزهایی وجود دارد؟",
                    "reading_az": "Dər surəte ensan çe çizhayi vocud darəd?",
                    "az": "İnsanın üzündə nələr var?",
                    "sample_answer_fa": "در صورت انسان چشم، ابرو، پلک، مژه، بینی، لب، چانه و گوش وجود دارد.",
                    "sample_answer_reading_az": "Dər surəte ensan çeşm, əbru, pelk, moje, bini, ləb, çane va guş vocud darəd.",
                    "sample_answer_az": "İnsanın üzündə göz, qaş, göz qapağı, kirpik, burun, dodaq, çənə və qulaq var.",
                },
                {
                    "fa": "با زبان، چشم و گوش چه کار می‌کنید؟",
                    "reading_az": "Ba zəban, çeşm va guş çe kar mikonid?",
                    "az": "Dil, göz və qulaqla nə edirsiniz?",
                    "sample_answer_fa": "با زبان صحبت می‌کنیم و طعم می‌چشیم، با چشم می‌بینیم و با گوش می‌شنویم.",
                    "sample_answer_reading_az": "Ba zəban sohbət mikonim va təm miçeşim, ba çeşm mibinim va ba guş mişənvim.",
                    "sample_answer_az": "Dillə danışırıq və dad bilirik, gözlə görürük, qulaqla eşidirik.",
                },
                {
                    "fa": "زانو و آرنج کجای بدن قرار دارند؟",
                    "reading_az": "Zanu va arənc kocaye bədən qərar darənd?",
                    "az": "Diz və dirsək bədənin harasında yerləşir?",
                    "sample_answer_fa": "زانو در پا و آرنج در دست قرار دارد.",
                    "sample_answer_reading_az": "Zanu dər pa va arənc dər dəst qərar darəd.",
                    "sample_answer_az": "Diz ayaqda, dirsək isə qolda (əldə) yerləşir.",
                },
                {
                    "fa": "در شکم انسان چه چیزهایی هست؟",
                    "reading_az": "Dər şekəme ensan çe çizhayi həst?",
                    "az": "İnsanın qarnında nələr var?",
                    "sample_answer_fa": "در شکم انسان معده، کلیه‌ها، کبد (جگر) و رودی بزرگ و کوچک قرار دارد.",
                    "sample_answer_reading_az": "Dər şekəme ensan moede, kolyeha, kəbed va rudeye bozorg va kuçək qərar darəd.",
                    "sample_answer_az": "İnsanın qarnında mədə, böyrəklər, qaraciyər və yoğun-nazik bağırsaqlar yerləşir.",
                },
                {
                    "fa": "زبان و معده درکجا قرار دارند؟",
                    "reading_az": "Zəban va moede dər koca qərar darənd?",
                    "az": "Dil və mədə harada yerləşir?",
                    "sample_answer_fa": "زبان در دهان و معده در شکم قرار دارد.",
                    "sample_answer_reading_az": "Zəban dər dəhan va moede dər şekəm qərar darəd.",
                    "sample_answer_az": "Dil ağızda, mədə isə qarında yerləşir.",
                },
                {
                    "fa": "یک دست چند انگشت دارد؟",
                    "reading_az": "Yek dəst çənd əngoşt darəd?",
                    "az": "Bir əldə neçə barmaq var?",
                    "sample_answer_fa": "یک دست پنج انگشت دارد.",
                    "sample_answer_reading_az": "Yek dəst pənc əngoşt darəd.",
                    "sample_answer_az": "Bir əldə beş barmaq var.",
                },
            ],
        },
        {
            # Səh. 227 «لطفاً بخوانید» — «مالِ …» quruluşu ilə 4 cümlə.
            "kind": "practice_reveal",
            "instruction_az": (
                "Verilmiş sözlərdən «مالِ …» quruluşu ilə cümlə qurub oxuyun. "
                "Nümunə: «دوچرخه‌ی آبی / من» → «این دوچرخه‌ی آبی، مالِ من است.»"
            ),
            "example_prompt_fa": "دوچرخه‌ی آبی / من",
            "example_answer_fa": "این دوچرخه‌ی آبی، مالِ من است.",
            "example_reading_az": "In doçərxeye abi, male mən əst.",
            "example_az": "Bu mavi velosiped mənimdir.",
            "items": [
                {
                    "prompt_fa": "این عینک / من — آن عینک / برادرم صادق",
                    "answer_fa": "این عینک، مالِ من است و آن عینک، مالِ برادرم صادق است.",
                    "reading_az": "In eynek, male mən əst va an eynek, male bəradərəm Sadeq əst.",
                    "az": "Bu eynək mənimdir, o eynək isə qardaşım Sadiqindir.",
                },
                {
                    "prompt_fa": "یکی از این دفترها / خواهرم پروین",
                    "answer_fa": "یکی از این دفترها مالِ خواهرم پروین است.",
                    "reading_az": "Yeki əz in dəftərha male xahərəm Pərvin əst.",
                    "az": "Bu dəftərlərdən biri bacım Pərvinindir.",
                },
                {
                    "prompt_fa": "این عصا / کیست؟ — پدربزرگم",
                    "answer_fa": "این عصا مالِ کیست؟ این عصا مالِ پدربزرگم است.",
                    "reading_az": "In əsa male kist? In əsa male pedərbozorgəm əst.",
                    "az": "Bu əsa kimindir? Bu əsa babamındır.",
                },
                {
                    "prompt_fa": "آیا آن خانه‌ی زیبا / عبّاس؟",
                    "answer_fa": "آیا آن خانه‌ی زیبا مالِ عبّاس است؟ بله، آن خانه‌ی زیبا مالِ عبّاس است.",
                    "reading_az": "Aya an xaneye ziba male Əbbas əst? Bəle, an xaneye ziba male Əbbas əst.",
                    "az": "O gözəl ev Abbasındır? Bəli, o gözəl ev Abbasındır.",
                },
            ],
        },
        {
            "kind": "answer_question",
            "title_fa": "مانند مثال بپرسید و پاسخ دهید — «مالِ کیست؟»",
            "instruction_az": "Nümunəyə uyğun olaraq sual verin və cavablandırın",
            "example_fa": "انگشتر / دوستم ← این انگشتر، مالِ کیست؟ این انگشتر، مالِ دوستم است.",
            "example_reading_az": "Əngoştər / dustəm ← In əngoştər, male kist? In əngoştər, male dustəm əst.",
            "example_az": "Üzük / dostum ← Bu üzük kimindir? Bu üzük dostumundur.",
            "items": [
                {
                    "fa": "پالتو / برادرِ حسن",
                    "reading_az": "Palto / bəradəre Həsən",
                    "az": "Palto / Həsənin qardaşı",
                    "sample_answer_fa": "این پالتو، مالِ کیست؟ این پالتو، مالِ برادر حسن است.",
                    "sample_answer_reading_az": "In palto, male kist? In palto, male bəradəre Həsən əst.",
                    "sample_answer_az": "Bu palto kimindir? Bu palto Həsənin qardaşınındır.",
                },
                {
                    "fa": "جامدادی / برادرزاده‌ام ریحانه",
                    "reading_az": "Camdadi / bəradərzadeəm Reyhane",
                    "az": "Qələmqabı / qardaşım qızı Reyhanə",
                    "sample_answer_fa": "این جامدادی، مالِ کیست؟ این جامدادی، مالِ برادرزاده‌ام ریحانه است.",
                    "sample_answer_reading_az": "In camdadi, male kist? In camdadi, male bəradərzadeəm Reyhane əst.",
                    "sample_answer_az": "Bu qələmqabı kimindir? Bu qələmqabı qardaşım qızı Reyhanəninkidir.",
                },
                {
                    "fa": "آپارتمان / عمویم",
                    "reading_az": "Apartəman / əmuyəm",
                    "az": "Mənzil / əmim",
                    "sample_answer_fa": "این آپارتمان، مالِ کیست؟ این آپارتمان، مالِ عمویم است.",
                    "sample_answer_reading_az": "In apartəman, male kist? In apartəman, male əmuyəm əst.",
                    "sample_answer_az": "Bu mənzil kimindir? Bu mənzil əmiminkidir.",
                },
                {
                    "fa": "مداد رنگی / فرزندم جواد",
                    "reading_az": "Medade rəngi / fərzəndəm Cəvad",
                    "az": "Rəngli qələm / övladım Cavad",
                    "sample_answer_fa": "این مداد رنگی، مالِ کیست؟ این مداد رنگی، مالِ فرزندم جواد است.",
                    "sample_answer_reading_az": "In medade rəngi, male kist? In medade rəngi, male fərzəndəm Cəvad əst.",
                    "sample_answer_az": "Bu rəngli qələm kimindir? Bu rəngli qələm övladım Cavadındır.",
                },
                {
                    "fa": "گل‌فروشی / آقا مهدی",
                    "reading_az": "Golforuşi / Aqa Məhdi",
                    "az": "Gül mağazası / Mehdi bəy",
                    "sample_answer_fa": "این گل‌فروشی، مالِ کیست؟ این گل‌فروشی، مالِ آقا مهدی است.",
                    "sample_answer_reading_az": "In golforuşi, male kist? In golforuşi, male Aqa Məhdi əst.",
                    "sample_answer_az": "Bu gül mağazası kimindir? Bu gül mağazası Mehdi bəyinkidir.",
                },
                {
                    "fa": "ساعت مچی / پسرم محمّد",
                    "reading_az": "Saəte moçi / posərəm Mohəmməd",
                    "az": "Qol saatı / oğlum Məhəmməd",
                    "sample_answer_fa": "این ساعت مچی، مالِ کیست؟ این ساعت مچی، مالِ پسرم محمّد است.",
                    "sample_answer_reading_az": "In saəte moçi, male kist? In saəte moçi, male posərəm Mohəmməd əst.",
                    "sample_answer_az": "Bu qol saatı kimindir? Bu qol saatı oğlum Məhəmmədindir.",
                },
            ],
        },
        {
            "kind": "answer_question",
            "title_fa": "مانند مثال جمله بگویید — «به وسیله‌ی …»",
            "instruction_az": "Nümunəyə uyğun cümlələr tərtib edin",
            "example_fa": "گوش ← ما به وسیله‌ی گوش می‌شنویم.",
            "example_reading_az": "Guş ← Ma be vəsileye guş mişənvim.",
            "example_az": "Qulaq ← Biz qulaq vasitəsilə eşidirik.",
            "items": [
                {
                    "fa": "چشم",
                    "reading_az": "Çeşm",
                    "az": "Göz",
                    "sample_answer_fa": "ما به وسیله‌ی چشم می‌بینیم.",
                    "sample_answer_reading_az": "Ma be vəsileye çeşm mibinim.",
                    "sample_answer_az": "Biz göz vasitəsilə görürük.",
                },
                {
                    "fa": "بینی",
                    "reading_az": "Bini",
                    "az": "Burun",
                    "sample_answer_fa": "ما به وسیله‌ی بینی نفس می‌کشیم و بوی عطر را احساس می‌کنیم.",
                    "sample_answer_reading_az": "Ma be vəsileye bini nəfəs mikeşim va buye ətr ra ehsas mikonim.",
                    "sample_answer_az": "Biz burun vasitəsilə nəfəs alırıq və ətrin qoxusunu duyuruq.",
                },
                {
                    "fa": "دست",
                    "reading_az": "Dəst",
                    "az": "Əl",
                    "sample_answer_fa": "ما به وسیله‌ی دست می‌نویسیم، غذا می‌خوریم و وسایل را برمی‌داریم.",
                    "sample_answer_reading_az": "Ma be vəsileye dəst minəvisim, qəza mixorim va vəsayel ra bərmidarim.",
                    "sample_answer_az": "Biz əl vasitəsilə yazırıq, yemək yeyirik və əşyaları götürürük.",
                },
                {
                    "fa": "زبان",
                    "reading_az": "Zəban",
                    "az": "Dil",
                    "sample_answer_fa": "ما به وسیله‌ی زبان حرف می‌زنیم و مزه‌ی غذاها را حس می‌کنیم.",
                    "sample_answer_reading_az": "Ma be vəsileye zəban sohbət mizənim va məzeye qəzaha ra hes mikonim.",
                    "sample_answer_az": "Biz dil vasitəsilə danışırıq və yeməklərin dadını hiss edirik.",
                },
                {
                    # Səh. 230, alt-orta şəkil: qırmızı ox əlin DƏRİSİNİ göstərir
                    # (sadə əl şəklindən fərqləndirmək üçün) → پوست.
                    "fa": "پوست",
                    "reading_az": "Pust",
                    "az": "Dəri",
                    "sample_answer_fa": "ما به وسیله‌ی پوست، گرمی و سردی را احساس می‌کنیم.",
                    "sample_answer_reading_az": "Ma be vəsileye pust, gərmi va sərdi ra ehsas mikonim.",
                    "sample_answer_az": "Biz dəri vasitəsilə istini və soyuğu hiss edirik.",
                },
                {
                    "fa": "پا",
                    "reading_az": "Pa",
                    "az": "Ayaq",
                    "sample_answer_fa": "ما به وسیله‌ی پا راه می‌رویم و می‌دویم.",
                    "sample_answer_reading_az": "Ma be vəsileye pa rah mirəvim va midəvim.",
                    "sample_answer_az": "Biz ayaq vasitəsilə gəzirik və qaçırıq.",
                },
            ],
        },
        {
            # Səh. 230 «لطفاً کامل کنید» — 6 bənd, cəmi 7 boşluq (6-cı bənddə iki boşluq var),
            # söz qutusunda da 7 söz var → multi_blank.
            "kind": "multi_blank",
            "title_fa": "لطفاً کامل کنید",
            "instruction_az": "Cümlələri söz qutusundakı sözlərlə tamamlayın (نمی‌بیند؛ نوزاد؛ کور؛ مهربان؛ نمی‌شنود؛ کر؛ معلول)",
            "example_fa": "کسی که به دیگران کمک نمی‌کند، ___ است.\nکسی که به دیگران کمک نمی‌کند، *نامهربان* است.",
            "example_reading_az": "Kəsi ke be digəran komək nemikonəd, namehrəban əst.",
            "example_az": (
                "Başqalarına kömək etməyən adam namehribandır.\n"
                "Hər boşluğa söz qutusundan bir söz seçilir; sonuncu cümlədə iki boşluq var."
            ),
            # 7 boşluq = 7 çip.
            "word_bank": ["نمی‌بیند", "نوزاد", "کور", "مهربان", "نمی‌شنود", "کر", "معلول"],
            "items": [
                {
                    "fa_with_blanks": "کسی که دیگران را دوست دارد و به آن‌ها کمک می‌کند، ___ است.",
                    "correct_answers": ["مهربان"],
                    "full_reading_az": "Kəsi ke digəran ra dust darəd va be anha komək mikonəd, mehrəban əst.",
                    "full_translation_az": "Başqalarını sevən və onlara kömək edən şəxs mehribandır.",
                },
                {
                    "fa_with_blanks": "کسی که دست و پایش سالم نیست، ___ است.",
                    "correct_answers": ["معلول"],
                    "full_reading_az": "Kəsi ke dəst va payəş saləm nist, mə'lul əst.",
                    "full_translation_az": "Əli və ayağı sağlam olmayan şəxs əlildir.",
                },
                {
                    "fa_with_blanks": "به بچّه‌ای که دو، سه هفته سن دارد، ___ می‌گویند.",
                    "correct_answers": ["نوزاد"],
                    "full_reading_az": "Be bəççe-i ke do, se həfte senn darəd, nouzad miguyənd.",
                    "full_translation_az": "İki-üç həftəlik uşağa körpə (yeni doğulmuş) deyirlər.",
                },
                {
                    "fa_with_blanks": "نابینا کسی است که ___ .",
                    "correct_answers": ["نمی‌بیند"],
                    "full_reading_az": "Nabina kəsi əst ke nemibinəd.",
                    "full_translation_az": "Gözdən əlil görməyən şəxsdir.",
                },
                {
                    "fa_with_blanks": "ناشنوا کسی است که ___ .",
                    "correct_answers": ["نمی‌شنود"],
                    "full_reading_az": "Naşənva kəsi əst ke nemişənəvəd.",
                    "full_translation_az": "Eşitmə əlili eşitməyən şəxsdir.",
                },
                {
                    "fa_with_blanks": "اسم دیگر نابینا، ___ و اسم دیگر ناشنوا، ___ است.",
                    "correct_answers": ["کور", "کر"],
                    "full_reading_az": "Esme digəre nabina kur va esme digəre naşənva kər əst.",
                    "full_translation_az": "Gözdən əlilin başqa adı kor, eşitmə əlilininki isə kardır.",
                },
            ],
        },
        {
            "kind": "picture_sentences",
            "title_fa": "برای هر تصویر، دو جمله بگویید — دست/دسته، پا/پایه...",
            "instruction_az": "Şəkillərə uyğun cümlələr qurub bədən üzvü və əşya adlarının fərqini göstərin",
            "items": [
                {
                    "image": "body_hands_handle",
                    "sentences": [
                        {"fa": "انسان دو دست دارد.", "reading_az": "Ensan do dəst darəd.", "az": "İnsanın iki əli var."},
                        {"fa": "پارچ و سطل دسته دارند.", "reading_az": "Parç va sətl dəste darənd.", "az": "Dolça və vedrənin qulpu var."},
                    ],
                },
                {
                    "image": "body_legs_base",
                    "sentences": [
                        {"fa": "ما دو پا داریم.", "reading_az": "Ma do pa darim.", "az": "Bizim iki ayağımız var."},
                        {"fa": "این صندلی، چهار پایه دارد.", "reading_az": "In səndəli, çəhar paye darəd.", "az": "Bu stulun dörd ayağı var."},
                    ],
                },
                {
                    "image": "body_eyes_spring",
                    "sentences": [
                        {"fa": "انسان‌ها چشم دارند.", "reading_az": "Ensanha çeşm darənd.", "az": "İnsanların gözü var."},
                        {"fa": "در کوه، چشمه وجود دارد.", "reading_az": "Dər kuh, çeşme vocud darəd.", "az": "Dağda bulaq var."},
                    ],
                },
                {
                    "image": "body_teeth_notches",
                    "sentences": [
                        {"fa": "این دندان است.", "reading_az": "In dəndan əst.", "az": "Bu dişdir."},
                        {"fa": "حرف «س» سه دندانه دارد.", "reading_az": "Hərfe «se» se dəndane darəd.", "az": "«S» hərfinin üç dişi var."},
                    ],
                },
                {
                    "image": "body_beard_root",
                    "sentences": [
                        {"fa": "این مرد ریش دارد.", "reading_az": "In mərd riş darəd.", "az": "Bu kişinin saqqalı var."},
                        {"fa": "درخت ریشه دارد.", "reading_az": "Dərəxt rişe darəd.", "az": "Ağacın kökü var."},
                    ],
                },
                {
                    "image": "body_horn_branch",
                    "sentences": [
                        {"fa": "گاو شاخ دارد.", "reading_az": "Gav şax darəd.", "az": "İnəyin buynuzu var."},
                        {"fa": "درخت شاخه دارد.", "reading_az": "Dərəxt şaxe darəd.", "az": "Ağacın budağı var."},
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
                        "fa": "مادر، نوزادش را بغل می‌کند و می‌بوسد.",
                        "reading_az": "Madər, nouzadəş ra bəğəl mikonəd va mibusəd.",
                        "az": "Ana körpəsini qucaqlayır və öpür.",
                    },
                    {
                        "fa": "کودکانتان را نوازش کنید و ببوسید.",
                        "reading_az": "Kudəkanətan ra nəvazəş konid va bəbusid.",
                        "az": "Uşaqlarınızı sığallayın və öpün.",
                    },
                    {
                        "fa": "هر روز در این بیمارستان حدود بیست نوزاد به دنیا می‌آید.",
                        "reading_az": "Hər ruz dər in bimarestan hodude bist nouzad be donya miayəd.",
                        "az": "Hər gün bu xəstəxanada təxminən iyirmi körpə dünyaya gəlir.",
                    },
                    {
                        "fa": "من دیروز به دیدن مادربزرگم رفتم و با او صحبت کردم.",
                        "reading_az": "Mən diruz be didəne madərbozorgəm rəftəm va ba u sohbət kərdəm.",
                        "az": "Mən dünən nənəmi görməyə getdim və onunla söhbət etdim.",
                    },
                    {
                        "fa": "دوستم معلول است؛ او برای راه رفتن از عصا استفاده می‌کند.",
                        "reading_az": "Dustəm mə'lul əst; u bəraye rah rəftən əz əsa estefade mikonəd.",
                        "az": "Dostum əlildir; o yeriş üçün əsadan istifadə edir.",
                    },
                    {
                        "fa": "علی به مرد نابینا کمک کرد و او را به آن طرف خیابان برد.",
                        "reading_az": "Əli be mərde nabina komək kərd va u ra be an tərəfe xiyaban bord.",
                        "az": "Əli gözdən əlil kişiyə kömək etdi və onu küçənin o biri tərəfinə keçirdi.",
                    },
                    {
                        "fa": "مادربزرگ سعید، هفتاد و پنج سال زندگی کرد؛ او پارسال از دنیا رفت.",
                        "reading_az": "Madərbozorge Səid, həftad o pənc sal zendegi kərd; u parsal əz donya rəft.",
                        "az": "Səidin nənəsi yetmiş beş il yaşadı; o keçən il vəfat etdi.",
                    },
                    {
                        "fa": "استادم گفت: روز مادر به دیدن مادرتان بروید و دست ایشان را ببوسید.",
                        "reading_az": "Ostadəm goft: Ruze madər be didəne madərətan bərəvid va dəste işan ra bəbusid.",
                        "az": "Müəllimim dedi: Analar günündə ananızın görüşünə gedin və onun əlini öpün.",
                    },
                    {
                        "fa": "هر روز در جهان هزاران نفر از دنیا می‌روند و هزاران نفر به دنیا می‌آیند.",
                        "reading_az": "Hər ruz dər cəhan hezaran nəfər əz donya mirəvənd va hezaran nəfər be donya miayənd.",
                        "az": "Hər gün dünyada minlərlə insan vəfat edir və minlərlə insan dünyaya gəlir.",
                    },
                    {
                        "fa": "پدربزرگم همیشه نوه‌هایش را نوازش می‌کند. او بسیار مهربان است.",
                        "reading_az": "Pedərbozorgəm həmişe novehayəş ra nəvazəş mikonəd. U besyar mehrəban əst.",
                        "az": "Babam həmişə nəvələrini sığallayır. O çox mehribandır.",
                    },
                    {
                        "fa": "نابینا کسی است که چشمانش نمی‌بیند و ناشنوا کسی است که گوش‌هایش نمی‌شنود.",
                        "reading_az": "Nabina kəsi əst ke çeşmanəş nimibinəd va naşənva kəsi əst ke guşhayəş nimişənəvəd.",
                        "az": "Gözdən əlil gözləri görməyən, eşitmə əlili isə qulaqları eşitməyən şəxsdir.",
                    },
                    {
                        "fa": "طلبه‌های این کلاس مهربان و متواضع هستند. آن‌ها به استادهایشان احترام می‌گذارند.",
                        "reading_az": "Tələbehaye in kelas mehrəban va motəvaze həstənd. Anha be ostadhayeşan ehteram migəzarənd.",
                        "az": "Bu sinfin tələbələri mehriban və təvazokardırlar. Onlar müəllimlərinə hörmət edirlər.",
                    },
                ],
            },
        ],
        "answer_items": [
            {
                "fa": "در صورت انسان چشم، ابرو، پلک، مژه، بینی و لب قرار دارد.",
                "reading_az": "Dər surəte ensan çeşm, əbru, pelk, moje, bini va ləb qərar darəd.",
                "az": "İnsanın üzündə göz, qaş, göz qapağı, kirpik, burun və dodaq yerləşir.",
            },
            {
                "fa": "موهای دخترم زیبا و بلند است. من هر روز موهای او را شانه می‌زنم.",
                "reading_az": "Muhaye doxtərəm ziba va bolənd əst. Mən hər ruz muhaye u ra şane mizənəm.",
                "az": "Qızımın saçları gözəl və uzundur. Mən hər gün onun saçlarını darayıram.",
            },
            {
                "fa": "دندان‌پزشک پس از معاینه گفت: هر روز سه بار دندان‌هایت را مسواک بزن.",
                "reading_az": "Dəndanpezəşk pəs əz moayene goft: Hər ruz se bar dəndanhayət ra mesvak bəzən.",
                "az": "Diş həkimi müayinədən sonra dedi: Hər gün üç dəfə dişlərini fırçala.",
            },
            {
                "fa": "برادرم به آرایشگاه رفت و موهای سر و صورتش را کوتاه کرد.",
                "reading_az": "Bəradərəm be arayeşgah rəft va muhaye sər va surətəş ra kotah kərd.",
                "az": "Qardaşım bərbərxanaya getdi və baş-saqqal saçını qısaltdı.",
            },
            {
                "fa": "ما با چشم‌هایمان می‌بینیم؛ با گوش‌هایمان می‌شنویم و با زبانمان صحبت می‌کنیم.",
                "reading_az": "Ma ba çeşmhayeman mibinim; ba guşhayeman mişənvim va ba zəbaneman sohbət mikonim.",
                "az": "Biz gözlərimizlə görürük; qulaqlarımızla eşidirik və dilimizlə danışırıq.",
            },
        ],
    },
    "reading_text": {
        "title_fa": "بدن انسان",
        "title_az": "İnsan bədəni",
        "paragraphs_fa": [
            "بدن انسان قسمت‌های گوناگونی، مانندِ پوست، گوشت، خون، استخوان و... دارد. رنگ پوست انسان‌ها گوناگون است. بعضی از انسان‌ها زردپوست هستند؛ بعضی سیاه‌پوست، برخی سرخ‌پوست و بعضی دیگر سفیدپوستند. ما به وسیله‌ی پوست، گرمی، سردی، زبری و نرمی را احساس می‌کنیم.",
            "در بدن انسان، بیش از دویست عدد استخوان وجود دارد. استخوان‌ها بسیار محکم هستند. محکم‌ترین و بلندترین استخوان بدن انسان، استخوان ران است.",
            "در بدن انسان، دو چشم برای دیدن و دو گوش برای شنیدن وجود دارد. بعضی از مردم، چشم‌هایشان ضعیف است و خوب نمی‌بینند. آن‌ها برای بهتر دیدن از عینک استفاده می‌کنند.",
            "ما از بینی علاوه بر نفس کشیدن، بوی غذاها، گل‌ها، عطرها و... را احساس می‌کنیم. به وسیله‌ی زبان حرف می‌زنیم و طعم و مزه‌ی خوردنی‌ها، مانندِ شیرین بودنِ عسل، شور بودنِ نمک، تند بودنِ فلفل و ترش بودنِ بعضی از میوه‌ها را حس می‌کنیم.",
            "در بدن ما اعضای دیگری هم وجود دارد، مانندِ قلب که به وسیله‌ی آن خون به همه‌جای بدن می‌رسد؛ پا که به وسیله‌ی آن راه می‌رویم و دست که به وسیله‌ی آن می‌نویسیم، غذا می‌خوریم و وسایل را برمی‌داریم.",
        ],
        "footnotes": [
            {"fa": "برخی", "az": "bəzi, bir neçəsi"},
            {"fa": "به وسیله‌ی", "az": "... vasitəsilə, ilə"},
        ],
        "full_translation_az": (
            "İnsan bədəninin dəri, ət, qan, sümük və s. kimi müxtəlif hissələri var. İnsanların dərisinin rəngi "
            "müxtəlifdir. Bəzi insanlar sarıdərilidir; bəzisi qaradərili, bir neçəsi qırmızıdərilidir və bəziləri "
            "isə ağdərilidirlər. Biz dəri vasitəsilə istini, soyuğu, sərtliyi və yumşaqlığı hiss edirik.\n\n"
            "İnsan bədənində iki yüzdən çox sümük var. Sümüklər çox möhkəmdir. İnsan bədəninin ən möhkəm və ən uzun sümüyü bud sümüyüdür.\n\n"
            "İnsan bədənində görmək üçün iki göz və eşitmək üçün iki qulaq var. Bəzi insanların gözləri zəifdir və yaxşı görmürlər. Onlar daha yaxşı görmək üçün eynəkdən istifadə edirlər.\n\n"
            "Biz burun vasitəsilə nəfəs almaqla yanaşı, yeməklərin, güllərin, ətirlərin qoxusunu da duyuruq. Dil vasitəsilə danışırıq və yeməklərin dadını — balın şirinliyini, duzun şorluğunu, istiotun acılığını və bəzi meyvələrin turşluğunu hiss edirik.\n\n"
            "Bədənimizdə başqa üzvlər də var: məsələn, qanın bədənin hər yerinə çatmasını təmin edən ürək; yeriməyimizə imkan verən ayaq və yazmağımıza, yemək yeməyimizə, əşyaları götürməyimizə kömək edən əl."
        ),
        "sentences": [
            {
                "fa": "بدن انسان قسمت‌های گوناگونی، مانندِ پوست، گوشت، خون، استخوان و... دارد.",
                "reading_az": "Bədəne ensan qəsməthaye gunaguni, manənde pust, guşt, xun, ostoxan va... darəd.",
                "az": "İnsan bədəninin dəri, ət, qan, sümük və s. kimi müxtəlif hissələri var.",
                "new_paragraph": True,
            },
            {"fa": "رنگ پوست انسان‌ها گوناگون است.", "reading_az": "Rənge puste ensanha gunagun əst.", "az": "İnsanların dərisinin rəngi müxtəlifdir."},
            {"fa": "بعضی از انسان‌ها زردپوست هستند؛ بعضی سیاه‌پوست، برخی سرخ‌پوست و بعضی دیگر سفیدپوستند.", "reading_az": "Bəzi əz ensanha zərdpust həstənd; bəzi siyahpust, bərxi sorxpust va bəzi digər sefidpustənd.", "az": "Bəzi insanlar sarıdərilidir; bəzisi qaradərili, bir neçəsi qırmızıdərilidir və bəziləri isə ağdərilidirlər."},
            {"fa": "ما به وسیله‌ی پوست، گرمی، سردی، زبری و نرمی را احساس می‌کنیم.", "reading_az": "Ma be vəsileye pust, gərmi, sərdi, zebri va nərmi ra ehsas mikonim.", "az": "Biz dəri vasitəsilə istini, soyuğu, sərtliyi və yumşaqlığı hiss edirik."},
            {
                "fa": "در بدن انسان، بیش از دویست عدد استخوان وجود دارد.",
                "reading_az": "Dər bədəne ensan, biştər əz devist ədəd ostoxan vocud darəd.",
                "az": "İnsan bədənində iki yüzdən çox sümük var.",
                "new_paragraph": True,
            },
            {"fa": "استخوان‌ها بسیار محکم هستند.", "reading_az": "Ostoxanha besyar mohkəm həstənd.", "az": "Sümüklər çox möhkəmdir."},
            {"fa": "محکم‌ترین و بلندترین استخوان بدن انسان، استخوان ران است.", "reading_az": "Mohkəmtərin va boləndtərin ostoxane bədəne ensan, ostoxane ran əst.", "az": "İnsan bədəninin ən möhkəm və ən uzun sümüyü bud sümüyüdür."},
            {
                "fa": "در بدن انسان، دو چشم برای دیدن و دو گوش برای شنیدن وجود دارد.",
                "reading_az": "Dər bədəne ensan, do çeşm bəraye didən va do guş bəraye şənidən vocud darəd.",
                "az": "İnsan bədənində görmək üçün iki göz və eşitmək üçün iki qulaq var.",
                "new_paragraph": True,
            },
            {"fa": "بعضی از مردم، چشم‌هایشان ضعیف است و خوب نمی‌بینند.", "reading_az": "Bəzi əz mərdom, çeşmhayeşan zəif əst va xub nimibinənd.", "az": "Bəzi insanların gözləri zəifdir və yaxşı görmürlər."},
            {"fa": "آن‌ها برای بهتر دیدن از عینک استفاده می‌کنند.", "reading_az": "Anha bəraye behtər didən əz eynek estefade mikonənd.", "az": "Onlar daha yaxşı görmək üçün eynəkdən istifadə edirlər."},
            {
                "fa": "ما از بینی علاوه بر نفس کشیدن، بوی غذاها، گل‌ها، عطرها و... را احساس می‌کنیم.",
                "reading_az": "Ma əz bini əlave bər nəfəs kəşidən, buye qəzaha, golha, ətrha va... ra ehsas mikonim.",
                "az": "Biz burun vasitəsilə nəfəs almaqla yanaşı, yeməklərin, güllərin, ətirlərin qoxusunu da duyuruq.",
                "new_paragraph": True,
            },
            {"fa": "به وسیله‌ی زبان حرف می‌زنیم و طعم و مزه‌ی خوردنی‌ها، مانندِ شیرین بودنِ عسل، شور بودنِ نمک، تند بودنِ فلفل و ترش بودنِ بعضی از میوه‌ها را حس می‌کنیم.", "reading_az": "Be vəsileye zəban sohbət mizənim va təmu məzeye xordəniha, manənde şirin budəne əsəl, şur budəne nəmək, tond budəne felfel va torş budəne bəzi əz miveha ra hes mikonim.", "az": "Dil vasitəsilə danışırıq və yeməklərin dadını — balın şirinliyini, duzun şorluğunu, istiotun acılığını və bəzi meyvələrin turşluğunu hiss edirik."},
            {
                "fa": "در بدن ما اعضای دیگری هم وجود دارد، مانندِ قلب که به وسیله‌ی آن خون به همه‌جای بدن می‌رسد؛ پا که به وسیله‌ی آن راه می‌رویم و دست که به وسیله‌ی آن می‌نویسیم، غذا می‌خوریم و وسایل را برمی‌داریم.",
                "reading_az": "Dər bədəne ma əzaye digəri həm vocud darəd, manənde qəlb ke be vəsileye an xun be həmecaye bədən mirəsəd; pa ke be vəsileye an rah mirəvim va dəst ke be vəsileye an minəvisim, qəza mixorim va vəsayel ra bərmidarim.",
                "az": "Bədənimizdə başqa üzvlər də var: məsələn, qanın bədənin hər yerinə çatmasını təmin edən ürək; yeriməyimizə imkan verən ayaq və yazmağımıza, yemək yeməyimizə, əşyaları götürməyimizə kömək edən əl.",
                "new_paragraph": True,
            },
        ],
        "comprehension_questions": [
            {
                "question_fa": "پوست انسان‌ها چه رنگ است؟",
                "reading_az": "Puste ensanha çe rəng əst?",
                "az": "İnsanların dərisi nə rəngdədir?",
                "sample_answer_fa": "رنگ پوست انسان‌ها گوناگون است: زردپوست، سیاه‌پوست، سرخ‌پوست و سفیدپوست.",
                "sample_answer_reading_az": "Rənge puste ensanha gunagun əst: zərdpust, siyahpust, sorxpust va sefidpust.",
                "sample_answer_az": "İnsanların dərisinin rəngi müxtəlifdir: sarıdərililər, qaradərililər, qırmızıdərililər və ağdərililər.",
            },
            {
                "question_fa": "بلندترین استخوان بدن کدام است؟",
                "reading_az": "Boləndtərin ostoxane bədən kodam əst?",
                "az": "Bədənin ən uzun sümüyü hansıdır?",
                "sample_answer_fa": "محکم‌ترین و بلندترین استخوان بدن انسان، استخوان ران است.",
                "sample_answer_reading_az": "Mohkəmtərin va boləndtərin ostoxane bədəne ensan, ostoxane ran əst.",
                "sample_answer_az": "İnsan bədəninin ən möhkəm və ən uzun sümüyü bud sümüyüdür.",
            },
            {
                "question_fa": "بینی برای چیست؟",
                "reading_az": "Bini bəraye çist?",
                "az": "Burun nə üçündür?",
                "sample_answer_fa": "بینی برای نفس کشیدن و احساس کردن بوی غذاها، گل‌ها و عطرهاست.",
                "sample_answer_reading_az": "Bini bəraye nəfəs kəşidən va ehsas kərdəne buye qəzaha, golha va ətrhast.",
                "sample_answer_az": "Burun nəfəs almaq və yeməklərin, güllərin, ətirlərin qoxusunu duymaq üçündür.",
            },
            {
                "question_fa": "چرا بعضی از انسان‌ها از عینک استفاده می‌کنند؟",
                "reading_az": "Çəra bəzi əz ensanha əz eynek estefade mikonənd?",
                "az": "Niyə bəzi insanlar eynəkdən istifadə edirlər?",
                "sample_answer_fa": "چون چشم‌هایشان ضعیف است و برای بهتر دیدن از عینک استفاده می‌کنند.",
                "sample_answer_reading_az": "Çun çeşmhayeşan zəif əst va bəraye behtər didən əz eynek estefade mikonənd.",
                "sample_answer_az": "Çünki gözləri zəifdir və daha yaxşı görmək üçün eynəkdən istifadə edirlər.",
            },
            {
                "question_fa": "انسان از زبان برای چه کارهایی استفاده می‌کند؟",
                "reading_az": "Ensan əz zəban bəraye çe karhayi estefade mikonəd?",
                "az": "İnsan dildən hansı işlər üçün istifadə edir?",
                "sample_answer_fa": "انسان از زبان برای حرف زدن و احساس کردن طعم و مزه‌ی خوردنی‌ها استفاده می‌کند.",
                "sample_answer_reading_az": "Ensan əz zəban bəraye sohbət kərdən va ehsas kərdəne təmu məzeye xordəniha estefade mikonəd.",
                "sample_answer_az": "İnsan dildən danışmaq və yeməklərin dadını hiss etmək üçün istifadə edir.",
            },
            {
                "question_fa": "انسان به وسیله‌ی پوست، چه چیزهایی را احساس می‌کند؟",
                "reading_az": "Ensan be vəsileye pust, çe çizhayi ra ehsas mikonəd?",
                "az": "İnsan dəri vasitəsilə nələri hiss edir?",
                "sample_answer_fa": "انسان به وسیله‌ی پوست، گرمی، سردی، زبری و نرمی را احساس می‌کند.",
                "sample_answer_reading_az": "Ensan be vəsileye pust, gərmi, sərdi, zebri va nərmi ra ehsas mikonəd.",
                "sample_answer_az": "İnsan dəri vasitəsilə istini, soyuğu, sərtliyi və yumşaqlığı hiss edir.",
            },
            {
                "question_fa": "انسان به وسیله‌ی پاها و دست‌هایش چه کار می‌کند؟",
                "reading_az": "Ensan be vəsileye paha va dəsthayəş çe kar mikonəd?",
                "az": "İnsan ayaqları və əlləri ilə nə edir?",
                "sample_answer_fa": "به وسیله‌ی پا راه می‌رود و به وسیله‌ی دست می‌نویسد، غذا می‌خورد و وسایل را برمی‌دارد.",
                "sample_answer_reading_az": "Be vəsileye pa rah mirəvəd va be vəsileye dəst minəvisəd, qəza mixorəd va vəsayel ra bərmidarəd.",
                "sample_answer_az": "Ayaq vasitəsilə gəzir, əl vasitəsilə isə yazır, yemək yeyir və əşyaları götürür.",
            },
        ],
    },
}
