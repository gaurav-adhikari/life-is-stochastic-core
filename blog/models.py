from django.db import models

class Blogs(models.Model):
    class Meta:
        db_table = "BLOG"

    id = models.BigAutoField(db_column="ID", primary_key=True)
    blog_title = models.TextField(
        db_column="BLOG_TITLE", null=False, blank=False, max_length=30
    )
    blog_content = models.TextField(
        db_column="BLOG_CONTENT", null=True, blank=True
    )
    created_date = models.DateTimeField(
        db_column="CREATED_DATE", auto_now_add=True
    )
    modified_date = models.DateTimeField(
        db_column="MODIFIED_DATE", auto_now_add=True
    )
    author = models.CharField(
        db_column="AUTHOR", max_length=30
    )
