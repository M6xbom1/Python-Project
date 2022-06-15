
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

x = str.replace("\n","")
x = x.replace("--","")
x = x.split(",")
y = str1.replace("\n","")
y = y.split(",")
z = str2.replace("\n","")
z = z.split(",")
print("str =",x)
print("str1 =",y)
print("str2 =",z)

