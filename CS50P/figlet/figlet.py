import sys
import random
from pyfiglet import Figlet
figlet = Figlet()

# Checking for errors. a) 0 or 2 arguments. b) first needs to be -f or --font c) second needs to be font name
all_fonts = figlet.getFonts()
if len(sys.argv) > 3 or len(sys.argv) == 2:
    sys.exit("Invalid usage")
elif len(sys.argv) == 3 and (sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in all_fonts):
    sys.exit("Invalid usage")

# if 0 arguments then random font set; if 2 arguments then user font set
if len(sys.argv) == 1: # i. e., 0 arguments
    ran_num = random.randint(1, 549)
    font_ran = all_fonts[ran_num-1]
    figlet.setFont(font=font_ran)
elif len(sys.argv) == 3:
    font_user = sys.argv[2]
    figlet.setFont(font=font_user)

# prompting input; renderText() in font and print
text = input("Input:")
print(figlet.renderText(text))
