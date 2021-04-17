"""
"Emdee five for life" web-challenge solution

https://app.hackthebox.eu/challenges/Emdee-five-for-life
"""
import sys

import hashlib
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


def hash_md5(string):
    """
    Encrypting a string using the md5 algorithm
    """
    hash_obj = hashlib.md5(string.encode())
    return hash_obj.hexdigest()


def encrypt(url):
    """
    Finding a string for a hash
    Hashing
    Entering a hash into a form
    Submitting a form
    """
    driver.get(f"http://{url}")

    str_for_hash = driver.find_element_by_xpath('//h3[@align="center"]')
    hash_string = hash_md5(str_for_hash.text)

    search_form = driver.find_element_by_name('hash')
    search_form.send_keys(hash_string)
    search_form.submit()


if __name__ == '__main__':
    web_url = sys.argv[1]
    encrypt(web_url)
