import os
import TexSoup as TS


def main():
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
                tex_text = []
                with open(file, encoding='cp1251') as tex_file:
                    for line in tex_file:
                        tex_text.append(line)
                print(tex_text)
            os.chdir('..')
        os.chdir('..')


if __name__ == '__main__':
    main()
