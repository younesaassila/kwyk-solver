@echo off
chcp 65001
title Installation des modules requis au fonctionnement de Kwyk Solver...
py --version | find "Python 3.9"
if %ERRORLEVEL% equ 0 (
  cls
  echo Erreur : Kwyk Solver ne supporte actuellement pas Python 3.9
) else (
  cls
  echo » Mise à jour de pip
  py -m pip install --upgrade pip
  echo » Installation de numpy
  py -m pip install numpy
  echo » Installation de requests
  py -m pip install requests
  echo » Installation de scipy
  py -m pip install scipy
  echo » Programme d'installation des modules requis terminé. Si une erreur est survenue, merci de la signaler en créant un rapport de bug à l'adresse : https://github.com/younesaassila/Kwyk-Solver/issues
)
pause
