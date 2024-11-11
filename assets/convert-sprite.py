from PIL import Image
import os
from pathlib import Path

def get_shade(rgba, shades, shade):
    w = (254 + shades) // shades
    b = (shade + 1) * w
    return 1 if rgba[0] >= b else 0

def get_mask(rgba):
    return 1 if rgba[3] >= 128 else 0

def convert(fname, shades, sw = None, sh = None, num = None, maskImage = False):

    if not (shades >= 2 and shades <= 4):
        print('shades argument must be 2, 3, or 4')
        return None

    im = Image.open(fname).convert('RGBA')
    pixels = list(im.getdata())
    
    masked = maskImage
    q = 0
    for i in pixels:
        q = q + 1
        # print(i[0])
        # print(i[1])
        # print(i[2])
        # print(i[3])
        if i[3] < 255:
            # print('masked!!! ')
            # print(q)
            masked = True
            # exit()
            break

    print('{}, shades {}, masked {}'.format(fname, shades, masked))


    w = im.width
    h = im.height
    if sw is None: sw = w
    if sh is None: sh = h
    nw = w // sw
    nh = h // sh
    if num is None: num = nw * nh
    sp = (sh + 7) // 8
    
    if nw * nh <= 0:
        print('%s: Invalid sprite dimensions' % fname)
        return None
        
    bytes = bytearray([sw, sh])
    
    for n in range(num):
        bx = (n % nw) * sw
        by = (n // nw) * sh
        for shade in range(shades - 1):
            for p in range(sp):
                for ix in range(sw):
                    x = bx + ix
                    byte = 0
                    mask = 0
                    for iy in range(8):
                        y = p * 8 + iy
                        if y >= sh: break
                        y += by
                        i = y * w + x
                        rgba = pixels[i]
                        byte |= (get_shade(rgba, shades, shade) << iy)
                        mask |= (get_mask(rgba) << iy)
                    bytes += bytearray([byte])
                    if masked:
                        bytes += bytearray([mask])
    
    return bytes
    
def convert_header(fname, fout, sym, shades, sw = None, sh = None, num = None, maskImage = False):
    bytes = convert(fname, shades, sw, sh, num, maskImage)
    if bytes is None: return
    with open(fout, 'a') as f:
        # f.write('#pragma once\n\n#include <stdint.h>\n#include <avr/pgmspace.h>\n\n')
        # f.write('constexpr uint8_t %s[] PROGMEM =\n{\n' % sym)
        f.write('uint8_t %s[] = {\n  ' % sym)
        for n in range(len(bytes)):
            if n % 16 == 2:
                f.write('\n  ')
            f.write('%3d,' % bytes[n])
            # f.write(' ' if n % 16 != 15 else '\n')
            # f.write(' ' if n % 18 != 2 else '\n')
            f.write(' ')
        if len(bytes) % 16 != 2:
            f.write('\n')
        f.write('};\n\n')

def deleteFile(filename):
    if os.path.isfile(filename):
        os.remove(filename)

BASE = '../'
IMAGES = '../images/'

deleteFile(BASE + 'Images.hpp')

#convert_header(IMAGES + 'PPOT.png', BASE + 'Images.hpp', 'PPOT', 4, 128, 64)

# add more images ..

convert_header(IMAGES + 'dpad_64x16.png', BASE + 'Images.hpp', 'dpad', 4, 16, 16)
convert_header(IMAGES + 'abutton_16x16.png', BASE + 'Images.hpp', 'abutton', 4, 16, 16)
convert_header(IMAGES + 'bbutton.png', BASE + 'Images.hpp', 'bbutton', 4, 16, 16)
convert_header(IMAGES + 'catg_64x64.png', BASE + 'Images.hpp', 'catg', 4, 64, 64)


convert_header(IMAGES + 'grayl_32x32.png', BASE + 'Images.hpp', 'graylsmall', 4, 32, 32)
convert_header(IMAGES + 'grayu_32x32.png', BASE + 'Images.hpp', 'grayusmall', 4, 32, 32)
convert_header(IMAGES + 'graysheet_32x32.png', BASE + 'Images.hpp', 'grayfsmall', 4, 32, 32)
convert_header(IMAGES + 'walkf_32x32.png', BASE + 'Images.hpp', 'graywalkfsmall', 4, 32, 32)
convert_header(IMAGES + 'grayr_32x32.png', BASE + 'Images.hpp', 'grayrsmall', 4, 32, 32)
convert_header(IMAGES + 'graywalkleft_32x32.png', BASE + 'Images.hpp', 'graywalkleftsmall', 4, 32, 32)

convert_header(IMAGES + 'grayl_64x64.png', BASE + 'Images.hpp', 'grayl', 4, 64, 64)
convert_header(IMAGES + 'grayu_64x64.png', BASE + 'Images.hpp', 'grayu', 4, 64, 64)
convert_header(IMAGES + 'graywalkf_64x64.png', BASE + 'Images.hpp', 'graywalkf', 4, 64, 64)
convert_header(IMAGES + 'graywalkleft_64x64.png', BASE + 'Images.hpp', 'graywalkleft', 4, 64, 64)
convert_header(IMAGES + 'grayr_64x64.png', BASE + 'Images.hpp', 'grayr', 4, 64, 64)
convert_header(IMAGES + 'graysheet_64x64.png', BASE + 'Images.hpp', 'grayf', 4, 64, 64)

#convert_header(IMAGES + 'idlesheet_64x64.png', BASE + 'Images.hpp', 'idle', 4, 64, 64)



