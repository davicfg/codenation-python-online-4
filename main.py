from Cesar import Cesar
from RequestHandler import RequestHandler as rh
import os
import hashlib

get = rh.get_json_cesar("1a6d008f1b4bd19cee0f1cb566dc8374a8f7020b")
deciphered = Cesar().decipher(get["numero_casas"], get["cifrado"])
get["decifrado"] = deciphered
get["resumo_criptografico"] = hashlib.sha1(get["cifrado"].encode('utf-8')).hexdigest()

#save file
f = open("answer.json", "w")
f.write(str(get))
f.close

result = rh.post_file("1a6d008f1b4bd19cee0f1cb566dc8374a8f7020b")

print(result.json())
