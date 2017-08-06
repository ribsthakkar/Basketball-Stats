from PIL import Image, ImageDraw

courtIm = Image.open('court.png')
draw = ImageDraw.Draw(courtIm)
r=10
draw.ellipse([50-r,200-r,50+r,200+r],fill= 'red')
courtIm.save('test.png')
