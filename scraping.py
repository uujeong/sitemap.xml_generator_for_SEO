import undetected_chromedriver as uc
from fake_useragent import UserAgent
from selenium_stealth import stealth

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def make_url(github_name):
    return f"https://{github_name}.github.io/sitemap.xml"

def set_driver():
    options = uc.ChromeOptions()
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument(f'--user-agent={UserAgent().random}')
    
    driver = uc.Chrome(options=options, enable_cdp_events=True, incognito=True, headless=True, use_subprocess=False)
    stealth(driver,
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Google Inc. (NVIDIA)",
        renderer="GeForce GTX 1050/PCIe/SSE2",
        fix_hairline=True,
    )
    return driver

def scrape_sitemap(github_name):
    url = make_url(github_name)
    driver = set_driver()
    driver.get(url)

    try:
        # 웹페이지가 완전히 로드될 때까지 기다립니다.
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "webkit-xml-viewer-source-xml")))

        # 'webkit-xml-viewer-source-xml' div의 내부 HTML을 가져옵니다.
        content = driver.find_element(By.ID, "webkit-xml-viewer-source-xml").get_attribute('innerHTML')

        # 필요한 XML 부분만 추출합니다.
        start = content.find('<urlset')
        end = content.rfind('</urlset>') + len('</urlset>')
        xml_content = content[start:end]

    except TimeoutException:
        print("요소를 찾는 데 시간이 너무 오래 걸립니다.")
        xml_content = ""
    finally:
        driver.quit()

    return xml_content
