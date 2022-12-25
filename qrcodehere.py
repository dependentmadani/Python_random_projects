import qrcode

img = qrcode.make('https://www.youtube.com/watch?v=Vw0vQa7fpuI')

img.save('thisImg.png')