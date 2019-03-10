# -*- coding: utf-8 -*-
import os

def exec():
    while True:
        dir = os.getcwd()
        files = search_dir(dir)
        cmd = str(input(":"))

        if cmd == 'exit':
            print("종료")
            break

        if cmd == 'cd ..':
            path = os.path.abspath(os.path.join(dir, ".."))
            os_chdir(path)
        else:
            if cmd in files.keys():
                file = files[cmd]
                path = file['path']
                if (file['type'] == 'directory'):
                    os_chdir(path)
                else:
                    file_read(path)
                    print()

def os_chdir(path):
    try:
        os.chdir(path)
    except Exception as ex:
        print('에러가 발생 했습니다', ex)
        pass


def search_dir(dirname):
    print("{0:^10}".format("타입"),"{0:^10}".format("파일명"))
    files = {}

    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)

        if os.path.isdir(full_filename) or os.path.isfile(full_filename):
            if os.path.isdir(full_filename):
                type = 'directory'
            else:
                type = os.path.splitext(full_filename)[-1]

            print("%s | %s" % ("{0:<10}".format(type), filename))
            files[filename] = {'type':type,'path':full_filename}

    return files

def file_read(filePath):
    f = open(filePath, 'r')
    try:
        while True:
            line = f.readline()
            if not line: break
            print(line)
    except Exception as ex:
        print('에러가 발생 했습니다', ex)
        pass
    finally:
        f.close()