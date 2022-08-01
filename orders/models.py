from secrets import choice
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()

class order(models.Model):

  customer = models.ForeignKey(User,on_delete=models.CASCADE)
  SIZE = (
  ('SMALL','small'),
  ('MEDIUM','medium'),
  ('LARGE','large'),
  ('EXTRA_LARGE','extraLarge'),
  )
  size = models.CharField(max_length=20,choices=SIZE ,default=SIZE[0][0])
  status = (
  ('PENDING','pending'),
  ('IN_TRANSIT','inTransit'),
  ('DELIVERED','delivered'),
  
  )
  order_status = models.CharField(max_length=20,choices=status,default=status[0][0])
  quantity = models.IntegerField()
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)

  def __str__(self):
    return f"<order(self.size) by (self.customer.id)>"





