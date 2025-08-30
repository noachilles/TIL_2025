import hashlib
import os

def hash_password(password, salt):    
    # salt와 결합하여 해시 객체 생성
    password_bytes = password.encode('utf-8')
    hash_obj = hashlib.sha256(salt + password_bytes)
    
    # 해시 값을 16진수 문자열로 변환하여 반환
    hash_digest = hash_obj.hexdigest()
    return hash_digest

def verify_password(stored_salt, stored_hash, password_to_check):
    password_bytes = password_to_check.encode('utf-8')
    hash_obj = hashlib.sha256(stored_salt + password_bytes)
    computed_hash = hash_obj.hexdigest()
    return computed_hash == stored_hash

# salt
salt = '소금'.encode('utf-8')
password = "defaultPassword123"

# 비밀번호 해시 생성
hashed_password = hash_password(password, salt)
print("생성된 해시 값:", hashed_password)

# 맞는 비밀번호 검증
is_valid = verify_password(salt, hashed_password, "defaultPassword123")
print(is_valid)

# 틀린 비밀번호 검증
is_valid = verify_password(salt, hashed_password, "wrongpassword")
print(is_valid)
