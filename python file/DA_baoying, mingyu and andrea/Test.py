import unittest
import Browser
import subprocess
import os
import json


class TestBrowser(unittest.TestCase):

    def test_status(self):
        self.assertTrue(Browser.r.status_code == 200) #assert true is to double cfm the server will reply ok

    def test_user_agent(self):
        header_dict = eval(Browser.rh.text)
        self.assertTrue(header_dict['headers']['User-Agent'] == 'Mobile')

    def test_scrappy_jpg(self):
        if os.path.exists('./results.json'):
            os.remove('./results.json')
        subprocess.Popen(['scrapy', 'runspider', 'Scrapy.py', '-o', 'results.json', '-t', 'json']).wait() #run scrapy script 10c
        results_file = open('results.json', 'r') #produce json file
        scrappy_output = json.load(results_file)
        results_file.close()
        for entries in scrappy_output:
            for key in entries.keys():
                if key == 'Image Link': #jpg
                    self.assertTrue(str(entries[key]).endswith('jpg') or str(entries[key]).endswith('jpeg'))  #makesure extract jpg file



if __name__ == '__main__':
    unittest.main()
