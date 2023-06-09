# Generated by Django 3.2.16 on 2023-05-01 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',), 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='follow',
            options={'ordering': ('-user',), 'verbose_name': 'Подписка', 'verbose_name_plural': 'Подписки'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ('-title',), 'verbose_name': 'Группа статей', 'verbose_name_plural': 'Группы статей'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('pub_date',), 'verbose_name': ('Статья',), 'verbose_name_plural': 'Статьи'},
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_follow'),
        ),
    ]
