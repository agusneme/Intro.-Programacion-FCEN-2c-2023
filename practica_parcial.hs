
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

