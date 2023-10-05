from abc import ABC, abstractmethod


class IModelChangeObserver(ABC):
    @abstractmethod
    def ApplyUpdateModel(self):
        pass


class IModelChanger(ABC):
    @abstractmethod
    def NotifyChange(self):
        pass


class ModelStore(IModelChangeObserver, IModelChanger):
    def __init__(self):
        self.Models = []
        self.Scenes = []
        self.Flashes = []
        self.Cameras = []

    def getScene(self, n_scene):
        return self.Scenes[n_scene]

    def NotifyChange(self):
        pass

    def ApplyUpdateModel(self):
        pass


class Angle3D:
    pass


class Camera:
    def __init__(self):
        self.location = None
        self.angle = None

    def Rotate(self, grad):
        pass

    def Move(self, cm):
        pass


class Color:
    pass


class Flash:
    def __init__(self):
        self.location = None
        self.angle = None
        self.color = None
        self.power = None

    def Rotate(self, grad):
        pass

    def Move(self, cm):
        pass


class Point3D:
    pass


class Poligon:
    def __init__(self):
        self.points = []


class PoligonalModel:
    def __init__(self):
        self.poligons = []
        self.textures = []


class Scene:
    def __init__(self):
        self.id = None
        self.models = []
        self.flashes = []

    def method1(self, in1):
        return in1

    def method2(self, in1, in2):
        ret = object()
        return ret


class Texture:
    pass
