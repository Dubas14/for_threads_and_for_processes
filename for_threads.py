import os
import shutil
import threading

def copy_file(file_path, dest_dir):
    """
    Копіює файл до цільової директорії, створюючи піддиректорію за розширенням файлу.
    """
    file_ext = os.path.splitext(file_path)[1][1:].lower()
    if not file_ext:  # Пропустити файли без розширення
        return
    
    target_dir = os.path.join(dest_dir, file_ext)
    os.makedirs(target_dir, exist_ok=True)
    
    shutil.copy2(file_path, target_dir)

def process_directory(source_dir, dest_dir):
    """
    Рекурсивно обходить директорію і копіює файли за розширеннями в цільову директорію.
    """
    threads = []
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            thread = threading.Thread(target=copy_file, args=(file_path, dest_dir))
            threads.append(thread)
            thread.start()

    # Очікуємо завершення всіх потоків
    for thread in threads:
        thread.join()

def main():
    source_dir = "picture"  # Вихідна директорія
    dest_dir = "dist"  # Цільова директорія
    
    process_directory(source_dir, dest_dir)
    
if __name__ == "__main__":
    main()