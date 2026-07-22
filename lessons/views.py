from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from rest_framework import viewsets

from .models import Grade, Lesson
from .serializers import GradeSerializer, LessonSerializer


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
        "true_false_exercises__items",
        "multiple_choice_exercises__items",
        "practice_reveal_exercises__items",
        "sentence_practice__listen_items",
        "sentence_practice__answer_items",
        "sentence_practice__infinitives__forms",
        "reading_text__footnotes",
    )
    serializer_class = LessonSerializer
    lookup_field = "number"
