module Solucion  where
-- dc_YeNtO

{-
problema relacionesValidas (relaciones: seq⟨String × String⟩) : Bool {
requiere: {True}
asegura: {(res = true) ↔ no hay tuplas en relaciones con ambas componentes 
iguales ni tuplas repetidas (sin considerar el orden)}
-}

relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((x,y):xs) = notElem (x,y) xs && notElem (y,x) xs && relacionesValidas xs
 
{-
problema personas(relaciones: seq(String x String) : seq(String)
    requiere: [relacionesValidas(relaciones)]
    asegura: { resu tiene exactamente los elementos que figuran 
    en alguna tupla de relaciones en cualquiera 
    de las dos posiciones, sin repetir}
-}

sacarDuplicados :: [String] -> [String]
sacarDuplicados []  = []
sacarDuplicados (x:xs) = x : sacarDuplicados (quitar x xs)
    where 
        quitar _ [] = []
        quitar y (z:zs)
            |y == z = quitar y zs
            |otherwise = z : quitar y zs
        
crearListaRelaciones :: [(String, String)] -> [String]
crearListaRelaciones [] = []
crearListaRelaciones ((x,y):xs) = x : y : crearListaRelaciones xs

personas :: [(String,String)] -> [String]
personas relaciones = sacarDuplicados (crearListaRelaciones relaciones)

{-
problema amigosDe (persona: String, relaciones: seq⟨String × String⟩) : seq⟨String⟩ {
requiere: {relacionesV alidas(relaciones)}
asegura: {resu tiene exactamente los elementos que figuran en alguna tupla de relaciones en las que alguna de las
componentes es persona}
amigosDe :: String -> [(String, String)] -> [String]
amigosDe 
-}

amigosDe :: String -> [(String,String)] -> [String]
amigosDe _ [] = []
amigosDe persona ((x,y):xs) | persona == x = y : amigosDe persona xs
    | persona == y = x: amigosDe persona xs
    | otherwise = amigosDe persona xs



{-
problema personaConMasAmigos (relaciones: seq⟨String × String⟩) : String {
requiere: {relaciones no vacıa}
requiere: {relacionesValidas(relaciones)}
asegura: {resu es el Strings que aparece m´as veces en las tuplas de relaciones (o alguno de ellos si hay empate)}
-}

{-
personaConMasAmigos :: [(String,String)] -> String
personaConMasAmigos [] = []
personaConMasAmigos ((x,y):relaciones)
    |amigos1 = length(amigosDe x relaciones)
    |amigos2 = length(amigosDe y relaciones)
    |if amigos1>amigos2 then amigos1 else amigos2 
-}

cantVeces :: (Eq t) => [t] -> [t,Int)]
cantVeces [] = []
cantVeces (x:xs) = (x, cantdeAp x (x:xs)): cantVeces (quitar x xs)

maximo :: [t,Int] -> t
-- requiere : xs no vacio
maximo [t1,n1] = t1
maximo ((t1,n1):(t2,n2):xs
    | n1 >= n2 = maximo ((t1,n1):xs)
    | otherwise = maximo ((t2,n2):xs)


elemQMasAparece :: (Eq t) => [t] -> t
elemQMasAparece [x] = x
elemQMasAparece xs = maximo (cantVeces xs)
