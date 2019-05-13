#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
MOOC分析图展示（词云、
2019年1月1日15:32:14
@author: guoenlei
"""

import re
from collections import Counter
from scipy.misc import imread
import pandas as pd
import seaborn as sns
from wordcloud import WordCloud
import jieba
import pymysql

# 从mysql中获取数据
import matplotlib.pyplot as plt
from matplotlib.image import imread


def get_mysql():
    kc_info=[]
    db = pymysql.connect(host='localhost',user='root',passwd='root',db='mooc_courses_info',charset='utf8')
    cur = db.cursor()
    sql = '''SHOW TABLES'''
    cur.execute(sql)
    tables= cur.fetchall()
    for subject in tables:
        cur.execute("select * from %s"% subject)
        results=cur.fetchall()
        kc_info.append(results)
    return tables,kc_info

tables, kc_info = get_mysql()

# 把全部的课程名提取出来并连接在一起
courses_text=''
for kc in kc_info[0]:
    course_text=kc[1]
    # 去除没用的乱七八糟
    courses_text = re.sub("[\“\”\《\》\（\）\，\——\：\、\-\(\)一二三上下与的及之和中 ]", " ", courses_text)
    courses_text=courses_text+' '+course_text

# 使用分词工具jieba进行分词
courses_jieba = list(jieba.cut(courses_text))
# 使用 counter 做词频统计，选取出现频率前 100 的词汇
c = Counter(courses_jieba)
common_c = c.most_common(200)


# 图1.课程中关键字的词云，先加载词云模板
def word_cloud(common_c):
    # 读入词云模板
    print('准备读取词云模板')
    bg_pic = imread('C:\\Users\\guoen\\Desktop\\大学毕设\\毕设软件\\词云模板\\4.jpg')  #加载词云背景图片
    # 配置词云参数
    print('准备配置词云参数')

    wc = WordCloud(
            # 设置字体
            font_path ='C:\\windows\\Fonts\\STSONG.TTF',
			  # 设置背景色
            background_color='white',
            # 允许最大词汇
            max_words=200,
            # 词云形状
            mask=bg_pic,
            # 最大号字体
            max_font_size=200,
            random_state=400,
            )
    print('准备生成词云了')
    # 生成词云
    wc.generate_from_frequencies(dict(common_c))
    # 生成图片并显示
    plt.figure()
    plt.imshow(wc)
    plt.axis('off')
    plt.show()
    # 保存图片
    wc.to_file('C:\\Users\\guoen\\Desktop\\大学毕设\\毕设软件\\生成词云\\3.jpg')
    print('OK,去看看你做的词云吧！')


# 1：课程中关键字的词云
word_cloud(common_c)


# 图2：记录开课数前20个的大学，并用柱形图表示出来
def bar_plot(datas):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置-黑体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    sns.set(font='SimHei')  # 解决Seaborn中文显示问题
    datas = pd.DataFrame(datas[0:20], columns=['大学', '开课数'])
    sns.barplot(x=datas['大学'], y=datas['开课数'], palette="muted")
    plt.xticks(rotation=90)
    plt.show()

uni_courses_num = {}
for kc in kc_info[0]:
    uni_courses_num[kc[2]] = uni_courses_num.get(kc[2], 0) + 1
items = list(uni_courses_num.items())
items.sort(key=lambda x: x[1], reverse=True)
# 2.柱状图展示开课最多的前二十名大学
bar_plot(items)


# 图3：大学开课数统计->课程热度分析
def bar_plot2(datas):
    f, ax = plt.subplots(figsize=(8, 12))
    datas = pd.DataFrame(datas[0:20], columns=['课程名称', '热度'])
    # orient='h'表示是水平展示的，alpha表示颜色的深浅程度
    sns.barplot(y=datas['课程名称'], x=datas['热度'], orient='h', alpha=0.8, color='red')
    # sns.barplot(y=datas['课程名称'], x=datas['热度'],palette="muted")
    # 设置X轴的各列下标字体是水平的
    plt.xticks(rotation='horizontal')
    # 设置Y轴下标的字体大小
    plt.yticks(fontsize=10)
    plt.show()


# 课程热度统计
courses_hot = []
for kc in kc_info[0]:
    courses_hot.append((kc[1], kc[5]))
courses_hot.sort(key=lambda x: x[1], reverse=True)
# 3.调用课程热度统计
bar_plot2(courses_hot)





# 图4.学科开课数统计
num=9
subject_courses=[]
for i in range(1,len(tables)):
    subject_courses.append((tables[i][0],len(kc_info[i])))
subject_courses.sort(key=lambda x:x[1], reverse=True)
left_courses=0
for i in range(num):
    print(subject_courses[-i-1][1])
    left_courses+=subject_courses[-i-1][1]
deal_subject_courses=subject_courses[0:len(subject_courses)-num]
deal_subject_courses.append(('others',left_courses))
print(deal_subject_courses)

def pie_plot(datas):
    # # 饼状图
    labels, sizes = [], []
    for i in range(len(datas)):
        labels.append(datas[i][0])
        sizes.append(datas[i][1])
        # plot.figure(figsize=(8,8))
    colors = ['red', 'yellow', 'blue', 'green', 'blueviolet', 'gold', 'pink', 'purple', 'tomato', 'white']
    colors = colors[0:len(sizes)]
    explode = (0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    explode = explode[0:len(sizes)]
    patches, l_text, p_text = plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                                      labeldistance=1.1, autopct='%2.1f%%', shadow=False,
                                      startangle=-180, pctdistance=0.6)

    # labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
    # autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
    # shadow，饼是否有阴影
    # startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    # pctdistance，百分比的text离圆心的距离
    # patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本

    # 改变文本的大小
    # 方法是把每一个text遍历。调用set_size方法设置它的属性
    for t in l_text:
        t.set_size = 30
    for t in p_text:
        t.set_size = 20
    # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
    # loc: 表示legend的位置，包括'upper right','upper left','lower right','lower left'等
    # bbox_to_anchor: 表示legend距离图形之间的距离，当出现图形与legend重叠时，可使用bbox_to_anchor进行调整legend的位置
    # 由两个参数决定，第一个参数为legend距离左边的距离，第二个参数为距离下面的距离
    plt.grid()
    plt.show()

# 4.学科开课数统计
pie_plot(deal_subject_courses)

