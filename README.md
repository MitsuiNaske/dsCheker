
# Configuration Guide for `config.json` / Руководство по настройке `config.json`

This project uses a `config.json` file to define essential parameters. Below is the structure and explanation for each field.  
Этот проект использует файл `config.json` для задания основных параметров. Ниже описана структура и назначение каждого поля.

---

## Configuration Fields / Поля конфигурации

### `proxy_format`
Specifies the format of the proxy. The value must strictly follow one of the two formats:  
Задает формат прокси. Значение должно строго соответствовать одному из форматов:
- **1**: `ip:port`  
- **2**: `ip:port:login:password`

### `proxy_type`
Defines the type of proxies used in the application. Choose one of the following values:  
Определяет тип используемых прокси. Выберите одно из следующих значений:
- `socks5` (in brackets / в скобках)  
- `http` (in brackets / в скобках)  

### `num_threads`
Sets the number of threads the application should use. Specify an integer value.  
Устанавливает количество потоков, используемых приложением. Задайте целое число.

---

## Example `config.json` / Пример `config.json`

Below is an example configuration file:  
Пример конфигурационного файла:  

```json
{
  "proxy_format": 1,
  "proxy_type": "(socks5)",
  "num_threads": 10
}

