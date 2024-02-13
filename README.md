<div align="center">

  <img src="assets/logo.jpeg" alt="logo" width="200" height="auto" />
    </a>
  <h1>Github Blog Sitemap Updater</h1>
  <p>
  
```plaintext
    This project provides an automation script to enhance the SEO (Search Engine Optimization) of your GitHub blog by automatically updating the sitemap.xml file every time you commit to GitHub. The sitemap.xml file helps search engines understand the structure of your website, improving your website's search engine rankings.
```
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

The structure of the `sitemap.xml` we will scrape looks like this:

<div align="center"> 
  <img width="1414" alt="image" src="https://github.com/uujeong/sitemap.xml_generator_for_SEO/assets/86465999/08d47d3d-d86c-415e-90ac-113ca19ff74b">
</div>

<!-- Features -->

### Features

- Automatically generates and updates the sitemap.xml for GitHub blogs.
- Sets up a Git Hook for automatic execution before commits.
- Utilizes Selenium and undetected_chromedriver for web scraping.

<!-- Env Variables -->

### Environment Variables

To run this project, you will need to install some packages, and the following environment variables:

<!-- Getting Started -->

## Getting Started

### Library

- `selenium`
- `undetected_chromedriver`
- `fake_useragent`
- `selenium_stealth`

### Installation

Virtual Environment is recommended to install the project.

- I used conda to create a virtual environment.

  ```bash
  conda create -n env_name python = version
  ```

- I used ...

  ```bash
  conda create -n gh-sitemap python = 3.10
  ```

### Run Locally

- Clone the project

  ```bash
  git clone https://github.com/uujeong/
  sitemap.xml_generator_for_SEO.git
  ```

- Go to the project directory

  ```bash
  cd my-project
  ```

* Activate the virtual environment

  ```bash
  conda activate env_name
  ```

* Install dependencies

  ```bash
  pip install -r requirements.txt
  ```

### Apply in your Website

1. Create a Git Hook Script:  
   In the .git/hooks directory, create a file named pre-commit. If a pre-commit file already exists, you can add to it. You can also copy the .git/hooks/pre-commit.sample file for use.

2. Edit the pre-commit Script:  
   Add the following script to the pre-commit file. This script runs the main.py script to generate and commit the updated sitemap.xml.

   ```bash
   #!/bin/sh

   # Run main.py script to update sitemap.xml
   python path/to/main.py

   # Check if sitemap.xml has been updated and stage it

   git add sitemap.xml
   ```

3. Grant Execution Permissions: Give the script execution permissions by running:

   ```sh
   chmod +x .git/hooks/pre-commit
   ```

Now, each time you commit to GitHub, the pre-commit hook will run the `main.py` script, automatically generating and updating the sitemap.xml file. This updated file will be automatically included in your commit and uploaded to GitHub when you push.

## License

See [MIT LICENSE](https://github.com/uujeong/sitemap.xml_generator_for_SEO/blob/main/LICENSE) for more information.

## Contact

[YU JEONG, KIM](https://uujeong/github.io)  
💌 u.j.kinn@gmail.com
