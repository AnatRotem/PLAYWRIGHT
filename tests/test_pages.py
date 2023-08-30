import re
import selectors
from playwright.sync_api import Page, expect
from pages.header_page import headerPage
from pages.base_page import BasePage

    
def test_cell(page: Page) -> None:
    
    base_page = BasePage(page)
    base_page.navigate()
    
    body = page.locator('//tbody')
    rows = body.locator('//tr')
    first_row = rows.locator('nth=0')
    cells_of_first_row = first_row.locator('//td').all()
    cell = rows.locator('//td[text=1]')
    
    
    #base_page.screenshot(path='myScreenshot.png')
    #for cell in cells:
        #cell_text = cell.text_content()
        #print("Cell Text: ", cell_text)
        
    #anats = page.locator('td[class=MuiTableCell-root]').all()
    #for cell in cells:
    #    text = cell.inner_text()
    #    print(text)
    #page.wait_for_selector(body)
    #cell = page.locator('.MuiTableRow-root:nth-child(2) .MuiTableCell-root:nth-child(2)')
    #cell_text = cell.inner_text()
    #print("Cell Text: ", cell_text)
    
 
    

    #cells_of_first_row1 = selectors.setTestIdAttribute()
    #print(cells_of_first_row1)
    
    members = {}
  
    #for tr in body.all():
   # for row in rows:
    #    cells = row.locator('td')
        
        # Create a dictionary for each row
    #    member = {
     #       'id': cells[0].inner_text(),
      #      'name': cells[1].inner_text(),
       #     'family': cells[2].inner_text()
        #}
        
        #ssmembers.append(member)   
        
    #print(members)
 
        
   




        
            
        
    
    
    

