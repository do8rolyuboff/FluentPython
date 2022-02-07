from unicodedata import name

sign_unicodes = {
        chr(i) for i in range(32, 128) if 'SIGN' in name(chr(i).decode(), u'')
    }

print(sign_unicodes)
