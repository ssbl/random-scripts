subsets [] = [[]]
subsets (x:xs) = let rest = subsets xs
                 in rest ++ (map (x:) rest)

main = print $ subsets [1,2,3]
