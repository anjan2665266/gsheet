# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField


class GSheetData(models.Model):
	sheet_id= models.CharField(max_length=100, null=True, blank=True)
	excel_data = JSONField(default=dict)
	status= models.BooleanField (default=1)
	created= models.DateTimeField(auto_now_add=True)
	class Meta:
		db_table = 'google_sheet_data'


