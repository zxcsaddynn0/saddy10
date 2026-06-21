# Итоговая работа: Автоматизация тестирования веб-приложения OpenCart

## Описание проекта

Данный репозиторий содержит итоговую работу по настройке локального окружения с помощью Docker и написанию автотестов для веб-приложения OpenCart с использованием Selenium WebDriver и Pytest.

Проект разворачивает полноценный интернет-магазин OpenCart 4 с базой данных MariaDB и веб-интерфейсом phpMyAdmin для управления БД, а также содержит набор из 10 автотестов, проверяющих основной функционал сайта.

## Структура проекта

    docker/
    ├── docker-compose.yml          # Конфигурация Docker Compose
    ├── .env                        # Переменные окружения (порты, IP)
    ├── .env.example                # Пример переменных окружения
    ├── .gitignore                  # Исключения для Git
    ├── README.md                   # Документация проекта
    └── selenium_tests/             # Папка с автотестами
        ├── test_opencart.py        # 10 автотестов на Selenium + Python
        └── test_report.html        # HTML-отчет о результатах тестирования

## Компоненты системы

| Компонент | Образ | Порт | Назначение |
|-----------|-------|------|------------|
| OpenCart | docker.io/bitnami/opencart:4 | 8081 | Интернет-магазин |
| MariaDB | docker.io/bitnami/mariadb:11.2 | 3306 | Система управления базой данных |
| phpMyAdmin | phpmyadmin/phpmyadmin:latest | 8888 | Веб-интерфейс для управления БД |

## Требования

- Docker Desktop с WSL 2
- Docker Compose v2+
- Python 3.8+
- Google Chrome (для запуска Selenium-тестов)
- Git

## Инструкция по запуску

### 1. Настройка переменных окружения

Создайте файл .env в корне проекта со следующим содержимым:

    OPENCART_PORT=8081
    PHPADMIN_PORT=8888
    LOCAL_IP=127.0.0.1

Совет: можно использовать готовый файл .env.example — просто скопируйте его:

    cp .env.example .env

### 2. Поднятие локального сервера

Выполните команду для запуска всех контейнеров в фоновом режиме:

    docker compose up -d

Проверьте статус контейнеров:

    docker ps

Сайт будет доступен по адресам:

- OpenCart: http://localhost:8081/
- Админ-панель OpenCart: http://localhost:8081/admin/
- phpMyAdmin: http://localhost:8888/

### 3. Первоначальная установка OpenCart

При первом запуске откройте в браузере: http://localhost:8081/install/

Заполните параметры подключения к базе данных:

- Hostname: mariadb
- Username: bn_opencart
- Password: (оставьте пустым)
- Database Name: bitnami_opencart
- Database Port: 3306

Параметры администратора:

- Username: admin
- Password: admin123
- E-Mail: admin@test.com

### 4. Установка зависимостей для тестов

    cd selenium_tests
    pip install selenium pytest pytest-html

### 5. Запуск автотестов

    python -m pytest test_opencart.py -v --html=test_report.html --self-contained-html

### 6. Просмотр отчета о тестировании

    start test_report.html

## Список автотестов

В проекте реализовано 10 автотестов, проверяющих основной функционал сайта:

| № | Имя теста | Описание |
|---|-----------|----------|
| 1 | test_open_main_page | Проверка открытия главной страницы |
| 2 | test_logo_presence | Проверка наличия логотипа |
| 3 | test_navigation_menu | Проверка наличия меню навигации |
| 4 | test_search_functionality | Проверка работы поиска товаров |
| 5 | test_open_category | Открытие категории товаров |
| 6 | test_open_product_card | Открытие карточки товара |
| 7 | test_add_to_cart | Добавление товара в корзину |
| 8 | test_open_cart | Переход на страницу корзины |
| 9 | test_open_login_page | Переход на страницу авторизации |
| 10 | test_footer_presence | Проверка наличия подвала сайта |

Во всех тестах используются явные ожидания (Explicit Waits) через WebDriverWait в сочетании с expected_conditions, что обеспечивает стабильность работы тестов при различной скорости загрузки DOM-дерева.

## Учетные данные

### Админ-панель OpenCart

- URL: http://localhost:8081/admin/
- Username: admin
- Password: admin123

### База данных

- Host: mariadb
- Port: 3306
- Database: bitnami_opencart
- User: bn_opencart
- Password: (пусто)

### phpMyAdmin

- URL: http://localhost:8888/
- Username: bn_opencart
- Password: (пусто)

## Полезные команды Docker

Остановить все контейнеры:

    docker compose down

Остановить и удалить volumes (полный сброс):

    docker compose down -v

Просмотр логов контейнера:

    docker logs docker-opencart-1
    docker logs docker-mariadb-1
    docker logs docker-phpadmin-1

Перезапуск контейнеров:

    docker compose restart

## Возможные проблемы и решения

### Проблема: образ bitnami/opencart не находится

Решение: Bitnami перенесла образы в репозиторий bitnamilegacy. Скачайте образ и создайте локальный тег:

    docker pull bitnamilegacy/opencart:4.0.2-3-debian-12-r33
    docker tag bitnamilegacy/opencart:4.0.2-3-debian-12-r33 docker.io/bitnami/opencart:4

Аналогично для MariaDB:

    docker pull bitnamilegacy/mariadb:11.2.3-debian-12-r4
    docker tag bitnamilegacy/mariadb:11.2.3-debian-12-r4 docker.io/bitnami/mariadb:11.2

### Проблема: порт 3306 или 8081 уже занят

Решение: найдите процесс и остановите его:

    netstat -ano | findstr :3306
    taskkill //PID <номер_процесса> //F

Или измените порт в файле .env.

### Проблема: phpMyAdmin падает с ошибкой exec format error

Решение: перескачайте образ с правильной архитектурой:

    docker rmi phpmyadmin/phpmyadmin:latest
    docker pull --platform linux/amd64 phpmyadmin/phpmyadmin:latest

## Технологии

- Docker / Docker Compose — контейнеризация и оркестрация
- OpenCart 4 — платформа интернет-магазина
- MariaDB 11.2 — реляционная база данных
- phpMyAdmin — веб-интерфейс для MySQL/MariaDB
- Python 3.x — язык программирования для тестов
- Selenium WebDriver — автоматизация браузера
- Pytest — фреймворк для тестирования
- pytest-html — генерация HTML-отчетов

## Автор

Студент группы 3ЭИТ
Малхасян Даниил Арсенович
2026 год
