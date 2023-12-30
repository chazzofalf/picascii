# Read the Readme.md for instructions!
import sys
try:
    import picascii.goofy_modes as gm
except:
    try:
        import picascii.goofy_modes as gm
    except:
        exit(1)
try:
    import picascii1 as p1
except:
    try:
        import picascii.picascii1 as p1
    except:
        exit(1)

try:
    import picascii2 as p2
except:
    try:
        import picascii.picascii2 as p2
    except:
        exit(1)

def main():        
    is_valid=True
    is_monochrome=False
    is_with_color=False
    user_needs_help=False
    mono_bright_color_symbol='⚪'
    mono_dark_color_symbol='⚫'
    mono_bright_color_symbol_set=False
    mono_dark_color_symbol_set=False
    mono_bright_color_symbol_parse_mode=False
    mono_dark_color_symbol_parse_mode=False
    input_file_parse_mode=False
    output_file_parse_mode=False
    max_side_size_parse_mode=False
    input_file=None
    output_file=None
    max_side_size=None
    # Parse the user supplied command line arguments.
    for f in sys.argv[1:]:
        if not mono_bright_color_symbol_parse_mode and not mono_dark_color_symbol_parse_mode and not input_file_parse_mode and not output_file_parse_mode and not max_side_size_parse_mode:
            if f == '--monochrome':
                if not is_with_color:
                    is_monochrome=True
                else:
                    is_valid=False
                    sys.stderr.write('You have already selected mode --with-colors. Choose one and only one.\n')
                    break
            elif f == '--with-colors':
                if not is_monochrome:
                    is_with_color=True
                else:
                    is_valid=False
                    sys.stderr.write('You have already selected mode --monochrome. Choose one and only one.\n')
                    break
            elif f == '--bright-symbol':
                if is_monochrome and not mono_bright_color_symbol_set:
                    mono_bright_color_symbol_parse_mode=True
                else:
                    is_valid=False
                    sys.stderr.write('You have already selected a bright symbol. Choose one and only one.\n')
                    break
            elif f == '--dark-symbol':
                if is_monochrome and not mono_dark_color_symbol_set:
                    mono_dark_color_symbol_parse_mode=True
                else:
                    is_valid=False
                    sys.stderr.write('You have already selected a dark symbol. Choose one and only one.\n')
                    break
            elif f == '--help':
                user_needs_help=True
                break
            elif f == '--input-file':
                if input_file is None:
                    input_file_parse_mode=True
                else:
                    is_valid=False
                    sys.stderr.write('You have already selected an input file. Choose one and only one.\n')
                    break
            elif f == '--output-file':
                if output_file is None:
                    output_file_parse_mode=True
                else:
                    is_valid=False
                    sys.stderr.write('You have already selected an output file. Choose one and only one.\n')
                    break
            elif f == '--max-side-size':
                if max_side_size is None:
                    max_side_size_parse_mode=True
                else:
                    is_valid=False
                    sys.stderr.write('You have already selected maximum edge length. Choose one and only one.\n')
                    break
            elif gm.has_goofy_mode(mode=f):
                if not is_with_color and not mono_bright_color_symbol_set and not mono_dark_color_symbol_set:
                    (mono_bright_color_symbol,mono_dark_color_symbol) = gm.get_goofy_mode_symbols(mode=f)
                    mono_bright_color_symbol_set = True
                    mono_dark_color_symbol_set = True
                    is_monochrome = True
                else:
                    is_valid=False
                    sys.stderr.write('Something bad has happened here. Check your options.\n')
                    break
            else:
                is_valid=False
                sys.stderr.write('This argument does not make sense.\n')
                break
        elif mono_bright_color_symbol_parse_mode:
            if len(f) == 1:
                mono_bright_color_symbol=f
                mono_bright_color_symbol_set=True
                mono_bright_color_symbol_parse_mode=False
            else:
                is_valid=False
                sys.stderr.write(f'A mark \'{f}\' can only have the length of one character\n')
                break
        elif mono_dark_color_symbol_parse_mode:
            if len(f) == 1:
                mono_dark_color_symbol=f
                mono_dark_color_symbol_set=True
                mono_dark_color_symbol_parse_mode=False
            else:
                is_valid=False
                sys.stderr.write(f'A mark \'{f}\' can only have the length of one character\n')
                break
        elif input_file_parse_mode:
            input_file=f
            input_file_parse_mode=False
        elif output_file_parse_mode:
            output_file=f
            output_file_parse_mode=False
        elif max_side_size_parse_mode:
            try:
                max_side_size=int(f)
                max_side_size_parse_mode=False
            except:
                is_valid=False
                sys.stderr.write('The side length must be an integer.\n')                
                break
            
    sys.stderr.write('Current requested settings were:\n')
    sys.stderr.write(f'--monochrome={is_monochrome}\n')
    sys.stderr.write(f'--with-colors={is_with_color}\n')
    sys.stderr.write(f'--input-file={input_file}\n')
    sys.stderr.write(f'--output-file={output_file}\n')
    sys.stderr.write(f'--max-side-size={max_side_size}\n')
    if not ((is_monochrome or is_with_color) and input_file is not None and output_file is not None and max_side_size is not None):
        sys.stderr.write('You did not fill out all the necessary options\n')
        sys.stderr.write('Current requested settings were:\n')
        sys.stderr.write(f'--monochrome={is_monochrome}\n')
        sys.stderr.write(f'--with-colors={is_with_color}\n')
        sys.stderr.write(f'--input-file={input_file}\n')
        sys.stderr.write(f'--output-file={output_file}\n')
        sys.stderr.write(f'--max-side-size={max_side_size}\n')
        
        
        is_valid = False
    
    if not is_valid:
        user_needs_help=True
        sys.stderr.write('The arguments that you supplied will not work. Please review and correct them and try again.\n')
        sys.stderr.write(f'Those arguments are: {sys.argv[1:]}\n')
    if user_needs_help:        
        help_the_user()
    else:
        if is_monochrome:
            p1.process(input_file=input_file,output_file=output_file,max_size=max_side_size,bright_mark=mono_bright_color_symbol,dark_mark=mono_dark_color_symbol)
        else:
            p2.process(input_file=input_file,output_file=output_file,max_size=max_side_size)
def help_the_user():
    help_text='''
You invoke picascii by running it as a python module:
# python -m picascii [your selected options ...]
Those options are:
--monochrome - You want to make a monochome text image using only two different symbols
--with-colors - You want to make a colorful text image using various color dot symbols.
You should be aware that you can only use one of --monochrome or --with-colors options during the invocation
These options are only available to you if you select monochrome mode.
--bright-symbol - You want to use a specific symbol to represent bright pixels. (⚪ is the default)
--dark-symbol - You want to use a specific symbol to represent dark pixels. (⚫ is the default)
The options are needed
--input-file - You want to use this image file as source. 
--output-file - You want to use this file as the output
--max-side-size - The maximum length of one edge of the image.

'''
    sys.stderr.write(help_text)
    sys.stderr.flush()
            

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