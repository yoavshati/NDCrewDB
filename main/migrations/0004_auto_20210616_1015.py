# Generated by Django 3.2.3 on 2021-06-16 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0003_auto_20210615_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='department',
            field=models.IntegerField(choices=[(1, 'כנף 1'), (2, 'כנף 4'), (3, 'בח"א 8'), (4, 'כנף 25'), (5, 'בח"א 28'), (6, 'בח"א 30'), (7, 'מחלקת שפיצים'), (8, 'מחלקת מנועים'), (9, 'מחלקת הנדסה'), (10, 'אחר')], verbose_name='שיוך ארגוני'),
        ),
        migrations.AlterField(
            model_name='user',
            name='EC_level',
            field=models.IntegerField(choices=[(1, 'אין הסמכה'), (2, 'רמה I'), (3, 'רמה II')], default=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='IRT_level',
            field=models.IntegerField(choices=[(1, 'אין הסמכה'), (2, 'רמה I'), (3, 'רמה II')], default=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='LST_level',
            field=models.IntegerField(choices=[(1, 'אין הסמכה'), (2, 'רמה I'), (3, 'רמה II')], default=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='MT_level',
            field=models.IntegerField(choices=[(1, 'אין הסמכה'), (2, 'רמה I'), (3, 'רמה II')], default=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='PAUT_level',
            field=models.IntegerField(choices=[(1, 'אין הסמכה'), (2, 'רמה I'), (3, 'רמה II')], default=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='PT_level',
            field=models.IntegerField(choices=[(1, 'אין הסמכה'), (2, 'רמה I'), (3, 'רמה II')], default=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='RT_level',
            field=models.IntegerField(choices=[(1, 'אין הסמכה'), (2, 'רמה I'), (3, 'רמה II')], default=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='UT_level',
            field=models.IntegerField(choices=[(1, 'אין הסמכה'), (2, 'רמה I'), (3, 'רמה II')], default=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.IntegerField(choices=[(1, 'כנף 1'), (2, 'כנף 4'), (3, 'בח"א 8'), (4, 'כנף 25'), (5, 'בח"א 28'), (6, 'בח"א 30'), (7, 'מחלקת שפיצים'), (8, 'מחלקת מנועים'), (9, 'מחלקת הנדסה'), (10, 'אחר')]),
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='auth.group'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tap_level',
            field=models.IntegerField(choices=[(1, 'אין הסמכה'), (2, 'רמה I'), (3, 'רמה II')], default=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='visual_level',
            field=models.IntegerField(choices=[(1, 'אין הסמכה'), (2, 'רמה I'), (3, 'רמה II')], default=2),
        ),
    ]