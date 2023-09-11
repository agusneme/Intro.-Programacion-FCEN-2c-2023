import Distribution.Simple.Utils (xargs)
 -- Ejercicio 1 
longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

-- Ejercicio 3 
-- 3
{-
maximo :: Ord t => [t] -> t
maximo (x:xs) = maximum (x:xs) 
-}

maximo :: [Int] -> Int
maximo [x] = x
maximo (x:y:xs)  | x > y = maximo (x:xs)
    | otherwise = maximo (y:xs)

-- Ejercicio 4
hayRepetidos :: Eq t => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) = elem x xs || hayRepetidos xs

