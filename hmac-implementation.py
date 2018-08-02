import hashlib
import hmac

h = hmac.new(b'mbghbvkjsc', b'', hashlib.sha3_512)
h.update(b"ASDF1234")
print(h.hexdigest())
h.update(b"neue Nachricht")
print(h.hexdigest())
h.update(b"governor washout beak")
print(h.hexdigest())
