#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

key = b'SEM ZADAJ KLUC'
cipher = Fernet(key)

dirs_to_decrypt = [
    '/home/admin/critical_docs',
    '/home/admin/internal_docs',
    '/home/admin/logs'
]

for directory in dirs_to_decrypt:
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.encrypted'):
                filepath = os.path.join(root, file)
                with open(filepath, 'rb') as enc_file:
                    encrypted_data = enc_file.read()
                decrypted_data = cipher.decrypt(encrypted_data)
                with open(filepath.replace('.encrypted', ''), 'wb') as dec_file:
                    dec_file.write(decrypted_data)
                os.remove(filepath)

print("Súbory úspešne obnovené.")
