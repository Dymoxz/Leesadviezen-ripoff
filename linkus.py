from playwright.sync_api import sync_playwright
import json

pages = []

#'xpath=/html/body/div/div[3]/div[1]/table/tbody/tr[2]/td[2]/strong'
 
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://www.leesadviezen.nl/alle-boeken/')

        niveau_knop = page.query_selector('xpath=/html/body/div/div[2]/div/div/table/thead/tr/td[5]')
        niveau_knop.click()

        page.wait_for_timeout(100)
        
        next_page = 2
        augh = False

        for x in range(107):
            for i in range(1,6):
                link = page.query_selector(f'xpath=/html/body/div/div[2]/div/div/table/tbody/tr[{i}]/td[2]/h3/a').get_attribute('href')
                pages.append(f'https://www.leesadviezen.nl{link}')
            

            print(f'SCRAPED :   {len(pages)}')
                                            
            page_button = page.query_selector(f'xpath=/html/body/div/div[2]/div/div/div[3]/span/a[{next_page}]')
            #page.wait_for_timeout(2000)
            page_button.click()
            
            if next_page == 5 or (next_page == 4 and augh == True):
                next_page = 4
                augh = True
            else:
                next_page += 1

        with open('test', 'w') as fp:
            json.dump(pages, fp)
        print()
        print(' D U M P E D ')
        print()

        page.wait_for_timeout(1000)
        browser.close()
 
 
if __name__ == '__main__':
    main()