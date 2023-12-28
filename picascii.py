# See installation instructions in Readme or picascii2.py # This is picascii2.py's last interesting butterfly ridden original stepbrother.
import PIL
import PIL.Image
import PIL.ImagePalette
import math
import sys
import io
def main():
    if len(sys.argv) == 3:
        name=sys.argv[1]
        size=int(sys.argv[2])
        
        img=PIL.Image.open(name)
        
        s=img.size
        sc=s[0] if s[0] > s[1] else s[1]
        r=size/sc
        
        s=tuple(math.floor(ss*r) for ss in s)
        img=img.resize(size=s)        
        img=img.convert(mode='1',dither=PIL.Image.Dither.FLOYDSTEINBERG)
        
        txt='\n'.join(''.join(('🦋' if img.getpixel((x,y))==255 else '⚫' for x in range(0,img.width))) for y in range(0,img.height))
        
        with io.TextIOWrapper( io.FileIO(file=f'{name}.txt',mode='w'),encoding='utf8') as bf:
            bf.write(f'{txt}\n')
            

if __name__=='__main__':
    main()
    
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
