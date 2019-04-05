from django.db import models
from match.models.userinfo import UserInfo

class Reaction(models.Model):
    id = models.IntegerField(primary_key=True)
    to_user = models.ForeignKey(UserInfo, on_delete=False, related_name="toid")
    from_user = models.ForeignKey(UserInfo, on_delete=False, related_name="fromid")
    status = models.IntegerField(primary_key=False)