```{ .python .no-copy }
import requests

cookies = {
    'll': '"118172"',
    'bid': '1g9KuH68SK4',
    '_pk_id.100001.4cf6': 'b0cd6adabb706ae6.1718802720.',
    '__yadk_uid': '7Fy28aQx1DCY4NnZHNsGL18fq4eCFizJ',
    '__utmc': '30149280',
    '__utmz': '30149280.1718802721.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    '__utmc': '223695111',
    '__utmz': '223695111.1718802721.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    '_vwo_uuid_v2': 'D816E9B77293C40EA8C8478097A9394E6|8963e2d5854837c41641bb0564b6793f',
    '_pk_ref.100001.4cf6': '%5B%22%22%2C%22%22%2C1718810576%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DI5UDdlLzyTcOQNcMLaeu6-ehnN7_hAH4R1JwYjyyLmFkXPGCnNdtD8MKfk52YKMgSTO_ecVUL9Drv0n-aGmR2q%26wd%3D%26eqid%3De79e93560000072c000000046672d91c%22%5D',
    '_pk_ses.100001.4cf6': '1',
    'ap_v': '0,6.0',
    '__utma': '30149280.23331474.1718455367.1718802721.1718810577.3',
    '__utma': '223695111.1593040718.1718802721.1718802721.1718810577.2',
    '__utmb': '223695111.0.10.1718810577',
    '__utmt': '1',
    '__utmb': '30149280.1.10.1718810577',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    # 'cookie': 'll="118172"; bid=1g9KuH68SK4; _pk_id.100001.4cf6=b0cd6adabb706ae6.1718802720.; __yadk_uid=7Fy28aQx1DCY4NnZHNsGL18fq4eCFizJ; __utmc=30149280; __utmz=30149280.1718802721.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=223695111; __utmz=223695111.1718802721.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _vwo_uuid_v2=D816E9B77293C40EA8C8478097A9394E6|8963e2d5854837c41641bb0564b6793f; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1718810576%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DI5UDdlLzyTcOQNcMLaeu6-ehnN7_hAH4R1JwYjyyLmFkXPGCnNdtD8MKfk52YKMgSTO_ecVUL9Drv0n-aGmR2q%26wd%3D%26eqid%3De79e93560000072c000000046672d91c%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.23331474.1718455367.1718802721.1718810577.3; __utma=223695111.1593040718.1718802721.1718802721.1718810577.2; __utmb=223695111.0.10.1718810577; __utmt=1; __utmb=30149280.1.10.1718810577',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://movie.douban.com/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'type': 'movie',
    'tag': '热门',
    'page_limit': '100',
    'page_start': '0',
}

response = requests.get('https://movie.douban.com/j/search_subjects', params=params, cookies=cookies, headers=headers)

# movie_dict结果数据
movie_dict = response.json()

# 仅保留电影名和评分和url
movie_dict = {
   'subjects': [
        {
            'title': movie['title'],
            'rate': movie['rate'],
            'url': movie['url'],
        }
        for movie in movie_dict['subjects']
    ]
}
# 电影列表
movie_list = []
for movie in movie_dict['subjects']:
    movie_list.append(movie)

# 按分数排序
movie_list.sort(key=lambda x: x['rate'], reverse=True)

# 结果写入到markdown文件中,格式为 [title](url)的评分为<rate>分
with open('DoubanHot.md', 'w') as f:
    for movie in movie_list:
        f.write(f"[{movie['title']}]({movie['url']})的评分为 {movie['rate']}分\n")
print("Markdown文件已生成")
```