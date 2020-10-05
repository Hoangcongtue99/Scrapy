- Tạo project: Mở CMD nhập: scrapy startproject <ProjectName>
- Vào file items.py nhập vào các trường mình sẽ crawl
- Tạo nhện: scrapy genspider <spidername> <tên miền sẽ crawl>
- Vào nhện, sửa list start_urls, sửa hàm parse để nó lấy dữ liệu
- Chạy project:
	+ Crawl: scrapy crawl <spidername> 
	+ Crawl giới hạn số item: scrapy crawl <spidername> -s CLOSESPIDER_ITEMCOUNT=<x>
		(x  là số item giới hạn)
	+ Crawl test trên 1 trang web: scrapy parse --spider=<spidername> <url>