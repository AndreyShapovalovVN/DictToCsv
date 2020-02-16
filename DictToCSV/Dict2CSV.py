import csv
import os
from uuid import uuid4
from collections import OrderedDict


class to_csv:
    _delimiter = ';'
    _codepage = 'utf8'

    def __init__(self, data=None):
        self.data = data or {}

    @property
    def header(self):
        data = self.data.get(self.file)
        head = {}
        for i in range(len(data)):
            head = head | data[i].keys()
        header = list(head)
        header.sort()
        return header

    def clear(self):
        self.data = {}

    def save_all(self, path='./'):
        for k in self.data.keys():
            self.save_one(k, path=path)
        self.clear()

    def save_one(self, file, path='./', header=None):
        if not self.data.get(file):
            raise NameError("'file' - not found keys from data")

        self.file = file
        out_csv = csv.DictWriter(
            open(os.path.join(path, '.'.join((file, 'csv'))),
                 'w',
                 encoding=self._codepage),
            fieldnames=header or self.header,
            delimiter=self._delimiter
        )
        out_csv.writeheader()
        out_csv.writerows(self.data[file])

    def xSave_one(self, file, path='./', header=None):
        if not isinstance(header, OrderedDict):
            raise TypeError("'header' not collections.OrderedDict")
        if not self.data.get(file):
            raise NameError("'file' - not found keys from data")

        csv_header = list(header.keys())
        out_csv = csv.DictWriter(
            open(os.path.join(path, '.'.join((file, 'csv'))),
                 'w', encoding=self._codepage),
            fieldnames=csv_header,
            delimiter=self._delimiter
        )
        out_csv.writeheader()

        for line in self.data.get(file):
            out_csv.writerow({i: line.get(header[i]) for i in csv_header})

    def xParce(self, data, parent, id=uuid4().hex, p_id=None):
        response = {'id': id, 'p_id': p_id}
        for item in data:
            if not self.data.get(parent):
                self.data[parent] = []

            if isinstance(data[item], list):
                for list_item in data[item]:
                    self.xParce(list_item, item, id=uuid4().hex, p_id=id)

            elif isinstance(data[item], type(None)):
                response[item] = None

            elif isinstance(data[item], str):
                response[item] = data[item]

            elif isinstance(data[item], int):
                response[item] = data[item]

            elif isinstance(data[item], float):
                response[item] = data[item]

            else:
                self.xParce(data[item], item, id=id, p_id=p_id)

        if len(response) > 2:
            self.data[parent].append(response)
        else:
            del self.data[parent]
