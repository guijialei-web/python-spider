import time

import requests
from lxml import etree
import csv

for n in range(2,10):
    # url = f'https://quzhou.anjuke.com/sale/p{n}/'
    url='https://bj.zu.anjuke.com/?kw=%E6%88%BF%E4%B8%9C%20%E5%A4%96%E5%9C%B0'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39',
        'cookie': 'aQQ_ajkguid=9F24F878-2EAC-D56F-5538-4929E29DCDFE; ajk-appVersion=; seo_source_type=0; id58=CroD4GQ9TLBdwhG/C5xeAg==; isp=true; 58tj_uuid=88cd13cd-098e-46fd-9854-c40e8612128d; als=0; ctid=18; _ga=GA1.2.340391032.1681884619; new_uv=2; sessid=6678913A-E3D7-A9E3-E8DA-B69359ED0BFD; twe=2; fzq_h=732c14d1187e16570a786b9941c5df16_1682353161348_795722e760074cbfb5d10400252cfdbb_613754691; fzq_js_anjuke_ershoufang_pc=58f2834b1dac8a46f80bf73fdca309b7_1682354447393_25; obtain_by=2; xxzl_cid=f70c281f2cdf4bbeb0e8f6321ca91ad3; xxzl_deviceid=EO0B33t1J2pRRIM7kqtaeooj0RAGCmsFFQaK7YFUzxliMSdl6HYPXVKjh4K90ZJ4'
        }
    resp = requests.get(url,headers=headers)
    print(resp.text)
    html = etree.HTML(resp.text)
    divs = html.xpath('/html/body/div[5]/div[3]/div[1]/div')
    print(divs)
    url_lst = []
    for div in divs:
        url =''.join(div.xpath('./a/@href'))
        url_lst.append(url)
    print(url_lst)
    for url in url_lst:
        resp2 = requests.get(url, headers=headers)
        html2=etree.HTML(resp2.text)
        area=''.join(html2.xpath('/html/body/div[1]/div/div/div[3]/div[2]/div[2]/div[1]/div[3]/div[2]/div[1]/i/text()'))+'平方米'
        total_price=''.join(html2.xpath('/html/body/div[1]/div/div/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]/text()'))+'万'
        one_price=''.join(html2.xpath('/html/body/div[1]/div/div/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/text()')).strip()
        louceng=''.join(html2.xpath('/html/body/div[1]/div/div/div[3]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]//text()'))
        cengshu=''.join(html2.xpath('/html/body/div[1]/div/div/div[3]/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/text()'))
        chaoxiang=''.join(html2.xpath('/html/body/div[1]/div/div/div[3]/div[2]/div[2]/div[1]/div[3]/div[3]/div[1]/i/text()'))
        xiaoqu=''.join(html2.xpath('/html/body/div[1]/div/div/div[3]/div[2]/div[2]/div[1]/div[4]/div[2]/div[1]/a[1]/text()')).strip()
        quyu=''.join(html2.xpath('/html/body/div[1]/div/div/div[3]/div[2]/div[2]/div[1]/div[4]/div[2]/div[2]/span[2]//text()'))
        with open('data2.csv', mode='a', encoding='utf-8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow([xiaoqu,quyu,area,total_price,one_price,louceng,cengshu])
        print(xiaoqu,quyu,area,total_price,one_price,louceng,cengshu)
        time.sleep(1)