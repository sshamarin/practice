# import sys, time
# indent = 0
# increase = True
#
# try:
#     while True:
#         print(' ' * indent, end = '')
#         print('********')
#         time.sleep(0.1)
#
#         if increase:
#             indent += 1
#             if indent == 20:
#                 increase = False
#         else:
#             indent -= 1
#             if indent == 0:
#                 increase = True
#
# except KeyboardInterrupt:
#     sys.exit()

import time, sys
intend = 0
changing = True
line = '********'

try:
    while True:
        print(' ' * intend, end = '')
        print(line)
        time.sleep(0.1)

        if changing == True:
            intend += 1
            if intend == 20:
                changing = False

        else:
            intend -= 1
            if intend == 0:
                changing = True

except KeyboardInterrupt:
    sys.exit()
