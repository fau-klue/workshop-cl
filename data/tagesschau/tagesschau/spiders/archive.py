import gzip
import os
import scrapy

from datetime import timedelta, date


def daterange(date1, date2):
    for n in range(int((date2 - date1).days) + 1):
        yield date1 + timedelta(n)


class ArchiveSpider(scrapy.Spider):

    name = 'archive'
    allowed_domains = ['tagesschau.de']

    start = date(2010, 1, 1)
    end = date(2014, 12, 31)
    start_urls = [
        f"https://www.tagesschau.de/archiv/?datum={dt}" for dt in daterange(start, end)
    ]

    def parse(self, response):

        for href in response.xpath('//a[@class="teaser-xs__link"]/@href'):
            yield response.follow(href.get(), callback=self.save)

    def save(self, response):

        page_name = response.url.split("/")[-1]

        # only real pages
        if page_name:

            stand = response.xpath('//div[@class="metatextline"]').get()
            if stand:
                d, m, y = stand.split("\n")[1].strip().split(" ")[1].split(".")
                dt = f'{y}/{y}-{m}/{y}-{m}-{d}'
            else:
                dt = "unknown"

            prefix = "/".join(response.url.split("/")[:-1]).split("tagesschau.de")[-1]
            dir_out = f"archive/{dt}/{prefix}/"
            os.makedirs(dir_out, exist_ok=True)

            with gzip.open(f"{dir_out}/{page_name}.gz", "wb") as f:
                f.write(response.body)
