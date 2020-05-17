Установка
---------

**Примечание**: инструкция выполняется относительно папки с проектом (*my_portfolio*) под *Linux* системой.

Установить pipenv https://docs.pipenv.org/

.. code-block:: bash

    $ pip install pipenv


Установить зависимости проекта, включая зависимости для разработки

.. code-block:: bash

    $ pipenv install --dev

Активировать virtualenv проекта

.. code-block:: bash

    $ pipenv shell

Запустить миграции

.. code-block:: bash

    $ python manage.py migrate

Запуск сервера

.. code-block:: bash

    $ python manage.py runserver