"""Компонент Контроллер (MVC) — управляющий модуль."""

import view_cli
import model


def start():
    view_cli.start_view()
    answer = view_cli.ask_if_show_all()
    if answer in ('y', 'д'):
        show_all()
    else:
        end()


def show_all():
    people = model.Person.get_all()
    view_cli.show_all_view(people)
    end()


def end():
    view_cli.end_view()


if __name__ == '__main__':
    start()
