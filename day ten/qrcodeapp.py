
import qrcode
name = input("Enter your name: ")
img = qrcode.make(name)
type(img) 
img.save(f"{name}.png")