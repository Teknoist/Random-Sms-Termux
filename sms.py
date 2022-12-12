import subprocess
import random

# rasgele 7 karakterli bir dize oluştur
letters = string.ascii_uppercase
print ( ''.join(random.choice(letters) for i in range(7)) )

# SMS Message Template (try to keep to within 150 characters)
smsmessage = ("BAGLAN4GB " + sms)

# Use Subprocess Run Function to send SMS
subprocess.run(["termux-sms-send", "-n", "2200", smsmessage])

# Print confirmation of each send
print(""smsmessage" 2200 numarasına yollandı.)


# Print end of process message
print("İşlem tamamlandı.")






