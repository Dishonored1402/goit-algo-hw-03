import os
import shutil
import sys

def copy_files(src_dir, dst_dir):
    if not os.path.exists(src_dir):
        print(f"Помилка: директорія {src_dir} не існує.")
        return

    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)

        if os.path.isdir(item_path):
            copy_files(item_path, dst_dir)

        elif os.path.isfile(item_path):
            try:
                file_extension = item.split('.')[-1] if '.' in item else 'no_extension'

                extension_dir = os.path.join(dst_dir, file_extension)
                if not os.path.exists(extension_dir):
                    os.makedirs(extension_dir)

                dst_file_path = os.path.join(extension_dir, item)
                shutil.copy(item_path, dst_file_path)
                print(f"Файл {item} скопійовано в {dst_file_path}")

            except Exception as e:
                print(f"Помилка при копіюванні файлу {item_path}: {e}")

def main():
    if len(sys.argv) < 2:
        print("Помилка: не вказано вихідну директорію.")
        sys.exit(1)

    src_dir = sys.argv[1]
    dst_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist'

    print(f"Вихідна директорія: {src_dir}")
    print(f"Директорія призначення: {dst_dir}")

    copy_files(src_dir, dst_dir)

if __name__ == "__main__":
    main()
