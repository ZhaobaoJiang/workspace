#!/usr/bin/env python
#coding: utf-8
#create data: 2017-02-25
#author: jiang.zhaobao
#function: search staff infomation

#使arg1字符串在arg2字符串中高亮显示
def highlight_key(arg1,arg2):
    #将传入的参数重新赋值
    key = arg1        
    msg = arg2
    #计算输入的key：arg1 变量的长度          
    length = len(key)
    #key在msg中的起始位置
    count = msg.index(key)
    #将msg：arg1分为三段，以key：arg1为分界线
    msg_start = msg[:count]
    msg_middle = msg[count:length+count]
    msg_end = msg[length+count:]
    #输出整个msg：arg2字符串，并高亮显示info：arg1
    print msg_start+green_start+msg_middle+green_end+msg_end

def main():
    while True:
	#输入要搜索的员工信息
	info = raw_input("Please input the key info:")
	for lines in fp.readlines():      #逐行读取fp文件
            if info == "" or info == " ": #如果为空或回车
                print red_start+"Input error!"+red_end
	        fp.seek(0)                #回到文件开始处
		break
            elif info in lines:           #匹配到输入的内容
		line = lines.strip('\n')  #去除换行符
		# 调用函数，高亮显示info字段
		highlight_key(info,line)
	        fp.seek(0)
		break
            else:
               #print "Can't find!Enter again!"
               fp.seek(0)
               

if __name__ == "__main__":
	#打开员工信息文件:staff_info.txt
	fp = file("staff_info.txt","r")

	#设置颜色变量
	green_start = "\033[92m"
	green_end = "\033[0m"
 
	red_start = '\033[41m'
	red_end = '\033[0m'
        #启动主函数
        main()
