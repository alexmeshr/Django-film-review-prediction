from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial')
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='sentiment',
            field=models.IntegerField(default=0),
        ),
    ]