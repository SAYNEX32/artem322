from PIL import Image, ImageDraw

im = Image.new('RGB',(1280, 720),(0, 0, 90))
draw = ImageDraw.Draw(im)




draw.rectangle((0, 400, 1280, 720), fill='lightsteelblue', outline=(255, 255, 255))   # земля

draw.ellipse((-70, -70, 200, 200), fill=(240, 248, 255), outline=(0, 0, 0))
draw.polygon((74, 138, 82, 120, 102, 110, 119, 107, 117, 125, 98, 142), fill=(205, 201, 201), outline='black')
draw.polygon((102, 84, 85, 79, 75, 57, 83, 13, 103, 10, 118, 37, 117, 63), fill=(205, 201, 201), outline='black')
draw.polygon((5, 20, 42, 17, 33, 56, 3, 67, -10, 15), fill=(205, 201, 201), outline='black')
draw.ellipse((10, 10, 30, 30), fill=(240, 248, 255), outline=(0, 0, 0))
draw.ellipse((13, 40, 28, 55), fill=(240, 248, 255), outline=(0, 0, 0))

draw.ellipse((350, 420, 600, 655), fill='lightgrey', outline=(0, 0, 0)) # нижний шарик

draw.ellipse((500, 580, 600, 675), fill='lightgrey', outline=(0, 0, 0))   #правый ножка
draw.ellipse((330, 580, 430, 675), fill='lightgrey', outline=(0, 0, 0))   #левый ножка

draw.line((550, 350, 720, 250), fill=(139, 80, 0), width=10)   #правый ручка
draw.line((680, 270, 720, 280), fill=(139, 80, 0), width=6)

draw.line((215, 270, 385, 370), fill=(139, 80, 0), width=10)   #левый ручка
draw.line((215, 300, 275, 305), fill=(139, 80, 0), width=6)
draw.line((270, 280, 320, 330), fill=(139, 80, 0), width=6)


draw.ellipse((370, 250, 580, 440), fill='lightgrey', outline=(0, 0, 0))   #средний шарик

draw.ellipse((467, 280, 483, 296), fill='black', outline=(0, 0, 0))
draw.ellipse((467, 340, 483, 356), fill='black', outline=(0, 0, 0))    #кружочки в центре
draw.ellipse((467, 395, 483, 411), fill='black', outline=(0, 0, 0))


draw.ellipse((400, 120, 550, 260), fill='lightgrey', outline=(0, 0, 0))   #верхний шарик

draw.ellipse((425, 210, 435, 220), fill='black', outline=(0, 0, 0))
draw.ellipse((440, 223, 450, 233), fill='black', outline=(0, 0, 0))
draw.ellipse((467, 230, 477, 240), fill='black', outline=(0, 0, 0))     #улыбка)
draw.ellipse((492, 225, 502, 235), fill='black', outline=(0, 0, 0))
draw.ellipse((510, 213, 520, 223), fill='black', outline=(0, 0, 0))

draw.polygon((472, 184, 472, 198, 511, 187), fill=(231, 121, 66), outline='black')

draw.ellipse((440, 160, 450, 170), fill='black', outline=(0, 0, 0))    #Левый глаз
draw.ellipse((500, 160, 510, 170), fill='black', outline=(0, 0, 0))    #правый глаз

draw.line((650, 670, 650, 250), fill=(139, 37, 0), width=12)
draw.line((618, 245, 605, 120), fill=(218, 165, 32), width=4)
draw.rectangle((615, 122, 620, 245), fill=(218, 165, 32), outline=(0, 0, 0))
draw.rectangle((635, 122, 640, 245), fill=(218, 165, 32), outline=(0, 0, 0))
draw.rectangle((655, 122, 660, 245), fill=(218, 165, 32), outline=(0, 0, 0))
draw.rectangle((625, 115, 630, 245), fill=(218, 165, 32), outline=(0, 0, 0))
draw.rectangle((662, 110, 667, 245), fill=(218, 165, 32), outline=(0, 0, 0))
draw.rectangle((670, 122, 675, 245), fill=(218, 165, 32), outline=(0, 0, 0))
draw.rectangle((622, 130, 627, 245), fill=(218, 165, 32), outline=(0, 0, 0))
draw.rectangle((640, 130, 645, 245), fill=(218, 165, 32), outline=(0, 0, 0))
draw.rectangle((648, 130, 653, 245), fill=(218, 165, 32), outline=(0, 0, 0))
draw.rectangle((680, 125, 685, 245), fill=(218, 165, 32), outline=(0, 0, 0))
draw.rectangle((631, 142, 636, 245), fill=(218, 165, 32), outline=(0, 0, 0))
draw.line((682, 245, 695, 120), fill=(218, 165, 32), width=4)
draw.line((662, 245, 680, 115), fill=(218, 165, 32), width=4)
draw.rectangle((613, 240, 687, 252), fill=(139, 37, 0), outline=(0, 0, 0))     #венек
draw.rectangle((613, 240, 687, 245), fill=(110, 123, 139), outline=(0, 0, 0))

draw.polygon((977, 468, 962, 545, 988, 550, 1021, 549, 1053, 540, 1037, 470), fill=(139, 69, 19), outline='black')#елочка
draw.polygon((781, 379, 801, 410, 863, 448, 923, 473, 972, 480, 1048, 480, 1107, 471, 1159, 452, 1196, 427, 1224, 400, 1237, 370, 1214, 378, 1187, 394, 1151, 402, 1125, 401, 1093, 399, 1069, 390, 1054, 380, 1049, 356, 1003, 357, 992, 382, 973, 399, 952, 405, 915, 406, 870, 399, 834, 389, 807, 383), fill=(47, 79, 79), outline='black')
draw.polygon((855, 290, 871, 324, 894, 356, 923, 371, 966, 379, 1017, 382, 1085, 382, 1145, 361, 1176, 317, 1186, 281, 1174, 295, 1160, 306, 1141, 320, 1109, 336, 1075, 333, 1052, 323, 1044, 294, 1017, 293, 1007, 325, 992, 335, 966, 338, 932, 331, 910, 320, 885, 307), fill=(47, 79, 79), outline='black')
draw.polygon((906, 251, 934, 277, 964, 292, 996, 301, 1030, 304, 1071, 298, 1098, 289, 1129, 276, 1146, 253, 1126, 261, 1106, 267, 1087, 271, 1074, 275, 1059, 272, 1050, 262, 1044, 239, 1018, 238, 1012, 263, 999, 274, 976, 274, 957, 271, 933, 261), fill=(47, 79, 79), outline='black')
draw.polygon((958, 220, 976, 232, 1001, 243, 1031, 247, 1061, 245, 1083, 237, 1103, 222, 1083, 220, 1068, 217, 1051, 209, 1041, 197, 1034, 182, 1024, 197, 1012, 208, 994, 214, 975, 218), fill=(47, 79, 79), outline='black')

im.show()