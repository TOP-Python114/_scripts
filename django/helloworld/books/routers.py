# noinspection PyProtectedMember, PyMethodMayBeStatic
class BooksRouter:
    app_labels = {'books'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.app_labels:
            return 'books_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.app_labels:
            return 'books_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.app_labels:
            return db == 'books_db'
        return None

