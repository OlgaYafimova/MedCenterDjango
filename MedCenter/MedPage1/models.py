from django.db import models


class Doctors(models.Model):
    doctors_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=80, verbose_name='Ф.И.О. врача')
    sex = models.CharField(max_length=7, choices=(("жен", "женский"), ("муж", "мужской")), verbose_name='Пол')
    date_birth = models.DateField(verbose_name='Дата рождения')
    phone = models.CharField(max_length=11, verbose_name='Телефон')
    specialization = models.CharField(max_length=30, verbose_name='Специализация')
    shedule = models.CharField(max_length=30, verbose_name='График работы')
    office = models.IntegerField(verbose_name='Номер кабинета')

    def __str__(self):
        return f"{self.specialization} - {self.full_name}"

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"
        ordering = ('full_name',)


class Doctors_education(models.Model):
    doc_educat_id = models.AutoField(primary_key=True)
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE, verbose_name='Ф.И.О. врача')
    education = models.TextField(verbose_name='Образование')
    courses = models.TextField(verbose_name='Курсы повышения квалификации')
    degrees = models.TextField(verbose_name='Научные степени')

    def __str__(self):
        return f"{self.doc_name}"

    class Meta:
        verbose_name = "Квалификация"
        verbose_name_plural = "Квалификации"
        ordering = ('doc_name',)


class Patients(models.Model):
    patients_id = models.AutoField(primary_key=True)
    pat_name = models.CharField(max_length=80, verbose_name='Ф.И.О. пациента')
    date_birth = models.DateField(verbose_name='Дата рождения')
    sex = models.CharField(max_length=7, choices=(("жен", "женский"), ("муж", "мужской")), verbose_name='Пол')
    address = models.TextField(verbose_name='Домашний адрес')
    phone = models.CharField(max_length=11, verbose_name='Телефон')
    chronic_deseases = models.TextField(max_length=300, verbose_name='Хронические заболевания')

    def __str__(self):
        return f"{self.pat_name}"

    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"
        ordering = ('pat_name',)


class Checkup(models.Model):
    checkup_id = models.AutoField(primary_key=True)
    name_pat = models.ForeignKey(Patients, on_delete=models.CASCADE, verbose_name='Пациент')
    name_doc = models.ForeignKey(Doctors, on_delete=models.CASCADE, verbose_name='Врач')
    date = models.DateField(verbose_name='Дата осмотра')
    symptomes = models.TextField(verbose_name='Симптомы')
    dyagnosis = models.TextField(verbose_name='Диагноз')
    prescriptions = models.TextField(verbose_name='Назначения')
    medicament = models.TextField(verbose_name='Название лекарства')
    method_of_taking = models.TextField(verbose_name='Способ приёма')
    main_effect = models.TextField(verbose_name='Действие')
    side_effect = models.TextField(verbose_name='Побочное действие')

    def __str__(self):
        return f"{self.date} - {self.name_pat}"

    class Meta:
        verbose_name = "Осмотр"
        verbose_name_plural = "Осмотры"
        ordering = ('date',)


class Laboratory(models.Model):
    laboratory_id = models.AutoField(primary_key=True)
    name_pat = models.ForeignKey(Patients, on_delete=models.CASCADE, verbose_name='Пациент')
    date = models.DateField(verbose_name='Дата анализа')
    type_of_analysis = models.CharField(max_length=100, choices=[
        ("биохимия","Биохимический анализ крови"),
        ("ОАК","Общий анализ крови"),
        ("гемостаз","Контроль свёртываемости"),
        ("Гормональная панель",(
            ("щитовидка","Гормоны щитовидной железы"),
            ("надпочечники","Гормоны надпочечников"),
            ("половые","Половые гормоны"))),
        ("инфекции","Инфекционная панель"),
        ("онко","Онкологическая панель")], verbose_name='Вид анализа')
    term = models.IntegerField(verbose_name='Срок исполнения')
    result = models.TextField(verbose_name='Результат')

    def __str__(self):
        return f"{self.date} - {self.name_pat} - {self.type_of_analysis}"

    class Meta:
        verbose_name = "Лабораторное исследование"
        verbose_name_plural = "Лабораторные исследования"
        ordering = ('date',)


class Instrumental(models.Model):
    instrumental_id = models.AutoField(primary_key=True)
    name_pat = models.ForeignKey(Patients, on_delete=models.CASCADE, verbose_name='Пациент')
    date = models.DateField(verbose_name='Дата исследования')
    type_of_research = models.TextField(verbose_name='Вид исследования')
    description = models.TextField(verbose_name='Описание')
    name_doc = models.ForeignKey(Doctors, on_delete=models.CASCADE, verbose_name='Врач, проводивший исследование')

    def __str__(self):
        return f"{self.date} - {self.name_pat}: {self.type_of_research}"

    class Meta:
        verbose_name = "Инструментальное исследование"
        verbose_name_plural = "Инструментальные исследования"
        ordering = ('date',)


class Surgery(models.Model):
    surgery_id = models.AutoField(primary_key=True)
    name_pat = models.ForeignKey(Patients, on_delete=models.CASCADE, verbose_name='Пациент')
    date = models.DateField(verbose_name='Дата операции')
    name_doc = models.ForeignKey(Doctors, on_delete=models.CASCADE, verbose_name='Врач')
    dyagnosis = models.TextField(verbose_name='Диагноз')
    name_oper = models.TextField(verbose_name='Название операции')
    descript_oper = models.TextField(verbose_name='Описание операции')
    after_oper_rec = models.TextField(verbose_name='Послеоперационные назначения')

    def __str__(self):
        return f"{self.date} - {self.name_pat}: {self.name_oper}"

    class Meta:
        verbose_name = "Операция"
        verbose_name_plural = "Операции"
        ordering = ('date',)


class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    name_pat = models.ForeignKey(Patients, on_delete=models.CASCADE, verbose_name='Пациент')
    date = models.DateField(verbose_name='Дата жалобы')
    complaint = models.TextField(verbose_name='Текст жалобы')
    response = models.TextField(verbose_name='Ответ администрации')

    def __str__(self):
        return f"{self.date} - {self.name_pat}"

    class Meta:
        verbose_name = "Жалоба"
        verbose_name_plural = "Жалобы"
        ordering = ('date',)


class Gratitude(models.Model):
    gratitude_id = models.AutoField(primary_key=True)
    name_pat = models.ForeignKey(Patients, on_delete=models.CASCADE, verbose_name='Пациент')
    date = models.DateField(verbose_name='Дата благодарности')
    gratitude = models.TextField(verbose_name='Текст благодарности')
    response = models.TextField(verbose_name='Ответ администрации')

    def __str__(self):
        return f"{self.date} - {self.name_pat}"

    class Meta:
        verbose_name = "Благодарность"
        verbose_name_plural = "Благодарности"
        ordering = ('date',)


class Accidents(models.Model):
    accidents_id = models.AutoField(primary_key=True)
    date = models.DateField(verbose_name='Дата аварии')
    name_doc = models.ForeignKey(Doctors, on_delete=models.CASCADE, verbose_name='Врач')
    name_pat = models.ForeignKey(Patients, on_delete=models.CASCADE, verbose_name='Пациент')
    accident = models.TextField(verbose_name='Описание аварии')
    actions_taken = models.TextField(verbose_name='Предпринятые действия')

    def __str__(self):
        return f"{self.date} - {self.name_doc}"

    class Meta:
        verbose_name = "Авария"
        verbose_name_plural = "Аварии"
        ordering = ('date',)
