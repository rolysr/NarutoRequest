# Generated by Django 4.0.3 on 2022-05-28 03:13

from django.db import migrations, models
import django.db.models.deletion
import village.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_c', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Invocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_i', models.CharField(max_length=30)),
                ('type_i', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_p', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=1)),
                ('clan', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('element', models.CharField(max_length=20)),
                ('is_hidden', models.BooleanField()),
                ('chakra_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ninja',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='village.person')),
                ('nickname', models.CharField(max_length=20)),
                ('max_chakra_amount', models.IntegerField()),
                ('invocations', models.ManyToManyField(to='village.invocation')),
                ('techniques', models.ManyToManyField(to='village.technique')),
            ],
        ),
        migrations.CreateModel(
            name='Parchment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sealed_date', models.DateField()),
                ('technique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='village.technique')),
                ('ninja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='village.ninja')),
            ],
        ),
        migrations.CreateModel(
            name='CurativeTechnique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curing_speed', models.CharField(max_length=5)),
                ('technique', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='village.technique')),
            ],
        ),
        migrations.CreateModel(
            name='AttackTechnique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attack_range', models.CharField(max_length=5)),
                ('technique', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='village.technique')),
            ],
        ),
        migrations.CreateModel(
            name='Chunin',
            fields=[
                ('ninja', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='village.ninja')),
                ('chunin_exam_grade', models.IntegerField()),
                ('c_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Genin',
            fields=[
                ('ninja', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='village.ninja')),
                ('assessment', models.TextField()),
                ('g_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Jounin',
            fields=[
                ('ninja', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='village.ninja')),
                ('jounin_exam_grade', models.IntegerField()),
                ('j_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MedicalNinja',
            fields=[
                ('ninja', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='village.ninja', validators=[village.models.medical_ninja_validator])),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_t', models.CharField(max_length=30)),
                ('members', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='village.ninja')),
                ('medical_ninja', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='village.medicalninja')),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_date', models.DateField()),
                ('f_date', models.DateField()),
                ('satisfactory_result', models.BooleanField()),
                ('reward_yens', models.IntegerField()),
                ('rank_m', models.CharField(max_length=1)),
                ('churikens_amount', models.IntegerField()),
                ('kunais_amount', models.IntegerField()),
                ('explosive_seals_amount', models.IntegerField()),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='village.client')),
                ('parchments', models.ManyToManyField(to='village.parchment')),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='village.team')),
                ('captain', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='village.jounin')),
            ],
        ),
    ]
