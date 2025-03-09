

import qrcode
name = input("Enter your name: ")
img = qrcode.make("https://technologychannel.org")
type(img) 
img.save(f"{name}.png")