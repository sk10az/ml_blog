# Generated by Django 4.1.7 on 2023-03-27 18:27

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_remove_category_email_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="description",
        ),
        migrations.AddField(
            model_name="post",
            name="content",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="media",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                blank=True, null=True
            ),
        ),
    ]