import argparse
import os
import glob
import time
import re

import tinify

def main(inpath, outpath, api) :
  
  tinify.key = api
  os.makedirs(outpath, exist_ok=True)
  
  file_list = sorted([os.path.basename(f) for f in glob.glob(inpath + '/*') if re.search('/*\.(jpg|jpeg|png|gif|bmp)', str(f))], key=numerical)
  
  for file in file_list:
    
    file_name = os.path.basename(file)
    output_file = outpath +  '/' + file_name

    print('compressing.. ' + file_name)
    tinify.from_file(file).to_file(output_file)
    
    input_file_size  = os.path.getsize(file)
    output_file_size = os.path.getsize(output_file)

    comporess_size = 100 - round(output_file_size / input_file_size * 100)
    
    print('compressed! : ' + str(round(input_file_size / 1024)) + 'KB => ' +  str(round(output_file_size / 1024)) + 'KB -' + str(comporess_size) + '%')
    
    compressions_this_month = tinify.compression_count
    time.sleep(1)
  
  print('Done compressed ' + str(len(file_list)) + ' images.' )
  print('You can compress the remaining ' + str(500 - compressions_this_month) + ' images this month.')

def atoi(text):
    return int(text) if text.isdigit() else text

def numerical(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='compress image files')
  parser.add_argument('--input', type=str, default='./input')
  parser.add_argument('--output', type=str, default='./output')
  parser.add_argument('--key', type=str, default='' )
  args = parser.parse_args()

  main(args.input, args.output, args.key)