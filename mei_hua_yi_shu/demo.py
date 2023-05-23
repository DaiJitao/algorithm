from typing import List, Optional

"""
以农历之年月日总和除以八，以余数为卦数求上卦;以年月日时总和除以八，以余数为卦数求下卦，再以年月日时总和除以六，以余数为动爻。

例：公历（阳历）2001年9月19日上午10点钟起卦，先把公历的年月日和时间换成阴历，查万年历（电脑上网查询）便可一目了然。经查万年历上面这个阳历日期为阴历：辛巳年八月初三，上午10点为巳时。

辛巳年

【注意事项】：时辰和年数是取用地支的序数，序数是子为1、丑为2······亥为12。
"""


class MeiHua(object):
    """地支序数"""

    def __init__(self):
        """ 先天八卦序数：乾一、兑二、离三、震四、巽五、坎六、艮七、坤八 """
        self.num2name, self.name2num = self.__get_num2name()

    def __get_num2name(self):
        dizhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
        num2name = {}
        name2num = {}
        for i, e in enumerate(dizhi):
            num2name[i + 1] = e
            name2num[e] = i + 1

        return num2name, name2num

    def __get_num(self, value, type='year'):
        """获取序数"""
        return self.name2num.get(value)

    def qi_gua(self, year, month_id, day_id, time_id):
        """
        取天清地浊之意
        :param year:
        :param month_id: 农历月份
        :param day_id: 农历日期
        :param time_id:
        :return:
        """
        year_id = self.name2num[year]
        print(f"year_id:{year_id}")
        上卦 = (year_id + month_id + day_id) % 8
        if 上卦 == 0: #刚好被8除尽，比如8/8,取第八个挂
            上卦 = 8

        # 动爻所在处，为用卦；
        下卦 = (year_id + month_id + day_id + time_id) % 8
        动爻 = (year_id + month_id + day_id + time_id) % 6
        return 上卦, 下卦, 动爻

def jia_zi():
    dizhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
    tiangan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
    # 六十甲子，天干在前去排列
    """
    01.甲子 02.乙丑 03.丙寅 04.丁卯 05.戊辰 06.己巳 07.庚午 08.辛未 09.壬申 10.癸酉
    11.甲戌 12.乙亥 13.丙子 14.丁丑 15.戊寅 16.己卯 17.庚辰 18.辛巳 19.壬午 20.癸未
    21.甲申 22.乙酉 23.丙戌 24.丁亥 25.戊子 26.己丑 27.庚寅 28.辛卯 29.壬辰 30.癸巳
    31.甲午 32.乙未 33.丙申 34.丁酉 35.戊戌 36.己亥 37.庚子 38.辛丑 39.壬寅 40.癸卯
    41.甲辰 42.乙巳 43.丙午 44.丁未 45.戊申 46.己酉 47.庚戌 48.辛亥 49.壬子 50.癸丑
    51.甲寅 52.乙卯 53.丙辰 54.丁巳 55.戊午 56.己未 57.庚申 58.辛酉 59.壬戌 60.癸亥
    """

if __name__ == '__main__':
    """ 癸卯年农历三月初九 9：14 巳时，转化为下面的数字 """
    year = '卯'
    month = 3 #
    day = 9
    time = 6

    """ 癸卯年农历三月19 11：34 午时，转化为下面的数字 """
    """ 
    癸卯年 兔:木
    丁巳月 火
    丙寅日 木
    """
    year = '卯'
    month = 3 #
    day = 19
    time = 7
    上卦, 下卦, 动爻 = MeiHua().qi_gua(year=year, month_id=month, day_id=day, time_id=time)
    print(上卦, 下卦, 动爻)
