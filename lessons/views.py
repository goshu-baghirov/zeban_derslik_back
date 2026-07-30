from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Max
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from rest_framework import viewsets

from .models import (
    AnswerQuestionExercise,
    AnswerQuestionExerciseItem,
    AnswerQuestionSentence,
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
from .serializers import (
    AnswerQuestionExerciseItemSerializer,
    AnswerQuestionExerciseSerializer,
    AnswerQuestionSentenceSerializer,
    ConjugationRowSerializer,
    ExampleSentenceSerializer,
    FillBlankExerciseSerializer,
    FillBlankItemSerializer,
    GradeSerializer,
    GrammarNoteWriteSerializer,
    InfinitiveSerializer,
    LessonSerializer,
    ListenReadExerciseNoteWriteSerializer,
    ListenReadSentenceSerializer,
    MultiBlankExerciseSerializer,
    MultiBlankItemSerializer,
    PictureSentenceExerciseSerializer,
    PictureSentenceItemSerializer,
    PictureSentenceLineSerializer,
    PracticeRevealExerciseSerializer,
    PracticeRevealItemSerializer,
    ReadingComprehensionQuestionSerializer,
    ReadingFootnoteSerializer,
    ReadingTextSerializer,
    SentencePracticeNoteWriteSerializer,
    VocabWordSerializer,
)


@staff_member_required
def grade_admin_redirect(request, number):
    """Sidebar-dakı sinif keçidləri üçün sabit URL: sinfi nömrəsinə görə tapıb
    onun admin redaktə səhifəsinə yönləndirir (PK-dan asılı deyil)."""
    grade = get_object_or_404(Grade, number=number)
    return redirect(reverse("admin:lessons_grade_change", args=[grade.pk]))


class GradeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Grade.objects.prefetch_related("lessons")
    serializer_class = GradeSerializer
    lookup_field = "number"


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lesson.objects.select_related("grade").prefetch_related(
        "vocabulary",
        "grammar_notes__conjugations",
        "grammar_notes__examples",
        "grammar_notes__drills__items",
        "fill_blank_exercises__items",
        "multi_blank_exercises__items",
        "practice_reveal_exercises__items",
        "picture_sentence_exercises__items__sentences",
        "answer_question_exercises__items",
        "sentence_practice__listen_exercises__items",
        "sentence_practice__answer_items",
        "sentence_practice__infinitives__forms",
        "reading_text__footnotes",
    )
    serializer_class = LessonSerializer
    lookup_field = "number"


class VocabWordViewSet(viewsets.ModelViewSet):
    """Powers the mobile app's Söz ehtiyatı edit screen: editing an existing
    word's fa/reading/az/image, or adding a brand-new word to a lesson.
    Deleting is intentionally not exposed here — not requested."""

    queryset = VocabWord.objects.all()
    serializer_class = VocabWordSerializer
    http_method_names = ["get", "post", "patch", "head", "options"]

    def perform_create(self, serializer):
        lesson = serializer.validated_data["lesson"]
        next_order = (lesson.vocabulary.aggregate(Max("order"))["order__max"] or 0) + 1
        serializer.save(order=next_order, edited_via_app=True)

    def perform_update(self, serializer):
        serializer.save(edited_via_app=True)


class GrammarNoteViewSet(viewsets.ModelViewSet):
    """Yalnız 'Qeyd' kartının (note_fa/reading_az/az) və izah qutusunun
    (explanation_az) redaktəsi üçün — yeni mövzu (GrammarNote) yaratmaq bu
    endpoint-dən mümkün deyil, ona görə create/list/destroy açılmayıb."""

    queryset = GrammarNote.objects.all()
    serializer_class = GrammarNoteWriteSerializer
    http_method_names = ["get", "patch", "head", "options"]

    def perform_update(self, serializer):
        # İki müstəqil bayraq: izahı redaktə etmək 'Qeyd' mətnini fayl
        # yeniləməsindən dondurmamalıdır (və əksinə). PATCH yalnız dəyişən
        # sahələri göndərdiyinə görə hansının gəldiyinə baxırıq.
        touched = set(serializer.validated_data)
        flags = {}
        if touched & {"note_fa", "note_reading_az", "note_az"}:
            flags["edited_via_app"] = True
        if "explanation_az" in touched:
            flags["explanation_edited_via_app"] = True
        serializer.save(**flags)


class ConjugationRowViewSet(viewsets.ModelViewSet):
    queryset = ConjugationRow.objects.all()
    serializer_class = ConjugationRowSerializer
    http_method_names = ["get", "post", "patch", "head", "options"]

    def perform_create(self, serializer):
        grammar_note = serializer.validated_data["grammar_note"]
        next_order = (grammar_note.conjugations.aggregate(Max("order"))["order__max"] or 0) + 1
        serializer.save(order=next_order, edited_via_app=True)

    def perform_update(self, serializer):
        serializer.save(edited_via_app=True)


class ExampleSentenceViewSet(viewsets.ModelViewSet):
    queryset = ExampleSentence.objects.all()
    serializer_class = ExampleSentenceSerializer
    http_method_names = ["get", "post", "patch", "head", "options"]

    def perform_create(self, serializer):
        grammar_note = serializer.validated_data["grammar_note"]
        next_order = (grammar_note.examples.aggregate(Max("order"))["order__max"] or 0) + 1
        serializer.save(order=next_order, edited_via_app=True)

    def perform_update(self, serializer):
        serializer.save(edited_via_app=True)


class ListenReadSentenceViewSet(viewsets.ModelViewSet):
    queryset = ListenReadSentence.objects.all()
    serializer_class = ListenReadSentenceSerializer
    http_method_names = ["get", "post", "patch", "head", "options"]

    def perform_create(self, serializer):
        serializer.save(edited_via_app=True)

    def perform_update(self, serializer):
        serializer.save(edited_via_app=True)


class AnswerQuestionSentenceViewSet(viewsets.ModelViewSet):
    queryset = AnswerQuestionSentence.objects.all()
    serializer_class = AnswerQuestionSentenceSerializer
    http_method_names = ["get", "post", "patch", "head", "options"]

    def perform_create(self, serializer):
        serializer.save(edited_via_app=True)

    def perform_update(self, serializer):
        serializer.save(edited_via_app=True)


class InfinitiveViewSet(viewsets.ModelViewSet):
    """'Məsdərlər' tam admin/tətbiq-mülkiyyətindədir (seed_lessons.py heç vaxt
    toxunmur) — ona görə edited_via_app bayrağı lazım deyil."""

    queryset = Infinitive.objects.all().prefetch_related("forms")
    serializer_class = InfinitiveSerializer
    http_method_names = ["get", "post", "patch", "head", "options"]


# --- Mətn (ReadingText) ---

class ReadingTextViewSet(viewsets.ModelViewSet):
    """Yalnız mövcud Oxu mətninin öz sahələrinin (title/image/tərcümə/
    paraqraf/cümlələr) redaktəsi üçün — hər dərsin öz ReadingText sətri
    seeding zamanı artıq yaradılır, ona görə create açılmayıb."""

    queryset = ReadingText.objects.all()
    serializer_class = ReadingTextSerializer
    http_method_names = ["get", "patch", "head", "options"]

    def perform_update(self, serializer):
        serializer.save(edited_via_app=True)


class ReadingFootnoteViewSet(viewsets.ModelViewSet):
    queryset = ReadingFootnote.objects.all()
    serializer_class = ReadingFootnoteSerializer
    http_method_names = ["get", "post", "patch", "head", "options"]

    def perform_create(self, serializer):
        reading_text = serializer.validated_data["reading_text"]
        next_order = (reading_text.footnotes.aggregate(Max("order"))["order__max"] or 0) + 1
        serializer.save(order=next_order, edited_via_app=True)

    def perform_update(self, serializer):
        serializer.save(edited_via_app=True)


class ReadingComprehensionQuestionViewSet(viewsets.ModelViewSet):
    queryset = ReadingComprehensionQuestion.objects.all()
    serializer_class = ReadingComprehensionQuestionSerializer
    http_method_names = ["get", "post", "patch", "head", "options"]

    def perform_create(self, serializer):
        reading_text = serializer.validated_data["reading_text"]
        next_order = (reading_text.comprehension_questions.aggregate(Max("order"))["order__max"] or 0) + 1
        serializer.save(order=next_order, edited_via_app=True)

    def perform_update(self, serializer):
        serializer.save(edited_via_app=True)


class SentencePracticeNoteViewSet(viewsets.ModelViewSet):
    """'Suallara cavab verin' siyahısının sonundakı 'Qeyd' kartının
    (answer_note_*) redaktəsi üçün."""

    queryset = SentencePractice.objects.all()
    serializer_class = SentencePracticeNoteWriteSerializer
    http_method_names = ["get", "patch", "head", "options"]

    def perform_update(self, serializer):
        serializer.save(answer_note_edited_via_app=True)


class ListenReadExerciseNoteViewSet(viewsets.ModelViewSet):
    """Bir 'Dinləyin və oxuyun' Çalışmasının sonundakı 'Qeyd' kartının
    (note_*) redaktəsi üçün."""

    queryset = ListenReadExercise.objects.all()
    serializer_class = ListenReadExerciseNoteWriteSerializer
    http_method_names = ["get", "patch", "head", "options"]

    def perform_update(self, serializer):
        serializer.save(note_edited_via_app=True)


# --- Çalışmalar (Boşluq doldurma) ---

class FillBlankExerciseViewSet(viewsets.ModelViewSet):
    queryset = FillBlankExercise.objects.all()
    serializer_class = FillBlankExerciseSerializer
    http_method_names = ["get", "patch", "head", "options"]

    def perform_update(self, serializer):
        serializer.save(edited_via_app=True)


class FillBlankItemViewSet(viewsets.ModelViewSet):
    queryset = FillBlankItem.objects.all()
    serializer_class = FillBlankItemSerializer
    http_method_names = ["get", "post", "patch", "head", "options"]

    def perform_create(self, serializer):
        exercise = serializer.validated_data["exercise"]
        next_order = (exercise.items.aggregate(Max("order"))["order__max"] or 0) + 1
        serializer.save(order=next_order, edited_via_app=True)

    def perform_update(self, serializer):
        serializer.save(edited_via_app=True)


class MultiBlankExerciseViewSet(viewsets.ModelViewSet):
    queryset = MultiBlankExercise.objects.all()
    serializer_class = MultiBlankExerciseSerializer
    http_method_names = ["get", "patch", "head", "options"]

    def perform_update(self, serializer):
        serializer.save(edited_via_app=True)


class MultiBlankItemViewSet(viewsets.ModelViewSet):
    queryset = MultiBlankItem.objects.all()
    serializer_class = MultiBlankItemSerializer
    http_method_names = ["get", "post", "patch", "head", "options"]

    def perform_create(self, serializer):
        exercise = serializer.validated_data["exercise"]
        next_order = (exercise.items.aggregate(Max("order"))["order__max"] or 0) + 1
        serializer.save(order=next_order, edited_via_app=True)

    def perform_update(self, serializer):
        serializer.save(edited_via_app=True)


# --- Çalışmalar (Praktika / özünüyoxlama — "Sadə yoxlama" və "Nümunə drilli") ---

class PracticeRevealExerciseViewSet(viewsets.ModelViewSet):
    """Yalnız lesson-a bağlı (Çalışmalar siyahısındakı) məşğələlər üçün
    istifadə olunur — Qrammatika mövzusunun öz drill kartları (grammar_note-a
    bağlı) mobil tətbiqdən redaktə olunmur, bu yenə eyni model/endpoint-dir,
    sadəcə mobil UI oraya bağlanmayıb."""

    queryset = PracticeRevealExercise.objects.all()
    serializer_class = PracticeRevealExerciseSerializer
    http_method_names = ["get", "patch", "head", "options"]

    def perform_update(self, serializer):
        serializer.save(edited_via_app=True)


class PracticeRevealItemViewSet(viewsets.ModelViewSet):
    queryset = PracticeRevealItem.objects.all()
    serializer_class = PracticeRevealItemSerializer
    http_method_names = ["get", "post", "patch", "head", "options"]

    def perform_create(self, serializer):
        exercise = serializer.validated_data["exercise"]
        next_order = (exercise.items.aggregate(Max("order"))["order__max"] or 0) + 1
        serializer.save(order=next_order, edited_via_app=True)

    def perform_update(self, serializer):
        serializer.save(edited_via_app=True)


# --- Çalışmalar (Şəkilli cümlə) ---

class PictureSentenceExerciseViewSet(viewsets.ModelViewSet):
    queryset = PictureSentenceExercise.objects.all()
    serializer_class = PictureSentenceExerciseSerializer
    http_method_names = ["get", "patch", "head", "options"]

    def perform_update(self, serializer):
        serializer.save(edited_via_app=True)


class PictureSentenceItemViewSet(viewsets.ModelViewSet):
    """Yalnız elementin öz şəkil sahələrini (image/image_have/image_not_have)
    idarə edir — cümlələr (sentences) ayrıca PictureSentenceLineViewSet
    vasitəsilə (multipart formada iç-içə siyahı göndərmək mümkün olmadığı
    üçün, VocabWord-dan fərqli olaraq bu, iki addımlı redaktədir: əvvəl
    element yarat/şəklini dəyiş, sonra onun cümlələrini ayrıca idarə et)."""

    queryset = PictureSentenceItem.objects.all()
    serializer_class = PictureSentenceItemSerializer
    http_method_names = ["get", "post", "patch", "head", "options"]

    def perform_create(self, serializer):
        exercise = serializer.validated_data["exercise"]
        next_order = (exercise.items.aggregate(Max("order"))["order__max"] or 0) + 1
        serializer.save(order=next_order, edited_via_app=True)

    def perform_update(self, serializer):
        serializer.save(edited_via_app=True)


class PictureSentenceLineViewSet(viewsets.ModelViewSet):
    queryset = PictureSentenceLine.objects.all()
    serializer_class = PictureSentenceLineSerializer
    http_method_names = ["get", "post", "patch", "head", "options"]

    def perform_create(self, serializer):
        item = serializer.validated_data["item"]
        next_order = (item.sentences.aggregate(Max("order"))["order__max"] or 0) + 1
        serializer.save(order=next_order)

    # ReadingComprehensionQuestion/FillBlankItem s.k. fərqli olaraq bu sətrin
    # öz edited_via_app sahəsi yoxdur — valideynin (PictureSentenceItem)
    # bayrağı bütöv elementi (şəkil + bütün cümlələri) qoruyur, bax seed_lessons.py.


# --- Çalışmalar (Sual-cavab) ---

class AnswerQuestionExerciseViewSet(viewsets.ModelViewSet):
    queryset = AnswerQuestionExercise.objects.all()
    serializer_class = AnswerQuestionExerciseSerializer
    http_method_names = ["get", "patch", "head", "options"]

    def perform_update(self, serializer):
        serializer.save(edited_via_app=True)


class AnswerQuestionExerciseItemViewSet(viewsets.ModelViewSet):
    queryset = AnswerQuestionExerciseItem.objects.all()
    serializer_class = AnswerQuestionExerciseItemSerializer
    http_method_names = ["get", "post", "patch", "head", "options"]

    def perform_create(self, serializer):
        exercise = serializer.validated_data["exercise"]
        next_order = (exercise.items.aggregate(Max("order"))["order__max"] or 0) + 1
        serializer.save(order=next_order, edited_via_app=True)

    def perform_update(self, serializer):
        serializer.save(edited_via_app=True)
