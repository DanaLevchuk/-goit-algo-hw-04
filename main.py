def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_id, name, age = parts
                    cats.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
    except Exception as e:
        print(f"Виникла помилка при читанні файлу: {e}")
    
    return cats


cats_info = get_cats_info("cats.txt")
print(cats_info)




