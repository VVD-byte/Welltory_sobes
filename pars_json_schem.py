from jsonschema import validate, ValidationError
import json
import os
import logging

logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, filename='logging.log', format='%(message)s')

class pars:
    def __init__(self):
        self.json_files = os.listdir('./task_folder/event')
        self.schema_files = os.listdir('./task_folder/schema')
        self.html = '<table border=2px><tr><th>Файл json\файл schema</th>' + ''.join(['<th>' + i + '</th>' for i in self.schema_files]) + '</tr>'

    def all_file(self):
        for i in self.json_files:
            self.html += '<tr><td>' + i + '</td>'
            for j in self.schema_files:
                res = self.proof(i, j)
                self.html += '<td>' + res + '</td>'
                logging.debug(f'json: {i}\t schema: {j}\t result:{res}')
            self.html += '</tr>'
            logging.debug('')
        self.html += '</table>'

        with open('dat.html', 'w') as t:
            t.write(self.html)

    def proof(self, i, j):
        try:
            validate(instance = self.open('./task_folder/event/' + i), schema = self.open('./task_folder/schema/' + j))
        except ValidationError as e:
            return e.message
        return '+'

    @staticmethod
    def open(src):
        with open(src, 'r') as t:
            return json.loads(t.read())