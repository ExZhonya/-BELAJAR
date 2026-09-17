import os, secrets
from argon2.low_level import hash_secret_raw, Type


class Password_Manager:
	@staticmethod
	def hash_password(password: str, salt: bytes = None) -> tuple[bytes, bytes]:
		if salt is None:
			salt = os.urandom(32)

		password_hash = hash_secret_raw(
			secret=password.encode('utf-8'),
			salt=salt,
			time_cost=3,
			memory_cost=65536,
			parallelism=4,
			hash_len=32,
			type=Type.ID
		)
		return password_hash, salt

	@staticmethod
	def verify_password(stored_hash: bytes, salt: bytes, password_input: str) -> bool:
		input_hash, _ = Password_Manager.hash_password(password_input, salt=salt)
		return secrets.compare_digest(stored_hash, input_hash)