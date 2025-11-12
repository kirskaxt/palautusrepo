*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  masa  masa123456
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  masa1234567
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ol  ol1234567
    Output Should Contain  Username is too short

Register With Enough Long BUt Invalid Username And Valid Password
    Input Credentials  päivi  keke123456
    Output Should Contain  Username contains invalid characters

Register With Valid Username And Too Short Password
    Input Credentials  jorma  salis2
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  jorma  salasanani
    Output Should Contain  Password cannot contain only letters


*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123
    