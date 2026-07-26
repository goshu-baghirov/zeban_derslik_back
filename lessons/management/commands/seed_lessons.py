"""Import the lesson content that currently lives as static Dart code in the
Flutter app (lib/data/lesson1_content.dart, lesson2_content.dart,
lessons_repository.dart) into the database, so it is editable from the admin
panel. Re-running this command is safe: each lesson's children are replaced.
"""
from pathlib import Path

from django.core.files import File
from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from lessons.models import lesson_image_path

from lessons.models import (
    AnswerQuestionExercise,
    AnswerQuestionExerciseItem,
    AnswerQuestionSentence,
    ConjugationRow,
    ExampleSentence,
    FillBlankExercise,
    FillBlankItem,
    Grade,
    GrammarNote,
    Lesson,
    ListenReadExercise,
    ListenReadSentence,
    PictureSentenceExercise,
    PictureSentenceItem,
    PictureSentenceLine,
    PracticeRevealExercise,
    PracticeRevealItem,
    ReadingComprehensionQuestion,
    ReadingFootnote,
    ReadingText,
    SentencePractice,
    VocabWord,
)
from .lesson_data import LESSONS as EXTRA_LESSONS

DEFAULT_ASSETS_DIR = Path(r"C:\Users\bagir\Desktop\zeban_derslik_mobile")

UPCOMING_TITLES = [
    ("انسان؛ خانواده و بستگان", "İnsan; ailə və qohumlar"),
    ("شغل ۱", "Peşə 1"),
    ("شغل ۲", "Peşə 2"),
    ("رنگ‌ها", "Rənglər"),
    ("پوشاک (لباس)", "Geyim"),
    ("وسایل شخصی", "Şəxsi əşyalar"),
    ("عدد (۱)", "Ədəd (1)"),
    ("عدد (۲)", "Ədəd (2)"),
    ("مکان", "Yer"),
    ("مسافرت", "Səyahət"),
    ("طبیعت", "Təbiət"),
    ("ساعت و زمان", "Saat və vaxt"),
    ("غذا", "Yemək"),
    ("میوه‌ها و سبزی‌ها", "Meyvə və tərəvəzlər"),
    ("صفت‌ها", "Sifətlər"),
    ("انسان و اعضای بدن", "İnsan və bədən üzvləri"),
    ("پزشکی", "Tibb"),
    ("ورزش", "İdman"),
]

LESSON_1 = {
    "number": 1,
    "title_fa": "نوشت‌افزار",
    "title_az": "Yazı ləvazimatı",
    "available": True,
    "vocabulary": [
        {"fa": "غلط‌گیر", "reading": "qələtgir", "az": "Qələtgir (korrektor)", "image": "assets/images/lessons/lesson_01/qaletgir.png"},
        {"fa": "خودنویس", "reading": "xodnevis", "az": "Dolma qələm", "image": "assets/images/lessons/lesson_01/khodnevis.png"},
        {"fa": "خودکار", "reading": "xodkar", "az": "Tükənməz qələm", "image": "assets/images/lessons/lesson_01/khodkar.png"},
        {"fa": "تابلو", "reading": "tablo", "az": "Lövhə (molbert)", "image": "assets/images/lessons/lesson_01/tablo.png"},
        {"fa": "کاغذ؛ مقوّا", "reading": "kağəz; moqəvva", "az": "Kağız; karton", "image": "assets/images/lessons/lesson_01/kaghaz_moqava.png"},
        {"fa": "دفتر", "reading": "dəftər", "az": "Dəftər", "image": "assets/images/lessons/lesson_01/daftar.png"},
        {"fa": "مدادتراش", "reading": "medadtəraş", "az": "Qələmyonan", "image": "assets/images/lessons/lesson_01/medadtarash.png"},
        {"fa": "پاک‌کن", "reading": "pak-kon", "az": "Pozan", "image": "assets/images/lessons/lesson_01/pakkon.png"},
        {"fa": "ماژیک", "reading": "majik", "az": "Marker", "image": "assets/images/lessons/lesson_01/majik.png"},
        {"fa": "خط‌کش", "reading": "xətkeş", "az": "Xətkeş", "image": "assets/images/lessons/lesson_01/khatkesh.png"},
        {"fa": "جامدادی", "reading": "camedadi", "az": "Qələmqabı", "image": "assets/images/lessons/lesson_01/jamedadi.png"},
        {"fa": "مدادرنگی", "reading": "medadrəngi", "az": "Rəngli karandaşlar", "image": "assets/images/lessons/lesson_01/medadrangi.png"},
        {"fa": "پوشه", "reading": "puşe", "az": "Qovluq", "image": "assets/images/lessons/lesson_01/pushe.png"},
        {"fa": "گیره", "reading": "gire", "az": "Qısqac (klips)", "image": "assets/images/lessons/lesson_01/gire.png"},
        {"fa": "زیردستی", "reading": "zirdəsti", "az": "Yazı altlığı", "image": "assets/images/lessons/lesson_01/zirdasti.png"},
        {"fa": "پرگار", "reading": "pərgar", "az": "Pərgar", "image": "assets/images/lessons/lesson_01/pargar.png"},
        {"fa": "منگنه", "reading": "məngəne", "az": "Stepler", "image": "assets/images/lessons/lesson_01/mangane.png"},
        {"fa": "چسب", "reading": "çəsb", "az": "Yapışqan (skoç)", "image": "assets/images/lessons/lesson_01/chasb.png"},
        {"fa": "چراغ مطالعه", "reading": "çerağe motaleə", "az": "Masa lampası", "image": "assets/images/lessons/lesson_01/cheraghe_motalee.png"},
        {"fa": "تقویم", "reading": "təqvim", "az": "Təqvim", "image": "assets/images/lessons/lesson_01/taqvim.png"},
        {"fa": "پاکت‌نامه", "reading": "pakətname", "az": "Zərf", "image": "assets/images/lessons/lesson_01/pakatname.png"},
        {"fa": "می‌گذارد", "reading": "migozarəd", "az": "qoyur", "image": "assets/images/lessons/lesson_01/migozarad.png"},
        {"fa": "نقّاشی می‌کشد", "reading": "nəqqaşi mikeşəd", "az": "rəsm çəkir", "image": "assets/images/lessons/lesson_01/naghashi_mikeshad.png"},
        {"fa": "پاک می‌کند", "reading": "pak mikonəd", "az": "silir", "image": "assets/images/lessons/lesson_01/pak_mikonad.png"},
        {"fa": "مداد", "reading": "medad", "az": "karandaş"},
        {"fa": "کاغذ", "reading": "kağəz", "az": "kağız"},
        {"fa": "ماشین‌حساب", "reading": "maşin-hesab", "az": "kalkulyator"},
        {"fa": "کیف", "reading": "kif", "az": "çanta"},
        {"fa": "رایانه", "reading": "rayane", "az": "komputer"},
    ],
    "grammar_notes": [
        {
            "title_az": 'Mənfi fel "نیست" (deyil)',
            "title_fa": "فعل منفیِ «نیست»",
            "conjugations": [],
            "examples": [
                {"fa": "این کتاب است.", "az": "Bu kitabdır."},
                {"fa": "این کتاب نیست؛ این دفتر است.", "az": "Bu kitab deyil; bu dəftərdir."},
                {"fa": "این مدادتراش نیست؛ این پاک‌کن است.", "az": "Bu qələmyonan deyil; bu pozandır."},
                {"fa": "این خودکار نیست؛ خودنویس است.", "az": "Bu tükənməz qələm deyil; dolma qələmdir."},
                {
                    "fa": "کتاب، زیر میز نیست؛ روی میز است.",
                    "reading_az": "Ketab, zire miz nist; ruye miz əst.",
                    "az": "Kitab masanın altında deyil; masanın üstündədir.",
                },
                {
                    "fa": "آن چراغ مطالعه، سبز نیست؛ آبی است.",
                    "reading_az": "An çərağe motale'e, səbz nist; abi əst.",
                    "az": "O oxu lampası yaşıl deyil; mavidir.",
                },
                {
                    "fa": "این ماشین‌حساب است؛ منگنه نیست.",
                    "reading_az": "İn maşinhesab əst; mengəne nist.",
                    "az": "Bu kalkulyatordur; stepler deyil.",
                },
            ],
            "drills": [
                {
                    "title_fa": "مانند مثال جایگزین کنید",
                    "instruction_az": "Nümunə kimi əvəz edin",
                    "example_fa": "این مدادرنگی، سبز *نیست*؛ قرمز *است*.",
                    "example_prompt_fa": "ماژیک / سیاه‌آبی",
                    "example_answer_fa": "این ماژیک، سیاه *نیست*؛ آبی *است*.",
                    "items": [
                        {
                            "prompt_fa": "پوشه / زرد / قرمز",
                            "answer_fa": "این پوشه، زرد نیست؛ قرمز است.",
                            "reading_az": "İn puşe, zərd nist; qermez əst.",
                            "az": "Bu qovluq sarı deyil; qırmızıdır.",
                        },
                        {
                            "prompt_fa": "تابلو / کوچک / بزرگ",
                            "answer_fa": "این تابلو، کوچک نیست؛ بزرگ است.",
                            "reading_az": "İn tablo, kuçek nist; bozorg əst.",
                            "az": "Bu lövhə kiçik deyil; böyükdür.",
                        },
                        {
                            "prompt_fa": "جامدادی / قرمز / صورتی",
                            "answer_fa": "این جامدادی، قرمز نیست؛ صورتی است.",
                            "reading_az": "İn camedadi, qermez nist; surəti əst.",
                            "az": "Bu qələmqabı qırmızı deyil; çəhrayıdır.",
                        },
                        {
                            "prompt_fa": "پاک‌کن / کثیف / تمیز",
                            "answer_fa": "این پاک‌کن، کثیف نیست؛ تمیز است.",
                            "reading_az": "İn pak-kon, kəsif nist; təmiz əst.",
                            "az": "Bu pozan çirkli deyil; təmizdir.",
                        },
                        {
                            "prompt_fa": "زیردستی / بزرگ / کوچک",
                            "answer_fa": "این زیردستی، بزرگ نیست؛ کوچک است.",
                            "reading_az": "İn zirdəsti, bozorg nist; kuçek əst.",
                            "az": "Bu yazı altlığı böyük deyil; kiçikdir.",
                        },
                        {
                            "prompt_fa": "خط‌کش / قهوه‌ای / سبز",
                            "answer_fa": "این خط‌کش، قهوه‌ای نیست؛ سبز است.",
                            "reading_az": "İn xətkeş, qəhvei nist; səbz əst.",
                            "az": "Bu xətkeş qəhvəyi deyil; yaşıldır.",
                        },
                    ],
                },
            ],
        },
        {
            "title_az": 'Mənfi fel "ندارم؛ نداری؛ ..." (yoxdur)',
            "title_fa": "فعل منفیِ «ندارم؛ نداری؛ ...»",
            "conjugations": [
                {"pronoun_fa": "من", "form_fa": "دارم / ندارم"},
                {"pronoun_fa": "تو", "form_fa": "داری / نداری"},
                {"pronoun_fa": "او", "form_fa": "دارد / ندارد"},
                {"pronoun_fa": "ما", "form_fa": "داریم / نداریم"},
                {"pronoun_fa": "شما", "form_fa": "دارید / ندارید"},
                {"pronoun_fa": "آن‌ها", "form_fa": "دارند / ندارند"},
            ],
            "examples": [
                {"fa": "من خودکار دارم؛ دفتر ندارم.", "az": "Mənim tükənməz qələmim var; dəftərim yoxdur."},
                {"fa": "ما پاکت‌نامه داریم؛ پوشه نداریم.", "az": "Bizim zərfimiz var; qovluğumuz yoxdur."},
                {
                    "fa": "من کاغذ دارم؛ دفتر ندارم.",
                    "reading_az": "Mən kağəz daram; dəftər nədaram.",
                    "az": "Mənim kağızım var; dəftərim yoxdur.",
                },
                {
                    "fa": "او پاک‌کن ندارد؛ غلط‌گیر دارد.",
                    "reading_az": "U pakkon nədarəd; qəltgir darəd.",
                    "az": "Onun pozanı yoxdur; korrektoru var.",
                },
                {
                    "fa": "شما خط‌کش دارید؛ ما خط‌کش نداریم.",
                    "reading_az": "Şoma xətkeş darid; ma xətkeş nədarim.",
                    "az": "Sizin xətkeşiniz var; bizim xətkeşimiz yoxdur.",
                },
                {
                    "fa": "ما ماژیک نداریم؛ مدادرنگی داریم.",
                    "reading_az": "Ma majik nədarim; medad-rəngi darim.",
                    "az": "Bizim markerimiz yoxdur; rəngli karandaşımız var.",
                },
                {
                    "fa": "آن‌ها پاکت‌نامه ندارند؛ من پاکت‌نامه دارم.",
                    "reading_az": "Anha pakət-name nədarənd; mən pakət-name daram.",
                    "az": "Onların zərfi yoxdur; mənim zərfim var.",
                },
                {
                    "fa": "شما (تو) تقویم نداری؛ احمد تقویم دارد.",
                    "reading_az": "To təqvim nədari; Əhməd təqvim darəd.",
                    "az": "Sənin təqvimin yoxdur; Əhmədin təqvimi var.",
                },
                {
                    "fa": "حسین و مهدی پوشه ندارند؛ زیردستی دارند.",
                    "reading_az": "Hoseyn və Mehdi puşe nədarənd; zirdəsti darənd.",
                    "az": "Hüseynlə Mehdinin qovluğu yoxdur; yazı altlıqları var.",
                },
            ],
            "drills": [
                {
                    "title_fa": "مانند مثال جایگزین کنید",
                    "instruction_az": "Nümunə kimi əvəz edin",
                    "example_fa": "ما پاکت‌نامه *داریم*؛ پوشه *نداریم*.",
                    "example_prompt_fa": "آن‌ها / مداد / مدادتراش",
                    "example_answer_fa": "آن‌ها مداد *دارند*؛ مدادتراش *ندارند*.",
                    "items": [
                        {
                            "prompt_fa": "ما / کاغذ / مقوّا",
                            "answer_fa": "ما کاغذ داریم؛ مقوّا نداریم.",
                            "reading_az": "Ma kağəz darim; moqəvva nədarim.",
                            "az": "Bizim kağızımız var; kartonumuz yoxdur.",
                        },
                        {
                            "prompt_fa": "او / عینک / عصا",
                            "answer_fa": "او عینک دارد؛ عصا ندارد.",
                            "reading_az": "U eynək darəd; əsa nədarəd.",
                            "az": "Onun eynəyi var; əsası yoxdur.",
                        },
                        {
                            "prompt_fa": "شما / قاشق / چنگال",
                            "answer_fa": "شما قاشق دارید؛ چنگال ندارید.",
                            "reading_az": "Şoma qaşoq darid; çəngal nədarid.",
                            "az": "Sizin qaşığınız var; çəngəliniz yoxdur.",
                        },
                        {
                            "prompt_fa": "من / منگنه / چسب",
                            "answer_fa": "من منگنه دارم؛ چسب ندارم.",
                            "reading_az": "Mən mengəne daram; çəsb nədaram.",
                            "az": "Mənim steplerim var; yapışqanım yoxdur.",
                        },
                        {
                            "prompt_fa": "درخت / ریشه / ریش",
                            "answer_fa": "درخت ریشه دارد؛ ریش ندارد.",
                            "reading_az": "Dərəxt riše darəd; riš nədarəd.",
                            "az": "Ağacın kökü var; saqqalı yoxdur.",
                        },
                        {
                            "prompt_fa": "آن‌ها / میز / چراغ مطالعه",
                            "answer_fa": "آن‌ها میز دارند؛ چراغ مطالعه ندارند.",
                            "reading_az": "Anha miz darənd; çərağe motale'e nədarənd.",
                            "az": "Onların masası var; oxu lampası yoxdur.",
                        },
                    ],
                },
                {
                    "title_fa": "مانند مثال بگویید",
                    "instruction_az": "Nümunə kimi deyin",
                    "example_fa": "من ماژیک *دارم*؛ مدادرنگی *ندارم*.",
                    "example_reading_az": "Mən majik daram; medad-rəngi nədaram.",
                    "example_az": "Mənim markerim var; rəngli karandaşım yoxdur.",
                    "example_image_have": "assets/images/lessons/lesson_01/majik.png",
                    "example_image_not_have": "assets/images/lessons/lesson_01/medadrangi.png",
                    "items": [
                        {
                            "prompt_fa": "ما",
                            "answer_fa": "ما خط‌کش داریم؛ پرگار نداریم.",
                            "reading_az": "Ma xətkeş darim; pərgar nədarim.",
                            "az": "Bizim xətkeşimiz var; pərgarımız yoxdur.",
                            "image_have": "assets/images/lessons/lesson_01/khatkesh.png",
                            "image_not_have": "assets/images/lessons/lesson_01/pargar.png",
                        },
                        {
                            "prompt_fa": "این خانم",
                            "answer_fa": "این خانم قیچی دارد؛ گونیا ندارد.",
                            "reading_az": "In xanom qeyçi darəd; gunya nədarəd.",
                            "az": "Bu xanımın qayçısı var; guniyası yoxdur.",
                            "image_have": "assets/images/lessons/lesson_01/qeychi.png",
                            "image_not_have": "assets/images/lessons/lesson_01/gunya.png",
                        },
                        {
                            "prompt_fa": "احمد",
                            "answer_fa": "احمد پاک‌کن دارد؛ ماژیک ندارد.",
                            "reading_az": "Əhməd pakkon darəd; majik nədarəd.",
                            "az": "Əhmədin pozanı var; markeri yoxdur.",
                            "image_have": "assets/images/lessons/lesson_01/pakkon.png",
                            "image_not_have": "assets/images/lessons/lesson_01/majik.png",
                        },
                        {
                            "prompt_fa": "شما (تو)",
                            "answer_fa": "شما (تو) رایانه داری؛ دوربین نداری.",
                            "reading_az": "To rayane dari; durbin nədari.",
                            "az": "Sənin komputerin var; fotoaparatın yoxdur.",
                            "image_have": "assets/images/lessons/lesson_01/rayaneh.png",
                            "image_not_have": "assets/images/lessons/lesson_01/durbin.png",
                        },
                        {
                            "prompt_fa": "آن‌ها",
                            "answer_fa": "آن‌ها پوشه دارند؛ تخته‌شاسی ندارند.",
                            "reading_az": "Anha puşe darənd; təxte-şasi nədarənd.",
                            "az": "Onların qovluğu var; yazı taxtası yoxdur.",
                            "image_have": "assets/images/lessons/lesson_01/pushe.png",
                            "image_not_have": "assets/images/lessons/lesson_01/takhteshasi.png",
                        },
                        {
                            "prompt_fa": "فیل‌ها",
                            "answer_fa": "فیل‌ها خرطوم دارند؛ شاخ ندارند.",
                            "reading_az": "Filha xortum darənd; şax nədarənd.",
                            "az": "Fillərin xortumu var; buynuzu yoxdur.",
                            "image_have": "assets/images/lessons/lesson_01/fil.png",
                            "image_not_have": "assets/images/lessons/lesson_01/boz.png",
                        },
                    ],
                },
            ],
        },
        {
            "title_az": "Mənfi sual cümləsi",
            "title_fa": "جمله‌ی پرسشی منفی",
            "conjugations": [],
            "examples": [
                {
                    "fa": "آیا فاطمه رایانه ندارد؟ چرا، فاطمه رایانه دارد.",
                    "az": "Fatimənin komputeri yoxdurmu? Xeyr (əksinə), Fatimənin komputeri var.",
                },
                {
                    "fa": "آیا فاطمه دوربین ندارد؟ نه، فاطمه دوربین ندارد؛ او رایانه دارد.",
                    "az": "Fatimənin kamerası yoxdurmu? Bəli, Fatimənin kamerası yoxdur; onun komputeri var.",
                },
                {
                    "fa": "آیا حسین مداد ندارد؟ چرا، حسین مداد دارد.",
                    "reading_az": "Aya Hoseyn medad nədarəd? Çera, Hoseyn medad darəd.",
                    "az": "Hüseynin qələmi yoxdurmu? Xeyr (əksinə), Hüseynin qələmi var.",
                },
                {
                    "fa": "آیا حسین با مداد نمی‌نویسد؟ نه، حسین با خودکار می‌نویسد.",
                    "reading_az": "Aya Hoseyn ba medad neminevisəd? Na, Hoseyn ba xodkar minevisəd.",
                    "az": "Hüseyn qələmlə yazmırmı? Bəli, Hüseyn tükənməz qələmlə yazır.",
                },
                {
                    "fa": "آیا این خانم، استاد نیست؟ آیا او در کلاس است؟ چرا، او در کلاس است.",
                    "reading_az": "Aya in xanom, ostad nist? Aya u dar kelas əst? Çera, u dar kelas əst.",
                    "az": "Bu xanım müəllim deyilmi? O sinifdədirmi? Xeyr (əksinə), o sinifdədir.",
                },
                {
                    "fa": "آیا در این ظرف، غذا نیست؟ آیا محمّد غذا می‌خورد؟ نه، محمّد غذا نمی‌خورد.",
                    "reading_az": "Aya dar in zarf, qəza nist? Aya Mohəmməd qəza mixorəd? Na, Mohəmməd qəza nemixorəd.",
                    "az": "Bu qabda yemək yoxdurmu? Məhəmməd yemək yeyirmi? Xeyr, Məhəmməd yemək yemir.",
                },
                {
                    "fa": "آیا شما (تو) زبان فارسی نمی‌خوانی؟ چرا، من زبان فارسی می‌خوانم.",
                    "reading_az": "Aya to zəbane farsi nemixani? Çera, mən zəbane farsi mixanam.",
                    "az": "Sən fars dilini oxumursanmı? Xeyr (əksinə), mən fars dilini oxuyuram.",
                },
                {
                    "fa": "آیا شما (تو) کتاب اوّل می‌خوانی؟ نه، من کتاب دوم می‌خوانم.",
                    "reading_az": "Aya to ketabe əvval mixani? Na, mən ketabe dovvom mixanam.",
                    "az": "Sən birinci kitabı oxuyursanmı? Xeyr, mən ikinci kitabı oxuyuram.",
                },
                {
                    "fa": "آیا مریم نقّاشی نمی‌کشد؟ چرا، مریم روی مقوّا نقّاشی می‌کشد.",
                    "reading_az": "Aya Məryəm nəqqaşi nemikeşəd? Çera, Məryəm ruye moqəvva nəqqaşi mikeşəd.",
                    "az": "Məryəm rəsm çəkmirmi? Xeyr (əksinə), Məryəm karton üzərində rəsm çəkir.",
                },
                {
                    "fa": "آیا او در دفتر نقّاشی می‌کشد؟ نه، او روی دفتر نقّاشی می‌کشد.",
                    "reading_az": "Aya u dar dəftər nəqqaşi mikeşəd? Na, u ruye dəftər nəqqaşi mikeşəd.",
                    "az": "O dəftərdə rəsm çəkirmi? Xeyr, o dəftər üzərində rəsm çəkir.",
                },
            ],
            "drills": [
                {
                    "title_fa": "با توجّه به تصویر پاسخ دهید",
                    "instruction_az": "Şəklə diqqət edərək cavab verin",
                    "items": [
                        {
                            "prompt_fa": "آیا این دختر، کتاب دارد؟",
                            "answer_fa": "بله، این دختر کتاب دارد.",
                            "reading_az": "Bəle, in doxtər ketab darəd.",
                            "az": "Bəli, bu qızın kitabı var.",
                        },
                        {
                            "prompt_fa": "آیا کتاب او روی میز نیست؟",
                            "answer_fa": "نه، کتاب او روی میز نیست؛ در دست اوست.",
                            "reading_az": "Na, ketabe u ruye miz nist; dər dəste u əst.",
                            "az": "Bəli, onun kitabı masanın üstündə deyil; onun əlindədir.",
                        },
                        {
                            "prompt_fa": "آیا او نقّاشی می‌کشد؟",
                            "answer_fa": "نه، او نقّاشی نمی‌کشد؛ او کتاب می‌خواند.",
                            "reading_az": "Na, u nəqqaşi nemikeşəd; u ketab mixanəd.",
                            "az": "Xeyr, o rəsm çəkmir; o kitab oxuyur.",
                        },
                        {
                            "prompt_fa": "آیا حسین مداد ندارد؟",
                            "answer_fa": "چرا، حسین مداد دارد.",
                            "reading_az": "Çera, Hoseyn medad darəd.",
                            "az": "Xeyr (əksinə), Hüseynin qələmi var.",
                        },
                        {
                            "prompt_fa": "آیا او با مداد نمی‌نویسد؟",
                            "answer_fa": "نه، او با مداد نمی‌نویسد؛ او با خودکار می‌نویسد.",
                            "reading_az": "Na, u ba medad neminevisəd; u ba xodkar minevisəd.",
                            "az": "Bəli, o mədədlə yazmır; o tükənməz qələmlə yazır.",
                        },
                        {
                            "prompt_fa": "مداد حسین کجاست؟",
                            "answer_fa": "مداد حسین، روی میز است.",
                            "reading_az": "Medade Hoseyn, ruye miz əst.",
                            "az": "Hüseynin qələmi masanın üstündədir.",
                        },
                    ],
                },
            ],
        },
    ],
    "exercises": [
        {
            "kind": "fill_blank",
            "instruction_az": "Boşluğu söz bankından uyğun sözlə doldurun.",
            "word_bank": ["پاک می‌کند", "نیست", "ندارید", "می‌گذارم", "می‌نویسد", "می‌کشند"],
            "items": [
                {
                    "fa_with_blank": "من کیف را روی میز ___ .",
                    "correct_answer": "می‌گذارم",
                    "reading_az": "migozaram",
                    "az": "qoyuram",
                    "full_reading_az": "Mən kif ra ruye miz migozaram.",
                    "full_translation_az": "Mən çantanı masanın üstünə qoyuram.",
                },
                {
                    "fa_with_blank": "او با مداد ___ .",
                    "correct_answer": "می‌نویسد",
                    "reading_az": "minevisəd",
                    "az": "yazır",
                    "full_reading_az": "U ba medad minevisəd.",
                    "full_translation_az": "O, qələmlə yazır.",
                },
                {
                    "fa_with_blank": "او با پاک‌کن ___ .",
                    "correct_answer": "پاک می‌کند",
                    "reading_az": "pak mikonəd",
                    "az": "silir",
                    "full_reading_az": "U ba pakkon pak mikonəd.",
                    "full_translation_az": "O, pozanla silir.",
                },
                {
                    "fa_with_blank": "آن‌ها روی تابلو نقّاشی نمی‌کشند؛ در دفتر نقّاشی ___ .",
                    "correct_answer": "می‌کشند",
                    "reading_az": "mikeşənd",
                    "az": "çəkirlər",
                    "full_reading_az": "Anha ruye təblo nəqqaşi nemikeşənd; dər dəftər nəqqaşi mikeşənd.",
                    "full_translation_az": "Onlar lövhənin üstündə rəsm çəkmirlər; dəftərdə rəsm çəkirlər.",
                },
                {
                    "fa_with_blank": "آیا این زیردستی ___ ؟ نه، این زیردستی نیست؛ پوشه است.",
                    "correct_answer": "نیست",
                    "reading_az": "nist",
                    "az": "deyil",
                    "full_reading_az": "Aya in zirdəsti nist? Nə, in zirdəsti nist; puşe əst.",
                    "full_translation_az": "Bu yazı altlığı deyilmi? Xeyr, bu yazı altlığı deyil; qovluqdur.",
                },
                {
                    "fa_with_blank": "آیا شما خط‌کش و پرگار ___ ؟ چرا، ما خط‌کش و پرگار داریم.",
                    "correct_answer": "ندارید",
                    "reading_az": "nədarid",
                    "az": "yoxdur",
                    "full_reading_az": "Aya şoma xətkeş və pərgar nədarid? Çera, ma xətkeş və pərgar darim.",
                    "full_translation_az": "Sizin xətkeşiniz və pərgarınız yoxdurmu? Xeyr (əksinə), bizim xətkeşimiz və pərgarımız var.",
                },
            ],
        },
        {
            "kind": "practice_reveal",
            "title_fa": "مانند مثال بگویید",
            "instruction_az": "Nümunə kimi deyin",
            "example_fa": (
                "پدر / می‌نویسد\n"
                "اسم پدرم احمد است؛ *او الآن* نامه می‌نویسد."
            ),
            "example_reading_az": (
                "Pedər / minevisəd.\n"
                "Esme pedərəm Əhməd əst; u əl-an name minevisəd."
            ),
            "example_az": (
                "Ata / yazır.\n"
                "Atamın adı Əhməddir; o indi məktub yazır."
            ),
            "items": [
                {
                    "prompt_fa": "خواهر / نقّاشی می‌کشد",
                    "answer_fa": "اسم خواهرم زینب است؛ او الآن نقّاشی می‌کشد.",
                    "reading_az": "Esme xahərəm Zeynəb əst; u əl-an nəqqaşi mikeşəd.",
                    "az": "Bacımın adı Zeynəbdir; o indi rəsm çəkir.",
                },
                {
                    "prompt_fa": "فرزند / می‌خورد",
                    "answer_fa": "اسم فرزندم علی است؛ او الآن غذا می‌خورد.",
                    "reading_az": "Esme fərzəndəm Əli əst; u əl-an qəza mixorəd.",
                    "az": "Övladımın adı Əlidir; o indi yemək yeyir.",
                },
                {
                    "prompt_fa": "استاد / پاک می‌کند",
                    "answer_fa": "اسم استادم رضا است؛ او الآن تابلو را پاک می‌کند.",
                    "reading_az": "Esme ostadəm Reza əst; u əl-an təblo ra pak mikonəd.",
                    "az": "Müəllimimin adı Rzadır; o indi lövhəni silir.",
                },
                {
                    "prompt_fa": "مادر / می‌خواند",
                    "answer_fa": "اسم مادرم فاطمه است؛ او الآن کتاب می‌خواند.",
                    "reading_az": "Esme madərəm Fateme əst; u əl-an ketab mixanəd.",
                    "az": "Anamın adı Fatimədir; o indi kitab oxuyur.",
                },
            ],
        },
        {
            "kind": "practice_reveal",
            "title_fa": "با فعل‌های «دارد» و «وجود دارد» جمله بسازید",
            "instruction_az": '"دارد" və "وجود دارد" felləri ilə cümlə qurun',
            "example_fa": (
                "کلاس ما / صندلی، رایانه و تابلو:\n"
                "کلاس ما صندلی، رایانه و تابلو *دارد*.\n"
                "*در* کلاس ما صندلی، رایانه و تابلو *وجود دارد*."
            ),
            "example_reading_az": (
                "Kelase ma / səndəli, rayane vo tablo:\n"
                "Kelase ma səndəli, rayane vo tablo darəd.\n"
                "Dər kelase ma səndəli, rayane vo tablo vocud darəd."
            ),
            "example_az": (
                "Bizim sinif / stul, komputer və lövhə:\n"
                "Bizim sinifin stulu, komputeri və lövhəsi var.\n"
                "Bizim sinifdə stul, komputer və lövhə var."
            ),
            "items": [
                {
                    "prompt_fa": "اتاق شما / فرش، تخت و تلفن",
                    "answer_fa": "اتاق شما فرش، تخت و تلفن دارد. / در اتاق شما فرش، تخت و تلفن وجود دارد.",
                    "reading_az": "Otaqe şoma fərş, təxt və telefon darəd. / Dər otaqe şoma fərş, təxt və telefon vocud darəd.",
                    "az": "Sizin otağınızın xalçası, çarpayısı və telefonu var. / Sizin otağınızda xalça, çarpayı və telefon var.",
                },
                {
                    "prompt_fa": "باغ پدرم / درخت سیب و گیلاس",
                    "answer_fa": "باغ پدرم درخت سیب و گیلاس دارد. / در باغ پدرم درخت سیب و گیلاس وجود دارد.",
                    "reading_az": "Bağe pedərəm dərəxte sib və gilas darəd. / Dər bağe pedərəm dərəxte sib və gilas vocud darəd.",
                    "az": "Atamın bağının alma və albalı ağacı var. / Atamın bağında alma və albalı ağacı var.",
                },
                {
                    "prompt_fa": "فروش‌گاه مدرسه / میوه، بستنی و ساندویچ",
                    "answer_fa": "فروش‌گاه مدرسه میوه، بستنی و ساندویچ دارد. / در فروش‌گاه مدرسه میوه، بستنی و ساندویچ وجود دارد.",
                    "reading_az": "Foruşgahe mædrese mive, bəstəni və sanduiç darəd. / Dər foruşgahe mædrese mive, bəstəni və sanduiç vocud darəd.",
                    "az": "Məktəbin mağazasının meyvəsi, dondurması və sendviçi var. / Məktəbin mağazasında meyvə, dondurma və sendviç var.",
                },
                {
                    "prompt_fa": "این فرودگاه / عابربانک، فروش‌گاه و رستوران",
                    "answer_fa": "این فرودگاه عابربانک، فروش‌گاه و رستوران دارد. / در این فرودگاه عابربانک، فروش‌گاه و رستوران وجود دارد.",
                    "reading_az": "In forudgah aberbank, foruşgah və restoran darəd. / Dər in forudgah aberbank, foruşgah və restoran vocud darəd.",
                    "az": "Bu hava limanının bankomatı, mağazası və restoranı var. / Bu hava limanında bankomat, mağaza və restoran var.",
                },
            ],
        },
        {
            "kind": "practice_reveal",
            "title_fa": "مانند مثال بپرسید و پاسخ دهید",
            "instruction_az": "Nümunə kimi soruşub cavab verin",
            "example_fa": (
                "او / روزنامه / نمی‌خواند:\n"
                "آیا او روزنامه نمی‌خواند؟ *چرا*، او روزنامه می‌خواند."
            ),
            "example_reading_az": (
                "U / ruzname / nemixanəd:\n"
                "Aya u ruzname nemixanəd? Çera, u ruzname mixanəd."
            ),
            "example_az": (
                "O / qəzet / oxumur:\n"
                "O qəzeti oxumur? Xeyr (əksinə), o qəzeti oxuyur."
            ),
            "items": [
                {
                    "prompt_fa": "ما / ساعت / نداریم",
                    "answer_fa": "آیا ما ساعت نداریم؟ چرا، ما ساعت داریم.",
                    "reading_az": "Aya ma saət nədarim? Çera, ma saət darim.",
                    "az": "Bizim saatımız yoxdurmu? Xeyr (əksinə), bizim saatımız var.",
                },
                {
                    "prompt_fa": "آن‌ها / لیمو / نمی‌خورند",
                    "answer_fa": "آیا آن‌ها لیمو نمی‌خورند؟ چرا، آن‌ها لیمو می‌خورند.",
                    "reading_az": "Aya anha limu nemixorənd? Çera, anha limu mixorənd.",
                    "az": "Onlar limon yemirlərmi? Xeyr (əksinə), onlar limon yeyirlər.",
                },
                {
                    "prompt_fa": "شما (تو) / نامه / نمی‌نویسی",
                    "answer_fa": "آیا شما (تو) نامه نمی‌نویسی؟ چرا، من نامه می‌نویسم.",
                    "reading_az": "Aya to name neminevisi? Çera, mən name minevisəm.",
                    "az": "Sən məktub yazmırsanmı? Xeyr (əksinə), mən məktub yazıram.",
                },
                {
                    "prompt_fa": "مهدی / تابلو / پاک نمی‌کند",
                    "answer_fa": "آیا مهدی تابلو را پاک نمی‌کند؟ چرا، مهدی تابلو را پاک می‌کند.",
                    "reading_az": "Aya Mehdi təblo ra pak nemikonəd? Çera, Mehdi təblo ra pak mikonəd.",
                    "az": "Mehdi lövhəni silmirmi? Xeyr (əksinə), Mehdi lövhəni silir.",
                },
                {
                    "prompt_fa": "شما / کتاب فارسی / نمی‌خوانید",
                    "answer_fa": "آیا شما کتاب فارسی نمی‌خوانید؟ چرا، ما کتاب فارسی می‌خوانیم.",
                    "reading_az": "Aya şoma ketabe farsi nemixanid? Çera, ma ketabe farsi mixanim.",
                    "az": "Siz fars dili kitabını oxumursunuzmu? Xeyr (əksinə), biz fars dili kitabını oxuyuruq.",
                },
                {
                    "prompt_fa": "فاطمه / در دفتر / نقّاشی نمی‌کشد",
                    "answer_fa": "آیا فاطمه در دفتر نقّاشی نمی‌کشد؟ چرا، فاطمه در دفتر نقّاشی می‌کشد.",
                    "reading_az": "Aya Fateme dər dəftər nəqqaşi nemikeşəd? Çera, Fateme dər dəftər nəqqaşi mikeşəd.",
                    "az": "Fatimə dəftərdə rəsm çəkmirmi? Xeyr (əksinə), Fatimə dəftərdə rəsm çəkir.",
                },
            ],
        },
        {
            "kind": "practice_reveal",
            "title_fa": "مانند مثال جایگزین کنید",
            "instruction_az": "Nümunə kimi əvəz edin",
            "example_fa": (
                "من کتاب را در کیف می‌گذارم.\n"
                "مریم / میوه / سبد:\n"
                "مریم میوه *را* در سبد می‌گذارد."
            ),
            "example_reading_az": (
                "Mən ketab ra dər kif migozaram.\n"
                "Məryəm / mive / səbəd:\n"
                "Məryəm mive ra dər səbəd migozarəd."
            ),
            "example_az": (
                "Mən kitabı çantaya qoyuram.\n"
                "Məryəm / meyvə / səbət:\n"
                "Məryəm meyvəni səbətə qoyur."
            ),
            "items": [
                {
                    "prompt_fa": "آن‌ها / قاشق / بشقاب",
                    "answer_fa": "آن‌ها قاشق را در بشقاب می‌گذارند.",
                    "reading_az": "Anha qaşoq ra dər bəşqab migozarənd.",
                    "az": "Onlar qaşığı boşqaba qoyurlar.",
                },
                {
                    "prompt_fa": "شما / پول / جیب",
                    "answer_fa": "شما پول را در جیب می‌گذارید.",
                    "reading_az": "Şoma pul ra dər jib migozarid.",
                    "az": "Siz pulu cibə qoyursunuz.",
                },
                {
                    "prompt_fa": "ما / خودنویس / جامدادی",
                    "answer_fa": "ما خودنویس را در جامدادی می‌گذاریم.",
                    "reading_az": "Ma xodnevis ra dər camedadi migozarim.",
                    "az": "Biz dolma qələmi qələmqabına qoyuruq.",
                },
                {
                    "prompt_fa": "علی / نامه / پاکت‌نامه",
                    "answer_fa": "علی نامه را در پاکت‌نامه می‌گذارد.",
                    "reading_az": "Əli name ra dər pakətname migozarəd.",
                    "az": "Əli məktubu zərfə qoyur.",
                },
            ],
        },
        {
            "kind": "picture_sentences",
            "instruction_az": "Hər şəkil üçün iki cümlə qurun.",
            "items": [
                {
                    "image": "assets/images/lessons/lesson_01/takhte_gach.png",
                    "sentences": [
                        {
                            "fa": "این پسر روی تابلو می‌نویسد.",
                            "reading_az": "In pesər ruye tablo minevisəd.",
                            "az": "Bu oğlan lövhənin üstündə yazır.",
                        },
                        {
                            "fa": "او با گچ سفید می‌نویسد.",
                            "reading_az": "U ba gəçe səfid minevisəd.",
                            "az": "O, ağ təbaşirlə yazır.",
                        },
                    ],
                },
                {
                    "image": "assets/images/lessons/lesson_01/chasb.png",
                    "sentences": [
                        {
                            "fa": "این چسب، زرد رنگ است.",
                            "reading_az": "In çəsb, zərd rəng əst.",
                            "az": "Bu yapışqan sarı rəngdədir.",
                        },
                        {
                            "fa": "من با چسب، کاغذ را می‌چسبانم.",
                            "reading_az": "Mən ba çəsb, kağəz ra michəsbanam.",
                            "az": "Mən yapışqanla kağızı yapışdırıram.",
                        },
                    ],
                },
                {
                    "image": "assets/images/lessons/lesson_01/medad_naghashi.png",
                    "sentences": [
                        {
                            "fa": "این پسر با مداد نقّاشی می‌کشد.",
                            "reading_az": "In pesər ba medad nəqqaşi mikeşəd.",
                            "az": "Bu oğlan qələmlə rəsm çəkir.",
                        },
                        {
                            "fa": "او روی دفتر نقّاشی می‌کشد.",
                            "reading_az": "U ruye dəftər nəqqaşi mikeşəd.",
                            "az": "O, dəftərin üstündə rəsm çəkir.",
                        },
                    ],
                },
                {
                    "image": "assets/images/lessons/lesson_01/taqvim.png",
                    "sentences": [
                        {
                            "fa": "این تقویم، آبی و نارنجی است.",
                            "reading_az": "In təqvim, abi və narenci əst.",
                            "az": "Bu təqvim mavi və narıncı rəngdədir.",
                        },
                        {
                            "fa": "امروز، پنج‌شنبه است.",
                            "reading_az": "Emruz, pəncşənbe əst.",
                            "az": "Bu gün cümə axşamıdır.",
                        },
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
                        "fa": "این خودکار، آبی است. من با خودکار آبی می‌نویسم.",
                        "reading_az": "İn xodkar, abi əst. Mən ba xodkare abi minevisəm.",
                        "az": "Bu tükənməz qələm mavidir. Mən mavi tükənməz qələmlə yazıram.",
                    },
                    {
                        "fa": "محمّد مدادتراش دارد. مدادتراش او قرمز است. او مدادتراش را در جامدادی می‌گذارد.",
                        "reading_az": "Məhəmməd medadtəraş darəd. Medadtəraşe u qermez əst. U medadtəraş ra dər camedani migozarəd.",
                        "az": "Məhəmmədin qələmyonanı var. Onun qələmyonanı qırmızıdır. O, qələmyonanı qələmqabına qoyur.",
                    },
                    {
                        "fa": "آن جامدادی، بزرگ و تمیز است. در آن جامدادی سه مداد، دو خودکار و یک پاک‌کن هست.",
                        "reading_az": "An camedani, bozorg və təmiz əst. Dər an camedani se medad, do xodkar və yek pakkon həst.",
                        "az": "O qələmqabı böyük və təmizdir. O qələmqabıda üç karandaş, iki tükənməz qələm və bir pozan var.",
                    },
                    {
                        "fa": "برادر کوچک من با مداد می‌نویسد و با پاک‌کن پاک می‌کند.",
                        "reading_az": "Bəradəre kuçəke mən ba medad minevisəd və ba pakkon pak mikonəd.",
                        "az": "Mənim kiçik qardaşım karandaşla yazır və pozanla silir.",
                    },
                    {
                        "fa": "آن‌ها با خودکار و خودنویس می‌نویسند و با غلط‌گیر پاک می‌کنند.",
                        "reading_az": "Anha ba xodkar və xodnəvis minevisənd və ba qəltgir pak mikonənd.",
                        "az": "Onlar tükənməz qələm və dolma qələmlə yazırlar və korrektorla silirlər.",
                    },
                    {
                        "fa": "آیا فاطمه روی تابلو نقّاشی می‌کشد؟ نه، فاطمه روی مقوّا نقّاشی می‌کشد.",
                        "reading_az": "Aya Fateme ruye təblo nəqqaşi mikeşəd? Nə, Fateme ruye moqəvva nəqqaşi mikeşəd.",
                        "az": "Fatimə lövhənin üstündə rəsm çəkirmi? Xeyr, Fatimə karton üzərində rəsm çəkir.",
                    },
                    {
                        "fa": "آیا در کیف شما (تو) ماشین‌حساب هست؟ بله، در کیف من ماشین‌حساب هست.",
                        "reading_az": "Aya dər kife şoma (to) maşinhesab həst? Bəle, dər kife mən maşinhesab həst.",
                        "az": "Sənin çantanda kalkulyator varmı? Bəli, mənim çantamda kalkulyator var.",
                    },
                    {
                        "fa": "آیا شما کتاب و نوشت‌افزار را در کیف می‌گذارید؟ بله، ما کتاب و نوشت‌افزار را در کیف می‌گذاریم.",
                        "reading_az": "Aya şoma ketab və neveştəfzar ra dər kif migozarid? Bəle, ma ketab və neveştəfzar ra dər kif migozarim.",
                        "az": "Siz kitab və yazı ləvazimatını çantaya qoyursunuzmu? Bəli, biz kitab və yazı ləvazimatını çantaya qoyuruq.",
                    },
                ],
            },
        ],
        "answer_items": [
            {
                "fa": "کتاب شما کجاست؟",
                "reading_az": "Ketabe şoma kocast?",
                "az": "Sizin kitabınız haradadır?",
                "sample_answer_fa": "کتاب من روی میز است.",
                "sample_answer_reading_az": "Ketabe mən ruye miz əst.",
                "sample_answer_az": "Mənim kitabım masanın üstündədir.",
            },
            {
                "fa": "کتاب‌ها را کجا می‌گذارید؟",
                "reading_az": "Ketabha ra koca migozarid?",
                "az": "Kitabları haraya qoyursunuz?",
                "sample_answer_fa": "کتاب‌ها را در کیف می‌گذاریم.",
                "sample_answer_reading_az": "Ketabha ra dər kif migozarim.",
                "sample_answer_az": "Kitabları çantaya qoyuruq.",
            },
            {
                "fa": "شما کدام کتاب را می‌خوانید؟",
                "reading_az": "Şoma kodam ketab ra mixanid?",
                "az": "Siz hansı kitabı oxuyursunuz?",
                "sample_answer_fa": "من کتاب دوم را می‌خوانم.",
                "sample_answer_reading_az": "Mən ketabe dovvom ra mixanəm.",
                "sample_answer_az": "Mən ikinci kitabı oxuyuram.",
            },
            {
                "fa": "آیا شما تابلو را پاک می‌کنید؟",
                "reading_az": "Aya şoma təblo ra pak mikonid?",
                "az": "Siz lövhəni silirsinizmi?",
                "sample_answer_fa": "بله، من تابلو را پاک می‌کنم.",
                "sample_answer_reading_az": "Bəle, mən təblo ra pak mikonəm.",
                "sample_answer_az": "Bəli, mən lövhəni silirəm.",
            },
            {
                "fa": "آیا دوست شما نقّاشی می‌کشد؟",
                "reading_az": "Aya duste şoma nəqqaşi mikeşəd?",
                "az": "Sizin dostunuz rəsm çəkirmi?",
                "sample_answer_fa": "بله، دوست من نقّاشی می‌کشد.",
                "sample_answer_reading_az": "Bəle, duste mən nəqqaşi mikeşəd.",
                "sample_answer_az": "Bəli, mənim dostum rəsm çəkir.",
            },
            {
                "fa": "آیا شما پاک‌کن و مدادتراش دارید؟",
                "reading_az": "Aya şoma pakkon və medadtəraş darid?",
                "az": "Sizin pozanınız və qələmyonanınız varmı?",
                "sample_answer_fa": "بله، من پاک‌کن و مدادتراش دارم.",
                "sample_answer_reading_az": "Bəle, mən pakkon və medadtəraş daram.",
                "sample_answer_az": "Bəli, mənim pozanım və qələmyonanım var.",
            },
        ],
    },
    "reading_text": {
        "title_fa": "در ایران",
        "title_az": "İranda",
        "image": "assets/images/lessons/lesson_01/reading_dar_iran.png",
        "paragraphs_fa": [
            "اسم من حسین است و اسم خواهرم فاطمه است. پدر ما پزشک است و مادر ما استاد دانشگاه است. ما الآن در ایران هستیم.",
            "من و خواهرم طلبه‌ی جامعة المصطفی هستیم. من در مدرسه‌ی المهدی و خواهرم در مدرسه‌ی بنت‌الهدی درس می‌خوانیم. ما زبان فارسی می‌خوانیم. خواهرم کتاب اوّل می‌خواند و من کتاب دوم می‌خوانم.",
            "من یک جامدادی بزرگ دارم. در جامدادی من مداد، خودکار، مدادتراش، خط‌کش، پاک‌کن و... وجود دارد.",
        ],
        "footnotes": [
            {"fa": "خواهرم: خواهر من", "az": "bacım: mənim bacım"},
            {"fa": "وجود دارد", "az": "var, mövcuddur"},
        ],
        "full_translation_az": (
            "Mənim adım Hüseyndir və bacımın adı Fatimədir. Atamız həkimdir, anamız isə universitet müəllimidir. "
            "Biz hazırda İrandayıq.\n\n"
            "Mən və bacım əl-Müstəfa Cəmiyyətinin tələbələriyik. Mən əl-Mehdi məktəbində, bacım isə Bintul-Huda "
            "məktəbində dərs oxuyuruq. Biz fars dili öyrənirik. Bacım birinci kitabı, mən isə ikinci kitabı oxuyuram.\n\n"
            "Mənim bir böyük qələmqabım var. Qələmqabımda karandaş, tükənməz qələm, qələmyonan, xətkeş, pozan və s. var."
        ),
        "sentences": [
            {
                "fa": "اسم من حسین است و اسم خواهرم فاطمه است.",
                "reading_az": "Esme mən Hoseyn əst və esme xahərəm Fateme əst.",
                "az": "Mənim adım Hüseyndir və bacımın adı Fatimədir.",
                "new_paragraph": True,
            },
            {
                "fa": "پدر ما پزشک است و مادر ما استاد دانشگاه است.",
                "reading_az": "Pedəre ma pezeşk əst və madəre ma ostade daneşgah əst.",
                "az": "Atamız həkimdir, anamız isə universitet müəllimidir.",
            },
            {
                "fa": "ما الآن در ایران هستیم.",
                "reading_az": "Ma əl-an dər Iran həstim.",
                "az": "Biz hazırda İrandayıq.",
            },
            {
                "fa": "من و خواهرم طلبه‌ی جامعة المصطفی هستیم.",
                "reading_az": "Mən və xahərəm təlləbeye Cameətol-Mostəfa həstim.",
                "az": "Mən və bacım əl-Müstəfa Cəmiyyətinin tələbələriyik.",
                "new_paragraph": True,
            },
            {
                "fa": "من در مدرسه‌ی المهدی و خواهرم در مدرسه‌ی بنت‌الهدی درس می‌خوانیم.",
                "reading_az": "Mən dər mædrese-ye əl-Mehdi və xahərəm dər mædrese-ye Bentol-Hoda dərs mixanim.",
                "az": "Mən əl-Mehdi məktəbində, bacım isə Bintul-Huda məktəbində dərs oxuyuruq.",
            },
            {
                "fa": "ما زبان فارسی می‌خوانیم.",
                "reading_az": "Ma zəbane farsi mixanim.",
                "az": "Biz fars dili öyrənirik.",
            },
            {
                "fa": "خواهرم کتاب اوّل می‌خواند و من کتاب دوم می‌خوانم.",
                "reading_az": "Xahərəm ketabe əvvəl mixanəd və mən ketabe dovvom mixanəm.",
                "az": "Bacım birinci kitabı, mən isə ikinci kitabı oxuyuram.",
            },
            {
                "fa": "من یک جامدادی بزرگ دارم.",
                "reading_az": "Mən yek camedadiye bozorg daram.",
                "az": "Mənim bir böyük qələmqabım var.",
                "new_paragraph": True,
            },
            {
                "fa": "در جامدادی من مداد، خودکار، مدادتراش، خط‌کش، پاک‌کن و... وجود دارد.",
                "reading_az": "Dər camedadiye mən medad, xodkar, medadtəraş, xətkeş, pakkon və ... vocud darəd.",
                "az": "Qələmqabımda karandaş, tükənməz qələm, qələmyonan, xətkeş, pozan və s. var.",
            },
        ],
        "comprehension_questions": [
            {
                "question_fa": "اسم خواهرِ حسین چیست؟",
                "reading_az": "Esme xahəre Hoseyn çist?",
                "az": "Hüseynin bacısının adı nədir?",
                "sample_answer_fa": "اسم خواهر حسین، فاطمه است.",
                "sample_answer_reading_az": "Esme xahəre Hoseyn, Fateme əst.",
                "sample_answer_az": "Hüseynin bacısının adı Fatimədir.",
            },
            {
                "question_fa": "آیا پدر حسین، معلّم است؟",
                "reading_az": "Aya pedəre Hoseyn, moəllem əst?",
                "az": "Hüseynin atası müəllimdirmi?",
                "sample_answer_fa": "نه، پدر حسین معلّم نیست؛ او پزشک است.",
                "sample_answer_reading_az": "Nə, pedəre Hoseyn moəllem nist; u pezeşk əst.",
                "sample_answer_az": "Xeyr, Hüseynin atası müəllim deyil; o, həkimdir.",
            },
            {
                "question_fa": "حسین و فاطمه، اهل کجا هستند؟",
                "reading_az": "Hoseyn və Fateme, əhle koca həstənd?",
                "az": "Hüseyn və Fatimə haralıdırlar?",
                "sample_answer_fa": "آن‌ها اهل لبنان هستند.",
                "sample_answer_reading_az": "Anha əhle Lobnan həstənd.",
                "sample_answer_az": "Onlar Livandandırlar.",
            },
            {
                "question_fa": "حسین و فاطمه کجا درس می‌خوانند؟",
                "reading_az": "Hoseyn və Fateme koca dərs mixanənd?",
                "az": "Hüseyn və Fatimə harada oxuyurlar?",
                "sample_answer_fa": "حسین در مدرسه‌ی المهدی و فاطمه در مدرسه‌ی بنت‌الهدی درس می‌خوانند.",
                "sample_answer_reading_az": "Hoseyn dər mædrese-ye əl-Mehdi və Fateme dər mædrese-ye Bentol-Hoda dərs mixanənd.",
                "sample_answer_az": "Hüseyn əl-Mehdi məktəbində, Fatimə isə Bintul-Huda məktəbində oxuyur.",
            },
            {
                "question_fa": "فاطمه و حسین، الآن کدام کتاب را می‌خوانند؟",
                "reading_az": "Fateme və Hoseyn, əl-an kodam ketab ra mixanənd?",
                "az": "Fatimə və Hüseyn indi hansı kitabı oxuyurlar?",
                "sample_answer_fa": "فاطمه کتاب اوّل و حسین کتاب دوم را می‌خواند.",
                "sample_answer_reading_az": "Fateme ketabe əvvəl və Hoseyn ketabe dovvom ra mixanənd.",
                "sample_answer_az": "Fatimə birinci kitabı, Hüseyn isə ikinci kitabı oxuyur.",
            },
            {
                "question_fa": "آیا در جامدادی حسین، مدادتراش و پاک‌کن وجود ندارد؟",
                "reading_az": "Aya dər camedadiye Hoseyn, medadtəraş və pakkon vocud nədarəd?",
                "az": "Hüseynin qələmqabında qələmyonan və pozan yoxdurmu?",
                "sample_answer_fa": "چرا، در جامدادی او مدادتراش و پاک‌کن وجود دارد.",
                "sample_answer_reading_az": "Çera, dər camedadiye u medadtəraş və pakkon vocud darəd.",
                "sample_answer_az": "Xeyr (əksinə), Hüseynin qələmqabında qələmyonan və pozan var.",
            },
        ],
    },
}

LESSON_2 = {
    "number": 2,
    "title_fa": "خانه",
    "title_az": "Ev",
    "available": True,
    "vocabulary": [
        {"fa": "باغچه", "reading": "bağçe", "az": "Bağça (həyət bağı)", "image": "assets/images/lessons/lesson_02/baghche.png"},
        {"fa": "پارکینگ", "reading": "parkinq", "az": "Avtomobil dayanacağı", "image": "assets/images/lessons/lesson_02/parking.png"},
        {"fa": "آپارتمان", "reading": "apartman", "az": "Mənzil", "image": "assets/images/lessons/lesson_02/apartman.png"},
        {"fa": "آشپزخانه", "reading": "aşpəzxane", "az": "Mətbəx", "image": "assets/images/lessons/lesson_02/ashpazkhane.png"},
        {"fa": "راهرو", "reading": "rahro", "az": "Dəhliz", "image": "assets/images/lessons/lesson_02/rahro.png"},
        {"fa": "پلّه", "reading": "pelle", "az": "Pillə", "image": "assets/images/lessons/lesson_02/polle.png"},
        {"fa": "غذا می‌پزد", "reading": "qəza mipəzəd", "az": "yemək bişirir", "image": "assets/images/lessons/lesson_02/ghaza_mipazad.png"},
        {"fa": "اجاق‌گاز", "reading": "ocaq-qaz", "az": "Qaz plitəsi", "image": "assets/images/lessons/lesson_02/ojagh_gaz.png"},
        {"fa": "کتری", "reading": "ketri", "az": "Çaydan", "image": "assets/images/lessons/lesson_02/ketri.png"},
        {"fa": "پشت‌بام", "reading": "poştebam", "az": "Dam", "image": "assets/images/lessons/lesson_02/poshtebam.png"},
        {"fa": "کولر", "reading": "kuler", "az": "Kondisioner", "image": "assets/images/lessons/lesson_02/kooler.png"},
        {"fa": "پرده", "reading": "pərde", "az": "Pərdə", "image": "assets/images/lessons/lesson_02/parde.png"},
        {"fa": "اتاق خواب", "reading": "otağe xab", "az": "Yataq otağı", "image": "assets/images/lessons/lesson_02/otagh_khab.png"},
        {"fa": "اتاق پذیرایی", "reading": "otağe pəzirayi", "az": "Qonaq otağı", "image": "assets/images/lessons/lesson_02/otagh_paziraei.png"},
        {"fa": "اتاق مطالعه", "reading": "otağe motaleə", "az": "İş/oxu otağı", "image": "assets/images/lessons/lesson_02/otagh_motalee.png"},
        {"fa": "پتو", "reading": "pətu", "az": "Adyal", "image": "assets/images/lessons/lesson_02/patu.png"},
        {"fa": "بالش", "reading": "baleş", "az": "Yastıq", "image": "assets/images/lessons/lesson_02/balesh.png"},
        {"fa": "تشک", "reading": "toşək", "az": "Döşək", "image": "assets/images/lessons/lesson_02/toshak.png"},
        {"fa": "می‌شوید", "reading": "mişuyəd", "az": "yuyur", "image": "assets/images/lessons/lesson_02/mishuyad.png"},
        {"fa": "دست‌شویی", "reading": "dəstşuyi", "az": "Əl-üz yuma yeri", "image": "assets/images/lessons/lesson_02/dastshuei.png"},
        {"fa": "توالت", "reading": "tualet", "az": "Tualet", "image": "assets/images/lessons/lesson_02/tovalet.png"},
        {"fa": "دوش می‌گیرد", "reading": "duş migirəd", "az": "duş qəbul edir", "image": "assets/images/lessons/lesson_02/dush_migirad.png"},
        {"fa": "حمّام", "reading": "həmmam", "az": "Hamam otağı", "image": "assets/images/lessons/lesson_02/hammam.png"},
        {"fa": "آب‌گرم‌کن", "reading": "abgərmkon", "az": "Su qızdırıcısı", "image": "assets/images/lessons/lesson_02/abgarmkon.png"},
        {"fa": "ایوان", "reading": "eyvan", "az": "Eyvan"},
        {"fa": "حیاط", "reading": "həyat", "az": "Həyət"},
        {"fa": "دیوار", "reading": "divar", "az": "Divar"},
        {"fa": "ستون", "reading": "sotun", "az": "Sütun"},
        {"fa": "حوض", "reading": "hoz", "az": "Hovuz"},
        {"fa": "پنجره", "reading": "pəncəre", "az": "Pəncərə"},
        {"fa": "در", "reading": "dər", "az": "Qapı"},
        {"fa": "ظرف‌شویی", "reading": "zərfşuyi", "az": "Qabyuyan maşın"},
        {"fa": "لباس‌شویی", "reading": "lebasşuyi", "az": "Paltaryuyan maşın"},
        {"fa": "یخچال", "reading": "yəxçal", "az": "Soyuducu"},
        {"fa": "شوفاژ", "reading": "şofaj", "az": "Radiator"},
        {"fa": "شومینه", "reading": "şomine", "az": "Kamin"},
        {"fa": "پنکه", "reading": "pənke", "az": "Ventilyator"},
        {"fa": "نردبان", "reading": "nərdeban", "az": "Nərdivan"},
        {"fa": "شیرآب", "reading": "şire ab", "az": "Su kranı"},
        {"fa": "لامپ", "reading": "lamp", "az": "Lampa"},
        {"fa": "تخت", "reading": "təxt", "az": "Çarpayı"},
        {"fa": "فرش", "reading": "fərş", "az": "Xalça"},
    ],
    "grammar_notes": [
        {
            "title_az": 'Sual cümləsində "یا" (ya)',
            "title_fa": "«یا» در جمله‌ی پرسشی",
            "conjugations": [],
            "examples": [
                {
                    "fa": "این اجاق‌گاز است یا لباس‌شویی است؟ این لباس‌شویی است.",
                    "reading_az": "İn ocaq-qaz əst ya ləbasşuyi əst? İn ləbasşuyi əst.",
                    "az": "Bu qaz plitəsidir, yoxsa paltaryuyandır? Bu paltaryuyandır.",
                },
                {
                    "fa": "این لباس‌شویی، بزرگ است یا کوچک؟ این لباس‌شویی، بزرگ است.",
                    "reading_az": "İn ləbasşuyi, bozorg əst ya kuçek? İn ləbasşuyi, bozorg əst.",
                    "az": "Bu paltaryuyan böyükdür, yoxsa kiçik? Bu paltaryuyan böyükdür.",
                },
                {
                    "fa": "محمّد پزشک است یا پرستار است؟ محمّد، پزشک است.",
                    "reading_az": "Mohəmməd pezeşk əst ya pərəstar əst? Mohəmməd, pezeşk əst.",
                    "az": "Məhəmməd həkimdir, yoxsa tibb bacısı? Məhəmməd həkimdir.",
                },
                {
                    "fa": "شما در حمّام دوش می‌گیرید یا در آشپزخانه؟ من در حمّام دوش می‌گیرم.",
                    "reading_az": "Şoma dər həmmam duş migirid ya dər aşpəzxane? Mən dər həmmam duş migiram.",
                    "az": "Siz hamamda duş alırsınız, yoxsa mətbəxdə? Mən hamamda duş alıram.",
                },
                {
                    "fa": "بینی برای شنیدن است یا بوییدن؟ بینی برای بوییدن است.",
                    "reading_az": "Bini bəraye şenidən əst ya buyidən? Bini bəraye buyidən əst.",
                    "az": "Burun eşitmək üçündür, yoxsa iyləmək üçün? Burun iyləmək üçündür.",
                },
                {
                    "fa": "این خانم‌ها ظرف می‌شویند یا غذا می‌پزند؟ این خانم‌ها غذا می‌پزند.",
                    "reading_az": "İn xanomha zərf mişuyənd ya qəza mipəzənd? İn xanomha qəza mipəzənd.",
                    "az": "Bu xanımlar qab yuyur, yoxsa yemək bişirir? Bu xanımlar yemək bişirir.",
                },
            ],
            "note_fa": (
                "۱. اگر در جمله‌ی پرسشی واژه‌ی «یا» باشد؛ جواب «بله»، «نه» و «چرا» درست نیست، "
                "مانند: این شلوار مشکی است یا آبی؟\n"
                "✅ این شلوار مشکی است.\n"
                "❌ بله، این شلوار مشکی است.\n"
                "❌ نه، این شلوار مشکی نیست؛ آبی است.\n"
                "۲. در جمله‌ی پرسشی که «یا» وجود دارد، اگر دو فعل همانند باشد، معمولاً فعل دوم را حذف می‌کنیم.\n"
                "✅ این لباس‌شویی بزرگ است یا کوچک؟\n"
                "✅ این لباس‌شویی بزرگ یا کوچک است؟"
            ),
            "note_reading_az": (
                '1. Əgər dər comleye porseşi vajeye "ya" başəd; cəvab "bəle", "na" va "çera" dorost nist, '
                "manənd: in şəlvar meşki əst ya abi?\n"
                "İn şəlvar meşki əst.\n"
                "Bəle, in şəlvar meşki əst.\n"
                "Na, in şəlvar meşki nist; abi əst.\n"
                '2. Dər comleye porseşi ke "ya" vocud darəd, əgər do fele həmanənd başəd, məmulən fele dovvom ra həzf mikonim.\n'
                "İn ləbasşuyi bozorg əst ya kuçek?\n"
                "İn ləbasşuyi bozorg ya kuçek əst?"
            ),
            "note_az": (
                '1. Sual cümləsində "یا" (ya) sözü olarsa, cavab olaraq "bəli", "xeyr" və "niyə" düzgün deyil, '
                "məsələn: Bu şalvar qara rəngdədir, yoxsa mavi?\n"
                "✅ Bu şalvar qara rəngdədir.\n"
                "❌ Bəli, bu şalvar qara rəngdədir.\n"
                "❌ Xeyr, bu şalvar qara rəngdə deyil; mavidir.\n"
                '2. "یа" (ya) olan sual cümləsində iki fel eyni olarsa, adətən ikinci feli buraxırıq.\n'
                "✅ Bu paltaryuyan böyükdür, yoxsa kiçik?\n"
                "✅ Bu paltaryuyan böyük, yoxsa kiçikdir?"
            ),
        },
        {
            "title_az": 'Sual cümləsi "چه‌کار می‌کند؟" (O nə edir?)',
            "title_fa": "جمله‌ی پرسشی «چه‌کار می‌کند؟»",
            "conjugations": [],
            "examples": [
                {
                    "fa": "این مرد چه‌کار می‌کند؟ این مرد روزنامه می‌خواند.",
                    "reading_az": "İn mərd çekar mikonəd? İn mərd ruzname mixanəd.",
                    "az": "Bu kişi nə edir? Bu kişi qəzet oxuyur.",
                },
                {
                    "fa": "آن خانم چه‌کار می‌کند؟ آن خانم غذا می‌پزد.",
                    "reading_az": "An xanom çekar mikonəd? An xanom qəza mipəzəd.",
                    "az": "O xanım nə edir? O xanım yemək bişirir.",
                },
                {
                    "fa": "فاطمه چه‌کار می‌کند؟ فاطمه نامه می‌نویسد.",
                    "reading_az": "Fateme çekar mikonəd? Fateme name minevisəd.",
                    "az": "Fatimə nə edir? Fatimə məktub yazır.",
                },
                {
                    "fa": "علی چه‌کار می‌کند؟ علی نقّاشی می‌کشد.",
                    "reading_az": "Əli çekar mikonəd? Əli nəqqaşi mikeşəd.",
                    "az": "Əli nə edir? Əli rəsm çəkir.",
                },
                {
                    "fa": "شما (تو) چه‌کار می‌کنی؟ من لباس می‌شویم.",
                    "reading_az": "Şoma (to) çekar mikoni? Mən lebas mişuyəm.",
                    "az": "Sən nə edirsən? Mən paltar yuyuram.",
                },
                {
                    "fa": "شما کدام لباس را می‌شویید؟ من پیراهن قرمز را می‌شویم.",
                    "reading_az": "Şoma kodam lebas ra mişuyid? Mən pirahəne qermez ra mişuyəm.",
                    "az": "Siz hansı paltarı yuyursunuz? Mən qırmızı köynəyi yuyuram.",
                },
                {
                    "fa": "شما (تو) چه‌کار می‌کنی؟ من دوش می‌گیرم.",
                    "reading_az": "Şoma (to) çekar mikoni? Mən duş migiram.",
                    "az": "Sən nə edirsən? Mən duş alıram.",
                },
                {
                    "fa": "شما کجا دوش می‌گیری؟ من در حمّام، دوش می‌گیرم.",
                    "reading_az": "Şoma koca duş migiri? Mən dər həmmam, duş migiram.",
                    "az": "Sən harada duş alırsan? Mən hamamda duş alıram.",
                },
                {
                    "fa": "نرگس چه دارد؟ او کیف و کتاب دارد.",
                    "reading_az": "Nərges çe darəd? U kif və ketab darəd.",
                    "az": "Nərgizin nəyi var? Onun çantası və kitabı var.",
                },
                {
                    "fa": "نرگس چه‌کار می‌کند؟ او درس می‌خواند.",
                    "reading_az": "Nərges çekar mikonəd? U dərs mixanəd.",
                    "az": "Nərgiz nə edir? O, dərs oxuyur.",
                },
                {
                    "fa": "نرگس کجا درس می‌خواند؟ او در اتاق مطالعه درس می‌خواند.",
                    "reading_az": "Nərges koca dərs mixanəd? U dər otağe motaleə dərs mixanəd.",
                    "az": "Nərgiz harada dərs oxuyur? O, iş otağında dərs oxuyur.",
                },
            ],
        },
        {
            "title_az": "Hörmət forması (تو → شما, او → ایشان)",
            "title_fa": "جمله‌ی محترمانه",
            "conjugations": [
                {"pronoun_fa": "تو", "form_fa": "شما"},
                {"pronoun_fa": "تو استاد هستی.", "form_fa": "شما استاد هستی. / شما استاد هستید."},
                {"pronoun_fa": "او", "form_fa": "ایشان"},
                {"pronoun_fa": "او استاد است.", "form_fa": "ایشان استاد است. / ایشان استاد هستند."},
            ],
            "examples": [
                {
                    "fa": "شما (تو) پزشک هستی. (شما پزشک هستید.)",
                    "reading_az": "Şoma (to) pezeşk həsti. (Şoma pezeşk həstid.)",
                    "az": "Sən həkimsən. → Hörmətlə: Siz həkimsiniz. (Fel həm təkdə, həm cəmdə ola bilər.)",
                },
                {
                    "fa": "ایشان (او) پلیس نیست؛ ایشان نگهبان است. (ایشان پلیس نیستند؛ ایشان نگهبان هستند.)",
                    "reading_az": "İşan (u) polis nist; işan negəhban əst. (İşan polis nistənd; işan negəhban həstənd.)",
                    "az": "O, polis deyil; keşikçidir. → Hörmətlə «او» yerinə «ایشان» deyilir; fel təkdə də, cəmdə də düzgündür.",
                },
                {
                    "fa": "آیا شما دو فرزند داری؟ (آیا شما دو فرزند دارید؟) — نه، من سه فرزند دارم.",
                    "reading_az": "Aya şoma do fərzənd dari? (Aya şoma do fərzənd darid?) — Nə, mən se fərzənd daram.",
                    "az": "Sizin iki övladınız var? — Xeyr, mənim üç övladım var. (Sual hər iki fel forması ilə düzgündür.)",
                },
                {
                    "fa": "آیا این خانم نقّاشی می‌کشد؟ (آیا ایشان نقّاشی می‌کشند؟) — نه، ایشان کتاب می‌خوانند.",
                    "reading_az": "Aya in xanom nəqqaşi mikeşəd? (Aya işan nəqqaşi mikeşənd?) — Nə, işan ketab mixanənd.",
                    "az": "Bu xanım rəsm çəkir? — Xeyr, o, kitab oxuyur. (Hörmətlə «ایشان» deyilir və fel cəmə keçir.)",
                },
                {
                    "fa": "آیا شما نامه می‌نویسی؟ (آیا شما نامه می‌نویسید؟) — نه، من روزنامه می‌خوانم.",
                    "reading_az": "Aya şoma name minevisi? (Aya şoma name minevisid?) — Nə, mən ruzname mixanəm.",
                    "az": "Siz məktub yazırsınız? — Xeyr, mən qəzet oxuyuram. (Sual hər iki fel forması ilə düzgündür.)",
                },
            ],
            "note_fa": (
                "۱. در جمله‌ی محترمانه به جای «تو» می‌گوییم «شما»:\n"
                "✅ تو استاد هستی. ← شما استاد هستی. / شما استاد هستید.\n"
                "۲. به جای «او» می‌گوییم «ایشان»:\n"
                "✅ او استاد است. ← ایشان استاد است. / ایشان استاد هستند.\n"
                "۳. در جمله‌ی محترمانه فعل می‌تواند مفرد بماند یا جمع شود؛ هر دو درست است."
            ),
            "note_reading_az": (
                '1. Dər comleye mohtərəmane be caye "to" miguyim "şoma":\n'
                "To ostad həsti. ← Şoma ostad həsti. / Şoma ostad həstid.\n"
                '2. Be caye "u" miguyim "işan":\n'
                "U ostad əst. ← İşan ostad əst. / İşan ostad həstənd.\n"
                "3. Dər comleye mohtərəmane fel mitəvanəd mofrəd bemanəd ya cəm şəvəd; hər do dorost əst."
            ),
            "note_az": (
                '1. Hörmət bildirən cümlədə "تو" (sən) əvəzinə "شما" (siz) deyilir:\n'
                "✅ Sən müəllimsən. ← Siz müəllimsiniz.\n"
                '2. "او" (o) əvəzinə "ایشان" (hörmətli "o") deyilir:\n'
                "✅ O, müəllimdir. ← O cənab / o xanım müəllimdir.\n"
                "3. Hörmət formasında fel həm təkdə qala bilər, həm də cəmə keçə bilər — hər ikisi düzgündür."
            ),
        },
    ],
    "exercises": [
        {
            "kind": "answer_question",
            "title_fa": "لطفاً پاسخ دهید",
            "instruction_az": "Suallara cavab verin",
            "note_fa": (
                "در جمله‌های پرسشی که «یا» وجود دارد، اگر دو فعل مختلف باشند، نمی‌توانیم فعل را حذف کنیم:\n"
                "✅ شما نقّاشی می‌کشید یا کتاب می‌خوانید؟\n"
                "❌ شما نقّاشی می‌کشید یا کتاب؟"
            ),
            "note_reading_az": (
                'Dər comlehaye porseşi ke "ya" vocud darəd, əgər do fel moxtəlef başənd, nemitəvanim fel ra həzf konim:\n'
                "Şoma nəqqaşi mikeşid ya ketab mixanid?\n"
                "Şoma nəqqaşi mikeşid ya ketab?"
            ),
            "note_az": (
                '"یа" (ya) olan sual cümlələrində iki fel fərqli olarsa, feli buraxa bilmərik:\n'
                "✅ Siz rəsm çəkirsiniz, yoxsa kitab oxuyursunuz?\n"
                "❌ Siz rəsm çəkirsiniz, yoxsa kitab?"
            ),
            "items": [
                {
                    "fa": "اتاق شما پنکه دارد یا کولر؟",
                    "reading_az": "Otaqe şoma pənke darəd ya kuler?",
                    "az": "Otağınızda ventilyator var, yoxsa kondisioner?",
                    "sample_answer_fa": "اتاق من کولر دارد.",
                    "sample_answer_reading_az": "Otaqe mən kuler darəd.",
                    "sample_answer_az": "Mənim otağımda kondisioner var.",
                },
                {
                    "fa": "شما (تو) اهل آفریقا هستی یا اروپا؟",
                    "reading_az": "Şoma (to) əhle Afriqa həsti ya Orupa?",
                    "az": "Siz (sən) Afrikadansınız, yoxsa Avropadan?",
                    "sample_answer_fa": "من اهل آفریقا هستم.",
                    "sample_answer_reading_az": "Mən əhle Afriqa həstəm.",
                    "sample_answer_az": "Mən Afrikadanam.",
                },
                {
                    "fa": "پتو و بالش شما تمیز است یا کثیف؟",
                    "reading_az": "Pətu va baleşe şoma təmiz əst ya kəsif?",
                    "az": "Adyalınız və yastığınız təmizdir, yoxsa çirkli?",
                    "sample_answer_fa": "پتو و بالش من تمیز است.",
                    "sample_answer_reading_az": "Pətu va baleşe mən təmiz əst.",
                    "sample_answer_az": "Mənim adyalım və yastığım təmizdir.",
                },
                {
                    "fa": "حیاط خانه‌ی شما باغچه دارد یا حوض؟",
                    "reading_az": "Həyate xane-ye şoma bağçe darəd ya hoz?",
                    "az": "Evinizin həyətində bağça var, yoxsa hovuz?",
                    "sample_answer_fa": "حیاط خانه‌ی ما باغچه دارد.",
                    "sample_answer_reading_az": "Həyate xane-ye ma bağçe darəd.",
                    "sample_answer_az": "Bizim evimizin həyətində bağça var.",
                },
                {
                    "fa": "استاد شما با ماژیک آبی می‌نویسد یا قرمز؟",
                    "reading_az": "Ostade şoma ba majike abi minevisəd ya qermez?",
                    "az": "Müəlliminiz mavi markerlə yazır, yoxsa qırmızı?",
                    "sample_answer_fa": "استاد من با ماژیک قرمز می‌نویسد.",
                    "sample_answer_reading_az": "Ostade mən ba majike qermez minevisəd.",
                    "sample_answer_az": "Müəllimim qırmızı markerlə yazır.",
                },
                {
                    "fa": "شما در آشپزخانه غذا می‌خورید یا در اتاق پذیرایی؟",
                    "reading_az": "Şoma dər aşpəzxane qəza mixorid ya dər otağe pəzirayi?",
                    "az": "Siz mətbəxdə yemək yeyirsiniz, yoxsa qonaq otağında?",
                    "sample_answer_fa": "من در اتاق پذیرایی غذا می‌خورم.",
                    "sample_answer_reading_az": "Mən dər otağe pəzirayi qəza mixorəm.",
                    "sample_answer_az": "Mən yeməyi qonaq otağında yeyirəm.",
                },
                {
                    "fa": "شما هر روز نقّاشی می‌کشید یا تکلیف می‌نویسید؟",
                    "reading_az": "Şoma hər ruz nəqqaşi mikeşid ya təklif minevisid?",
                    "az": "Siz hər gün rəsm çəkirsiniz, yoxsa tapşırıq yazırsınız?",
                    "sample_answer_fa": "من هر روز تکلیف می‌نویسم.",
                    "sample_answer_reading_az": "Mən hər ruz təklif minevisəm.",
                    "sample_answer_az": "Mən hər gün tapşırıq yazıram.",
                },
                {
                    "fa": "پدر شما ماشین را در پارکینگ می‌گذارد یا در حیاط؟",
                    "reading_az": "Pedəre şoma maşin ra dər parkinq migozarəd ya dər həyat?",
                    "az": "Atanız maşını avtomobil dayanacağına qoyur, yoxsa həyətə?",
                    "sample_answer_fa": "پدر من ماشین را در پارکینگ می‌گذارد.",
                    "sample_answer_reading_az": "Pedəre mən maşin ra dər parkinq migozarəd.",
                    "sample_answer_az": "Atam maşını avtomobil dayanacağında qoyur.",
                },
            ],
        },
        {
            "kind": "picture_sentences",
            "title_fa": "مانند مثال بپرسید و پاسخ دهید",
            "instruction_az": "Nümunə kimi soruşun və cavab verin",
            "example_fa": "مریم ظرف می‌شوید یا غذا می‌پزد؟",
            "example_reading_az": "Məryəm zərf mişuyəd ya qəza mipəzəd?",
            "example_az": "Məryəm qab yuyur, yoxsa yemək bişirir?",
            "example_answer_fa": "مریم غذا می‌پزد.",
            "example_answer_reading_az": "Məryəm qəza mipəzəd.",
            "example_answer_az": "Məryəm yemək bişirir.",
            "example_image_have": "assets/images/lessons/lesson_02/ghaza_mipazad.png",
            "example_image_not_have": "assets/images/lessons/lesson_02/zarf_mishuyad.png",
            "items": [
                {
                    "image_have": "assets/images/lessons/lesson_02/rahro.png",
                    "image_not_have": "assets/images/lessons/lesson_02/parking.png",
                    "sentences": [
                        {
                            "fa": "این راهرو است یا پارکینگ؟ این راهرو است.",
                            "reading_az": "İn rahro əst ya parkinq? İn rahro əst.",
                            "az": "Bu dəhlizdir, yoxsa avtomobil dayanacağı? Bu dəhlizdir.",
                        },
                    ],
                },
                {
                    "image_have": "assets/images/lessons/lesson_02/labasshuyi.png",
                    "image_not_have": "assets/images/lessons/lesson_02/abgarmkon.png",
                    "sentences": [
                        {
                            "fa": "این لباس‌شویی است یا آب‌گرم‌کن؟ این لباس‌شویی است.",
                            "reading_az": "İn ləbasşuyi əst ya abgərmkon? İn ləbasşuyi əst.",
                            "az": "Bu paltaryuyandır, yoxsa su qızdırıcısı? Bu paltaryuyandır.",
                        },
                    ],
                },
                {
                    "image_have": "assets/images/lessons/lesson_02/mishuyad.png",
                    "image_not_have": "assets/images/lessons/lesson_02/dush_migirad.png",
                    "sentences": [
                        {
                            "fa": "او دست می‌شوید یا دوش می‌گیرد؟ او دست می‌شوید.",
                            "reading_az": "U dəst mişuyəd ya duş migirəd? U dəst mişuyəd.",
                            "az": "O əlini yuyur, yoxsa duş alır? O əlini yuyur.",
                        },
                    ],
                },
                {
                    "image_have": "assets/images/lessons/lesson_02/ketab.png",
                    "image_not_have": "assets/images/lessons/lesson_01/jamedadi.png",
                    "sentences": [
                        {
                            "fa": "این کتاب است یا جامدادی؟ این کتاب است.",
                            "reading_az": "İn ketab əst ya camedadi? İn ketab əst.",
                            "az": "Bu kitabdır, yoxsa qələmqabı? Bu kitabdır.",
                        },
                    ],
                },
                {
                    "image_have": "assets/images/lessons/lesson_02/otagh_paziraei.png",
                    "image_not_have": "assets/images/lessons/lesson_02/otagh_motalee.png",
                    "sentences": [
                        {
                            "fa": "این اتاق پذیرایی است یا اتاق مطالعه؟ این اتاق پذیرایی است.",
                            "reading_az": "İn otağe pəzirayi əst ya otağe motaleə? İn otağe pəzirayi əst.",
                            "az": "Bu qonaq otağıdır, yoxsa iş otağı? Bu qonaq otağıdır.",
                        },
                    ],
                },
                {
                    "image_have": "assets/images/lessons/lesson_01/naghashi_mikeshad.png",
                    "image_not_have": "assets/images/lessons/lesson_01/pak_mikonad.png",
                    "sentences": [
                        {
                            "fa": "او نقّاشی می‌کشد یا تابلو را پاک می‌کند؟ او نقّاشی می‌کشد.",
                            "reading_az": "U nəqqaşi mikeşəd ya təblo ra pak mikonəd? U nəqqaşi mikeşəd.",
                            "az": "O rəsm çəkir, yoxsa lövhəni silir? O rəsm çəkir.",
                        },
                    ],
                },
            ],
        },
        {
            "kind": "picture_sentences",
            "title_fa": "مانند مثال بپرسید و پاسخ دهید",
            "instruction_az": "Nümunə kimi soruşun və cavab verin",
            "example_fa": "این کودک چه‌کار می‌کند؟",
            "example_reading_az": "İn kudək çekar mikonəd?",
            "example_az": "Bu uşaq nə edir?",
            "example_answer_fa": "این کودک غذا می‌خورد.",
            "example_answer_reading_az": "İn kudək qəza mixorəd.",
            "example_answer_az": "Bu uşaq yemək yeyir.",
            "example_image": "assets/images/lessons/lesson_02/ghaza_mikhorad.png",
            "items": [
                {
                    "sentences": [
                        {
                            "fa": "این پسر چه‌کار می‌کند؟ این پسر ماشین را می‌شوید.",
                            "reading_az": "İn pesər çekar mikonəd? İn pesər maşin ra mişuyəd.",
                            "az": "Bu oğlan nə edir? Bu oğlan maşını yuyur.",
                        },
                    ],
                },
                {
                    "sentences": [
                        {
                            "fa": "این خانم چه‌کار می‌کند؟ این خانم کتاب می‌خواند.",
                            "reading_az": "İn xanom çekar mikonəd? İn xanom ketab mixanəd.",
                            "az": "Bu xanım nə edir? Bu xanım kitab oxuyur.",
                        },
                    ],
                },
                {
                    "sentences": [
                        {
                            "fa": "این دختر چه‌کار می‌کند؟ این دختر درس می‌خواند.",
                            "reading_az": "İn doxtər çekar mikonəd? İn doxtər dərs mixanəd.",
                            "az": "Bu qız nə edir? Bu qız dərs oxuyur.",
                        },
                    ],
                },
                {
                    "sentences": [
                        {
                            "fa": "این پسر چه‌کار می‌کند؟ این پسر دوش می‌گیرد.",
                            "reading_az": "İn pesər çekar mikonəd? İn pesər duş migirəd.",
                            "az": "Bu oğlan nə edir? Bu oğlan duş alır.",
                        },
                    ],
                },
                {
                    "sentences": [
                        {
                            "fa": "این خانم‌ها چه‌کار می‌کنند؟ این خانم‌ها غذا می‌پزند.",
                            "reading_az": "İn xanomha çekar mikonənd? İn xanomha qəza mipəzənd.",
                            "az": "Bu xanımlar nə edir? Bu xanımlar yemək bişirir.",
                        },
                    ],
                },
                {
                    "sentences": [
                        {
                            "fa": "این خانم چه‌کار می‌کند؟ این خانم نقّاشی می‌کشد.",
                            "reading_az": "İn xanom çekar mikonəd? İn xanom nəqqaşi mikeşəd.",
                            "az": "Bu xanım nə edir? Bu xanım rəsm çəkir.",
                        },
                    ],
                },
                {
                    "sentences": [
                        {
                            "fa": "این پسر چه‌کار می‌کند؟ این پسر غذا می‌خورد.",
                            "reading_az": "İn pesər çekar mikonəd? İn pesər qəza mixorəd.",
                            "az": "Bu oğlan nə edir? Bu oğlan yemək yeyir.",
                        },
                    ],
                },
                {
                    "sentences": [
                        {
                            "fa": "این پسر چه‌کار می‌کند؟ این پسر صورتش را می‌شوید.",
                            "reading_az": "İn pesər çekar mikonəd? İn pesər surətəş ra mişuyəd.",
                            "az": "Bu oğlan nə edir? Bu oğlan üzünü yuyur.",
                        },
                    ],
                },
                {
                    "sentences": [
                        {
                            "fa": "این دختر چه‌کار می‌کند؟ این دختر روی تخته می‌نویسد.",
                            "reading_az": "İn doxtər çekar mikonəd? İn doxtər ruye təxte minevisəd.",
                            "az": "Bu qız nə edir? Bu qız lövhəyə yazır.",
                        },
                    ],
                },
            ],
        },
        {
            "kind": "fill_blank",
            "instruction_az": "Boşluğu söz bankından uyğun sözlə doldurun.",
            "word_bank": [
                "دوش می‌گیرند", "پاک می‌کنم", "وجود دارد", "غذا می‌پزد",
                "درس می‌خوانید", "می‌کشیم", "می‌گذارد", "می‌شوید",
            ],
            "items": [
                {
                    "fa_with_blank": "آن‌ها در حمّام ___ .",
                    "correct_answer": "دوش می‌گیرند",
                    "reading_az": "duş migirənd",
                    "az": "duş alırlar",
                    "full_reading_az": "Anha dər həmmam duş migirənd.",
                    "full_translation_az": "Onlar hamamda duş alırlar.",
                },
                {
                    "fa_with_blank": "من هر روز تابلو را ___ .",
                    "correct_answer": "پاک می‌کنم",
                    "reading_az": "pak mikonəm",
                    "az": "təmizləyirəm",
                    "full_reading_az": "Mən hər ruz təblo ra pak mikonəm.",
                    "full_translation_az": "Mən hər gün lövhəni təmizləyirəm.",
                },
                {
                    "fa_with_blank": "در اتاق‌خوابِ من، تخت ___ .",
                    "correct_answer": "وجود دارد",
                    "reading_az": "vocud darəd",
                    "az": "var",
                    "full_reading_az": "Dər otağe xabe mən, təxt vocud darəd.",
                    "full_translation_az": "Mənim yataq otağımda çarpayı var.",
                },
                {
                    "fa_with_blank": "مادرم هر روز در آشپزخانه ___ .",
                    "correct_answer": "غذا می‌پزد",
                    "reading_az": "qəza mipəzəd",
                    "az": "yemək bişirir",
                    "full_reading_az": "Madərəm hər ruz dər aşpəzxane qəza mipəzəd.",
                    "full_translation_az": "Anam hər gün mətbəxdə yemək bişirir.",
                },
                {
                    "fa_with_blank": "شما هر روز در اتاقِ مطالعه ___ .",
                    "correct_answer": "درس می‌خوانید",
                    "reading_az": "dərs mixanid",
                    "az": "dərs oxuyursunuz",
                    "full_reading_az": "Şoma hər ruz dər otağe motaleə dərs mixanid.",
                    "full_translation_az": "Siz hər gün iş otağında dərs oxuyursunuz.",
                },
                {
                    "fa_with_blank": "من و حسین در کلاس، نقّاشی ___ .",
                    "correct_answer": "می‌کشیم",
                    "reading_az": "mikeşim",
                    "az": "çəkirik",
                    "full_reading_az": "Mən va Hoseyn dər kelas, nəqqaşi mikeşim.",
                    "full_translation_az": "Mən və Hüseyn sinifdə rəsm çəkirik.",
                },
                {
                    "fa_with_blank": "نرگس لباس‌های کثیف را در لباس‌شویی ___ .",
                    "correct_answer": "می‌گذارد",
                    "reading_az": "migozarəd",
                    "az": "qoyur",
                    "full_reading_az": "Nərges lebashaye kəsif ra dər ləbasşuyi migozarəd.",
                    "full_translation_az": "Nərgiz çirkli paltarları paltaryuyana qoyur.",
                },
                {
                    "fa_with_blank": "خدیجه لباس‌های کثیف را با لباس‌شویی ___ .",
                    "correct_answer": "می‌شوید",
                    "reading_az": "mişuyəd",
                    "az": "yuyur",
                    "full_reading_az": "Xədice lebashaye kəsif ra ba ləbasşuyi mişuyəd.",
                    "full_translation_az": "Xədicə çirkli paltarları paltaryuyanla yuyur.",
                },
            ],
        },
        {
            "kind": "answer_question",
            "title_fa": "خانه‌ی ما",
            "instruction_az": "Nümunə kimi deyin",
            "example_fa": "*خانه‌ی ما*\nخانه‌ی ما دو اتاق خواب، یک اتاق پذیرایی، آشپزخانه و سرویس بهداشتی *دارد*.",
            "example_reading_az": "Xane-ye ma do otağe xab, yek otağe pəzirayi, aşpəzxane va servise behdaşti darəd.",
            "example_az": "Bizim evimizin iki yataq otağı, bir qonaq otağı, mətbəxi və sanitar qovşağı var.",
            "items": [
                {
                    "fa": "اتاق من",
                    "reading_az": "Otaqe mən",
                    "az": "Mənim otağım",
                    "sample_answer_fa": "اتاق من یک تخت، یک میز و یک کتابخانه دارد.",
                    "sample_answer_reading_az": "Otaqe mən yek təxt, yek miz va yek ketabxane darəd.",
                    "sample_answer_az": "Mənim otağımın bir çarpayısı, bir masası və bir kitab rəfi var.",
                },
                {
                    "fa": "آشپزخانه‌ی ما",
                    "reading_az": "Aşpəzxane-ye ma",
                    "az": "Bizim mətbəximiz",
                    "sample_answer_fa": "آشپزخانه‌ی ما یک اجاق‌گاز، یک یخچال و یک ظرف‌شویی دارد.",
                    "sample_answer_reading_az": "Aşpəzxane-ye ma yek ocaq-qaz, yek yəxçal va yek zərfşuyi darəd.",
                    "sample_answer_az": "Bizim mətbəximizin bir qaz plitəsi, bir soyuducusu və bir qabyuyan maşını var.",
                },
                {
                    "fa": "مدرسه‌ی شما",
                    "reading_az": "Mædrese-ye şoma",
                    "az": "Sizin məktəbiniz",
                    "sample_answer_fa": "مدرسه‌ی ما چند کلاس، یک کتابخانه و یک حیاط بزرگ دارد.",
                    "sample_answer_reading_az": "Mædrese-ye ma çənd kelas, yek ketabxane va yek həyate bozorg darəd.",
                    "sample_answer_az": "Bizim məktəbimizin bir neçə sinfi, bir kitabxanası və bir böyük həyəti var.",
                },
                {
                    "fa": "حیاط خانه‌ی پدرم",
                    "reading_az": "Həyate xane-ye pedərəm",
                    "az": "Atamın evinin həyəti",
                    "sample_answer_fa": "حیاط خانه‌ی پدرم یک باغچه و چند درخت میوه دارد.",
                    "sample_answer_reading_az": "Həyate xane-ye pedərəm yek bağçe va çənd dərəxte mive darəd.",
                    "sample_answer_az": "Atamın evinin həyətində bir bağça və bir neçə meyvə ağacı var.",
                },
            ],
        },
        {
            "kind": "practice_reveal",
            "title_fa": "مانند مثال تبدیل کنید",
            "instruction_az": "Nümunə kimi hörmət formasına çevirin",
            "example_fa": "*تو* پرستار *هستی*. ← *شما* پرستار *هستی*. / *شما* پرستار *هستید*.",
            "example_reading_az": "To pərəstar həsti. ← Şoma pərəstar həsti. / Şoma pərəstar həstid.",
            "example_az": "Sən tibb bacısısan. ← Siz tibb bacısısınız. (Fel tək və ya cəm ola bilər.)",
            "items": [
                {
                    "prompt_fa": "تو نگهبان هستی.",
                    "answer_fa": "شما نگهبان هستی. / شما نگهبان هستید.",
                    "reading_az": "Şoma negəhban həsti. / Şoma negəhban həstid.",
                    "az": "Siz keşikçisiniz.",
                },
                {
                    "prompt_fa": "او استاد نیست.",
                    "answer_fa": "ایشان استاد نیست. / ایشان استاد نیستند.",
                    "reading_az": "İşan ostad nist. / İşan ostad nistənd.",
                    "az": "Onlar müəllim deyillər.",
                },
                {
                    "prompt_fa": "او کتاب را روی میز می‌گذارد.",
                    "answer_fa": "ایشان کتاب را روی میز می‌گذارد. / ایشان کتاب را روی میز می‌گذارند.",
                    "reading_az": "İşan ketab ra ruye miz migozarəd. / İşan ketab ra ruye miz migozarənd.",
                    "az": "Onlar kitabı masanın üstünə qoyurlar.",
                },
                {
                    "prompt_fa": "تو در رستوران، غذا می‌خوری.",
                    "answer_fa": "شما در رستوران، غذا می‌خوری. / شما در رستوران، غذا می‌خورید.",
                    "reading_az": "Şoma dər restoran, qəza mixori. / Şoma dər restoran, qəza mixorid.",
                    "az": "Siz restoranda yemək yeyirsiniz.",
                },
                {
                    "prompt_fa": "آیا او محمّدمهدی است؟",
                    "answer_fa": "آیا ایشان محمّدمهدی است؟ / آیا ایشان محمّدمهدی هستند؟",
                    "reading_az": "Aya işan Mohəmmədmehdi əst? / Aya işan Mohəmmədmehdi həstənd?",
                    "az": "O zat Məhəmmədmehdidirmi?",
                },
                {
                    "prompt_fa": "آیا تو الآن دوش می‌گیری؟",
                    "answer_fa": "آیا شما الآن دوش می‌گیری؟ / آیا شما الآن دوش می‌گیرید؟",
                    "reading_az": "Aya şoma əl-an duş migiri? / Aya şoma əl-an duş migirid?",
                    "az": "Siz indi duş alırsınız?",
                },
            ],
        },
        {
            "kind": "fill_blank",
            "instruction_az": "Boşluğu söz bankından uyğun sözlə doldurun.",
            "word_bank": [
                "قفسه", "پارکینگ", "مطالعه", "حمّام", "پشت‌بام", "لباس‌شویی", "خواب",
            ],
            "items": [
                {
                    "fa_with_blank": "او الآن در ___ دوش می‌گیرد.",
                    "correct_answer": "حمّام",
                    "reading_az": "həmmam",
                    "az": "hamam",
                    "full_reading_az": "U al-an dər həmmam duş migirəd.",
                    "full_translation_az": "O, indi hamamda duş alır.",
                },
                {
                    "fa_with_blank": "من کتاب‌هایم را در ___ می‌گذارم.",
                    "correct_answer": "قفسه",
                    "reading_az": "qafase",
                    "az": "rəf",
                    "full_reading_az": "Mən ketab-hayam ra dər qafase migozaram.",
                    "full_translation_az": "Mən kitablarımı rəfə qoyuram.",
                },
                {
                    "fa_with_blank": "ماشین در ___ است.",
                    "correct_answer": "پارکینگ",
                    "reading_az": "parkinq",
                    "az": "avtomobil dayanacağı",
                    "full_reading_az": "Maşin dər parkinq əst.",
                    "full_translation_az": "Maşın avtomobil dayanacağındadır.",
                },
                {
                    "fa_with_blank": "کولر روی ___ است.",
                    "correct_answer": "پشت‌بام",
                    "reading_az": "poştebam",
                    "az": "dam",
                    "full_reading_az": "Kuler ruye poştebam əst.",
                    "full_translation_az": "Kondisioner damın üstündədir.",
                },
                {
                    "fa_with_blank": "مادرم لباس‌های کثیف را در ___ می‌گذارد.",
                    "correct_answer": "لباس‌شویی",
                    "reading_az": "lebasşuyi",
                    "az": "paltaryuyan",
                    "full_reading_az": "Madərəm lebashaye kəsif ra dər ləbasşuyi migozarəd.",
                    "full_translation_az": "Anam çirkli paltarları paltaryuyana qoyur.",
                },
                {
                    "fa_with_blank": "در اتاق ___‌ی من دو قفسه‌ی کتاب وجود دارد.",
                    "correct_answer": "مطالعه",
                    "reading_az": "motaleə",
                    "az": "iş/oxu",
                    "full_reading_az": "Dər otağe motaleə-ye mən do qafase-ye ketab vocud darəd.",
                    "full_translation_az": "Mənim iş otağımda iki kitab rəfi var.",
                },
                {
                    "fa_with_blank": "در اتاق ___ جواد تخت، تشک، بالش و پتو هست.",
                    "correct_answer": "خواب",
                    "reading_az": "xab",
                    "az": "yataq",
                    "full_reading_az": "Dər otağe xabe Cavad təxt, toşək, baleş va pətu həst.",
                    "full_translation_az": "Cavadın yataq otağında çarpayı, döşək, yastıq və adyal var.",
                },
            ],
        },
        {
            "kind": "picture_sentences",
            "title_fa": "برای هر تصویر، دو جمله بگویید",
            "instruction_az": "Hər şəkil üçün iki cümlə deyin",
            "items": [
                {
                    "image": "assets/images/lessons/lesson_02/ashpazkhane.png",
                    "sentences": [
                        {
                            "fa": "این آشپزخانه است.",
                            "reading_az": "İn aşpəzxane əst.",
                            "az": "Bu mətbəxdir.",
                        },
                        {
                            "fa": "در آشپزخانه، اجاق‌گاز و کتری وجود دارد.",
                            "reading_az": "Dər aşpəzxane, ocaq-qaz və ketri vocud darəd.",
                            "az": "Mətbəxdə qaz plitəsi və çaydan var.",
                        },
                    ],
                },
                {
                    "image": "assets/images/lessons/lesson_02/otagh_khab.png",
                    "sentences": [
                        {
                            "fa": "این اتاق خواب است.",
                            "reading_az": "İn otağe xab əst.",
                            "az": "Bu yataq otağıdır.",
                        },
                        {
                            "fa": "در اتاق خواب، تخت و بالش وجود دارد.",
                            "reading_az": "Dər otağe xab, təxt və baleş vocud darəd.",
                            "az": "Yataq otağında çarpayı və yastıq var.",
                        },
                    ],
                },
                {
                    "image": "assets/images/lessons/lesson_02/ghaza_mipazad.png",
                    "sentences": [
                        {
                            "fa": "این خانم در آشپزخانه است.",
                            "reading_az": "İn xanom dər aşpəzxane əst.",
                            "az": "Bu xanım mətbəxdədir.",
                        },
                        {
                            "fa": "این خانم غذا می‌پزد.",
                            "reading_az": "İn xanom qəza mipəzəd.",
                            "az": "Bu xanım yemək bişirir.",
                        },
                    ],
                },
                {
                    "image": "assets/images/lessons/lesson_02/otagh_paziraei.png",
                    "sentences": [
                        {
                            "fa": "این اتاق پذیرایی است.",
                            "reading_az": "İn otağe pəzirayi əst.",
                            "az": "Bu qonaq otağıdır.",
                        },
                        {
                            "fa": "در اتاق پذیرایی، مبل وجود دارد.",
                            "reading_az": "Dər otağe pəzirayi, mobl vocud darəd.",
                            "az": "Qonaq otağında divan var.",
                        },
                    ],
                },
                {
                    "image": "assets/images/lessons/lesson_02/otagh_motalee.png",
                    "sentences": [
                        {
                            "fa": "این اتاق مطالعه است.",
                            "reading_az": "İn otağe motaleə əst.",
                            "az": "Bu iş otağıdır.",
                        },
                        {
                            "fa": "من در اتاق مطالعه درس می‌خوانم.",
                            "reading_az": "Mən dər otağe motaleə dərs mixanəm.",
                            "az": "Mən iş otağında dərs oxuyuram.",
                        },
                    ],
                },
                {
                    "image": "assets/images/lessons/lesson_02/dush_migirad.png",
                    "sentences": [
                        {
                            "fa": "این پسر در حمّام است.",
                            "reading_az": "İn pesər dər həmmam əst.",
                            "az": "Bu oğlan hamamdadır.",
                        },
                        {
                            "fa": "این پسر دوش می‌گیرد.",
                            "reading_az": "İn pesər duş migirəd.",
                            "az": "Bu oğlan duş alır.",
                        },
                    ],
                },
                {
                    "image": "assets/images/lessons/lesson_02/baghche.png",
                    "sentences": [
                        {
                            "fa": "این باغچه است.",
                            "reading_az": "İn bağçe əst.",
                            "az": "Bu bağçadır.",
                        },
                        {
                            "fa": "در باغچه، گل و درخت وجود دارد.",
                            "reading_az": "Dər bağçe, gol və dərəxt vocud darəd.",
                            "az": "Bağçada gül və ağac var.",
                        },
                    ],
                },
                {
                    "image": "assets/images/lessons/lesson_02/hammam.png",
                    "sentences": [
                        {
                            "fa": "این حمّام است.",
                            "reading_az": "İn həmmam əst.",
                            "az": "Bu hamam otağıdır.",
                        },
                        {
                            "fa": "حمّام ما تمیز است.",
                            "reading_az": "Həmmame ma təmiz əst.",
                            "az": "Bizim hamamımız təmizdir.",
                        },
                    ],
                },
            ],
        },
    ],
    "sentence_practice": {
        "answer_note_fa": "۱. کجاست؟ = کجا است؟",
        "answer_note_reading_az": "1. Kocast? = Koca əst?",
        "answer_note_az": '1. "کجاست؟" (haradadır?) — "کجا است؟" birləşməsinin qısaldılmış formasıdır; hər ikisi eyni mənadadır.',
        "listen_exercises": [
            {
                "items": [
                    {
                        "fa": "خانه‌ی ما دو طبقه است و شش اتاق دارد.",
                        "reading_az": "Xane-ye ma do təbəqe əst və şeş otaq darəd.",
                        "az": "Bizim evimiz iki mərtəbəlidir və altı otağı var.",
                    },
                    {
                        "fa": "اتاق خواب و اتاق مطالعه‌ی من در طبقه‌ی دوم است.",
                        "reading_az": "Otağe xab və otağe motaleə-ye mən dər təbəqe-ye dovvom əst.",
                        "az": "Yataq otağım və iş otağım ikinci mərtəbədədir.",
                    },
                    {
                        "fa": "در اتاق خوابِ من، تخت، تشک، بالش، پتو و پرده وجود دارد.",
                        "reading_az": "Dər otağe xabe mən, təxt, toşək, baleş, pətu və pərde vocud darəd.",
                        "az": "Mənim yataq otağımda çarpayı, döşək, yastıq, adyal və pərdə var.",
                    },
                    {
                        "fa": "حیاط خانه‌ی ما بزرگ است. در حیاط ما یک باغچه هست.",
                        "reading_az": "Həyate xane-ye ma bozorg əst. Dər həyate ma yek bağçe həst.",
                        "az": "Evimizin həyəti böyükdür. Həyətimizdə bir bağça var.",
                    },
                    {
                        "fa": "در باغچه‌ی خانه‌ی ما یک درخت سیب و یک درخت انار وجود دارد.",
                        "reading_az": "Dər bağçe-ye xane-ye ma yek dərəxte sib və yek dərəxte anar vocud darəd.",
                        "az": "Evimizin bağçasında bir alma ağacı və bir nar ağacı var.",
                    },
                    {
                        "fa": "آن‌ها در تابستان با آب سرد و در زمستان با آب گرم دوش می‌گیرند.",
                        "reading_az": "Anha dər tabestan ba abe sərd və dər zemestan ba abe gərm duş migirənd.",
                        "az": "Onlar yayda soyuq su ilə, qışda isə isti su ilə duş alırlar.",
                    },
                    {
                        "fa": "خانه‌ی ما پارکینگ و حیاط ندارد. پدرم ماشین را در خیابان می‌گذارد.",
                        "reading_az": "Xane-ye ma parkinq və həyat nədarəd. Pedərəm maşin ra dər xiyaban migozarəd.",
                        "az": "Bizim evimizin avtomobil dayanacağı və həyəti yoxdur. Atam maşını küçəyə qoyur.",
                    },
                    {
                        "fa": "مادرم هر روز در آشپزخانه غذا می‌پزد و خواهرم سارا ظرف‌ها را می‌شوید.",
                        "reading_az": "Madərəm hər ruz dər aşpəzxane qəza mipəzəd və xahərəm Sara zərfha ra mişuyəd.",
                        "az": "Anam hər gün mətbəxdə yemək bişirir, bacım Sara isə qabları yuyur.",
                    },
                    {
                        "fa": "پرده‌های خانه‌ی ما کثیف است. من با لباس‌شویی، پرده‌های کثیف را می‌شویم.",
                        "reading_az": "Pərdehaye xane-ye ma kəsif əst. Mən ba ləbasşuyi, pərdehaye kəsif ra mişuyəm.",
                        "az": "Bizim evimizin pərdələri çirklidir. Mən çirkli pərdələri paltaryuyanla yuyuram.",
                    },
                    {
                        "fa": "در آشپزخانه‌ی ما اجاق‌گاز، لباس‌شویی، آب‌گرم‌کن و یک ظرف‌شویی بزرگ وجود دارد.",
                        "reading_az": "Dər aşpəzxane-ye ma ocaq-qaz, ləbasşuyi, abgərmkon və yek zərfşuyi-ye bozorg vocud darəd.",
                        "az": "Bizim mətbəximizdə qaz plitəsi, paltaryuyan, su qızdırıcısı və bir böyük qabyuyan maşın var.",
                    },
                ],
            },
        ],
        "answer_items": [
            {
                "fa": "آیا پدر شما غذا نمی‌پزد؟",
                "reading_az": "Aya pedəre şoma qəza nemipəzəd?",
                "az": "Atanız yemək bişirmir?",
                "sample_answer_fa": "نه، پدر من غذا نمی‌پزد؛ مادرم غذا می‌پزد.",
                "sample_answer_reading_az": "Nə, pedəre mən qəza nemipəzəd; madərəm qəza mipəzəd.",
                "sample_answer_az": "Xeyr, atam yemək bişirmir; anam yemək bişirir.",
            },
            {
                "fa": "شما ظرف‌ها را کجا می‌شویید؟",
                "reading_az": "Şoma zərfha ra koca mişuyid?",
                "az": "Siz qabları harada yuyursunuz?",
                "sample_answer_fa": "ما ظرف‌ها را در آشپزخانه می‌شوییم.",
                "sample_answer_reading_az": "Ma zərfha ra dər aşpəzxane mişuyim.",
                "sample_answer_az": "Biz qabları mətbəxdə yuyuruq.",
            },
            {
                "fa": "یخچال مدرسه‌ی شما کجاست؟",
                "reading_az": "Yəxçale mædrese-ye şoma kocast?",
                "az": "Məktəbinizin soyuducusu haradadır?",
                "sample_answer_fa": "یخچال مدرسه‌ی ما در آشپزخانه است.",
                "sample_answer_reading_az": "Yəxçale mædrese-ye ma dər aşpəzxane əst.",
                "sample_answer_az": "Məktəbimizin soyuducusu mətbəxdədir.",
            },
            {
                "fa": "آیا پرده‌ی اتاق شما تمیز نیست؟",
                "reading_az": "Aya pərde-ye otağe şoma təmiz nist?",
                "az": "Otağınızın pərdəsi təmiz deyilmi?",
                "sample_answer_fa": "چرا، پرده‌ی اتاق ما تمیز است.",
                "sample_answer_reading_az": "Çera, pərde-ye otağe ma təmiz əst.",
                "sample_answer_az": "Xeyr (əksinə), otağımızın pərdəsi təmizdir.",
            },
            {
                "fa": "آیا کولر شما روی پشت‌بام است؟",
                "reading_az": "Aya kuler-e şoma ruye poştebam əst?",
                "az": "Sizin kondisioneriniz damın üstündədir?",
                "sample_answer_fa": "بله، کولر ما روی پشت‌بام است.",
                "sample_answer_reading_az": "Bəle, kuler-e ma ruye poştebam əst.",
                "sample_answer_az": "Bəli, bizim kondisionerimiz damın üstündədir.",
            },
            {
                "fa": "آیا لباس‌شویی شما در حمّام است؟",
                "reading_az": "Aya ləbasşuyi-ye şoma dər həmmam əst?",
                "az": "Paltaryuyanınız hamamdadır?",
                "sample_answer_fa": "نه، لباس‌شویی ما در آشپزخانه است.",
                "sample_answer_reading_az": "Nə, ləbasşuyi-ye ma dər aşpəzxane əst.",
                "sample_answer_az": "Xeyr, bizim paltaryuyanımız mətbəxdədir.",
            },
        ],
    },
    "reading_text": {
        "title_fa": "خانه‌ی برادرم",
        "title_az": "Qardaşımın evi",
        "image": "assets/images/lessons/lesson_02/reading_khane_baradaram.png",
        "paragraphs_fa": [
            "تهران، پایتخت ایران است. خانه‌ی برادرم احمد در تهران است. خانه‌ی او دو طبقه است.",
            "ایشان سه فرزند دارد: دو دختر به نام فاطمه و زینب و یک پسر به نام علی. فاطمه بزرگ‌ترین فرزند برادرم است.",
            "خانه‌ی برادرم یک سالن پذیرایی، دو اتاق خواب، یک اتاق مطالعه، آشپزخانه و سرویس‌بهداشتی دارد. سالن پذیرایی و اتاق مطالعه‌ی آن‌ها در طبقه‌ی دوم است.",
            "در سالن پذیرایی آن‌ها مبل، میز پذیرایی و یک تلویزیون بزرگ هست و در اتاق مطالعه سه قفسه‌ی کتاب، چهار صندلی و یک میز بزرگ وجود دارد.",
            "روی میز، رایانه، چراغ مطالعه، تقویم، کتاب و نوشت‌افزار هست. فاطمه و علی هر روز در این اتاق درس می‌خوانند و تکلیف می‌نویسند.",
        ],
        "footnotes": [
            {"fa": "بزرگ‌ترین", "az": "ən böyük"},
            {"fa": "وجود دارد / هست", "az": "var"},
        ],
        "full_translation_az": (
            "Tehran, İranın paytaxtıdır. Qardaşım Əhmədin evi Tehrandadır. Onun evi iki mərtəbəlidir.\n\n"
            "Onun üç övladı var: Fatimə və Zeynəb adında iki qızı və Əli adında bir oğlu. Fatimə qardaşımın ən böyük övladıdır.\n\n"
            "Qardaşımın evində bir qonaq otağı, iki yataq otağı, bir iş otağı, mətbəx və sanitar qovşağı var. Onların "
            "qonaq otağı və iş otağı ikinci mərtəbədədir.\n\n"
            "Qonaq otağında divan, qonaq masası və böyük bir televizor var, iş otağında isə üç kitab rəfi, dörd stul "
            "və böyük bir masa var.\n\n"
            "Masanın üstündə komputer, masa lampası, təqvim, kitab və yazı ləvazimatı var. Fatimə və Əli hər gün bu "
            "otaqda dərs oxuyur və tapşırıq yazırlar."
        ),
        "sentences": [
            {
                "fa": "تهران، پایتخت ایران است.",
                "reading_az": "Tehran, paytəxte Iran əst.",
                "az": "Tehran, İranın paytaxtıdır.",
                "new_paragraph": True,
            },
            {
                "fa": "خانه‌ی برادرم احمد در تهران است.",
                "reading_az": "Xane-ye bəradərəm Əhməd dər Tehran əst.",
                "az": "Qardaşım Əhmədin evi Tehrandadır.",
            },
            {
                "fa": "خانه‌ی او دو طبقه است.",
                "reading_az": "Xane-ye u do təbəqe əst.",
                "az": "Onun evi iki mərtəbəlidir.",
            },
            {
                "fa": "ایشان سه فرزند دارد: دو دختر به نام فاطمه و زینب و یک پسر به نام علی.",
                "reading_az": "İşan se fərzənd darəd: do doxtər be name Fateme və Zeynəb və yek pesər be name Əli.",
                "az": "Onun üç övladı var: Fatimə və Zeynəb adında iki qızı, Əli adında bir oğlu.",
                "new_paragraph": True,
            },
            {
                "fa": "فاطمه بزرگ‌ترین فرزند برادرم است.",
                "reading_az": "Fateme bozorgtərin fərzənde bəradərəm əst.",
                "az": "Fatimə qardaşımın ən böyük övladıdır.",
            },
            {
                "fa": "خانه‌ی برادرم یک سالن پذیرایی، دو اتاق خواب، یک اتاق مطالعه، آشپزخانه و سرویس‌بهداشتی دارد.",
                "reading_az": "Xane-ye bəradərəm yek salone pəziraei, do otağe xab, yek otağe motaleə, aşpəzxane və servise behdaşti darəd.",
                "az": "Qardaşımın evində bir qonaq otağı, iki yataq otağı, bir iş otağı, mətbəx və sanitar qovşağı var.",
                "new_paragraph": True,
            },
            {
                "fa": "سالن پذیرایی و اتاق مطالعه‌ی آن‌ها در طبقه‌ی دوم است.",
                "reading_az": "Salone pəziraei va otağe motaleə-ye anha dər təbəqe-ye dovvom əst.",
                "az": "Onların qonaq otağı və iş otağı ikinci mərtəbədədir.",
            },
            {
                "fa": "در سالن پذیرایی آن‌ها مبل، میز پذیرایی و یک تلویزیون بزرگ هست.",
                "reading_az": "Dər salone pəziraei-ye anha mobl, mize pəziraei və yek televizione bozorg həst.",
                "az": "Onların qonaq otağında divan, qonaq masası və böyük bir televizor var.",
                "new_paragraph": True,
            },
            {
                "fa": "و در اتاق مطالعه سه قفسه‌ی کتاب، چهار صندلی و یک میز بزرگ وجود دارد.",
                "reading_az": "Va dər otağe motaleə se qafase-ye ketab, çahar səndəli və yek mize bozorg vocud darəd.",
                "az": "İş otağında isə üç kitab rəfi, dörd stul və böyük bir masa var.",
            },
            {
                "fa": "روی میز، رایانه، چراغ مطالعه، تقویم، کتاب و نوشت‌افزار هست.",
                "reading_az": "Ruye miz, rayane, çerağe motaleə, təqvim, ketab və neveştəfzar həst.",
                "az": "Masanın üstündə komputer, masa lampası, təqvim, kitab və yazı ləvazimatı var.",
                "new_paragraph": True,
            },
            {
                "fa": "فاطمه و علی هر روز در این اتاق درس می‌خوانند و تکلیف می‌نویسند.",
                "reading_az": "Fateme va Əli hər ruz dər in otaq dərs mixanənd va təklif minevisənd.",
                "az": "Fatimə və Əli hər gün bu otaqda dərs oxuyur və tapşırıq yazırlar.",
            },
        ],
        "comprehension_questions": [
            {
                "question_fa": "پایتخت ایران کجاست؟",
                "reading_az": "Paytəxte Iran kocast?",
                "az": "İranın paytaxtı haradadır?",
                "sample_answer_fa": "پایتخت ایران، تهران است.",
                "sample_answer_reading_az": "Paytəxte Iran, Tehran əst.",
                "sample_answer_az": "İranın paytaxtı Tehrandır.",
            },
            {
                "question_fa": "خانه‌ی احمد در کدام شهر است؟",
                "reading_az": "Xane-ye Əhməd dər kodam şəhr əst?",
                "az": "Əhmədin evi hansı şəhərdədir?",
                "sample_answer_fa": "خانه‌ی احمد در تهران است.",
                "sample_answer_reading_az": "Xane-ye Əhməd dər Tehran əst.",
                "sample_answer_az": "Əhmədin evi Tehrandadır.",
            },
            {
                "question_fa": "آیا احمد دو پسر و یک دختر دارد؟",
                "reading_az": "Aya Əhməd do pesər və yek doxtər darəd?",
                "az": "Əhmədin iki oğlu və bir qızı varmı?",
                "sample_answer_fa": "نه، احمد دو دختر و یک پسر دارد.",
                "sample_answer_reading_az": "Nə, Əhməd do doxtər və yek pesər darəd.",
                "sample_answer_az": "Xeyr, Əhmədin iki qızı və bir oğlu var.",
            },
            {
                "question_fa": "اسم بزرگ‌ترین فرزند احمد چیست؟",
                "reading_az": "Esme bozorgtərin fərzəde Əhməd çist?",
                "az": "Əhmədin ən böyük övladının adı nədir?",
                "sample_answer_fa": "اسم بزرگ‌ترین فرزند احمد، فاطمه است.",
                "sample_answer_reading_az": "Esme bozorgtərin fərzəde Əhməd, Fateme əst.",
                "sample_answer_az": "Əhmədin ən böyük övladının adı Fatimədir.",
            },
            {
                "question_fa": "سالن پذیرایی آن‌ها در کدام طبقه است؟",
                "reading_az": "Salone pəziraei-ye anha dər kodam təbəqe əst?",
                "az": "Onların qonaq otağı hansı mərtəbədədir?",
                "sample_answer_fa": "سالن پذیرایی آن‌ها در طبقه‌ی دوم است.",
                "sample_answer_reading_az": "Salone pəziraei-ye anha dər təbəqe-ye dovvom əst.",
                "sample_answer_az": "Onların qonaq otağı ikinci mərtəbədədir.",
            },
            {
                "question_fa": "فاطمه در اتاق مطالعه چه‌کار می‌کند؟",
                "reading_az": "Fateme dər otağe motaleə çekar mikonəd?",
                "az": "Fatimə iş otağında nə edir?",
                "sample_answer_fa": "فاطمه در اتاق مطالعه درس می‌خواند و تکلیف می‌نویسد.",
                "sample_answer_reading_az": "Fateme dər otağe motaleə dərs mixanəd və təklif minevisəd.",
                "sample_answer_az": "Fatimə iş otağında dərs oxuyur və tapşırıq yazır.",
            },
            {
                "question_fa": "مبل و قفسه‌های کتاب کجاست؟",
                "reading_az": "Mobl və qafasehaye ketab kocast?",
                "az": "Divan və kitab rəfləri haradadır?",
                "sample_answer_fa": "مبل در سالن پذیرایی و قفسه‌های کتاب در اتاق مطالعه است.",
                "sample_answer_reading_az": "Mobl dər salone pəziraei və qafasehaye ketab dər otağe motaleə əst.",
                "sample_answer_az": "Divan qonaq otağında, kitab rəfləri isə iş otağındadır.",
            },
        ],
    },
}


class Command(BaseCommand):
    help = "Zəban Dərslik mobil tətbiqindəki statik dərs məzmununu (Dart) verilənlər bazasına köçürür."

    def add_arguments(self, parser):
        parser.add_argument(
            "--assets-dir",
            default=str(DEFAULT_ASSETS_DIR),
            help="zeban_derslik_mobile layihəsinin kök qovluğu (assets/images/... buradan oxunur).",
        )

    def handle(self, *args, **options):
        assets_dir = Path(options["assets_dir"])
        if not assets_dir.exists():
            raise CommandError(f"Mobil layihə qovluğu tapılmadı: {assets_dir}")

        with transaction.atomic():
            self._seed_full_lesson(LESSON_1, assets_dir)
            self._seed_full_lesson(LESSON_2, assets_dir)
            seeded_numbers = {1, 2}
            for lesson_data in EXTRA_LESSONS:
                self._seed_full_lesson(lesson_data, assets_dir)
                seeded_numbers.add(lesson_data["number"])
            self._seed_placeholders(seeded_numbers)

        try:
            self.stdout.write(self.style.SUCCESS("Dersler ugurla kecirildi."))
        except Exception:
            pass

    def _attach_image(self, field_owner, field_name, rel_path, assets_dir):
        if not rel_path:
            return
        abs_path = assets_dir / rel_path
        if not abs_path.exists():
            self.stdout.write(self.style.WARNING(f"Şəkil tapılmadı, keçildi: {abs_path}"))
            return

        # Sabit fayl adı: eyni şəkil artıq media-da varsa, yenidən yükləmə —
        # sadəcə sahəni mövcud fayla yönəlt (hash-suffiksli dublikatların qarşısı).
        target = lesson_image_path(field_owner, abs_path.name)
        if default_storage.exists(target):
            if default_storage.size(target) == abs_path.stat().st_size:
                setattr(field_owner, field_name, target)
                return
            # Məzmun dəyişibsə köhnəni silirik ki, ad sabit qalsın.
            default_storage.delete(target)

        with abs_path.open("rb") as fh:
            getattr(field_owner, field_name).save(abs_path.name, File(fh), save=False)

    def _grade2(self):
        # Bütün mövcud dərslik kontenti 2-ci sinifə aiddir.
        grade, _ = Grade.objects.get_or_create(
            number=2, defaults={"title": "2-ci sinif", "available": True}
        )
        return grade

    def _seed_full_lesson(self, data, assets_dir):
        lesson, _ = Lesson.objects.update_or_create(
            number=data["number"],
            defaults={
                "grade": self._grade2(),
                "title_fa": data["title_fa"],
                "title_az": data["title_az"],
                "available": data["available"],
                "order": data["number"],
            },
        )

        # Nümunə cümlələrin admin paneldən yazılmış "reading_az" dəyərləri
        # (fa mətninə görə) yadda saxlanır ki, aşağıdakı silmə-yenidənyaratma
        # onları itirməsin — bu sahə seed fayllarında yox, yalnız DB-də yaşayır.
        preserved_example_readings = dict(
            ExampleSentence.objects.filter(grammar_note__lesson=lesson)
            .exclude(reading_az="")
            .values_list("fa", "reading_az")
        )

        # Qrammatika: tətbiqdən redaktə/əlavə olunmuş qeyd/hallanma sətri/nümunə
        # cümlə (edited_via_app=True) başlığa/əvəzliyə/fars mətninə görə anbara
        # götürülür ki, aşağıdakı silmə-yenidənyaratma onları itirməsin (vocab-
        # dakı eyni prinsip). Yeni qrammatika MÖVZUSU tətbiqdən yaradıla bilmir
        # (yalnız mövcud mövzunun daxili siyahılarına əlavə/redaktə) — ona görə
        # GrammarNote özü üçün "faylda olmayan əlavə mövzu" halı yoxdur.
        existing_notes_by_title = {
            n.title_fa: n for n in lesson.grammar_notes.all().prefetch_related("conjugations", "examples")
        }

        # Çalışmalar: tətbiqdən redaktə olunmuş konteynerlər (instruction_az/
        # title_fa/example_* və s.) VƏ elementlər (items) silmədən əvvəl anbara
        # götürülür. Konteynerlər üçün təbii mətn açarı etibarlı olmadığından
        # (instruction_az uzun/təkrarlana bilər), öz NÖVÜNÜN daxilindəki SIRAYA
        # görə uyğunlaşdırılır — eyni növün çalışmalarını öz aralarında yenidən
        # sıralamaq nadir hal olduğundan bu kifayət qədər etibarlıdır. Elementlər
        # isə (vocab/qrammatika kimi) öz mətn açarlarına görə ayrıca qorunur.
        existing_fill_blank = list(lesson.fill_blank_exercises.all().prefetch_related("items"))
        existing_practice_reveal = list(lesson.practice_reveal_exercises.all().prefetch_related("items"))
        existing_picture_sentences = list(lesson.picture_sentence_exercises.all().prefetch_related("items__sentences"))
        existing_answer_question = list(lesson.answer_question_exercises.all().prefetch_related("items"))
        existing_reading_text = (
            ReadingText.objects.filter(lesson=lesson)
            .prefetch_related("footnotes", "comprehension_questions")
            .first()
        )

        # İdempotent: yenidən yaratmadan əvvəl mövcud alt-elementləri sil.
        # (Lüğət/vocabulary AŞAĞIDA, saxlanması lazım olan tətbiq-redaktəli
        # sözlərin anbara götürülməsindən SONRA silinir — bax aşağı şərh.)
        lesson.grammar_notes.all().delete()
        lesson.fill_blank_exercises.all().delete()
        lesson.practice_reveal_exercises.all().delete()
        lesson.picture_sentence_exercises.all().delete()
        lesson.answer_question_exercises.all().delete()
        ReadingText.objects.filter(lesson=lesson).delete()
        # SentencePractice itself is not wiped here: "Məsdərlər" (Infinitive/
        # ConjugatedForm) content lives only in the admin panel, never in this
        # file, so re-seeding must not delete it. Only the listen/answer
        # sentence lists below (which do live in this file) get replaced.

        # Mobil tətbiqin Söz ehtiyatı redaktə ekranından dəyişdirilmiş/əlavə
        # edilmiş sözlər (edited_via_app=True) bu fayldakı məzmunla üstələnmir
        # — silmədən əvvəl fa mətninə görə anbara götürülür, sonra ya öz
        # yerində (mövcud sözü redaktə edibsə) ya da faylda heç olmayan
        # tamam yeni söz kimi sonda bərpa olunur (Infinitive/ConjugatedForm-
        # dakı admin-only prinsipin yüngül versiyası, bax [[zeban-derslik-projects]]).
        existing_by_fa = {w.fa: w for w in lesson.vocabulary.all()}
        seed_fa_set = {item["fa"] for item in data["vocabulary"]}
        extra_words = [w for fa, w in existing_by_fa.items() if fa not in seed_fa_set and w.edited_via_app]

        lesson.vocabulary.all().delete()

        for order, item in enumerate(data["vocabulary"]):
            prior = existing_by_fa.get(item["fa"])
            use_prior = prior is not None and prior.edited_via_app
            word = VocabWord(
                lesson=lesson,
                fa=item["fa"],
                reading_az=(prior.reading_az if use_prior else item.get("reading", "")),
                az=(prior.az if use_prior else item["az"]),
                order=order,
                edited_via_app=use_prior,
            )
            if use_prior and prior.image:
                word.image = prior.image.name
            else:
                self._attach_image(word, "image", item.get("image"), assets_dir)
            word.save()

        next_order = len(data["vocabulary"])
        for extra in extra_words:
            extra.pk = None
            extra.lesson = lesson
            extra.order = next_order
            extra.save()
            next_order += 1

        for order, note_data in enumerate(data["grammar_notes"]):
            prior_note = existing_notes_by_title.get(note_data["title_fa"])
            note_prior_ok = prior_note is not None and prior_note.edited_via_app
            note = GrammarNote.objects.create(
                lesson=lesson,
                title_az=note_data["title_az"],
                title_fa=note_data["title_fa"],
                order=order,
                note_fa=(prior_note.note_fa if note_prior_ok else note_data.get("note_fa", "")),
                note_reading_az=(
                    prior_note.note_reading_az if note_prior_ok else note_data.get("note_reading_az", "")
                ),
                note_az=(prior_note.note_az if note_prior_ok else note_data.get("note_az", "")),
                edited_via_app=note_prior_ok,
            )

            prior_conjugations = {r.pronoun_fa: r for r in prior_note.conjugations.all()} if prior_note else {}
            seed_pronouns = {row["pronoun_fa"] for row in note_data["conjugations"]}
            for c_order, row in enumerate(note_data["conjugations"]):
                prior_row = prior_conjugations.get(row["pronoun_fa"])
                row_prior_ok = prior_row is not None and prior_row.edited_via_app
                ConjugationRow.objects.create(
                    grammar_note=note,
                    pronoun_fa=row["pronoun_fa"],
                    form_fa=(prior_row.form_fa if row_prior_ok else row["form_fa"]),
                    order=c_order,
                    edited_via_app=row_prior_ok,
                )
            next_row_order = len(note_data["conjugations"])
            for pronoun, r in prior_conjugations.items():
                if pronoun not in seed_pronouns and r.edited_via_app:
                    r.pk = None
                    r.grammar_note = note
                    r.order = next_row_order
                    r.save()
                    next_row_order += 1

            prior_examples = {e.fa: e for e in prior_note.examples.all()} if prior_note else {}
            seed_example_fas = {ex["fa"] for ex in note_data["examples"]}
            for e_order, ex in enumerate(note_data["examples"]):
                prior_ex = prior_examples.get(ex["fa"])
                ex_prior_ok = prior_ex is not None and prior_ex.edited_via_app
                ExampleSentence.objects.create(
                    grammar_note=note,
                    order=e_order,
                    fa=ex["fa"],
                    az=(prior_ex.az if ex_prior_ok else ex["az"]),
                    reading_az=(
                        prior_ex.reading_az
                        if ex_prior_ok
                        else ex.get("reading_az") or preserved_example_readings.get(ex["fa"], "")
                    ),
                    edited_via_app=ex_prior_ok,
                )
            next_ex_order = len(note_data["examples"])
            for fa, e in prior_examples.items():
                if fa not in seed_example_fas and e.edited_via_app:
                    e.pk = None
                    e.grammar_note = note
                    e.order = next_ex_order
                    e.save()
                    next_ex_order += 1
            for d_order, drill_data in enumerate(note_data.get("drills", [])):
                drill = PracticeRevealExercise(
                    grammar_note=note,
                    title_fa=drill_data.get("title_fa", ""),
                    instruction_az=drill_data["instruction_az"],
                    example_fa=drill_data.get("example_fa", ""),
                    example_prompt_fa=drill_data.get("example_prompt_fa", ""),
                    example_answer_fa=drill_data.get("example_answer_fa", ""),
                    example_reading_az=drill_data.get("example_reading_az", ""),
                    example_az=drill_data.get("example_az", ""),
                    order=d_order,
                )
                self._attach_image(drill, "example_image_have", drill_data.get("example_image_have"), assets_dir)
                self._attach_image(drill, "example_image_not_have", drill_data.get("example_image_not_have"), assets_dir)
                drill.save()
                for i_order, raw_item in enumerate(drill_data["items"]):
                    item = dict(raw_item)
                    image_have = item.pop("image_have", None)
                    image_not_have = item.pop("image_not_have", None)
                    drill_item = PracticeRevealItem(exercise=drill, order=i_order, **item)
                    self._attach_image(drill_item, "image_have", image_have, assets_dir)
                    self._attach_image(drill_item, "image_not_have", image_not_have, assets_dir)
                    drill_item.save()

        exercise_order = {
            "fill_blank": 0, "practice_reveal": 0,
            "picture_sentences": 0, "answer_question": 0,
        }
        for overall_order, ex_data in enumerate(data["exercises"]):
            kind = ex_data["kind"]
            position = exercise_order[kind]
            exercise_order[kind] += 1

            if kind == "fill_blank":
                prior = existing_fill_blank[position] if position < len(existing_fill_blank) else None
                prior_ok = prior is not None and prior.edited_via_app
                exercise = FillBlankExercise.objects.create(
                    lesson=lesson,
                    instruction_az=(prior.instruction_az if prior_ok else ex_data["instruction_az"]),
                    word_bank=(prior.word_bank if prior_ok else ex_data["word_bank"]),
                    order=overall_order,
                    edited_via_app=prior_ok,
                )
                prior_items = {i.fa_with_blank: i for i in prior.items.all()} if prior else {}
                seed_blanks = {item["fa_with_blank"] for item in ex_data["items"]}
                for i_order, item in enumerate(ex_data["items"]):
                    prior_item = prior_items.get(item["fa_with_blank"])
                    item_ok = prior_item is not None and prior_item.edited_via_app
                    if item_ok:
                        FillBlankItem.objects.create(
                            exercise=exercise, order=i_order, edited_via_app=True,
                            fa_with_blank=prior_item.fa_with_blank, correct_answer=prior_item.correct_answer,
                            reading_az=prior_item.reading_az, az=prior_item.az,
                            full_reading_az=prior_item.full_reading_az,
                            full_translation_az=prior_item.full_translation_az,
                        )
                    else:
                        FillBlankItem.objects.create(exercise=exercise, order=i_order, **item)
                next_item_order = len(ex_data["items"])
                for fa_blank, i in prior_items.items():
                    if fa_blank not in seed_blanks and i.edited_via_app:
                        i.pk = None
                        i.exercise = exercise
                        i.order = next_item_order
                        i.save()
                        next_item_order += 1

            elif kind == "practice_reveal":
                prior = existing_practice_reveal[position] if position < len(existing_practice_reveal) else None
                prior_ok = prior is not None and prior.edited_via_app
                exercise = PracticeRevealExercise(
                    lesson=lesson,
                    title_fa=(prior.title_fa if prior_ok else ex_data.get("title_fa", "")),
                    instruction_az=(prior.instruction_az if prior_ok else ex_data["instruction_az"]),
                    example_fa=(prior.example_fa if prior_ok else ex_data.get("example_fa", "")),
                    example_prompt_fa=(prior.example_prompt_fa if prior_ok else ex_data.get("example_prompt_fa", "")),
                    example_answer_fa=(prior.example_answer_fa if prior_ok else ex_data.get("example_answer_fa", "")),
                    example_reading_az=(prior.example_reading_az if prior_ok else ex_data.get("example_reading_az", "")),
                    example_az=(prior.example_az if prior_ok else ex_data.get("example_az", "")),
                    order=overall_order,
                    edited_via_app=prior_ok,
                )
                if prior_ok and prior.example_image_have:
                    exercise.example_image_have = prior.example_image_have.name
                if prior_ok and prior.example_image_not_have:
                    exercise.example_image_not_have = prior.example_image_not_have.name
                exercise.save()
                prior_items = {i.prompt_fa: i for i in prior.items.all()} if prior else {}
                seed_prompts = {item["prompt_fa"] for item in ex_data["items"]}
                for i_order, item in enumerate(ex_data["items"]):
                    prior_item = prior_items.get(item["prompt_fa"])
                    item_ok = prior_item is not None and prior_item.edited_via_app
                    if item_ok:
                        PracticeRevealItem.objects.create(
                            exercise=exercise, order=i_order, edited_via_app=True,
                            prompt_fa=prior_item.prompt_fa, answer_fa=prior_item.answer_fa,
                            reading_az=prior_item.reading_az, az=prior_item.az,
                            image_have=(prior_item.image_have.name if prior_item.image_have else ""),
                            image_not_have=(prior_item.image_not_have.name if prior_item.image_not_have else ""),
                        )
                    else:
                        PracticeRevealItem.objects.create(exercise=exercise, order=i_order, **item)
                next_item_order = len(ex_data["items"])
                for prompt_fa, i in prior_items.items():
                    if prompt_fa not in seed_prompts and i.edited_via_app:
                        i.pk = None
                        i.exercise = exercise
                        i.order = next_item_order
                        i.save()
                        next_item_order += 1

            elif kind == "picture_sentences":
                prior = existing_picture_sentences[position] if position < len(existing_picture_sentences) else None
                prior_ok = prior is not None and prior.edited_via_app
                exercise = PictureSentenceExercise(
                    lesson=lesson,
                    instruction_az=(prior.instruction_az if prior_ok else ex_data["instruction_az"]),
                    title_fa=(prior.title_fa if prior_ok else ex_data.get("title_fa", "")),
                    example_fa=(prior.example_fa if prior_ok else ex_data.get("example_fa", "")),
                    example_reading_az=(prior.example_reading_az if prior_ok else ex_data.get("example_reading_az", "")),
                    example_az=(prior.example_az if prior_ok else ex_data.get("example_az", "")),
                    example_answer_fa=(prior.example_answer_fa if prior_ok else ex_data.get("example_answer_fa", "")),
                    example_answer_reading_az=(
                        prior.example_answer_reading_az if prior_ok else ex_data.get("example_answer_reading_az", "")
                    ),
                    example_answer_az=(prior.example_answer_az if prior_ok else ex_data.get("example_answer_az", "")),
                    order=overall_order,
                    edited_via_app=prior_ok,
                )
                if prior_ok and prior.example_image:
                    exercise.example_image = prior.example_image.name
                else:
                    self._attach_image(exercise, "example_image", ex_data.get("example_image"), assets_dir)
                if prior_ok and prior.example_image_have:
                    exercise.example_image_have = prior.example_image_have.name
                else:
                    self._attach_image(exercise, "example_image_have", ex_data.get("example_image_have"), assets_dir)
                if prior_ok and prior.example_image_not_have:
                    exercise.example_image_not_have = prior.example_image_not_have.name
                else:
                    self._attach_image(
                        exercise, "example_image_not_have", ex_data.get("example_image_not_have"), assets_dir
                    )
                exercise.save()

                # Elementlər öz cümlələrinin fars mətnləri (tuple) ilə tanınır —
                # şəkillər (fərqli olaraq) təbii mətn açarı daşımadığından.
                prior_items_by_lines = {
                    tuple(s.fa for s in i.sentences.all()): i for i in (prior.items.all() if prior else [])
                }
                seed_line_keys = {
                    tuple(line["fa"] for line in item_data["sentences"]) for item_data in ex_data["items"]
                }
                for i_order, item_data in enumerate(ex_data["items"]):
                    key = tuple(line["fa"] for line in item_data["sentences"])
                    prior_item = prior_items_by_lines.get(key)
                    item_ok = prior_item is not None and prior_item.edited_via_app
                    pic_item = PictureSentenceItem(exercise=exercise, order=i_order, edited_via_app=item_ok)
                    if item_ok and prior_item.image:
                        pic_item.image = prior_item.image.name
                    else:
                        self._attach_image(pic_item, "image", item_data.get("image"), assets_dir)
                    if item_ok and prior_item.image_have:
                        pic_item.image_have = prior_item.image_have.name
                    else:
                        self._attach_image(pic_item, "image_have", item_data.get("image_have"), assets_dir)
                    if item_ok and prior_item.image_not_have:
                        pic_item.image_not_have = prior_item.image_not_have.name
                    else:
                        self._attach_image(pic_item, "image_not_have", item_data.get("image_not_have"), assets_dir)
                    pic_item.save()
                    lines = (
                        [{"fa": s.fa, "reading_az": s.reading_az, "az": s.az} for s in prior_item.sentences.all()]
                        if item_ok else item_data["sentences"]
                    )
                    for s_order, line in enumerate(lines):
                        PictureSentenceLine.objects.create(item=pic_item, order=s_order, **line)
                next_item_order = len(ex_data["items"])
                for key, i in prior_items_by_lines.items():
                    if key not in seed_line_keys and i.edited_via_app:
                        old_lines = list(i.sentences.all())
                        i.pk = None
                        i.exercise = exercise
                        i.order = next_item_order
                        i.save()
                        for s_order, line in enumerate(old_lines):
                            PictureSentenceLine.objects.create(
                                item=i, order=s_order, fa=line.fa, reading_az=line.reading_az, az=line.az
                            )
                        next_item_order += 1

            elif kind == "answer_question":
                prior = existing_answer_question[position] if position < len(existing_answer_question) else None
                prior_ok = prior is not None and prior.edited_via_app
                exercise = AnswerQuestionExercise.objects.create(
                    lesson=lesson,
                    title_fa=(prior.title_fa if prior_ok else ex_data.get("title_fa", "")),
                    example_fa=(prior.example_fa if prior_ok else ex_data.get("example_fa", "")),
                    example_reading_az=(prior.example_reading_az if prior_ok else ex_data.get("example_reading_az", "")),
                    example_az=(prior.example_az if prior_ok else ex_data.get("example_az", "")),
                    instruction_az=(prior.instruction_az if prior_ok else ex_data["instruction_az"]),
                    note_fa=(prior.note_fa if prior_ok else ex_data.get("note_fa", "")),
                    note_reading_az=(prior.note_reading_az if prior_ok else ex_data.get("note_reading_az", "")),
                    note_az=(prior.note_az if prior_ok else ex_data.get("note_az", "")),
                    order=overall_order,
                    edited_via_app=prior_ok,
                )
                prior_items = {i.fa: i for i in prior.items.all()} if prior else {}
                seed_fas = {item["fa"] for item in ex_data["items"]}
                for i_order, item in enumerate(ex_data["items"]):
                    prior_item = prior_items.get(item["fa"])
                    item_ok = prior_item is not None and prior_item.edited_via_app
                    if item_ok:
                        AnswerQuestionExerciseItem.objects.create(
                            exercise=exercise, order=i_order, edited_via_app=True,
                            fa=prior_item.fa, reading_az=prior_item.reading_az, az=prior_item.az,
                            sample_answer_fa=prior_item.sample_answer_fa,
                            sample_answer_reading_az=prior_item.sample_answer_reading_az,
                            sample_answer_az=prior_item.sample_answer_az,
                        )
                    else:
                        AnswerQuestionExerciseItem.objects.create(exercise=exercise, order=i_order, **item)
                next_item_order = len(ex_data["items"])
                for fa, i in prior_items.items():
                    if fa not in seed_fas and i.edited_via_app:
                        i.pk = None
                        i.exercise = exercise
                        i.order = next_item_order
                        i.save()
                        next_item_order += 1

        if "sentence_practice" in data:
            practice_data = data["sentence_practice"]
            # get_or_create (not create): "Məsdərlər" (Infinitive/ConjugatedForm)
            # is admin-only content and must survive re-seeding untouched.
            practice, _ = SentencePractice.objects.get_or_create(lesson=lesson)
            if not practice.answer_note_edited_via_app:
                practice.answer_note_fa = practice_data.get("answer_note_fa", "")
                practice.answer_note_reading_az = practice_data.get("answer_note_reading_az", "")
                practice.answer_note_az = practice_data.get("answer_note_az", "")
            practice.save()

            # Tətbiqdən redaktə/əlavə olunmuş cümlələr (edited_via_app=True) fa
            # mətninə görə qorunur — vocabulary-dəki eyni prinsip (bax yuxarı şərh).
            # "Dinləyin və oxuyun" indi Çalışma-lara bölünür (ListenReadExercise);
            # köhnə/yeni çalışmalar sırasına (position) görə uyğunlaşdırılır — eyni
            # prinsip "answer_question" kind-inin exercises siyahısında olduğu kimi.
            existing_listen_exercises = list(practice.listen_exercises.all().prefetch_related("items"))

            prior_answer = {s.fa: s for s in practice.answer_items.all()}
            seed_answer_fas = {item["fa"] for item in practice_data.get("answer_items", [])}
            extra_answer = [s for fa, s in prior_answer.items() if fa not in seed_answer_fas and s.edited_via_app]

            practice.listen_exercises.all().delete()
            practice.answer_items.all().delete()

            for ex_position, ex_data in enumerate(practice_data.get("listen_exercises", [])):
                prior_exercise = (
                    existing_listen_exercises[ex_position]
                    if ex_position < len(existing_listen_exercises) else None
                )
                exercise = ListenReadExercise.objects.create(practice=practice, order=ex_position + 1)
                prior_items = {s.fa: s for s in prior_exercise.items.all()} if prior_exercise else {}
                seed_item_fas = {item["fa"] for item in ex_data["items"]}
                for l_order, item in enumerate(ex_data["items"]):
                    prior = prior_items.get(item["fa"])
                    use_prior = prior is not None and prior.edited_via_app
                    ListenReadSentence.objects.create(
                        exercise=exercise,
                        fa=item["fa"],
                        reading_az=(prior.reading_az if use_prior else item.get("reading_az", "")),
                        az=(prior.az if use_prior else item["az"]),
                        order=l_order,
                        edited_via_app=use_prior,
                    )
                next_item_order = len(ex_data["items"])
                for fa, s in prior_items.items():
                    if fa not in seed_item_fas and s.edited_via_app:
                        s.pk = None
                        s.exercise = exercise
                        s.order = next_item_order
                        s.save()
                        next_item_order += 1

            for a_order, item in enumerate(practice_data.get("answer_items", [])):
                prior = prior_answer.get(item["fa"])
                use_prior = prior is not None and prior.edited_via_app
                AnswerQuestionSentence.objects.create(
                    practice=practice,
                    fa=item["fa"],
                    reading_az=(prior.reading_az if use_prior else item.get("reading_az", "")),
                    az=(prior.az if use_prior else item["az"]),
                    sample_answer_fa=(prior.sample_answer_fa if use_prior else item.get("sample_answer_fa", "")),
                    sample_answer_reading_az=(
                        prior.sample_answer_reading_az if use_prior else item.get("sample_answer_reading_az", "")
                    ),
                    sample_answer_az=(prior.sample_answer_az if use_prior else item.get("sample_answer_az", "")),
                    order=a_order,
                    edited_via_app=use_prior,
                )
            next_answer_order = len(practice_data.get("answer_items", []))
            for extra in extra_answer:
                extra.pk = None
                extra.practice = practice
                extra.order = next_answer_order
                extra.save()
                next_answer_order += 1

        reading_data = data["reading_text"]
        reading_prior_ok = existing_reading_text is not None and existing_reading_text.edited_via_app
        reading = ReadingText(
            lesson=lesson,
            title_fa=(existing_reading_text.title_fa if reading_prior_ok else reading_data["title_fa"]),
            title_az=(existing_reading_text.title_az if reading_prior_ok else reading_data["title_az"]),
            paragraphs_fa=(existing_reading_text.paragraphs_fa if reading_prior_ok else reading_data["paragraphs_fa"]),
            full_translation_az=(
                existing_reading_text.full_translation_az if reading_prior_ok else reading_data["full_translation_az"]
            ),
            sentences=(existing_reading_text.sentences if reading_prior_ok else reading_data.get("sentences", [])),
            edited_via_app=reading_prior_ok,
        )
        if reading_prior_ok and existing_reading_text.image:
            reading.image = existing_reading_text.image.name
        else:
            self._attach_image(reading, "image", reading_data.get("image"), assets_dir)
        reading.save()

        prior_footnotes = (
            {f.fa: f for f in existing_reading_text.footnotes.all()} if existing_reading_text else {}
        )
        seed_footnote_fas = {footnote["fa"] for footnote in reading_data["footnotes"]}
        for f_order, footnote in enumerate(reading_data["footnotes"]):
            prior_footnote = prior_footnotes.get(footnote["fa"])
            footnote_ok = prior_footnote is not None and prior_footnote.edited_via_app
            if footnote_ok:
                ReadingFootnote.objects.create(
                    reading_text=reading, order=f_order, edited_via_app=True,
                    fa=prior_footnote.fa, az=prior_footnote.az,
                )
            else:
                ReadingFootnote.objects.create(reading_text=reading, order=f_order, **footnote)
        next_footnote_order = len(reading_data["footnotes"])
        for fa, f in prior_footnotes.items():
            if fa not in seed_footnote_fas and f.edited_via_app:
                f.pk = None
                f.reading_text = reading
                f.order = next_footnote_order
                f.save()
                next_footnote_order += 1

        prior_questions = (
            {q.question_fa: q for q in existing_reading_text.comprehension_questions.all()}
            if existing_reading_text else {}
        )
        seed_question_fas = {q["question_fa"] for q in reading_data.get("comprehension_questions", [])}
        for q_order, question in enumerate(reading_data.get("comprehension_questions", [])):
            prior_question = prior_questions.get(question["question_fa"])
            question_ok = prior_question is not None and prior_question.edited_via_app
            if question_ok:
                ReadingComprehensionQuestion.objects.create(
                    reading_text=reading, order=q_order, edited_via_app=True,
                    question_fa=prior_question.question_fa, reading_az=prior_question.reading_az,
                    az=prior_question.az, sample_answer_fa=prior_question.sample_answer_fa,
                    sample_answer_reading_az=prior_question.sample_answer_reading_az,
                    sample_answer_az=prior_question.sample_answer_az,
                )
            else:
                ReadingComprehensionQuestion.objects.create(reading_text=reading, order=q_order, **question)
        next_question_order = len(reading_data.get("comprehension_questions", []))
        for question_fa, q in prior_questions.items():
            if question_fa not in seed_question_fas and q.edited_via_app:
                q.pk = None
                q.reading_text = reading
                q.order = next_question_order
                q.save()
                next_question_order += 1

        try:
            self.stdout.write(self.style.SUCCESS(f"Ders {data['number']} ({data['title_az']}) yuklendi."))
        except Exception:
            pass

    def _seed_placeholders(self, seeded_numbers):
        created = 0
        for offset, (title_fa, title_az) in enumerate(UPCOMING_TITLES):
            number = offset + 3
            if number in seeded_numbers:
                continue
            Lesson.objects.update_or_create(
                number=number,
                defaults={
                    "grade": self._grade2(),
                    "title_fa": title_fa,
                    "title_az": title_az,
                    "available": False,
                    "order": number,
                },
            )
        try:
            self.stdout.write(self.style.SUCCESS(f"{created} kilidli ders yaradildi."))
        except Exception:
            pass
