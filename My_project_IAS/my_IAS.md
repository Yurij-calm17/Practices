1.1 Назва теми: Підвищення ефективності роботи інформаційно-аналітичного підрозділу пункту управління оперативного рівня під час відпрацювання звітно-інформаційних документів

1.2 Актуальність теми: Інформаційно-аналітичні підрозділи (ІАП) відіграють ключову роль в оперативному управлінні, оскільки забезпечують командирів своєчасною, повною та достовірною інформацією для прийняття рішень. Однією з найбільш ресурсоємних функцій є обробка звітно-інформаційних документів. У зв’язку з великим обсягом інформації, різноманітністю форматів та потребою в швидкому аналізі, виникає необхідність автоматизації даного процесу.

Використання Microsoft Access дозволяє створити просту у реалізації, локальну інформаційно-аналітичну систему для обробки, фільтрації, зберігання та часткової інтелектуалізації звітних даних.

1.3 Мета дослідження: Підвищення ефективності функціонування інформаційно-аналітичного підрозділу шляхом автоматизації обробки звітно-інформаційних документів на основі впровадження міні-ІАС, розробленої в середовищі Microsoft Access.

1.4 Об’єкт дослідження: Інформаційна діяльність підрозділів військового управління оперативного рівня.

1.5 Предмет дослідження: Технології збору, збереження, аналізу та візуалізації звітно-інформаційних документів в умовах функціонування пункту управління.

1.6 Завдання дослідження:

Проаналізувати особливості організації звітного документообігу в ІАП.

Визначити основні недоліки чинної моделі обробки інформації.

Розробити структуру бази даних для зберігання звітних документів у Microsoft Access.

Реалізувати систему обробки та перегляду документів (форми, запити, звіти).

Оцінити ефективність впровадженого рішення та його вплив на оперативність роботи підрозділу.

1.7 Очікуваний результат: Функціональна інформаційно-аналітична система, реалізована в Microsoft Access, яка дозволяє структуровано зберігати, аналізувати та візуалізувати звітну інформацію, знижуючи час її обробки та підвищуючи точність і повноту аналітичних узагальнень.

#📌 2. Структура бази даних у Microsoft Access
Метою цього етапу є визначення сутностей, таблиць і зв’язків, необхідних для моделювання звітно-інформаційного процесу в ІАП.

2.1 Основні функціональні компоненти ІАС:

Зберігання звітно-інформаційних документів

Ведення обліку авторів/відправників документів

Відстеження обробки документів (стан, відповідальні)

Витяг ключових параметрів документа

Аналітична звітність і фільтрація за запитами

2.2 Сутності та таблиці бази даних

Документи
Зберігає основну інформацію про кожен звітно-інформаційний документ.

ID_Документа (Автонумерація, ключове поле)

Дата_реєстрації (Дата/час)

Назва_документа (Текст)

Тип_документа (Комбо-поле: Звіт, Оперативне зведення, Прогноз, Інше)

Автор (Зовнішній ключ до таблиці Користувачі)

Підрозділ (Текст або зовнішній ключ)

Рівень_важливості (Комбо-поле: Низький, Середній, Високий)

Статус_обробки (Комбо-поле: Прийнято, В роботі, Погоджено, Відхилено)

Короткий_зміст (Текстове поле MEMO)

Шлях_до_файлу (Текст — для зв’язку з документом у файловій системі)

Користувачі
Облік осіб, що створюють або обробляють документи.

ID_Користувача (Автонумерація)

ПІБ (Текст)

Посада (Текст)

Підрозділ (Текст)

Роль (Комбо: Аналітик, Керівник, Відповідальний)

Журнал_змін
Лог дій користувачів над документами (для відстеження етапів обробки).

ID_Запису (Автонумерація)

ID_Документа (Зовнішній ключ)

Дата_дії (Дата/час)

Дія (Текст)

Користувач (Зовнішній ключ)

Типи_документів (довідник)

ID_Типу (Автонумерація)

Назва_типу (Текст)

Опис (Текст)

(Опціонально: можна реалізувати цю таблицю або використовувати фіксовані значення у комбо-полі.)

2.3 Зв’язки між таблицями:

Документи.ID_Документа = Журнал_змін.ID_Документа (один до багатьох)

Користувачі.ID_Користувача = Документи.Автор (один до багатьох)

Користувачі.ID_Користувача = Журнал_змін.Користувач (один до багатьох)

2.4 Рекомендації до реалізації в Access:

Створити всі таблиці за допомогою конструктора.

Встановити типи даних: короткий текст, довгий текст (для змісту), дата/час, числовий (ID), логічний (у разі потреби).

Визначити зв’язки через вікно «Схема даних» (Relationships).

Для комбо-полів використовувати списки значень або підключення до довідників.

📌 3. Розробка форм у Microsoft Access

Мета цього кроку — створити зручний інтерфейс для роботи з документами: введення, перегляду, фільтрації, а також обробки змін.

Нижче подано перелік форм, які варто реалізувати, їх функціональні особливості та рекомендовану структуру:

3.1 Головна форма (панель навігації)

Призначення:

Вхідна точка системи

Швидкий доступ до основних функцій

Елементи:

Кнопки: Ввести новий документ, Переглянути документи, Статистика, Користувачі, Вихід

Логотип або назва системи

Можливо: вітальне повідомлення та поточна дата

3.2 Форма введення нового документа (форма Документи)

Тип: Зв’язана форма

Джерело записів: таблиця Документи

Елементи:

Поля: Дата_реєстрації (автозаповнення сьогоднішньою датою), Назва_документа, Тип (випадаючий список), Автор (комбо зі списку користувачів), Підрозділ, Рівень_важливості, Статус (за замовчуванням — “Прийнято”), Короткий_зміст, Шлях_до_файлу

Кнопки: Зберегти, Очистити, Повернутися

Особливості:

Тип_документа реалізувати через поле з підстановкою значень або зв’язок із таблицею Типи_документів

Автор — комбо-поле, що тягне дані з таблиці Користувачі

Можна додати подію VBA для автозаповнення дати

3.3 Форма перегляду/редагування документів

Тип: Форма + підформа (або вкладки)

Елементи:

Таблиця з усіма документами

Поля фільтра: Тип, Дата від/до, Статус, Автор

Кнопки: Відкрити документ, Редагувати, Додати до журналу, Сформувати звіт

Можна додати сортування за датою/важливістю

3.4 Форма журналу змін (форма Журнал_змін)

Тип: Підформа або окрема форма

Джерело записів: таблиця Журнал_змін

Елементи:

Поля: ID_Документа (комбо або приховане), Дата_дії (автозаповнення), Дія (випадаючий список: “Прийнято”, “Передано”, “Погоджено”, “Завершено”), Користувач

Кнопки: Додати запис, Очистити

3.5 Форма користувачів (форма Користувачі)

Тип: форма на основі таблиці Користувачі

Елементи:

Поля: ПІБ, Посада, Підрозділ, Роль

Кнопки: Додати, Видалити, Редагувати

3.6 Додатково (опціонально)

Спливаючі повідомлення/підказки (через макроси або VBA)

Перевірка обов’язкових полів перед збереженням

Можливість експорту звіту в PDF (через макрос або VBA)

📌 4. Побудова запитів та аналітичних звітів у Microsoft Access

Цей крок передбачає створення SQL-запитів (запити на вибірку, параметричні, агрегатні), які забезпечують аналітичну обробку інформації, збереженої в базі даних, та дозволяють формувати звіти за встановленими критеріями.

4.1 Запити на вибірку (SELECT-запити)

Запит: Усі документи за певний період

Мета: відобразити документи, зареєстровані в обраному діапазоні дат.

Поля: Назва_документа, Дата_реєстрації, Тип_документа, Автор, Підрозділ, Статус

Критерії: [Введіть дату початку:] і [Введіть дату завершення:]

Запит: Непогоджені або відхилені документи

Мета: виявити документи, які не отримали остаточного статусу.

Критерій у полі Статус: "В роботі" або "Відхилено"

Запит: Документи певного типу

Мета: відібрати документи за обраним типом (наприклад, лише "Оперативне зведення").

Критерій у полі Тип_документа: [Введіть тип документа:]

4.2 Агрегатні (підсумкові) запити

Запит: Кількість документів за типами

Групування по полю Тип_документа

Агрегація: Count(ID_Документа)

Запит: Кількість документів по підрозділах

Поля: Підрозділ, Count(ID_Документа)

Запит: Кількість документів за рівнем важливості

Поля: Рівень_важливості, Count(ID_Документа)

4.3 Параметричні звіти

Можна реалізувати звіти, які відкриваються через кнопку на формі або через макрос:

Звіт «Зведення по документах за тиждень»

Джерело: запит з критеріями дати

Вміст: перелік документів + підсумок за типами

Звіт «Аналіз обробки документів»

Джерело: Журнал_змін

Вміст: кількість дій кожного користувача, середній час обробки

Звіт «Звіт по користувачу»

Запит на вибірку документів автора

Параметр: [Введіть ПІБ автора:]

4.4 Візуалізація та діаграми

У звітах можна додати:

Діаграми типу "Кругова" (розподіл за типами)

"Стовпчикові" графіки (по підрозділах, статусах)

Таблиці з умовним форматуванням (наприклад, виділення "Відхилено" червоним кольором)

4.5 Автоматизація

Кнопки на формах для запуску запитів та відкриття звітів

Макроси для експорту звітів у PDF

VBA-скрипти для підрахунку часу між створенням документа та погодженням

✅ Після реалізації запитів і звітів у Access твоя система отримає аналітичну силу, необхідну для підтримки рішень.