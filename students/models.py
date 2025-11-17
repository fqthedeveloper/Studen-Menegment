from django.db import models

class StudSelection(models.Model):
    sel_SelectedIDKey = models.IntegerField(primary_key=True)
    sel_UserName = models.CharField(max_length=25, null=True, blank=True)
    sel_TableName = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'StudSelection'
