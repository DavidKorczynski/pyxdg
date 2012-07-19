#!/usr/bin/python
from xdg.DesktopEntry import *

import resources

import os, sys
import shutil
import re
import tempfile
import unittest

class DesktopEntryTest(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.tmpdir, "gedit.desktop")
        with open(self.test_file, "w") as f:
            f.write(resources.gedit_desktop)
    
    def tearDown(self):
        shutil.rmtree(self.tmpdir)
    
    def test_write_file(self):
        de = DesktopEntry()
        de.parse(self.test_file)
        de.removeKey("Name")
        de.addGroup("Hallo")
        de.set("key", "value", "Hallo")
        
        path = os.path.join(self.tmpdir, "test.desktop")
        de.write(path)
        
        with open(path) as f:
            contents = f.read()
        
        assert "[Hallo]" in contents, contents
        assert re.search("key\s*=\s*value", contents), contents
    
    def test_validate(self):
        entry = DesktopEntry(self.test_file)
        self.assertEqual(entry.getName(), 'gedit')
        entry.validate()
