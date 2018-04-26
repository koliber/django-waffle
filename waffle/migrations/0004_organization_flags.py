# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from waffle.utils import uses_org_flags, get_setting


class Migration(migrations.Migration):
    dependencies = [
        ('waffle', '0003_update_strings_for_i18n'),
    ]

    operations = []

    if uses_org_flags():
        organization_model_name = get_setting('ORGANIZATION_MODEL')
        dependencies.append(
            migrations.swappable_dependency(organization_model_name)
        )

        operations.append(
            migrations.AddField(
                model_name='flag',
                name='organizations',
                field=models.ManyToManyField(help_text='Activate this flag for these organizations.',
                                             to=organization_model_name,
                                             verbose_name='Organizations',
                                             blank=True),
            )
        )
