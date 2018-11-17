import os, sys, re

# the name of the directory with program
my_dir = os.path.dirname(sys.argv[0]) or '.'

# list containing the names of the entries in the directory given by path
# dir_list = os.listdir(my_dir)

# count max depth in tree
def depth(path):
    names = [os.path.join(path, name) for name in os.listdir(path)]
    dirs = [name for name in names if os.path.isdir(name)]
    if not dirs:
        return 0
    # recursively call depth
    depths = [depth(d) for d in dirs]
    return max(depths)+1

# create list of dirnames
def dirnames(path):
    # for names in path
    dir_names = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    # recursively call names
    names = [os.path.join(path, name) for name in dir_names]
    if not names:
        return []
    for d in names:
        dir_names.extend(dirnames(d))
    return dir_names

# how much directories have cyrillic names
def cyr_dir(dirlist):
    count = 0
    for s in dirlist:
        if re.match(r'^[а-яА-ЯёЁ]+$', s):
            count += 1
    return count

# the most frequent first letter in dirnames
def first_l(dirlist):
    freq = {}
    for d in dirlist:
        if re.match(r'[а-яА-ЯеЁa-zA-Z]', d[0]):
            if not d[0] in freq:
                freq[d[0]] = 0
            freq[d[0]] = freq[d[0]] + 1
    return(max(freq))

with open('HW_05_res.txt', 'w+', encoding = 'utf-8') as f:
    print('Наибольшая глубина папки: ', depth(my_dir), file = f)
    # print((dirnames(my_dir))
    print('Папок с полностью кириллическими названиями: ', cyr_dir(dirnames(my_dir)), file = f)
    print('Большинство названий папок начинаются на букву: ',first_l(dirnames(my_dir)), file = f)
