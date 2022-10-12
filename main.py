"""Speech rec."""
import os
import random
import speech_recognition


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.8

commands_dict = {
    "commands": {
        "greeting": ["раз", "привет", "приветствую"],
        "create_task": ["добавить задачу", "создать задачу", "заметка"],
        "play_music": ["включи музыку", "дискотека"]
    }
}


def listen_command():
    """listen to mic."""

    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language="ru-RU").lower()

        return query
    except speech_recognition.UnknownValueError:
        return "Unknown command"


def greeting():
    """Hello func."""
    return "Привет нищеброд!"


def create_task():
    print("Что добавим в список дел?")

    query = listen_command()

    with open("todo-list.txt", "a") as file: 
        file.write(f"{query}\n")

        return f"Задача {query} добавлена в список дел!"


def play_music():
    """play music"""
    files = os.listdir("Music")
    random_file = f"Music/{random.choice(files)}"
    os.system(f"xdg-open{random_file}")

    return f"Танцуем под {random_file}"


def main():
    query = listen_command()

    for k, v in commands_dict["commands"].items():
        if query in v:
            print(globals()[k]())


if __name__ == "__main__":
    main()
