
str = '''At the same time, however, many of us know someone who,
after being fully vaccinated, has tested positive for the coronavirus and showed symptoms. 
I know several, as well. Maybe it's your kid's teacher, your brother-in-law, your neighbor, 
your coworker or your mechanic. And while it's great news that we can leave chicken soup at 
their door instead of attending their memorial service, it makes the phenomenon seem very real 
and not at all "rare" -- so we should probably stop describing them that way. In fact, because 
vaccinated individuals are not getting tested very often, we have no idea how common these infections really are.'''


str1 = '''The virus that causes COVID-19 is mainly transmitted through droplets generated when an infected person coughs, 
sneezes, or exhales. These droplets are too heavy to hang in the air, and quickly fall on floors or surfaces.
You can be infected by breathing in the virus if you are within close proximity of someone who has COVID-19, or 
by touching a contaminated surface and then your eyes, nose or mouth.'''


str2 = '''Python is a multi-paradigm programming language. Object-oriented programming and structured programming 
are fully supported, and many of its features support functional programming and aspect-oriented programming 
(including by metaprogramming and metaobjects (magic methods). Many other paradigms are supported via extensions, 
including design by contract and logic programming. Python uses dynamic typing and a combination of reference 
counting and a cycle-detecting garbage collector for memory management. It also features dynamic name resolution 
(late binding), which binds method and variable names during program execution.'''


wordstr = str.split(" ")
list_ = []
for i in wordstr:
    if str.count(i)>=1 & (i not in list_) & (str.lower() not in list_):
        list_.append(i)
print(" ".join(list_))

wordstr1 = str1.split(" ")
list1_ = []
for i in wordstr1:
    if str1.count(i)>=1 & (i not in list1_) & (str1.lower() not in list_):
        list_.append(i)
print(" ".join(list1_))

wordstr2 = str2.split(" ")
list2_ = []
for i in wordstr2:
    if str2.count(i)>=1 & (i not in list2_) & (str2.lower() not in list2_):
        list2_.append(i)
print(" ".join(list2_))
