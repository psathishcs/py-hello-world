import os
dir = 'C:\\Users\\psathishcs\\Desktop'
file_list = os.listdir(dir)
print(file_list)

for r, d, f in os.walk(dir):
    for file in f:
        if ".docx" in file:
            print(os.path.join(r, file))
