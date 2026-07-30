import nested_admin
from django.contrib import admin
from django.utils.html import format_html

from .models import (
    AnswerQuestionExercise,
    AnswerQuestionExerciseItem,
    AnswerQuestionSentence,
    ConjugatedForm,
    ConjugationRow,
    ExampleSentence,
    FillBlankExercise,
    FillBlankItem,
    Grade,
    GrammarNote,
    Infinitive,
    Lesson,
    ListenReadExercise,
    ListenReadSentence,
    MultiBlankExercise,
    MultiBlankItem,
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


def thumb(url, size=40):
    if url:
        return format_html(
            '<img src="{}" style="width:{}px;height:{}px;object-fit:cover;'
            'border-radius:6px;border:1px solid #334155;" />',
            url, size, size,
        )
    return "—"


class VocabWordInline(nested_admin.NestedTabularInline):
    model = VocabWord
    extra = 1
    fields = ("order", "fa", "reading_az", "az", "image", "preview", "edited_via_app")
    readonly_fields = ("preview", "edited_via_app")

    def preview(self, obj):
        return thumb(obj.image.url if obj.image else None)

    preview.short_description = "Önizləmə"


class ConjugationRowInline(nested_admin.NestedTabularInline):
    model = ConjugationRow
    extra = 1
    fields = ("order", "pronoun_fa", "form_fa", "edited_via_app")
    readonly_fields = ("edited_via_app",)


class ExampleSentenceInline(nested_admin.NestedTabularInline):
    model = ExampleSentence
    extra = 1
    fields = ("order", "fa", "reading_az", "az", "edited_via_app")
    readonly_fields = ("edited_via_app",)


class TopicDrillItemInline(nested_admin.NestedTabularInline):
    model = PracticeRevealItem
    extra = 1
    fields = ("order", "prompt_fa", "answer_fa", "reading_az", "az", "image_have", "image_not_have")


class TopicDrillInline(nested_admin.NestedStackedInline):
    """Mövzunun öz detalında kart kimi görünən məşğələ (məs. «مانند مثال
    جایگزین کنید») — ümumi "Çalışmalar" siyahısındakılardan fərqli olaraq
    birbaşa bu Qrammatika qeydinə bağlıdır (lesson sahəsi boş qalır)."""

    model = PracticeRevealExercise
    fk_name = "grammar_note"
    extra = 0
    fields = (
        "title_fa", "instruction_az", "example_fa", "example_prompt_fa", "example_answer_fa",
        "example_image_have", "example_image_not_have",
    )
    verbose_name = "Mövzu kartı (məsələn, «Nümunə kimi əvəz edin»)"
    verbose_name_plural = "Mövzu kartları"
    inlines = [TopicDrillItemInline]


class GrammarNoteInline(nested_admin.NestedStackedInline):
    model = GrammarNote
    extra = 0
    fields = (
        "order", "title_az", "title_fa", "explanation_az", "explanation_edited_via_app",
        "note_fa", "note_reading_az", "note_az", "edited_via_app",
    )
    readonly_fields = ("edited_via_app", "explanation_edited_via_app")
    inlines = [ConjugationRowInline, ExampleSentenceInline, TopicDrillInline]


class FillBlankItemInline(nested_admin.NestedTabularInline):
    model = FillBlankItem
    extra = 1


class FillBlankExerciseInline(nested_admin.NestedStackedInline):
    model = FillBlankExercise
    extra = 0
    inlines = [FillBlankItemInline]


class MultiBlankItemInline(nested_admin.NestedTabularInline):
    model = MultiBlankItem
    extra = 1
    fields = ("order", "fa_with_blanks", "correct_answers", "full_reading_az", "full_translation_az")


class MultiBlankExerciseInline(nested_admin.NestedStackedInline):
    model = MultiBlankExercise
    extra = 0
    fields = (
        "order", "title_fa", "instruction_az", "word_bank",
        "example_fa", "example_reading_az", "example_az", "edited_via_app",
    )
    readonly_fields = ("edited_via_app",)
    inlines = [MultiBlankItemInline]


class PictureSentenceLineInline(nested_admin.NestedTabularInline):
    model = PictureSentenceLine
    extra = 2
    fields = ("order", "fa", "reading_az", "az")


class PictureSentenceItemInline(nested_admin.NestedStackedInline):
    model = PictureSentenceItem
    extra = 1
    fields = ("order", "image", "preview", "image_have", "image_not_have")
    readonly_fields = ("preview",)
    inlines = [PictureSentenceLineInline]

    def preview(self, obj):
        return thumb(obj.image.url if obj.image else None, size=80)

    preview.short_description = "Önizləmə"


class PictureSentenceExerciseInline(nested_admin.NestedStackedInline):
    model = PictureSentenceExercise
    extra = 0
    fields = (
        "instruction_az",
        "title_fa",
        "example_fa",
        "example_reading_az",
        "example_az",
        "example_answer_fa",
        "example_answer_reading_az",
        "example_answer_az",
        "example_image",
        "example_image_have",
        "example_image_not_have",
        "order",
    )
    inlines = [PictureSentenceItemInline]


class AnswerQuestionExerciseItemInline(nested_admin.NestedTabularInline):
    model = AnswerQuestionExerciseItem
    extra = 1
    fields = ("order", "fa", "reading_az", "az", "sample_answer_fa", "sample_answer_reading_az", "sample_answer_az")


class AnswerQuestionExerciseInline(nested_admin.NestedStackedInline):
    model = AnswerQuestionExercise
    extra = 0
    fields = (
        "order", "title_fa", "example_fa", "example_reading_az", "example_az",
        "instruction_az", "note_fa", "note_reading_az", "note_az",
    )
    inlines = [AnswerQuestionExerciseItemInline]


class PracticeRevealItemInline(nested_admin.NestedTabularInline):
    model = PracticeRevealItem
    extra = 1
    fields = ("order", "prompt_fa", "answer_fa", "reading_az", "az")


class PracticeRevealExerciseInline(nested_admin.NestedStackedInline):
    model = PracticeRevealExercise
    fk_name = "lesson"
    extra = 0
    inlines = [PracticeRevealItemInline]


class ListenReadSentenceInline(nested_admin.NestedTabularInline):
    model = ListenReadSentence
    extra = 1
    fields = ("order", "fa", "reading_az", "az", "edited_via_app")
    readonly_fields = ("edited_via_app",)


class ListenReadExerciseInline(nested_admin.NestedStackedInline):
    model = ListenReadExercise
    extra = 0
    fields = ("order", "note_fa", "note_reading_az", "note_az", "note_edited_via_app")
    readonly_fields = ("note_edited_via_app",)
    inlines = [ListenReadSentenceInline]


class AnswerQuestionSentenceInline(nested_admin.NestedTabularInline):
    model = AnswerQuestionSentence
    extra = 1
    fields = (
        "order", "fa", "reading_az", "az",
        "sample_answer_fa", "sample_answer_reading_az", "sample_answer_az", "edited_via_app",
    )
    readonly_fields = ("edited_via_app",)


class ConjugatedFormInline(nested_admin.NestedTabularInline):
    model = ConjugatedForm
    extra = 6
    fields = ("order", "person", "fa", "reading_az", "az")


class InfinitiveInline(nested_admin.NestedStackedInline):
    model = Infinitive
    extra = 0
    fields = ("order", "fa", "reading_az", "az")
    inlines = [ConjugatedFormInline]


class SentencePracticeInline(nested_admin.NestedStackedInline):
    model = SentencePractice
    extra = 0
    max_num = 1
    inlines = [ListenReadExerciseInline, AnswerQuestionSentenceInline, InfinitiveInline]


class ReadingFootnoteInline(nested_admin.NestedTabularInline):
    model = ReadingFootnote
    extra = 1


class ReadingComprehensionQuestionInline(nested_admin.NestedTabularInline):
    model = ReadingComprehensionQuestion
    extra = 1


class ReadingTextInline(nested_admin.NestedStackedInline):
    model = ReadingText
    extra = 0
    max_num = 1
    fields = ("title_fa", "title_az", "image", "preview", "paragraphs_fa", "full_translation_az", "sentences")
    readonly_fields = ("preview",)
    inlines = [ReadingFootnoteInline, ReadingComprehensionQuestionInline]

    def preview(self, obj):
        return thumb(obj.image.url if obj and obj.image else None)

    preview.short_description = "Önizləmə"


class LessonInline(admin.TabularInline):
    """Grade-2 lesson list shown inside the grade's own admin page. Other
    grades will get their own (different) content structure later."""

    model = Lesson
    extra = 0
    fields = ("order", "title_az", "title_fa", "available")
    show_change_link = True
    verbose_name = "Dərs"
    verbose_name_plural = "Dərslər"


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("number", "title", "available", "lesson_count")
    list_editable = ("available",)
    ordering = ("number",)
    inlines = [LessonInline]

    def get_fieldsets(self, request, obj=None):
        # Add səhifəsində (obj=None) forma tam görünür ki, yeni sinif yaratmaq
        # mümkün olsun; redaktə səhifəsində isə "General" tabı gizlədilir —
        # o səhifə yalnız sinfin dərs siyahısını idarə etmək üçündür.
        if obj is None:
            return super().get_fieldsets(request, obj)
        return []

    @admin.display(description="Dərs sayı")
    def lesson_count(self, obj):
        return obj.lessons.count()


@admin.register(Lesson)
class LessonAdmin(nested_admin.NestedModelAdmin):
    list_display = ("number", "title_az", "title_fa", "grade", "available", "order", "vocab_count")
    list_editable = ("available", "order")
    list_filter = ("grade",)
    search_fields = ("title_az", "title_fa")
    ordering = ("order", "number")
    inlines = [
        VocabWordInline,
        SentencePracticeInline,
        GrammarNoteInline,
        FillBlankExerciseInline,
        MultiBlankExerciseInline,
        PracticeRevealExerciseInline,
        PictureSentenceExerciseInline,
        AnswerQuestionExerciseInline,
        ReadingTextInline,
    ]

    @admin.display(description="Söz sayı")
    def vocab_count(self, obj):
        return obj.vocabulary.count()


@admin.register(GrammarNote)
class GrammarNoteAdmin(nested_admin.NestedModelAdmin):
    list_display = ("title_az", "title_fa", "lesson", "order")
    list_filter = ("lesson__grade", "lesson")
    search_fields = ("title_az", "title_fa")
    ordering = ("lesson", "order")
    inlines = [ConjugationRowInline, ExampleSentenceInline, TopicDrillInline]

