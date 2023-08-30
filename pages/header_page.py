#from playwright.sync_api import sync_playwright, expect 
import re
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class headerPage(BasePage):
    
    #mapping of elements identifiers used in the header of the table
    HEADER = '//thead'
    HEADER_CELLS = '//th'
    
    def __init__(self, page: Page):
        super().__init__(page)
        
        #self.page = page
        #self.HEADER = self.page.locator('//thead')
        #self.HEADER_ID = self.HEADER.locator('//th').filter(has_text="ID")
        #self.HEADER_NAME = self.HEADER.locator('//th').filter(has_text="Name")
        #self.HEADER_FAMILY = self.HEADER.locator('//th').filter(has_text="Family")
        

   
   