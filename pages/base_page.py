from playwright.sync_api import sync_playwright, Page

class BasePage: 
    
    URL = 'http://localhost:3000/'
    
    def __init__(self, page: Page):
        self.page = page
        self.TABLE = self.page.locator('//table')

        
    def navigate(self):
        self.page.goto(self.URL)
   
    
    
    
    



    