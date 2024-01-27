import qrcode as qr

img = qr.make("https://www.youtube.com/results?search_query=chai+aur+code")

img.save("chai_aur_code.png")
