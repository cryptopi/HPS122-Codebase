
def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

items = []
SPECIAL_CHARS = ['_', '&', '%', '#']
WEBSITE_ENDINGS = ['.edu', '.com', '.io', '.org', '.it', '.br']
with open('bib.txt', 'r') as bib_file:
    for line in bib_file:
        line = line.strip()
        for special in SPECIAL_CHARS:
            line = line.replace(special, f'\\{special}')
        for website_ending in WEBSITE_ENDINGS:
            if website_ending in line:
                beginning = line.index(website_ending)
                while line[beginning] != ' ':
                    beginning -= 1
                    end = line.index(website_ending)
                while end < len(line) and line[end] != ' ':
                    end += 1
                website = line[beginning:end]
                website = website.strip()
                website = '\\\\'.join(chunks(website, 62))
                website = '\\\\\\texttt{' + website + '}'
                line = line[:beginning] + website + line[end:]
        items.append(line)

bibliography = '\\begin{thebibliography}\n'
for i in range(len(items)):
    item = items[i]
    bibliography += '\\bibitem{item-' + str(i) + '}\n'
    bibliography += item + '\n'
bibliography += '\\end{thebibliography}'

print(bibliography)
