import os
 
# 输入你要更改文件的目录
path = "D:\gitfile\MyFYP\Dataset_new\dataset\Training_labels"
 
# 123是要查找文件名里包含123的文件
originalname = '_mask'
# 321是要被替换的字符串，如果就是删除originalname，那么replacename = ''就可以
replacename = ''
 
def replace(path):
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    # 遍历文件夹
    for file in files:
        if os.path.isdir(path + '\\' + file):
            main1(path + '\\' + file)
        else:
            files2 = os.listdir(path + '\\')
            for file1 in files2:
                if originalname in file1:
                    # 用‘’替换掉 X变量
                    n = str(path + '\\' + file1.replace(originalname, replacename))
                    n1 = str(path + '\\' + str(file1))
                    try:
                        os.rename(n1, n)
                    except IOError:
                        continue
 
 
replace(path)