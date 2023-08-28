doubleMe x = x+ x

f :: Int -> Int
f n
    | n == 1 = 8
    | n == 4 = 131
    | n == 16 = 16

g :: Int -> Int
g n
    | n == 8 = 16 
    | n == 16 = 4
    | n == 131 = 1

h x = f(g x)
k x = g(f x)

maximo :: Int -> Int -> Int -> Int
maximo x y z
    | x >= y && x >= z = x
    | y >= x && y >= z = y
    | z >= x && z >= y = z


sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z
    | x /= y && x /= z &&  y /= z = x + y + z
    | x == y && x /= z &&  y /= z = z
    | x /= y && x == z &&  y /= z = y
    | x /= y && x /= z &&  y == z = x

digitoUnidades :: Int -> Int
digitoUnidades x = mod x 10

valorAbsoluto :: Int -> Int 
valorAbsoluto x = abs(x)

digitoDecenas :: Int -> Int
digitoDecenas x = digitoUnidades(div x 10)