*** Settings ***
Library  SeleniumLibrary

*** Variables ***

${browser}        chrome
${url}            https://rahulshettyacademy.com/seleniumPractise/#/

*** Test Cases ***
Test Automation on Rahul Shetty Academy
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    Sleep    2s
    Click Element      div.container div.products-wrapper:nth-child(2) div.products div.product:nth-child(1) div.product-action > button:nth-child(1)
    Click Element      div.container div.products-wrapper:nth-child(2) div.products div.wrapperTwo div:nth-child(3) > select:nth-child(1)
    Log to Console   Output
    Close Browser
