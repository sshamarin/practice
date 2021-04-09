# def spam(devideby):
#     try:
#         return 42 / devideby
#     except ZeroDivisionError:
#         print('error! you cannot divide by zero')
#
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

def spam(devideby):
#    try:
        return 42 / devideby
#    except ZeroDivisionError:
#        print('error! you cannot divide by zero')

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1)) # do not execute, cause programm moves into except section
                   # and do not return to section try
except ZeroDivisionError:
    print('error!')
