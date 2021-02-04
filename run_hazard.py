
if __name__ == "__main__":
    import sys

    sys.path

    sys.path.append('D:/repositorydef/SeismicRisk/Logic/HazardModel')

    from Logic.HazardModel import Hazard

    Hazard.createEpicenter("7", "8.9", "8.7", "1", "2", "1")
