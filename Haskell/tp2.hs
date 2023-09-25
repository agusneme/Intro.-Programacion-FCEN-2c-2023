type Posicion = [Int]
type Jugada = (Int, Int)

jugar          :: Posicion -> Jugada -> Posicion
jugar p (i, n) = quitar 0 (reemplazarEnésimoElemento i (p !! (i - 1) - n) p)

posiblesJugadas   :: Posicion -> [Jugada]
posiblesJugadas p = auxiliarPosiblesJugadas p (length p)

esPosicionGanadora   :: Posicion -> Bool
esPosicionGanadora p = algunaEsJugadaGanadora p (posiblesJugadas p)

jugadaGanadora   :: Posicion -> Jugada
jugadaGanadora p = cualJugadaEsGanadora p (posiblesJugadas p)

numeroDeJugadasGanadoras   :: Posicion -> Int
numeroDeJugadasGanadoras p = contarJugadasGanadoras p (posiblesJugadas p)

-------------- Funciones Auxiliares --------------

quitar :: Int -> [Int] -> [Int]
quitar _   []               = []
quitar n (x:xs) | x == n    = xs
                | otherwise = x:quitar n xs

reemplazarEnésimoElemento :: Int -> Int -> [Int] -> [Int]
reemplazarEnésimoElemento _ _   []               = []
reemplazarEnésimoElemento i n (x:xs) | i == 1    = n:xs
                                     | otherwise = x:reemplazarEnésimoElemento (i - 1) n xs

auxiliarPosiblesJugadas :: Posicion -> Int -> [Jugada]
auxiliarPosiblesJugadas [] _ = []
auxiliarPosiblesJugadas p n = (posiblesJugadasEnUnMontoncito n (last p)) ++  (auxiliarPosiblesJugadas (init p) (n - 1))

posiblesJugadasEnUnMontoncito :: Int -> Int -> [Jugada]
posiblesJugadasEnUnMontoncito i 1 = [(i, 1)]
posiblesJugadasEnUnMontoncito i n = (i, n):posiblesJugadasEnUnMontoncito i (n - 1)

algunaEsJugadaGanadora :: Posicion -> [Jugada] -> Bool
algunaEsJugadaGanadora _   []   = False
algunaEsJugadaGanadora p (j:js) = not (esPosicionGanadora (jugar p j)) || algunaEsJugadaGanadora p js

cualJugadaEsGanadora :: Posicion -> [Jugada] -> Jugada
cualJugadaEsGanadora p (j:js) | not (esPosicionGanadora (jugar p j)) = j
                              | otherwise                            = cualJugadaEsGanadora p js

contarJugadasGanadoras :: Posicion -> [Jugada] -> Int
contarJugadasGanadoras _   []                                          = 0
contarJugadasGanadoras p (j:js) | not (esPosicionGanadora (jugar p j)) = 1 + contarJugadasGanadoras p js
                                | otherwise                            = contarJugadasGanadoras p js