from rest_framework.routers import DefaultRouter

from .views import (
    AnswerQuestionExerciseItemViewSet,
    AnswerQuestionExerciseViewSet,
    AnswerQuestionSentenceViewSet,
    ConjugationRowViewSet,
    ExampleSentenceViewSet,
    FillBlankExerciseViewSet,
    FillBlankItemViewSet,
    GradeViewSet,
    GrammarNoteViewSet,
    InfinitiveViewSet,
    LessonViewSet,
    ListenReadExerciseNoteViewSet,
    ListenReadSentenceViewSet,
    MultiBlankExerciseViewSet,
    MultiBlankItemViewSet,
    PictureSentenceExerciseViewSet,
    PictureSentenceItemViewSet,
    PictureSentenceLineViewSet,
    PracticeRevealExerciseViewSet,
    PracticeRevealItemViewSet,
    ReadingComprehensionQuestionViewSet,
    ReadingFootnoteViewSet,
    ReadingTextViewSet,
    SentencePracticeNoteViewSet,
    VocabWordViewSet,
)

router = DefaultRouter()
router.register("grades", GradeViewSet, basename="grade")
router.register("lessons", LessonViewSet, basename="lesson")
router.register("vocab-words", VocabWordViewSet, basename="vocab-word")
router.register("grammar-notes", GrammarNoteViewSet, basename="grammar-note")
router.register("conjugation-rows", ConjugationRowViewSet, basename="conjugation-row")
router.register("example-sentences", ExampleSentenceViewSet, basename="example-sentence")
router.register("listen-sentences", ListenReadSentenceViewSet, basename="listen-sentence")
router.register("listen-exercise-notes", ListenReadExerciseNoteViewSet, basename="listen-exercise-note")
router.register("answer-sentences", AnswerQuestionSentenceViewSet, basename="answer-sentence")
router.register("infinitives", InfinitiveViewSet, basename="infinitive")
router.register("reading-texts", ReadingTextViewSet, basename="reading-text")
router.register("reading-footnotes", ReadingFootnoteViewSet, basename="reading-footnote")
router.register(
    "reading-comprehension-questions", ReadingComprehensionQuestionViewSet, basename="reading-comprehension-question"
)
router.register("sentence-practice-notes", SentencePracticeNoteViewSet, basename="sentence-practice-note")
router.register("fill-blank-exercises", FillBlankExerciseViewSet, basename="fill-blank-exercise")
router.register("fill-blank-items", FillBlankItemViewSet, basename="fill-blank-item")
router.register("multi-blank-exercises", MultiBlankExerciseViewSet, basename="multi-blank-exercise")
router.register("multi-blank-items", MultiBlankItemViewSet, basename="multi-blank-item")
router.register("practice-reveal-exercises", PracticeRevealExerciseViewSet, basename="practice-reveal-exercise")
router.register("practice-reveal-items", PracticeRevealItemViewSet, basename="practice-reveal-item")
router.register("picture-sentence-exercises", PictureSentenceExerciseViewSet, basename="picture-sentence-exercise")
router.register("picture-sentence-items", PictureSentenceItemViewSet, basename="picture-sentence-item")
router.register("picture-sentence-lines", PictureSentenceLineViewSet, basename="picture-sentence-line")
router.register("answer-question-exercises", AnswerQuestionExerciseViewSet, basename="answer-question-exercise")
router.register(
    "answer-question-exercise-items", AnswerQuestionExerciseItemViewSet, basename="answer-question-exercise-item"
)

urlpatterns = router.urls
