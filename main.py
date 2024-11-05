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

# Core Functions for EGN Generation and Validation

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

# Zodiac Sign Calculation
def zodiac_sign(day, month):
    """Determine the zodiac sign based on birth day and month."""
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Близнаци"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Лъв"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Везни"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Скорпион"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Стрелец"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Козирог"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Водолей"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Риби"
    return "Неизвестен знак"

# Tarot Card Mapping
def tarot_card(life_path_number):
    """Return tarot card and meaning based on life path number."""
    tarot_map = {
        1: ("Магьосникът", "Използвайте своите таланти и умения, за да постигнете целите си."),
        2: ("Върховната жрица", "Интуицията ви ще бъде вашият водач. Обръщайте внимание на вътрешния си глас."),
        3: ("Императрицата", "Това е период на растеж и изобилие. Подхранвайте своите идеи."),
        4: ("Императорът", "Стремете се към стабилност и ред в живота си. Бъдете лидер."),
        5: ("Жрецът", "Следвайте традициите и се обръщайте към мъдростта на миналото."),
        6: ("Влюбените", "Слушайте сърцето си. Важните решения ще изискват баланс и любов."),
        7: ("Колесницата", "Упоритостта ще ви помогне да преодолеете предизвикателствата."),
        8: ("Силата", "Съчетайте нежност и твърдост, за да преодолеете трудности."),
        9: ("Отшелникът", "Отдръпнете се и обмислете пътя си. Време за вътрешно изследване."),
        10: ("Колелото на съдбата", "Животът ви ще се промени. Приемете промените."),
        11: ("Справедливостта", "Бъдете справедливи и търсете истината. Действията ви ще имат последствия."),
        12: ("Обесеният", "Търпението ще ви доведе до прозрение. Погледнете от нов ъгъл."),
        13: ("Смърт", "Не се страхувайте от края на един етап, ново начало предстои."),
        14: ("Умереност", "Търсете баланс във всички неща. Избягвайте крайностите."),
        15: ("Дяволът", "Внимавайте с изкушенията и зависимостите. Освободете се."),
        16: ("Кулата", "Неочаквани промени ще разклатят основите ви. Приемете новото."),
        17: ("Звездата", "Надеждата ще освети пътя ви. Вярвайте в своите мечти."),
        18: ("Луната", "Интуицията ви ще бъде силна. Внимавайте за илюзии."),
        19: ("Слънцето", "Щастие и успех ви очакват. Време за радост и просперитет."),
        20: ("Страшният съд", "Преразгледайте миналото си и се подгответе за обновление."),
        21: ("Светът", "Завършек на цикъл. Готови сте да започнете нов етап.")
    }
    return tarot_map.get(life_path_number, ("Неизвестна карта", "Тълкуване липсва"))

# Human Design and Numerology Details Based on Life Path Number
def human_design_details(life_path_number):
    types = ["Манифестор", "Генератор", "Проектор", "Манифестиращ Генератор", "Рефлектор"]
    strategies = ["Информирай", "Изчакай отговор", "Изчакай покана", "Изчакай възможностите"]
    authorities = ["Емоционален", "Сакрален", "Саморазбиране", "Отразяване на околните"]

    # Assign types and attributes based on life path number
    design_type = types[life_path_number % len(types)]
    strategy = strategies[life_path_number % len(strategies)]
    authority = authorities[life_path_number % len(authorities)]
    
    return f"Human Design Тип: {design_type}\nСтратегия: {strategy}\nАвторитет: {authority}"

def past_tip(life_path_number):
    """Return a past life insight based on the life path number."""
    tips = {
        1: "Вие сте били решителен и независим. Миналите предизвикателства ви помогнаха да развиете лидерски качества.",
        2: "Миналото ви е било посветено на сътрудничество и разбирателство. Винаги сте търсили хармония.",
        3: "Креативността и изразяването са били основни аспекти на миналото ви. Често сте вдъхновявали другите.",
        4: "Стабилността и редът са били важни за вас. Работили сте усилено за материална сигурност.",
        5: "Били сте търсач на приключения и промени. Приспособимостта е вашият ключов талант.",
        6: "Грижовността и любовта към семейството са в основата на миналото ви.",
        7: "Вие сте били мислител, често навътре обърнат и фокусиран върху личното разбиране.",
        8: "Успехът и материалният свят са били в центъра на вашето внимание.",
        9: "Вашето минало е белязано от състрадание и служене на другите."
    }
    return tips.get(life_path_number, "Миналото ви е мистериозно и неопределено.")

def future_tip(life_path_number):
    """Return a future prediction based on the life path number."""
    tips = {
        1: "Ще имате възможности да проявите лидерски умения и да достигнете нови висоти.",
        2: "Предстоят периоди на сътрудничество и дълбоки връзки с околните.",
        3: "Бъдете отворени за творчески проекти. Ще има възможности да се изразявате.",
        4: "Очаква ви стабилен период, в който можете да изградите нещо трайно.",
        5: "Новите преживявания ще бъдат ключови. Подгответе се за промени и растеж.",
        6: "Очакват ви възможности за укрепване на семейни и лични връзки.",
        7: "Ще имате време за духовно развитие и дълбоки прозрения.",
        8: "Постигате големи материални цели и успехи в кариерата.",
        9: "В бъдеще ще ви бъде дадена възможност да помагате на другите и да оставите следа."
    }
    return tips.get(life_path_number, "Бъдещето ви е изпълнено с мистерии.")

# Generate Prediction
def generate_prediction(egn):
    info = get_egn_info(egn)
    year = int(egn[:2]) + (1900 if egn[2:4] < '20' else 2000)
    month = int(egn[2:4])
    day = int(egn[4:6])

    zodiac = zodiac_sign(day, month)
    life_path_number = (sum(map(int, egn)) % 9) + 1
    tarot_name, tarot_meaning = tarot_card(life_path_number)
    human_design_info = human_design_details(life_path_number)

    prediction = (
        f"{info}\n\n"
        f"Зодиакален знак: {zodiac}\n"
        f"Таро карта: {tarot_name} - {tarot_meaning}\n\n"
        f"{human_design_info}\n\n"
        f"Минало: {past_tip(life_path_number)}\n"
        f"Бъдеще: {future_tip(life_path_number)}\n"
    )
    return prediction

# Popup for details
def show_details_popup(egn):
    content = Label(text=generate_prediction(egn), size_hint=(1, None), height=400)
    popup = Popup(title="Детайли и Прогноза", content=content, size_hint=(0.9, 0.7))
    popup.open()

class EGNApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(text="Генератор и проверка на ЕГН", font_size=24)
        layout.add_widget(self.label)

        self.region_spinner = Spinner(text="Избери регион", values=list(EGN_REGIONS.keys()), size_hint=(1, None), height=44)
        layout.add_widget(self.region_spinner)

        self.gender_spinner = Spinner(text="Избери пол", values=["Мъж", "Жена"], size_hint=(1, None), height=44)
        layout.add_widget(self.gender_spinner)

        self.day_input = TextInput(hint_text="Ден", multiline=False, size_hint=(1, None), height=40)
        self.month_input = TextInput(hint_text="Месец", multiline=False, size_hint=(1, None), height=40)
        self.year_input = TextInput(hint_text="Година", multiline=False, size_hint=(1, None), height=40)
        layout.add_widget(self.day_input)
        layout.add_widget(self.month_input)
        layout.add_widget(self.year_input)

        self.num_egn_label = Label(text="Брой ЕГН (1-1000):", size_hint=(1, None), height=40)
        layout.add_widget(self.num_egn_label)
        self.num_egn_slider = Slider(min=1, max=1000, value=5, step=1, size_hint=(1, None), height=40)
        layout.add_widget(self.num_egn_slider)

        self.generate_button = Button(text="Генерирай ЕГН", size_hint=(1, None), height=44, on_press=self.generate_egn_list)
        layout.add_widget(self.generate_button)

        self.check_egn_input = TextInput(hint_text="Въведете ЕГН за проверка", multiline=False, size_hint=(1, None), height=40)
        layout.add_widget(self.check_egn_input)

        self.check_button = Button(text="Провери ЕГН", size_hint=(1, None), height=44, on_press=self.check_egn)
        layout.add_widget(self.check_button)

        self.egn_display = GridLayout(cols=1, size_hint_y=None)
        self.egn_display.bind(minimum_height=self.egn_display.setter('height'))
        self.scroll_view = ScrollView(size_hint=(1, 1))
        self.scroll_view.add_widget(self.egn_display)
        layout.add_widget(self.scroll_view)

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

        for _ in range(num_egn):
            egn = generate_sequential_egn(day, month, year, gender, region)
            if egn not in unique_egns:
                unique_egns.add(egn)
                btn = Button(text=egn, size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn_instance: show_details_popup(btn_instance.text))
                self.egn_display.add_widget(btn)
                if len(unique_egns) >= num_egn:
                    break

    def check_egn(self, instance):
        egn = self.check_egn_input.text.strip()
        if len(egn) == 10 and egn.isdigit():
            show_details_popup(egn)
        else:
            popup = Popup(title="Невалидно ЕГН", content=Label(text="Моля, въведете валидно 10-цифрено ЕГН."), size_hint=(0.8, 0.4))
            popup.open()

if __name__ == '__main__':
    EGNApp().run()
