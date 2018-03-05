from django.db import models
from django.utils import timezone

class ileti(models.Model):
	yazar = models.CharField(max_length=60)
	baslik = models.CharField(max_length=80)
	yazi_tarihi = models.DateField()
	icerik = models.TextField()
	yayimlanma_tarihi = models.DateField(default=timezone.now)

	def __str__(self):
		return self.baslik
