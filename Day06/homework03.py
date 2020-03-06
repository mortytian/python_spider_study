import re

s3="""Regular Expression Syntax
A regular expression (or RE) specifies a set of strings that matches it; the functions in this module let you 1/2 check 123 if a particular string matches a given regular expression
(or if a given regular 45% expression 45.5%matches a particular string, which comes down to the same thing).  testMar
Regular expressions No.1 can be 1.234 concatenated to form new regular expressions; if A and B are both regular expressions, -3 then AB is also a regular expression.
In general, if a -1.2 string p matches A and another string q matches B, the string pq will match AB. This holds unless A or B contain low precedence operations; boundary conditions between A and B;
or have numbered group references. Thus, complex expressions can easily be constructed from simpler primitive expressions like the ones described here. For details of the theory and implementation of regular expressions,
consult the Friedl book [Frie09], or almost any textbook about compiler construction.
A brief explanation of the format of regular expressions follows. For further information and a gentler presentation, consult the Regular Expression HOWTO. Python3 """

pattern_number = '\d+%|\d+.\d+%|-\d+.\d+|\d+\.\d+|\d+'
numbers = re.findall(pattern_number, s3)

pattern_word = '[a-zA-Z]+'
words = re.findall(pattern_word, s3)
print(words)