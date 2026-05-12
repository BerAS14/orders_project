# Orders System
Система управления заказами.

---

## Возможности
- Создание и просмотр заказов
- Два типа заказов: **Единичный** и **Множественный**
- Фильтрация по статусу
- Автоматическая генерация номеров заказов (`ORD-0001`)
- Авторизация пользователей
- Адаптивный современный интерфейс

## Быстрый старт

### 1. Клонирование проекта
```bash
git clone https://github.com/BerAS14/orders_project.git
cd orders_project
```
### 2. Создать файл `.env` на основе `.env.example`
### 3. Установка зависимостей (через uv)
Скачать uv https://github.com/astral-sh/uv/releases и добавить в `%PATH%`
```bash
uv sync --frozen
```
### 4. Применение миграций
```bash
uv run python manage.py migrate
```
### 5. Создание суперпользователя
```bash
uv run python manage.py createsuperuser
```
### 6. Запуск сервера
```bash
uv run python manage.py runserver
```
Перейдите по адресу: http://127.0.0.1:8000

## Технологии
Python 3.14.2
Django 6.0.4
uv — менеджер пакетов и виртуальных окружений
HTML + CSS (собственный дизайн без Bootstrap)
SQLite (по умолчанию)

## Структура проекта
orders-project/
├── config/              # Основные настройки проекта
├── orders/              # Приложение заказов
├── accounts/            # Приложение пользователей
├── templates/
├── static/
├── .github/workflows/   # GitHub Actions
├── manage.py
├── pyproject.toml
└── uv.lock

## Запуск тестов
### Все тесты
```bash
uv run python manage.py test
```
### Только приложение orders
```bash
uv run python manage.py test orders -v 2
```
