#Functions 
import math
from art import logo


#Challenge Caeser Cipher ------------------------

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z']
end_Code = True

while end_Code:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your encode message:\n".lower())
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26

  def Ceaser(start_text, shift_amount, cipher_direction):
      end_text = ""

      if cipher_direction == "decode":
              shift_amount *= -1
        
      for letter in start_text:

        if letter in alphabet:
            
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        
        else:
            end_text += letter
      
      print(f"the encoded text is {end_text}")
  
  Ceaser(start_text=text, shift_amount=shift, cipher_direction=direction)
  result =  input("Type 'yes' if you want to go again. Otherwise type 'no' \n")

if result == "no":
    end_Code = False
    print("Goodbye")


