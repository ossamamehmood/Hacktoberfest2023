#Password manager By SATYAM NAMDEV and RISHABH SINGH
import hashlib
import os
import sys
import random
import string
import pwinput
from getpass import getpass 		
from tabulate import tabulate
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

class PasswordManager:
	def __init__(self):
		try:
			# passowrds database
			db_handle = open("passwords.db", "rb")
			self.path_to_database = "passwords.db"
		except KeyboardInterrupt:
			sys.exit()
		except:
			self.path_to_database = self.check_database()
			db_handle = open(self.path_to_database, "rb")
		# read decryption key and decrypt database
		self.db_key_hash = db_handle.read(64).decode()
		self.ciphertext = db_handle.read()
		for _ in range(3):
			self.decryption_key = pwinput.pwinput("Decryption key: ")
			self.decryption_key = self.pad_db_key(self.decryption_key)
			# calculate SHA-256 sum for the supplied password
			password_hash = hashlib.sha256(self.decryption_key.encode()).hexdigest()
			# check if they match
			if (self.db_key_hash == password_hash):
				db_handle.close()
				self.decrypt_db()
				break
			else:
				print("\U0000274C Invalid password")


	def decrypt_db(self):
		# decrypt database with AES-CBC
		if len(self.ciphertext.strip()) != 0:
			aes_instance = AES.new(self.decryption_key.encode(), AES.MODE_CBC, self.decryption_key[:16].encode())
			self.content = unpad(aes_instance.decrypt(self.ciphertext), AES.block_size).decode("UTF-8")
			self.records_count = len(self.content.split("|"))
			print("\U00002714 {} records found".format(self.records_count))
		else:
			self.content = ""
			self.records_count = 0
			print("\U0001F5D1 Database has no records")
		self.display_options()


	def save_db(self):
		db_handle = open(self.path_to_database, "wb")
		ciphertext = b""
		if self.records_count != 0:
			# encrypt records with AES-CBC
			aes_instance = AES.new(self.decryption_key.encode(), AES.MODE_CBC, self.decryption_key[:16].encode())
			ciphertext = aes_instance.encrypt(pad(self.content.encode(), AES.block_size))
		db_handle.seek(0)
		db_handle.write(self.db_key_hash.encode() + ciphertext)
		db_handle.close()


	def check_database(self):
		print("> 'passwords.db' not found in current path")
		try:
			for _ in range(3):
				path_to_database = input("> Please enter the absolute path to 'passwords.db' or press enter to create a new database: ")
				path_to_database = "/".join(path_to_database.split("/")[:-1])
				if os.path.exists(path_to_database + "/passwords.db"):
					return path_to_database + "/passwords.db"
				elif path_to_database == "":
					path_to_database = "passwords.db"
					db_handle = open(path_to_database, "wb")
					default_pass = hashlib.sha256(self.pad_db_key("password123").encode()).hexdigest()
					db_handle.write(default_pass.encode())
					db_handle.close()
					print("Default decryption key for database is 'password123'")
					return path_to_database
				else:
					print("\U0001F5D1 Database not found")
		except KeyboardInterrupt:
			sys.exit()



	def show_credentials(self):
		if self.records_count != 0:
			table = self.content.split("|")
			table = [creds.split("-") for creds in table]
			headers = ["id", "username/email", "password", "platform"]
			print(tabulate(table, headers, tablefmt = "grid"))
		else:
			print("\U0001F5D1 Database has no records")


	def add_credentials(self):
		while True:
			new_creds = []
			username_or_email = input("username/email: ")
			password1 = input("password: ")
			password2 = input("retype password: ")
			if password1 != password2:
				print("passwords do not match \U0000274C")
				continue
			platform = input("platform: ")
			if self.records_count == 0:
				new_creds.extend([str(1), username_or_email, password1, platform])
				self.content = "-".join(new_creds)
			else:
				record_id = int(self.content.split("|")[-1].split("-")[0]) + 1
				new_creds.extend([str(record_id), username_or_email, password1, platform])
				self.content = self.content + "|" + "-".join(new_creds)
			self.records_count += 1
			self.save_db()
			print("Record added \U00002714")
			break


	def edit_credentials(self):
		if self.records_count != 0:
			self.show_credentials()
			record_id_to_edit = None
			for _ in range(3):
				try:
					record_id_to_edit = int(input("Record id to edit: "))
				except:
					print("\U0000274C Invalid record id")
					continue
				record_index = self.find_record(record_id_to_edit)
				if record_index != None:
					print("[1] Change username/email")
					print("[2] Change password")
					try:
						option = int(input("> "))
					except:
						print("\U0000274C Invalid option")
						continue
					records = self.content.split("|")
					records = [record.split("-") for record in records]
					if option == 1:
						new_username_or_email = input("New username/email: ")
						records[record_index][1] = new_username_or_email
					elif option == 2:
						new_password = input("New password: ")
						records[record_index][2] = new_password
					else:
						print("\U0000274C Invalid option")
						continue
					records = "|".join(["-".join(record) for record in records])
					self.content = records
					self.save_db()
					print("\U00002714 Record modified")
					break
				else:
					print("\U0001F5D1 Record id not found")
		else:
			print("\U0001F5D1 No records to modify")


	def delete_credentials(self):
		if self.records_count != 0:
			self.show_credentials()
			record_id_to_delete = None
			for _ in range(3):
				try:
					record_id_to_delete = int(input("Record id to delete: "))
				except:
					print("\U0000274C Invalid record id")
					continue
				record_index = self.find_record(record_id_to_delete)
				if record_index != None:
					new_records = self.content.split("|")
					del new_records[record_index]
					self.records_count -= 1
					if self.records_count == 0:
						self.content = ""
					else:
						self.content = "|".join(new_records)
					self.save_db()
					print("\U00002714 Record deleted")
					break
				else:
					print("\U0001F5D1 Record id not found")
		else:
			print("\U0001F5D1 No records to delete")


	def change_db_password(self):
		while True:
			current_password = getpass("Current decryption key: ")
			current_password = self.pad_db_key(current_password)
			current_password_hash = hashlib.sha256(current_password.encode()).hexdigest()
			if current_password_hash != self.db_key_hash:
				print("\U0000274C Current password is incorrect")
				continue
			new_password = pwinput.pwinput("New decryption key: ")
			if len(new_password) < 10:
				print("\U0000274C Password must be at least 10 characters")
				continue
			confirm_new_password = input("Confirm new decryption key: ")
			if new_password != confirm_new_password:
				print("\U0000274C Decryption keys do not match")
				continue
			new_password = self.pad_db_key(new_password)
			new_password_hash = hashlib.sha256(new_password.encode()).hexdigest()
			self.decryption_key = new_password
			self.db_key_hash = new_password_hash
			self.save_db()
			print("\U00002714 Decryption key updated successfully")
			break


	def generate_password(self,l):
		characters = string.ascii_letters + string.digits + string.punctuation
		password = "".join(random.choices(list(characters), k=l))
		print(password)


	def pad_db_key(self, password):
		if len(password) % 16 == 0:
			return password
		else:
			return password + ("0" * (16 - (len(password) % 16)))


	def find_record(self, record_id):
		records = self.content.split("|")
		records = [record.split("-") for record in records]
		for i in range(len(records)):
			if int(records[i][0]) == record_id:
				return i
		return None


	def display_options(self):
		try:
			while True:
				print("[1] Show credentials")
				print("[2] Add credentials")
				print("[3] Edit credentials")
				print("[4] Delete credentials")
				print("[5] Change database password")
				print("[6] Generate password")
				print("[7] Exit")
				option = int(input("> "))
				if option == 1:
					self.show_credentials()
				elif option == 2:
					self.add_credentials()
				elif option == 3:
					self.edit_credentials()
				elif option == 4:
					self.delete_credentials()
				elif option == 5:
					self.change_db_password()
				elif option == 6:
					l = int(input("Enter length of password(for strong password l>8  :) :"))
					self.generate_password(l)
				elif option == 7:
					print("\U0001F44B \U0001F44B That's it ! Goodbye")
					break
				else:
					print("\U0000274C Invalid option")

		except KeyboardInterrupt:
			print()
			print("\U0001F44B Goodbye ")
password_manager = PasswordManager()