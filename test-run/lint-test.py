import os

stl_cores_dir="../"

os.system("fusesoc library add basejump "+stl_cores_dir)

all_files=os.listdir(stl_cores_dir)
core_directories=[]
for i in all_files:
  if i.startswith('bsg'):
    core_directories.append(i)

for i in core_directories:
  cores_in_dir=os.listdir(stl_cores_dir+i)
  for j in cores_in_dir:
    j=j.split('.')[0]
    print("fusesoc run --target lint "+j)
    os.system("fusesoc run --target lint "+j)

os.system("rm fusesoc.conf")
os.system("rm -rf build")
