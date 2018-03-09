import re
def addr(addr):
    if re.match(r'^[0-9a-zA-Z]*\@[0-9a-zA-Z]*\.[a-zA-Z]*$',addr):
        return True
    else:
        return False
def addr2(addr):
    if re.match(r'^(<?)([\w\s]*)(>?)([0-9a-zA-Z]*)\@([0-9a-zA-Z]*)\.([a-zA-Z]*)\=\>([a-zA-Z]*)$',addr):
        return True
    else:
        return False

def name_of_email(addr):
    re_email=re.compile(r'^(<?)([a-zA-Z\s])(>?)([a-zA-Z\s])@([a-zA-Z.]*)$')
    if re_email.match(addr):
        return re_email.match(addr).group(2)
    else:
        return None
a=name_of_email('<Tom Paris> tom@voyager.org => Tom Paris')
print(a)

print(re.match(r'^\w?',''))