import argparse
import glob
import hashlib
# import json
import os

import cv2


def glob_files(folder, file_type='*'):
  search_string = os.path.join(folder, file_type)
  files = glob.glob(search_string)

  print('Searching ', search_string)
  paths = []
  for f in files:
    # if not os.path.isdir(f):
      paths.append(f)

  # We sort the images in alphabetical order to match them
  #  to the annotation files
  paths.sort()

  return paths


class Deduper():
  def __init__(self):
    self.hashes = set()

  # https://stackoverflow.com/questions/26000198/what-does-colon-equal-in-python-mean
  def get_hash(self, img_path):
    # This function will return the `md5` checksum for any input image.
    with open(img_path, "rb") as f:
      img_hash = hashlib.md5()
      chunk = f.read()
      while chunk:
          img_hash.update(chunk)
          chunk = f.read()

    return img_hash.hexdigest()

  def dedupe(self, path):
    dupe_count = 0
    files = glob_files(path)

    for file in files:
      image = cv2.imread(file)
      if image is not None:
        hash = self.get_hash(file)

        if hash in self.hashes:
          dupe_count += 1
          print("Dupe ", file)
        else:
          self.hashes.add(hash)
      else:
        print(file, ' is not an image file')

    print("Dupe count ", dupe_count)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-path", action="store", dest="path", type=str)

    args = parser.parse_args()

    deduper = Deduper()
    deduper.dedupe(args.path)
