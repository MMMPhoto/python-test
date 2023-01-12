import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', '1434', 'Belmont'. 'Ave', 'Atlanta', 'GA', '30310']

# Check if command line arguments were passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open(f'http://www.google.com/maps/place/{address}')