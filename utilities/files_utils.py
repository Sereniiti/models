import tarfile
import os.path

def make_tarfile(output_filename, source_dir):
  with tarfile.open(output_filename, "w:gz") as tar:
    tar.add(source_dir, arcname=os.path.basename(source_dir))

def unpack_tarfile(filename,dirname):
  with tarfile.open(filename, "r:gz") as tar:
    tar.extractall(dirname)
  os.remove(filename)