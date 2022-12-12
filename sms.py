import subprocess
import random
import string

# rasgele 7 karakterli bir dize oluştur
letters = string.ascii_uppercase
sms = ( ''.join(random.choice(letters) for i in range(7)) )


# SMS Message Template (try to keep to within 150 characters)
smsmessage = ("BAGLAN4GB " + sms)

# Use Subprocess Run Function to send SMS
subprocess.run(["termux-sms-send", "-n", "2200", smsmessage])

# Print confirmation of each send
print(smsmessage)


# Print end of process message
print("İşlem tamamlandı.")





