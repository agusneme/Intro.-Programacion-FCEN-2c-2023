absoluto :: Int -> Int
absoluto = abs


absolutoMax :: Int -> Int -> Int
absolutoMax x y 
    | abs x > abs y = abs x
    | otherwise = abs y

maximo3 :: Int -> Int -> Int -> Int
maximo3 x y z
    | x >= y && x >= z = x
    | y >= x && y >= z = y
    | otherwise = z

algunoEs0 :: Rational -> Rational -> Bool
algunoEs0 x y
    | x == 0 || y == 0 = True
    | otherwise = False 

ambosSon0 :: Rational -> Rational -> Bool
ambosSon0 x y
    | x == 0 && y == 0 = True
    | otherwise = False 

prodInt :: (Int,Int) -> (Int,Int) ->  Bool
prodInt x y
    | fst x < fst y && snd x < snd y = True
    | otherwise = False


fibonaci :: Int -> Int
fibonaci x
    | x == 0 = 0
    | x == 1 = 1
    | otherwise = fibonaci (x-1) + fibonaci (x-2)

sumaImpares :: Int -> Int
sumaImpares 0 = 0
sumaImpares x = (2*x-1) + sumaImpares (x-1)






relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((x,y):xs)
    | x == y = False
    | pertenece (x,y) xs = False
    | pertenece (y,x) xs = False
    | otherwise = relacionesValidas xs


pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y:ys) 
    | x == y = True
    | otherwise = pertenece x ys


--Ejercicio 1
votosEnBlanco :: [(String,String)] -> [Int] -> Int -> Int
votosEnBlanco  [] votos totalVotos = totalVotos - (votosAfirmativos votos)

votosAfirmativos :: [Int] -> Int
votosAfirmativos [] = 0
votosAfirmativos (v:vs) = v + votosAfirmativos vs

--Ejercicio 2
formulasValidas :: [(String, String)] -> Bool
formulasValidas [] = True
formulasValidas (f:fs) = fst f /= snd f && not (estaEnFormulas(fst f) fs) && not (estaEnFormulas(snd f) fs) && (formulasValidas fs)

estaEnFormulas :: String -> [(String,String)] -> Bool
estaEnFormulas  _ [] = False
estaEnFormulas c (f:fs) = c == (fst f) || c == (snd f) || estaEnFormulas c fs

--Ejercicio 3

division :: Int -> Int -> Float 
division a b = (fromIntegral a) / (fromIntegral b)

porcentajeDeVotos :: String -> [(String,String)] -> [Int] -> Float
porcentajeDeVotos presi fs votos = division (contarVotos presi fs votos)  (votosAfirmativos votos)

contarVotos :: String -> [(String,String)] -> [Int] -> Int
contarVotos presi [f] [v] = v
contarVotos presi (f:fs) (v:vs)
    | presi == fst f = v
    | otherwise = contarVotos presi fs vs

--Ejercicio 4

proximoPresidente :: [(String,String)] -> [Int] -> String
proximoPresidente [(presi,_)] _ = presi
proximoPresidente (f1:f2:fs) (v1:v2:vs) 
    | v1 > v2 = proximoPresidente (f1:fs) (v1:vs)
    | otherwise = proximoPresidente (f2:fs) (v2:vs)

removeDuplicates :: Eq a => [a] -> [a]
removeDuplicates [] = []
removeDuplicates  (x:xs) = x : removeDuplicates (removeAllOccurrences x xs)

removeAllOccurrences :: Eq a => a -> [a] -> [a]
removeAllOccurrences _ [] = []
removeAllOccurrences y (z:zs)
    | y == z = removeAllOccurrences y zs
    | otherwise = z : removeAllOccurrences y zs