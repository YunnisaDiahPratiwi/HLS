import scrapy
import pandas as pd

class SintaScraper(scrapy.Spider):
    name = "sinta"
    start_page = 835  # Halaman awal
    end_page = 1668    # Ubah sesuai kebutuhan
    base_url = "https://sinta.kemdikbud.go.id/affiliations/profile/398/?page=835"
    view_param = "&view=googlescholar"

    def start_requests(self):
        for page in range(self.start_page, self.end_page + 1):
            url = f"{self.base_url}{page}{self.view_param}"
            yield scrapy.Request(url=url, callback=self.parse, meta={"page": page})

    def parse(self, response):
        articles = response.css(".ar-list-item")
        scraped_data = []
        
        for item in articles:
            title = item.css(".ar-title a::text").get(default="N/A").strip()
            link = item.css(".ar-title a::attr(href)").get(default="N/A")
            authors = item.css(".ar-meta::text").get(default="N/A").strip()
            journal = item.css(".ar-pub::text").get(default="N/A").strip()
            year = item.css(".ar-year::text").get(default="N/A").strip()
            citations = item.css(".ar-cited::text").get(default="0").strip()

            scraped_data.append([title, link, authors, journal, year, citations])

        # Simpan hasil scraping ke CSV
        if scraped_data:
            df = pd.DataFrame(scraped_data, columns=["Title", "URL", "Authors", "Journal", "Year", "Citations"])
            df.to_csv("sinta_scraped_data.csv", mode='a', header=False, index=False, encoding="utf-8")

            self.log(f"✅ Berhasil scrape halaman {response.meta['page']}")
        else:
            self.log(f"⚠️ Tidak ada artikel di halaman {response.meta['page']}")
