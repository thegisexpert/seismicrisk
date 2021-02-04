
import subprocess
cmd = "xcopy 'D:\repositorydef\SeismicRisk' 'C:\Users\AG\.qgis2\python\plugins\SeismicRisk' /S"

subprocess.run(cmd, shell=True)

rmdir /S "C:\Users\AG\.qgis2\python\plugins\SeismicRisk"
xcopy "D:\repositorydef\SeismicRisk" "C:\Users\AG\.qgis2\python\plugins\SeismicRisk" /S