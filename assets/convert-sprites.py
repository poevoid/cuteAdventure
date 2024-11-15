from PIL import Image
import os

def get_shade(rgba, shades, shade):
    w = (254 + shades) // shades
    b = (shade + 1) * w
    return 1 if rgba[0] >= b else 0

def get_mask(rgba):
    return 1 if rgba[3] >= 128 else 0

def convert_impl(fname, shades, sw = None, sh = None, num = None):

    if not (shades >= 2 and shades <= 4):
        print('shades argument must be 2, 3, or 4')
        return None

    print('Converting:', fname)

    im = Image.open(fname).convert('RGBA')
    pixels = list(im.getdata())
    
    masked = False
    for i in pixels:
        if i[3] < 255:
            masked = True
            break
    
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
    
def convert_header(fname, fout, sym, shades, sw = None, sh = None, num = None):
    bytes = convert_impl(fname, shades, sw, sh, num)
    if bytes is None: return
    with open(fout, 'w') as f:
       
        f.write('uint8_t %s[] =\n{\n' % sym)
        for n in range(len(bytes)):
            if n % 16 == 0:
                f.write('    ')
            f.write('%3d,' % bytes[n])
            f.write(' ' if n % 16 != 15 else '\n')
        if len(bytes) % 16 != 0:
            f.write('\n')
        f.write('};\n')

def convert_bin(fname, fout, shades, sw = None, sh = None, num = None):
    bytes = convert_impl(fname, shades, sw, sh, num)
    if bytes is None: return
    with open(fout, 'wb') as f:
        f.write(bytes)

def convert(fout, sym, fname, sw, sh, num = None):
    if fout[-4:] == '.bin':
        convert_bin(fname, fout, 4, sw, sh, num)
    else:
        convert_header(fname, fout, sym, 4, sw, sh, num)


def deleteFile(filename):
    if os.path.isfile(filename):
        os.remove(filename)

bw = '_bw'
bw = ''
BASE = '../'
IMAGES = '../images/'

deleteFile(BASE + 'Images.hpp')

#convert_header(IMAGES + 'PPOT.png', BASE + 'Images.hpp', 'PPOT', 4, 128, 64)

# add more images ..

convert_header(IMAGES + 'dpad_64x16.png', BASE + 'Images.hpp', 'dpad', 4, 16, 16)
convert_header(IMAGES + 'abutton_16x16.png', BASE + 'Images.hpp', 'abutton', 4, 16, 16)
convert_header(IMAGES + 'bbutton.png', BASE + 'Images.hpp', 'bbutton', 4, 16, 16)
convert_header(IMAGES + 'catg_64x64.png', BASE + 'Images.hpp', 'catg', 4, 64, 64)


convert_header(IMAGES + 'idleleft_32x32.png', BASE + 'Images.hpp', 'idlelsmall', 4, 32, 32)
convert_header(IMAGES + 'idleu_32x32.png', BASE + 'Images.hpp', 'idleusmall', 4, 32, 32)
convert_header(IMAGES + 'idlef_32x32.png', BASE + 'Images.hpp', 'idlefsmall', 4, 32, 32)
convert_header(IMAGES + 'walkf_32x32.png', BASE + 'Images.hpp', 'walkfsmall', 4, 32, 32)
convert_header(IMAGES + 'idleright_32x32.png', BASE + 'Images.hpp', 'idlersmall', 4, 32, 32)
convert_header(IMAGES + 'walkleft_32x32.png', BASE + 'Images.hpp', 'walkleftsmall', 4, 32, 32)
convert_header(IMAGES + 'walkright_32x32.png', BASE + 'Images.hpp', 'walkrightsmall', 4, 32, 32)

convert_header(IMAGES + 'idleleft_64x64.png', BASE + 'Images.hpp', 'idlel', 4, 64, 64)
convert_header(IMAGES + 'idleu_64x64.png', BASE + 'Images.hpp', 'idleu', 4, 64, 64)
convert_header(IMAGES + 'walkf_64x64.png', BASE + 'Images.hpp', 'walkf', 4, 64, 64)
convert_header(IMAGES + 'walkleft_64x64.png', BASE + 'Images.hpp', 'walkleft', 4, 64, 64)
convert_header(IMAGES + 'walkright_64x64.png', BASE + 'Images.hpp', 'walkright', 4, 64, 64)
convert_header(IMAGES + 'idleright_64x64.png', BASE + 'Images.hpp', 'idler', 4, 64, 64)
convert_header(IMAGES + 'idlef_64x64.png', BASE + 'Images.hpp', 'idlef', 4, 64, 64)


convert_header(IMAGES + 'test_32x32.png', BASE + 'Images.hpp', 'test', 4, 32, 32)
#convert_header(IMAGES + 'idlesheet_64x64.png', BASE + 'Images.hpp', 'idle', 4, 64, 64)

