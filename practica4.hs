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


-- Ejercicio 7

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales x
    | x < 10 = True
    | otherwise  = (ultimoDigito x == ultimoDigito (sacarUltimoDigito x))  
    

ultimoDigito :: Integer -> Integer
ultimoDigito x = mod x 10

sacarUltimoDigito :: Integer -> Integer
sacarUltimoDigito x = div x 10


