import nested_admin
from django.contrib import admin
from django.utils.html import format_html

from .models import (
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
    fields = ("order", "fa", "reading_az", "az", "image", "preview")
    readonly_fields = ("preview",)

    def preview(self, obj):
        return thumb(obj.image.url if obj.image else None)

    preview.short_description = "Önizləmə"


class ConjugationRowInline(nested_admin.NestedTabularInline):
    model = ConjugationRow
    extra = 1


class ExampleSentenceInline(nested_admin.NestedTabularInline):
    model = ExampleSentence
    extra = 1
    fields = ("order", "fa", "reading_az", "az")


class TopicDrillItemInline(nested_admin.NestedTabularInline):
    model = PracticeRevealItem
    extra = 1
    fields = ("order", "prompt_fa", "answer_fa", "reading_az", "az")


class TopicDrillInline(nested_admin.NestedStackedInline):
    """Mövzunun öz detalında kart kimi görünən məşğələ (məs. «مانند مثال
    جایگزین کنید») — ümumi "Çalışmalar" siyahısındakılardan fərqli olaraq
    birbaşa bu Qrammatika qeydinə bağlıdır (lesson sahəsi boş qalır)."""

    model = PracticeRevealExercise
    fk_name = "grammar_note"
    extra = 0
    max_num = 1
    fields = ("title_fa", "instruction_az", "example_fa", "example_prompt_fa", "example_answer_fa")
    verbose_name = "Mövzu kartı (məsələn, «Nümunə kimi əvəz edin»)"
    verbose_name_plural = "Mövzu kartları"
    inlines = [TopicDrillItemInline]


class GrammarNoteInline(nested_admin.NestedStackedInline):
    model = GrammarNote
    extra = 0
    inlines = [ConjugationRowInline, ExampleSentenceInline, TopicDrillInline]


class FillBlankItemInline(nested_admin.NestedTabularInline):
    model = FillBlankItem
    extra = 1


class FillBlankExerciseInline(nested_admin.NestedStackedInline):
    model = FillBlankExercise
    extra = 0
    inlines = [FillBlankItemInline]


class TrueFalseImageItemInline(nested_admin.NestedTabularInline):
    model = TrueFalseImageItem
    extra = 1
    fields = ("order", "image", "preview", "statement_fa", "statement_az", "is_true")
    readonly_fields = ("preview",)

    def preview(self, obj):
        return thumb(obj.image.url if obj.image else None)

    preview.short_description = "Önizləmə"


class TrueFalseImageExerciseInline(nested_admin.NestedStackedInline):
    model = TrueFalseImageExercise
    extra = 0
    inlines = [TrueFalseImageItemInline]


class MultipleChoiceItemInline(nested_admin.NestedTabularInline):
    model = MultipleChoiceItem
    extra = 1


class MultipleChoiceExerciseInline(nested_admin.NestedStackedInline):
    model = MultipleChoiceExercise
    extra = 0
    inlines = [MultipleChoiceItemInline]


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
    fields = ("order", "fa", "reading_az", "az")


class AnswerQuestionSentenceInline(nested_admin.NestedTabularInline):
    model = AnswerQuestionSentence
    extra = 1
    fields = ("order", "fa", "reading_az", "az", "sample_answer_fa", "sample_answer_reading_az", "sample_answer_az")


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
    inlines = [ListenReadSentenceInline, AnswerQuestionSentenceInline, InfinitiveInline]


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
        TrueFalseImageExerciseInline,
        MultipleChoiceExerciseInline,
        PracticeRevealExerciseInline,
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

