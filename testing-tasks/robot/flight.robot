*** Settings ***
Library     SeleniumLibrary
Library      String
Suite Setup  Generate Random String

*** Variables ***
${URL}       http://blazedemo.com/
${Browser}    Chrome
${PageText}    Welcome to the Simple Travel Agency!
${DepartureCity}    Departs: Boston
${ArrivalCity}    Arrives: Cairo


*** Test Cases ***
Check
    Open Browser    ${URL}    ${Browser}
    Page Should Contain    ${PageText}
