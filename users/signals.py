# Where is the user created when we register? -In the User Table
# Kaydolduğumuzda kullanıcı nerede oluşturulur? -Kullanıcı Tablosunda
from django.contrib.auth.models import User  

# Send signals immediately after the user is created
# Kullanıcı oluşturulduktan hemen sonra sinyal gönder
from django.db.models.signals import post_save 
from django.dispatch import receiver  # catch signals # sinyalleri yakala

# The table we will create tokens after capturing the signals
# Sinyalleri yakaladıktan sonra token oluşturacağımız tablo
from rest_framework.authtoken.models import Token  



# After the user is created, the following event will occur.
# Kullanıcı oluşturulduktan sonra aşağıdaki olay gerçekleşecektir.
@receiver(post_save, sender = User) 

    # instance represents User here. created is False by default, returns True when created.
    # instance Kullanıcıyı temsil eder. oluşturulan varsayılan olarak False'dir, oluşturulduğunda True değerini döndürür.
def crate_Token(sender, instance = None, created = False, **kwargs):  
    if created:
        Token.objects.create(user = instance)

#? Thanks to Signals, we generated tokens when the user registered, so the user did not have to login again after registering.
#! Not: Normally signals are defined in models.py, since we define external, we need to make some changes in apps.py page.
#? Sinyaller sayesinde, kullanıcı kaydolduğunda token ürettik, böylece kullanıcının kaydolduktan sonra tekrar giriş yapmasına gerek kalmadı.
#! Not: Normalde models.py'de sinyaller tanımlıdır, biz harici tanımladığımız için apps.py sayfasında bazı değişiklikler yapmamız gerekiyor.