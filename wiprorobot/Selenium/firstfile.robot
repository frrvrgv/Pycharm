*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}      chrome
${url}          https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

*** Test Cases ***
LoginTest
        open browser    ${url}    ${browser}
        Sleep  4S
        loginToapplication
        close browser

*** Keywords ***
loginToapplication
        maximize browser window
        Sleep  4S
        input Text  xpath://input[@name='username']   Admin
        input Text  xpath://input[@name='password']   admin123
        Sleep  2S
        click Element   xpath://button[@type='submit']
        Sleep  2S