import os
"""Хм, а есть прогноз, когда именно для разметки html можно будет литературу извлечь?

Там не надо особо изобретать. Просто надо:
1) Дойдя до \textbf{Литература} перевести его в <div><strong>Литература</strong></div>, а затем все строки начинающиеся с последовательных чисел с точкой переводить в <div class="ref"> </div> с учётом
2) \textit{...} заменить на <em>...</em>
3) ~ заменить на &nbsp;
4) -- заменить на &ndash;
5) Что-то начинающееся на http... обернуть в <a href="http..." target="_blank"></a>

То же самое сделать для \textbf{References} → <div><br><strong>References</strong></div>"""

def main():
    os.chdir('sources')
    base_dir = os.getcwd()
    dir_list = os.listdir()
    for directory in dir_list:
        os.chdir(directory)
        sub_dir_list = os.listdir()
        for sub_dir in sub_dir_list:
            os.chdir(sub_dir)
            tex_text = []
            with open('lit-ra.tex', encoding='cp1251') as tex_file:
                for line in tex_file:
                    tex_text.append(line)
            print(tex_text)
            os.chdir('..')
        os.chdir('..')

if __name__ == '__main__':
    main()
