import os
import libs_and_refs_pasha


def main():
    badfiles = 0
    BadFiles = open('BadFiles.txt', 'w')
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
                        print(os.path.abspath(file))
                        fRead = open(file, 'r')
                        fWrite = open(os.path.splitext(file)[0] + ".html", 'w')
                        libs_and_refs_pasha.parser(fRead, fWrite)
                        fRead.close()
                        fWrite.close()
                    except Exception as ex:
                        BadFiles.write(os.path.abspath(file) + "\n")
                        badfiles += 1
            os.chdir('..')
        os.chdir('..')
    BadFiles.write("Итого необработанных файлов: " + str(badfiles))
    BadFiles.close()
if __name__ == '__main__':
    main()
