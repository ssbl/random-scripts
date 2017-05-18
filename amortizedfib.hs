fib = f
    where f i = xs !! i
          xs = map fib' [0..]
          fib' 1 = 1
          fib' 2 = 1
          fib' n = fib (n - 2) + fib (n - 1)

fib2 :: Int -> Integer
fib2 = let fibs = scanl (+) 0 (1:fibs) in (fibs !!)
