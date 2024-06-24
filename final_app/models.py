# myapp/models.py
from django.db import models
from django.contrib.auth.models import User
from typing import Optional

class Job(models.Model):
    """ A model representing a job listing.

    attribute: title (str): The title of the job.
    attribute: company_name (str): The name of the company offering the job.
    attribute: location (str): The location where the job is based.
    attribute: link (str): A URL link to the job listing.
    attribute: image (Optional[str]): A URL link to an image related to the job listing (optional).
    """
    title: str = models.CharField(max_length=200)
    company_name: str = models.CharField(max_length=200)
    location: str = models.CharField(max_length=200)
    link: str = models.URLField(max_length=500)
    image: Optional[str] = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        """ Returns the string representation of the Job instance.
        return: str: The title of the job.
        """
        return self.title
