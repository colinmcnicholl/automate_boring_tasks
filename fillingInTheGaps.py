#! python3
# fillingInTheGaps.py - finds all files with a given prefix, such as 'spam001.txt',
# 'spam002.txt', and so on, in a single folder and locates any gaps in the numbering
# (such as if there is a 'spam001.txt and 'spam003.txt' but no 'spam002.txt').
# The program renames all the later files to close this gap.
# Colin McNicholl: 12/10/2017

import os, re, shutil

dir = 'C:\\Users\\Colin\\atbs'

pattern = re.compile(r'^(spam)(\d+)(.txt)')

fileList = []

for file in os.listdir(dir):
    num = pattern.search(file)
    if num != None:
        num = num.group(2)
        fileList.append((int(num.lstrip('0')), file, len(num)))
        fileList = sorted(fileList)
for index in range(len(fileList)):
    padding = fileList[index][2]
    num = str(int(index) + 1)
    padded_num = num.rjust(padding, '0')
    source = os.path.join(dir, fileList[index][1])
    destination = os.path.join(dir, pattern.sub(r'\g<1>%s\g<3>' % padded_num, fileList[index][1]))
    shutil.move(source, destination)
# for i in 001 002 004 005 006 009 ; do touch ${dir}/spam$i.txt ; echo $i > ${dir}/spam$i.txt ; done
# for i in 011 012 014 025 026 319 ; do touch ${dir}/spam$i.txt ; echo $i > ${dir}/spam$i.txt ; done