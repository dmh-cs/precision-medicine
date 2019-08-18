from glob import iglob
from bs4 import BeautifulSoup
from progressbar import progressbar
import os
import re


def main():
  outpath = '/mnt/med/text_trials/'
  fields_to_extract = ['brief_title', 'brief_summary', 'official_title', 'detailed_description']
  for doc_name in progressbar(iglob('/mnt/med/trials/**', recursive=True)):
    if not os.path.isfile(doc_name): continue
    with open(doc_name) as fh:
      soup = BeautifulSoup(fh.read(), 'xml')
    text = '\n'.join([re.sub(r'\s+', ' ', node.get_text()).strip()
                      for node in soup.find_all(fields_to_extract)])
    with open(outpath + doc_name.split('/')[-1], 'w') as fh:
      fh.write(text)


if __name__ == "__main__":
  import ipdb
  import traceback
  import sys

  try:
    main()
  except: # pylint: disable=bare-except
    extype, value, tb = sys.exc_info()
    traceback.print_exc()
    ipdb.post_mortem(tb)
