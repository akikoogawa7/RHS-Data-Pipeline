#%%
from requests.api import get
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

#%%
main = driver.get('https://www.rhs.org.uk/Plants/Search-Results?f_plant_pollination_true=f%2Fplant_pollination%2Ftrue&form-mode=true&context=b%3D0%26hf%3D10%26l%3Den%26q%3D%2523all%26s%3Ddesc%2528plant_merged%2529%26sl%3DplantForm&unwind=undefined')

#%%
# Begins looping through elements for links
def get_all_plants_on_page():
  """Function to add to the list of all plants with links"""
  plant_list = []
  plants = driver.find_elements_by_xpath('//*[@id="planet_search_list"]/div/plants-search-result-list/div/ul/li')
  for target_plant in plants:
      link = target_plant.find_element_by_class_name("btn-2").get_attribute('href')
      plant_list.append(link)
      print(link)
  return plant_list
  
sleep(10)

#%%
# Loops through all pages 1 by 1 in 50s
# Out of 30518 pages
pollinator_plants_list = []
for i in range(50):
  base_url = 'https://www.rhs.org.uk/plants/search-results?context=b%253D0%2526hf%253D10%2526l%253Den%2526q%253D%252523all%2526s%253Ddesc%252528plant_merged%252529%2526sl%253Dplants%2526r%253Df%25252Fplant_pollination%25252Ftrue&s=desc(plant_merged)&f_plant_pollination_true=f%2Fplant_pollination%2Ftrue&form-mode=true&unwind=undefined&page='
  driver.get(base_url + str(i))
  new_plants = get_all_plants_on_page()
  pollinator_plants_list.extend(new_plants)

#%%
# Scrape data from all_plants_list
pollinator_plants_data = []
colour_imgs_autumn = []
colour_imgs_spring = []
colour_imgs_summer = []
colour_imgs_winter = []

for plant in pollinator_plants_list:
  try:
    plant_item_details = driver.get(plant)
    plant_detail_box = driver.find_elements_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[1]')
  
    """Type"""
    scientific_name = driver.find_element_by_xpath('.//h1').text
    print(scientific_name)
    common_name = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[1]/h2').text
    print(common_name)
    other_common_names = driver.find_element_by_xpath('.//p').text
    print(other_common_names)
    family = driver.find_element_by_xpath('.//*[@id="ctl00_ctl00_ctl00_plcMainContent_plcMainContent_plcMainContent_PlantDetail1_Li15"]/p').text
    print(family)
    genus = driver.find_element_by_xpath('.//*[@id="ctl00_ctl00_ctl00_plcMainContent_plcMainContent_plcMainContent_PlantDetail1_Li2"]/p').text
    print(genus)
    plant_range = driver.find_element_by_xpath('.//*[@id="ctl00_ctl00_ctl00_plcMainContent_plcMainContent_plcMainContent_PlantDetail1_Li4"]/p').text
    print(plant_range)
    # pollinator_perfect = driver.find_element_by_xpath('.//h5').text
    # print(pollinator_perfect)

    """Characteristics"""
    foliage = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[1]/div/div/div/ul/li[1]/p').text
    print(foliage)
    habit = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[1]/div/div/div/ul/li[2]/p').text
    print(habit)
    hardiness = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[1]/div/div/div/ul/li[3]/p').text
    print(hardiness)

    """Sunlight"""
    sunlight = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[3]/div/div/div[1]/ul').text
    print(sunlight)
    aspect = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[3]/div/div/div[2]/ul/li[1]/p').text
    print(aspect)
    exposure = driver.find_element_by_xpath('//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[3]/div/div/div[2]/ul/li[2]/p').text
    print(exposure)

    """Soil"""
    soil = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[4]/div/div/div[1]/ul').text
    print(soil)
    moisture = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[4]/div/div/div[2]/ul/li[1]/p').text
    print(moisture)
    pH = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[4]/div/div/div[2]/ul/li[3]/p').text
    print(pH)

    """Size"""
    ultimate_height = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[5]/div/div/div/ul/li[1]/p').text
    print(ultimate_height)
    ultimate_spread = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[5]/div/div/div/ul/li[2]/p').text
    print(ultimate_spread)
    time_to_ultimate_height = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[5]/div/div/div/ul/li[3]/p').text
    print(time_to_ultimate_height)

    """How to Grow"""
    cultivation = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[3]/div[1]/div[1]/p[1]').text
    print(cultivation)
    propagation = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[3]/div[1]/div[1]/p[2]').text
    print(propagation)
    suggested_planting_locations = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[3]/div[1]/div[1]/p[3]').text
    print(suggested_planting_locations)

    """How to Care"""
    pruning = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[3]/div[1]/div[2]/p[1]').text
    print(pruning)
    pests = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[3]/div[1]/div[2]/p[2]').text
    print(pests)
    diseases = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[3]/div[1]/div[2]/p[3]').text
    print(diseases)

    """Colour in Season Images"""
    all_autumn_imgs = [img.get_attribute('src') for img in driver.find_elements_by_xpath('.//div[1]/ul/li/div/div/img')]
    print(all_autumn_imgs)
    all_spring_imgs = [img.get_attribute('src') for img in driver.find_elements_by_xpath('.//div[2]/ul/li/div/div/img')]
    print(all_spring_imgs)
    all_summer_imgs = [img.get_attribute('src') for img in driver.find_elements_by_xpath('.//div[3]/ul/li/div/div/img')]
    print(all_summer_imgs)
    all_winter_imgs = [img.get_attribute('src') for img in driver.find_elements_by_xpath('.//div[4]/ul/li/div/div/img')]
    print(all_winter_imgs)
    sleep(5)
    
    pollinator_plants_data_dict = {
      'ScientificName': scientific_name,
      'CommonName': common_name,
      'OtherCommonNames': other_common_names,
      'Family': family,
      'Genus': genus,
      'PlantRange': plant_range,
      # 'PollinatorPerfect': pollinator_perfect,
      'Foliage': foliage,
      'Habit': habit,
      'Hardiness': hardiness,
      'Sunlight': sunlight,
      'Aspect': aspect,
      'Exposure': exposure,
      'Soil': soil,
      'Moisture': moisture,
      'pH': pH,
      'UltimateHeight': ultimate_height,
      'UltimateSpread': ultimate_spread,
      'TimeToUltimateHeight': time_to_ultimate_height,
      'Cultivation': cultivation,
      'Propagation': propagation,
      'SuggestedPlantingLocation': suggested_planting_locations,
      'Pruning': pruning,
      'Pests': pests,
      'Diseases': diseases,
      'ColourInAutumn': all_autumn_imgs,
      'ColourInSpring': all_spring_imgs,
      'ColourInSummer': all_summer_imgs,
      'ColourInWinter': all_winter_imgs,
    }
    colours_autumn = {
      'CommonName': common_name,
      'ScientificName': scientific_name,
      'ColourInAutumn': all_autumn_imgs,
    }
    colours_spring = {
      'CommonName': common_name,
      'ScientificName': scientific_name,
      'ColourInSpring': all_spring_imgs,
    }
    colours_summer = {
      'CommonName': common_name,
      'ScientificName': scientific_name,
      'ColourInSummer': all_summer_imgs,
    }
    colours_winter = {
      'CommonName': common_name,
      'ScientificName': scientific_name,
      'ColourInWinter': all_winter_imgs,
    }
    pollinator_plants_data.append(pollinator_plants_data_dict)
    colour_imgs_autumn.append(colours_autumn)
    colour_imgs_spring.append(colours_spring)
    colour_imgs_summer.append(colours_summer)
    colour_imgs_winter.append(colours_winter)
  except: Exception
  pass

#%%
print(len(pollinator_plants_list))

#%%
import pandas as pd
df = pd.DataFrame(pollinator_plants_data)
print(df)

#%%
df.to_csv('pollinator_plants_data_50.csv')

#%%
driver.quit()

#%%
import pandas as pd

df.to_csv('pollinator_plants_data.csv', mode='a')

# %%
