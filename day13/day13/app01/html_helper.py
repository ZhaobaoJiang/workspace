#!/usr/bin/env python2.7
#coding:utf-8

'''
Created on Jun 7, 2017

@author: root
'''
from django.utils.safestring import mark_safe
class PageInfo:
    def __init__(self,current_page,all_count,per_item):
        self.CurrentPage = current_page
        self.AllCount = all_count
        self.PerItem = per_item
    @property  
    def start(self):
        return (self.CurrentPage-1)*self.PerItem
    @property
    def end(self):
        return self.CurrentPage*self.PerItem
    @property
    def all_page_count(self):
        temp = divmod(self.AllCount, self.PerItem)
        if temp[1] == 0:
            all_page_count = temp[0]
        else:
            all_page_count = temp[0] + 1
        return all_page_count
    
def Pager(page,all_page_count):
    '''
        page:当前页
        all_page_count:总页数
    '''
    page_html = []
    first_html = "<a href='/index/%d'>首页</a>" %(1)
    if page <= 1:
        prv_html = "<a href='#'>上一页</a>"
    else:
        prv_html = "<a href='/index/%d'>上一页</a>" %(page-1)
    page_html.append(first_html)
    page_html.append(prv_html)
    
    for i in range(all_page_count):
        if page == i+1:
            a_html = "<a sytle='color:green' href='/index/%d'>%d</a>" %(i+1,i+1)
        else:
            a_html = "<a href='/index/%d'>%d</a>" %(i+1,i+1)
        page_html.append(a_html)
    if page >= all_page_count:
        next_html = "<a href='#'>下一页</a>"
    else:
        next_html = "<a href='/index/%d'>下一页</a>" %(page+1)
    page_html.append(next_html)
    end_html = "<a href='/index/%d'>尾页</a>" %(all_page_count)
    page_html.append(end_html)
    page = mark_safe(''.join(page_html))
    return page