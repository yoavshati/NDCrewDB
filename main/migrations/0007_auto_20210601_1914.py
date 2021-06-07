# Generated by Django 3.2.3 on 2021-06-01 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210531_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferanceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_description', models.CharField(max_length=50, verbose_name='תיאור פריט')),
                ('manufacturer_id', models.CharField(max_length=50, verbose_name='מספר יצרן')),
                ('test_method', models.IntegerField(choices=[(1, 'בדיקת ראיה'), (2, 'בדיקת הקשה'), (3, 'זרמי ערבולת'), (4, 'נוזלים חודרים'), (5, 'חלקיקים מגנטיים'), (6, 'אולטרסאונד'), (7, 'רדיוגרפיה'), (8, 'תרמוגרפיה'), (9, 'שירוגרפיה'), (10, 'אחר')], verbose_name='שיטת בדיקה')),
                ('literature_code', models.CharField(max_length=50, verbose_name='שיוך לספרות טכנית')),
                ('testing_hours', models.FloatField(verbose_name='שעתון בדיקה')),
            ],
        ),
        migrations.CreateModel(
            name='TestItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_description', models.CharField(max_length=50, verbose_name='תיאור פריט')),
                ('manufacturer_id', models.CharField(max_length=50, verbose_name='מספר יצרן')),
                ('test_method', models.IntegerField(choices=[(1, 'בדיקת ראיה'), (2, 'בדיקת הקשה'), (3, 'זרמי ערבולת'), (4, 'נוזלים חודרים'), (5, 'חלקיקים מגנטיים'), (6, 'אולטרסאונד'), (7, 'רדיוגרפיה'), (8, 'תרמוגרפיה'), (9, 'שירוגרפיה'), (10, 'אחר')], verbose_name='שיטת בדיקה')),
                ('literature_code', models.CharField(max_length=50, verbose_name='שיוך לספרות טכנית')),
                ('testing_hours', models.FloatField(verbose_name='שעתון בדיקה')),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.RemoveField(
            model_name='user',
            name='rank',
        ),
        migrations.AddField(
            model_name='test',
            name='manufacturer_id',
            field=models.CharField(blank=True, max_length=16, verbose_name='מספר יצרן'),
        ),
        migrations.AlterField(
            model_name='test',
            name='checker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='checker', related_query_name='checker', to=settings.AUTH_USER_MODEL, verbose_name='בודק'),
        ),
        migrations.AlterField(
            model_name='test',
            name='meter_id',
            field=models.CharField(blank=True, max_length=16, verbose_name="מס' סידורי של מכשיר הבדיקה"),
        ),
        migrations.AlterField(
            model_name='test',
            name='part_id',
            field=models.CharField(blank=True, max_length=16, verbose_name="מס' סידורי של הפריט"),
        ),
        migrations.AlterField(
            model_name='test',
            name='tag_number',
            field=models.CharField(blank=True, max_length=16, verbose_name='מספר תג תהליך בדיקת אל הרס'),
        ),
        migrations.AlterField(
            model_name='test',
            name='tester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tester', related_query_name='tester', to=settings.AUTH_USER_MODEL, verbose_name='מבצע'),
        ),
    ]