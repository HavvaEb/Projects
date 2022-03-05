import csv
from selenium import webdriver # The selenium.webdriver module provides all the implementations of WebDriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup # Beautiful Soup is a library for Data Scrapping
import re # String Manipulation

with open('housing8.csv','w', encoding='utf8', newline='') as f:
    thewriter = csv.writer(f)
    header= ['Title', 'Location', 'Price', 'Area', 'Number_of_Rooms','Furnished','Kitchen type', 'Status','Garden surface','Swimming Pool']
    thewriter.writerow(header)

    driver = webdriver.Chrome('F:/chromedriver') # Here, we create instance of chrome WebDriver

    for page in range(1,255):
        print(page)
        url = 'https://www.immoweb.be/en/search/house/for-sale?countries=BE&page=' + str(page) + '&orderBy=relevance'
        driver.get(url) 
        # The driver.get method will lead to a page given by the URL. WebDriver will wait until the page is fully
        # loaded (i.e. the "onload" event has been triggered) before returning the control to your script.
        print(url)
        soup = BeautifulSoup(driver.page_source,"html.parser") 
        # And then we use Beautiful soup. 
        # The HTML parser is a structured markup processing tool, which is used to parse HTML files.
        players_list = []
        for p in soup.find_all("a", attrs={"class":"card__title-link"}): 
            # In addition to the tag `a`, which is easily identifiable, we notice some additional
            # information such as the value of the class variable of these identical tags.
            # to get the urls of properties in one page
            players_list.append(p.get("href"))
        
                
        for urls in players_list: 
            # - Extract the content into a variable using BeautifulSoup
            # - Get title
            # - Get price
            # - Get location
            # - Get area
            # - Get number of rooms
            driver.get(urls)
            soup = BeautifulSoup(driver.page_source,"html.parser") 
            price = soup.find_all("p" , attrs={"class":"classified__price"})  # "p" is the tag and attrs is identify the class's name
            price0 = re.findall(r'[$€£]{1}\d+\,?\d{0,3}',str(price),re.UNICODE)


            title = soup.find('h1', class_="classified__title").text.replace('\n', '')
            title = title.strip() #strip() method removes any spaces or specified characters at the start and end of a string.
            title0 = " ".join(title.split()) # The split() method splits a string into a list.

            area = soup.find('p', class_="classified__information--property").text.replace('\n', '')
            area = area.strip()
            area0 = " ".join(area.split())
            area0 = area0.replace("square meters","")

            location = soup.find('span', class_="classified__information--address-row").text.replace('\n', '')
            location = location.strip()
            location0 = " ".join(location.split())

            number_of_rooms = soup.find('span', class_="overview__text").text.replace('\n', '')
            number_of_rooms = number_of_rooms.strip()
            number_of_rooms0 = " ".join(number_of_rooms.split())

            lev = soup.find_all("div",attrs={"class":"accordion__content"})
            lev1 = lev[0]
            lev2 = lev1.find_all('tr', class_ = 'classified-table__row')
            # - Extract the content into a variable using BeautifulSoup for sub-header
            # - Get status
            # - Get furnished
            # - Get type kitchen
            # - Get garden
            # - Get swimming pool
            status0=None
            for i in lev2:

                if (str(i).find("Building condition")>0):
                    lev22 = i
                    lev3 = lev22.find('td', class_ = 'classified-table__data').text.replace('\n', '')
                    lev3 = lev3.strip()
                    status0 = " ".join(lev3.split())
            

            lev1 = lev[1]
            lev2 = lev1.find_all('tr', class_ = 'classified-table__row')
            
            Furnished0=None
            for i in lev2:
                
                if (str(i).find("Furnished")>0):
                    lev22 = i
                    lev3 = lev22.find('td', class_ = 'classified-table__data').text.replace('\n', '')
                    lev3 = lev3.strip()
                    Furnished0 = " ".join(lev3.split())
            

            kitchen0 = None
            for i in lev2:
                
                if (str(i).find("Kitchen type")>0):
                    lev22 = i
                    lev3 = lev22.find('td', class_ = 'classified-table__data').text.replace('\n', '')
                    lev3 = lev3.strip()
                    kitchen0 = " ".join(lev3.split())


            lev1 = lev[2]
            lev2 = lev1.find_all('tr', class_ = 'classified-table__row')
            garden0=None
            for i in lev2:
                
                if (str(i).find("Garden surface")>0):
                    lev22 = i
                    lev3 = lev22.find('td', class_ = 'classified-table__data').text.replace('\n', '')
                    lev3 = lev3.strip()
                    garden0 = " ".join(lev3.split())
                    garden0 = garden0.replace("square meters","")
                    

            lev1 = lev[3]
            swim0=None
            for i in lev1:

                if (str(i).find("Swimming pool")>0):
                    lev22 = i
                    lev3 = lev22.find('td', class_ = 'classified-table__data').text.replace('\n', '')
                    lev3 = lev3.strip()
                    swim0 = " ".join(lev3.split())


            info = [str(title0),str(location0),str(price0[0]), str(area0),str(number_of_rooms0),str(Furnished0), str(kitchen0), str(status0), garden0, str(swim0)]
            info = [str(i or None) for i in info] #Fill empty array with None
            thewriter.writerow(info)







                

