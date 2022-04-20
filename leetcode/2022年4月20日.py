"""
假设有一个同时存储文件和目录的文件系统。下图展示了文件系统的一个示例：



这里将 dir 作为根目录中的唯一目录。dir 包含两个子目录 subdir1 和 subdir2 。subdir1 包含文件 file1.ext 和子目录 subsubdir1；subdir2 包含子目录 subsubdir2，该子目录下包含文件 file2.ext 。

在文本格式中，如下所示(⟶表示制表符)：

dir
⟶ subdir1
⟶ ⟶ file1.ext
⟶ ⟶ subsubdir1
⟶ subdir2
⟶ ⟶ subsubdir2
⟶ ⟶ ⟶ file2.ext
如果是代码表示，上面的文件系统可以写为 "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" 。'\n' 和 '\t' 分别是换行符和制表符。

文件系统中的每个文件和文件夹都有一个唯一的 绝对路径 ，即必须打开才能到达文件/目录所在位置的目录顺序，所有路径用 '/' 连接。上面例子中，指向 file2.ext 的 绝对路径 是 "dir/subdir2/subsubdir2/file2.ext" 。每个目录名由字母、数字和/或空格组成，每个文件名遵循 name.extension 的格式，其中 name 和 extension由字母、数字和/或空格组成。

给定一个以上述格式表示文件系统的字符串 input ，返回文件系统中 指向 文件 的 最长绝对路径 的长度 。 如果系统中没有文件，返回 0。

 

示例 1：


输入：input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
输出：20
解释：只有一个文件，绝对路径为 "dir/subdir2/file.ext" ，路径长度 20
示例 2：


输入：input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
输出：32
解释：存在两个文件：
"dir/subdir1/file1.ext" ，路径长度 21
"dir/subdir2/subsubdir2/file2.ext" ，路径长度 32
返回 32 ，因为这是最长的路径
示例 3：

输入：input = "a"
输出：0
解释：不存在任何文件
示例 4：

输入：input = "file1.txt\nfile2.txt\nlongfile.txt"
输出：12
解释：根目录下有 3 个文件。
因为根目录中任何东西的绝对路径只是名称本身，所以答案是 "longfile.txt" ，路径长度为 12
 

提示：

1 <= input.length <= 104
input 可能包含小写或大写的英文字母，一个换行符 '\n'，一个制表符 '\t'，一个点 '.'，一个空格 ' '，和数字。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-absolute-file-path
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""

s = "skd\n\talskjv\n\t\tlskjf\n\t\t\tklsj.slkj\n\t\tsdlfkj.sdlkjf\n\t\tslkdjf.sdfkj\n\tsldkjf\n\t\tlskdjf\n\t\t\tslkdjf.sldkjf\n\t\t\tslkjf\n\t\t\tsfdklj\n\t\t\tlskjdflk.sdkflj\n\t\t\tsdlkjfl\n\t\t\t\tlskdjf\n\t\t\t\t\tlskdjf.sdlkfj\n\t\t\t\t\tlsdkjf\n\t\t\t\t\t\tsldkfjl.sdlfkj\n\t\t\t\tsldfjlkjd\n\t\t\tsdlfjlk\n\t\t\tlsdkjf\n\t\tlsdkjfl\n\tskdjfl\n\t\tsladkfjlj\n\t\tlskjdflkjsdlfjsldjfljslkjlkjslkjslfjlskjgldfjlkfdjbljdbkjdlkjkasljfklasjdfkljaklwejrkljewkljfslkjflksjfvsafjlgjfljgklsdf.a"
# s = "a\n\taa\n\t\taaa\n\t\t\tfile1.txt\naaaaaaaaaaaaaaaaaaaaa\n\tsth.png"
split_ = s.split("\n")
#print(split_)
hashmap = {}
one_file_flag=0
max_layer = 0


#先是对输入进行切分
for file in split_:
    t_num = file.count("\t")
    if "." in file:
        ext_flag=1
    else:
        ext_flag=0
    hashmap[file] = (t_num,ext_flag)
    if t_num !=0:
        one_file_flag=1 #存在子文件夹
if one_file_flag==0:
     print(max(map(len,split_)))  #返回最长的那个路径

#print(hashmap.items())
last_layer = -1
paths = []
base_ = [x for x in range(10)]
for name,(layer,is_ext) in hashmap.items():
    base_[int(layer)] = name.replace("\t","")
    if is_ext==1:
        paths.append(base_)
        base_= base_[:-1]+[x for x in range(5)]  #！！！！！

print(paths)
all_ret = []
for path in paths:
    ret =0
    for path__ in path:
        if isinstance(path__,str) : #如果为字符串
            ret += len(path__)+1
            if "."in path__:
                break
    all_ret.append(ret-1)

print(max(all_ret))





# def lengthLongestPath(self, input: str) -> int:




class Solution:
    def lengthLongestPath(self, input: str) -> int:
        split_ = input.split("\n")  #切分
        hashmap = {}                #哈希表记录
        one_file_flag=0             #是否为一层的代码
        if "." not in input:        #是否存在文件
            return 0
        for file in split_:        #对切分段进行
            t_num = file.count("\t")  #判断层数多少
            if "." in file:
                ext_flag=1
            else:
                ext_flag=0
            hashmap[file] = (t_num,ext_flag)  #这是第几层 ，是否是文件
            if t_num !=0:             #如果只是一层的话
                one_file_flag=1
        if one_file_flag==0:
            return max(map(len,split_))  #返回最长文件的那个路径

        paths = []
        base_ = [x for x in range(10)]
        for name,(layer,is_ext) in hashmap.items():
            base_[int(layer)] = name.replace("\t","")
            if is_ext==1:     #如果为文件的话
                paths.append(base_)
                base_= base_[:-1]+[x for x in range(3)]
        all_ret = []
        for path in paths:
            ret =0
            for path__ in path:
                if isinstance(path__,str): #如果为字符串
                    ret += len(path__)+1
                    if "."in path__:
                        break
            all_ret.append(ret-1)
        return(max(all_ret))

"""
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        st = []
        ans, i, n = 0, 0, len(input)
        while i < n:
            # 检测当前文件的深度
            depth = 1
            while i < n and input[i] == '\t':
                depth += 1
                i += 1

            # 统计当前文件名的长度
            length, isFile = 0, False
            while i < n and input[i] != '\n':
                if input[i] == '.':
                    isFile = True
                length += 1
                i += 1
            i += 1  # 跳过换行符

            while len(st) >= depth:
                st.pop()
            if st:
                length += st[-1] + 1
            if isFile:
                ans = max(ans, length)
            else:
                st.append(length)
        return ans

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/longest-absolute-file-path/solution/wen-jian-de-zui-chang-jue-dui-lu-jing-by-fi0r/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""