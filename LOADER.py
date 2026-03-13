
import marshal, base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

KEY = b'16byteslongkey!!'
IV = b'16byteslongiv!!!'

with open("/storage/emulated/0/PROJECT-2026/PHANTOM-GLORY/PHANTOM-4th/GLORY.py", "r") as f:
    encrypted = base64.b64decode(f.read())

cipher = AES.new(KEY, AES.MODE_CBC, IV)
decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)

code_obj = marshal.loads(decrypted)
exec(code_obj)
