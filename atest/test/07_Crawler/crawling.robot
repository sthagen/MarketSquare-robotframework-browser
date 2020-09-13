*** Settings ***
Resource    ../keywords.resource

*** Test Cases ***
Crawling
   ${urls}=  Crawl site  reaktor.com