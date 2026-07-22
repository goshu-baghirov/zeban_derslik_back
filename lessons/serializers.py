from rest_framework import serializers

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
        fields = ("prompt_fa", "answer_fa", "reading_az", "az")


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
        fields = ("title_az", "title_fa", "conjugations", "examples", "drills")


class FillBlankItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FillBlankItem
        fields = ("fa_with_blank", "correct_answer")


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
        fields = ("listen_items", "answer_items", "infinitives")


class ReadingFootnoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingFootnote
        fields = ("fa", "az")


class ReadingTextSerializer(serializers.ModelSerializer):
    footnotes = ReadingFootnoteSerializer(many=True, read_only=True)

    class Meta:
        model = ReadingText
        fields = ("title_fa", "title_az", "image", "paragraphs_fa", "full_translation_az", "footnotes")


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
        exercises = []
        for exercise in obj.fill_blank_exercises.all():
            exercises.append(FillBlankExerciseSerializer(exercise, context=self.context).data)
        for exercise in obj.true_false_exercises.all():
            exercises.append(TrueFalseImageExerciseSerializer(exercise, context=self.context).data)
        for exercise in obj.multiple_choice_exercises.all():
            exercises.append(MultipleChoiceExerciseSerializer(exercise, context=self.context).data)
        for exercise in obj.practice_reveal_exercises.all():
            exercises.append(PracticeRevealExerciseSerializer(exercise, context=self.context).data)
        return exercises


class LessonSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ("number", "title_fa", "title_az", "available")


class GradeSerializer(serializers.ModelSerializer):
    lessons = LessonSummarySerializer(many=True, read_only=True)

    class Meta:
        model = Grade
        fields = ("number", "title", "available", "lessons")
