import logging
import subprocess
import sys
import os

class RIOT():
    def __init__(self, fullname, binary, session_name, tap):
        self.fullname = fullname
        self.binary = "/tmp/olsr_node.elf"
        self.session_name = session_name
        self.tap = tap
        self.pid = self.fullname

        self.logger = logging.getLogger("")

    def create(self):
	os.system("xterm -e gdb -ex run --args " + self.binary + " " + self.tap + " &")
	return True

    def destroy(self):
	return True

    def isActive(self):
	return False

    def exist(self):
        return True

    def __str__(self):
        return "%s %s" % (self.binary, self.tap)
