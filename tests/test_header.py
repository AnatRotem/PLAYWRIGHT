import re
from playwright.sync_api import Page, expect
from pages.header_page import headerPage
from pages.base_page import BasePage


def test_header_is_displayed(page: Page) -> None:
    
    #base_page = BasePage(page)
    #base_page.navigate()
    
    header_page = headerPage(page)
    header_page.navigate()
    
    header_texts = ["ID", "Name", "Family"]

    header = page.locator(header_page.HEADER)
    header_cells = header.locator(header_page.HEADER_CELLS)
    
    for text in header_texts:
        expect(header_cells.filter(has_text=text)).to_be_visible()


def test_the_layout_of_the_header (page: Page) -> None:
    pass #TBD

    
def test_pls(page: Page) -> None:
    
    body = page.locator('//tbody')
    rows = body.locator('//tr')
    first_row = rows.locator('nth=0')
    cells = first_row.locator('//td').all()
    cell = rows.locator('//td[text=1]')
   
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
 
        
   




        
            
        
    
    
    

