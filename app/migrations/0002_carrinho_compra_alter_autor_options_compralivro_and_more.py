# Generated by Django 4.2.2 on 2023-06-26 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name_plural': 'Autores'},
        ),
        migrations.CreateModel(
            name='CompraLivro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.compra')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.livro')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='livro',
            field=models.ManyToManyField(through='app.CompraLivro', to='app.livro'),
        ),
        migrations.AddField(
            model_name='compra',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CarrinhoLivro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.carrinho')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.livro')),
            ],
            options={
                'verbose_name_plural': 'CarrinhoLivros',
            },
        ),
        migrations.AddField(
            model_name='carrinho',
            name='livro',
            field=models.ManyToManyField(through='app.CarrinhoLivro', to='app.livro'),
        ),
        migrations.AddField(
            model_name='carrinho',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
