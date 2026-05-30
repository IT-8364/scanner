[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Author: OlegQWERTY8364](https://img.shields.io/badge/Author-OlegQWERTY8364-orange)](https://github.com/IT-8364)

## 1. Запуск

```bash
python scanner.py <host> <ports>
```

### Описание:

* **`<host>`** — IP-адрес (например, `8.47.69.6`) или домен (например, `example.com`).
* **`<ports>`** — порты, которые необходимо проверить. Поддерживаются следующие форматы записи:

  * Одиночный порт (`80`).
  * Список портов (`22,80,443`).
  * Диапазон портов (`1-1024`).
  * Комбинированный вариант (`80,135-139,443`).



## 2. Работа

При обнаружении открытого TCP-порта утилита выводит сообщение в консоль в следующем формате:

```text
[port]/tcp open
```

*Пример вывода:*

```text
22/tcp open
80/tcp open
443/tcp open
```

