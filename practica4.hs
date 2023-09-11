-- Ejercicio 1
fibonacci :: Integer -> Integer
fibonacci n
    | n == 0 = 0
    | n == 1 = 1
    | otherwise = fibonacci (n-1) + fibonacci (n-2)

-- Ejercicio 2

parteEntera :: Float -> Integer
parteEntera x
    | 0 <= x && x < 1= 0
    | x > -1 &&  x <= 0 = -1
    | x >= 1 = 1 + parteEntera(x-1)
    | otherwise = (-1) + parteEntera(x+1)

-- Ejercicio 3

esDivisible :: Integer -> Integer -> Bool
esDivisible _ 0 = False
esDivisible 0 _ = True
esDivisible x y 
    | x < y = False
    | otherwise = esDivisible (x-y) y

-- Ejercicio 4

sumaImpares :: Integer -> Integer
sumaImpares n = sumaImparesAux  n 1 -1

sumaImparesAux :: Integer -> Integer -> Integer
sumaImparesAux 0 _ = 0
sumaImparesAux n impar = impar + sumaImparesAux (n-1) (n+2)


-- Ejercicio 5

medioFact :: Integer -> Integer
medioFact 0 = 1
medioFact 1 = 1 
medioFact n = n * medioFact (n-2)

-- Ejercicio 6

sumaDigitos :: Integer -> Integer
sumaDigitos n
    | n < 10 = n
    | otherwise = ultimoDigito n + sumaDigitos (sacarUltimoDigito n)

-- Ejercicio 7

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales x
    | x < 10 = True
    | otherwise  = (ultimoDigito x == ultimoDigito (sacarUltimoDigito x))  
    

ultimoDigito :: Integer -> Integer
ultimoDigito x = mod x 10

sacarUltimoDigito :: Integer -> Integer
sacarUltimoDigito x = div x 10
-- Ejercicio 13 ^^^
{-
sumatoriaDoble ::  Integer -> Integer -> Integer
sumatoriaDoble _ 0 = 0
sumatoriaDoble n j = n^2 + sumatoriaDoble n(m-1)
-}

sumaBaseFija :: Integer -> Integer -> Integer
sumaBaseFija b 1 = b
sumaBaseFija b e = sumaBaseFija b (e-1) + b ^ e

sumarPotencias :: Integer -> Integer -> Integer
sumarPotencias 1 m = sumaBaseFija 1 m
sumarPotencias n m = sumaBaseFija n m + sumarPotencias (n-1) m


-- Ejercicio 16

menorDivisor :: Integer -> Integer
menorDivisor 
    | x < 1 = True
    | otherwise = 
