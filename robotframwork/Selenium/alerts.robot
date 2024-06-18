*** Settings ***
Library      SeleniumLibrary

*** Variables ***

${browser}          chrome
${url}              https://chercher.tech/practice/practice-pop-ups-selenium-webdriver

*** Test Cases ***
RadioButton
          open browser       ${url}        ${browser}
          maximize browser window
          Sleep     4s
          Click Element      xpath://input[@name='alert']
          Sleep     4s
          # simple alert
          ${alertmessage} =   Handle Alert    action =   ACCEPT timeout=3
          Log To Console          ${alertmessage}
          # confirmational alert
          Click Element       xpath://input[@name='confirmation']
          Sleep      4s
          ${alertmessage} =Handle Alert        action           =              DISMISS timeout=3
          Log To Console           ${alertmessage}
          # prompt alert
          Click Element        xpath://input[@name='prompt']
          Sleep       4s

           # prompt alert
           Input Text Into Alert          Users        timeout=3
           ${alertmessage}= Handle Alert action        =         ACCEPT timeout=3
           Log To Console     ${alertmessage}
           ${alertmessage} = Handle Alert action=ACCEPT timeout=3
           Log To Console     ${alertmessage}
