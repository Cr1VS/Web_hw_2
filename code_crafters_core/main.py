from code_crafters_core.AvadaKedavra import shutdown_with_countdown
from code_crafters_core.FileSorting import executing_command
from prompt_toolkit.application.current import get_app
from code_crafters_core.RecordData import bcolors
from code_crafters_core.AddressBook import *
from code_crafters_core.NoteFeature import *
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from pathlib import Path
from code_crafters_core.Languages import *
import threading
import asyncio
import random


def pre_run() -> None:
    app = get_app()
    b = app.current_buffer
    if b.complete_state:
        b.complete_next()
    else:
        b.start_completion(select_first=False)

def choose_language() -> str:
    while True:
        language = input(f"{bcolors.BOLD}🏳️  Please choose a language (en/ru/ua): {bcolors.RESET}")
        if language in ("en", "ru", 'ua'):
            return language
        else:
            print(f"{bcolors.WARNING}🙃 Wrong language format entered!{bcolors.RESET}\n{bcolors.BLUE}Please enter en | ru or ua to choose language:{bcolors.RESET}")

def one_command_vizualization(user_input: str, lists: Tuple[list, list]) -> str:
    if user_input:
        for com_list, ex_com in zip(lists[0], lists[1]):  
            if com_list.__contains__(user_input):
                return f"{com_list} {ex_com}"
    return ""

def available_commands(command: Optional[str] = None) -> Union[Tuple[list, list], str]:

    if language == "en":
        english_all_available_commands = EnglishAllAvailableCommands()
        command_list = english_all_available_commands.gets_all_available_commands()
        command_description = english_all_available_commands.gets_all_available_commands_description()

    elif language == "ru":
        russian_all_available_commands = RussianAllAvailableCommands()
        command_list = russian_all_available_commands.gets_all_available_commands()
        command_description = russian_all_available_commands.gets_all_available_commands_description()
      
    elif language == "ua":
        ukrainian_all_available_commands = UkrainianAllAvailableCommands()
        command_list = ukrainian_all_available_commands.gets_all_available_commands()
        command_description = ukrainian_all_available_commands.gets_all_available_commands_description()

    if command:
        return (command_list, command_description)

    return "".join(
        "|{:<10} - {:<20}|\n".format(command_list[item], command_description[item])
        for item in range(len(command_list))
    )

async def get_input() -> str:
    global exit_flag
    if language == "ru":
        commands_prompts = RussianCommandsPrompts()
        commands_prompts = commands_prompts.gets_commands_prompts()        
        commands_explain = RussianCommandsList()
        commands_list = commands_explain.gets_commands_list()
        print(f"{bcolors.PINK}🤖 Я здесь, чтобы сделать твой день немного ярче!\n🌞 Не стесняйтесь задавать вопросы или просто общаться. Вместе мы можем сделать этот день незабываемым! 🎉🎈{bcolors.RESET}")
    elif language == "en":
        commands_prompts = EnglishCommandsPrompts()
        commands_prompts = commands_prompts.gets_commands_prompts()       
        commands_explain = EnglishCommandsList()
        commands_list = commands_explain.gets_commands_list()
        print(f"{bcolors.PINK}🤖 I'm here to make your day a little brighter!\n🌞 Feel free to ask questions or just communicate. Together we can make this day unforgettable!{bcolors.RESET}")
    elif language == "ua" :
        commands_prompts = UkrainianCommandsPrompts()
        commands_prompts = commands_prompts.gets_commands_prompts()       
        commands_explain = UkrainianCommandsList()
        commands_list = commands_explain.gets_commands_list()
        print(f"{bcolors.PINK}🤖 Я тут, щоб зробити ваш день трохи яскравішим!\n🌞 Не соромтеся задавати питання або просто спілкуватися. Разом ми можемо зробити цей день незабутнім!{bcolors.RESET}")   
    try:
        session = PromptSession()
        result = await session.prompt_async(
            random.choice(commands_prompts),
            completer=commands_list,
            pre_run=pre_run,
            style=Style.from_dict({"prompt": "bg:#ansigreen #ffffff"}),
        )
        timer_thread.cancel()
        return result
    except KeyboardInterrupt:
        print(f"\n{bcolors.FAIL}❌ KeyBoard interrupt error, EXITING❗{bcolors.RESET}\n")
        save_to_file_contacts(file_name, book)
        save_to_file_notes(note_name, note)
        exit_flag = True       
    except RuntimeError:
        pass

def timer_function() -> None:
    print(f"\n{bcolors.WARNING}⏰ Time's up! You didn't enter any command💀 {bcolors.RESET}")
    print(f"{bcolors.WARNING}😄 I'm offended, you're not using me, so I run the Awadakedabra command and I shut down you forever!💀 {bcolors.RESET}")
    shutdown_with_countdown()

def wait_for_input(timeout: int = 120, timeout2: int = 1000) -> Optional[str]:
    loop = asyncio.get_event_loop()
    result = None
    global timer_thread

    async def wait_input():
        nonlocal result
        result = await get_input()
        
    timer_thread = threading.Timer(timeout2, timer_function)
    timer_thread.start()

    try:
        loop.run_until_complete(asyncio.wait_for(wait_input(), timeout=timeout))
    except asyncio.TimeoutError:
        print(f"{bcolors.ORANGE}\n⏰: You are here, I'm waiting for your command{bcolors.RESET}")
    
    return result

def deserialize(file_path: Path, class_instance: Type[Union[AddressBook, NoteBook]], read_from_file_func: Callable[..., Union[AddressBook, NoteBook]]) -> Union[AddressBook, NoteBook]:
    if file_path.exists() and file_path.is_file():
        with open(file_path, "rb") as fh:
            check_content = fh.read()

        if not check_content:
            instance = class_instance()
        else:
            instance = read_from_file_func(file_path)
            
    else:
        with open(file_path, "wb"):
            pass
        instance = class_instance()
        
    return instance

def save_to_file_contacts(file_path: Path, instance) -> None:
    serialization = AddressBook()
    serialization.save_to_file(file_path, instance)
    
def save_to_file_notes(file_path: Path, instance) -> None:
    serialization = NoteBook()
    serialization.note_save_to_file(file_path, instance)
    
def main():  
    global exit_flag
    global file_name
    global note_name
    global book
    global note
    global language
 
    file_name = "database.bin"
    note_name = "notebase.bin"
    
    file_database = Path(file_name)
    note_database = Path(note_name)  

    book = deserialize(file_database, AddressBook, AddressBook.read_from_file)
    note = deserialize(note_database, NoteBook, NoteBook.note_read_from_file)
    
    console_interface = ConsoleInterface()
    console_interface_note = ConsoleInterfaceNote()
     
    try:
        print(f"{bcolors.PINK}👋 Hello! My name is Bot Jul. Please choose the language and we will begin 🤖 {bcolors.RESET}")
        language = choose_language()
        exit_flag = False
        while True:
            user_input = wait_for_input()
            print(one_command_vizualization(user_input, available_commands(user_input)))
            match user_input:
                case "cli" | "команды" | "можливості":
                    print(available_commands())
                
                case "change language" | "изменить язык" | "зміти мову":
                    language = choose_language()

                case "contact add" | "добавление контакта" | "додати контакт":
                    # 'зберігає контакт з іменем, адресом, номером телефона, email та днем народження до книги контактів'
                    book.add_contacts()

                case "contact find" | "поиск контакта" | "пошук контакта":
                    # 'здійснює пошук контакту серед контактів книги'
                    console_interface.search_contact(book)

                case "contact show all" | "показать все контакты" | "показати всі контакти":
                    # "показує всі існуючі контакти в книзі контактів"
                    console_interface.show_all_contacts(book)

                case "contact phone add" | "добавить телефон" | "додати телефон":
                    # "додати іще 1-ин phone до існуючого контакту"
                    book.add_phone()

                case "contact phone remove" | "удалить телефон" | "видалити телефон":
                    # "видалення існуючого phone",
                    book.remove_phone()

                case "contact email add" | "добавить электронную почту" | "додати електронну пошту":
                    # "додати іще 1-ин email до існуючого контакту"
                    book.add_email()

                case "contact email remove" | "удалить электронную почту" | "видалити електронну пошту":
                    # "видалення існуючого email",
                    book.remove_email()

                case "contact phone edit" | "редактировать телефон" | "редагувати телефон":
                    # "редагування phone існуючого контакту"
                    book.edit_phone()

                case "contact email edit" | "редактировать электронную почту" | "редагувати електронну пошту":
                    # 'редагування email існуючого контакту'
                    book.edit_email()

                case "contact birthday edit" | "редактировать день рождения" | "редагувати день народження":
                    # 'редагування birthday існуючого контакту'
                    book.edit_birthday()

                case "contact remove" | "удалить контакт" | "видалити контакт":
                    # "видалення існуючого контакту"
                    book.del_contact()

                case "display birthdays" | "показать дни рождения" | "показати дні народження":
                    # "виводить список контактів, у яких день народження через задану кількість днів від поточної дати"
                    book.show_contacts_birthdays()

                case "note add" | "добавить заметку" | "додати нотатку":
                    # "зберігає нотатку за іменем автора",
                    note.add_new_note()

                case "note find" | "найти заметку" | "знайти нотатку":
                    # "здійснює пошук нотатки серед існуючих нотатків"
                    console_interface_note.find_author(note)

                case "note show all" | "показать все заметки" | "показати всі нотатки":
                    # "показує всі існуючі нотатки"
                    console_interface_note.note_show_all(note)

                case "note edit" | "редактировать заметку" | "редагувати нотатку":
                    # "редагування існуючої нотатки"
                    note.note_edit()

                case "note remove" | "удалить заметку" | "видалити нотатку":
                    # "видалення існуючої нотатки"
                    note.note_remove()

                case "tag add" | "добавить тег" | "додати тег":
                    #  "додавання тегів до існуючої нотатки"
                    note.tag_add()

                case "tag edit" | "редактировать тег" | "редагувати тег":
                    #  "редагування тегів існуючої нотатки"
                    note.tag_edit()

                case "tag remove" | "удалить теги из заметки" | "видалити тег":
                    #  "видалення тегів з існуючої нотатки"
                    note.tag_remove()

                case "tag find sort" | "найти и отсортировать по тегам" | "знайти та сортувати по тегам":
                    #  "пошук та сортування нотаток за тегами"
                    console_interface_note.tag_find_and_sort(note)

                case "file sort" | "сортировать файлы" | "відсортувати файли":
                    #  "сортування файлів у зазначеній папці за категоріями (зображення, документи, відео та ін.)."
                    executing_command(user_input.lower())
                
                case "file extension show" | "показать все разширения" | "показати всі розширення":
                    #  "сортування файлів у зазначеній папці за категоріями (зображення, документи, відео та ін.)."
                    executing_command(user_input.lower())

                case "file extension add" | "добавить расширение" | "додати розширення файла":
                    #  "додавання додатково розширення для сортування"
                    executing_command(user_input.lower())

                case "file extension remove" | "удалить расширение" | "видалити розширення файла":
                    #  "видалення розширення із списку для сортування"
                    executing_command(user_input.lower())

                case "quit" | "exit" | "q" | "выход" | "в" | "до зустрічі" | "д":
                    print(f"{bcolors.PINK}Good bye!{bcolors.RESET}\n")                   
                    save_to_file_contacts(file_name, book)
                    save_to_file_notes(note_name, note)
                    break
                
                case _:
                    if language == "ru":
                        commands_messages_error = RussianErrorCommandMessages()
                        error_messages_list = commands_messages_error.gets_error_command_messages()
                    elif language == "en":
                        commands_messages_error = EnglishErrorCommandMessages()
                        error_messages_list = commands_messages_error.gets_error_command_messages()
                    elif language == "ua":
                        commands_messages_error = UkrainianErrorCommandMessages()
                        error_messages_list = commands_messages_error.gets_error_command_messages()
                    
                    print(random.choice(error_messages_list))
                    if exit_flag:
                        timer_thread.cancel()
                        break
                            
    except FileNotFoundError:
        print(f"{bcolors.FAIL}\n❌ File not found error!{bcolors.RESET}")
        save_to_file_contacts(file_name, book)
        save_to_file_notes(note_name, note)
    except ValueError:
        print(f"{bcolors.FAIL}\n❌ Invalid value error!{bcolors.RESET}")
        save_to_file_contacts(file_name, book)
        save_to_file_notes(note_name, note)
    except KeyboardInterrupt:
        print(f"{bcolors.FAIL}\n❌ Keyboard interrupt error, EXITING!\n{bcolors.RESET}")
        save_to_file_contacts(file_name, book)
        save_to_file_notes(note_name, note)
    except Exception as ex:
        print(f"{bcolors.FAIL}\n❌ Unexpected error!{bcolors.RESET}")
        print(ex)
        save_to_file_contacts(file_name, book)
        save_to_file_notes(note_name, note)


if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    