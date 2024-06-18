*** Settings ***
Library     SeleniumLibrary


*** Variables ***

*** Test Cases ***
Verify screenshot
             Open Browser             https://the-internet.herokuapp.com           Chrome
             Wait Until Element Is Visible          xpath://h1[normalize-space()='Welcome to the-internet']            timeout=5
             Capture Page Screenshot                C:/Users/Administrator/Downloads/IMG-20240522-WA0011
             Capture Element Screenshot             xpath://h2[normalize-space()='Available Examples']  C:/Users/Administrator/Downloads/IMG-20240522-WA0011
             Close Browser
