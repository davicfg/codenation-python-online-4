class Cesar:
  
  @staticmethod
  def decipher(rotation, text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text = text.lower()
    deciphered = ""

    for letter in text:
      if letter in alphabet:
        position= alphabet.find(letter)
        position= (position - rotation) % 26
        deciphered += alphabet[position]
      else:
        deciphered += letter
    return deciphered

        



