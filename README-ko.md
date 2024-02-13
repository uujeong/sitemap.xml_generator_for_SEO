<div align="center">

  <img src="assets/logo.jpeg" alt="logo" width="200" height="auto" />
    </a>
  <h1>Github Blog Sitemap Updater</h1>
  <p>

    이 프로젝트는 깃허브 블로그의 SEO(Search Engine Optimization)를 향상시키기 위해, 깃허브에 커밋할 때마다 자동으로 sitemap.xml 파일을 업데이트하는 자동화 스크립트를 제공합니다. sitemap.xml 파일은 웹사이트의 구조를 검색 엔진에 알려주어, 웹사이트의 검색 엔진 순위를 개선하는 데 도움을 줍니다.

  </p>
<br />
<!-- Badges -->
<p>
  <a href="https://github.com/uujeong/sitemap.xml_generator_for_SEO/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/uujeong/awesome-readme-template" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/uujeong/awesome-readme-template" alt="last update" />
  </a>
  <a href="https://github.com/uujeong/sitemap.xml_generator_for_SEO/network/members">
    <img src="https://img.shields.io/github/forks/uujeong/sitemap.xml_generator_for_SEO" alt="forks" />
  </a>
  <a href="https://github.com/uujeong/sitemap.xml_generator_for_SEO/stargazers">
    <img src="https://img.shields.io/github/stars/uujeong/awesome-readme-template" alt="stars" />
  </a>
  <a href="https://github.com/uujeong/sitemap.xml_generator_for_SEO/issues/">
    <img src="https://img.shields.io/github/issues/uujeong/awesome-readme-template" alt="open issues" />
  </a>
    <a href="https://github.com/uujeong/sitemap.xml_generator_for_SEO/blob/master/LICENSE"><img src="https://img.shields.io/npm/l/tabler.svg?label=License&message=MIT&color=1c7ed6" alt="License"></a>
    <a href="https://github.com/uujeong/archive/dev.zip" target="__blank"><img src="https://img.shields.io/static/v1?label=Download&message=ZIP&color=339af0" alt="Tabler preview"></a>
</p>
   
</div>

<br />

<!--한국어 번역-->

## 🇰🇷 한국어로 읽기

이 링크를 클릭하여 [한국어](./README-ko.md)로 읽을 수 있습니다.

<br />
<!-- Table of Contents -->

# Table of Contents

- [About the Project](#about-the-project)
  - [Tech Stack](#tech-stack)
  - [Features](#features)
  - [Environment Variables](#environment-variables)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Run Locally](#run-locally)
- [License](#license)
- [Contact](#contact)

<!-- About the Project -->

## About the Project

우리가 스크래핑할 `.sitemap.xml` 의 구조는 다음과 같습니다.

<div align="center"> 
  <img width="1414" alt="image" src="https://github.com/uujeong/sitemap.xml_generator_for_SEO/assets/86465999/08d47d3d-d86c-415e-90ac-113ca19ff74b">
</div>

<!-- Features -->

### Features

- 깃허브 블로그의 `sitemap.xml` 자동 생성 및 업데이트
- 커밋 전 자동 실행을 위한 Git Hook 설정
- `Selenium`과 `undetected_chromedriver`를 이용한 웹 스크랩핑

<!-- Env Variables -->

### Environment Variables

이 패키지를 실행할는데에 몇가지 파이썬 패키지 설치가 필요합니다.
개발 환경은 가상환경을 권장합니다.

<!-- Getting Started -->

## Getting Started

### Library

- `selenium`
- `undetected_chromedriver`
- `fake_useragent`
- `selenium_stealth`

### Installation

가상환경을 활용해 프로젝트를 실행하기를 권장합니다.

- 가상환경 conda 명령어를 통해 생성합니다.

```bash
  conda create -n env_name python = version
```

- 제가 사용한 명령어는 다음과 같습니다.

```bash
  conda create -n gh-sitemap python = 3.10
```

### Run Locally

- 이 프로젝트를 `git clone` 명령어로 복제합니다.

```bash
  git clone https://github.com/uujeong/
  sitemap.xml_generator_for_SEO.git
```

- 프로젝트 디렉토리로 이동합니다.

```bash
  cd my-project
```

- 가상환경을 활성화합니다.

```bash
  conda activate env_name
```

- 의존성 패키지들을 설치합니다.

```bash
  pip install requirements.txt
```

### Apply in your Website

1. Git Hook 스크립트 생성  
   : .git/hooks 디렉토리에 `pre-commit 파일`을 생성합니다. 만약 `pre-commit 파일`이 이미 존재한다면, 기존 스크립트에 추가할 수 있습니다. .`git/hooks/pre-commit.sample 파일`을 복사하여 사용할 수도 있습니다.

2. pre-commit 스크립트 편집  
   : pre-commit 파일을 편집하여 다음 스크립트를 추가합니다. 이 스크립트는 main.py 스크립트를 실행하여 sitemap.xml을 생성하고 변경사항을 커밋에 포함시킵니다.

```bash
#!/bin/sh

# sitemap.xml을 업데이트하기 위해 main.py 스크립트 실행
python path/to/main.py

# sitemap.xml이 업데이트 되었는지 확인하고 스테이징 영역에 추가

git add sitemap.xml
```

3. 실행 권한 부여:
   스크립트에 실행 권한을 부여합니다. 터미널에서 다음 명령어를 실행합니다:

```sh
chmod +x .git/hooks/pre-commit
```

이제 깃허브에 커밋을 할 때마다 pre-commit 훅이 실행되어 main.py 스크립트를 통해 sitemap.xml 파일이 자동으로 생성되고 업데이트됩니다. 이 업데이트된 sitemap.xml 파일은 커밋에 자동으로 포함되어 깃허브에 푸시될 때 함께 업로드됩니다.

## License

[MIT LICENSE](https://github.com/uujeong/sitemap.xml_generator_for_SEO/blob/main/LICENSE) 를 따릅니다.

## Contact

[YU JEONG, KIM](https://uujeong/github.io)  
💌 u.j.kinn@gmail.com
