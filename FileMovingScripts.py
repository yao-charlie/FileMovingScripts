import os, shutil, pathlib, re

def nestedMove(directoryName, fileList):
    source = pathlib.Path(directoryName)
    destination = source
    fLIndex = 0

    #iterate over all paths and continue past non-files
    for path in source.glob('**/*'):
        if not path.is_file():
            continue


    #isolate path
        rel_path = path.relative_to(source)

    #replace directory characters
        target_file_name = str(rel_path).replace('\\','-').replace('\\\\', '_')

    #Special case from file list adding suffix.
    #TODO: check into filetypes instead?
    #    target_file_name = fileList[fLIndex] + str(rel_path)[-4]+ str(rel_path)[-3]+ str(rel_path)[-2]+ str(rel_path)[-1]

    #move files
        shutil.move(str(path), str(destination/target_file_name))
        fLIndex = fLIndex + 1

# used for a file where there was a category and subsequent file names, e.g.:
#Alpha
#   1.txt
#   2.txt
#Beta
#   1.txt
#   2.txt
def textRenameParser(fileName, regexParameter):
    with open(fileName) as jabber:
        content = jabber.read().splitlines()

    fileList = []

    for index, name in enumerate(content):
        if re.search(regexParameter, name):
            prefix = name

        else:
            fileList.append(prefix + content[index])
    return(fileList)





# #deprecated walk code
#
# for folderName, subFolders, fileNames in os.walk('F:\_PythonTestFolder'):
#     print('Current folder: ' + folderName)
#
#     for subFolder in subFolders:
#         print('Subfolder of ' + folderName +': '+ subFolder)
#
#     for filename in fileNames:
#         print('File inside ' + folderName + ': '+ filename)
#
#
# for dirpath in os.walk('F:\_PythonTestFolder'):
#     print(dirpath)
#     print(dirpath[0])
#
# for folderName, subFolders, fileNames in os.walk('F:\_PythonTestFolder'):
#
#     # for subFolder in subFolders:
#     #     print('Subfolder of ' + folderName + ': ' + subFolder)
#
#     for filename in fileNames:
#         shutil.move()


