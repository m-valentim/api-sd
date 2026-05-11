from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# 1. Gera a chave privada
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
).decode()

# 2. Gera a chave pública
public_key = private_key.public_key()
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
).decode()

print("--- COPIE O CONTEÚDO ABAIXO PARA O SEU .ENV ---")
print(f'PRIVATE_KEY="{private_pem.strip().replace("\n", "\\n")}"')
print("\n")
print(f'PUBLIC_KEY="{public_pem.strip().replace("\n", "\\n")}"')