print('''นายธนกฤต ฉัตรวิเชียร  รหัสนิสิต:64102010076
นายอาชวิน ฉัตรอนันทเวช  รหัสนิสิต:64102010088''')

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

def sentences():
    print("'The First Function'")
    x = str.replace("\n","")
    x = x.replace("--","")
    x = x.split(".")
    y = str1.replace("\n","")
    y = y.split(".")
    z = str2.replace("\n","")
    z = z.split(".")
    print("str =",x)
    print()
    print("str1 =",y)
    print()
    print("str2 =",z)
    print()
   
def non_duplicate():
    print("'The Secont Function'")
    wordstr = str.split()
    list_ = []
    for i in wordstr:
        a = i.replace(".","")
        if str.count(i)>=1 & (i not in list_) & (str.lower() not in list_) & (a not in list_):
            list_.append(i)
    print(" ".join(list_))
    print()


    wordstr1 = str1.split()
    list1_ = []
    for j in wordstr1:
        b = j.replace(".","")
        if str1.count(j)>=1 & (j not in list1_) & (str1.lower() not in list1_)& (b not in list1_):
            list1_.append(j)
    print(" ".join(list1_))
    print()


    wordstr2 = str2.split()
    list2_ = []
    for p in wordstr2:
        c = p.replace(".","")
        if str2.count(p)>=1 & (p not in list2_) & (str2.lower() not in list2_)& (c not in list2_):
            list2_.append(p)
    print(" ".join(list2_))
    print()


def duplicate():
    print("'The Third Function'")
    words = str.split()
    counts = {"this":0,"these":0,"those":0,"a":0,"an":0,"the":0,"is":0,"am":0,"are":0}
    for i in words:
        if i in counts:
            counts[i] += 1
    print(counts)
    print()

    words1 = str1.split()
    counts1 = {"this":0,"these":0,"those":0,"a":0,"an":0,"the":0,"is":0,"am":0,"are":0}
    for j in words1:
        if j in counts:
            counts1[j] += 1
    print(counts1)
    print()

    words2 = str2.split()
    counts2 = {"this":0,"these":0,"those":0,"a":0,"an":0,"the":0,"is":0,"am":0,"are":0}
    for p in words2:
        if p in counts:
            counts2[p] += 1
    print(counts2)
    print()


#callfunction here!

#sentences()
#non_duplicate()
#duplicate()
