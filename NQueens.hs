{-# LANGUAGE BangPatterns #-}

-- Faster solutions.
import           Data.Bits
import           System.Environment (getArgs)

nqueens :: Int -> Int
nqueens n = try 0 0 0 0
    where try :: Int -> Int -> Int -> Int -> Int
          try ld !cols rd !c
              | cols == all = c+1
              | otherwise   = let poss = (complement (ld .|. cols .|. rd)) .&. all
                              in go poss c
              where all = 2^n - 1
                    go :: Int -> Int -> Int
                    go 0 x = x
                    go p x = let b = p .&. (-p)
                               in try ((ld  .|. b) `shiftL` 1)
                                      (cols .|. b)
                                      ((rd  .|. b) `shiftR` 1) x
                                  + go (p-b) x

main :: IO ()
main = do
  [n] <- getArgs
  print . nqueens $ read n
