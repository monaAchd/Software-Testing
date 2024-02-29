*** Settings ***
Library   String

*** Variables ***
${one}   Donald
${two}   Duck

*** Test Cases ***
Check outcome
   ${three}=   Set Variable   Donald Duck
   Should Be Equal   ${one} ${two}   ${three}
