# noinspection PyProtectedMember,PyMethodMayBeStatic
class AcademyRouter:
    app_labels = {'faculties'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.app_labels:
            return 'academy'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.app_labels:
            return 'academy'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.app_labels:
            return db == 'academy'
        return None
