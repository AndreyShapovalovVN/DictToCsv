import csv
import os
from uuid import uuid4


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
        return list(head)

    def clear(self):
        self.data = {}

    def save_all(self, path='./'):
        for k in self.data.keys():
            self.save_one(k, path=path)
        self.clear()

    def save_one(self, file, path='./', header=None):
        if self.data.get(file):
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
