import sys
import function
import window

argvs = sys.argv
if len(argvs) > 5:
    print("参数过多")
    sys.exit(0)

if (argvs[1] != 'c') & (argvs[1] != 'w') & (argvs[1] != 'l') & (argvs[1] != 'a') & (argvs[1] != 'x'):
    print("您输入的功能参数是"+argvs[1])
    print("功能参数只能为'c','w','l','a','x'")
    sys.exit(0)

# 输入x,调用gui
if argvs[1] == 'x':
    window.showWindow()

# 功能参数输入正确，不遍历文件夹
elif argvs[2] != 's':
    fun = argvs[1]
    filename = argvs[2]
    if fun == 'c':
        print(function.printCharNumber(filename))
    elif fun == 'w':
        print(function.printWordNumber(filename))
    elif fun == 'l':
        print(function.printLineNumber(filename))
    elif fun == 'a':
        print(function.printSpecialLine(filename))


# 功能参数正确，遍历文件夹
else:
    if len(argvs) < 4:
        print("请输入文件夹的路径")
        sys.exit(0)
    else:
        folderpath = argvs[3]
        fun = argvs[1]
        # 没有通配符
        if len(argvs) < 5:
            for result in function.processFolder(folderpath, fun):
                print(result)
        # 有通配符
        else:
            type = argvs[4]
            if type[0] != '*':
                print("通配符输入不正确，应为*.xxx")
                sys.exit(0)
            # 通配符第一个字母输入正确,将文件类型切出来
            type = type[2:]
            print("文件夹下."+type+"文件的字数情况为")
            for result in function.processFolder(folderpath, fun, type):
                print(result)
