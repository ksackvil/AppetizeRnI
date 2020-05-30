from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import imageio
import os

# -------------------------------------#
OUTPUT_FOLDER = 'output/'
# -------------------------------------#

# read through the input.txt
def main():
    with open('input.txt') as fp:
        line = fp.readline()
        cnt = 1
        while line:
                PLACE_NAME = line.strip().split('|')[0]
                PLACE_ID = line.strip().split('|')[1]

                scrapeUber(PLACE_NAME, PLACE_ID)
                
                line = fp.readline()
                cnt += 1

# use selenium to scrape
def scrapeUber(PLACE_NAME, PLACE_ID):
    data = {'categories': []}
    reserved = {'<','>',':','"','\\','|','/','?','*','"'}

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.ubereats.com/ca/vancouver/food-delivery/'+PLACE_NAME+'/'+PLACE_ID)

    # Make folders if they don't exist 
    if not os.path.exists(OUTPUT_FOLDER+PLACE_NAME):
        os.makedirs(OUTPUT_FOLDER+PLACE_NAME)

    if not os.path.exists(OUTPUT_FOLDER+PLACE_NAME+'/images'):
        os.makedirs(OUTPUT_FOLDER+PLACE_NAME+'/images')

    cats_wrapper = driver.find_element_by_xpath("//body").find_element_by_id('root').find_element_by_id('wrapper').find_elements_by_xpath('//main/div[2]/ul/li')

    for cat in cats_wrapper:
        driver.execute_script("arguments[0].scrollIntoView();", cat.find_element_by_xpath('.//h2'))
        cat_name = cat.find_element_by_xpath('.//h2').text
        items_wrapper = cat.find_elements_by_xpath('.//ul/li')
        num_cats = len(data['categories'])

        temp_cat_data = {
            "name": cat_name,
            "items": []
        }
        data['categories'].append(temp_cat_data)   

        for item in items_wrapper:
            item_name = ""
            item_description = ""
            item_price = ""
            item_image = ""

            item_name_wrapper = item.find_elements_by_xpath('.//a/div/div[1]/h4/div')
            item_image_wrapper = item.find_elements_by_xpath('.//a/div/div[2]/img')
            div_one = item.find_elements_by_xpath('.//a/div/div[1]/div[1]/div')
            div_two = item.find_elements_by_xpath('.//a/div/div[1]/div[2]/div')

            if len(item_name_wrapper) == 1:
                item_name = item_name_wrapper[0].text
            else:
                print('Cannot find item name, XPATH is invalid or no name is provided')

            if len(item_image_wrapper) == 1:
                item_image = item_image_wrapper[0].get_attribute('src')
                item_image_name = item_image_wrapper[0].get_attribute('alt')

                for c in reserved:
                    item_image_name = item_image_name.replace(c, '')

                im = imageio.imread(item_image)
                with open(OUTPUT_FOLDER+PLACE_NAME + '/images/'+item_image_name+'.jpeg', 'w+') as f:
                    imageio.imwrite(f, im, 'jpeg')
            else:
                print('Cannot find item image, XPATH is invalid or no image is provided')

            # description exists
            if len(div_two) == 1:
                if len(div_one) == 1 :
                    item_description = div_one[0].text
                else:
                    print('Cannot find item description, XPATH is invalid or no description is provided')

                if len(div_two) == 1:
                    item_price = div_two[0].text
                else:
                    print('Cannot find item price, XPATH is invalid or no price is provided')

            # sold out or contains tag
            elif len(div_two) == 2:
                if len(div_one) == 1 :
                    item_description = div_one[0].text
                else:
                    print('Cannot find item description, XPATH is invalid or no description is provided')

                # handle case if tag is present
                if 'Sold' in div_two[0].text:
                    item_price = div_two[1].text
                else:
                    item_price = div_two[0].text

            # description does not exists
            else:
                # handle case if tag is present
                if 'Sold' in div_one[0].text:
                    item_price = div_one[1].text
                else:
                    item_price = div_one[0].text

            temp_item_data = {
                "name": item_name,
                "description": item_description,
                "price": item_price,
                "image": item_image
            }
            data['categories'][num_cats]['items'].append(temp_item_data)

    with open(OUTPUT_FOLDER+PLACE_NAME+'/'+PLACE_NAME+'.json', 'w') as outfile:
        json.dump(data, outfile)

    driver.close()
    driver.quit()


if __name__ == "__main__": 
    main()