from django.db import models


def lesson_image_path(instance, filename):
    """Group uploaded images under media/lessons/lesson_XX/ regardless of
    which model (VocabWord, TrueFalseImageItem, ReadingText, PracticeRevealItem/
    Exercise) owns the field. PracticeRevealExercise/Item can be linked either
    directly to a Lesson or indirectly through a GrammarNote, so both paths
    are resolved here."""
    lesson = None
    if getattr(instance, "lesson_id", None):
        lesson = instance.lesson
    elif getattr(instance, "exercise_id", None):
        exercise = instance.exercise
        lesson = exercise.lesson or (exercise.grammar_note.lesson if exercise.grammar_note_id else None)
    elif getattr(instance, "grammar_note_id", None):
        lesson = instance.grammar_note.lesson

    folder = f"lesson_{lesson.number:02d}" if lesson else "misc"
    return f"lessons/{folder}/{filename}"


class Grade(models.Model):
    """School grade (1-ci sinif ... 6-cı sinif). Each grade owns its own
    content structure; for now only grade 2 has lessons."""

    number = models.PositiveIntegerField("Sinif nömrəsi", unique=True)
    title = models.CharField("Ad", max_length=100)
    available = models.BooleanField("Aktivdir", default=False)

    class Meta:
        ordering = ["number"]
        verbose_name = "Sinif"
        verbose_name_plural = "Siniflər"

    def __str__(self):
        return self.title


class Lesson(models.Model):
    grade = models.ForeignKey(
        Grade, related_name="lessons", on_delete=models.CASCADE, verbose_name="Sinif"
    )
    number = models.PositiveIntegerField(unique=True)
    title_fa = models.CharField("Başlıq (fars)", max_length=255)
    title_az = models.CharField("Başlıq (az)", max_length=255)
    available = models.BooleanField("Aktivdir", default=False)
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "number"]
        verbose_name = "Dərs"
        verbose_name_plural = "Dərslər"

    def save(self, *args, **kwargs):
        # "Number" sahəsi admin inline formasında göstərilmir; yeni dərs
        # yaradılanda nömrə avtomatik verilir (mövcud maksimum + 1).
        if self.number is None:
            max_number = Lesson.objects.aggregate(models.Max("number"))["number__max"] or 0
            self.number = max_number + 1
            if not self.order:
                self.order = self.number
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.number}. {self.title_az}"


class VocabWord(models.Model):
    lesson = models.ForeignKey(Lesson, related_name="vocabulary", on_delete=models.CASCADE)
    fa = models.CharField("Fars", max_length=255)
    reading_az = models.CharField(
        "Oxunuşu (az hərfləri ilə)", max_length=255, blank=True, default=""
    )
    az = models.CharField("Azərbaycan", max_length=255)
    image = models.ImageField("Şəkil", upload_to=lesson_image_path, blank=True, null=True)
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Söz"
        verbose_name_plural = "Lüğət"

    def __str__(self):
        return f"{self.fa} — {self.az}"


class GrammarNote(models.Model):
    lesson = models.ForeignKey(Lesson, related_name="grammar_notes", on_delete=models.CASCADE)
    title_az = models.CharField("Başlıq (az)", max_length=255)
    title_fa = models.CharField("Başlıq (fars)", max_length=255)
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Qrammatika qeydi"
        verbose_name_plural = "Qrammatika qeydləri"

    def __str__(self):
        return self.title_az


class ConjugationRow(models.Model):
    grammar_note = models.ForeignKey(GrammarNote, related_name="conjugations", on_delete=models.CASCADE)
    pronoun_fa = models.CharField("Əvəzlik (fars)", max_length=100)
    form_fa = models.CharField("Fel forması (fars)", max_length=255)
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "id"]


class ExampleSentence(models.Model):
    grammar_note = models.ForeignKey(GrammarNote, related_name="examples", on_delete=models.CASCADE)
    fa = models.CharField("Fars", max_length=500)
    reading_az = models.CharField("Üzündən oxunuş (az)", max_length=500, blank=True, default="")
    az = models.CharField("Azərbaycan", max_length=500)
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "id"]


class FillBlankExercise(models.Model):
    lesson = models.ForeignKey(Lesson, related_name="fill_blank_exercises", on_delete=models.CASCADE)
    instruction_az = models.TextField("Tapşırıq (az)")
    word_bank = models.JSONField("Söz bankı", default=list, blank=True)
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Boşluq doldurma məşğələsi"
        verbose_name_plural = "Boşluq doldurma məşğələləri"

    def __str__(self):
        return self.instruction_az[:60]


class FillBlankItem(models.Model):
    exercise = models.ForeignKey(FillBlankExercise, related_name="items", on_delete=models.CASCADE)
    fa_with_blank = models.CharField("Cümlə (boşluqlu)", max_length=500)
    correct_answer = models.CharField("Düzgün cavab", max_length=255)
    reading_az = models.CharField("Cavabın oxunuşu (az hərfləri ilə)", max_length=255, blank=True, default="")
    az = models.CharField("Cavabın tərcüməsi (az)", max_length=255, blank=True, default="")
    full_reading_az = models.CharField("Cümlənin oxunuşu (az hərfləri ilə)", max_length=500, blank=True, default="")
    full_translation_az = models.CharField("Cümlənin ümumi tərcüməsi (az)", max_length=500, blank=True, default="")
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "id"]


class TrueFalseImageExercise(models.Model):
    lesson = models.ForeignKey(Lesson, related_name="true_false_exercises", on_delete=models.CASCADE)
    instruction_az = models.TextField("Tapşırıq (az)")
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Doğru/Yanlış (şəkilli) məşğələsi"
        verbose_name_plural = "Doğru/Yanlış (şəkilli) məşğələləri"

    def __str__(self):
        return self.instruction_az[:60]


class TrueFalseImageItem(models.Model):
    exercise = models.ForeignKey(TrueFalseImageExercise, related_name="items", on_delete=models.CASCADE)
    image = models.ImageField("Şəkil", upload_to=lesson_image_path, blank=True, null=True)
    statement_fa = models.CharField("Cümlə (fars)", max_length=500)
    statement_az = models.CharField("Cümlə (az)", max_length=500)
    is_true = models.BooleanField("Doğrudur", default=True)
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "id"]


class PictureSentenceExercise(models.Model):
    """«برای هر تصویر، دو جمله بگویید» tipli məşğələ: nömrələnmiş şəkillər
    şaquli sırayla düzülür, hər birinin altında (adətən iki) nümunə cümlə
    toxunuşla açılır."""

    lesson = models.ForeignKey(Lesson, related_name="picture_sentence_exercises", on_delete=models.CASCADE)
    instruction_az = models.TextField("Tapşırıq (az)")
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Şəkilli cümlə məşğələsi"
        verbose_name_plural = "Şəkilli cümlə məşğələləri"

    def __str__(self):
        return self.instruction_az[:60]


class PictureSentenceItem(models.Model):
    exercise = models.ForeignKey(PictureSentenceExercise, related_name="items", on_delete=models.CASCADE)
    image = models.ImageField("Şəkil", upload_to=lesson_image_path, blank=True, null=True)
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "id"]


class PictureSentenceLine(models.Model):
    item = models.ForeignKey(PictureSentenceItem, related_name="sentences", on_delete=models.CASCADE)
    fa = models.CharField("Cümlə (fars)", max_length=500)
    reading_az = models.CharField("Oxunuşu (az)", max_length=500, blank=True, default="")
    az = models.CharField("Tərcümə (az)", max_length=500, blank=True, default="")
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "id"]


class MultipleChoiceExercise(models.Model):
    lesson = models.ForeignKey(Lesson, related_name="multiple_choice_exercises", on_delete=models.CASCADE)
    instruction_az = models.TextField("Tapşırıq (az)")
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Çoxseçimli məşğələ"
        verbose_name_plural = "Çoxseçimli məşğələlər"

    def __str__(self):
        return self.instruction_az[:60]


class MultipleChoiceItem(models.Model):
    exercise = models.ForeignKey(MultipleChoiceExercise, related_name="items", on_delete=models.CASCADE)
    question_fa = models.CharField("Sual (fars)", max_length=500)
    options = models.JSONField("Variantlar", default=list)
    correct_index = models.PositiveIntegerField("Düzgün variantın indeksi (0-dan başlar)", default=0)
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "id"]


class PracticeRevealExercise(models.Model):
    # Ya "lesson" (Çalışmalar siyahısındakı sərbəst məşğələ), ya da
    # "grammar_note" (mövzunun öz detalında görünən kart) doldurulur — ikisi
    # eyni vaxtda boş qala bilməz, amma DB səviyyəsində məcburi deyil.
    lesson = models.ForeignKey(
        Lesson, related_name="practice_reveal_exercises", on_delete=models.CASCADE,
        null=True, blank=True,
    )
    grammar_note = models.ForeignKey(
        GrammarNote, related_name="drills", on_delete=models.CASCADE,
        null=True, blank=True,
    )
    title_fa = models.CharField(
        "Başlıq (fars)", max_length=255, blank=True, default="",
        help_text="Yalnız mövzu kartı kimi göstərildikdə istifadə olunur (məs. «مانند مثال جایگزین کنید»).",
    )
    instruction_az = models.TextField("Tapşırıq (az)")
    example_fa = models.CharField(
        "Nümunə cümlə (fars)", max_length=500, blank=True, default="",
        help_text="Dərslikdəki nümunə qutusunun baza cümləsi. Vurğulanacaq fel(lər)i *ulduz* içinə al (məs. «...سبز *نیست*؛ قرمز *است*.»).",
    )
    example_prompt_fa = models.CharField(
        "Nümunənin söz dəsti (fars)", max_length=255, blank=True, default="",
        help_text="Məs. «ماژیک / سیاه‌آبی».",
    )
    example_answer_fa = models.CharField(
        "Nümunənin işlənmiş cavabı (fars)", max_length=500, blank=True, default="",
        help_text="example_prompt_fa əsasında qurulan nümunə cümlə, eyni *ulduz* qaydası ilə.",
    )
    example_reading_az = models.CharField(
        "Nümunənin oxunuşu (az)", max_length=500, blank=True, default="",
        help_text="example_fa (və varsa example_answer_fa) üçün üzündən oxunuş.",
    )
    example_az = models.CharField(
        "Nümunənin tərcüməsi (az)", max_length=500, blank=True, default="",
        help_text="example_fa (və varsa example_answer_fa) üçün tərcümə.",
    )
    example_image_have = models.ImageField(
        "Nümunə şəkli («var» tərəfi)", upload_to=lesson_image_path, blank=True, null=True,
        help_text="Şəkillə göstərilən «has/dارم» tərəfi üçün nümunə şəkli (məs. تصویری بازی/بگویید məşğələləri).",
    )
    example_image_not_have = models.ImageField(
        "Nümunə şəkli («yoxdur» tərəfi)", upload_to=lesson_image_path, blank=True, null=True,
    )
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Praktika (özünüyoxlama) məşğələsi"
        verbose_name_plural = "Praktika (özünüyoxlama) məşğələləri"

    def __str__(self):
        return self.title_fa or self.instruction_az[:60]


class PracticeRevealItem(models.Model):
    exercise = models.ForeignKey(PracticeRevealExercise, related_name="items", on_delete=models.CASCADE)
    prompt_fa = models.CharField("Sual/tapşırıq (fars)", max_length=500)
    answer_fa = models.CharField("Nümunə cavab (fars)", max_length=500)
    reading_az = models.CharField("Cavabın oxunuşu (az)", max_length=500, blank=True, default="")
    az = models.CharField("Cavabın tərcüməsi (az)", max_length=500, blank=True, default="")
    image_have = models.ImageField(
        "Şəkil («var» tərəfi)", upload_to=lesson_image_path, blank=True, null=True,
        help_text="Bu sətrin sahib olduğu əşya/xüsusiyyətin şəkli (məs. «دارم» tərəfi).",
    )
    image_not_have = models.ImageField(
        "Şəkil («yoxdur» tərəfi)", upload_to=lesson_image_path, blank=True, null=True,
    )
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "id"]


class SentencePractice(models.Model):
    """'Sözlərin işləndiyi cümlələr' kartı: hər dərsdə iki nömrələnmiş
    siyahı — گوش کنید و بخوانید (listen_items) və لطفاً پاسخ دهید (answer_items)."""

    lesson = models.OneToOneField(Lesson, related_name="sentence_practice", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sözlərin işləndiyi cümlələr"
        verbose_name_plural = "Sözlərin işləndiyi cümlələr"

    def __str__(self):
        return f"Sözlərin işləndiyi cümlələr — Dərs {self.lesson.number}"


class ListenReadSentence(models.Model):
    practice = models.ForeignKey(SentencePractice, related_name="listen_items", on_delete=models.CASCADE)
    fa = models.CharField("Cümlə (fars)", max_length=500)
    reading_az = models.CharField("Oxunuşu (az hərfləri ilə)", max_length=500, blank=True, default="")
    az = models.CharField("Tərcümə (az)", max_length=500)
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Dinlə və oxu cümləsi"
        verbose_name_plural = "Dinlə və oxu cümlələri (گوش کنید و بخوانید)"

    def __str__(self):
        return self.fa[:60]


class AnswerQuestionSentence(models.Model):
    practice = models.ForeignKey(SentencePractice, related_name="answer_items", on_delete=models.CASCADE)
    fa = models.CharField("Sual (fars)", max_length=500)
    reading_az = models.CharField("Sualın oxunuşu (az hərfləri ilə)", max_length=500, blank=True, default="")
    az = models.CharField("Tərcümə (az)", max_length=500)
    sample_answer_fa = models.CharField("Nümunə cavab (fars)", max_length=500, blank=True, default="")
    sample_answer_reading_az = models.CharField(
        "Nümunə cavabın oxunuşu (az hərfləri ilə)", max_length=500, blank=True, default=""
    )
    sample_answer_az = models.CharField("Nümunə cavabın tərcüməsi (az)", max_length=500, blank=True, default="")
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Cavab veriləcək sual"
        verbose_name_plural = "Cavab veriləcək suallar (لطفاً پاسخ دهید)"

    def __str__(self):
        return self.fa[:60]


class Infinitive(models.Model):
    """'Sözlərin işləndiyi cümlələr' kartındakı 'Məsdərlər' bölməsi: hər dərsdə
    bəzi feillərin məsdəri və indiki zamanda hallanması (mən/sən/o/biz/siz/onlar)."""

    practice = models.ForeignKey(SentencePractice, related_name="infinitives", on_delete=models.CASCADE)
    fa = models.CharField("Məsdər (fars)", max_length=255)
    reading_az = models.CharField("Oxunuşu (az hərfləri ilə)", max_length=255, blank=True, default="")
    az = models.CharField("Tərcümə (az)", max_length=255)
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Məsdər"
        verbose_name_plural = "Məsdərlər"

    def __str__(self):
        return f"{self.fa} — {self.az}"


class ConjugatedForm(models.Model):
    PERSON_CHOICES = [
        ("men", "Mən"),
        ("sen", "Sən"),
        ("o", "O"),
        ("biz", "Biz"),
        ("siz", "Siz"),
        ("onlar", "Onlar"),
    ]

    infinitive = models.ForeignKey(Infinitive, related_name="forms", on_delete=models.CASCADE)
    person = models.CharField("Şəxs", max_length=10, choices=PERSON_CHOICES)
    fa = models.CharField("Fel forması (fars)", max_length=255)
    reading_az = models.CharField("Oxunuşu (az hərfləri ilə)", max_length=255, blank=True, default="")
    az = models.CharField("Tərcümə (az)", max_length=255)
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Hallanmış forma"
        verbose_name_plural = "Hallanmış formalar"

    def __str__(self):
        return self.fa


class ReadingText(models.Model):
    lesson = models.OneToOneField(Lesson, related_name="reading_text", on_delete=models.CASCADE)
    title_fa = models.CharField("Başlıq (fars)", max_length=255)
    title_az = models.CharField("Başlıq (az)", max_length=255)
    image = models.ImageField("Şəkil", upload_to=lesson_image_path, blank=True, null=True)
    paragraphs_fa = models.JSONField("Paraqraflar (fars)", default=list)
    full_translation_az = models.TextField("Tam tərcümə (az)")
    sentences = models.JSONField(
        "Cümlələr (toxunanda oxunuş+tərcümə görünür)",
        default=list,
        blank=True,
        help_text='Hər biri {"fa", "reading_az", "az", "new_paragraph"} formasında. Boşdursa köhnə paraqraf görünüşü işlədilir.',
    )

    class Meta:
        verbose_name = "Oxu mətni"
        verbose_name_plural = "Oxu mətnləri"

    def __str__(self):
        return self.title_az


class ReadingFootnote(models.Model):
    reading_text = models.ForeignKey(ReadingText, related_name="footnotes", on_delete=models.CASCADE)
    fa = models.CharField("Fars", max_length=500)
    az = models.CharField("Azərbaycan", max_length=500)
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "id"]


class ReadingComprehensionQuestion(models.Model):
    """"لطفاً پاسخ دهید" bölməsi: mətndən sonra, sözlərdən sonra göstərilən,
    qapalı kartın içində açılan anlama sualları."""

    reading_text = models.ForeignKey(ReadingText, related_name="comprehension_questions", on_delete=models.CASCADE)
    question_fa = models.CharField("Sual (fars)", max_length=500)
    reading_az = models.CharField("Sualın oxunuşu (az hərfləri ilə)", max_length=500, blank=True, default="")
    az = models.CharField("Sualın tərcüməsi (az)", max_length=500, blank=True, default="")
    sample_answer_fa = models.CharField("Nümunə cavab (fars)", max_length=500, blank=True, default="")
    sample_answer_reading_az = models.CharField(
        "Nümunə cavabın oxunuşu (az hərfləri ilə)", max_length=500, blank=True, default=""
    )
    sample_answer_az = models.CharField("Nümunə cavabın tərcüməsi (az)", max_length=500, blank=True, default="")
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Anlama sualı"
        verbose_name_plural = "Anlama sualları"
