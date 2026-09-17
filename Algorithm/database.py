from auth import Password_Manager
from algorithms import SearchAlgorithms, SortAlgorithm

class UserDatabase:
	def __init__(self):
		self.users = {}
		self.hash_index = {}

	def register_user(self, username: str, password: str, email: str) -> bool:
		if username in self.users:
			print("Username already exists!")
			return False

		pw_hash, salt = Password_Manager.hash_password(password)

		self.users[username] = {
			"salt" : salt,
			"hash" : pw_hash,
			"email" : email,
		}
		self.hash_index[pw_hash] = username
		print(f"Register Successful! {pw_hash}")
		return True

	def login_user(self, username: str, password: str) -> bool:
		user = SearchAlgorithms.hash_lookup(self.users, username)
		if not user:
			print("Invalid Credentials!")
			return False

		if Password_Manager.verify_password(user["hash"], user["salt"], password):
			print(f"Access Granted! Welcome back, {username}")
			return True
		else:
			print("Invalid Credentials!")
			return False

	def find_user_by_hash(self, hash_bytes: bytes) -> str | None:
		return SearchAlgorithms.hash_lookup(self.hash_index, hash_bytes)

	def list_users_sorted(self) -> list[tuple[str,str]]:
		user_list = [(username, data["email"]) for username, data in self.users.items()]
		return SortAlgorithm.merge_sort(user_list)