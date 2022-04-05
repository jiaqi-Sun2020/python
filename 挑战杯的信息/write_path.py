import os
base_path = r"./CULane/driver_23_30frame/05171114_0770.MP4"
write_path = r"./driver_23_30frame/05171114_0770.MP4"
file_names = os.listdir(base_path)

all_str = ""
for file_name in file_names:
    if file_name.endswith(".jpg"):
        path = write_path+'/'+ file_name
        all_str +=path+"\n"
    else:
        continue



with open("sjq_test.txt", "w") as f:
    f.write(all_str)  # 自带文件关闭功能，不需要再写f.close()
