from caesar_cipher.corpus_loader import word_list, name_list
import re



def encrypt(plain_text, shift):
    encrypted_text = ""

    for char in plain_text:
        # Check if the character is a letter
        if char.isalpha():
            # Determine the shift amount based on the character case
            if char.islower():
                shift_amount = (ord(char) - ord('a') + shift) % 26
                encrypted_char = chr(ord('a') + shift_amount)
            else:
                shift_amount = (ord(char) - ord('A') + shift) % 26
                encrypted_char = chr(ord('A') + shift_amount)
        else:
            # Non-alphabetic characters remain unchanged
            encrypted_char = char

        encrypted_text += encrypted_char

    return encrypted_text
    

def decrypt(encoded, shift):
    return encrypt(encoded, -shift)

def count_words(text):
    potential_words = text.split()
    word_count = 0
    for potential_word in potential_words:
      word = re.sub(r'[^A-Za-z]+', '', potential_word)
      if word.lower() in word_list or word in name_list:
        word_count += 1
      else: 
        pass
    return word_count

def crack(encrypted_text):
    phrase_list = []
    for shift in range(26):
        phrase_list.append(decrypt(encrypted_text, shift))
        # counter = 0
        # decrypted_text = decrypt(encrypted_text, shift)
        # text_list = decrypted_text.split()
        for phrase in phrase_list:
            # print('word ', word)
            # if word.lower() in name_list or word.lower() in word_list:
            #     counter += 1
            word_count = count_words(phrase)
            percentage = int(word_count / len(phrase.split()) * 100)
            if percentage > 50:
                return phrase
    return ''

    # for shift in range(26):
    #     counter = 0
    #     decrypted_text = encrypt(encrypted_text, shift)
    #     if decrypted_text.split() in name_list:
    #         break
    # return decrypted_text

# if __name__ == '__main__':
#    encrypted = encrypt("It was the best of times, it was the worst of times.", 5)
#    print(encrypted)  # Output: "Ny bfx ymj gjxy tk ynrjx, ny bfx ymj btwxy tk ynrjx."