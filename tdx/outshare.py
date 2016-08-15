#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by   2016/07/20 

import tushare


import tushare as ts

# result = ts.get_hist_data('600848',start='2015-01-05',end='2015-01-09')
# print type(result)
# print result
# print ts.get_hist_data('600848', ktype='W')
# print result[['open','close','high','low','volume']]
# df[['code','name','price','bid','ask','volume','amount','time']]

print ts.get_today_all()
if __name__ == '__main__':
    pass

'''
import requests
import time
from  multiprocessing import Pool, process


def http_get(url):
	try:
		res = requests.get(url)
		print res.status_code,time.time()

	except Exception, e:
		print e


if __name__ == '__main__':
	# url = 'http://123.125.199.162:42271/gameserverweb/gm/shop.jsp'
	# p = Pool(10)
	# for i in range(1):
	# 	p.apply_async(http_get, args=(url,))
	# p.close()
	# p.join()
	# # p1 = process(target=http_get, args=(url,))
	# # p1.start()
	#
	x = 'abc'
	def func():
		x = 100
		print x
	func()

	print x
 '''