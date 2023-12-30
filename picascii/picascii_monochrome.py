# Read the Readme.md for instructions!
# See installation instructions in Readme or picascii2.py # This is picascii2.py's less interesting monochrome (was butterfly ridden, but user now gets to pick the symbol if they want) original stepbrother.
import PIL
import PIL.Image
import PIL.ImagePalette
import math
import sys
import io
def process(input_file,output_file,max_size,bright_mark='⚪',dark_mark='⚫'):   
    #name=sys.argv[1]
    
    
    img=PIL.Image.open(input_file)
    
    s=img.size
    sc=s[0] if s[0] > s[1] else s[1]
    r=max_size/sc
    
    s=tuple(math.floor(ss*r) for ss in s)
    img=img.resize(size=s)        
    img=img.convert(mode='1',dither=PIL.Image.Dither.FLOYDSTEINBERG)
    
    txt='\n'.join(''.join((bright_mark if img.getpixel((x,y))==255 else dark_mark for x in range(0,img.width))) for y in range(0,img.height))
    
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
