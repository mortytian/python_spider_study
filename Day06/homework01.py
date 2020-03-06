import re
s1 = """2008-08-08北京奥运会,2008-05-12汶川地震,2019-10-01建国70周年"""
date = re.findall('\d{4}-\d{2}-\d{2}', s1)
for i in range(len(date)):
    date[i] = re.sub('-','/', date[i])

print(date)


