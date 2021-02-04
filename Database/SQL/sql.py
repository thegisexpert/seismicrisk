
def getWorkingDir():
    import inspect

    # sqldir = inspect.getfile(SeismicRiskDockWidget.__class__)

    import os
    path = os.path.dirname(__file__)



    return path