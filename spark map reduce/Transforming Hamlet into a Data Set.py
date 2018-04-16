## 2. Extract Line Numbers ##

raw_hamlet = sc.textFile("hamlet.txt")
split_hamlet = raw_hamlet.map(lambda line: line.split('\t'))
split_hamlet.take(5)
def return_line(line):
    value = line[0].replace('hamlet@','')
    line[0] = value
    return line
hamlet_with_ids = split_hamlet.map(lambda x:return_line(x))
hamlet_with_ids.take(10)

## 3. Remove Blank Values ##

hamlet_with_ids.take(5)
def remove_blank(line):
    if len(line) == 1:
        return False
    else:
        return True
hamlet_text_only_1 = hamlet_with_ids.filter(lambda x:remove_blank(x))
hamlet_text_only_1.take(5)
hamlet_text_only = hamlet_text_only_1.map(lambda x:[l for l in x if l != ''])

## 4. Remove Pipe Characters ##

hamlet_text_only.take(10)
def remove_pip(line):
    re = list()
    for l in line:
        if l == '|':
            pass
        elif '|' in l:
            haha = l.replace('|','')
            re.append(haha)
        else:
            re.append(l)
    return re
clean_hamlet = hamlet_text_only.map(lambda line: remove_pip(line))