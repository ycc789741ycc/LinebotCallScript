from selenium import webdriver
from selenium.webdriver.common.by import By                     
from selenium.webdriver.support.ui import WebDriverWait                                                            
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os

class AutoFillForm():
    """
    YourForm = "File.txt"
    """
    def __init__(self,YourForm):
        with open(YourForm,'rb') as f:
            self.element_word = [item.decode('utf-8','ignore').split(sep="|")[1] for item in f.readlines()]
        assert len(self.element_word)>=9

    def start(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeLgTOiwG0yz-Shi_HreeV5Krm3mhwKR2X2_jCDPzXQ0iYdNA/viewform")

        element1_Xpath = r"//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input"
        element1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element1_Xpath)))
        element1.send_keys(self.element_word[0])

        element2_Xpath = r"//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input"
        element2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element2_Xpath)))
        element2.send_keys(self.element_word[1])

        element3_Xpath = r"//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input"
        element3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element3_Xpath)))
        element3.send_keys(self.element_word[3])

        element4_Xpath = r"//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input"
        element4 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element4_Xpath)))
        element4.send_keys(self.element_word[4])

        element5_Xpath = r"//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input"
        element5 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element5_Xpath)))
        element5.send_keys(self.element_word[5])

        element6_Xpath = r"//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input"
        element6 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element6_Xpath)))
        element6.send_keys(self.element_word[8])

        '''
        element7_Xpath = r"//*[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input"
        element7 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element7_Xpath)))
        element7.send_keys(self.element_word[6])

        choice = int(self.element_word[7].strip())
        element8_Xpath=None
        if(choice==1):
            element8_Xpath = r"//*[@id='i33']/div[3]/div"
        else:
            element8_Xpath = r"//*[@id='i36']/div[3]/div"
        element8 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element8_Xpath)))
        element8.click()

        element9_Xpath = r"//*[@id='mG61Hd']/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input"
        element9 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element9_Xpath)))
        element9.send_keys(self.element_word[8])
        '''

        scrollelement_Xpath = r"//*[@id='i32']/div[3]/div"
        scrollelement = driver.find_element_by_xpath(scrollelement_Xpath)
        scrollelement.location_once_scrolled_into_view

        element10_Xpath = r"//*[@id='i32']/div[3]/div"
        element10 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element10_Xpath)))
        element10.click()

        
        element11_Xpath = r"//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div/div/span/span"
        element11 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element11_Xpath)))
        element11.click()
        

        elementcheck_Xpath = r"/html/body/div[1]/div[2]/div[1]/div/div[4]/a"
        
        result = None

        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, elementcheck_Xpath)))
            result = self.element_word[0]
        except:
            driver.close()
            raise RuntimeError

        check = driver.current_url.split(r"/")
        check = check[len(check)-1]
        print(check)
        if('formResponse' in check):
            print("回報成功")
        else:
            print("回報失敗")
            raise RuntimeError

        driver.close()
        #os.system("pause")
        return result

if __name__ == '__main__':
    Script = AutoFillForm("YourForm.txt")
    Script.start()
    