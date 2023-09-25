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
esDivisible x y
    | y == 0 = False
    | x < y = False
    | x == y = True
    | otherwise = esDivisible (x - y) y

-- Ejercicio 4

sumaImpares :: Integer -> Integer
sumaImpares 0 = 0
sumaImpares x = (2*x-1) + sumaImpares (x-1)

-- Ejercicio 5



-- Ejercicio 7

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales x
    | x < 10 = True
    | otherwise  = ultimoDigito x == ultimoDigito (sacarUltimoDigito x)
    

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
menorDivisor x = menorDivisorHasta x 2

menorDivisorHasta :: Integer -> Integer -> Integer
menorDivisorHasta x d | x == d = x
    | mod x d == 0 = d
    | otherwise = menorDivisorHasta x (d+1)

-- Ejercicio 19

esPrimo :: Integer -> Bool
esPrimo x = menorDivisor x == x

proximoPrimo :: Integer -> Integer
proximoPrimo x | esPrimo x = x
    | otherwise = proximoPrimo (x+1) 


esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos n = esSumaPrimerosKPrimos n 1

esSumaPrimerosKPrimos :: Integer -> Integer -> Bool
esSumaPrimerosKPrimos n k | n == sumaPrimerosKPrimos k = True
    | n < sumaPrimerosKPrimos k = False
    | otherwise = esSumaPrimerosKPrimos n (k+1)

sumaPrimerosKPrimos :: Integer -> Integer
sumaPrimerosKPrimos 1 = 2
sumaPrimerosKPrimos k = sumaPrimerosKPrimos (k-1) + kEsimoPrimo k

kEsimoPrimo :: Integer -> Integer
kEsimoPrimo 1 = 2
kEsimoPrimo k = proximoPrimo (kEsimoPrimo (k-1) +1)