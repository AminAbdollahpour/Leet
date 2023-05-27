# def to_jaden_case(string):
#     return " ".join(item.capitalize() for item in string.split())
#
#
# string = "How can mirrors be real if our eyes aren't real"
# print(to_jaden_case(string))
import string


def JadenCase(str):
    str = string.capwords(str)
    return str


str = "How can mirrors be real if our eyes aren't real"
print(JadenCase(str))
