from src.View.GUI import WStarting, WChooseFiles, WLoadImage


def StartingW2Component(self):
    pass


def StartingW2Watch(self):
    pass


def StartingW2Load(self):
    self.close()
    WChooseFiles()
    pass


def LoadW2LoadPLY(self):
    pass


def LoadPLY2Open3D(self):
    pass


def LoadW2LoadPNGs(self):
    pass


def LoadPNGs2Open3D(self):
    pass


def LoadPNGs2Load(self):
    pass


WStarting.toComponent = StartingW2Component
WStarting.toWatch = StartingW2Watch
WStarting.toLoad = StartingW2Load
WLoadImage.toChoose = LoadW2LoadPNGs

if __name__ == '__main__':
    window = WStarting()
