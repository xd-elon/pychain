import hashlib
from ecdsa import SigningKey, SECP256k1

# 1. Gerar uma chave privada (256 bits)
private_key = SigningKey.generate(curve=SECP256k1)
private_key_bytes = private_key.to_string()

# 2. Gerar a chave pública correspondente
public_key = private_key.get_verifying_key()
public_key_bytes = public_key.to_string()

# 3. Gerar o endereço aplicando hash na chave pública
# Primeiro, SHA-256 na chave pública
sha256 = hashlib.sha256(public_key_bytes).digest()

# Depois, RIPEMD-160 no hash SHA-256
ripemd160 = hashlib.new('ripemd160')
ripemd160.update(sha256)
address = ripemd160.hexdigest()

print("Chave Privada:", private_key_bytes.hex())
print("Chave Pública:", public_key_bytes.hex())
print("Endereço:", address)