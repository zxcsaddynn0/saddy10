\# Итоговая работа: Автоматизация тестирования веб-приложения OpenCart



\## Описание проекта



Данный репозиторий содержит итоговую работу по настройке локального окружения с помощью Docker и написанию автотестов для веб-приложения OpenCart с использованием Selenium WebDriver и Pytest.



Проект разворачивает полноценный интернет-магазин OpenCart 4 с базой данных MariaDB и веб-интерфейсом phpMyAdmin для управления БД, а также содержит набор из 10 автотестов, проверяющих основной функционал сайта.



\## Структура проекта



&#x20;   docker/

&#x20;   ├── docker-compose.yml          # Конфигурация Docker Compose

&#x20;   ├── .env                        # Переменные окружения (порты, IP)

&#x20;   ├── README.md                   # Документация проекта

&#x20;   ├── report/                     # Отчет о проделанной работе

&#x20;   └── selenium\_tests/             # Папка с автотестами

&#x20;       ├── test\_opencart.py        # 10 автотестов на Selenium + Python

&#x20;       └── test\_report.html        # HTML-отчет о результатах тестирования



\## Компоненты системы



| Компонент    | Образ                             | Порт  | Назначение                        |

|--------------|-----------------------------------|-------|-----------------------------------|

| OpenCart     | docker.io/bitnami/opencart:4      | 8081  | Интернет-магазин                  |

| MariaDB      | docker.io/bitnami/mariadb:11.2    | 3306  | Система управления базой данных   |

| phpMyAdmin   | phpmyadmin/phpmyadmin:latest      | 8888  | Веб-интерфейс для управления БД   |



\## Требования



\- Docker Desktop с WSL 2

\- Docker Compose v2+

\- Python 3.8+

\- Google Chrome (для запуска Selenium-тестов)

\- Git



\## Инструкция по запуску



\### 1. Настройка переменных окружения



Создайте файл `.env` в корне проекта со следующим содержимым:



&#x20;   OPENCART\_PORT=8081

&#x20;   PHPADMIN\_PORT=8888

&#x20;   LOCAL\_IP=127.0.0.1



\### 2. Поднятие локального сервера



Выполните команду для запуска всех контейнеров в фоновом режиме:



&#x20;   docker compose up -d



Проверьте статус контейнеров:



&#x20;   docker ps



Сайт будет доступен по адресам:



\- OpenCart: http://localhost:8081/

\- Админ-панель OpenCart: http://localhost:8081/admin/

\- phpMyAdmin: http://localhost:8888/



\### 3. Первоначальная установка OpenCart



При первом запуске откройте в браузере:



&#x20;   http://localhost:8081/install/



Заполните параметры подключения к базе данных:



\- Hostname: `mariadb`

\- Username: `bn\_opencart`

\- Password: (оставьте пустым)

\- Database Name: `bitnami\_opencart`

\- Database Port: `3306`



Параметры администратора:



\- Username: `admin`

\- Password: `admin123`

\- E-Mail: `admin@test.com`



\### 4. Установка зависимостей для тестов



&#x20;   cd selenium\_tests

&#x20;   pip install selenium pytest pytest-html



\### 5. Запуск автотестов



&#x20;   python -m pytest test\_opencart.py -v --html=test\_report.html --self-contained-html



\### 6. Просмотр отчета о тестировании



&#x20;   start test\_report.html



\## Список автотестов



В проекте реализовано 10 автотестов, проверяющих основной функционал сайта:



| №  | Имя теста                | Описание                                |

|----|--------------------------|-----------------------------------------|

| 1  | test\_open\_main\_page      | Проверка открытия главной страницы      |

| 2  | test\_logo\_presence       | Проверка наличия логотипа               |

| 3  | test\_navigation\_menu     | Проверка наличия меню навигации         |

| 4  | test\_search\_functionality| Проверка работы поиска товаров          |

| 5  | test\_open\_category       | Открытие категории товаров              |

| 6  | test\_open\_product\_card   | Открытие карточки товара                |

| 7  | test\_add\_to\_cart         | Добавление товара в корзину             |

| 8  | test\_open\_cart           | Переход на страницу корзины             |

| 9  | test\_open\_login\_page     | Переход на страницу авторизации         |

| 10 | test\_footer\_presence     | Проверка наличия подвала сайта          |



Во всех тестах используются \*\*явные ожидания (Explicit Waits)\*\* через `WebDriverWait` в сочетании с `expected\_conditions`, что обеспечивает стабильность работы тестов при различной скорости загрузки DOM-дерева.



\## Учетные данные



\### Админ-панель OpenCart



\- URL: http://localhost:8081/admin/

\- Username: `admin`

\- Password: `admin123`



\### База данных



\- Host: `mariadb`

\- Port: `3306`

\- Database: `bitnami\_opencart`

\- User: `bn\_opencart`

\- Password: (пусто)



\### phpMyAdmin



\- URL: http://localhost:8888/

\- Username: `bn\_opencart`

\- Password: (пусто)



\## Полезные команды Docker



Остановить все контейнеры:



&#x20;   docker compose down



Остановить и удалить volumes (полный сброс):



&#x20;   docker compose down -v



Просмотр логов контейнера:



&#x20;   docker logs docker-opencart-1

&#x20;   docker logs docker-mariadb-1

&#x20;   docker logs docker-phpadmin-1



Перезапуск контейнеров:



&#x20;   docker compose restart



\## Технологии



\- \*\*Docker / Docker Compose\*\* — контейнеризация и оркестрация

\- \*\*OpenCart 4\*\* — платформа интернет-магазина

\- \*\*MariaDB 11.2\*\* — реляционная база данных

\- \*\*phpMyAdmin\*\* — веб-интерфейс для MySQL/MariaDB

\- \*\*Python 3.x\*\* — язык программирования для тестов

\- \*\*Selenium WebDriver\*\* — автоматизация браузера

\- \*\*Pytest\*\* — фреймворк для тестирования

\- \*\*pytest-html\*\* — генерация HTML-отчетов



\## Автор



Студент группы \[номер группы]

\[ФИО]

2026 год

