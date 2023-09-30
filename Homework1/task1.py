class IModelChangeObserver:
    def ApplyUpdateModel(self):
        pass


class IModelChanger:
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
        # реализация метода
        pass

    def ApplyUpdateModel(self):
        # реализация метода
        pass


class Angle3D:
    # добавить необходимые атрибуты и методы
    pass


class Camera:
    def __init__(self):
        self.location = None
        self.angle = None

    def Rotate(self, grad):
        # реализация метода
        pass

    def Move(self, cm):
        # реализация метода
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
        # реализация метода
        pass

    def Move(self, cm):
        # реализация метода
        pass


class Point3D:
    def __init__(self):
        self.x = None
        self.y = None
        self.z = None

    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    def setZ(self, z):
        self.z = z

    def getZ(self):
        return self.z


class Polygon:
    def __init__(self):
        self.points = []


class PolygonalModel:
    def __init__(self):
        self.polygons = []
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
