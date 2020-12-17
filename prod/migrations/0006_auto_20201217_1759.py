# Generated by Django 3.1.3 on 2020-12-17 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prod', '0005_auto_20201217_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='bezel_material',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bezel_material', to='prod.material', verbose_name='Материал безеля'),
        ),
        migrations.AlterField(
            model_name='product',
            name='bracer',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bracer', to='prod.material', verbose_name='Материал браслета'),
        ),
        migrations.AlterField(
            model_name='product',
            name='bracer_colour',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bracer_colour', to='prod.colour', verbose_name='Цвет браслета'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='prod.brand', verbose_name='Бренд'),
        ),
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='prod.condition', verbose_name='Состояние часов'),
        ),
        migrations.AlterField(
            model_name='product',
            name='corpus_material',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='corpus_material', to='prod.material', verbose_name='Материал корпуса'),
        ),
        migrations.AlterField(
            model_name='product',
            name='dial',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dial_colour', to='prod.colour', verbose_name='Циферблат'),
        ),
        migrations.AlterField(
            model_name='product',
            name='equipment',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='prod.equipment', verbose_name='Комплектация'),
        ),
        migrations.AlterField(
            model_name='product',
            name='glass',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='prod.glass', verbose_name='Стекло'),
        ),
        migrations.AlterField(
            model_name='product',
            name='meh_type',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='prod.mehtype', verbose_name='Тип механизма'),
        ),
        migrations.AlterField(
            model_name='product',
            name='numbers',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='prod.numbers', verbose_name='Цифры'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sex',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='prod.sex', verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='product',
            name='watch_type',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='prod.watchtype', verbose_name='Тип часов'),
        ),
        migrations.AlterField(
            model_name='product',
            name='waterproof',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='prod.waterproof', verbose_name='Водонепроницаемость'),
        ),
        migrations.AlterField(
            model_name='product',
            name='zip_material',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='zip_material', to='prod.material', verbose_name='Тип застёжки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='zip_type',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='prod.ziptype', verbose_name='Материал застёжки'),
        ),
    ]