from pyquery import PyQuery as pq
doc = pq(url='https://cuiqingcai.com')
print(doc('title'))


#
# from pyquery import PyQuery as pq
# import requests
# doc = pq(requests.get('https://cuiqingcai.com').text)
# print(doc('title'))

#
# from pyquery import PyQuery as pq
# doc = pq(filename='demo.html')
# print(doc('li'))