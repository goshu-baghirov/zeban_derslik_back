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
        {"fa": "صحبت می‌کند", "reading": "sohbət mikonəd", "az": "danişır, söhbət edir"},
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
        {"fa": "استخوان", "reading": "ostəxan", "az": "Sümük"},
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
                    "reading_az": "Aya an xaneye ziba male Əbbaş əst? Bəle, an xaneye ziba male Əbbas əst.",
                    "az": "O gözəl ev Abbasındır? Bəli, o gözəl ev Abbasındır.",
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
            "kind": "fill_blank",
            "title_fa": "لطفاً کامل کنید — اعضای بدن",
            "instruction_az": "Cümlələri mötərizədəki sözlərlə tamamlayın (کوتاه؛ دست؛ خون؛ قوی؛ بیست؛ بزرگ؛ پا)",
            "word_bank": ["کوتاه", "دست", "خون", "قوی", "بیست", "بزرگ", "پا"],
            "items": [
                {
                    "fa_with_blank": "شکم انسان‌های چاق، ...... است.",
                    "correct_answer": "بزرگ",
                    "reading_az": "Şekəme enşanhaye çağ, bozorg əst.",
                    "az": "Kök insanların qarnı böyükdür.",
                    "full_reading_az": "Şekəme enşanhaye çağ, bozorg əst.",
                    "full_translation_az": "Kök insanların qarnı böyükdür.",
                },
                {
                    "fa_with_blank": "در رگ‌های انسان ...... وجود دارد.",
                    "correct_answer": "خون",
                    "reading_az": "Dər rəghaye enşan xun vocud darəd.",
                    "az": "İnsanın damarlarında qan var.",
                    "full_reading_az": "Dər rəghaye enşan xun vocud darəd.",
                    "full_translation_az": "İnsanın damarlarında qan var.",
                },
                {
                    "fa_with_blank": "انسان ...... انگشت دارد.",
                    "correct_answer": "بیست",
                    "reading_az": "Ensan bist əngoşt darəd.",
                    "az": "İnsanın iyirmi barmağı var.",
                    "full_reading_az": "Ensan bist əngoşt darəd.",
                    "full_translation_az": "İnsanın iyirmi barmağı var.",
                },
                {
                    "fa_with_blank": "انسان دو ......، دو ...... و یک سر دارد.",
                    "correct_answer": "دست / پا",
                    "reading_az": "Ensan do dəst, do pa va yek sər darəd.",
                    "az": "İnsanın iki əli, iki ayağı və bir başı var.",
                    "full_reading_az": "Ensan do dəst, do pa va yek sər darəd.",
                    "full_translation_az": "İnsanın iki əli, iki ayağı və bir başı var.",
                },
                {
                    "fa_with_blank": "من روزهای جمعه ناخن‌هایم را ...... می‌کنم.",
                    "correct_answer": "کوتاه",
                    "reading_az": "Mən ruzhaye com'e naxonhayəm ra kotah mikonəm.",
                    "az": "Mən cümə günləri dırnaqlarımı tuturamm (qısaldıram).",
                    "full_reading_az": "Mən ruzhaye com'e naxonhayəm ra kotah mikonəm.",
                    "full_translation_az": "Mən cümə günləri dırnaqlarımı tuturamm (qısaldıram).",
                },
                {
                    "fa_with_blank": "بازوها و ماهیچه‌های آن جوان بسیار ...... هستند.",
                    "correct_answer": "قوی",
                    "reading_az": "Bazuha va mahiçehaye an cəvan besyar qəvi həstənd.",
                    "az": "O gəncin qolları və əzələləri çox güclüdür.",
                    "full_reading_az": "Bazuha va mahiçehaye an cəvan besyar qəvi həstənd.",
                    "full_translation_az": "O gəncin qolları və əzələləri çox güclüdür.",
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
                    "reading_az": "Dər surəte enşan çe çizhayi vocud darəd?",
                    "az": "İnsanın üzündə nələr var?",
                    "sample_answer_fa": "در صورت انسان چشم، ابرو، پلک، مژه، بینی، لب، چانه و گوش وجود دارد.",
                    "sample_answer_reading_az": "Dər surəte enşan çeşm, əbru, pelk, moje, bini, ləb, çane va guş vocud darəd.",
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
                    "reading_az": "Dər şekَme enşan çe çizhayi həst?",
                    "az": "İnsanın qarnında nələr var?",
                    "sample_answer_fa": "در شکم انسان معده، کلیه‌ها، کبد (جگر) و رودی بزرگ و کوچک قرار دارد.",
                    "sample_answer_reading_az": "Dər şekəme enşan moede, kolyeha, kəbed va rudeye bozorg va kuçək qərar darəd.",
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
            "kind": "fill_blank",
            "title_fa": "لطفاً کامل کنید — انسان و اعضای بدن",
            "instruction_az": "Cümlələri söz qutusu ilə tamamlayın (نمی‌بیند؛ نوزاد؛ کور؛ مهربان؛ نمی‌شنود؛ کر؛ معلول)",
            "word_bank": ["نمی‌بیند", "نوزاد", "کور", "مهربان", "نمی‌شنود", "کر", "معلول"],
            "items": [
                {
                    "fa_with_blank": "کسی که دیگران را دوست دارد و به آن‌ها کمک می‌کند، ...... است.",
                    "correct_answer": "مهربان",
                    "reading_az": "Kəsi ke digəran ra dust darəd va be anha komək mikonəd, mehrəban əst.",
                    "az": "Başqalarını sevən və onlara kömək edən şəxs mehribandır.",
                    "full_reading_az": "Kəsi ke digəran ra dust darəd va be anha komək mikonəd, mehrəban əst.",
                    "full_translation_az": "Başqalarını sevən və onlara kömək edən şəxs mehribandır.",
                },
                {
                    "fa_with_blank": "کسی که دست و پایش سالم نیست، ...... است.",
                    "correct_answer": "معلول",
                    "reading_az": "Kəsi ke dəst va payəş saləm nist, mə'lul əst.",
                    "az": "Əli və ayağı sağlam olmayan şəxs əlildir.",
                    "full_reading_az": "Kəsi ke dəst va payəş saləm nist, mə'lul əst.",
                    "full_translation_az": "Əli və ayağı sağlam olmayan şəxs əlildir.",
                },
                {
                    "fa_with_blank": "به بچه‌ای که دو، سه هفته سن دارد، ...... می‌گویند.",
                    "correct_answer": "نوزاد",
                    "reading_az": "Be bəççe-i ke do, se həfte sen darəd, nouzad miguyənd.",
                    "az": "İki-üç həftəlik uşağa körpə (yeni doğulmuş) deyirlər.",
                    "full_reading_az": "Be bəççe-i ke do, se həfte sen darəd, nouzad miguyənd.",
                    "full_translation_az": "İki-üç həftəlik uşağa körpə (yeni doğulmuş) deyirlər.",
                },
                {
                    "fa_with_blank": "نابینا کسی است که ...... .",
                    "correct_answer": "نمی‌بیند",
                    "reading_az": "Nabina kəsi əst ke nimibinəd.",
                    "az": "Gözdən əlil görməyən şəxsdir.",
                    "full_reading_az": "Nabina kəsi əst ke nimibinəd.",
                    "full_translation_az": "Gözdən əlil görməyən şəxsdir.",
                },
                {
                    "fa_with_blank": "ناشنوا کسی است که ...... .",
                    "correct_answer": "نمی‌شنود",
                    "reading_az": "Naşənva kəsi əst ke nimişənəvəd.",
                    "az": "Eşitmə əlili eşitməyən şəxsdir.",
                    "full_reading_az": "Naşənva kəsi əst ke nimişənəvəd.",
                    "full_translation_az": "Eşitmə əlili eşitməyən şəxsdir.",
                },
                {
                    "fa_with_blank": "اسم دیگر نابینا، ...... و اسم دیگر ناشنوا، ...... است.",
                    "correct_answer": "کور / کر",
                    "reading_az": "Esme digəre nabina kur va esme digəre naşənva kor əst.",
                    "az": "Gözdən əlilin başqa adı kor, eşitmə əlilininki isə kardır.",
                    "full_reading_az": "Esme digəre nabina kur va esme digəre naşənva kor əst.",
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
                "reading_az": "Dər surəte enşan çeşm, əbru, pelk, moje, bini va ləb qərar darəd.",
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
            "müxtəlifdir. Bəzi insanlar sarıdərilidir; bəzisi qarədərili, bir neçəsi qırmızıdərilidir və bəziləri "
            "isə ağdərilidirlər. Biz dəri vasitəsilə istini, soyuğu, sərtliyi və yumşaqlığı hiss edirik.\n\n"
            "İnsan bədənində iki yüzdən çox sümük var. Sümüklər çox möhkəmdir. İnsan bədəninin ən möhkəm və ən uzun sümüyü bud sümüyüdür.\n\n"
            "İnsan bədənində görmək üçün iki göz və eşitmək üçün iki qulaq var. Bəzi insanların gözləri zəifdir və yaxşı görmürlər. Onlar daha yaxşı görmək üçün eynəkdən istifadə edirlər.\n\n"
            "Biz burun vasitəsilə nəfəs almaqla yanaşı, yemeklərin, güllərin, ətirlərin qoxusunu da duyuruq. Dil vasitəsilə danışırıq və yeməklərin dadını — balın şirinliyini, duzun şorluğunu, istiotun acılığını və bəzi meyvələrin turşluğunu hiss edirik.\n\n"
            "Bədənimizdə başqa üzvlər də var: məsələn, qanın bədənin hər yerinə çatmasını təmin edən ürək; yeriməyimizə imkan verən ayaq və yazmağımıza, yemək yeməyimizə, əşyaları götürməyimizə kömək edən əl."
        ),
        "sentences": [
            {
                "fa": "بدن انسان قسمت‌های گوناگونی، مانندِ پوست، گوشت، خون، استخوان و... دارد.",
                "reading_az": "Bədəne enşan qəsməthaye gunaguni, manənde pust, guşt, xun, ostəxan va... darəd.",
                "az": "İnsan bədəninin dəri, ət, qan, sümük və s. kimi müxtəlif hissələri var.",
                "new_paragraph": True,
            },
            {"fa": "رنگ پوست انسان‌ها گوناگون است.", "reading_az": "Rənge puste enshanha gunagun əst.", "az": "İnsanların dərisinin rəngi müxtəlifdir."},
            {"fa": "بعضی از انسان‌ها زردپوست هستند؛ بعضی سیاه‌پوست، برخی سرخ‌پوست و بعضی دیگر سفیدپوستند.", "reading_az": "Bəzi əz enshanha zərdpust həstənd; bəzi siyahpust, bərxi sorxpust va bəzi digər sefidpustənd.", "az": "Bəzi insanlar sarıdərilidir; bəzisi qarədərili, bir neçəsi qırmızıdərilidir və bəziləri isə ağdərilidirlər."},
            {"fa": "ما به وسیله‌ی پوست، گرمی، سردی، زبری و نرمی را احساس می‌کنیم.", "reading_az": "Ma be vəsileye pust, gərmi, sərdi, zebri va nərmi ra ehsas mikonim.", "az": "Biz dəri vasitəsilə istini, soyuğu, sərtliyi və yumşaqlığı hiss edirik."},
            {
                "fa": "در بدن انسان، بیش از دویست عدد استخوان وجود دارد.",
                "reading_az": "Dər bədəne enşan, biştər əz devist ədəd ostəxan vocud darəd.",
                "az": "İnsan bədənində iki yüzdən çox sümük var.",
                "new_paragraph": True,
            },
            {"fa": "استخوان‌ها بسیار محکم هستند.", "reading_az": "Ostəxanha besyar mohkəm həstənd.", "az": "Sümüklər çox möhkəmdir."},
            {"fa": "محکم‌ترین و بلندترین استخوان بدن انسان، استخوان ران است.", "reading_az": "Mohkəmtərin va boləndtərin ostəxane bədəne enşan, ostəxane ran əst.", "az": "İnsan bədəninin ən möhkəm və ən uzun sümüyü bud sümüyüdür."},
            {
                "fa": "در بدن انسان، دو چشم برای دیدن و دو گوش برای شنیدن وجود دارد.",
                "reading_az": "Dər bədəne enşan, do çeşm bəraye didən va do guş bəraye şənidən vocud darəd.",
                "az": "İnsan bədənində görmək üçün iki göz və eşitmək üçün iki qulaq var.",
                "new_paragraph": True,
            },
            {"fa": "بعضی از مردم، چشم‌هایشان ضعیف است و خوب نمی‌بینند.", "reading_az": "Bəzi əz mərdom, çeşmhayeşan zəif əst va xub nimibinənd.", "az": "Bəzi insanların gözləri zəifdir və yaxşı görmürlər."},
            {"fa": "آن‌ها برای بهتر دیدن از عینک استفاده می‌کنند.", "reading_az": "Anha bəraye behtər didən əz eynek estefade mikonənd.", "az": "Onlar daha yaxşı görmək üçün eynəkdən istifadə edirlər."},
            {
                "fa": "ما از بینی علاوه بر نفس کشیدن، بوی غذاها، گل‌ها، عطرها و... را احساس می‌کنیم.",
                "reading_az": "Ma əz bini əlave bər nəfəs kəşidən, buye qəzaha, golha, ətrha va... ra ehsas mikonim.",
                "az": "Biz burun vasitəsilə nəfəs almaqla yanaşı, yemeklərin, güllərin, ətirlərin qoxusunu da duyuruq.",
                "new_paragraph": True,
            },
            {"fa": "به وسیله‌ی زبان حرف می‌زنیم و طعم و مزه‌ی خوردنی‌ها، مانندِ شیرین بودنِ عسل، شور بودنِ نمک، تند بودنِ فلفل و ترش بودنِ بعضی از میوه‌ها را حس می‌کنیم.", "reading_az": "Be vəsileye zəban sohbət mizənim va təmu məzeye xordəniha, manənde şirin budəne əsəl, şur budəne nəmək, tond budəne felfel va torş budəne bəzi əz miveha ra hes mikonim.", "az": "Dil vasitəsilə danışırıq və yeməklərin dadını — balın şirinliyini, duzun şorluğunu, istiotun acılığını və bəzi meyvələrin turşluğunu hiss edirik."},
            {
                "fa": "در بدن ما اعضای دیگری هم وجود دارد، مانندِ قلب که به وسیله‌ی آن خون به همه‌جای بدن می‌رسد؛ پا که به وسیله‌ی آن راه می‌رویم و دست که به وسیله‌ی آن می‌نویسیم، غذا می‌خریم و وسایل را برمی‌داریم.",
                "reading_az": "Dər bədəne ma əzaye digəri həm vocud darəd, manənde qəlb ke be vəsileye an xun be həmecaye bədən miræsəd; pa ke be vəsileye an rah mirəvim va dəst ke be vəsileye an minəvisim, qəza mixorim va vəsayel ra bərmidarim.",
                "az": "Bədənimizdə başqa üzvlər də var: məsələn, qanın bədənin hər yerinə çatmasını təmin edən ürək; yeriməyimizə imkan verən ayaq və yazmağımıza, yemək yeməyimizə, əşyaları götürməyimizə kömək edən əl.",
                "new_paragraph": True,
            },
        ],
        "comprehension_questions": [
            {
                "question_fa": "پوست انسان‌ها چه رنگ است؟",
                "reading_az": "Puste enshanha çe rəng əst?",
                "az": "İnsanların dərisi nə rəngdədir?",
                "sample_answer_fa": "رنگ پوست انسان‌ها گوناگون است: زردپوست، سیاه‌پوست، سرخ‌پوست و سفیدپوست.",
                "sample_answer_reading_az": "Rənge puste enshanha gunagun əst: zərdpust, siyahpust, sorxpust va sefidpust.",
                "sample_answer_az": "İnsanların dərisinin rəngi müxtəlifdir: sarıdərililər, qarədərililər, qırmızıdərililər və ağdərililər.",
            },
            {
                "question_fa": "بلندترین استخوان بدن کدام است؟",
                "reading_az": "Boləndtərin ostəxane bədən kodam əst?",
                "az": "Bədənin ən uzun sümüyü hansıdır?",
                "sample_answer_fa": "محکم‌ترین و بلندترین استخوان بدن انسان، استخوان ران است.",
                "sample_answer_reading_az": "Mohkəmtərin va boləndtərin ostəxane bədəne enşan, ostəxane ran əst.",
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
                "reading_az": "Çəra bəzi əz enshanha əz eynek estefade mikonənd?",
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
                "sample_answer_fa": "به وسیله‌ی پا راه می‌رود و به وسیله‌ی دست می‌نویسد، غذا می‌خورد و وسایل را برمی‌داریم.",
                "sample_answer_reading_az": "Be vəsileye pa rah mirəvəd va be vəsileye dəst minəvisəd, qəza mixorəd va vəsayel ra bərmidarəd.",
                "sample_answer_az": "Ayaq vasitəsilə gəzir, əl vasitəsilə isə yazır, yemək yeyir və əşyaları götürür.",
            },
        ],
    },
}
