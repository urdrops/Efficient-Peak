from pynput import keyboard, mouse
import threading
import time
import psutil

# Переменные для хранения статистики
total_keypresses = 0

total_scroll_pixels = 0
average_scroll_speed = 0

left_clicks = 0
right_clicks = 0

# Переменные для отслеживания скорости скроллинга
scroll_start_time = 0
scroll_end_time = 0
scroll_distance = 0

# Переменные для отслеживания сетевого трафика
network_start_time = time.time()
received_bytes = 0
sent_bytes = 0


# Функция обработки нажатия клавиши
def on_key_press(key):
    global total_keypresses, ctrl_keypresses, alt_keypresses, shift_keypresses

    total_keypresses += 1


# Функция обработки скроллинга мыши
def on_scroll(x, y, dx, dy):
    global total_scroll_pixels, average_scroll_speed, scroll_start_time, scroll_end_time, scroll_distance

    total_scroll_pixels += abs(dy)
    current_time = time.time()

    if scroll_start_time == 0:
        scroll_start_time = current_time
    else:
        scroll_end_time = current_time
        scroll_distance += abs(dy)


# Функция обработки кликов мыши
def on_click(x, y, button, pressed):
    global left_clicks, right_clicks

    if pressed:
        if button == mouse.Button.left:
            left_clicks += 1
        elif button == mouse.Button.right:
            right_clicks += 1


# Функция для отслеживания сетевого трафика
# Функция для отслеживания сетевого трафика
def track_network_traffic():
    global network_start_time, received_bytes, sent_bytes

    while True:
        start_time = time.time()

        # Получение данных о сетевом трафике
        start_received_bytes = psutil.net_io_counters().bytes_recv
        start_sent_bytes = psutil.net_io_counters().bytes_sent

        time.sleep(120)  # Периодичность проверки сетевого трафика

        end_time = time.time()

        # Получение данных о сетевом трафике после интервала
        end_received_bytes = psutil.net_io_counters().bytes_recv
        end_sent_bytes = psutil.net_io_counters().bytes_sent

        # Разница между начальным и конечным трафиком
        interval_received_bytes = end_received_bytes - start_received_bytes
        interval_sent_bytes = end_sent_bytes - start_sent_bytes

        # Переводим байты в мегабайты
        interval_received_mb = round(interval_received_bytes / (1024 * 1024), 5)
        interval_sent_mb = round(interval_sent_bytes / (1024 * 1024), 5)

        print(f"0, 0, 0, {interval_sent_mb}, ", end="")
        print(f"{interval_received_mb}", end="")
        received_bytes = end_received_bytes
        sent_bytes = end_sent_bytes
        network_start_time = end_time


# ... (остальной код остается без изменений)


# Функция для вывода статистики и сброса данных
def print_statistics():
    global total_keypresses
    global total_scroll_pixels, average_scroll_speed, scroll_start_time, scroll_end_time, scroll_distance
    global left_clicks, right_clicks

    average_keypresses = total_keypresses / 2.0  # среднее количество кликов в секунду

    if scroll_start_time != 0 and scroll_end_time != 0:
        time_difference = scroll_end_time - scroll_start_time
        average_scroll_speed = scroll_distance / time_difference
    print("\n\n")
    print(f"{total_keypresses}, ", end="")
    print(f"{average_keypresses}, 0, ", end="")

    print(f"{total_scroll_pixels}, ", end="")
    print(f"{round(average_scroll_speed, 5)}, ", end="")
    print(f"{left_clicks}, ", end="")
    print(f"{right_clicks}, ", end="")

    # Сброс данных
    total_keypresses = 0

    total_scroll_pixels = 0
    average_scroll_speed = 0
    scroll_start_time = 0
    scroll_end_time = 0
    scroll_distance = 0

    left_clicks = 0
    right_clicks = 0


# Функция для выполнения каждые 2 минуты
def timer():
    print_statistics()
    threading.Timer(120, timer).start()


# Запуск таймера
timer()

# Запуск функции отслеживания сетевого трафика в отдельном потоке
network_thread = threading.Thread(target=track_network_traffic)
network_thread.start()

# Настройка слушателя клавиатуры
with keyboard.Listener(on_press=on_key_press) as key_listener:
    # Настройка слушателя мыши
    with mouse.Listener(on_scroll=on_scroll, on_click=on_click) as mouse_listener:
        key_listener.join()
        mouse_listener.join()
