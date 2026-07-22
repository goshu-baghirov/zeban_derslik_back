import django.db.models.deletion
from django.db import migrations, models

GRADE_TITLES = {
    1: "1-ci sinif",
    2: "2-ci sinif",
    3: "3-cü sinif",
    4: "4-cü sinif",
    5: "5-ci sinif",
    6: "6-cı sinif",
}


def create_grades_and_assign_lessons(apps, schema_editor):
    Grade = apps.get_model("lessons", "Grade")
    Lesson = apps.get_model("lessons", "Lesson")
    for number, title in GRADE_TITLES.items():
        Grade.objects.get_or_create(
            number=number, defaults={"title": title, "available": number == 2}
        )
    grade2 = Grade.objects.get(number=2)
    Lesson.objects.filter(grade__isnull=True).update(grade=grade2)


class Migration(migrations.Migration):

    dependencies = [
        ("lessons", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Grade",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("number", models.PositiveIntegerField(unique=True, verbose_name="Sinif nömrəsi")),
                ("title", models.CharField(max_length=100, verbose_name="Ad")),
                ("available", models.BooleanField(default=False, verbose_name="Aktivdir")),
            ],
            options={
                "verbose_name": "Sinif",
                "verbose_name_plural": "Siniflər",
                "ordering": ["number"],
            },
        ),
        migrations.AddField(
            model_name="lesson",
            name="grade",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lessons",
                to="lessons.grade",
                verbose_name="Sinif",
            ),
        ),
        migrations.AddField(
            model_name="vocabword",
            name="reading_az",
            field=models.CharField(
                blank=True, default="", max_length=255, verbose_name="Oxunuşu (az hərfləri ilə)"
            ),
        ),
        migrations.RunPython(create_grades_and_assign_lessons, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="lesson",
            name="grade",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lessons",
                to="lessons.grade",
                verbose_name="Sinif",
            ),
        ),
    ]
