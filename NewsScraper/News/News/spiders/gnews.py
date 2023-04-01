import csv

import scrapy
import pandas as pd


class Writer:

    def __init__(self,file_path,fields):
        self.file_path = file_path
        self.fields = fields
        with open(file_path,'w') as csvfile:
            write = csv.DictWriter(csvfile,fieldnames=fields)
            write.writeheader()

    def csv_dicwrite(self,data):
        with open(self.file_path,'a',newline="",encoding='utf-8') as csvfile:
            write = csv.DictWriter(csvfile,fieldnames=self.fields)
            write.writerow(data)




class GnewsSpider(scrapy.Spider):
    name = "gnews"

    def __init__(self):
        self.search = ["zomato"]
        self.file_writer = Writer('gnews.csv',['Title','Site'])


    def start_requests(self):
        links = []

        # Search links
        for i in self.search:
            links.append(f'https://news.google.com/search?for={i}')


        for i in range(len(links)):
            yield scrapy.Request(links[i],callback=self.parse_upper)

    def parse_upper(self, response):
        title = response.xpath('//div[@class="NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc"]//h3/a/text()').getall()
        glinks = response.xpath('//div[@class="NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc"]//h3/a/@href').getall()

        j = 0
        for i in glinks:
            print("https://news.google.com/"+i.replace("./",""))
            yield scrapy.Request("https://news.google.com/"+i.replace("./",""),callback=self.parse,
                                 meta={"title":title[j]})
            j += 1

    def parse(self, response):
        site_link = response.xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[3]/a/@href').get()
        title = response.meta['title']

        data = {'Site':site_link,'Title':title}

        yield data
        # self.file_writer.csv_dicwrite(data)

        print(data)





