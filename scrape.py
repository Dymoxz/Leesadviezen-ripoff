from playwright.sync_api import sync_playwright
import json
from csv import writer

with open('test', 'r') as fp:
    links = json.load(fp)
    # links = [links[1]]

#'xpath=/html/body/div/div[3]/div[1]/table/tbody/tr[2]/td[2]/strong'
 
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        
        for link in links:

            page.goto(link)
            
            book_meta = []
            
            for i in [2,3,4,5,6]:
                if i == 6:
                    info = page.query_selector(f'xpath=/html/body/div/div[3]/div[1]/table/tbody/tr[{i}]/td[2]/img').get_attribute('src')
                    book_meta.append(info[62])
                else:
                    info = page.query_selector(f'xpath=/html/body/div/div[3]/div[1]/table/tbody/tr[{i}]/td[2]/strong')
                    book_meta.append(info.inner_text())

            p_num = 7

            while len(book_meta) == 5:
                try:
                    a = page.query_selector(f'xpath=/html/body/div/div[3]/div[1]/table/tbody/tr[{p_num}]/td[2]/strong').inner_text()
                except:
                    book_meta.append('unknown')
                if a.isnumeric():
                    book_meta.append(a)
                else:
                    p_num += 1


            print(book_meta)
    
            with open('data.csv', 'a', newline='') as f_object:
                writer_object = writer(f_object)
            
                writer_object.writerow(book_meta)

                f_object.close()




        page.wait_for_timeout(10000)
        browser.close()
 
 
if __name__ == '__main__':
    main()