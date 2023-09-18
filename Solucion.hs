module Solucion  where

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
sacarDuplicados (x:xs) = x : sacarDuplicados (filter (/= x) xs)


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


-- amigosDe persona relaciones = (filter(/= persona) (sacarDuplicados(crearListaRelaciones relaciones)))

