# Python_Hw1

Desciption:
(Module1) = file
When you use an automated teller machine (ATM) with your bank card, you need to use a
personal identification number (PIN) to access your account. If a user fails more than three times when
entering the PIN, the machine will block the card.

1. create a python module to support the scenario described above. Assume the user’s PIN is “1234” and write a program that asks the user for the PIN no more than three times, and does the following:

  • If the user enters the right number, print a message saying, “Your PIN is correct”, and end the
  program
  • If the user enters a wrong number, print a message saying, “Your PIN is incorrect” and if you
  have asked for the PIN less than three times, ask for it again.
  • If the user enters the wrong number three times, print the message, “Your bank card is blocked”
  and end the program with an exit code of 1.
  • Your input should be taken using a definition called GetInput(). In there, you will return the pin
  if it is valid:
