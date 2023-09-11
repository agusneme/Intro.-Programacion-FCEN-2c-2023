 -- Ejercicio 1 
longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

-- Ejercicio 4

hayRepetidos :: Eq t => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) = elem x xs || hayRepetidos xs
