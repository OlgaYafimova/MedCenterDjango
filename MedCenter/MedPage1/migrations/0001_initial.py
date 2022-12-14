# Generated by Django 4.1.2 on 2022-10-28 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('doctors_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=80, verbose_name='Ф.И.О. врача')),
                ('sex', models.CharField(choices=[('жен', 'женский'), ('муж', 'мужской')], max_length=7, verbose_name='Пол')),
                ('date_birth', models.DateField(verbose_name='Дата рождения')),
                ('phone', models.IntegerField(verbose_name='Телефон')),
                ('specialization', models.CharField(max_length=30, verbose_name='Специализация')),
                ('shedule', models.CharField(max_length=30, verbose_name='График работы')),
                ('office', models.IntegerField(verbose_name='Номер кабинета')),
            ],
            options={
                'verbose_name': 'Врач',
                'verbose_name_plural': 'Врачи',
                'ordering': ('full_name',),
            },
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('patients_id', models.AutoField(primary_key=True, serialize=False)),
                ('pat_name', models.CharField(max_length=80, verbose_name='Ф.И.О. пациента')),
                ('date_birth', models.DateField(verbose_name='Дата рождения')),
                ('sex', models.CharField(choices=[('жен', 'женский'), ('муж', 'мужской')], max_length=7, verbose_name='Пол')),
                ('address', models.TextField(verbose_name='Домашний адрес')),
                ('phone', models.CharField(max_length=11, verbose_name='Телефон')),
                ('chronic_deseases', models.TextField(max_length=300, verbose_name='Хронические заболевания')),
            ],
            options={
                'verbose_name': 'Пациент',
                'verbose_name_plural': 'Пациенты',
                'ordering': ('pat_name',),
            },
        ),
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('surgery_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Дата операции')),
                ('dyagnosis', models.TextField(verbose_name='Диагноз')),
                ('name_oper', models.TextField(verbose_name='Название операции')),
                ('descript_oper', models.TextField(verbose_name='Описание операции')),
                ('after_oper_rec', models.TextField(verbose_name='Послеоперационные назначения')),
                ('name_doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedPage1.doctors', verbose_name='Врач')),
                ('name_pat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedPage1.patients', verbose_name='Пациент')),
            ],
            options={
                'verbose_name': 'Операция',
                'verbose_name_plural': 'Операции',
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('laboratory_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Дата анализа')),
                ('type_of_analysis', models.CharField(choices=[('биохимия', 'Биохимический анализ крови'), ('ОАК', 'Общий анализ крови'), ('гемостаз', 'Контроль свёртываемости'), ('Гормональная панель', (('щитовидка', 'Гормоны щитовидной железы'), ('надпочечники', 'Гормоны надпочечников'), ('половые', 'Половые гормоны'))), ('инфекции', 'Инфекционная панель'), ('онко', 'Онкологическая панель')], max_length=100, verbose_name='Вид анализа')),
                ('term', models.IntegerField(verbose_name='Срок исполнения')),
                ('result', models.TextField(verbose_name='Результат')),
                ('name_pat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedPage1.patients', verbose_name='Пациент')),
            ],
            options={
                'verbose_name': 'Лабораторное исследование',
                'verbose_name_plural': 'Лабораторные исследования',
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Instrumental',
            fields=[
                ('instrumental_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Дата исследования')),
                ('type_of_research', models.TextField(verbose_name='Вид исследования')),
                ('description', models.TextField(verbose_name='Описание')),
                ('name_doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedPage1.doctors', verbose_name='Врач, проводивший исследование')),
                ('name_pat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedPage1.patients', verbose_name='Пациент')),
            ],
            options={
                'verbose_name': 'Инструментальное исследование',
                'verbose_name_plural': 'Инструментальные исследования',
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Gratitude',
            fields=[
                ('gratitude_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Дата благодарности')),
                ('gratitude', models.TextField(verbose_name='Текст благодарности')),
                ('response', models.TextField(verbose_name='Ответ администрации')),
                ('name_pat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedPage1.patients', verbose_name='Пациент')),
            ],
            options={
                'verbose_name': 'Благодарность',
                'verbose_name_plural': 'Благодарности',
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Doctors_education',
            fields=[
                ('doc_educat_id', models.AutoField(primary_key=True, serialize=False)),
                ('education', models.TextField(verbose_name='Образование')),
                ('courses', models.TextField(verbose_name='Курсы повышения квалификации')),
                ('degrees', models.TextField(verbose_name='Научные степени')),
                ('doc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedPage1.doctors', verbose_name='Ф.И.О. врача')),
            ],
            options={
                'verbose_name': 'Квалификация',
                'verbose_name_plural': 'Квалификации',
                'ordering': ('doc_name',),
            },
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('complaint_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Дата жалобы')),
                ('complaint', models.TextField(verbose_name='Текст жалобы')),
                ('response', models.TextField(verbose_name='Ответ администрации')),
                ('name_pat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedPage1.patients', verbose_name='Пациент')),
            ],
            options={
                'verbose_name': 'Жалоба',
                'verbose_name_plural': 'Жалобы',
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Checkup',
            fields=[
                ('checkup_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Дата осмотра')),
                ('symptomes', models.TextField(verbose_name='Симптомы')),
                ('dyagnosis', models.TextField(verbose_name='Диагноз')),
                ('prescriptions', models.TextField(verbose_name='Назначения')),
                ('medicament', models.TextField(verbose_name='Название лекарства')),
                ('method_of_taking', models.TextField(verbose_name='Способ приёма')),
                ('main_effect', models.TextField(verbose_name='Действие')),
                ('side_effect', models.TextField(verbose_name='Побочное действие')),
                ('name_doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedPage1.doctors', verbose_name='Врач')),
                ('name_pat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedPage1.patients', verbose_name='Пациент')),
            ],
            options={
                'verbose_name': 'Осмотр',
                'verbose_name_plural': 'Осмотры',
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Accidents',
            fields=[
                ('accidents_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Дата аварии')),
                ('accident', models.TextField(verbose_name='Описание аварии')),
                ('actions_taken', models.TextField(verbose_name='Предпринятые действия')),
                ('name_doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedPage1.doctors', verbose_name='Врач')),
                ('name_pat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedPage1.patients', verbose_name='Пациент')),
            ],
            options={
                'verbose_name': 'Авария',
                'verbose_name_plural': 'Аварии',
                'ordering': ('date',),
            },
        ),
    ]
