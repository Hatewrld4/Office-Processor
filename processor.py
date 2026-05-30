import pandas as pd
import os

def consolidate_reports(input_folder="reports", output_file="Final_Report.xlsx"):
    all_data = []
    
    # Перевіряємо чи є папка з файлами
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
        print(f"[-] Папка '{input_folder}' створена. Покладіть туди Excel файли.")
        return

    # Зчитуємо всі Excel файли в папці
    for file in os.listdir(input_folder):
        if file.endswith(".xlsx"):
            print(f"[+] Обробка файлу: {file}")
            df = pd.read_excel(os.path.join(input_folder, file))
            all_data.append(df)

    # Об'єднуємо все в один звіт
    if all_data:
        final_report = pd.concat(all_data, ignore_index=True)
        final_report.to_excel(output_file, index=False)
        print(f"[SUCCESS] Звіт готовий! Збережено як {output_file}")
    else:
        print("[-] Файлів для обробки не знайдено.")

if __name__ == "__main__":
    consolidate_reports()