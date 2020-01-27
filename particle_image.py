from PIL import Image
# Settings:
im = Image.open('sugar_line.png')
f = open(r'particle_img.mcfunction', "w")
x, y, z = 0, 100, 0
direction = 'z'
zoom_level = 5
particle_name = "endRod"
# xd yd zd speed amount pattern player
particle_value = "0 0 0 0 1 force"

width, height = im.size[0], im.size[1]
for w in range(0, width):
    for h in range(0, height):
        imgdata = (im.getpixel((w, h)))
        if imgdata[0] == 0:
            if direction == 'z':
                cmd = f'particle {particle_name} {x-w/zoom_level} {y-h/zoom_level} {z} {particle_value}'
                f.write(f'{cmd}\n')
            elif direction == 'y':
                cmd = f'particle {particle_name} {x - w / zoom_level} {y} {z - h / zoom_level} {particle_value}'
                f.write(f'{cmd}\n')
            elif direction == 'x':
                cmd = f'particle {particle_name} {x} {y - h / zoom_level} {z - w / zoom_level} {particle_value}'
                f.write(f'{cmd}\n')
f.close()

