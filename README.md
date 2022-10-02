# DISCLAIMERS

* emulate_dos is a project that was made in order for me to learn
how DOS (Denial of Service) attacks work and to attempt to SAFELY emulate one, in a controlled environment.
* I do NOT perform hacking, except for educational purposes.
* I do NOT condone the act of malicious hacking.
* This project is for educational purposes ONLY.
* I take NO responsibility for anything that occurs from
anyone who uses this project in any capacity.
* This project was tested against my computer's localhost IP address.

## How To Run

1. Have python3 installed
2. Clone the project repo
3. Open your computer's terminal
4. Enter the emulate_dos directory
5. In the terminal, enter the following command: python3 main.py

## Design

This project was desinged by implementing a Dispatcher design pattern.
The BotDispatcher creates and manages the user-defined amount of Bot objects. Once a Bot object is created, it is put in it's own thread
and it is used to ping the user-defined host address. Then the Bots success status is recorded in the form of a STATUS enum. Lastly, the BotDispatcher's evluate() function displays which Bots
succeeded and which Bots failed.
