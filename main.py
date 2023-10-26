import os
import libs_and_refs_pasha


def main():
    badfiles = 0
    os.chdir('sources')
    base_dir = os.getcwd()
    dir_list = os.listdir()
    for directory in dir_list:
        os.chdir(directory)
        sub_dir_list = os.listdir()
        for sub_dir in sub_dir_list:
            os.chdir(sub_dir)
            files = os.listdir()
            for file in files:
                if not any(map(str.isdigit, file)) and ".html" not in file:
                    try:
                        fRead = open(file, 'r')
                        fWrite = open(os.path.splitext(file)[0] + ".html", 'w')
                        libs_and_refs_pasha.parser(fRead, fWrite)
                    except Exception as ex:
                        print("Не смог выполниться: " + os.path.abspath(file))
                        badfiles += 1
            os.chdir('..')
        os.chdir('..')
    print("Итого необработанных файлов: " + str(badfiles))

if __name__ == '__main__':
    main()
