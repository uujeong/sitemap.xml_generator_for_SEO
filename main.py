from scraping import scrape_sitemap

def main():
    # 깃허브 계정명을 입력
    github_name = "uujeong"
    xml_content = scrape_sitemap(github_name)
    
    if xml_content:
        with open('sitemap.xml', 'w', encoding='utf-8') as file:
            file.write(xml_content)
            print(f"파일이 저장되었습니다.")
    else:
        print("스크랩한 데이터가 없습니다.")

if __name__ == "__main__":
    main()
