# ProofOfConcept KeePass Attack

## This code is referenced under the KeePass section of the report

Short program that demonstrates the vulnerability KeePass version 2.0

## How to replicate the vulnerability
1. Open KeePassXC and authenticate the database by logging in
2. While the database is authenticated, create a memory dump file for it
   by selecting first keePass -> Create Dump File
  
3. Finally, you can run this command: python poc.py [Path to Dump File]

  So if the dump was in the same directory and named KeePass.DMP, the command would be:

     python poc.py KeePass.DMP

Once the memory dump file is created, the attack can be performed even if the database is locked again or if KeePass is closed.

The provided Python code performs all of these steps, and it attempts multiple password guesses based on the text files provided.
