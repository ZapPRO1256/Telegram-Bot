# News Parser + Telegram Bot

Цей проект поєднує в собі парсер новин та Telegram-бота для представлення новин користувачам. Парсер збирає останні новини з вибраних джерел, а бот надсилає їх підписникам у Telegram.

## Зміст

- [Вступ](#вступ)
- [Вимоги](#вимоги)
- [Установка](#установка)
- [Конфігурація](#конфігурація)
- [Використання](#використання)

## Вступ

Проект призначений для автоматичного збирання новин з вебсайтів та надсилання їх користувачам через Telegram-бота. Це зручний спосіб отримувати актуальні новини безпосередньо у месенджер.

## Вимоги

- Python 3.8+
- Telegram Bot API Token
- Встановлені пакети:
  - `requests`
  - `beautifulsoup4 4.12.3`
  - `certifi 2024.7.4`
  - `charset-normalizer 3.3.2`
  - `idna 3.7`
  - `lxml 5.2.2`
  - `pyTelegramBotAPI 4.21.0`
  - `requests 2.32.3`
  - `soupsieve 2.5`
  - `urllib3 2.2.2`

## Установка

1. Клонування репозиторію

    ```bash
    git clone https://github.com/ZapPRO1256/Telegram-Bot.git
    ```

2. Перехід до каталогу проекту

    ```bash
    cd Telegram-Bot
    ```

3. Створення віртуального середовища та активація

    ```bash
    python -m venv .venv
    source venv/bin/activate  # для Windows: .venv\Scripts\activate
    ```

4. Установка залежностей

    ```bash
    pip install -r requirements.txt
    ```

## Конфігурація

1. Замініть TOKEN в кореневому файлі main на ваш Telegram Bot API Token

## Використання

Запустіть парсер і бота:

```bash
python main.py

