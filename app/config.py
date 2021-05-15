# -*- coding: utf-8 -*-

from subprocess import run, PIPE
from os import getenv
from sys import exit
from app.utils import parse_as_boolean
import logging


try:
    # Настройки приложения
    VERSION = getenv("VERSION", "Unknown")
    COMMIT = str(run(["git log --pretty=format:'%h' -n 1"], shell=True, stdout=PIPE).stdout.decode("UTF-8"))
    DEVELOPER_MODE = parse_as_boolean(getenv("DEVELOPER_MODE", False))
    FNBR_API_KEY = getenv("FNBR_API_KEY")
    CHANNEL_ID = int(getenv("CHANNEL_ID")) if getenv("CHANNEL_ID") else None

    # Настройки Telegram клиента
    API_ID = int(getenv("3611561")) if getenv("3611561") else None
    API_HASH = getenv("50aea2c1e9e3a806c6a0ce237d337bd6")
    BOT_TOKEN = getenv("1857269812:AAE1ywlLSZuHwlC-GKj-67dIePhRqy6KmYQ")

    # Настройки сообщества VK
    VK_TOKEN = getenv("3658d485d74644870d3ec4070aa848934911d111e2b0f2d7ea6fef8ffedeede13b98b06cf1d63cc48f8f4")
    VK_COMMUNITY_ID = int(getenv("public191905232")) if getenv("public191905232") else None

    # Настройки Redis
    REDIS_HOST = getenv("REDIS_HOST", "127.0.0.1")
    REDIS_PORT = getenv("REDIS_PORT", 6379)
except:
    logging.critical("Произошла ошибка при формировании настроек в конфигурационном файле.", exc_info=True)
    exit(1)
