import subprocess
import random
import string


# Kullanıcıdan kaç kere tekrar edileceğini sor
tekrar_sayisi = int(input("Kaç kere tekrar edilsin? "))

# Belirtilen sayıda tekrar edilen döngü
for i in range(tekrar_sayisi):
  # rasgele 7 karakterli bir dize oluştur
  letters = string.ascii_uppercase
  sms = ( ''.join(random.choice(letters) for i in range(7)) )
  smsmessage = ("BAGLAN4GB " + sms)
  # Use Subprocess Run Function to send SMS
  subprocess.run(["termux-sms-send", "-n", "2200", "-s", "1", smsmessage])
  # Print confirmation of each send
  print(smsmessage)
