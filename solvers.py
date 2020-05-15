import numpy as np
from fractions import Fraction

# Solveur des exercices 28036 et 28037
def solver_28036_28037():
  print("Veuillez renseigner les coefficients de l'équation paramétrique donnée ax + by + cz + d = 0 :")
  a, b, c, d = int(input("a = ")), int(input("b = ")), int(input("c = ")), int(input("d = "))
  print("Veuillez renseigner les coordonnées du point A :")
  Ax, Ay, Az = int(input("Ax = ")), int(input("Ay = ")), int(input("Az = "))
  print("Veuillez renseigner les coordonnées du point B :")
  Bx, By, Bz = int(input("Bx = ")), int(input("By = ")), int(input("Bz = "))

  # Calcul des coordonnées du vecteur AB
  ABx = Bx - Ax
  ABy = By - Ay
  ABz = Bz - Az

  # Calcul du produit scalaire entre le vecteur normal au plan et le vecteur AB
  scalar_product = a * ABx + b * ABy + c * ABz

  # Vérifions si les points de la droite sont tous les deux inclus dans le plan
  is_a_in_plane = a * Ax + b * Ay + c * Az + d == 0
  is_b_in_plane = a * Bx + b * By + c * Bz + d == 0
  if (is_a_in_plane and is_b_in_plane):
    print("(AB) est incluse dans le plan")
  else:
    # Vérification du parallélisme de (AB) au plan
    if (scalar_product == 0):
      print("(AB) est parallèle au plan")
    else:
      # La droite (AB) est sécante au plan
      print("(AB) est sécante au plan")
      # Calculons le point d'intersection
      dividend = ((-a * Ax) + (-b * Ay) + (-c * Az) + (-d))
      divisor = ((a * ABx) + (b * ABy) + (c * ABz))
      t = dividend / divisor
      inter_x = ABx * t + Ax
      inter_y = ABy * t + Ay
      inter_z = ABz * t + Az
      print(f"Le point d'intersection du plan et de la droite (AB) est M({Fraction(inter_x).limit_denominator()}; {Fraction(inter_y).limit_denominator()}; {Fraction(inter_z).limit_denominator()})")
      # Vérifions si (AB) et le plan sont orthogonaux
      if (ABx == 0 or ABy == 0 or ABz == 0):
        print("(AB) et le plan NE sont PAS orthogonaux")
      else:
        coeff_x = a / ABx
        coeff_y = b / ABy
        coeff_z = c / ABz
        if (coeff_x == coeff_y == coeff_z):
          print("(AB) et le plan sont orthogonaux")
        else:
          print("(AB) et le plan NE sont PAS orthogonaux")

# Solveur de l'exercice 20118
def solver_20118():
  print("Veuillez renseigner les coordonnées du point A :")
  Ax, Ay, Az = int(input("Ax = ")), int(input("Ay = ")), int(input("Az = "))
  print("Veuillez renseigner les coordonnées du vecteur normal →(n) :")
  a, b, c = int(input("Nx = ")), int(input("Ny = ")), int(input("Nz = "))
  d = - (a * Ax) - (b * Ay) - (c * Az)
  print(f"Une équation cartésienne de P est {Fraction(a).limit_denominator()} x + {Fraction(b).limit_denominator()} y + {Fraction(c).limit_denominator()} z + {Fraction(d).limit_denominator()} = 0")

# Solveur de l'exercice 20119
def solver_20119():
  print("Veuillez renseigner les coordonnées du point A :")
  Ax, Ay, Az = int(input("Ax = ")), int(input("Ay = ")), int(input("Az = "))
  print("Veuillez renseigner les coordonnées du point B :")
  Bx, By, Bz = int(input("Bx = ")), int(input("By = ")), int(input("Bz = "))
  print("Veuillez renseigner les coordonnées du point C :")
  Cx, Cy, Cz = int(input("Cx = ")), int(input("Cy = ")), int(input("Cz = "))
  ABx = Bx - Ax
  ABy = By - Ay
  ABz = Bz - Az
  ACx = Cx - Ax
  ACy = Cy - Ay
  ACz = Cz - Az
  # Produit vectoriel →(AB) * →(AC)
  a = (ABy * ACz) - (ACy * ABz)
  b = (ABz * ACx) - (ACz * ABx)
  c = (ABx * ACy) - (ACx * ABy)
  d = - (a * Ax) - (b * Ay) - (c * Az)
  print(f"Une équation cartésienne de P est {Fraction(a).limit_denominator()} x + {Fraction(b).limit_denominator()} y + {Fraction(c).limit_denominator()} z + {Fraction(d).limit_denominator()} = 0")

# Solveur de l'exercice 20128
def solver_20128():
  print("Veuillez renseigner les coefficients pour chacune des coordonnées de l'équation paramétrique de la droite D :")
  Dxt, Dyt, Dzt = int(input("x : �t = ")), int(input("y : �t = ")), int(input("z : �t = "))
  print("Veuillez renseigner les constantes pour chacune des coordonnées de l'équation paramétrique de la droite D :")
  Dx, Dy, Dz = int(input(f"x : {Dxt}t + � = ")), int(input(f"y : {Dyt}t + � = ")), int(input(f"z : {Dzt}t + � = "))
  print("Veuillez renseigner les coefficients pour chacune des coordonnées de l'équation paramétrique de la droite D' :")
  D_xt, D_yt, D_zt = int(input("x : �t = ")), int(input("y : �t = ")), int(input("z : �t = "))
  print("Veuillez renseigner les constantes pour chacune des coordonnées de l'équation paramétrique de la droite D' :")
  D_x, D_y, D_z = int(input(f"x : {D_xt}t + � = ")), int(input(f"y : {D_yt}t + � = ")), int(input(f"z : {D_zt}t + � = "))
  a = np.array([ [Dxt, -D_xt], [Dyt - Dzt, -D_yt - (-D_zt)] ])
  b = np.array([ (D_x - Dx), ((D_y - Dy) - (D_z - Dz)) ])
  t1 = np.linalg.solve(a, b)[0]
  x = Dxt * t1 + Dx
  y = Dyt * t1 + Dy
  z = Dzt * t1 + Dz
  print(f"Le point d'intersection des deux droites est M({Fraction(x).limit_denominator()}; {Fraction(y).limit_denominator()}; {Fraction(z).limit_denominator()})")

# Solveur pour l'exercice 20129
def solver_20129():
  print("Veuillez renseigner les coordonnées du point A :")
  ax, ay, az = int(input("Ax = ")), int(input("Ay = ")), int(input("Az = "))
  print("Veuillez renseigner les coordonnées du point B :")
  bx, by, bz = int(input("Bx = ")), int(input("By = ")), int(input("Bz = "))
  print("Veuillez renseigner les coordonnées du point C :")
  cx, cy, cz = int(input("Cx = ")), int(input("Cy = ")), int(input("Cz = "))
  print("Veuillez renseigner les coordonnées du point D :")
  dx, dy, dz = int(input("Dx = ")), int(input("Dy = ")), int(input("Dz = "))
  ABx, ABy, ABz = bx - ax, by - ay, bz - az
  CDx, CDy, CDz = dx - cx, dy - cy, dz - cz
  Dxt, Dyt, Dzt = ABx, ABy, ABz
  Dx, Dy, Dz = ax, ay, az
  D_xt, D_yt, D_zt = CDx, CDy, CDz
  D_x, D_y, D_z = cx, cy, cz
  a = np.array([ [Dxt, -D_xt], [Dyt - Dzt, -D_yt - (-D_zt)] ])
  b = np.array([ (D_x - Dx), ((D_y - Dy) - (D_z - Dz)) ])
  t1 = np.linalg.solve(a, b)[0]
  x = Dxt * t1 + Dx
  y = Dyt * t1 + Dy
  z = Dzt * t1 + Dz
  print(f"Le point d'intersection des deux droites est M({Fraction(x).limit_denominator()}; {Fraction(y).limit_denominator()}; {Fraction(z).limit_denominator()})")

# Solveur de l'exercice 20110
def solver_20110():
  print("Veuillez renseigner les coordonnées du point M :")
  Mx, My, Mz = int(input("Mx = ")), int(input("My = ")), int(input("Mz = "))
  print("Veuillez renseigner les coefficients pour chacune des coordonnées de l'équation paramétrique de la droite (d) :")
  Dxt, Dyt, Dzt = int(input("x : �t = ")), int(input("y : �t = ")), int(input("z : �t = "))
  location = input("Où se situe l'inconnue ? x, y ou z : ")
  print("Veuillez renseigner les constantes connues pour chacune des coordonnées de l'équation paramétrique de la droite (d) :")
  Dx, Dy, Dz, t = 0, 0, 0, 0
  missing_constant = 0
  if (location == "x"):
    Dy = int(input(f"y : {Dyt}t + � = "))
    Dz = int(input(f"z : {Dzt}t + � = "))
    t = (My - Dy) / Dyt
    missing_constant = -Dxt * t + Mx
  elif (location == "y"):
    Dx = int(input(f"x : {Dxt}t + � = "))
    Dz = int(input(f"z : {Dzt}t + � = "))
    t = (Mz - Dz) / Dzt
    missing_constant = -Dyt * t + My
  elif (location == "z"):
    Dx = int(input(f"x : {Dxt}t + � = "))
    Dy = int(input(f"y : {Dyt}t + � = "))
    t = (Mx - Dx) / Dxt
    missing_constant = -Dzt * t + Mz
  print(f"La constante inconnue en {location} doit être égale à {Fraction(missing_constant).limit_denominator()}")

