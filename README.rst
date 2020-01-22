** Convert Dict to CSV **
=========================

**What python version is supported?**
-------------------------------------

- Python 3.6

**Using:**
----------
::

    t = to_csv(xParce(<dict>))
    t._delimiter = ';'
    t._codepage = 'utf8'

    t.save_all()
    # Или
    t.save_one('filename(имя обьекта)', path='./', header=None)

