from prompt_toolkit.completion import WordCompleter
from code_crafters_core.RecordData import bcolors
from abc import ABC, abstractmethod
from typing import List, Tuple, Union, Optional, Type, Callable
from code_crafters_core.NoteFeature import *


class LanguagesCommandsPrompts(ABC):
    @abstractmethod
    def gets_commands_prompts(self) -> List[str]:
        pass


class RussianCommandsPrompts(LanguagesCommandsPrompts):
    def gets_commands_prompts(self) -> List[str]:
        return [
            "🎩✨ Абракадабра! Введите волшебную команду:✍️  ",
            "👋 Скажите мне, что вы хотите сделать:✍️  ",
            "👋 Привет! Чем я могу помочь? Введите команду:✍️  ",
            "💫 Жду вашу команду для начала работы:✍️  ",
            "👋 Добро пожаловать в удивительный мир возможностей! Ожидаю вашей команды для начала:✍️  ",
            "🌈 Добро пожаловать в мир возможностей! Ожидаю вашей волшебной команды:✍️  ",
            "🌈 Доброго времени суток! Ожидаю вашей команды:✍️ ",
            "🌈 Привет! Какие чудеса сегодня?:✍️  ",
        ]


class EnglishCommandsPrompts(LanguagesCommandsPrompts):
    def gets_commands_prompts(self) -> List[str]:
        return [
            "🎩✨ Abracadabra! Enter the magic command:✍️  ",
            "👋 Let me know what you want to do:✍️  ",
            "🎩✨ Tell me what you want to do: ",
            "💫 Waiting for your command to start work:✍️  ",
            "👋 Welcome to the amazing world of opportunities! Waiting for your command to start:✍️  ",
            "🌈 Welcome to the world of opportunities! Waiting for your magic command:✍️  ",
            "🎩✨ Welcome to the magical world of possibilities! Enter the magic command:✍️ ",
            "👋 Hello! How can I help? Enter a command:✍️  ",
            "🌈 Good day! Waiting for your command:✍️  ",
            "💫 Greetings! Enter a command:✍️  ",
            "👋 Hello! What wonders do you seek today?:✍️  ",
        ]


class UkrainianCommandsPrompts(LanguagesCommandsPrompts):
    def gets_commands_prompts(self) -> List[str]:
        return [
            "🎩✨ Абракадабра! Введіть магічну команду:✍️  ",
            "👋 Будьте добрі скажіть, що я маю зробити:✍️  ",
            "💫 Чекаю на ваші накази:✍️  ",
            "👋 Вітаю Вас в чарівному світі можливостей! Чекаю на Вашу команду для початку:✍️  ",
            "🌈 Вітаю Вас в чарівному світі можливостей! Чекаю на Вашу чарівну команду:✍️  ",
            "🎩✨ Абракадабра! Введіть чарівну команду:✍️  ",
            "🎩✨ Скажіть мені, що ви хочете зробити:✍️  ",
            "👋 Привіт! Як я можу допомогти? Введіть команду:✍️  ",
            "🌈 Доброго дня! Очікую вашої команди:✍️  ",
            "💫 Вітаю вас! Введіть команду:✍️  ",
            "🕰 Привіт! Які чудеса сьогодні?:✍️ ",
        ]


class LanguagesCommandsList(ABC):
    @abstractmethod
    def gets_commands_list(self) -> List[str]:
        pass


class RussianCommandsList(LanguagesCommandsList):
    def gets_commands_list(self) -> List[str]:
        return WordCompleter(
            [
                "команды",
                "изменить язык",
                "добавление контакта",
                "поиск контакта",
                "показать все контакты",
                "добавить телефон",
                "удалить телефон",
                "добавить электронную почту",
                "удалить электронную почту",
                "редактировать телефон",
                "редактировать электронную почту",
                "редактировать день рождения",
                "удалить контакт",
                "показать дни рождения",
                "добавить заметку",
                "найти заметку",
                "показать все заметки",
                "редактировать заметку",
                "удалить заметку",
                "добавить тег",
                "редактировать тег",
                "удалить тег",
                "найти и отсортировать по тегам",
                "сортировать файлы",
                "показать все разширения",
                "добавить расширение",
                "удалить расширение",
                "выход",
            ]
        )


class EnglishCommandsList(LanguagesCommandsList):
    def gets_commands_list(self) -> List[str]:
        return WordCompleter(
            [
                "cli",
                "change language",
                "contact add",
                "contact find",
                "contact show all",
                "contact phone add",
                "contact phone remove",
                "contact email add",
                "contact email remove",
                "contact phone edit",
                "contact email edit",
                "contact birthday edit",
                "contact remove",
                "display birthdays",
                "note add",
                "note find",
                "note show all",
                "note edit",
                "note remove",
                "tag add",
                "tag edit",
                "tag remove",
                "tag find sort",
                "file sort",
                "file extension-show",
                "file extension-add",
                "file extension-remove",
                "quit",
                "exit",
                "q",
            ]
        )


class UkrainianCommandsList(LanguagesCommandsList):
    def gets_commands_list(self) -> List[str]:
        return WordCompleter(
            [
                "можливості",
                "зміти мову",
                "додати контакт",
                "пошук контакта",
                "показати всі контакти",
                "додати телефон",
                "видалити телефон",
                "додати електронну пошту",
                "видалити електронну пошту",
                "редагувати телефон",
                "редагувати електронну пошту",
                "редагувати день народження",
                "видалити контакт",
                "показати дні народження",
                "додати нотатку",
                "знайти нотатку",
                "показати всі нотатки",
                "редагувати нотатку",
                "видалити нотатку",
                "додати тег",
                "редагувати тег",
                "видалити тег",
                "знайти та сортувати по тегам",
                "відсортувати файли",
                "показати всі розширення",
                "додати розширення файла",
                "видалити розширення файла",
                "до зустрічі",
            ]
        )


class LanguagesErrorCommandMessages(ABC):
    @abstractmethod
    def gets_error_command_messages(self) -> List[str]:
        pass


class RussianErrorCommandMessages(LanguagesErrorCommandMessages):
    def gets_error_command_messages(self) -> List[str]:
        return [
            f"{bcolors.WARNING}🙃 Ой! Похоже, вы ввели неправильную команду. Пожалуйста, попробуйте снова!😔{bcolors.RESET}",
            f"{bcolors.WARNING}😟 Упс! Это не похоже на правильную команду. Давайте попробуем еще раз😔{bcolors.RESET}",
            f"{bcolors.WARNING}😯 Ошибка: Команда не распознана. Попробуйте еще раз.😔{bcolors.RESET}",
            f"{bcolors.WARNING}😮 Хмм, я не понимаю эту команду. Давайте попробуем что-то еще.😔{bcolors.RESET}",
        ]


class EnglishErrorCommandMessages(LanguagesErrorCommandMessages):
    def gets_error_command_messages(self) -> List[str]:
        return [
            f"{bcolors.WARNING}🙃 Oh! You seem to have introduced the wrong command. Please try again!😔{bcolors.RESET}",
            f"{bcolors.WARNING}😔 Oops! This is not like the right command. Let's try again😔{bcolors.RESET}",
            f"{bcolors.WARNING}😟 Error: The command is not recognized. Try again.😔{bcolors.RESET}",
            f"{bcolors.WARNING}😮 Hmm, I don't understand this command. Let's try something else.😔{bcolors.RESET}",
        ]


class UkrainianErrorCommandMessages(LanguagesErrorCommandMessages):
    def gets_error_command_messages(self) -> List[str]:
        return [
            f"{bcolors.WARNING}😔 Ой! Начебто Ви ввели хибну команду. Будь ласка спробуйте ыще раз!😔{bcolors.RESET}",
            f"{bcolors.WARNING}😯 Упс! Це не схоже правельну команду. Давайте спробуэмо ыще раз!😔{bcolors.RESET}",
            f"{bcolors.WARNING}😔 Помилка: Незрозумыла команда. Спробуйте іще раз.😔{bcolors.RESET}",
            f"{bcolors.WARNING}😔😮 Хмм, я не розумію цю команду. давайте спробуємо щось інше!😔{bcolors.RESET}",
        ]


class LanguagesAllAvailableCommands(ABC):
    @abstractmethod
    def gets_all_available_commands(self) -> List[str]:
        pass

    @abstractmethod
    def gets_all_available_commands_description(self) -> List[str]:
        pass


class RussianAllAvailableCommands(LanguagesAllAvailableCommands):
    def gets_all_available_commands(self) -> List[str]:
        return [
            f"{bcolors.ORANGE}команды{bcolors.RESET}",
            f"{bcolors.ORANGE}изменить язык{bcolors.RESET}",
            f"{bcolors.ORANGE}добавление контакта{bcolors.RESET}",
            f"{bcolors.ORANGE}поиск контакта{bcolors.RESET}",
            f"{bcolors.ORANGE}показать все контакты{bcolors.RESET}",
            f"{bcolors.ORANGE}добавить телефон{bcolors.RESET}",
            f"{bcolors.ORANGE}удалить телефон{bcolors.RESET}",
            f"{bcolors.ORANGE}добавить электронную почту{bcolors.RESET}",
            f"{bcolors.ORANGE}удалить электронную почту{bcolors.RESET}",
            f"{bcolors.ORANGE}редактировать телефон{bcolors.RESET}",
            f"{bcolors.ORANGE}редактировать электронную почту{bcolors.RESET}",
            f"{bcolors.ORANGE}редактировать день рождения{bcolors.RESET}",
            f"{bcolors.ORANGE}удалить контакт{bcolors.RESET}",
            f"{bcolors.ORANGE}показать дни рождения{bcolors.RESET}",
            f"{bcolors.ORANGE}добавить заметку{bcolors.RESET}",
            f"{bcolors.ORANGE}найти заметку{bcolors.RESET}",
            f"{bcolors.ORANGE}показать все заметки{bcolors.RESET}",
            f"{bcolors.ORANGE}редактировать заметку{bcolors.RESET}",
            f"{bcolors.ORANGE}удалить заметку{bcolors.RESET}",
            f"{bcolors.ORANGE}добавить тег{bcolors.RESET}",
            f"{bcolors.ORANGE}редактировать тег{bcolors.RESET}",
            f"{bcolors.ORANGE}удалить тег{bcolors.RESET}",
            f"{bcolors.ORANGE}найти и отсортировать по тегам{bcolors.RESET}",
            f"{bcolors.ORANGE}сортировать файлы{bcolors.RESET}",
            f"{bcolors.ORANGE}показать все разширения{bcolors.RESET}",
            f"{bcolors.ORANGE}добавить расширение{bcolors.RESET}",
            f"{bcolors.ORANGE}удалить расширение{bcolors.RESET}",
            f"{bcolors.ORANGE}выход{bcolors.RESET}",
        ]

    def gets_all_available_commands_description(self) -> List[str]:
        return [
            f"{bcolors.BLUE}выводит список всех доступных команд{bcolors.RESET}",
            f"{bcolors.BLUE}изменение языка приложения{bcolors.RESET}",
            f"{bcolors.BLUE}сохраняет контакт с именем, адресом, номером телефона, электронной почтой и днем рождения в контактную книгу{bcolors.RESET}",
            f"{bcolors.BLUE}ищет контакт в книге контактов{bcolors.RESET}",
            f"{bcolors.BLUE}показывает все существующие контакты в книге контактов{bcolors.RESET}",
            f"{bcolors.BLUE}добавить еще 1-ин телефон к существующему контакту{bcolors.RESET}",
            f"{bcolors.BLUE}удаление существующего телефона{bcolors.RESET}",
            f"{bcolors.BLUE}добавить еще 1-ин почту к существующему контакту{bcolors.RESET}",
            f"{bcolors.BLUE}удалять существующее почту{bcolors.RESET}",
            f"{bcolors.BLUE}редактировать телефон действующего контактного лица{bcolors.RESET}",
            f"{bcolors.BLUE}редактирование электронной почты существующего контакта{bcolors.RESET}",
            f"{bcolors.BLUE}редактирование дня рождения существующего контакта{bcolors.RESET}",
            f"{bcolors.BLUE}удалять существующий контакт{bcolors.RESET}",
            f"{bcolors.BLUE}отображает список контактов, имеющих день рождения после указанного числа дней с текущей даты{bcolors.RESET}",
            f"{bcolors.BLUE}сохраняет примечание по имени автора{bcolors.RESET}",
            f"{bcolors.BLUE}поиск примечаний среди существующих примечаний{bcolors.RESET}",
            f"{bcolors.BLUE}показывает все существующие примечания{bcolors.RESET}",
            f"{bcolors.BLUE}редактирование существующей записки{bcolors.RESET}",
            f"{bcolors.BLUE}удаление существующего примечания{bcolors.RESET}",
            f"{bcolors.BLUE}добавление тегов в существующее примечание{bcolors.RESET}",
            f"{bcolors.BLUE}редактирование тегов для существующей заметки{bcolors.RESET}",
            f"{bcolors.BLUE}удаление тегов из существующей записи{bcolors.RESET}",
            f"{bcolors.BLUE}поиск и сортировка заметок по тегам{bcolors.RESET}",
            f"{bcolors.BLUE}Сортировать файлы в указанной папке по категориям (изображения, документы, видео и т.д.).{bcolors.RESET}",
            f"{bcolors.BLUE}показать все доступные расширения для сортировки.{bcolors.RESET}",
            f"{bcolors.BLUE}добавление дополнительного расширения для сортировки{bcolors.RESET}",
            f"{bcolors.BLUE}удаление расширения из списка для сортировки{bcolors.RESET}",
            f"{bcolors.BLUE}завершение работы бота{bcolors.RESET}",
        ]


class EnglishAllAvailableCommands(LanguagesAllAvailableCommands):
    def gets_all_available_commands(self) -> List[str]:
        return [
            f"{bcolors.ORANGE}cli{bcolors.RESET}",
            f"{bcolors.ORANGE}change language{bcolors.RESET}",
            f"{bcolors.ORANGE}contact add{bcolors.RESET}",
            f"{bcolors.ORANGE}contact find{bcolors.RESET}",
            f"{bcolors.ORANGE}contact show all{bcolors.RESET}",
            f"{bcolors.ORANGE}contact phone add{bcolors.RESET}",
            f"{bcolors.ORANGE}contact phone remove{bcolors.RESET}",
            f"{bcolors.ORANGE}contact email add{bcolors.RESET}",
            f"{bcolors.ORANGE}contact email remove{bcolors.RESET}",
            f"{bcolors.ORANGE}contact phone edit{bcolors.RESET}",
            f"{bcolors.ORANGE}contact email edit{bcolors.RESET}",
            f"{bcolors.ORANGE}contact birthday edit{bcolors.RESET}",
            f"{bcolors.ORANGE}contact remove{bcolors.RESET}",
            f"{bcolors.ORANGE}display birthdays{bcolors.RESET}",
            f"{bcolors.ORANGE}note add{bcolors.RESET}",
            f"{bcolors.ORANGE}note find{bcolors.RESET}",
            f"{bcolors.ORANGE}note show all{bcolors.RESET}",
            f"{bcolors.ORANGE}note edit{bcolors.RESET}",
            f"{bcolors.ORANGE}note remove{bcolors.RESET}",
            f"{bcolors.ORANGE}tag add{bcolors.RESET}",
            f"{bcolors.ORANGE}tag edit{bcolors.RESET}",
            f"{bcolors.ORANGE}tag remove{bcolors.RESET}",
            f"{bcolors.ORANGE}tag find sort{bcolors.RESET}",
            f"{bcolors.ORANGE}file sort{bcolors.RESET}",
            f"{bcolors.ORANGE}file extension show{bcolors.RESET}",
            f"{bcolors.ORANGE}file extension add{bcolors.RESET}",
            f"{bcolors.ORANGE}file extension remove{bcolors.RESET}",
            f"{bcolors.ORANGE}quit{bcolors.RESET}",
            f"{bcolors.ORANGE}exit{bcolors.RESET}",
            f"{bcolors.ORANGE}q{bcolors.RESET}",
        ]

    def gets_all_available_commands_description(self) -> List[str]:
        return [
            f"{bcolors.BLUE}display a list of all available commands{bcolors.RESET}",
            f"{bcolors.BLUE}change the application language{bcolors.RESET}",
            f"{bcolors.BLUE}save a contact with name, address, phone number, email, and birthday to the contacts book{bcolors.RESET}",
            f"{bcolors.BLUE}search for a contact among the contacts in the book{bcolors.RESET}",
            f"{bcolors.BLUE}show all existing contacts in the contacts book{bcolors.RESET}",
            f"{bcolors.BLUE}add another phone number to an existing contact{bcolors.RESET}",
            f"{bcolors.BLUE}delete an existing phone number{bcolors.RESET}",
            f"{bcolors.BLUE}add another email to an existing contact{bcolors.RESET}",
            f"{bcolors.BLUE}delete an existing email{bcolors.RESET}",
            f"{bcolors.BLUE}edit the phone number of an existing contact{bcolors.RESET}",
            f"{bcolors.BLUE}edit the email of an existing contact{bcolors.RESET}",
            f"{bcolors.BLUE}edit the birthday of an existing contact{bcolors.RESET}",
            f"{bcolors.BLUE}delete an existing contact{bcolors.RESET}",
            f"{bcolors.BLUE}display a list of contacts whose birthday is within a specified number of days from the current date{bcolors.RESET}",
            f"{bcolors.BLUE}save a note with the author's name{bcolors.RESET}",
            f"{bcolors.BLUE}search for a note among existing notes{bcolors.RESET}",
            f"{bcolors.BLUE}show all existing notes{bcolors.RESET}",
            f"{bcolors.BLUE}edit an existing note{bcolors.RESET}",
            f"{bcolors.BLUE}delete an existing note{bcolors.RESET}",
            f"{bcolors.BLUE}add tags to an existing note{bcolors.RESET}",
            f"{bcolors.BLUE}edit tags of an existing note{bcolors.RESET}",
            f"{bcolors.BLUE}remove tags from an existing note{bcolors.RESET}",
            f"{bcolors.BLUE}search and sort notes by tags{bcolors.RESET}",
            f"{bcolors.BLUE}sort files in the specified folder by categories (images, documents, videos, etc.){bcolors.RESET}",
            f"{bcolors.BLUE}show all extensions{bcolors.RESET}",
            f"{bcolors.BLUE}add additional extension for sorting{bcolors.RESET}",
            f"{bcolors.BLUE}remove an extension from the sorting list{bcolors.RESET}",
            f"{bcolors.BLUE}exit the program{bcolors.RESET}",
            f"{bcolors.BLUE}exit the program{bcolors.RESET}",
            f"{bcolors.BLUE}exit the program{bcolors.RESET}",
        ]


class UkrainianAllAvailableCommands(LanguagesAllAvailableCommands):
    def gets_all_available_commands(self) -> List[str]:
        return [
            f"{bcolors.ORANGE}команди{bcolors.RESET}",
            f"{bcolors.ORANGE}зміти мову{bcolors.RESET}",
            f"{bcolors.ORANGE}додати контакт{bcolors.RESET}",
            f"{bcolors.ORANGE}пошук контакта{bcolors.RESET}",
            f"{bcolors.ORANGE}показати всі контакти{bcolors.RESET}",
            f"{bcolors.ORANGE}додати телефон{bcolors.RESET}",
            f"{bcolors.ORANGE}видалити телефон{bcolors.RESET}",
            f"{bcolors.ORANGE}додати електронну пошту{bcolors.RESET}",
            f"{bcolors.ORANGE}видалити електронну пошту{bcolors.RESET}",
            f"{bcolors.ORANGE}редагувати телефон{bcolors.RESET}",
            f"{bcolors.ORANGE}редагувати електронну пошту{bcolors.RESET}",
            f"{bcolors.ORANGE}редагувати день народження{bcolors.RESET}",
            f"{bcolors.ORANGE}видалити контакт{bcolors.RESET}",
            f"{bcolors.ORANGE}показати дні народження{bcolors.RESET}",
            f"{bcolors.ORANGE}додати нотатку{bcolors.RESET}",
            f"{bcolors.ORANGE}знайти нотатку{bcolors.RESET}",
            f"{bcolors.ORANGE}показати всі нотатки{bcolors.RESET}",
            f"{bcolors.ORANGE}редагувати нотатку{bcolors.RESET}",
            f"{bcolors.ORANGE}видалити нотатку{bcolors.RESET}",
            f"{bcolors.ORANGE}додати тег{bcolors.RESET}",
            f"{bcolors.ORANGE}редагувати тег{bcolors.RESET}",
            f"{bcolors.ORANGE}видалити тег{bcolors.RESET}",
            f"{bcolors.ORANGE}знайти та сортувати по тегам{bcolors.RESET}"
            f"{bcolors.ORANGE}відсортувати файли{bcolors.RESET}",
            f"{bcolors.ORANGE}показати всі розширення{bcolors.RESET}",
            f"{bcolors.ORANGE}додати розширення файла{bcolors.RESET}",
            f"{bcolors.ORANGE}видалити розширення файла{bcolors.RESET}",
            f"{bcolors.ORANGE}вихід{bcolors.RESET}",
        ]

    def gets_all_available_commands_description(self) -> List[str]:
        return [
            f"{bcolors.BLUE}виводить список всіх доступних команд{bcolors.RESET}",
            f"{bcolors.BLUE}змінити мову додатка{bcolors.RESET}",
            f"{bcolors.BLUE}зберігає контакт з іменем, адресом, номером телефона, пошту та днем народження до книги контактів{bcolors.RESET}",
            f"{bcolors.BLUE}здійснює пошук контакту серед контактів книги{bcolors.RESET}",
            f"{bcolors.BLUE}показує всі існуючі контакти в книзі контактів{bcolors.RESET}",
            f"{bcolors.BLUE}додати іще 1-ин телефон до існуючого контакту{bcolors.RESET}",
            f"{bcolors.BLUE}видалення існуючого телефон{bcolors.RESET}",
            f"{bcolors.BLUE}додати іще 1-ин пошту до існуючого контакту{bcolors.RESET}",
            f"{bcolors.BLUE}видалення існуючу пошту{bcolors.RESET}",
            f"{bcolors.BLUE}редагування телефон існуючого контакту{bcolors.RESET}",
            f"{bcolors.BLUE}редагування пошти існуючого контакту{bcolors.RESET}",
            f"{bcolors.BLUE}редагування дня народження існуючого контакту{bcolors.RESET}",
            f"{bcolors.BLUE}видалення існуючого контакту{bcolors.RESET}",
            f"{bcolors.BLUE}виводить список контактів, у яких день народження через задану кількість днів від поточної дати{bcolors.RESET}",
            f"{bcolors.BLUE}зберігає нотатку за іменем автора{bcolors.RESET}",
            f"{bcolors.BLUE}здійснює пошук нотатки серед існуючих нотатків{bcolors.RESET}",
            f"{bcolors.BLUE}показує всі існуючі нотатки{bcolors.RESET}",
            f"{bcolors.BLUE}редагування існуючої нотатки{bcolors.RESET}",
            f"{bcolors.BLUE}видалення існуючої нотатки{bcolors.RESET}",
            f"{bcolors.BLUE}додавання тегів до існуючої нотатки{bcolors.RESET}",
            f"{bcolors.BLUE}редагування тегів існуючої нотатки{bcolors.RESET}",
            f"{bcolors.BLUE}видалення тегів з існуючої нотатки{bcolors.RESET}",
            f"{bcolors.BLUE}пошук та сортування нотаток за тегами{bcolors.RESET}",
            f"{bcolors.BLUE}сортування файлів у зазначеній папці за категоріями (зображення, документи, відео та ін.).{bcolors.RESET}",
            f"{bcolors.BLUE}показати всі наявні розширеннядля сортування{bcolors.RESET}",
            f"{bcolors.BLUE}додавання додатково розширення для сортування{bcolors.RESET}",
            f"{bcolors.BLUE}видалення розширення із списку для сортування{bcolors.RESET}",
            f"{bcolors.BLUE}завершення роботи бота{bcolors.RESET}",
        ]
