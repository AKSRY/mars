#! python3
import os

#.txtファイルを空行ごとにバラす
def file_flagm(f_path, to_path):
  origin = open(f_path)
  lines = origin.readlines()
  origin.close()
  chunks = {}
  while '\n' in lines:
    raw_chunk = ''
    for lp_0 in range(lines.index('\n')):
      raw_chunk += lines[lp_0]
    chunks[lines[0].strip('\n')] = raw_chunk
    del raw_chunk
    del lines[0:lines.index('\n')+1]
  os.chdir(to_path)
  for lp_0 in chunks.keys():
    flagmented = open(str(lp_0)+'.txt', 'w')
    flagmented.write(chunks[lp_0])
    flagmented.close()