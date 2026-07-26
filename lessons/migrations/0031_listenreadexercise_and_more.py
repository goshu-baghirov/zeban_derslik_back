# Generated manually — introduces ListenReadExercise as a grouping layer
# between SentencePractice and ListenReadSentence ("Dinləyin və oxuyun" is
# now split into numbered Çalışma sub-lists instead of one flat list).

from django.db import migrations, models
import django.db.models.deletion


def group_existing_sentences(apps, schema_editor):
    SentencePractice = apps.get_model("lessons", "SentencePractice")
    ListenReadExercise = apps.get_model("lessons", "ListenReadExercise")

    for practice in SentencePractice.objects.filter(listen_items__isnull=False).distinct():
        exercise = ListenReadExercise.objects.create(practice=practice, order=1)
        practice.listen_items.update(exercise=exercise)


def ungroup_sentences(apps, schema_editor):
    ListenReadSentence = apps.get_model("lessons", "ListenReadSentence")
    for sentence in ListenReadSentence.objects.select_related("exercise"):
        sentence.practice_id = sentence.exercise.practice_id
        sentence.save(update_fields=["practice"])


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0030_answerquestionexercise_edited_via_app_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListenReadExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Sıra')),
                ('practice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listen_exercises', to='lessons.sentencepractice')),
            ],
            options={
                'verbose_name': 'Dinlə-oxu çalışması',
                'verbose_name_plural': 'Dinlə-oxu çalışmaları (گوش کنید و بخوانید)',
                'ordering': ['order', 'id'],
            },
        ),
        migrations.AddField(
            model_name='listenreadsentence',
            name='exercise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='lessons.listenreadexercise'),
        ),
        migrations.RunPython(group_existing_sentences, ungroup_sentences),
        migrations.RemoveField(
            model_name='listenreadsentence',
            name='practice',
        ),
        migrations.AlterField(
            model_name='listenreadsentence',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='lessons.listenreadexercise'),
        ),
    ]
