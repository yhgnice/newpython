#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by   2016/08/15 



import  sys
import urllib

def cbk(a,b,c):
	per = 100.0*a*b/c
	if per >100:
		per=100
	def cls(str):
		return '\r'*len(str)
	out='%.2f%%'%per
	sys.stdout.write(u'下载进度：')
	sys.stdout.write(out)
	sys.stdout.write(cls(out))

url="http://96.ierge.cn/11/168/336613.mp3"
urllib.urlretrieve(url,'download_123.mp3',cbk)


if __name__ == '__main__':
	pass

