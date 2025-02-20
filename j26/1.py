import requests
import threading
import time
def fetch_url(url):
 response = requests.get(url)
 print(f'URL: {url}, length: {len(response.text)}')
start_time = time.time() # اجرا شروع زمان
urls = [
 'https://www.digikala.com/',
 'https://snapp.ir/',
 'https://www.aparat.com/',
 'https://divar.ir/',
 'https://shaparak.ir/',
 'https://namnak.com/',
 'https://www.digikala.com/',
 'https://snapp.ir/',
 'https://www.aparat.com/',
 'https://divar.ir/',
 'https://shaparak.ir/',
 'https://namnak.com/',
]
threads = []
for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
end_time = time.time() # اجرا پایان زمان
time_execution = end_time - start_time
print(f'run time with thread: {time_execution} s')