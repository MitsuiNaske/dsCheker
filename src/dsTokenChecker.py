import threading
import queue
import requests
from fake_headers import Headers
from rich.progress import Progress
from config import *
from src.console import *

token_queue = queue.Queue()
proxy_queue = queue.Queue()

valid = 0
invalid = 0
payments = 0
duplicates = 0


def load_tokens():
  with open("tokens.txt", "r") as file:
    for line in file:
      token_queue.put(line.strip())


def load_proxy():
  with open("proxy.txt", "r") as file:
    for line in file:
      proxy_queue.put(line.strip())


def is_proxy_valid(proxy):
  try:
    response = requests.get("http://httpbin.org/ip", proxies=proxy, timeout=5)
    response.raise_for_status()
    return True
  except requests.RequestException:
    return False


def get_proxy():
  while True:
    if not proxy_queue.empty():
      proxy_str = proxy_queue.get().strip()

      if proxy_format == 1:
        ip, port = proxy_str.split(':')
        proxy = {"http": f"{proxy_type}://{ip}:{port}"}
      else:
        ip, port, username, password = proxy_str.split(':')
        proxy = {"http": f"{proxy_type}://{username}:{password}@{ip}:{port}"}

      if is_proxy_valid(proxy):
        return proxy
    else:
      load_proxy()


def check_token(token, proxy):
  global valid, invalid, payments
  header = generate_fake_headers(token)
  req_token = requests.get("https://discord.com/api/v9/users/@me",
                           headers=header,
                           proxies=proxy)

  if req_token.status_code == 200:
    if check_payments(header, proxy):
      payments += 1
      return "payments"
    else:
      valid += 1
      return "valid"
  else:
    invalid += 1
    return "invalid"


def check_payments(header, proxy):
  req_payments = requests.get(
      "https://discord.com/api/v9/users/@me/billing/payment-sources",
      headers=header,
      proxies=proxy)
  return len(req_payments.json()) > 0


def generate_fake_headers(token):
  headers = Headers(browser="chrome", os="win", headers=True)
  fake_headers = headers.generate()
  fake_headers["Authorization"] = token
  return fake_headers


def save_token(token, file_path):
  with open(file_path, "a") as f:
    f.write(f"{token}\n")


def work(progress_task, progress):
  while not token_queue.empty():
    token = token_queue.get()
    if token is None:
      break
    proxy = get_proxy()
    result = check_token(token, proxy)
    if result == "payments":
      save_token(token, "./result/payments.txt")
    elif result == "valid":
      save_token(token, "./result/valid.txt")
    else:
      save_token(token, "./result/invalid.txt")
    progress.update(progress_task, advance=1)


def discord_token_checker():
  load_proxy()
  load_tokens()

  threads = []

  with Progress() as progress:
    progress_task = progress.add_task("[green]Проверка токенов...",
                                      total=token_queue.qsize())

    for _ in range(num_threads):
      thread = threading.Thread(target=work, args=(
          progress_task,
          progress,
      ))
      thread.start()
      threads.append(thread)

    for thread in threads:
      thread.join()

  console.print(f"Valid tokens: {valid}")
  console.print(f"Invalid tokens: {invalid}")
  console.print(f"Tokens with payments: {payments}")
