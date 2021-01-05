# Generated by Django 3.0.7 on 2020-09-12 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100, verbose_name='IP адрес нарушителя')),
                ('why', models.CharField(max_length=1000, verbose_name='Причина блокировки')),
            ],
            options={
                'verbose_name': 'Заблокировать пользователя по IP ',
                'verbose_name_plural': 'Заблокировать пользователя по IP',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, null=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категории товаров',
                'verbose_name_plural': 'Категории товаров',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=50000, verbose_name='Текст раздела')),
            ],
            options={
                'verbose_name': 'FAQ (Правила магазина)',
                'verbose_name_plural': 'FAQ (Правила магазина)',
            },
        ),
        migrations.CreateModel(
            name='Messenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название соц-сети')),
                ('link', models.CharField(max_length=1000, verbose_name='Ссылка')),
                ('icon', models.CharField(max_length=100, verbose_name='Иконка (fontawesome.com)')),
                ('color', models.CharField(max_length=100, verbose_name='Цвет иконки')),
                ('size', models.CharField(default='22px', max_length=100, verbose_name='Цвет иконки')),
            ],
            options={
                'verbose_name': 'Соцсети (Обратная связь)',
                'verbose_name_plural': 'Соцсети (Обратная связь)',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, null=True, verbose_name='Название')),
                ('description', models.TextField(default='NONE', max_length=50000, null=True, verbose_name='Описание')),
                ('notes', models.TextField(default='NONE', max_length=50000, null=True, verbose_name='Примечания')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Disabled', 'Disabled')], max_length=50, null=True, verbose_name='Статус')),
                ('key_account', models.CharField(choices=[('KEY', 'KEY'), ('ACCOUNT', 'ACCOUNT')], max_length=50, null=True, verbose_name='Ключ или аккаунт')),
                ('email', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=50, null=True, verbose_name='Наличие почты')),
                ('new', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=50, null=True, verbose_name='Новое')),
                ('discount', models.CharField(choices=[('0', '0'), ('5', '5'), ('10', '10'), ('15', '15'), ('20', '20'), ('25', '25'), ('30', '30'), ('35', '35'), ('40', '40'), ('45', '45'), ('50', '50'), ('55', '55'), ('60', '60'), ('65', '65'), ('70', '70'), ('75', '75'), ('80', '80'), ('85', '85'), ('90', '90'), ('95', '95')], default=0, max_length=50, null=True, verbose_name='Скидка (default=0)')),
                ('guarantee', models.CharField(choices=[('1 день', '1 день'), ('2 дня', '2 дня'), ('3 дня', '3 дня'), ('1 неделя', '1 неделя'), ('14 дней', '14 дней'), ('1 месяц', '1 месяц'), ('3 месяца', '3 месяца'), ('1 год', '1 год'), ('Вечная', 'Вечная'), ('NO', 'NO')], max_length=50, null=True, verbose_name='Гарантия')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, default='default_image.png', null=True, upload_to='', verbose_name='Обложка (16/9)')),
                ('data_created', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товары',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Настройки сайта', max_length=50, verbose_name='Название конфигурации')),
                ('background', models.CharField(default='#f2edf3', max_length=50, verbose_name='Фон сайта')),
                ('slyder', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=50, null=True, verbose_name='Слайдер на главной')),
                ('loader', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=50, null=True, verbose_name='Анимация загрузки сайта')),
                ('loader_time', models.CharField(default='2500', max_length=50, verbose_name='Время загрузки сайта')),
                ('animation', models.CharField(default='1200', max_length=50, verbose_name='Скорость анимаций на сайте ')),
                ('ico_image', models.ImageField(blank=True, default='default_ico.ico', null=True, upload_to='', verbose_name='Иконка сайта в строке браузера (16x16)')),
                ('logo_image', models.ImageField(blank=True, default='default_logo.svg', null=True, upload_to='', verbose_name='Лого сайта')),
                ('logo_image_width', models.CharField(default='35', max_length=50, verbose_name='Лого сайта (width)')),
                ('logo_text', models.CharField(default='Shop', max_length=50, verbose_name='Текст рядом с лого')),
                ('ban_image', models.ImageField(blank=True, default='default_ban.png', null=True, upload_to='', verbose_name='Фотография на странице бана')),
                ('support', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=50, null=True, verbose_name='Обратная связь (Иконка рядом с лого)')),
                ('buttons_style', models.CharField(choices=[('primary', 'primary'), ('secondary', 'secondary'), ('success', 'success'), ('danger', 'danger'), ('warning', 'warning'), ('info', 'info'), ('light', 'light'), ('dark', 'dark')], default='success', max_length=50, null=True, verbose_name='Цвет кнопок на сайте')),
                ('key_color', models.CharField(default='#EB2F83', max_length=100, verbose_name='Настройки иконки КЛЮЧ\nЦвет иконки ключа')),
                ('border_key', models.CharField(default='#EB2F83', max_length=100, verbose_name='Цвет рамки')),
                ('background_key', models.CharField(default='#fff', max_length=100, verbose_name='Цвет заднего фона')),
                ('border_radius_key', models.CharField(default='1rem', max_length=100, verbose_name='Border radius')),
                ('padding_top_bottom_key', models.CharField(default='8px', max_length=100, verbose_name='Padding top + bottom')),
                ('padding_left_right_key', models.CharField(default='10px', max_length=100, verbose_name='Padding left + right')),
            ],
            options={
                'verbose_name': 'Настройки сайта',
                'verbose_name_plural': 'Настройки сайта',
            },
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500, verbose_name='Текст обращения')),
                ('user_support', models.CharField(max_length=50, verbose_name='Контакты для связи с пользователем')),
                ('answer', models.TextField(max_length=5000, verbose_name='Ответ администрации')),
                ('ip', models.CharField(default=0, max_length=100, verbose_name='IP пользователя')),
                ('data_created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Обращения пользователей',
                'verbose_name_plural': 'Обращения пользователей',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Product')),
            ],
            options={
                'verbose_name': 'Слайдер на главной странице',
                'verbose_name_plural': 'Слайдер на главной странице',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery', verbose_name='Изображение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='mainapp.Product')),
            ],
            options={
                'verbose_name': 'Галерея (Фотографии к товару)',
                'verbose_name_plural': 'Галерея (Фотографии к товару)',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=50, verbose_name='Автор')),
                ('text', models.TextField(max_length=500, verbose_name='Текст комментария')),
                ('ip', models.CharField(default=0, max_length=100, verbose_name='IP автора')),
                ('data_created', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Product')),
            ],
            options={
                'verbose_name': 'Комментарии пользователей',
                'verbose_name_plural': 'Комментарии пользователей',
            },
        ),
    ]
