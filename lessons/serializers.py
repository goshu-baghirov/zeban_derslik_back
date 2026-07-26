from rest_framework import serializers

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
    ListenReadSentence,
    MultipleChoiceExercise,
    MultipleChoiceItem,
    PictureSentenceExercise,
    PictureSentenceItem,
    PictureSentenceLine,
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


class VocabWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VocabWord
        fields = ("fa", "reading_az", "az", "image")


class ConjugationRowSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConjugationRow
        fields = ("pronoun_fa", "form_fa")


class ExampleSentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleSentence
        fields = ("fa", "reading_az", "az")


class PracticeRevealItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeRevealItem
        fields = ("prompt_fa", "answer_fa", "reading_az", "az", "image_have", "image_not_have")


class PracticeRevealExerciseSerializer(serializers.ModelSerializer):
    items = PracticeRevealItemSerializer(many=True, read_only=True)
    type = serializers.SerializerMethodField()

    class Meta:
        model = PracticeRevealExercise
        fields = (
            "type",
            "title_fa",
            "instruction_az",
            "example_fa",
            "example_prompt_fa",
            "example_answer_fa",
            "example_reading_az",
            "example_az",
            "example_image_have",
            "example_image_not_have",
            "items",
        )

    def get_type(self, obj):
        return "practice_reveal"


class GrammarNoteSerializer(serializers.ModelSerializer):
    conjugations = ConjugationRowSerializer(many=True, read_only=True)
    examples = ExampleSentenceSerializer(many=True, read_only=True)
    drills = PracticeRevealExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = GrammarNote
        fields = (
            "title_az",
            "title_fa",
            "conjugations",
            "examples",
            "drills",
            "note_fa",
            "note_reading_az",
            "note_az",
        )


class FillBlankItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FillBlankItem
        fields = ("fa_with_blank", "correct_answer", "reading_az", "az", "full_reading_az", "full_translation_az")


class FillBlankExerciseSerializer(serializers.ModelSerializer):
    items = FillBlankItemSerializer(many=True, read_only=True)
    type = serializers.SerializerMethodField()

    class Meta:
        model = FillBlankExercise
        fields = ("type", "instruction_az", "word_bank", "items")

    def get_type(self, obj):
        return "fill_blank"


class TrueFalseImageItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrueFalseImageItem
        fields = ("image", "statement_fa", "statement_az", "is_true")


class TrueFalseImageExerciseSerializer(serializers.ModelSerializer):
    items = TrueFalseImageItemSerializer(many=True, read_only=True)
    type = serializers.SerializerMethodField()

    class Meta:
        model = TrueFalseImageExercise
        fields = ("type", "instruction_az", "items")

    def get_type(self, obj):
        return "true_false_image"


class PictureSentenceLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = PictureSentenceLine
        fields = ("fa", "reading_az", "az")


class PictureSentenceItemSerializer(serializers.ModelSerializer):
    sentences = PictureSentenceLineSerializer(many=True, read_only=True)

    class Meta:
        model = PictureSentenceItem
        fields = ("image", "image_have", "image_not_have", "sentences")


class PictureSentenceExerciseSerializer(serializers.ModelSerializer):
    items = PictureSentenceItemSerializer(many=True, read_only=True)
    type = serializers.SerializerMethodField()

    class Meta:
        model = PictureSentenceExercise
        fields = (
            "type",
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
            "items",
        )

    def get_type(self, obj):
        return "picture_sentences"


class AnswerQuestionExerciseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerQuestionExerciseItem
        fields = ("fa", "reading_az", "az", "sample_answer_fa", "sample_answer_reading_az", "sample_answer_az")


class AnswerQuestionExerciseSerializer(serializers.ModelSerializer):
    items = AnswerQuestionExerciseItemSerializer(many=True, read_only=True)
    type = serializers.SerializerMethodField()

    class Meta:
        model = AnswerQuestionExercise
        fields = ("type", "title_fa", "instruction_az", "note_fa", "note_reading_az", "note_az", "items")

    def get_type(self, obj):
        return "answer_question"


class MultipleChoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoiceItem
        fields = ("question_fa", "options", "correct_index")


class MultipleChoiceExerciseSerializer(serializers.ModelSerializer):
    items = MultipleChoiceItemSerializer(many=True, read_only=True)
    type = serializers.SerializerMethodField()

    class Meta:
        model = MultipleChoiceExercise
        fields = ("type", "instruction_az", "items")

    def get_type(self, obj):
        return "multiple_choice"


class ListenReadSentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListenReadSentence
        fields = ("fa", "reading_az", "az")


class AnswerQuestionSentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerQuestionSentence
        fields = ("fa", "reading_az", "az", "sample_answer_fa", "sample_answer_reading_az", "sample_answer_az")


class ConjugatedFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConjugatedForm
        fields = ("person", "fa", "reading_az", "az")


class InfinitiveSerializer(serializers.ModelSerializer):
    forms = ConjugatedFormSerializer(many=True, read_only=True)

    class Meta:
        model = Infinitive
        fields = ("fa", "reading_az", "az", "forms")


class SentencePracticeSerializer(serializers.ModelSerializer):
    listen_items = ListenReadSentenceSerializer(many=True, read_only=True)
    answer_items = AnswerQuestionSentenceSerializer(many=True, read_only=True)
    infinitives = InfinitiveSerializer(many=True, read_only=True)

    class Meta:
        model = SentencePractice
        fields = (
            "listen_items", "answer_items", "infinitives",
            "answer_note_fa", "answer_note_reading_az", "answer_note_az",
        )


class ReadingFootnoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingFootnote
        fields = ("fa", "az")


class ReadingComprehensionQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingComprehensionQuestion
        fields = (
            "question_fa",
            "reading_az",
            "az",
            "sample_answer_fa",
            "sample_answer_reading_az",
            "sample_answer_az",
        )


class ReadingTextSerializer(serializers.ModelSerializer):
    footnotes = ReadingFootnoteSerializer(many=True, read_only=True)
    comprehension_questions = ReadingComprehensionQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = ReadingText
        fields = (
            "title_fa",
            "title_az",
            "image",
            "paragraphs_fa",
            "full_translation_az",
            "sentences",
            "footnotes",
            "comprehension_questions",
        )


class LessonSerializer(serializers.ModelSerializer):
    vocabulary = VocabWordSerializer(many=True, read_only=True)
    grammar_notes = GrammarNoteSerializer(many=True, read_only=True)
    reading_text = ReadingTextSerializer(read_only=True)
    sentence_practice = SentencePracticeSerializer(read_only=True)
    exercises = serializers.SerializerMethodField()
    grade = serializers.IntegerField(source="grade.number", read_only=True)

    class Meta:
        model = Lesson
        fields = (
            "grade",
            "number",
            "title_fa",
            "title_az",
            "available",
            "vocabulary",
            "grammar_notes",
            "exercises",
            "sentence_practice",
            "reading_text",
        )

    def get_exercises(self, obj):
        # Hər növün öz sıra nömrəsi var (order=overall_order, seed_lessons.py-də
        # "exercises" siyahısındakı yeri), amma bu, əvvəllər YALNIZ eyni növ
        # daxilində sıralanırdı — növlər özləri həmişə sabit ardıcıllıqla
        # (fill_blank → true_false_image → multiple_choice → practice_reveal →
        # picture_sentences) göstərilirdi, "order" dəyərindən asılı olmayaraq.
        # Bütün növləri bir siyahıda toplayıb ÜMUMİ "order" ilə sıralamaq,
        # istənilən növün istənilən mövqedə görünməsinə imkan verir.
        exercises = []
        for exercise in obj.fill_blank_exercises.all():
            exercises.append((exercise.order, FillBlankExerciseSerializer(exercise, context=self.context).data))
        for exercise in obj.true_false_exercises.all():
            exercises.append((exercise.order, TrueFalseImageExerciseSerializer(exercise, context=self.context).data))
        for exercise in obj.multiple_choice_exercises.all():
            exercises.append((exercise.order, MultipleChoiceExerciseSerializer(exercise, context=self.context).data))
        for exercise in obj.practice_reveal_exercises.all():
            exercises.append((exercise.order, PracticeRevealExerciseSerializer(exercise, context=self.context).data))
        for exercise in obj.picture_sentence_exercises.all():
            exercises.append((exercise.order, PictureSentenceExerciseSerializer(exercise, context=self.context).data))
        for exercise in obj.answer_question_exercises.all():
            exercises.append((exercise.order, AnswerQuestionExerciseSerializer(exercise, context=self.context).data))
        exercises.sort(key=lambda pair: pair[0])
        return [data for _, data in exercises]


class LessonSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ("number", "title_fa", "title_az", "available")


class GradeSerializer(serializers.ModelSerializer):
    lessons = LessonSummarySerializer(many=True, read_only=True)

    class Meta:
        model = Grade
        fields = ("number", "title", "available", "lessons")
