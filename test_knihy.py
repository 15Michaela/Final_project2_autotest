import pytest
from playwright.sync_api import Page, expect

#Test 1: Kontrola funkčnosti tlačítka "Přihlášení"
# Po kliknutí na tlačítko "Přihlášení" se objeví přihlašovací tabulka

def test_zobrazeni_prihlaseni(page: Page):
    page.goto("https://www.knihydobrovsky.cz/")

    #Odklik cookies
    page.get_by_role("button", name="Povolit vše").click()

    #Klik na tlačítko "Přihlášení"
    page.get_by_label("Přihlášení").click()

    #Ověření, zda je vidět přihlašovací okno - vidím e-mail/heslo
    expect(page.get_by_text("E-mail", exact=True)).to_be_visible()
    expect(page.get_by_text("Heslo", exact=True)).to_be_visible()

    #Druhé ověření, zda je vidět tlačítko "Zapomenuté heslo" + klik
    expect(page.get_by_role("link", name="Zapomenuté heslo")).to_be_visible()
    page.get_by_role("link", name="Zapomenuté heslo").click()




# Test 2: Ověření zobrazení košíku
# Po kliknutí na košík se ověří, že je zobrazen text "Váš košík je prázdný"
# Po přidání knihy do košíku se zde objeví

def test_kontrola_kosiku(page: Page):
    page.goto("https://www.knihydobrovsky.cz/")

    #Odklik cookies
    page.get_by_role("button", name="Povolit vše").click()

    #Klik na košík
    page.get_by_label("Košík", exact=True).click()

    #Ověření zobrazení textu
    expect(page.get_by_role("heading", name="Váš košík je prázdný")).to_be_visible()





# Test 3: Ověření funkce vyhledávání
# Po zadání názvu knihy do vyhledávacího pole a kliknutí na lupu
# se ověří, že se mezi výsledky nachází "Dvůr trnů a růží"

def test_kontrola_funkce_vyhledavani(page: Page):
    page.goto("https://www.knihydobrovsky.cz/")

    #Odklik cookies
    page.get_by_role("button", name="Povolit vše").click()
    
    #Najdi a klikni do vyhledávacího pole - počkej, až bude vidět
    search_input = page.locator("input#search")

    #Vložení hledaného textu "Dvůr trnů a růží"
    search_input.fill("Dvůr trnů a růží")

    #Klik na lupu - vyhledání
    page.get_by_role("button", name=" Vyhledat").click()

    #Ověření - je vidět hledaný název
    expect(page.get_by_role("link", name="Dvůr trnů a růží", exact=True).first).to_be_visible()
    
   