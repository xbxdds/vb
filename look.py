import requests
import re

url='https://pvp.qq.com/web201605/js/herolist.json'
headers={
    'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36 Edg/99.0.1150.36'
}
data=requests.get(url=url,headers=headers).json()
for data_list in data:
    #print(data_list)
    #英雄
    hero_id=data_list['ename']
    hero_name=data_list['cname']
    #拿到皮肤详情页地址
    hero_url=f'https://pvp.qq.com/web201605/herodetail/{hero_id}.shtml'
    #第二次发送请求
    #print(hero_id,hero_name,hero_url)
    data2=requests.get(url=hero_url,headers=headers)
    data2.encoding=data2.apparent_encoding
    data2=data2.text
    skin_name=re.findall('<ul class="pic-pf-list pic-pf-list3" data-imgname="(.*?)">',data2)
    #皮肤
    skin_name=''.join(skin_name)
    skin_name=re.sub('&\d+','',skin_name).split('|')
    for index in range(1,len(skin_name)+1):
        skin_url=f'https://game.gtimg.cn/images/yxzj/img201606/heroimg/{hero_id}/{hero_id}-mobileskin-{index}.jpg'
        #print(hero_id,hero_name,skin_name,skin_url)
        img_name=skin_name[int(index)-1]
        #print(img_name)

        img_data=requests.get(url=skin_url,headers=headers).content
        with open('王者荣耀\\'+hero_name+'--'+img_name,mode='wb') as f:
            f.write(img_data)
        print(hero_name+'打印成功')

        #print(index)
        #https://game.gtimg.cn/images/yxzj/img201606/heroimg/155/155-mobileskin-1.jpg
