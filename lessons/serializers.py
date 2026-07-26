from django.db.models import Max
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


class VocabWordSerializer(serializers.ModelSerializer):
    # Yalnız yaradarkən lazımdır: sözün hansı dərsə aid olduğunu Lesson.number
    # ilə göstərir (mobil tətbiq dərsin PK-sını deyil, nömrəsini bilir).
    lesson = serializers.SlugRelatedField(
        slug_field="number", queryset=Lesson.objects.all(), write_only=True, required=True
    )

    class Meta:
        model = VocabWord
        fields = ("id", "lesson", "fa", "reading_az", "az", "image", "order")
        read_only_fields = ("id", "order")


class ConjugationRowSerializer(serializers.ModelSerializer):
    # Yalnız yaradarkən lazımdır: sətrin hansı qrammatika mövzusuna aid
    # olduğunu GrammarNote-un id-si ilə göstərir.
    grammar_note = serializers.PrimaryKeyRelatedField(
        queryset=GrammarNote.objects.all(), write_only=True, required=True
    )

    class Meta:
        model = ConjugationRow
        fields = ("id", "grammar_note", "pronoun_fa", "form_fa", "order")
        read_only_fields = ("id", "order")


class ExampleSentenceSerializer(serializers.ModelSerializer):
    grammar_note = serializers.PrimaryKeyRelatedField(
        queryset=GrammarNote.objects.all(), write_only=True, required=True
    )

    class Meta:
        model = ExampleSentence
        fields = ("id", "grammar_note", "fa", "reading_az", "az", "order")
        read_only_fields = ("id", "order")


class GrammarNoteWriteSerializer(serializers.ModelSerializer):
    """'Qeyd' kartının (note_fa/reading_az/az) mobil tətbiqdən redaktəsi üçün.
    Başlıq (title_fa/az) qəsdən yazıla bilən deyil — seed_lessons.py bu sahəni
    mövzunun sabit açarı kimi istifadə edir (bax seed_lessons.py-dəki şərh)."""

    class Meta:
        model = GrammarNote
        fields = ("id", "note_fa", "note_reading_az", "note_az")
        read_only_fields = ("id",)


class PracticeRevealItemSerializer(serializers.ModelSerializer):
    exercise = serializers.PrimaryKeyRelatedField(
        queryset=PracticeRevealExercise.objects.all(), write_only=True, required=True
    )

    class Meta:
        model = PracticeRevealItem
        fields = ("id", "exercise", "prompt_fa", "answer_fa", "reading_az", "az", "image_have", "image_not_have")
        read_only_fields = ("id",)


class PracticeRevealExerciseSerializer(serializers.ModelSerializer):
    items = PracticeRevealItemSerializer(many=True, read_only=True)
    type = serializers.SerializerMethodField()

    class Meta:
        model = PracticeRevealExercise
        fields = (
            "id",
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
            "id",
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
    exercise = serializers.PrimaryKeyRelatedField(
        queryset=FillBlankExercise.objects.all(), write_only=True, required=True
    )

    class Meta:
        model = FillBlankItem
        fields = (
            "id", "exercise", "fa_with_blank", "correct_answer",
            "reading_az", "az", "full_reading_az", "full_translation_az",
        )
        read_only_fields = ("id",)


class FillBlankExerciseSerializer(serializers.ModelSerializer):
    items = FillBlankItemSerializer(many=True, read_only=True)
    type = serializers.SerializerMethodField()

    class Meta:
        model = FillBlankExercise
        fields = ("id", "type", "instruction_az", "word_bank", "items")

    def get_type(self, obj):
        return "fill_blank"


class PictureSentenceLineSerializer(serializers.ModelSerializer):
    # Yalnız yaradarkən lazımdır: sətrin hansı şəkil elementinə aid olduğunu
    # PictureSentenceItem-in id-si ilə göstərir.
    item = serializers.PrimaryKeyRelatedField(
        queryset=PictureSentenceItem.objects.all(), write_only=True, required=True
    )

    class Meta:
        model = PictureSentenceLine
        fields = ("id", "item", "fa", "reading_az", "az")
        read_only_fields = ("id",)


class PictureSentenceItemSerializer(serializers.ModelSerializer):
    sentences = PictureSentenceLineSerializer(many=True, read_only=True)
    exercise = serializers.PrimaryKeyRelatedField(
        queryset=PictureSentenceExercise.objects.all(), write_only=True, required=True
    )

    class Meta:
        model = PictureSentenceItem
        fields = ("id", "exercise", "image", "image_have", "image_not_have", "sentences")
        read_only_fields = ("id",)


class PictureSentenceExerciseSerializer(serializers.ModelSerializer):
    items = PictureSentenceItemSerializer(many=True, read_only=True)
    type = serializers.SerializerMethodField()

    class Meta:
        model = PictureSentenceExercise
        fields = (
            "id",
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
    exercise = serializers.PrimaryKeyRelatedField(
        queryset=AnswerQuestionExercise.objects.all(), write_only=True, required=True
    )

    class Meta:
        model = AnswerQuestionExerciseItem
        fields = (
            "id", "exercise", "fa", "reading_az", "az",
            "sample_answer_fa", "sample_answer_reading_az", "sample_answer_az",
        )
        read_only_fields = ("id",)


class AnswerQuestionExerciseSerializer(serializers.ModelSerializer):
    items = AnswerQuestionExerciseItemSerializer(many=True, read_only=True)
    type = serializers.SerializerMethodField()

    class Meta:
        model = AnswerQuestionExercise
        fields = (
            "id", "type", "title_fa", "example_fa", "example_reading_az", "example_az",
            "instruction_az", "note_fa", "note_reading_az", "note_az", "items",
        )

    def get_type(self, obj):
        return "answer_question"


class ListenReadSentenceSerializer(serializers.ModelSerializer):
    exercise = serializers.PrimaryKeyRelatedField(
        queryset=ListenReadExercise.objects.all(), write_only=True, required=True
    )

    class Meta:
        model = ListenReadSentence
        fields = ("id", "exercise", "fa", "reading_az", "az", "order")
        read_only_fields = ("id", "order")

    def create(self, validated_data):
        exercise = validated_data.pop("exercise")
        next_order = (exercise.items.aggregate(Max("order"))["order__max"] or 0) + 1
        return ListenReadSentence.objects.create(exercise=exercise, order=next_order, **validated_data)

    def update(self, instance, validated_data):
        validated_data.pop("exercise", None)
        return super().update(instance, validated_data)


class ListenReadExerciseSerializer(serializers.ModelSerializer):
    items = ListenReadSentenceSerializer(many=True, read_only=True)

    class Meta:
        model = ListenReadExercise
        fields = ("id", "order", "items")


class AnswerQuestionSentenceSerializer(serializers.ModelSerializer):
    lesson = serializers.SlugRelatedField(
        slug_field="number", queryset=Lesson.objects.all(), write_only=True, required=True
    )

    class Meta:
        model = AnswerQuestionSentence
        fields = (
            "id", "lesson", "fa", "reading_az", "az",
            "sample_answer_fa", "sample_answer_reading_az", "sample_answer_az", "order",
        )
        read_only_fields = ("id", "order")

    def create(self, validated_data):
        lesson = validated_data.pop("lesson")
        practice, _ = SentencePractice.objects.get_or_create(lesson=lesson)
        next_order = (practice.answer_items.aggregate(Max("order"))["order__max"] or 0) + 1
        return AnswerQuestionSentence.objects.create(practice=practice, order=next_order, **validated_data)

    def update(self, instance, validated_data):
        validated_data.pop("lesson", None)
        return super().update(instance, validated_data)


class ConjugatedFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConjugatedForm
        fields = ("id", "person", "fa", "reading_az", "az")
        read_only_fields = ("id",)


class InfinitiveSerializer(serializers.ModelSerializer):
    forms = ConjugatedFormSerializer(many=True, required=False)
    # Yalnız yaradarkən lazımdır: hansı dərsə aid olduğunu göstərir.
    lesson = serializers.SlugRelatedField(
        slug_field="number", queryset=Lesson.objects.all(), write_only=True, required=False
    )

    class Meta:
        model = Infinitive
        fields = ("id", "lesson", "fa", "reading_az", "az", "forms")
        read_only_fields = ("id",)

    def create(self, validated_data):
        lesson = validated_data.pop("lesson")
        forms_data = validated_data.pop("forms", [])
        practice, _ = SentencePractice.objects.get_or_create(lesson=lesson)
        next_order = (practice.infinitives.aggregate(Max("order"))["order__max"] or 0) + 1
        infinitive = Infinitive.objects.create(practice=practice, order=next_order, **validated_data)
        for f_order, form in enumerate(forms_data):
            ConjugatedForm.objects.create(infinitive=infinitive, order=f_order, **form)
        return infinitive

    def update(self, instance, validated_data):
        validated_data.pop("lesson", None)
        forms_data = validated_data.pop("forms", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if forms_data is not None:
            existing = {f.person: f for f in instance.forms.all()}
            for f_order, form in enumerate(forms_data):
                row = existing.get(form.get("person"))
                if row is not None:
                    row.fa = form.get("fa", row.fa)
                    row.reading_az = form.get("reading_az", row.reading_az)
                    row.az = form.get("az", row.az)
                    row.order = f_order
                    row.save()
                else:
                    ConjugatedForm.objects.create(infinitive=instance, order=f_order, **form)
        return instance


class SentencePracticeSerializer(serializers.ModelSerializer):
    listen_exercises = ListenReadExerciseSerializer(many=True, read_only=True)
    answer_items = AnswerQuestionSentenceSerializer(many=True, read_only=True)
    infinitives = InfinitiveSerializer(many=True, read_only=True)

    class Meta:
        model = SentencePractice
        fields = (
            "id", "listen_exercises", "answer_items", "infinitives",
            "answer_note_fa", "answer_note_reading_az", "answer_note_az",
        )


class SentencePracticeNoteWriteSerializer(serializers.ModelSerializer):
    """'Suallara cavab verin' siyahısının sonundakı 'Qeyd' kartının (answer_note_*)
    mobil tətbiqdən redaktəsi üçün."""

    class Meta:
        model = SentencePractice
        fields = ("id", "answer_note_fa", "answer_note_reading_az", "answer_note_az")
        read_only_fields = ("id",)


class ReadingFootnoteSerializer(serializers.ModelSerializer):
    reading_text = serializers.PrimaryKeyRelatedField(
        queryset=ReadingText.objects.all(), write_only=True, required=True
    )

    class Meta:
        model = ReadingFootnote
        fields = ("id", "reading_text", "fa", "az")
        read_only_fields = ("id",)


class ReadingComprehensionQuestionSerializer(serializers.ModelSerializer):
    reading_text = serializers.PrimaryKeyRelatedField(
        queryset=ReadingText.objects.all(), write_only=True, required=True
    )

    class Meta:
        model = ReadingComprehensionQuestion
        fields = (
            "id",
            "reading_text",
            "question_fa",
            "reading_az",
            "az",
            "sample_answer_fa",
            "sample_answer_reading_az",
            "sample_answer_az",
        )
        read_only_fields = ("id",)


class ReadingTextSerializer(serializers.ModelSerializer):
    footnotes = ReadingFootnoteSerializer(many=True, read_only=True)
    comprehension_questions = ReadingComprehensionQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = ReadingText
        fields = (
            "id",
            "title_fa",
            "title_az",
            "image",
            "paragraphs_fa",
            "full_translation_az",
            "sentences",
            "footnotes",
            "comprehension_questions",
        )
        read_only_fields = ("id",)


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
        # "exercises" siyahısındakı yeri); bütün növləri bir siyahıda toplayıb
        # ÜMUMİ "order" ilə sıralamaq, istənilən növün istənilən mövqedə
        # görünməsinə imkan verir.
        exercises = []
        for exercise in obj.fill_blank_exercises.all():
            exercises.append((exercise.order, FillBlankExerciseSerializer(exercise, context=self.context).data))
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
