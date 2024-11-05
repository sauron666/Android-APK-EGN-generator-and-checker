import random
from datetime import datetime
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.dropdown import DropDown
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

# Set background color for the app
Window.clearcolor = (0.95, 0.95, 0.95, 1)

# EGN Regions and Weights
EGN_REGIONS = {
    "Благоевград": (0, 43), "Бургас": (44, 93), "Варна": (94, 139), "Велико Търново": (140, 169),
    "Видин": (170, 183), "Враца": (184, 217), "Габрово": (218, 233), "Кърджали": (234, 281),
    "Кюстендил": (282, 301), "Ловеч": (302, 319), "Монтана": (320, 341), "Пазарджик": (342, 377),
    "Перник": (378, 395), "Плевен": (396, 435), "Пловдив": (436, 501), "Разград": (502, 527),
    "Русе": (528, 555), "Силистра": (556, 575), "Сливен": (576, 601), "Смолян": (602, 623),
    "София - град": (624, 721), "София - окръг": (722, 751), "Стара Загора": (752, 789),
    "Добрич (Толбухин)": (790, 821), "Търговище": (822, 843), "Хасково": (844, 871),
    "Шумен": (872, 903), "Ямбол": (904, 925), "Друг/Неизвестен": (926, 999)
}

weights = [2, 4, 8, 5, 10, 9, 7, 3, 6]

# Основни функции за изчисление и валидация на EGN

def determine_region(code):
    for region, (start, end) in EGN_REGIONS.items():
        if start <= code <= end:
            return region
    return "Неизвестен регион"

def calculate_checksum(egn):
    checksum = sum(int(egn[i]) * weights[i] for i in range(9)) % 11
    return str(checksum if checksum < 10 else 0)

def generate_sequential_egn(day=None, month=None, year=None, gender=None, region_name=None):
    day = day if day else random.randint(1, 28)
    month = month if month else random.randint(1, 12)
    year = year if year else random.randint(1900, 2099)
    gender_digit = 0 if gender == "Мъж" else 1 if gender == "Жена" else random.choice([0, 1])

    if region_name in EGN_REGIONS:
        start, end = EGN_REGIONS[region_name]
    else:
        start, end = (0, 999)

    region_code = start + random.randint(0, (end - start) // 2) * 2 + gender_digit
    egn_base = f"{year % 100:02}{month:02}{day:02}{region_code:03}"
    egn = egn_base + calculate_checksum(egn_base)
    return egn

def get_egn_info(egn):
    year = int(egn[:2])
    month = int(egn[2:4])
    day = int(egn[4:6])
    region_code = int(egn[6:9])
    gender_digit = int(egn[8])
    gender = "Мъж" if gender_digit % 2 == 0 else "Жена"

    if month > 40:
        year += 2000
        month -= 40
    elif month > 20:
        year += 1800
        month -= 20
    else:
        year += 1900

    region = determine_region(region_code)
    birth_date = f"{day:02}-{month:02}-{year}"

    return (f"ЕГН: {egn}\nПол: {gender}\nДата на раждане: {birth_date}\nРегион: {region}")

# Прогнози на базата на зодиак, таро и числото на жизнения път

def zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Овен (Елемент: Огън)"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Телец (Елемент: Земя)"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Близнаци (Елемент: Въздух)"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Рак (Елемент: Вода)"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Лъв (Елемент: Огън)"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Дева (Елемент: Земя)"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Везни (Елемент: Въздух)"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Скорпион (Елемент: Вода)"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Стрелец (Елемент: Огън)"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Козирог (Елемент: Земя)"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Водолей (Елемент: Въздух)"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Риби (Елемент: Вода)"
    return "Неизвестен знак"

def tarot_card(life_path_number):
    tarot_options = {
        1: [
            ("Магьосникът", "Използвайте своите таланти и умения, за да постигнете целите си."),
            ("Императорът", "Стремете се към стабилност и ред в живота си. Бъдете лидер."),
            ("Колелото на съдбата", "Животът ви ще се промени. Приемете промените.")
        ],
        2: [
            ("Върховната жрица", "Интуицията ви ще бъде вашият водач. Обръщайте внимание на вътрешния си глас."),
            ("Жрецът", "Следвайте традициите и се обръщайте към мъдростта на миналото."),
            ("Влюбените", "Слушайте сърцето си. Важните решения ще изискват баланс и любов.")
        ],
        3: [
            ("Императрицата", "Това е период на растеж и изобилие. Подхранвайте своите идеи."),
            ("Справедливостта", "Бъдете справедливи и търсете истината. Действията ви ще имат последствия."),
            ("Слънцето", "Щастие и успех ви очакват. Време за радост и просперитет.")
        ],
        # Добавете допълнителни карти за други числа на жизнения път, ако е необходимо
    }
    return random.choice(tarot_options.get(life_path_number, [("Неизвестна карта", "Тълкуване липсва")]))

def past_tip(life_path_number):
    tips = {
        1: [
            "Миналото ви е било посветено на постижения и независимост.",
            "Преодолели сте големи предизвикателства, като сте използвали своите умения и амбиция.",
            "Вашата увереност и стремеж към успех са ви направили лидер в различни области."
        ],
        2: [
            "Вашето минало е било белязано от изграждане на значими и дълготрайни взаимоотношения.",
            "Отдавали сте се на грижи за другите и сте създавали трайни връзки.",
            "Вие сте били мостът между хората, създавайки хармония и разбирателство."
        ],
        3: [
            "Миналото ви е белязано от творчество и интуиция.",
            "Винаги сте търсили нови идеи и възможности за изразяване.",
            "Вашето въображение и интуиция са ви водили към уникални проекти и начинания."
        ],
        # Добавете допълнителни съвети за други числа на жизнения път, ако е необходимо
    }
    return random.choice(tips.get(life_path_number, ["Миналото ви е мистериозно и уникално."]))

def future_tip(life_path_number):
    tips = {
        1: [
            "Очаква ви ново начало и възможност за лидерство.",
            "Ще бъдете изправени пред предизвикателства, които ще изискват вашата решителност и амбиция.",
            "Вашата увереност ще ви помогне да постигнете нови върхове."
        ],
        2: [
            "Силните взаимоотношения и успешните партньорства ще играят важна роля в бъдещето ви.",
            "Ще се фокусирате върху създаване на хармония и баланс в личния и професионалния си живот.",
            "Вашата способност да сътрудничите ще отвори нови възможности за растеж."
        ],
        3: [
            "Очакват ви творчески проекти и нови идеи.",
            "Бъдещето ви ще бъде изпълнено с възможности за изразяване на вашето въображение.",
            "Творческият ви подход ще ви донесе признание и успех."
        ],
        # Добавете допълнителни съвети за други числа на жизнения път, ако е необходимо
    }
    return random.choice(tips.get(life_path_number, ["Бъдещето ви е изпълнено с мистерии."]))

def human_design_details(life_path_number):
    types = {
        1: ["Манифестор", "Проектор"],
        2: ["Генератор", "Манифестиращ Генератор"],
        3: ["Рефлектор", "Генератор"]
        # Добавете допълнителни типове за други числа на жизнения път, ако е необходимо
    }
    strategies = {
        1: ["Информирай преди действие", "Изчакай покана"],
        2: ["Изчакай отговор", "Следвай интуицията"],
        3: ["Изчакай покана", "Изчакай отговор"]
        # Добавете допълнителни стратегии за други числа на жизнения път, ако е необходимо
    }
    authorities = {
        1: ["Емоционален", "Самопрожектиран"],
        2: ["Сакрален", "Лунен"],
        3: ["Емоционален", "Сакрален"]
        # Добавете допълнителни авторитети за други числа на жизнения път, ако е необходимо
    }

    design_type = random.choice(types.get(life_path_number, ["Неизвестен тип"]))
    strategy = random.choice(strategies.get(life_path_number, ["Неизвестна стратегия"]))
    authority = random.choice(authorities.get(life_path_number, ["Неизвестен авторитет"]))
    
    return f"Тип: {design_type}\nСтратегия: {strategy}\nАвторитет: {authority}"

def generate_prediction(egn):
    info = get_egn_info(egn)
    life_path_number = (sum(map(int, egn)) % 9) + 1
    zodiac = zodiac_sign(int(egn[4:6]), int(egn[2:4]))
    tarot_name, tarot_meaning = tarot_card(life_path_number)
    design_info = human_design_details(life_path_number)
    past = past_tip(life_path_number)
    future = future_tip(life_path_number)

    return (f"{info}\n\nЗодиакален знак: {zodiac}\n"
            f"Таро карта: {tarot_name} - {tarot_meaning}\n\n"
            f"Human Design:\n{design_info}\n\n"
            f"Минало: {past}\nБъдеще: {future}")

# Popup за подробности с прогноза
def show_details_popup(egn):
    content = ScrollView(size_hint=(1, None), height=dp(700))
    label = Label(text=generate_prediction(egn), size_hint_y=None, text_size=(Window.width * 0.85, None), halign='left', valign='top', font_size='22sp', padding=(dp(10), dp(10)))
    label.bind(size=label.setter('text_size'))  # Make sure text size matches label size
    label.bind(texture_size=label.setter('size'))  # Adjust the size of label based on the texture size
    content.add_widget(label)
    popup = Popup(title="Детайли и Прогноза", content=content, size_hint=(0.9, 0.9), auto_dismiss=True)
    popup.open()

def show_info_popup():
    content = Label(text="Това приложение е създадено от Marto - ГарванЪ. Целта му е да генерира и проверява валидността на ЕГН, както и да предоставя гадателски прогнози на базата на ЕГН.",
                    size_hint=(1, None), height=dp(400), text_size=(Window.width * 0.85, None), halign='center', valign='top', font_size='20sp', padding=(dp(10), dp(10)))
    popup = Popup(title="Информация за приложението", content=content, size_hint=(0.85, 0.5), auto_dismiss=True)
    popup.open()

class EGNApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))

        self.label = Label(text="Генератор и проверка на ЕГН", font_size='24sp', bold=True, size_hint=(1, None), height=dp(60), color=(0, 0, 0, 1))
        layout.add_widget(self.label)

        self.region_spinner = Spinner(text="Избери регион", values=list(EGN_REGIONS.keys()), size_hint=(1, None), height=dp(50), background_color=(0.3, 0.5, 0.7, 1), font_size='18sp')
        layout.add_widget(self.region_spinner)

        self.gender_spinner = Spinner(text="Избери пол", values=["Мъж", "Жена"], size_hint=(1, None), height=dp(50), background_color=(0.3, 0.5, 0.7, 1), font_size='18sp')
        layout.add_widget(self.gender_spinner)

        input_layout = BoxLayout(size_hint=(1, None), height=dp(50), spacing=dp(10))
        self.day_input = TextInput(hint_text="Ден", multiline=False, size_hint=(1, None), height=dp(50), font_size='18sp')
        self.month_input = TextInput(hint_text="Месец", multiline=False, size_hint=(1, None), height=dp(50), font_size='18sp')
        self.year_input = TextInput(hint_text="Година", multiline=False, size_hint=(1, None), height=dp(50), font_size='18sp')
        input_layout.add_widget(self.day_input)
        input_layout.add_widget(self.month_input)
        input_layout.add_widget(self.year_input)
        layout.add_widget(input_layout)

        self.num_egn_label = Label(text="Брой ЕГН (1-1000):", size_hint=(1, None), height=dp(40), font_size='18sp', color=(0, 0, 0, 1))
        layout.add_widget(self.num_egn_label)
        
        self.num_egn_slider = Slider(min=1, max=1000, value=5, step=1, size_hint=(1, None), height=dp(40))
        self.num_egn_slider.bind(value=self.update_slider_label)
        layout.add_widget(self.num_egn_slider)

        self.generate_button = Button(text="Генерирай ЕГН", size_hint=(1, None), height=dp(60), background_color=(0.3, 0.5, 0.7, 1), color=(1, 1, 1, 1), font_size='20sp', on_press=self.generate_egn_list)
        layout.add_widget(self.generate_button)

        self.check_egn_input = TextInput(hint_text="Въведете ЕГН за проверка", multiline=False, size_hint=(1, None), height=dp(50), font_size='18sp')
        layout.add_widget(self.check_egn_input)

        self.check_button = Button(text="Провери ЕГН", size_hint=(1, None), height=dp(60), background_color=(0.3, 0.5, 0.7, 1), color=(1, 1, 1, 1), font_size='20sp', on_press=self.check_egn)
        layout.add_widget(self.check_button)

        self.egn_display = GridLayout(cols=1, size_hint_y=None, padding=dp(10), spacing=dp(10))
        self.egn_display.bind(minimum_height=self.egn_display.setter('height'))
        self.scroll_view = ScrollView(size_hint=(1, 1), bar_width=dp(10))
        self.scroll_view.add_widget(self.egn_display)
        layout.add_widget(self.scroll_view)

        # Label for tracking the number of EGN generated
        self.egn_counter_label = Label(text="Генерирани ЕГН: 0", size_hint=(1, None), height=dp(40), font_size='18sp', color=(0, 0, 0, 1))
        layout.add_widget(self.egn_counter_label)

        # Button for app creator information
        self.info_button = Button(text="Информация", size_hint=(1, None), height=dp(40), font_size='16sp', on_press=lambda x: show_info_popup())
        layout.add_widget(self.info_button)

        return layout

    def generate_egn_list(self, instance):
        day = int(self.day_input.text) if self.day_input.text.isdigit() else None
        month = int(self.month_input.text) if self.month_input.text.isdigit() else None
        year = int(self.year_input.text) if self.year_input.text.isdigit() else None
        gender = self.gender_spinner.text if self.gender_spinner.text in ["Мъж", "Жена"] else None
        region = self.region_spinner.text if self.region_spinner.text in EGN_REGIONS else None

        self.egn_display.clear_widgets()
        num_egn = int(self.num_egn_slider.value)
        unique_egns = set()

        for i in range(num_egn):
            egn = generate_sequential_egn(day, month, year, gender, region)
            if egn not in unique_egns:
                unique_egns.add(egn)
                btn = Button(text=egn, size_hint_y=None, height=dp(50), font_size='18sp', background_color=(0.8, 0.8, 0.8, 1))
                btn.bind(on_release=lambda btn_instance: show_details_popup(btn_instance.text))
                self.egn_display.add_widget(btn)
                # Update counter label
                self.egn_counter_label.text = f"Генерирани ЕГН: {i + 1}"
                if len(unique_egns) >= num_egn:
                    break

    def check_egn(self, instance):
        egn = self.check_egn_input.text.strip()
        if len(egn) == 10 and egn.isdigit():
            show_details_popup(egn)
        else:
            popup = Popup(title="Невалидно ЕГН", content=Label(text="Моля, въведете валидно 10-цифрено ЕГН.", font_size='18sp', color=(1, 0, 0, 1)), size_hint=(0.8, 0.4))
            popup.open()

    def update_slider_label(self, instance, value):
        self.num_egn_label.text = f"Брой ЕГН (1-1000): {int(value)}"

if __name__ == '__main__':
    EGNApp().run()
