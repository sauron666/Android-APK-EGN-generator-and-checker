# EGN generator and Checker App

## Описание на проекта
EGN Checker е приложение, което позволява валидирането, генерирането и анализа на единни граждански номера (ЕГН). Целта му е да предостави информация за валидността на ЕГН, както и да помогне с генериране на ЕГН въз основа на различни критерии (дата на раждане, регион и други).

Алгоритъмът, използван в това приложение, е базиран на публично достъпната информация за структурата на ЕГН. За валидирането и генерирането на ЕГН сме следвали принципите, изложени и на официалния сайт на ЕСГРАОН.

Приложението предлага допълнителни функции, включително генериране на астрологична прогноза, съобразена със зодиакален знак, таро и Human Design детайли, въз основа на въведеното ЕГН.

## Основни функции
- **Генериране на ЕГН**: Генериране на валидни ЕГН на база зададени критерии, като дата на раждане, регион и пол.
- **Валидиране на ЕГН**: Проверка за валидност на въведените ЕГН.
- **Анализ на ЕГН**: Извличане на информация, като дата на раждане, регион и пол на лицето, въз основа на ЕГН.
- **Прогнози на база зодиак и таро**: Генериране на предсказания въз основа на зодиакалния знак и други астрологични елементи, получени от ЕГН.

## Технологии
- **Python**: Основният програмен език, използван за разработката на приложението.
- **Kivy**: Библиотека за разработка на графични потребителски интерфейси (GUI), с която е създаден интерфейсът на приложението.

## Как да стартирате приложението
1. Клонирайте репото:
   ```sh
   git clone https://github.com/sauron666/Android-APK-EGN-generator-and-checker.gi
   ```

2. Стартирайте приложението:
   ```sh
   python main.py
   ```

## Сходни проекти
Сходен проект може да бъде намерен на https://georgi.unixsol.org/programs/egn.php), където е използван същият алгоритъм за валидиране и генериране на ЕГН. Този проект използва данни за статистическото разпределение на ражданията по региони и предоставя информация за валидността и произхода на ЕГН.

