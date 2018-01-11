# -*- coding: utf-8 -*-

# @Author  : Scott
# @Time    : 2018/1/9 10:39
# @desc    :

import requests
import webbrowser
import urllib.parse

def open_webbrowser(question):
    webbrowser.open('https://baidu.com/s?wd=' + urllib.parse.quote(question))
    #webbrowser.open('https://baidu.com/s?wd=' + question)

def open_webbrowser_count(question,choices):
    #print('\n -- 题目+选项搜索结果计数法 -- Question:' + question + '\n')
    #print('Question: ' + question + '\n')
    """
    if '不是' in question:
        print('**请注意此题为否定题,选计数最少的**')
    """

    counts = []
    for i in range(len(choices)):
        # 请求
        req = requests.get(url='http://www.baidu.com/s', params={'wd': question + choices[i]})
        content = req.text
        index = content.find('百度为您找到相关结果约') + 11
        content = content[index:]
        index = content.find('个')
        count = content[:index].replace(',', '')
        counts.append(count)
        #print(choices[i] + " : " + count)
        #print("\033[0;31m{0:^10}:{1:^10}\033[0m".format(choices[i],count))
        #print(counts)
    output(question, choices, counts, 1)

def count_base(question,choices):
    #print('\n -- 题目搜索结果包含选项词频计数法 --  Question:' + question + '\n')
    # 请求
    req = requests.get(url='http://www.baidu.com/s', params={'wd':question})
    content = req.text
    #print(content)
    counts = []
    #print('Question: ' + question + '\n')
    """
    if '不是' in question:
        print('**请注意此题为否定题,选计数最少的**')
    """
    for i in range(len(choices)):
        counts.append(content.count(choices[i]))
        #print((choices[i], + " : " + str(counts[i]))
        #print("\033[0;31m{0:^10}:{1:^10}\033[0m".format(choices[i], str(counts[i])))
    output(question, choices, counts ,2)

def output(question, choices, counts, type):
    data = [choices, list(map(int, counts))]
    #print(choices, counts)
    sum_C = sum(data[1])

    if sum_C == 0:
        print('{0}方法失效'.format(type))
    else:
        for i in [0,1,2]:
            data[1][i] = (data[1][i] / sum_C) * 100

        # 最可能的答案
        max_index = data[1].index(max(data[1]))
        max_pro = data[1][max_index]

        # 剩余答案中最可能的答案
        remain_data = data[1].copy()
        remain_data.remove(max_pro)
        mid_pro = max(remain_data)
        mid_index = data[1].index(mid_pro)

        # 最后剩余的
        remain_data.remove(mid_pro)
        min_index = data[1].index(remain_data[0])

        #print('\n 方法:{0} Question:{1} \n'.format(type, question))
        # 绿色为最可能的答案 红色为最不可能的答案
        print("\033[1;32m{0} {1:>5.3}%\033[0m   {2} {3:>5.3}%\033[0;31m   {4} {5:>5.3}%\033[0m  {6}" \
              .format(data[0][max_index], data[1][max_index], \
                     data[0][mid_index], data[1][mid_index], \
                     data[0][min_index], data[1][min_index], type))




def run_algorithm(al_num, question, choices):
    if al_num == 0:
        open_webbrowser(question)
    elif al_num == 1:
        open_webbrowser_count(question, choices)
    elif al_num == 2:
        count_base(question, choices)

if __name__ == '__main__':
    question = '新装修的房子通常哪种化学物质含量会比较高?'
    choices = ['甲醛', '苯', '甲醇']
    run_algorithm(2, question, choices)


