@echo off
chcp 65001
title Installation des modules requis au fonctionnement de Kwyk Solver...
cls
echo » Mise à jour de pip
py -m pip install --upgrade pip
echo » Installation de numpy
py -m pip install numpy
echo » Installation de requests
py -m pip install requests
echo » Installation de scipy
py -m pip install scipy
echo » Programme d'installation des modules requis terminé.
pause
