# -*- coding: UTF-8 -*-
from django.db import models
from datetime import datetime

class MyModel(models.Model):
    language = models.CharField(_("language"), max_length=15, db_index=True)
    title = models.CharField(_("title"), max_length=255)
    menu_title = models.CharField(_("title"), max_length=255, blank=True, null=True, help_text=_("overwrite the title in the menu"))
    path = models.CharField(_("Path"), max_length=255, db_index=True)
    has_url_overwrite = models.BooleanField(_("has url overwrite"), default=False, db_index=True, editable=False)
    creation_date = models.DateTimeField(_("creation date"), editable=False, default=datetime.now)
