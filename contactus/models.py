from django.db import models

class ContactUs(models.Model):
    class Meta:
        db_table = "CONTACT_US"

    id = models.BigAutoField(db_column="ID", primary_key=True)
    created_date = models.DateTimeField(
        db_column="CREATED_DATE", auto_now_add=True
    )
    modified_date = models.DateTimeField(
        db_column="MODIFIED_DATE", auto_now_add=True
    )
    full_name = models.CharField(
        db_column="FULL_NAME", null=False, blank=False, max_length=70
    )
    contact_email = models.EmailField(
        db_column="CONTACT_EMAIL", null=False, blank=False
    )
    contact_message = models.TextField(
        db_column="CONTACT_MESSAGE", null=False, blank=False
    )
