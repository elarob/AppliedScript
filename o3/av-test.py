#!/usr/bin/env python3
import os 	# fil- och kataloghantering
import time		# tidsfördröjning för AV/EDR
import platform 	# identfiera operativsystem
import sys		# för sys.exit()


# Kontrollera operativsystem
system = platform.system()
print(f"Operativsystem: {system}")

if system == "Windows":
	print("Windows upptäckt. Scriptet fortsätter...")
elif system == "Linux":
	print("Linux upptäckt. Detta script är avsett för Windows.")
	sys.exit(1) # avslutar med felkod
elif system == "Darwin":
	print("macOS upptäckt. Detta script är avsett för Windows.")
	sys.exit(1) # avslutar med felkod

else:
	print(f"Okänt operativsystem ({system}). Detta script är avsett för Windows. Avbryter körning.")
	sys.exit(1) # avslutar med felkod



# EICAR antivirus test string (ofarlig)
eicar_str = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"


# Skapa fil i användarens hemkatalog
filename = "eicar_test.txt"
filepath = os.path.join(os.path.expanduser("~"), filename)
print(f"Skapar testfil: {filepath}")

# Skriv testfil
try:
	with open(filepath, "w") as f:
		f.write(eicar_str)
	print("EICAR testfil skapad.")
except Exception as e:
	print("Kunde inte skapa filen.")
	print(e)
	sys.exit(1)

# Fördröjning - vänta på AV/EDR-respons
print("Väntar 3 sekunder för eventuell AV-reaktion...")
time.sleep(3)

# Kontrollera om filen finns
try:
	with open(filepath, "r", encoding="ascii") as f:
		file_content = f.read()

	if file_content == eicar_str:
		print("Filen finns kvar och innehållet matchar EICAR-signaturen.")
		print("Antivirus har inte blockerat filen")

	else:
		print("Filen finns kvar men innehållet har ändrats")

except Exception:
	print("Filen kunde inte läsas.")
	print("AV/EDR har troligen tagit bort eller karantänsatt filen.")
	print("Din AV/EDR-lösning fungerar som förväntat.")