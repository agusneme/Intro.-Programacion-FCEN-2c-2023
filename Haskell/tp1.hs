-- Ejericio 1
satisfaceGoldbach :: Integer -> Bool
satisfaceGoldbach n = esPar n && n > 2 && esSumadePrimos n

-- Ejercicio 2
verificarConjeturaHasta:: Integer -> Bool
verificarConjeturaHasta 4 = True
verificarConjeturaHasta n = satisfaceGoldbach n && verificarConjeturaHasta (n - 2)

-- Ejercicio 3
descomposicionEnPrimos :: Integer -> (Integer, Integer)
descomposicionEnPrimos n = descomposicionEnPrimosDesde 1 1 n

-- Ejercicio 4
numeroDeDescomposiciones :: Integer -> Integer
numeroDeDescomposiciones n = contarDescomposicionesEnPrimos 0 0 n

-- Funciones auxiliares
esPar :: Integer -> Bool
esPar n = n `mod` 2 == 0

esPrimo :: Integer -> Bool
esPrimo n | n > 1 && menorDivisorDesde 2 n == n = True
          | otherwise = False
    where menorDivisorDesde i m | i == m         = i
                                | m `mod` i == 0 = i
                                | otherwise      = menorDivisorDesde (i + 1) m

enesimoPrimo :: Integer -> Integer
enesimoPrimo 1 = 2
enesimoPrimo n = minimoPrimoDesde (1 + enesimoPrimo (n - 1))
    where minimoPrimoDesde m | esPrimo m = m
                             | otherwise = minimoPrimoDesde (m + 1)

-- itero sobre i, k como si fueran índices de una lista de primos indexada en 1. Devuelve (0,0) si el número no puede descomponerse
descomposicionEnPrimosDesde :: Integer -> Integer -> Integer -> (Integer, Integer)
descomposicionEnPrimosDesde i k n | iésimoPrimo >= n               = (0, 0)
                                  | iésimoPrimo + késimoPrimo == n = (iésimoPrimo, késimoPrimo)
                                  | iésimoPrimo + késimoPrimo < n  = descomposicionEnPrimosDesde    i   (k + 1) n
                                  | iésimoPrimo + késimoPrimo > n  = descomposicionEnPrimosDesde (i + 1)   1    n
                                  where iésimoPrimo = enesimoPrimo i
                                        késimoPrimo = enesimoPrimo k

esSumadePrimos :: Integer -> Bool
esSumadePrimos n = descomposicionEnPrimosDesde 1 1 n /= (0,0)

-- k es la variable sobre la que itero, h es el contador de descomposiciones posibles, n es el número a descomponer
contarDescomposicionesEnPrimos :: Integer -> Integer -> Integer -> Integer
contarDescomposicionesEnPrimos k h n | k < n && esPrimo k && esPrimo (n - k)               = contarDescomposicionesEnPrimos (k + 1) (h + 1) n
                                     | k < n && (not (esPrimo k) || not (esPrimo (n - k))) = contarDescomposicionesEnPrimos (k + 1)    h    n
                                     | k >= n                                              = h