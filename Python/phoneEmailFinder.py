#! python3
import re, pyperclip
phoneRegex = re.compile(r'''
((/d/d/d) | (\(\d\d\d\)))?
(\s|-)
\d\d\d
-
\d\d\d\d
(((ext(\.)?\s)|x)
(\d{2, 5}))?
''', re.VERBOSE)


emailRegex = re.compile(r'''
[a-zA-Z0-9.+_]+
@
[a-zA-Z0-9.+_]+
''', re.VERBOSE)

text = pyperclip.paste()

phone = phoneRegex.findall(text)
email = emailRegex.findall(text)
print(phone)
print(email)
