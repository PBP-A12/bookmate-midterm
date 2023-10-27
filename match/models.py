from django.db import models

# Create your models here.
from authentication.models import Member

class Matching(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="matching_user")
    matched_member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="matched_member")
    matched_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)