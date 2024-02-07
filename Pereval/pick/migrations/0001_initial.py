

from django.db import migrations, models
import django.db.models.deletion
import pick.func


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('height', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Координаты',
                'verbose_name_plural': 'Координаты',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.ImageField(blank=True, null=True, upload_to=pick.func.get_path_upload_photos, verbose_name='Изображение')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'pereval_images',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(blank=True, max_length=10, null=True, verbose_name='Зима')),
                ('summer', models.CharField(blank=True, max_length=10, null=True, verbose_name='Лето')),
                ('autumn', models.CharField(blank=True, max_length=10, null=True, verbose_name='Осень')),
                ('spring', models.CharField(blank=True, max_length=10, null=True, verbose_name='Весна')),
            ],
            options={
                'verbose_name': 'Уровень сложности',
                'verbose_name_plural': 'Уровни сложности',
            },
        ),
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('new', 'новый'), ('pending', 'в работе'), ('accepted', 'принят'), ('rejected', 'отклонен')], max_length=10)),
                ('beauty_title', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True, verbose_name='Название вершины')),
                ('other_titles', models.TextField(blank=True, null=True, verbose_name='Другое название')),
                ('connect', models.TextField(blank=True, null=True)),
                ('add_time', models.TimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'pereval_added',
                'verbose_name_plural': 'Перевалы',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('fam', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('otc', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('email',), name='user_unique'),
        ),
        migrations.AddField(
            model_name='pereval',
            name='coords',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pick.coords'),
        ),
        migrations.AddField(
            model_name='pereval',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pick.level'),
        ),
        migrations.AddField(
            model_name='pereval',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pick.user'),
        ),
        migrations.AddField(
            model_name='image',
            name='pereval',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pick.pereval'),
        ),
    ]
