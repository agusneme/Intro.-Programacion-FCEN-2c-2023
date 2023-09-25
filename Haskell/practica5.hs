 -- Ejercicio 1.1 
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use foldl" #-}

longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

--Ejercicio 1.2

ultimo :: [t] -> t
ultimo x 
        | not (null x) = last x

--Ejercicio 1.3

principio :: [t] ->[t]
principio s
    | null s = []
    | length s == 1 = []
    | otherwise = head s : principio(tail s)

-- Ejercicio 1.4

reverso :: [t] -> [t]
reverso s = reversoAux s []

reversoAux :: [t] -> [t] -> [t]
reversoAux [] acc = acc
reversoAux (x:xs) acc = reversoAux xs (x:acc)


--Ejercicio 2

--Ejercicio 2.1

pertenece ::  (Eq t) => t -> [t] -> Bool 
pertenece _ [] = False
pertenece e (x:xs)
    | e == x = True
    | otherwise = pertenece  e xs

-- Ejercicio 2.2

todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [x] = True
todosIguales (x:y:xs)
    | x == y    = todosIguales (y:xs)
    | otherwise = False

-- Ejercicio 2.3

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:xs) = notElem x xs && todosDistintos xs
    
-- Ejercicio 2.4
hayRepetidos :: Eq t => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) = elem x xs || hayRepetidos xs

-- Ejercicio 2.5
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar y (z:zs)
        | y == z = quitar y zs
        |otherwise = z : quitar y zs

-- Ejercicio 2.6

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos x (y:ys)
    | x == y    = quitarTodos x ys
    | otherwise = y : quitarTodos x ys

-- Ejercicio 2.7


eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos xs = eliminarRepetidosAux xs []

eliminarRepetidosAux :: (Eq t) => [t] -> [t] -> [t]
eliminarRepetidosAux [] _ = []
eliminarRepetidosAux (x:xs) acc
    | x `elem` acc = eliminarRepetidosAux xs acc
    | otherwise   = x : eliminarRepetidosAux xs (x:acc)

-- Ejercicio 2.8

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos s r = sinRepetir s == sinRepetir r

sinRepetir :: (Eq t) => [t] -> [t]
sinRepetir [] = []
sinRepetir (x:xs)
    | x `elem` xs  = sinRepetir xs
    | otherwise = x : sinRepetir xs


-- Ejercicio 3
-- 3.3
{-
maximo :: Ord t => [t] -> t
maximo (x:xs) = maximum (x:xs) 
-}

maximo :: [Int] -> Int
maximo [x] = x
maximo (x:y:xs)  | x > y = maximo (x:xs)
    | otherwise = maximo (y:xs)


-- 3.9
ordenar :: [Int] -> [Int]
ordenar [] = []
ordenar (x:xs) = minimo xs : ordenar (quitar (minimo xs) xs) 

quitar2 :: Int -> [Int] -> [Int]
quitar2 e (x:xs) | e /= x = x : quitar e xs
    | otherwise = xs

minimo :: [Int] -> Int
minimo [x] = x
minimo (x:y:xs)  | x < y = minimo (x:xs)
    | otherwise = minimo (y:xs)