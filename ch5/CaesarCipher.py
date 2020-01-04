class CaesarCipher:
  def __init__(self, shift):
    encoder = [None]*26
    decoder = [None]*26
    for k in range(26):
      encoder[k] = chr((k+shift)%26 + ord('A'))
      decoder[k] = chr((k-shift)%26 + ord('A'))
    self._forward = ''.join(encoder)
    self._backward = ''.join(decoder)
    print(self._forward)
    print(self._backward)
  
  def encrypt(self, message):
    return self._transform(message, self._forward)

  def decrypt(self, secret):
    return self._transform(secret, self._backward)

  def _transform(self, original, code):
    msg = list(original)
    for k in range(len(msg)):
      if msg[k].isupper():
        j = ord(msg[k]) - ord('A')
        msg[k] = code[j]
    return ''.join(msg)

class CaesarCipher2:
  def __init__(self, shift):
    self._shift = shift
  
  def encrypt(self, message):
    encoded = []
    for letter in message:
      if letter.isupper():
        encoded.append(chr(ord('A') + (ord(letter) - ord('A') + self._shift) % 26))
      else:
        encoded.append(letter)
    return ''.join(encoded)

  def decrypt(self, message):
    pass

if __name__ == '__main__':
  cipher = CaesarCipher(3)
  message = 'the quick brown fox jumps over the lazy dog'
  message = message.upper()
  coded = cipher.encrypt(message)
  print('secret:', coded)
  answer = cipher.decrypt(coded)
  print('message:', answer)

  cipher2 = CaesarCipher2(3)
  message = 'the quick brown fox jumps over the lazy dog'
  message = message.upper()
  coded = cipher2.encrypt(message)
  print('secret:', coded)