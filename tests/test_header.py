import re
from playwright.sync_api import Page, expect
from pages.header_page import headerPage
from pages.base_page import BasePage


def test_header_is_displayed(page: Page) -> None:
    
    header_page = headerPage(page)
    header_page.navigate()
    
    header_texts = ["ID", "Name", "Family"]

    header = page.locator(header_page.HEADER)
    header_cells = header.locator(header_page.HEADER_CELLS)
    
    for text in header_texts:
        expect(header_cells.filter(has_text=text)).to_be_visible()


def test_the_layout_of_the_header (page: Page) -> None:
    pass #TBD

    
def test_cell(page: Page) -> None:
    
    body = page.locator('//tbody')
    rows = body.locator('//tr')
    first_row = rows.locator('nth=0')
    cells = first_row.locator('//td').all()
  

    
    members = {}

 
        
   




        
            
        
    
    
    

