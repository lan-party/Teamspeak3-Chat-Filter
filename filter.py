import telnetlib

print("Reverse text chat filter for Teamspeak 3")
print("Type /end to quit!")

HOST = 'localhost'
PORT = 25639
tmode = 2
a = 1
session = telnetlib.Telnet(HOST, PORT)

def reverse(msg):
	back = ""
	for a in range(0, len(msg)):
		back += msg[(len(msg) -1) -a]
	return back

while a == 1:
	msg= raw_input(": ")
	msg = reverse(msg)
	msg = msg.replace(" ", "\\s")
	if msg == "dne/":
		a = 0
	else:
		session.write("sendtextmessage targetmode=" + str(tmode) + " msg=" + msg + "\n")
