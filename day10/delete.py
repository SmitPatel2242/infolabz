import os
l = ["blur","gray","resize","edges"]


for i in l:
    for item in os.listdir(i):
        item_path = os.path.join(i, item)
        if os.path.isfile(item_path):
            os.remove(item_path)


os.rmdir("blur")
os.rmdir("resize")
os.rmdir("gray")
os.rmdir("edges")

