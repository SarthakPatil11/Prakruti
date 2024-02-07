# Generated by Django 4.1.3 on 2023-01-31 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prakruti_App', '0005_alter_users_phone_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Med_per_ord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_id', models.IntegerField()),
                ('m_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_id', models.IntegerField()),
                ('UserName', models.CharField(default='', max_length=20)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Status', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='appointments',
            old_name='Day',
            new_name='Date',
        ),
        migrations.RemoveField(
            model_name='blogs',
            name='Img',
        ),
        migrations.RemoveField(
            model_name='blogs',
            name='text',
        ),
        migrations.AddField(
            model_name='appointments',
            name='U_id',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogs',
            name='file',
            field=models.FileField(blank=True, default='Prakruti_App/Blogs/hr1.jpg', null=True, upload_to='Prakruti_App/Blogs/'),
        ),
        migrations.AlterField(
            model_name='m_remedy',
            name='Content',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='m_remedy',
            name='Desc',
            field=models.CharField(default='', max_length=100),
        ),
    ]