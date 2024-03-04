def parserMain(fRead, fWrite):
    partcount = 0
    dict = {'name': '', 'author': ''}
    with fRead as myfile:
        lines = myfile.readlines()
        n = len(lines)
        i = 0
        while partcount == 0 and i < n:
            #name
            if '\noident' in lines[i] and '\bf' in lines[i]:
                start_point = lines[i].find('\bf')
                start_point += 4
                end_point = lines[i].find('}')
                if end_point != -1:
                    dict['name'] = lines[i][start_point:end_point]
                else:
                    i += 1
                    end_point = lines[i].find('}')
                    dict['name'] = lines[i-1][start_point:] + lines[i][:end_point]
            if 'zagol' in lines[i]:
                start_point = lines[i].find('\zagol')
                start_point += 7
                end_point = lines[i].find('}')
                if end_point != -1:
                    dict['name'] = lines[i][start_point:end_point]
                else:
                    i += 1
                    end_point = lines[i].find('}')
                    dict['name'] = lines[i - 1][start_point:] + lines[i][:end_point]
            #author
            if '\'

            i += 1

