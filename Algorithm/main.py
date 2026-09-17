from database import UserDatabase

def main():
	db = UserDatabase()

	print("=== 1. Register User ===")
	db.register_user("zayna", "zayna is my love!", "zayna@lover.com")
	db.register_user("zasdfad", "zayna is my love!", "zayna@lover.com")
	db.register_user("afsdgdshg", "zayna is my love!", "zayna@lover.com")

	print("=== 2. Login User ===")
	db.login_user("zayna", "zayna is my love!")
	db.login_user("zayna", "zayna is my wife!")

	print("=== 3. Search & Sort ===")
	zayna_hash = db.users["zayna"]["hash"]
	print(f"Owner of hash: {db.find_user_by_hash(zayna_hash)}")

	print("\nSorted User:")
	for username, email in db.list_users_sorted():
		print(f" - {username} ({email})")

if __name__ == "__main__":
	main()