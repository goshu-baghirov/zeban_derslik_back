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
    AnswerQuestionSentence,
    ConjugationRow,
    ExampleSentence,
    FillBlankExercise,
    FillBlankItem,
    Grade,
    GrammarNote,
    Lesson,
    ListenReadSentence,
    MultipleChoiceExercise,
    MultipleChoiceItem,
    PracticeRevealExercise,
    PracticeRevealItem,
    ReadingComprehensionQuestion,
    ReadingFootnote,
    ReadingText,
    SentencePractice,
    TrueFalseImageExercise,
    TrueFalseImageItem,
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
            "kind": "true_false_image",
            "instruction_az": "Şəklə baxın: cümlə doğrudurmu?",
            "items": [
                {"image": "assets/images/lessons/lesson_01/khodkar.png", "statement_fa": "این خودکار است.", "statement_az": "Bu tükənməz qələmdir.", "is_true": True},
                {"image": "assets/images/lessons/lesson_01/medadtarash.png", "statement_fa": "این پاک‌کن است.", "statement_az": "Bu pozandır.", "is_true": False},
                {"image": "assets/images/lessons/lesson_01/majik.png", "statement_fa": "این ماژیک است.", "statement_az": "Bu markerdir.", "is_true": True},
                {"image": "assets/images/lessons/lesson_01/jamedadi.png", "statement_fa": "این پوشه است.", "statement_az": "Bu qovluqdur.", "is_true": False},
                {"image": "assets/images/lessons/lesson_01/taqvim.png", "statement_fa": "این تقویم است.", "statement_az": "Bu təqvimdir.", "is_true": True},
                {"image": "assets/images/lessons/lesson_01/pushe.png", "statement_fa": "این چسب است.", "statement_az": "Bu yapışqandır.", "is_true": False},
            ],
        },
        {
            "kind": "multiple_choice",
            "instruction_az": '"در ایران" mətninə görə düzgün cavabı seçin.',
            "items": [
                {"question_fa": "اسم خواهر حسین چیست؟", "options": ["فاطمه", "زینب", "مریم"], "correct_index": 0},
                {"question_fa": "پدر حسین چه‌کاره است؟", "options": ["معلّم است", "پزشک است", "استاد دانشگاه است"], "correct_index": 1},
                {"question_fa": "مادر حسین چه‌کاره است؟", "options": ["پرستار است", "پزشک است", "استاد دانشگاه است"], "correct_index": 2},
                {"question_fa": "حسین و فاطمه اهل کجا هستند؟", "options": ["ایران", "لبنان", "عراق"], "correct_index": 1},
                {"question_fa": "خواهر حسین کدام کتاب را می‌خواند؟", "options": ["کتاب اوّل", "کتاب دوم", "کتاب سوم"], "correct_index": 0},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": "Suallara öz cavabınızı düşünün, sonra nümunə cavabı yoxlayın.",
            "items": [
                {
                    "prompt_fa": "اسم استاد شما چیست؟",
                    "answer_fa": "استاد من، آقای احمدی است.",
                    "reading_az": "Ostade mən, aqaye Əhmədi əst.",
                    "az": "Mənim müəllimim cənab Əhmədidir.",
                },
                {
                    "prompt_fa": "شما تابلو را پاک نمی‌کنید؟",
                    "answer_fa": "چرا، من تابلو را پاک می‌کنم.",
                    "reading_az": "Çera, mən təblo ra pak mikonəm.",
                    "az": "Xeyr (əksinə), mən lövhəni silirəm.",
                },
                {
                    "prompt_fa": "آیا شما کتاب دوم را می‌خوانید؟",
                    "answer_fa": "بله، من کتاب دوم را می‌خوانم.",
                    "reading_az": "Bəle, mən ketabe dovvom ra mixanəm.",
                    "az": "Bəli, mən ikinci kitabı oxuyuram.",
                },
                {
                    "prompt_fa": "آیا استاد شما تابلو نمی‌نویسد؟",
                    "answer_fa": "چرا، استاد من تابلو می‌نویسد.",
                    "reading_az": "Çera, ostade mən təblo minevisəd.",
                    "az": "Xeyr (əksinə), mənim müəllimim lövhəyə yazır.",
                },
                {
                    "prompt_fa": "شما (تو) در کدام مدرسه درس می‌خوانی؟",
                    "answer_fa": "من در مدرسه‌ی المهدی درس می‌خوانم.",
                    "reading_az": "Mən dər mædrese-ye Əl-Mehdi dars mixanam.",
                    "az": "Mən Əl-Mehdi məktəbində oxuyuram.",
                },
            ],
        },
    ],
    "sentence_practice": {
        "listen_items": [
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
            },
            {
                "question_fa": "آیا پدر حسین، معلّم است؟",
                "reading_az": "Aya pedəre Hoseyn, moəllem əst?",
                "az": "Hüseynin atası müəllimdirmi?",
            },
            {
                "question_fa": "حسین و فاطمه، اهل کجا هستند؟",
                "reading_az": "Hoseyn və Fateme, əhle koca həstənd?",
                "az": "Hüseyn və Fatimə haralıdırlar?",
            },
            {
                "question_fa": "حسین و فاطمه کجا درس می‌خوانند؟",
                "reading_az": "Hoseyn və Fateme koca dərs mixanənd?",
                "az": "Hüseyn və Fatimə harada oxuyurlar?",
            },
            {
                "question_fa": "فاطمه و حسین، الآن کدام کتاب را می‌خوانند؟",
                "reading_az": "Fateme və Hoseyn, əl-an kodam ketab ra mixanənd?",
                "az": "Fatimə və Hüseyn indi hansı kitabı oxuyurlar?",
            },
            {
                "question_fa": "آیا در جامدادی حسین، مدادتراش و پاک‌کن وجود ندارد؟",
                "reading_az": "Aya dər camedadiye Hoseyn, medadtəraş və pakkon vocud nədarəd?",
                "az": "Hüseynin qələmqabında qələmyonan və pozan yoxdurmu?",
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
                    "az": "Bu qaz plitəsidir, yoxsa paltaryuyandır? Bu paltaryuyandır.",
                },
                {
                    "fa": "این لباس‌شویی، بزرگ است یا کوچک؟ این لباس‌شویی، بزرگ است.",
                    "az": "Bu paltaryuyan böyükdür, yoxsa kiçik? Bu paltaryuyan böyükdür.",
                },
                {"fa": "محمّد پزشک است یا پرستار است؟ محمّد، پزشک است.", "az": "Məhəmməd həkimdir, yoxsa tibb bacısı? Məhəmməd həkimdir."},
                {
                    "fa": "شما در حمّام دوش می‌گیرید یا در آشپزخانه؟ من در حمّام دوش می‌گیرم.",
                    "az": "Siz hamamda duş alırsınız, yoxsa mətbəxdə? Mən hamamda duş alıram.",
                },
            ],
        },
        {
            "title_az": 'Sual cümləsi "چه‌کار می‌کند؟" (O nə edir?)',
            "title_fa": "جمله‌ی پرسشی «چه‌کار می‌کند؟»",
            "conjugations": [],
            "examples": [
                {"fa": "این مرد چه‌کار می‌کند؟ این مرد روزنامه می‌خواند.", "az": "Bu kişi nə edir? Bu kişi qəzet oxuyur."},
                {"fa": "آن خانم چه‌کار می‌کند؟ آن خانم غذا می‌پزد.", "az": "O xanım nə edir? O xanım yemək bişirir."},
                {"fa": "فاطمه چه‌کار می‌کند؟ فاطمه نامه می‌نویسد.", "az": "Fatimə nə edir? Fatimə məktub yazır."},
                {"fa": "علی چه‌کار می‌کند؟ علی نقّاشی می‌کشد.", "az": "Əli nə edir? Əli rəsm çəkir."},
            ],
        },
        {
            "title_az": "Hörmət forması (تو → شما, او → ایشان)",
            "title_fa": "جمله‌ی محترمانه",
            "conjugations": [
                {"pronoun_fa": "تو استادی.", "form_fa": "شما استادید."},
                {"pronoun_fa": "او استاد است.", "form_fa": "ایشان استادند."},
            ],
            "examples": [
                {"fa": "تو نگهبانی. → شما نگهبانید.", "az": "Sən keşikçisən. → Siz keşikçisiniz."},
                {
                    "fa": "او کتاب را روی میز می‌گذارد. → ایشان کتاب را روی میز می‌گذارند.",
                    "az": "O, kitabı masanın üstünə qoyur. → Onlar (hörmətlə) kitabı masanın üstünə qoyurlar.",
                },
                {
                    "fa": "آیا او محمّدمهدی است؟ → آیا ایشان محمّدمهدی هستند؟",
                    "az": "O, Məhəmmədmehdidirmi? → O zat (hörmətlə) Məhəmmədmehdidirmi?",
                },
            ],
        },
    ],
    "exercises": [
        {
            "kind": "fill_blank",
            "instruction_az": "Boşluğu söz bankından uyğun sözlə doldurun.",
            "word_bank": [
                "دوش می‌گیرند", "پاک می‌کنم", "وجود دارد", "غذا می‌پزد",
                "درس می‌خوانید", "می‌کشیم", "می‌گذارد", "می‌شوید",
            ],
            "items": [
                {"fa_with_blank": "آن‌ها در حمّام ___ .", "correct_answer": "دوش می‌گیرند"},
                {"fa_with_blank": "من هر روز تابلو را ___ .", "correct_answer": "پاک می‌کنم"},
                {"fa_with_blank": "در اتاق‌خوابِ من، تخت ___ .", "correct_answer": "وجود دارد"},
                {"fa_with_blank": "مادرم هر روز در آشپزخانه ___ .", "correct_answer": "غذا می‌پزد"},
                {"fa_with_blank": "شما هر روز در اتاقِ مطالعه ___ .", "correct_answer": "درس می‌خوانید"},
                {"fa_with_blank": "من و حسین در کلاس، نقّاشی ___ .", "correct_answer": "می‌کشیم"},
                {"fa_with_blank": "نرگس لباس‌های کثیف را در لباس‌شویی ___ .", "correct_answer": "می‌گذارد"},
                {"fa_with_blank": "خدیجه لباس‌های کثیف را با لباس‌شویی ___ .", "correct_answer": "می‌شوید"},
            ],
        },
        {
            "kind": "true_false_image",
            "instruction_az": "Şəklə baxın: cümlə doğrudurmu?",
            "items": [
                {"image": "assets/images/lessons/lesson_02/ashpazkhane.png", "statement_fa": "این آشپزخانه است.", "statement_az": "Bu mətbəxdir.", "is_true": True},
                {"image": "assets/images/lessons/lesson_02/hammam.png", "statement_fa": "این توالت است.", "statement_az": "Bu tualetdir.", "is_true": False},
                {"image": "assets/images/lessons/lesson_02/balesh.png", "statement_fa": "این بالش است.", "statement_az": "Bu yastıqdır.", "is_true": True},
                {"image": "assets/images/lessons/lesson_02/kooler.png", "statement_fa": "این پرده است.", "statement_az": "Bu pərdədir.", "is_true": False},
                {"image": "assets/images/lessons/lesson_02/ketri.png", "statement_fa": "این کتری است.", "statement_az": "Bu çaydandır.", "is_true": True},
                {"image": "assets/images/lessons/lesson_02/toshak.png", "statement_fa": "این پتو است.", "statement_az": "Bu adyaldır.", "is_true": False},
            ],
        },
        {
            "kind": "multiple_choice",
            "instruction_az": '"خانه‌ی برادرم" mətninə görə düzgün cavabı seçin.',
            "items": [
                {"question_fa": "پایتخت ایران کجاست؟", "options": ["تبریز", "اصفهان", "تهران"], "correct_index": 2},
                {"question_fa": "خانه‌ی احمد چند طبقه است؟", "options": ["یک طبقه", "دو طبقه", "سه طبقه"], "correct_index": 1},
                {"question_fa": "احمد چند فرزند دارد؟", "options": ["دو دختر و یک پسر", "یک دختر و دو پسر", "سه پسر"], "correct_index": 0},
                {"question_fa": "سالن پذیرایی و اتاق مطالعه‌ی آن‌ها در کدام طبقه است؟", "options": ["طبقه‌ی اوّل", "طبقه‌ی دوم", "پشت‌بام"], "correct_index": 1},
                {"question_fa": "اسم بزرگ‌ترین فرزند احمد چیست؟", "options": ["زینب", "فاطمه", "علی"], "correct_index": 1},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": '"یا" ilə sual qurun və cavab verin.',
            "items": [
                {"prompt_fa": "بینی برای شنیدن است یا بوییدن؟", "answer_fa": "بینی برای بوییدن است."},
                {"prompt_fa": "این خانم‌ها ظرف می‌شویند یا غذا می‌پزند؟", "answer_fa": "این خانم‌ها غذا می‌پزند."},
                {"prompt_fa": "این اجاق‌گاز است یا لباس‌شویی؟", "answer_fa": "این لباس‌شویی است."},
                {"prompt_fa": "این لباس‌شویی، بزرگ است یا کوچک؟", "answer_fa": "این لباس‌شویی، بزرگ است."},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": '"چه‌کار می‌کند؟" sualına cavab verin.',
            "items": [
                {"prompt_fa": "فاطمه چه‌کار می‌کند؟", "answer_fa": "فاطمه نامه می‌نویسد."},
                {"prompt_fa": "علی چه‌کار می‌کند؟", "answer_fa": "علی نقّاشی می‌کشد."},
                {"prompt_fa": "نرگس چه‌کار می‌کند؟", "answer_fa": "نرگس درس می‌خواند؛ او در اتاق مطالعه درس می‌خواند."},
                {"prompt_fa": "شما (تو) چه‌کار می‌کنی؟ (لباس)", "answer_fa": "من لباس می‌شویم."},
                {"prompt_fa": "شما (تو) چه‌کار می‌کنی؟ (حمّام)", "answer_fa": "من دوش می‌گیرم."},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": 'Nümunə kimi hörmət formasına çevirin: "تو پرستار هستی. → شما پرستار هستید."',
            "items": [
                {"prompt_fa": "تو نگهبان هستی.", "answer_fa": "شما نگهبان هستید."},
                {"prompt_fa": "او استاد نیست.", "answer_fa": "ایشان استاد نیستند."},
                {"prompt_fa": "او کتاب را روی میز می‌گذارد.", "answer_fa": "ایشان کتاب را روی میز می‌گذارند."},
                {"prompt_fa": "تو در رستوران، غذا می‌خوری.", "answer_fa": "شما در رستوران، غذا می‌خورید."},
                {"prompt_fa": "آیا او محمّدمهدی است؟", "answer_fa": "آیا ایشان محمّدمهدی هستند؟"},
                {"prompt_fa": "آیا تو الآن دوش می‌گیری؟", "answer_fa": "آیا شما الآن دوش می‌گیرید؟"},
            ],
        },
        {
            "kind": "practice_reveal",
            "instruction_az": '"خانه‌ی برادرم" mətninə əsasən cavab verin.',
            "items": [
                {
                    "prompt_fa": "فاطمه در اتاق مطالعه چه‌کار می‌کند؟",
                    "answer_fa": "فاطمه در اتاق مطالعه درس می‌خواند و تکلیف می‌نویسد.",
                },
                {
                    "prompt_fa": "مبل و قفسه‌های کتاب کجاست؟",
                    "answer_fa": "مبل و قفسه‌های کتاب در سالن پذیرایی و اتاق مطالعه است.",
                },
            ],
        },
    ],
    "sentence_practice": {
        "listen_items": [],
        "answer_items": [],
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

        # Idempotent: wipe existing children before recreating them.
        lesson.vocabulary.all().delete()
        lesson.grammar_notes.all().delete()
        lesson.fill_blank_exercises.all().delete()
        lesson.true_false_exercises.all().delete()
        lesson.multiple_choice_exercises.all().delete()
        lesson.practice_reveal_exercises.all().delete()
        ReadingText.objects.filter(lesson=lesson).delete()
        # SentencePractice itself is not wiped here: "Məsdərlər" (Infinitive/
        # ConjugatedForm) content lives only in the admin panel, never in this
        # file, so re-seeding must not delete it. Only the listen/answer
        # sentence lists below (which do live in this file) get replaced.

        for order, item in enumerate(data["vocabulary"]):
            word = VocabWord(
                lesson=lesson,
                fa=item["fa"],
                reading_az=item.get("reading", ""),
                az=item["az"],
                order=order,
            )
            self._attach_image(word, "image", item.get("image"), assets_dir)
            word.save()

        for order, note_data in enumerate(data["grammar_notes"]):
            note = GrammarNote.objects.create(
                lesson=lesson, title_az=note_data["title_az"], title_fa=note_data["title_fa"], order=order,
            )
            for c_order, row in enumerate(note_data["conjugations"]):
                ConjugationRow.objects.create(grammar_note=note, order=c_order, **row)
            for e_order, ex in enumerate(note_data["examples"]):
                ExampleSentence.objects.create(
                    grammar_note=note,
                    order=e_order,
                    fa=ex["fa"],
                    az=ex["az"],
                    reading_az=ex.get("reading_az") or preserved_example_readings.get(ex["fa"], ""),
                )
            for d_order, drill_data in enumerate(note_data.get("drills", [])):
                drill = PracticeRevealExercise.objects.create(
                    grammar_note=note,
                    title_fa=drill_data.get("title_fa", ""),
                    instruction_az=drill_data["instruction_az"],
                    example_fa=drill_data.get("example_fa", ""),
                    example_prompt_fa=drill_data.get("example_prompt_fa", ""),
                    example_answer_fa=drill_data.get("example_answer_fa", ""),
                    order=d_order,
                )
                for i_order, item in enumerate(drill_data["items"]):
                    PracticeRevealItem.objects.create(exercise=drill, order=i_order, **item)

        exercise_order = {"fill_blank": 0, "true_false_image": 0, "multiple_choice": 0, "practice_reveal": 0}
        for overall_order, ex_data in enumerate(data["exercises"]):
            kind = ex_data["kind"]
            order = exercise_order[kind]
            exercise_order[kind] += 1

            if kind == "fill_blank":
                exercise = FillBlankExercise.objects.create(
                    lesson=lesson, instruction_az=ex_data["instruction_az"],
                    word_bank=ex_data["word_bank"], order=overall_order,
                )
                for i_order, item in enumerate(ex_data["items"]):
                    FillBlankItem.objects.create(exercise=exercise, order=i_order, **item)

            elif kind == "true_false_image":
                exercise = TrueFalseImageExercise.objects.create(
                    lesson=lesson, instruction_az=ex_data["instruction_az"], order=overall_order,
                )
                for i_order, item in enumerate(ex_data["items"]):
                    tf_item = TrueFalseImageItem(
                        exercise=exercise,
                        statement_fa=item["statement_fa"],
                        statement_az=item["statement_az"],
                        is_true=item["is_true"],
                        order=i_order,
                    )
                    self._attach_image(tf_item, "image", item.get("image"), assets_dir)
                    tf_item.save()

            elif kind == "multiple_choice":
                exercise = MultipleChoiceExercise.objects.create(
                    lesson=lesson, instruction_az=ex_data["instruction_az"], order=overall_order,
                )
                for i_order, item in enumerate(ex_data["items"]):
                    MultipleChoiceItem.objects.create(exercise=exercise, order=i_order, **item)

            elif kind == "practice_reveal":
                exercise = PracticeRevealExercise.objects.create(
                    lesson=lesson, instruction_az=ex_data["instruction_az"], order=overall_order,
                )
                for i_order, item in enumerate(ex_data["items"]):
                    PracticeRevealItem.objects.create(exercise=exercise, order=i_order, **item)

        if "sentence_practice" in data:
            practice_data = data["sentence_practice"]
            # get_or_create (not create): "Məsdərlər" (Infinitive/ConjugatedForm)
            # is admin-only content and must survive re-seeding untouched.
            practice, _ = SentencePractice.objects.get_or_create(lesson=lesson)
            practice.listen_items.all().delete()
            practice.answer_items.all().delete()
            for l_order, item in enumerate(practice_data.get("listen_items", [])):
                ListenReadSentence.objects.create(practice=practice, order=l_order, **item)
            for a_order, item in enumerate(practice_data.get("answer_items", [])):
                AnswerQuestionSentence.objects.create(practice=practice, order=a_order, **item)

        reading_data = data["reading_text"]
        reading = ReadingText(
            lesson=lesson,
            title_fa=reading_data["title_fa"],
            title_az=reading_data["title_az"],
            paragraphs_fa=reading_data["paragraphs_fa"],
            full_translation_az=reading_data["full_translation_az"],
            sentences=reading_data.get("sentences", []),
        )
        self._attach_image(reading, "image", reading_data.get("image"), assets_dir)
        reading.save()
        for f_order, footnote in enumerate(reading_data["footnotes"]):
            ReadingFootnote.objects.create(reading_text=reading, order=f_order, **footnote)
        for q_order, question in enumerate(reading_data.get("comprehension_questions", [])):
            ReadingComprehensionQuestion.objects.create(reading_text=reading, order=q_order, **question)

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
