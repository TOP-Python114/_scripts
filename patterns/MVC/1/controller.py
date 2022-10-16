"""Компонент Контроллер (MVC) — управляющий модуль."""

# import view_cli as view
import view_gui as view
import model


def start():
    view.start_view()
    answer = view.ask_if_show_all()
    answer_check(answer)


def answer_check(answer: str) -> None:
    if answer in ('y', 'д'):
        show_all()
    else:
        end()


def show_all():
    people = model.Person.get_all()
    view.show_all_view(people)
    end()


def end():
    view.end_view()


if __name__ == '__main__':
    start()
