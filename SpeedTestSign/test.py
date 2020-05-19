import re
pattern2  =re.compile(r'.*(Error).*')
pattern = re.compile('(.*)\\((\d+)\):\\s+(warning|error|Error):\\s+(.*)|(.*: Error: .*\\(referred from .*\\))')
string = """*** linking...
.\Objects\1_GPIO.axf: Error: L6218E: Undefined symbol iit (referred from main.o).
.\Objects\1_GPIO.axf: Error: L6218E: Undefined symbol keyscanner (referred from main.o).
Not enough information to list image symbols.
Not enough information to list load addresses in the image map.
Finished: 2 information, 0 warning and 2 error messages.
".\Objects\1_GPIO.axf" - 2 Error(s), 2 Warning(s).
Target not created.
Build Time Elapsed:  00:00:04
main.c(65): warning:  #223-D: function "iit" declared implicitly
  	iit();
main.c(72): warning:  #223-D: function "keyscanner" declared implicitly
  			switch (keyscanner())
main.c: 2 warnings, 0 errors
"""
mach = re.finditer(pattern,string)
for ma in mach:
    for each in ma.groups():
        print(each)