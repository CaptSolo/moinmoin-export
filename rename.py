# Quick and dirty script to rename pages directories prior to converting
# them including the rename patterns I needed.

import os
import sys

replacements = [
  ['(20)',' '],
  ['(20c3a5)',' å'],
  ['(23)','#'],
  ['(2b2b)','++'],
  ['(2d)','-'],
  ['(2dc3a5)','-å'],
  ['(2e)','.'],
  ['(2f)','--'],
  ['(c396)','Ö'],
  ['(c3a4)','ä'],
  ['(c3a5)','å'],
  ['(c3a9)','e'],
  ['(c3b6)','ö'],

  ['(c481)','ā'],
  ['(c4ab)','ī'],
  ['(c586)','ņ'],
  ['(c493c5a1)','ēš'],
  ['(c5ab)','ū'],
  ['(c4b7)','ķ'],
  ['(c4b7c493)','ķē'],
  ['(c4a3c493c5a1)','ģēš'],
  ['(c4a3c493)','ģē'],
  ['(c493)','ē'],
  ['(c4bc)','ļ'],
  ['(c5a1)','š'],
  ['(c4a3)','ģ'],
  ['(c5bec481)','žā'],
#  ['(3f)','?'],
#  ['(3a)',':'],
]

def main():
    if len(sys.argv) != 2:
        print("Script takes a single parameter, the path to the pages dir")
        sys.exit(-1)
    path=sys.argv[1]
    dirs = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    for name in dirs:
        new_name = name
        for replace in replacements:
          new_name = new_name.replace(replace[0], replace[1])
        os.rename(os.path.join(path,name), os.path.join(path,new_name))

if __name__ == '__main__':
    main()
