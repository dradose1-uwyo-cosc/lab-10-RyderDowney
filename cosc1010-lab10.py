# Ryder Downey
# UWYO COSC 1010
# Submission Date: 11/24/24
# Lab 10
# Lab Section: 14
# Sources, people worked with, help given to: 
# your
# comments
# here

from hashlib import sha256 
from pathlib import Path
#uses given hash function
def get_hash(to_hash):
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()  # Ensure to use .upper() for consistency

#Try/except blocks to read the hash
try:
    with open('hash', 'r') as hash_file: #sets each seperate password in the rockyou file as hash_file to then be checked against stored_hash
        stored_hash = hash_file.read().strip()#reads and strips the hash_file and names it stored_hash for later use
except Exception as e: #accounts for any exception errors the program might come across
    print(f"An error occurred while reading the 'hash' file: {e}")
    exit(1)
#Try/except blocks to read in the data from the rockyou file and to then try to match it to the given stored_hash
try:
    with open('rockyou.txt', 'r') as passwords_file:#opens the rockyou file for usage
        for password in passwords_file:
            password = password.strip()
            if get_hash(password) == stored_hash: #hashes the passwords in rockyou and then matches it with stored_hash
                print(f"Password found: {password}")
                break #exits once correct password is found
        else:
            print("Password not found in the list.") #an externality for if no password is found
except Exception as e: #again accounts for exception errors the program might come across
    print(f"An error occurred while reading the 'rockyou.txt' file: {e}")
