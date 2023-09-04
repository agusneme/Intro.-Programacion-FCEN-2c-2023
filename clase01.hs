doubleMe :: Num a => a -> a
doubleMe x = x+ x
--Ejercicio 1--
-- A
f :: Int -> Int
f n
    | n == 1 = 8
    | n == 4 = 131
    | n == 16 = 16
-- B
g :: Int -> Int
g n
    | n == 8 = 16 
    | n == 16 = 4
    | n == 131 = 1
-- C
h :: Int -> Int
h x = f(g x)
k :: Int -> Int
k x = g(f x)

--Ejercicio 2--
-- A
valorAbsoluto :: Int -> Int 
valorAbsoluto = abs

--B
maximoabsoluto :: Int -> Int -> Int
maximoabsoluto x y
    | abs x > abs y = abs x
    | otherwise = abs y

-- C
maximo3 :: Int -> Int -> Int -> Int
maximo3 x y z
    | x >= y && x >= z = x
    | y >= x && y >= z = y
    | z >= x && z >= y = z

-- D
algunoEs0 :: Rational -> Rational -> Bool
algunoEs0 x y
    | x == 0 || y == 0 = True
    | otherwise = False

-- E
ambosSon0 :: Rational -> Rational -> Bool
ambosSon0 x y
    | x == 0 && y == 0 = True
    | otherwise = False

-- F ????????????????


-- G
sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z
    | x /= y && x /= z &&  y /= z = x + y + z
    | x == y && x /= z &&  y /= z = z
    | x /= y && x == z &&  y /= z = y
    | x /= y && x /= z &&  y == z = x

-- H
esMultiploDe:: Int -> Int -> Bool
esMultiploDe x y
    | x `mod` y == 0 = True
    | otherwise = False 

-- I
digitoUnidades :: Int -> Int
digitoUnidades x = mod x 10

--J
digitoDecenas :: Int -> Int
digitoDecenas x = digitoUnidades(div x 10)

-- Ejercicio 3 --

estanRelacionados :: Int -> Int -> Bool
estanRelacionados a b
    | a == 0 || b == 0 = False
    | a * a + a* b * k == 0 = True
    | otherwise = False
    where k = -a `div` b

-- Ejercicio 4 --

--A
prodInt :: (Integer,Integer) -> (Integer,Integer) -> Integer
prodInt (a,b) (c,d) = a*c + b*d 
--Pregunta como puedo hacer para que valga para R3--

--B
todoMenor ::  (Integer,Integer) -> (Integer,Integer) -> Bool
todoMenor (a,b) (c,d) = a < c && b < d

--C
distanciaPuntos :: Floating a => (a, a) -> (a, a) -> a
distanciaPuntos (a,b) (c,d) = sqrt((c-a)^2 + (d-b)^2)

--D
sumaTerna :: Num a => (a, a, a) -> a
sumaTerna (a,b,c) = a+b+c

--E

--F

posPrimerPar (a,b,c)
    | even a = 1
    | even b = 2
    | even c = 3
    | otherwise = 4


-- Ejercicio 5 --

todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (n1, n2, n3) = (funcion n1 > funciong n1) && (funcion n2 > funciong n2) && (funcion n3 > funciong n3)

funcion :: Integer -> Integer
funcion n
    | n <= 7 = n ^ 2
    | n > 7 = 2* n - 1

funciong :: Integer -> Integer
funciong g
    | even g = g `div` 2
    | otherwise = 3 * g + 1

-- Ejercicio 6 --

bisiesto :: Int -> Bool
bisiesto a
    | (a `mod` 4 /= 0) || ((a `mod` 100 == 0) &&  (a `mod` 400 /= 0)) = False
    | otherwise = True

-- Ejercicio 7 --


-- Ejercicio 8 --

comparar :: Int -> Int -> Int
comparar a b
    | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
    | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
    | otherwise = 0

sumaUltimosDosDigitos :: Int -> Int
sumaUltimosDosDigitos x = (x `mod` 10) + (x `div` 10 `mod` 10)


-- Ejercicio 9 --
{-- 
a) En la f1 se recibe un numero en coma flotante (Float), se utilizan guardas para evaluar el valor de este. Si 'n' es igual a 0 devuelve 1 en otro caso devuelve 0

b) En la f2 se recibe un numero en coma flotante (Float), se utilizan guardas para evaluar el valor de este. Si 'n' es igual a 1 devuelve 15, si es igual a -1 devuelve -15

c) En la f3 se recibe un numero en coma flotante (Float), se utilizan guardas para evaluar el valor de este. Si 'n' es menor o igual a 9 devuelve 7, si es mayor o igual a 3 devuelve 5

d) En la f4 se reciben dos numeros en coma flotante (Float), toma ambos valores y los suma para luego dividirlo entre 2. Calcula el promedio entre dos numeros de coma flotante.

e) En la f5 se recibe una argumento de tipo tupla, donde la tupla tiene dos elementos 'x' e 'y', ambos de tipo 'Float'. Esta funcion calcula el promedio entre ambos elementos de la tupla.

f) En la f6 se recibe un numero en coma flotante (Float) y un entero (Integer). Trunca el valor del numero de coma flotante para luego compararlo con el segundo valor, si son iguales retorna True. 
--}