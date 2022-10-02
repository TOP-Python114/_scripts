"""Демонстратор наблюдателя: базовая реализация."""

class Camera:
    """Камера наблюдения. (Наблюдатель)"""
    id_ = 0

    def __init__(self, name: str):
        self.id = self.__class__.id_
        self.__class__.id_ += 1
        self.name = name

    def make_photo(self):
        """Реакция наблюдателя на событие."""
        print(f'фото с камеры {self.name}')

    def __hash__(self):
        return self.id


class CameraSystem:
    """Пост управления камерами. (Субъект наблюдения)"""
    def __init__(self):
        self.cameras: set[Camera] = set()

    def connect(self, camera: Camera):
        """Подключает камеру к посту. (Подписка экземпляра наблюдателя)"""
        self.cameras.add(camera)

    def disconnect(self, camera: Camera):
        """Отключает камеру от поста. (Отмена подписки экземпляра наблюдателя)"""
        self.cameras.remove(camera)

    def notify(self):
        """Отправляет сигнал всем камерам (наблюдателям)."""
        for camera in self.cameras:
            camera.make_photo()


subject = CameraSystem()

camera1 = Camera('Северо-Восток')
camera2 = Camera('Северо-Запад')
camera3 = Camera('Восток')

subject.connect(camera1)
subject.connect(camera2)
subject.connect(camera3)

# происходит событие — кто-то звонит в дверь
subject.notify()

subject.disconnect(camera2)

# происходит событие — кто-то звонит в дверь
subject.notify()
