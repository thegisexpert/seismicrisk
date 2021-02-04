
def getPathScripts():
    #return "C:/Data/Python/"
    # return ""


        

    '''
    
    :return: 
    from Database.SQL import sql

    path = sql.getWorkingDir()

    print " working dir is "
    print path
    '''

    import inspect

    # sqldir = inspect.getfile(SeismicRiskDockWidget.__class__)

    import os
    path = os.path.dirname(__file__)

    path = path.replace("\\", "/")

    print " path in directory " + path

    return path


def getPathSqlDir():
    # return "C:/Data/Python/"
    # return ""




    '''

    :return: 
    from Database.SQL import sql

    path = sql.getWorkingDir()

    print " working dir is "
    print path
    '''

    import inspect

    # sqldir = inspect.getfile(SeismicRiskDockWidget.__class__)

    import os
    path = os.path.dirname(__file__)

    path = path.replace("\\", "/")

    print " Utils 61 " + path

    path = path.replace("Logic2/Utils", "Database/SQL")

    print " path in directory " + path

    path = path + "/"

    return path


def getPathTempDir():
    # return "C:/Data/Python/"
    # return ""




    '''

    :return: 
    from Database.SQL import sql

    path = sql.getWorkingDir()

    print " working dir is "
    print path
    '''

    import inspect

    # sqldir = inspect.getfile(SeismicRiskDockWidget.__class__)

    import os
    path = os.path.dirname(__file__)

    path = path.replace("\\", "/")

    path = path.replace("Logic2/Utils/", "Database/temp")
    path = path + "/"

    print " path in directory " + path

    return path

