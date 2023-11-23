import cv2
import os
import string
image = input("Enter the image file name in which you have to encrypt the secret message")
if not os.path.isfile(image):
    print("Image not found")
    exit()
img=cv2.imread(image)
msg = input("Enter secert message")
password = input("Enter password")
def caesar_cipher(text,n):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) - 65 + n) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) - 97 + n) % 26 + 97)
        else:
            encrypted_text += char

    return encrypted_text
encrypted_message = caesar_cipher(msg, 5)
c={}
d={}
def encryption():
    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)
    p,q,r=0,0,0
    for i in range(len(encrypted_message)):
        img[p, q, r] = d[encrypted_message[i]]
        p = p + 1
        q  = q + 1
        r = (r + 1) % 3
    cv2.imwrite("Encryptedmsg.jpg", img)
    os.system("start Encryptedmsg.jpg")
def decryption():
    message = ""
    p,q,r=0,0,0
    pas = input("Enter passcode for Decryption")
    if password == pas:
        for i in range(len(encrypted_message)):
            message = message + c[img[p, q, r]]
            p= p + 1
            q= q+ 1
            r = (r + 1) % 3
        new=caesar_cipher(message,-5)
        print("Decryption message",new )
    else:
        print("Not valid key")
encryption()
decryption()





