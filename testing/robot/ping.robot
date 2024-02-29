*** Settings ***
Library   OperatingSystem
Library   Collections
Library   String

# Mona Achaaoud

*** Test Cases ***
Read adresses for ping command from a file
   ${path}=   Set Variable   C:/monaAchd/Software-Testing/testing/robot/webpages.txt
   ${output}=   Get File    ${path}
   ${addresses}=   Split String   ${output}
   Set Global Variable    ${addresses}

*** Test Cases ***
Find out IP, average ping time in loop and create result file
   ${path}=   Set Variable   C:/monaAchd/Software-Testing/testing/robot/webpages.txt
   ${output}=   Get File    ${path}
   ${addresses}=   Split String   ${output}
   Set Global Variable    ${addresses}
    ${Length}=   Get Length    ${addresses}  
   Should Be Equal As Numbers     ${length}  3
   FOR    ${index}    IN RANGE    ${length}
              ${output}=    Run and return rc and output   ping ${addresses}[${index}]
       Log    ${output}
   END
   
Get IPv4 Adress Info
   ${result}=   Run And Return Rc And Output    ipconfig
   @{output}=   Split String   ${result}[1]
   Set Global Variable    ${output}
   Log   ${output}
   ${index}=   Get Index From List   ${output}   Subnet
   ${index}=   Evaluate   ${index}-1
   ${IPAdress}=   Set Variable   ${output}[${index}]
   
Create result file
   ${path}   Set Variable   C:/monaAchd/Software-Testing/testing/robot/
   Create File    ${path}result.txt     172.24.160.1

  


   
