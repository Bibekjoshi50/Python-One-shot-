
import qrcode
name = input("enter your name:")

url = "https://technologychannel.org"

img = qrcode.make(url)

img.save(f"{name}.png")

print(f"QR code saved as {name}.png")