from faker import Faker
import datetime

fake = Faker('ru_RU')

def generate_order_data():
    # Генерируем дату заказа: от 1 до 10 дней от текущей даты
    order_date = datetime.date.today() + datetime.timedelta(days=fake.random_int(min=1, max=10))
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "address": fake.street_address(),
        "metro": fake.random_element(elements=("Белорусская", "Октябрьская", "Площадь Ленина")),
        "phone": fake.msisdn()[:10],  # Берём первые 10 цифр
        "order_date": order_date.strftime("%d.%m.%Y"),
        "rental_period": fake.random_element(elements=("сутки", "двое суток", "трое суток")),
        "comment": fake.sentence(nb_words=5)
    }

# Создаём два набора случайных данных для заказа
order_data = [generate_order_data() for _ in range(2)]

# Константные данные для FAQ-тестов (проверьте актуальные ответы с сайта)
faq_data = [
    {
        "question_index": 0,
        "expected_answer": "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    },
    {
        "question_index": 1,
        "expected_answer": "Пока что у нас такой сервис работает только для одного самоката. А вот как можно заказать несколько, расскажем позже."
    },
    # Добавьте остальные пары вопрос/ответ при необходимости
]
