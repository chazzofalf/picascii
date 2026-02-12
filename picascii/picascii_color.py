# Read the Readme.md for instructions!

import PIL
import PIL.Image
import PIL.ImagePalette
import math
import sys
import io
# 🔴🟠🟡🟢🔵🟣⚫⚪🟤

def process(input_file,output_file,max_size):
    
    name=input_file
    size=max_size
    
    img=PIL.Image.open(name)
    img=img.convert(mode='RGB')
    s=img.size
    sc=s[0] if s[0] > s[1] else s[1]
    r=size/sc
    
    s=tuple(math.floor(ss*r) for ss in s)
    img=img.resize(size=s)
    colors = []
    colors.append([248,49,47])   # 🔴
    colors.append([255,103,35])  # 🟠
    colors.append([252,213,63])  # 🟡
    colors.append([0,210,106])   # 🟢
    colors.append([0,116,186])   # 🔵
    colors.append([141,101,197]) # 🟣
    colors.append([0,0,0])       # ⚫
    colors.append([255,255,255]) # ⚪
    colors.append([109,69,52])   # 🟤
    img_pal=PIL.Image.new(mode='RGB',size=(len(colors),1))
    for f in range(0,len(colors)):
        img_pal.putpixel(xy=(f,0),value=tuple(colors[f]))
    #img_pal.show()
    pal_data=[g for f in colors for g in f]
    
    pal=PIL.ImagePalette.ImagePalette(mode='RGB',palette=pal_data)        
    img2=PIL.Image.new('P',img.size)
    img2.putpalette( pal_data)
    img=img.quantize(palette=img2,colors=len(colors))
    #img.show()
    #img=img.quantize(palette=img_pal,dither=PIL.Image.Dither.FLOYDSTEINBERG)
    
    #img=img.convert(mode='P',palette=pal,dither=PIL.Image.Dither.FLOYDSTEINBERG)
    text_map="🔴🟠🟡🟢🔵🟣⚫⚪🟤"
    def index_for_color(color):
        idx=0
        for f in colors:
            if f[0] == color[0] and f[1] == color[1] and f[2] == color[2]:
                return idx
            else:
                idx += 1
        return None
    def debug_pixel(pv):
        #print(pv)
        return pv
    txt='\n'.join(''.join((text_map[debug_pixel(img.getpixel((x,y)))] for x in range(0,img.width))) for y in range(0,img.height))
    
    with io.TextIOWrapper( io.FileIO(file=output_file,mode='w'),encoding='utf8') as bf:
        bf.write(f'{txt}\n')
            




# Charles "chazz_the_intrepid" Timothy Montgomery 2023 
# Use it? Sure! Have Fun. But do please be kind and respectful to others! 
# Want Make something out this as in extend it or put? Well ping me and tell me about it. I would like to be part of the action! 
# Email: chazzofalf@gmail.com 
# discord: chazz_the_intrepid 
# X: chazz_the_intre 
# FB: charles.montgomery3 
# Github: chazzofalf

# If you want any other way of contacting me please just DM me using one of above listed contact methods.
# If you do. Please be prepared to fully identify yourself and explain your desired business with me.