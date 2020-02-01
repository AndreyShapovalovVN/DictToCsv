** Convert Dict to CSV **
=========================

**What python version is supported?**
-------------------------------------

- Python 3.6

**Using:**
----------
::

    from DictToCSV.Dict2CSV import * 
    
    xParce(<dict>, 'root')
    t = to_csv()
    t._delimiter = ';'
    t._codepage = 'utf8'

    t.save_all()
    # Или
    t.save_one('filename(имя обьекта)', path='./', header=None)

