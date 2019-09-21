import re
import os


# 输出行数
def printLineNumber(filepath):
    if not os.path.isfile(filepath):
        return "您输入的路径为" + filepath + "路径不存在或不是文件，请检查"
    with open(filepath, encoding='utf-8') as f:
        lines = f.readlines()
    linenumber = len(lines)
    if lines[-1][-1] == '\n':
        linenumber = linenumber + 1
    return os.path.basename(filepath) + "有%d行" % linenumber


# 输出字符数
def printCharNumber(filepath):
    if not os.path.isfile(filepath):
        return "您输入的路径为" + filepath + "路径不存在或不是文件，请检查"
    with open(filepath, encoding='utf-8') as f:
        lines = f.readlines()
    charNumber = 0
    for line in lines:
        charNumber += len(line)
    if lines.__len__() != 0:
        charNumber = charNumber - lines.__len__() + 1  # 回车的换行符不能算字符
    return os.path.basename(filepath) + "有%d个字符" % charNumber


# 输出单词数
def printWordNumber(filepath):
    if not os.path.isfile(filepath):
        return "您输入的路径为" + filepath + "路径不存在或不是文件，请检查"
    with open(filepath, encoding='utf-8') as f:
        lines = f.readlines()
    word = []
    for line in lines:
        line = re.sub("[^\w]", " ", line)  # 用正则表达式筛选单词中有的字符
        wo = line.split()
        word.extend(wo)
    return os.path.basename(filepath) + "有%d个单词" % word.__len__()


# 输出特殊行数
def printSpecialLine(filepath):
    if not os.path.isfile(filepath):
        return "您输入的路径为" + filepath + "路径不存在或不是文件，请检查"
    with open(filepath, encoding='utf-8') as f:
        lines = f.readlines()
    linenumber = 0  # 正在处理第几行
    startline = 0  # 注释块从第几行开始
    blanklines = 0  # 空行数
    notelines = 0  # 注释行数
    isStart = False

    for line in lines:
        linenumber = linenumber + 1
        line = line.replace(' ', '')  # 把字符串中空字符全部替换掉

        # 空行
        if line == "" or line == "{" or line == "}" or line == '\n':
            if line.startswith("") and isStart:  # 注释中的空行不算空行
                continue
            blanklines = blanklines + 1

        # 单行注释行
        elif line.startswith("//") or line.startswith("}//") or line.startswith("{//"):
            notelines = notelines + 1

        # 注释块的开始
        elif line.startswith("/*"):
            isStart = True
            startline = linenumber

        # 注释块结束
        elif line.startswith("*/"):
            notelines = notelines + linenumber - startline + 1
            isStart = False
            startline = 0
    if lines[-1][-1] == '\n':
        linenumber = linenumber + 1
        blanklines = blanklines + 1
    codelines = linenumber - notelines - blanklines  # 代码行等于总行数减空行和注释行

    return os.path.basename(filepath) + "有" + str(blanklines) + "个空行" + '\n' + \
           "有" + str(codelines) + "个代码行" + '\n' + "有" + str(notelines) + "个注释行"


# 对文件夹递归输出
result = []
def processFolder(folderpath, function, type='0'):
    if not os.path.exists(folderpath):
        return "您输入的路径为" + folderpath + "路径不存在，请检查"

    elif os.path.isfile(folderpath):
        return "您输入的路径为" + folderpath + "这是一个文件，该模式应输入一个文件夹"

    filelist = os.listdir(folderpath)
    # 如果是文件，执行输出，如果是文件夹，递归调用
    for file in filelist:
        path = os.path.join(folderpath, file)
        # 是一个文件
        if os.path.isfile(path):
            # 没有通配符
            if type == '0':
                if function == 'c':
                    result.append(printCharNumber(path)+'\n')
                elif function == 'w':
                    result.append(printWordNumber(path)+'\n')
                elif function == 'l':
                    result.append(printLineNumber(path)+'\n')
                else:
                    result.append(printSpecialLine(path)+'\n')
            # 有通配符
            else:
                for i in range(len(file)):
                    if file[i] == '.':
                        break
                # 通过文件名中第一个点的位置找到文件类型，和输入一致则输出行数
                if type == file[i + 1:]:
                    if function == 'c':
                        result.append(printCharNumber(path)+'\n')
                    elif function == 'w':
                        result.append(printWordNumber(path)+'\n')
                    elif function == 'l':
                        result.append(printLineNumber(path)+'\n')
                    else:
                        result.append(printSpecialLine(path)+'\n')
        # 是一个文件夹
        else:
            processFolder(path, function, type)
    return result
