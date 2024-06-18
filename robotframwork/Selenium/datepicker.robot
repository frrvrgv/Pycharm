*** Settings ***
Library  SeleniumLibrary


*** Variables ***

*** Test Cases ***
Verify screenshot
    Open Browser       https://jqueryui.com/datepicker/      Chrome
    Maximize Browser Window
    Wait Until Element Is Visible    xpath://h3[normalize-space()='Datepicker']         timeout=5
    Sleep    3s
    Click Element         //input[@id='datepicker']
    Sleep    3s
    Click Element            //tbody/tr[1]/td[1]
    Sleep    3s
    Close Browser