# Dərs 12 — مسافرت (Səyahət)
# Mənbə: کتاب دوم, səh. 147-158

LESSON = {
    "number": 12,
    "title_fa": "مسافرت",
    "title_az": "Səyahət",
    "available": True,
    "vocabulary": [
        {"fa": "قارّه", "reading": "qarre", "az": "Qitə"},
        {"fa": "دفتر مسافرتی", "reading": "dəftəre mosaferəti", "az": "Turizm agentliyi"},
        {"fa": "بلیت", "reading": "belit", "az": "Bilet"},
        {"fa": "قطار شهری (مترو)", "reading": "qətare şəhri (metro)", "az": "Metro"},
        {"fa": "اتوبوس", "reading": "otobus", "az": "Avtobus"},
        {"fa": "پایانه‌ی مسافربری (ترمینال)", "reading": "payaneye mosaferbəri (terminal)", "az": "Avtovağzal (terminal)"},
        {"fa": "مسافر", "reading": "mosafer", "az": "Sərnişin, səyyah"},
        {"fa": "ایستگاه راه‌آهن", "reading": "istqahe rah-ahən", "az": "Dəmiryol stansiyası"},
        {"fa": "راه (جادّه)", "reading": "rah (cadde)", "az": "Yol"},
        {"fa": "تصادف", "reading": "təsadof", "az": "Qəza"},
        {"fa": "ترافیک", "reading": "terafik", "az": "Sıxlıq (tıxac)"},
        {"fa": "شلوغ", "reading": "şoluğ", "az": "İzdihamlı"},
        {"fa": "خلوت", "reading": "xəlvət", "az": "Sakit, boş"},
        {"fa": "نشانی (آدرس)", "reading": "neşani (adres)", "az": "Ünvan"},
        {"fa": "میدان", "reading": "meydan", "az": "Meydan"},
        {"fa": "چهارراه", "reading": "çəharrah", "az": "Dördyol ayrıcı"},
        {"fa": "کوچه", "reading": "kuçe", "az": "Döngə (dar küçə)"},
        {"fa": "بن‌بست", "reading": "bonbəst", "az": "Dalan"},
        {"fa": "اوّل، وسط، آخر", "reading": "əvvəl, vəsət, axər", "az": "Əvvəl, orta, son"},
        {"fa": "سمت راست، سمت چپ", "reading": "səmte rast, səmte çəp", "az": "Sağ tərəf, sol tərəf"},
        {"fa": "مستقیم", "reading": "mostəqim", "az": "Düz (istiqamətdə)"},
        {"fa": "کره‌ی زمین", "reading": "koreye zəmin", "az": "Yer kürəsi"},
        {"fa": "پلاک", "reading": "pelak", "az": "Ev nömrəsi (lövhə)"},
        {"fa": "سوار می‌شود", "reading": "səvar mişəvəd", "az": "minir"},
        {"fa": "پیاده می‌شود", "reading": "piyade mişəvəd", "az": "düşür (nəqliyyatdan)"},
        {"fa": "پیاده می‌رود", "reading": "piyade mirəvəd", "az": "piyada gedir"},
        {"fa": "می‌رسد", "reading": "miresəd", "az": "çatır"},
        {"fa": "ماشین شخصی", "reading": "maşine şəxsi", "az": "Şəxsi avtomobil"},
        {"fa": "پرترافیک", "reading": "porterafik", "az": "Sıxlıqlı (tıxaclı)"},
        {"fa": "تعطیلات", "reading": "tətilat", "az": "Tətil, istirahət"},
        {"fa": "بعضی از", "reading": "bəzi əz", "az": "…-dan bəzisi"},
        {"fa": "ابتدا", "reading": "ebteda", "az": "Əvvəlcə"},
        {"fa": "سپس", "reading": "səpəs", "az": "sonra"},
        {"fa": "سفر می‌کند (مسافرت می‌کند)", "reading": "səfər mikonəd (mosaferət mikonəd)", "az": "səyahət edir"},
        {"fa": "آب و هوا", "reading": "abohəva", "az": "İqlim"},
    ],
    "grammar_notes": [
        {
            "title_az": "«بعد؛ بعد از» ↔ «قبل؛ قبل از»",
            "title_fa": "«بعد»؛ «بعد از» — «قبل»؛ «قبل از»",
            "conjugations": [
                {"pronoun_fa": "من دو روز بعد در تهران هستم.", "form_fa": "من دو روز قبل در مشهد بودم."},
                {"pronoun_fa": "دوشنبه، بعد از یک‌شنبه است.", "form_fa": "یک‌شنبه، قبل از دوشنبه است."},
            ],
            "examples": [
                {"fa": "من الآن در کلاس هستم و سه ساعت بعد به خانه می‌روم.", "reading_az": "Mən əlan dər kelas hastəm va se saət bəd be xane mirəvəm.", "az": "Mən indi sinifdəyəm və üç saat sonra evə gedirəm."},
                {"fa": "کتاب‌خانه‌ی آیت‌الله مرعشی، بعد از حرم حضرت معصومه (س) و قبل از چهارراه شهدا است.", "reading_az": "Ketabxaneye Ayətollah Mərəşi, bəd əz hərəme həzrəte Məsume (s) va qəbl əz çəharrahe şohəda əst.", "az": "Ayətullah Mərəşi kitabxanası Məsumə həzrətlərinin hərəmindən sonra, şəhidlər dördyolundan əvvəldir."},
                {"fa": "یک‌شنبه، بعد از شنبه و قبل از دوشنبه است.", "reading_az": "Yekşənbe, bəd əz şənbe va qəbl əz doşənbe əst.", "az": "Bazar günü şənbədən sonra, bazar ertəsindən əvvəldir."},
                {"fa": "ما بعد از کتاب دوم، کتاب سوم را می‌خوانیم.", "reading_az": "Ma bəd əz ketabe dovvom, ketabe sevvom ra mixanim.", "az": "Biz ikinci kitabdan sonra üçüncü kitabı oxuyuruq."},
                {"fa": "فرودگاه مهرآباد تهران، بعد از میدان بزرگ آزادی است.", "reading_az": "Forudgahe Mehrabade Tehran, bəd əz meydane bozorge Azadi əst.", "az": "Tehranın Mehrabad hava limanı böyük Azadi meydanından sonradır."},
                {"fa": "من قبل از خوردن غذا و بعد از آن دست‌هایم را می‌شویم.", "reading_az": "Mən qəbl əz xordəne qəza va bəd əz an dəsthayəm ra mişuyəm.", "az": "Mən yeməkdən əvvəl və sonra əllərimi yuyuram."},
            ],
        },
        {
            "title_az": "Zaman zərfi «دیشب؛ امشب؛ فردا شب» + keçmiş zaman feli «رفتم؛ رفتی؛ …»",
            "title_fa": "قید زمان «... دیشب؛ امشب؛ فردا شب؛ ...» و فعل گذشته‌ی «رفتم؛ رفتی؛ ...»",
            "conjugations": [
                {"pronoun_fa": "پریشب", "form_fa": "دو شب قبل"},
                {"pronoun_fa": "دیشب", "form_fa": "یک شب قبل"},
                {"pronoun_fa": "امشب", "form_fa": "امروز شب"},
                {"pronoun_fa": "فرداشب", "form_fa": "یک شب بعد"},
                {"pronoun_fa": "پس‌فرداشب", "form_fa": "دو شب بعد"},
            ],
            "examples": [
                {"fa": "من دیشب به خانه‌ی پدرم رفتم. من امشب به خانه‌ی پدرم می‌روم.", "reading_az": "Mən dişəb be xaneye pedərəm rəftəm. Mən əmşəb be xaneye pedərəm mirəvəm.", "az": "Mən dünən gecə atamın evinə getdim. Mən bu gecə atamın evinə gedirəm."},
                {"fa": "من فرداشب به خانه‌ی برادرم می‌روم.", "reading_az": "Mən fərdaşəb be xaneye bəradərəm mirəvəm.", "az": "Mən sabah gecə qardaşımın evinə gedirəm."},
                {"fa": "طلبه‌ها هفته‌ی قبل به اصفهان رفتند و دو هفته‌ی بعد به مازندران می‌روند.", "reading_az": "Tələbeha həfteye qəbl be Esfəhan rəftənd va do həfteye bəd be Mazəndəran mirəvənd.", "az": "Tələbələr keçən həftə İsfahana getdilər və iki həftə sonra Mazandarana gedirlər."},
                {"fa": "برادرت دیشب به مسافرت رفت یا امشب می‌رود؟ او دو شب قبل به مسافرت رفت.", "reading_az": "Bəradərət dişəb be mosaferət rəft ya əmşəb mirəvəd? U do şəb qəbl be mosaferət rəft.", "az": "Qardaşın dünən gecə səyahətə getdi, yoxsa bu gecə gedir? O, iki gecə əvvəl səyahətə getdi."},
                {"fa": "خانواده‌ام دیروز برای زیارت امام رضا (ع) با قطار به مشهد رفتند. آن‌ها سه روز آن‌جا می‌مانند.", "reading_az": "Xanevadeəm diruz bəraye ziyarəte Emam Reza ba qətar be Məşhəd rəftənd. Anha se ruz anja mimanənd.", "az": "Ailəm dünən İmam Rzanı (ə) ziyarət etmək üçün qatarla Məşhədə getdi. Onlar üç gün orada qalırlar."},
                {"fa": "ما امروز، بعد از کلاس برای خواندن نماز به مسجد می‌رویم.", "reading_az": "Ma emruz, bəd əz kelas bəraye xandəne nəmaz be məsced mirəvim.", "az": "Biz bu gün dərsdən sonra namaz qılmaq üçün məscidə gedirik."},
                {"fa": "معصومه امروز، قبل از کلاس برای مطالعه و نوشتن تکلیف به کتاب‌خانه رفت.", "reading_az": "Məsume emruz, qəbl əz kelas bəraye motaleə va neveştəne təklif be ketabxane rəft.", "az": "Məsumə bu gün dərsdən əvvəl mütaliə etmək və tapşırıq yazmaq üçün kitabxanaya getdi."},
                {"fa": "من و دوستانم امروز صبح از خانه تا ایستگاه مترو پیاده رفتیم.", "reading_az": "Mən va dustanəm emruz sobh əz xane ta istqahe metro piyade rəftim.", "az": "Mən və dostlarım bu gün səhər evdən metro stansiyasına qədər piyada getdik."},
                {"fa": "پدرم پریشب با هواپیما به بیروت رفت. ایشان فرداشب برمی‌گردد.", "reading_az": "Pedərəm perişəb ba həvapeyma be Beyrut rəft. İşan fərdaşəb bərmigərdəd.", "az": "Atam iki gecə əvvəl təyyarə ilə Beyruta getdi. O sabah gecə qayıdır."},
                {"fa": "دوستم سه شب قبل برای دیدن خانواده‌اش به کشورش رفت. او دوازده روز بعد به ایران برمی‌گردد.", "reading_az": "Dustəm se şəb qəbl bəraye didəne xanevadeəş be kəşvərəş rəft. U davazdəh ruz bəd be Iran bərmigərdəd.", "az": "Dostum üç gecə əvvəl ailəsini görmək üçün öz ölkəsinə getdi. O, on iki gün sonra İrana qayıdır."},
            ],
        },
        {
            "title_az": "Zaman zərfi «پارسال؛ امسال؛ سال بعد» + keçmiş zaman feli «آمدم؛ آمدی؛ …»",
            "title_fa": "قید زمان «... پارسال؛ امسال؛ سال بعد؛ ...» و فعل گذشته‌ی «آمدم؛ آمدی؛ ...»",
            "conjugations": [
                {"pronoun_fa": "دو سال قبل", "form_fa": "پیرارسال"},
                {"pronoun_fa": "پارسال", "form_fa": "سال قبل"},
                {"pronoun_fa": "امسال", "form_fa": "سال جاری"},
                {"pronoun_fa": "یک سال بعد", "form_fa": "سال بعد"},
                {"pronoun_fa": "دو سال بعد", "form_fa": "دو سال بعد"},
            ],
            "examples": [
                {"fa": "من پارسال به ایران آمدم. من امسال به ایران آمدم.", "reading_az": "Mən parsal be Iran amədəm. Mən əmsal be Iran amədəm.", "az": "Mən keçən il İrana gəldim. Mən bu il İrana gəldim."},
                {"fa": "من یک سال بعد به لبنان می‌آیم. من دو سال بعد به لبنان می‌آیم.", "reading_az": "Mən yek sal bəd be Lobnan miayəm. Mən do sal bəd be Lobnan miayəm.", "az": "Mən bir il sonra Livana gəlirəm. Mən iki il sonra Livana gəlirəm."},
                {"fa": "مهدی و حسین دو سال قبل برای درس خواندن به ایران آمدند و چهار سال این‌جا می‌مانند.", "reading_az": "Mehdi va Hoseyn do sal qəbl bəraye dərsxandən be Iran amədənd va çəhar sal inja mimanənd.", "az": "Mehdi və Hüseyn iki il əvvəl oxumaq üçün İrana gəldilər və dörd il burada qalırlar."},
                {"fa": "پدر شما امسال به ایران می‌آید یا سال آینده؟ پدرم سال آینده به ایران می‌آید.", "reading_az": "Pedəre şoma əmsal be Iran miayəd ya sale ayənde? Pedərəm sale ayənde be Iran miayəd.", "az": "Sizin atanız bu il İrana gəlir, yoxsa gələn il? Atam gələn il İrana gəlir."},
                {"fa": "خانواده‌ام دو سال قبل برای زیارت به ایران آمدند؛ آن‌ها امسال هم می‌آیند.", "reading_az": "Xanevadeəm do sal qəbl bəraye ziyarət be Iran amədənd; anha əmsal həm miayənd.", "az": "Ailəm iki il əvvəl ziyarət üçün İrana gəldi; onlar bu il də gəlirlər."},
                {"fa": "زینب و خانواده‌اش پارسال برای زیارت خانه‌ی خدا به مکّه رفتند؛ آن‌ها امسال هم می‌روند.", "reading_az": "Zeynəb va xanevadeəş parsal bəraye ziyarəte xaneye Xoda be Məkke rəftənd; anha əmsal həm mirəvənd.", "az": "Zeynəb və ailəsi keçən il Allahın evini ziyarət etmək üçün Məkkəyə getdilər; onlar bu il də gedirlər."},
                {"fa": "من پارسال به شهر قم آمدم و خواهرم امسال می‌آید. ما دو سال بعد به کشورمان برمی‌گردیم.", "reading_az": "Mən parsal be şəhre Qom amədəm va xahərəm əmsal miayəd. Ma do sal bəd be kəşvəreman bərmigərdim.", "az": "Mən keçən il Qum şəhərinə gəldim, bacım isə bu il gəlir. Biz iki il sonra öz ölkəmizə qayıdırıq."},
                {"fa": "آیا شما سال گذشته این‌جا بودید؟ نه، من حدود دو ماه قبل به این‌جا آمدم.", "reading_az": "Aya şoma sale gozəşte inja budid? Nə, mən hodude do mah qəbl be inja amədəm.", "az": "Siz keçən il burada idiniz? Xeyr, mən təxminən iki ay əvvəl buraya gəldim."},
                {"fa": "شما چند سال بعد به کشورتان برمی‌گردید؟ من سه سال بعد به کشورم برمی‌گردم.", "reading_az": "Şoma çənd sal bəd be kəşvəretan bərmigərdid? Mən se sal bəd be kəşvərəm bərmigərdəm.", "az": "Siz neçə il sonra ölkənizə qayıdırsınız? Mən üç il sonra ölkəmə qayıdıram."},
                {"fa": "پدرم پارسال از بحرین تا مکّه پیاده رفت؛ ایشان امسال هم پیاده به مکّه می‌رود.", "reading_az": "Pedərəm parsal əz Bəhreyn ta Məkke piyade rəft; işan əmsal həm piyade be Məkke mirəvəd.", "az": "Atam keçən il Bəhreyndən Məkkəyə piyada getdi; o bu il də piyada Məkkəyə gedir."},
            ],
            "drills": [
                {
                    "title_fa": "مانند مثال تبدیل کنید",
                    "instruction_az": "Nümunə kimi əvəz edin: «دوستم سال بعد برای درس خواندن به این‌جا می‌آید. (پارسال) → دوستم پارسال برای درس خواندن به این‌جا آمد.»",
                    "items": [
                        {"prompt_fa": "ما سال آینده به کشورتان می‌آییم. (دو سال قبل)", "answer_fa": "ما دو سال قبل به کشورتان آمدیم.", "reading_az": "Ma do sal qəbl be kəşvəretan amədim.", "az": "Biz iki il əvvəl sizin ölkənizə gəldik."},
                        {"prompt_fa": "مهندس‌ها امسال برای ساختن پل به این‌جا می‌آیند. (پارسال)", "answer_fa": "مهندس‌ها پارسال برای ساختن پل به این‌جا آمدند.", "reading_az": "Mohəndesha parsal bəraye saxtəne pol be inja amədənd.", "az": "Mühəndislər keçən il körpü tikmək üçün buraya gəldilər."},
                        {"prompt_fa": "دوستانم پارسال برای دیدن من به این‌جا می‌آیند. (سال آینده)", "answer_fa": "دوستانم سال آینده برای دیدن من به این‌جا می‌آیند.", "reading_az": "Dustanəm sale ayənde bəraye didəne mən be inja miayənd.", "az": "Dostlarım gələn il məni görmək üçün buraya gəlirlər."},
                        {"prompt_fa": "حسین و همسرش سال بعد برای زندگی‌کردن به این شهر می‌آیند. (سال قبل)", "answer_fa": "حسین و همسرش سال قبل برای زندگی‌کردن به این شهر آمدند.", "reading_az": "Hoseyn va həmsərəş sale qəbl bəraye zendegikərdən be in şəhr amədənd.", "az": "Hüseyn və həyat yoldaşı keçən il bu şəhərdə yaşamaq üçün gəldilər."},
                        {"prompt_fa": "من امسال برای زیارت امام علی (ع) با هواپیما به شهر نجف می‌روم. (سال گذشته)", "answer_fa": "من سال گذشته برای زیارت امام علی (ع) با هواپیما به شهر نجف رفتم.", "reading_az": "Mən sale gozəşte bəraye ziyarəte Emam Əli ba həvapeyma be şəhre Nəcəf rəftəm.", "az": "Mən keçən il İmam Əlini (ə) ziyarət etmək üçün təyyarə ilə Nəcəf şəhərinə getdim."},
                        {"prompt_fa": "دکتر جوادی دیروز برای معاینه‌ی بیماران به این بیمارستان آمد. (پس‌فردا)", "answer_fa": "دکتر جوادی پس‌فردا برای معاینه‌ی بیماران به این بیمارستان می‌آید.", "reading_az": "Doktor Cavadi pəsfərda bəraye moayeneye bimaran be in bimarestan miayəd.", "az": "Doktor Cavadi birigün xəstələrin müayinəsi üçün bu xəstəxanaya gəlir."},
                    ],
                },
            ],
        },
        {
            "title_az": "«بعضی از» quruluşu (…-lərdən bəzisi)",
            "title_fa": "«بعضی از»",
            "conjugations": [
                {"pronoun_fa": "طلبه / شهر مشهد / درس", "form_fa": "بعضی از طلبه‌ها در شهر مشهد درس می‌خوانند."},
            ],
            "examples": [
                {"fa": "بعضی از مردم با ماشین شخصی مسافرت می‌کنند و بعضی هم به دفترهای مسافرتی می‌روند.", "reading_az": "Bəzi əz mərdom ba maşine şəxsi mosaferət mikonənd va bəzi həm be dəftərhaye mosaferəti mirəvənd.", "az": "İnsanların bəzisi şəxsi maşınla səyahət edir, bəzisi isə turizm agentliklərinə gedir."},
                {"fa": "بعضی از دانش‌جوها در کتاب‌خانه مطالعه می‌کنند.", "reading_az": "Bəzi əz daneşcuha dər ketabxane motaleə mikonənd.", "az": "Tələbələrin bəzisi kitabxanada mütaliə edir."},
                {"fa": "دوست من بعضی از روزهای هفته به باشگاه می‌رود.", "reading_az": "Duste mən bəzi əz ruzhaye həfte be başgah mirəvəd.", "az": "Dostum həftənin bəzi günləri idman zalına gedir."},
                {"fa": "بعضی از خانم‌ها در بیمارستان کار می‌کنند.", "reading_az": "Bəzi əz xanomha dər bimarestan kar mikonənd.", "az": "Xanımların bəzisi xəstəxanada işləyir."},
                {"fa": "بعضی از انسان‌ها با ماشین شخصی مسافرت می‌کنند.", "reading_az": "Bəzi əz insanha ba maşine şəxsi mosaferət mikonənd.", "az": "İnsanların bəzisi şəxsi avtomobillə səyahət edir."},
                {"fa": "در زبان فارسی پس از واژه‌های «بعضی از»، «بسیاری از» و «بیشتر»، واژه‌ی جمع یا اسم جمع می‌آید.", "reading_az": "Dər zəbane farsi pəs əz vajehaye «bəzi əz», «besyari əz» va «bişttər», vajeye cəm ya esme cəm miayəd.", "az": "Fars dilində «بعضی از», «بسیاری از» və «بیشتر» sözlərindən sonra cəm isim gəlir."},
            ],
            "drills": [
                {
                    "title_fa": "مانند مثال با واژه‌ی «بعضی از» جمله بگویید",
                    "instruction_az": "«بعضی از» ilə cümlə qurun: «طلبه / شهر مشهد / درس → بعضی از طلبه‌ها در شهر مشهد درس می‌خوانند.»",
                    "items": [
                        {"prompt_fa": "دوست من / قارّه‌ی اروپا / زندگی", "answer_fa": "بعضی از دوستان من در قارّه‌ی اروپا زندگی می‌کنند.", "reading_az": "Bəzi əz dustane mən dər qarreye Orupa zendegi mikonənd.", "az": "Dostlarımın bəzisi Avropa qitəsində yaşayır."},
                        {"prompt_fa": "خانم / بیمارستان / کار", "answer_fa": "بعضی از خانم‌ها در بیمارستان کار می‌کنند.", "reading_az": "Bəzi əz xanomha dər bimarestan kar mikonənd.", "az": "Xanımların bəzisi xəstəxanada işləyir."},
                        {"prompt_fa": "انسان / ماشین شخصی / مسافرت", "answer_fa": "بعضی از انسان‌ها با ماشین شخصی مسافرت می‌کنند.", "reading_az": "Bəzi əz insanha ba maşine şəxsi mosaferət mikonənd.", "az": "İnsanların bəzisi şəxsi avtomobillə səyahət edir."},
                        {"prompt_fa": "دانش‌جو / کتاب‌خانه / مطالعه", "answer_fa": "بعضی از دانش‌جوها در کتاب‌خانه مطالعه می‌کنند.", "reading_az": "Bəzi əz daneşcuha dər ketabxane motaleə mikonənd.", "az": "Tələbələrin bəzisi kitabxanada mütaliə edir."},
                    ],
                },
            ],
        },
    ],
    "exercises": [
        {
            "kind": "fill_blank",
            "instruction_az": "«قبل، قبل از، بعد، بعد از» ilə tamamlayın.",
            "word_bank": ["بعد از", "قبل از", "بعد", "قبل"],
            "items": [
                {
                    "fa_with_blank": "او ده روز ___ به کشورش می‌رود.",
                    "correct_answer": "بعد",
                    "reading_az": "bəd",
                    "az": "sonra",
                    "full_reading_az": "U dəh ruz bəd be kəşvərəş mirəvəd.",
                    "full_translation_az": "O, on gün sonra öz ölkəsinə gedir.",
                },
                {
                    "fa_with_blank": "پدر و مادرم دو هفته ___ در ایران بودند.",
                    "correct_answer": "قبل",
                    "reading_az": "qəbl",
                    "az": "əvvəl",
                    "full_reading_az": "Pedər va madərəm do həfte qəbl dər Iran budənd.",
                    "full_translation_az": "Ata-anam iki həftə əvvəl İranda idi.",
                },
                {
                    "fa_with_blank": "صندوق‌دار ___ گرفتنِ پول، آن را می‌شمارد.",
                    "correct_answer": "بعد از",
                    "reading_az": "bəd əz",
                    "az": "-dan sonra",
                    "full_reading_az": "Sənduqdar bəd əz gereftəne pul, an ra mişomarəd.",
                    "full_translation_az": "Kassir pulu aldıqdan sonra onu sayır.",
                },
                {
                    "fa_with_blank": "پنج‌شنبه ___ جمعه و ___ چهارشنبه است.",
                    "correct_answer": "قبل از",
                    "reading_az": "qəbl əz",
                    "az": "-dan əvvəl",
                    "full_reading_az": "Pəncşənbe qəbl əz come va bəd əz çəharşənbe əst.",
                    "full_translation_az": "Cümə axşamı cümədən əvvəl və çərşənbədən sonradır.",
                },
                {
                    "fa_with_blank": "مسافران ___ مسافرت از دفتر مسافرتی بلیت اتوبوس، قطار یا هواپیما می‌خرند.",
                    "correct_answer": "قبل از",
                    "reading_az": "qəbl əz",
                    "az": "-dan əvvəl",
                    "full_reading_az": "Mosaferan qəbl əz mosaferət əz dəftəre mosaferəti belite otobus, qətar ya həvapeyma mixərənd.",
                    "full_translation_az": "Sərnişinlər səyahətdən əvvəl turizm agentliyindən avtobus, qatar və ya təyyarə bileti alırlar.",
                },
            ],
        },
        {
            "kind": "fill_blank",
            "instruction_az": "Uyğun felin keçmiş zaman formasını yazın.",
            "word_bank": ["رفتم", "رفت", "برمی‌گردد", "رفتند", "آمدند"],
            "items": [
                {
                    "fa_with_blank": "من پریشب به خانه‌ی برادرم ___ .",
                    "correct_answer": "رفتم",
                    "reading_az": "rəftəm",
                    "az": "getdim",
                    "full_reading_az": "Mən perişəb be xaneye bəradərəm rəftəm.",
                    "full_translation_az": "Mən iki gecə əvvəl qardaşımın evinə getdim.",
                },
                {
                    "fa_with_blank": "دوستم دیشب به شمال ___ و فرداشب برمی‌گردد.",
                    "correct_answer": "رفت",
                    "reading_az": "rəft",
                    "az": "getdi",
                    "full_reading_az": "Dustəm dişəb be şomal rəft va fərdaşəb bərmigərdəd.",
                    "full_translation_az": "Dostum dünən gecə şimala getdi və sabah gecə qayıdır.",
                },
                {
                    "fa_with_blank": "علی سه شب قبل برای زیارت به مشهد رفت؛ برادرش دو شب بعد ___ .",
                    "correct_answer": "رفت",
                    "reading_az": "rəft",
                    "az": "getdi",
                    "full_reading_az": "Əli se şəb qəbl bəraye ziyarət be Məşhəd rəft; bəradərəş do şəb bəd rəft.",
                    "full_translation_az": "Əli üç gecə əvvəl ziyarət üçün Məşhədə getdi; qardaşı iki gecə sonra getdi.",
                },
                {
                    "fa_with_blank": "محسن و برادرش دیشب به خانه‌ی پدربزرگشان ___ و پس‌فردا شب برمی‌گردند.",
                    "correct_answer": "آمدند",
                    "reading_az": "amədənd",
                    "az": "gəldilər",
                    "full_reading_az": "Mohsen va bəradərəş dişəb be xaneye pedərbozorgeşan amədənd va pəsfərdaşəb bərmigərdənd.",
                    "full_translation_az": "Möhsün və qardaşı dünən gecə babalarının evinə gəldilər və srağagün gecə qayıdırlar.",
                },
                {
                    "fa_with_blank": "طلبه‌ها هفته‌ی قبل به اصفهان ___ .",
                    "correct_answer": "رفتند",
                    "reading_az": "rəftənd",
                    "az": "getdilər",
                    "full_reading_az": "Tələbeha həfteye qəbl be Esfəhan rəftənd.",
                    "full_translation_az": "Tələbələr keçən həftə İsfahana getdilər.",
                },
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Nümunə kimi cümlə qurun: «ما ساعت هفت سوار اتوبوس می‌شویم و ساعت هشت به مدرسه می‌رسیم.»",
            "items": [
                {
                    "prompt_fa": "مسافران / هواپیما / مشهد",
                    "answer_fa": "مسافران سوار هواپیما می‌شوند و به مشهد می‌رسند.",
                    "reading_az": "Mosaferan səvare həvapeyma mişəvənd va be Məşhəd miresənd.",
                    "az": "Sərnişinlər təyyarəyə minirlər və Məşhədə çatırlar.",
                },
                {
                    "prompt_fa": "کارگرها / مترو / کارخانه",
                    "answer_fa": "کارگرها سوار مترو می‌شوند و به کارخانه می‌رسند.",
                    "reading_az": "Kargərha səvare metro mişəvənd va be karxane miresənd.",
                    "az": "Fəhlələr metroya minirlər və zavoda çatırlar.",
                },
                {
                    "prompt_fa": "آن کشاورز / اسب / مزرعه",
                    "answer_fa": "آن کشاورز سوار اسب می‌شود و به مزرعه می‌رسد.",
                    "reading_az": "An keşavərz səvare əsb mişəvəd va be məzree miresəd.",
                    "az": "O əkinçi ata minir və tarlaya çatır.",
                },
                {
                    "prompt_fa": "من / ماشینم / دانش‌گاه",
                    "answer_fa": "من سوار ماشینم می‌شوم و به دانش‌گاه می‌رسم.",
                    "reading_az": "Mən səvare maşinəm mişəvəm va be daneşgah miresəm.",
                    "az": "Mən maşınıma minirəm və universitetə çatıram.",
                },
            ],
        },
    ],
    "sentence_practice": {
        "listen_exercises": [
            {
                "items": [
                    {
                        "fa": "در کره‌ی زمین، پنج قارّه به نام‌های آسیا، اروپا، آفریقا، آمریکا و اقیانوسیه وجود دارد.",
                        "reading_az": "Dər koreye zəmin, pənc qarre be namhaye Asiya, Orupa, Afriqa, Amrika va Oqyanusiye vocud darəd.",
                        "az": "Yer kürəsində Asiya, Avropa, Afrika, Amerika və Okeaniya adlı beş qitə var.",
                    },
                    {
                        "fa": "چین و اندونزی در قارّه‌ی آسیا، مصر و نیجریه در قارّه‌ی آفریقا قرار دارند.",
                        "reading_az": "Çin va Ondonezi dər qarreye Asiya, Mesr va Nijeriye dər qarreye Afriqa qərar darənd.",
                        "az": "Çin və Endoneziya Asiya qitəsində, Misir və Nigeriya isə Afrika qitəsində yerləşir.",
                    },
                    {
                        "fa": "حسین امروز به دفتر مسافرتی می‌رود و برای رفتن به کشورش بلیت هواپیما می‌خرد.",
                        "reading_az": "Hoseyn emruz be dəftəre mosaferəti mirəvəd va bəraye rəftən be kəşvərəş belite həvapeyma mixərəd.",
                        "az": "Hüseyn bu gün turizm agentliyinə gedir və öz ölkəsinə getmək üçün təyyarə bileti alır.",
                    },
                    {
                        "fa": "مسافران پس از خریدن بلیت به ایستگاه راه‌آهن می‌روند و سوار قطار می‌شوند.",
                        "reading_az": "Mosaferan pəs əz xəridəne belit be istqahe rah-ahən mirəvənd va səvare qətar mişəvənd.",
                        "az": "Sərnişinlər bilet aldıqdan sonra dəmiryol stansiyasına gedir və qatara minirlər.",
                    },
                    {
                        "fa": "مسافران برای خواندن نماز و خوردن ناهار از اتوبوس پیاده می‌شوند.",
                        "reading_az": "Mosaferan bəraye xandəne nəmaz va xordəne nahar əz otobus piyade mişəvənd.",
                        "az": "Sərnişinlər namaz qılmaq və nahar yemək üçün avtobusdan düşürlər.",
                    },
                    {
                        "fa": "امدادگران و پلیس‌ها هنگام تصادف به مردم کمک می‌کنند.",
                        "reading_az": "Emdadgəran va polisha hengame təsadof be mərdom komək mikonənd.",
                        "az": "Xilasedicilər və polislər qəza zamanı insanlara kömək edirlər.",
                    },
                    {
                        "fa": "من با دست چپ می‌نویسم و فرزندانم با دست راست می‌نویسند.",
                        "reading_az": "Mən ba dəste çəp minevisəm va fərzəndanəm ba dəste rast minevisənd.",
                        "az": "Mən sol əllə yazıram, övladlarım isə sağ əllə yazırlar.",
                    },
                    {
                        "fa": "من و دوستانم هر روز ساعت هفت سوار اتوبوس می‌شویم و ساعت هشت به دانش‌گاه می‌رسیم.",
                        "reading_az": "Mən va dustanəm hər ruz saəte həft səvare otobus mişəvim va saəte həşt be daneşgah miresim.",
                        "az": "Mən və dostlarım hər gün saat yeddidə avtobusa minirik və saat səkkizdə universitetə çatırıq.",
                    },
                    {
                        "fa": "عمویم هر روز صبح پیاده به محلّ‌کارش می‌رود و شب با مترو یا تاکسی به خانه برمی‌گردد.",
                        "reading_az": "Əmuyəm hər ruz sobh piyade be məhəllekarəş mirəvəd va şəb ba metro ya taksi be xane bərmigərdəd.",
                        "az": "Əmim hər gün səhər piyada iş yerinə gedir və gecə metro və ya taksi ilə evə qayıdır.",
                    },
                    {
                        "fa": "تصادف در خیابان‌های شلوغ و پرترافیک، بیشتر از خیابان‌های خلوت و کم‌ترافیک است.",
                        "reading_az": "Təsadof dər xiyabanhaye şoluğ va porterafik, bişttər əz xiyabanhaye xəlvət va kəmterafik əst.",
                        "az": "Qəza izdihamlı və tıxaclı küçələrdə, sakit və az sıxlıqlı küçələrdən daha çoxdur.",
                    },
                    {
                        "fa": "خانه‌ی امام خمینی (ره) در شهر قم، خیابان معلّم، اوّل کوچه‌ی ۱۱، سمت چپ قرار دارد.",
                        "reading_az": "Xaneye Emam Xomeyni dər şəhre Qom, xiyabane Moəllem, əvvəle kuçeye yazdəh, səmte çəp qərar darəd.",
                        "az": "İmam Xomeyninin (r) evi Qum şəhərində, Müəllim küçəsində, on birinci döngənin başında, sol tərəfdə yerləşir.",
                    },
                ],
            },
        ],
        "answer_items": [],
    },
    "reading_text": {
        "title_fa": "مسافرت",
        "title_az": "Səyahət",
        "paragraphs_fa": [
            "بسیاری از مردم جهان در روزهای تعطیل به مسافرت می‌روند. در این روزها بیشتر جادّه‌ها و خیابان‌ها شلوغ و پرترافیک است. بعضی از مردم با ماشین شخصی مسافرت می‌کنند و بعضی هم به دفترهای مسافرتی می‌روند و بلیت هواپیما، قطار یا اتوبوس می‌خرند.",
            "احمد و خانواده‌اش هر سال دو یا سه بار به مسافرت می‌روند. آن‌ها در تعطیلات عید نوروز برای دیدن پدر، مادر و بستگانشان به شهر همدان مسافرت می‌کنند و در روزهای اوّل تابستان، حدود چهار روز، برای زیارت امام رضا (ع) به مشهد می‌روند. آن‌ها هر سال در روزهای آخر تابستان به یکی از شهرهای زیبای ایران سفر می‌کنند.",
            "احمد و همسرش پارسال برای مسافرت، شهرهای اصفهان و شیراز را انتخاب کردند. آن‌ها ابتدا به اصفهان رفتند و سه روز در آن‌جا ماندند و سپس به شیراز مسافرت کردند. این دو شهر از شهرهای بزرگ، قدیمی و زیبای ایران هستند.",
            "آن‌ها امسال به شهرهای تبریز و اردبیل می‌روند. این دو شهر دارای کوه‌های بلند و آب‌وهوای بسیار خوبی است. احمد با خانواده‌اش ابتدا به اردبیل می‌روند و دو روز آن‌جا می‌مانند. آن‌ها سپس به شهر تبریز مسافرت می‌کنند.",
        ],
        "footnotes": [
            {"fa": "بعضی از", "az": "…-dan bəzisi"},
            {"fa": "ابتدا / سپس", "az": "əvvəlcə / sonra"},
            {"fa": "تعطیلات", "az": "tətil, istirahət"},
            {"fa": "آب‌وهوا", "az": "iqlim"},
        ],
        "full_translation_az": (
            "Dünya əhalisinin çoxu istirahət günlərində səyahətə çıxır. Bu günlərdə yolların və küçələrin çoxu "
            "izdihamlı və tıxaclı olur. İnsanların bəzisi şəxsi avtomobillə səyahət edir, bəzisi isə turizm "
            "agentliklərinə gedib təyyarə, qatar və ya avtobus bileti alır.\n\n"
            "Əhməd və ailəsi hər il iki-üç dəfə səyahətə gedir. Onlar Novruz bayramı tətilində ata, ana və "
            "qohumlarını görmək üçün Həmədan şəhərinə, yayın ilk günlərində isə təxminən dörd gün İmam Rzanı (ə) "
            "ziyarət etmək üçün Məşhədə gedirlər. Onlar hər il yayın son günlərində İranın gözəl şəhərlərindən "
            "birinə səyahət edirlər.\n\n"
            "Əhməd və həyat yoldaşı keçən il səyahət üçün İsfahan və Şiraz şəhərlərini seçdilər. Onlar əvvəlcə "
            "İsfahana getdilər və orada üç gün qaldılar, sonra isə Şiraza səyahət etdilər. Bu iki şəhər İranın "
            "böyük, qədim və gözəl şəhərlərindəndir.\n\n"
            "Onlar bu il Təbriz və Ərdəbil şəhərlərinə gedirlər. Bu iki şəhərin uca dağları və çox yaxşı iqlimi "
            "var. Əhməd ailəsi ilə əvvəlcə Ərdəbilə gedir və orada iki gün qalır. Sonra isə Təbriz şəhərinə "
            "səyahət edirlər."
        ),
        "sentences": [
            {
                "fa": "بسیاری از مردم جهان در روزهای تعطیل به مسافرت می‌روند.",
                "reading_az": "Besyari əz mərdome cəhan dər ruzhaye tətil be mosaferət mirəvənd.",
                "az": "Dünya əhalisinin çoxu istirahət günlərində səyahətə çıxır.",
                "new_paragraph": True,
            },
            {
                "fa": "در این روزها بیشتر جادّه‌ها و خیابان‌ها شلوغ و پرترافیک است.",
                "reading_az": "Dər in ruzha bişttər cadeha va xiyabanha şoluğ va porterafik əst.",
                "az": "Bu günlərdə yolların və küçələrin çoxu izdihamlı və tıxaclı olur.",
            },
            {
                "fa": "بعضی از مردم با ماشین شخصی مسافرت می‌کنند و بعضی هم به دفترهای مسافرتی می‌روند و بلیت هواپیما، قطار یا اتوبوس می‌خرند.",
                "reading_az": "Bəzi əz mərdom ba maşine şəxsi mosaferət mikonənd va bəzi həm be dəftərhaye mosaferəti mirəvənd va belite həvapeyma, qətar ya otobus mixərənd.",
                "az": "İnsanların bəzisi şəxsi avtomobillə səyahət edir, bəzisi isə turizm agentliklərinə gedib təyyarə, qatar və ya avtobus bileti alır.",
            },
            {
                "fa": "احمد و خانواده‌اش هر سال دو یا سه بار به مسافرت می‌روند.",
                "reading_az": "Əhməd va xanevadeəş hər sal do ya se bar be mosaferət mirəvənd.",
                "az": "Əhməd və ailəsi hər il iki-üç dəfə səyahətə gedir.",
                "new_paragraph": True,
            },
            {
                "fa": "آن‌ها در تعطیلات عید نوروز برای دیدن پدر، مادر و بستگانشان به شهر همدان مسافرت می‌کنند و در روزهای اوّل تابستان، حدود چهار روز، برای زیارت امام رضا (ع) به مشهد می‌روند.",
                "reading_az": "Anha dər tətilate eyde Novruz bəraye didəne pedər, madər va bəstegan-eşan be şəhre Həmədan mosaferət mikonənd va dər ruzhaye əvvəle tabestan, hodude çəhar ruz, bəraye ziyarəte Emam Reza be Məşhəd mirəvənd.",
                "az": "Onlar Novruz bayramı tətilində ata, ana və qohumlarını görmək üçün Həmədan şəhərinə, yayın ilk günlərində isə təxminən dörd gün İmam Rzanı (ə) ziyarət etmək üçün Məşhədə gedirlər.",
            },
            {
                "fa": "آن‌ها هر سال در روزهای آخر تابستان به یکی از شهرهای زیبای ایران سفر می‌کنند.",
                "reading_az": "Anha hər sal dər ruzhaye axəre tabestan be yeki əz şəhrhaye zibaye Iran səfər mikonənd.",
                "az": "Onlar hər il yayın son günlərində İranın gözəl şəhərlərindən birinə səyahət edirlər.",
            },
            {
                "fa": "احمد و همسرش پارسال برای مسافرت، شهرهای اصفهان و شیراز را انتخاب کردند.",
                "reading_az": "Əhməd va həmsərəş parsal bəraye mosaferət, şəhrhaye Esfəhan va Şiraz ra entexab kərdənd.",
                "az": "Əhməd və həyat yoldaşı keçən il səyahət üçün İsfahan və Şiraz şəhərlərini seçdilər.",
                "new_paragraph": True,
            },
            {
                "fa": "آن‌ها ابتدا به اصفهان رفتند و سه روز در آن‌جا ماندند و سپس به شیراز مسافرت کردند.",
                "reading_az": "Anha ebteda be Esfəhan rəftənd va se ruz dər anja mandənd va səpəs be Şiraz mosaferət kərdənd.",
                "az": "Onlar əvvəlcə İsfahana getdilər və orada üç gün qaldılar, sonra isə Şiraza səyahət etdilər.",
            },
            {
                "fa": "این دو شهر از شهرهای بزرگ، قدیمی و زیبای ایران هستند.",
                "reading_az": "İn do şəhr əz şəhrhaye bozorg, qədimi va zibaye Iran həstənd.",
                "az": "Bu iki şəhər İranın böyük, qədim və gözəl şəhərlərindəndir.",
            },
            {
                "fa": "آن‌ها امسال به شهرهای تبریز و اردبیل می‌روند.",
                "reading_az": "Anha əmsal be şəhrhaye Təbriz va Ərdəbil mirəvənd.",
                "az": "Onlar bu il Təbriz və Ərdəbil şəhərlərinə gedirlər.",
                "new_paragraph": True,
            },
            {
                "fa": "این دو شهر دارای کوه‌های بلند و آب‌وهوای بسیار خوبی است.",
                "reading_az": "İn do şəhr daraye kuhhaye bolənd va abohəvaye besyar xubi əst.",
                "az": "Bu iki şəhərin uca dağları və çox yaxşı iqlimi var.",
            },
            {
                "fa": "احمد با خانواده‌اش ابتدا به اردبیل می‌روند و دو روز آن‌جا می‌مانند.",
                "reading_az": "Əhməd ba xanevadeəş ebteda be Ərdəbil mirəvənd va do ruz anja mimanənd.",
                "az": "Əhməd ailəsi ilə əvvəlcə Ərdəbilə gedir və orada iki gün qalır.",
            },
            {
                "fa": "آن‌ها سپس به شهر تبریز مسافرت می‌کنند.",
                "reading_az": "Anha səpəs be şəhre Təbriz mosaferət mikonənd.",
                "az": "Sonra isə Təbriz şəhərinə səyahət edirlər.",
            },
        ],
        "comprehension_questions": [
            {
                "question_fa": "در چه روزهایی جادّه‌ها شلوغ و پرترافیک است؟",
                "reading_az": "Dər çe ruzhayi cadeha şoluğ va porterafik əst?",
                "az": "Yollar hansı günlərdə izdihamlı və tıxaclı olur?",
                "sample_answer_fa": "در روزهای تعطیل، بیشتر جادّه‌ها و خیابان‌ها شلوغ و پرترافیک است.",
                "sample_answer_reading_az": "Dər ruzhaye tətil, bişttər cadeha va xiyabanha şoluğ va porterafik əst.",
                "sample_answer_az": "İstirahət günlərində yolların və küçələrin çoxu izdihamlı və tıxaclı olur.",
            },
            {
                "question_fa": "مردم با چه چیزهایی مسافرت می‌کنند؟",
                "reading_az": "Mərdom ba çe çizhayi mosaferət mikonənd?",
                "az": "İnsanlar nə ilə səyahət edirlər?",
                "sample_answer_fa": "بعضی از مردم با ماشین شخصی مسافرت می‌کنند و بعضی هم با هواپیما، قطار یا اتوبوس.",
                "sample_answer_reading_az": "Bəzi əz mərdom ba maşine şəxsi mosaferət mikonənd va bəzi həm ba həvapeyma, qətar ya otobus.",
                "sample_answer_az": "İnsanların bəzisi şəxsi avtomobillə, bəzisi isə təyyarə, qatar və ya avtobusla səyahət edir.",
            },
            {
                "question_fa": "احمد و خانواده‌اش هر سال چند بار به مسافرت می‌روند؟",
                "reading_az": "Əhməd va xanevadeəş hər sal çənd bar be mosaferət mirəvənd?",
                "az": "Əhməd və ailəsi hər il neçə dəfə səyahətə gedir?",
                "sample_answer_fa": "احمد و خانواده‌اش هر سال دو یا سه بار به مسافرت می‌روند.",
                "sample_answer_reading_az": "Əhməd va xanevadeəş hər sal do ya se bar be mosaferət mirəvənd.",
                "sample_answer_az": "Əhməd və ailəsi hər il iki-üç dəfə səyahətə gedir.",
            },
            {
                "question_fa": "آن‌ها برای دیدن چه کسانی به همدان می‌روند؟",
                "reading_az": "Anha bəraye didəne çe kəsani be Həmədan mirəvənd?",
                "az": "Onlar kimləri görmək üçün Həmədana gedirlər?",
                "sample_answer_fa": "آن‌ها برای دیدن پدر، مادر و بستگانشان به همدان می‌روند.",
                "sample_answer_reading_az": "Anha bəraye didəne pedər, madər va bəstegan-eşan be Həmədan mirəvənd.",
                "sample_answer_az": "Onlar ata, ana və qohumlarını görmək üçün Həmədana gedirlər.",
            },
            {
                "question_fa": "احمد و همسرش پارسال به کجا مسافرت کردند؟",
                "reading_az": "Əhməd va həmsərəş parsal be koca mosaferət kərdənd?",
                "az": "Əhməd və həyat yoldaşı keçən il haraya səyahət etdi?",
                "sample_answer_fa": "احمد و همسرش پارسال به اصفهان و شیراز مسافرت کردند.",
                "sample_answer_reading_az": "Əhməd va həmsərəş parsal be Esfəhan va Şiraz mosaferət kərdənd.",
                "sample_answer_az": "Əhməd və həyat yoldaşı keçən il İsfahan və Şiraza səyahət etdi.",
            },
            {
                "question_fa": "آن‌ها هر سال چه روزهایی به حرم امام رضا (ع) می‌روند؟",
                "reading_az": "Anha hər sal çe ruzhayi be hərəme Emam Reza mirəvənd?",
                "az": "Onlar hər il hansı günlərdə İmam Rzanın hərəminə gedirlər?",
                "sample_answer_fa": "آن‌ها هر سال در روزهای اوّل تابستان به حرم امام رضا (ع) می‌روند.",
                "sample_answer_reading_az": "Anha hər sal dər ruzhaye əvvəle tabestan be hərəme Emam Reza mirəvənd.",
                "sample_answer_az": "Onlar hər il yayın ilk günlərində İmam Rzanın hərəminə gedirlər.",
            },
            {
                "question_fa": "احمد و خانواده‌اش چند روز در اردبیل می‌مانند؟",
                "reading_az": "Əhməd va xanevadeəş çənd ruz dər Ərdəbil mimanənd?",
                "az": "Əhməd və ailəsi Ərdəbildə neçə gün qalırlar?",
                "sample_answer_fa": "آن‌ها دو روز در اردبیل می‌مانند.",
                "sample_answer_reading_az": "Anha do ruz dər Ərdəbil mimanənd.",
                "sample_answer_az": "Onlar Ərdəbildə iki gün qalırlar.",
            },
        ],
    },
}
