#Regular Expressions
import re

# To find a pattern we use different set of re character sets that allows to search for a match in a string.

# re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
# re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
# re.findall: Returns a list containing all matches
# re.split: Takes a string, splits it at the match points, returns a list
# re.sub: Replaces one or many matches within a string

# txt = 'i love to study python and javascript'
# match = re.match('i love to study', txt, re.I)
# print(match)
# # We can get the starting and ending position of the match as tuple using span

# span = match.span()
# print(span)

# # Lets find the start and stop position from the span

# start, end = span
# print(start, end)

# substring = txt[start:end]
# print(substring)

#search
# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''
# match = re.search('first', txt, re.I)
# print(match)

# # We can get the starting and ending position of the match as tuple using span

# span = match.span()
# print(span)     # (100, 105)
# # Lets find the start and stop position from the span
# start, end = span
# print(start, end)  # 100 105
# substring = txt[start:end]
# print(substring) 


# findall() returns all the matches as a list

# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''

# # It return a list
# matches = re.findall('language', txt, re.I)
# print(matches)  

# note:As you can see, the word language was found two times in the string


# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''

# matches = re.findall('Python|python', txt)
# print(matches)  

# matches = re.findall('[Pp]ython', txt)
# print(matches)  


# Replacing a Substring

# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''

# match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
# print(match_replaced)  
# # OR
# match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
# print(match_replaced) 



# txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
# T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
# I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
# D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

# matches = re.sub('%', '', txt)
# print(matches)



# Splitting Text Using RegEx Split

# txt = '''I am teacher and  I love teaching.
# There is nothing as rewarding as educating and empowering people.
# I found teaching more interesting than any other jobs.
# Does this motivate you to be a teacher?'''
# print(re.split('\n', txt)) 


# Writing RegEx Patterns

# regex_pattern = r'apple'
# txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
# matches = re.findall(regex_pattern, txt)
# print(matches)

# # To make case insensitive adding flag '
# matches = re.findall(regex_pattern, txt, re.I)
# print(matches) 
# regex_pattern = r'[Aa]pple' 
# matches = re.findall(regex_pattern, txt)
# print(matches) 


# Square Bracket
# Let us use square bracket to include lower and upper case

# regex_pattern = r'[Aa]pple'
# txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
# matches = re.findall(regex_pattern, txt)
# print(matches)  


# Escape character(\) in RegEx

# regex_pattern = r'\d' 
# txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
# matches = re.findall(regex_pattern, txt)
# print(matches) 

#One or more times(+)

# regex_pattern = r'\d+' 
# txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
# matches = re.findall(regex_pattern, txt)
# print(matches) 


# Period(.)

# regex_pattern = r'[a].' 
# txt = '''Apple and banana are fruits'''
# matches = re.findall(regex_pattern, txt)
# print(matches)  

# regex_pattern = r'[a].+' 
# matches = re.findall(regex_pattern, txt)
# print(matches) 

# Zero or more times(*)
# note:Zero or many times. The pattern could may not occur or it can occur many times.

# regex_pattern = r'[a].*' 
# txt = '''Apple and banana are fruits'''
# matches = re.findall(regex_pattern, txt)
# print(matches) 


# Zero or one time(?) Zero or one time. The pattern may not occur or it may occur once.

# txt = '''I am not sure if there is a convention how to write the word e-mail.
# Some people write it as email others may write it as Email or E-mail.'''
# regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
# matches = re.findall(regex_pattern, txt)
# print(matches)  

#Quantifier in RegEx


# txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
# regex_pattern = r'\d{4}' 
# matches = re.findall(regex_pattern, txt)
# print(matches)  

# txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
# regex_pattern = r'\d{1, 4}'   
# matches = re.findall(regex_pattern, txt)
# print(matches) 


#Cart ^

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches) 