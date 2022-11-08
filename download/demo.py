with open(r'D:\myData\大正藏典籍分类\論集部\index.html', mode='a', encoding='utf-8') as fp:
    fp.write('url: {}, name:{}\n'.format('1', '1'))

if __name__ == '__main__':
    import os


    def get_FileSize(filePath):
        """文件大小， 字节"""
        fsize = os.path.getsize(filePath)
        print(fsize)
        return fsize


    f = r'C:\Users\daijitao\Downloads\阿含部\aa.txt'
    res  = get_FileSize(f)
