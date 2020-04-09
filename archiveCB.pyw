#! python3

import datetime
import pyperclip
import os

os.makedirs('D:\\Documents\\python_test\\archiveCB', exist_ok=True)
os.chdir('D:\\Documents\\python_test\\archiveCB')

current = datetime.datetime.now()
memo = open('archiveCB {}.txt'.format(current.strftime('%Y-%m-%d')), 'a')
memo.write(pyperclip.paste() + '\n\n')
memo.close()