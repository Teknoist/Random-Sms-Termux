import subprocess
import random

# Adres defterine kayıtlar ekleyin Key = İsim, Value = Telefon Numarası
addressbook = {"Name1" : "2200"
                }
# rasgele 7 karakterli bir dize oluştur
sms = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

# Loop through the addressbook dictionary and send each number the message
for (c,v) in addressbook.items():
    
    # SMS Message Template (try to keep to within 150 characters)
    smsmessage = str("BAGLAN4GB " + sms)
    
    # Use Subprocess Run Function to send SMS
    subprocess.run(["termux-sms-send", "-n", phonenumber, smsmessage])
    
    # Print confirmation of each send
    print("Sent Message to " + k + " via " + v)


# Print end of process message
print("Message sending complete")






