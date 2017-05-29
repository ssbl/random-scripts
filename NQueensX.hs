{-# LANGUAGE BangPatterns #-}
-- Can we place n queens on a board sized m x m ?
-- From HTDP

import           Control.Applicative
import           Data.Function       (on)
import           Data.Maybe          (fromJust, isNothing, listToMaybe)
import           System.Environment  (getArgs)

type Board = [[Bool]]

data Posn  = Pos !Int !Int
           deriving Show

-- Generate an (n x n) board with the function f.
buildBoard :: Integer -> (Integer -> Integer -> Bool) -> Board
buildBoard n f = [[f i j | j <- [0..n-1]] | i <- [0..n-1]]

-- Return value at board_ij.
boardRef :: Board -> Integer -> Integer -> Bool
boardRef board i j = let fi = fromInteger
                         row = board !! fi i
                     in row !! fi j

-- Wrapper for Posn.
pos :: Integer -> Integer -> Posn
pos = Pos `on` fromInteger

-- Check whether queen at board_ij threatens queen at board_pq.
isThreatened :: Posn -> Posn -> Bool
isThreatened (Pos i j) (Pos p q) =
    i == p || j == q || abs (i - p) == abs (j - q)

-- N for the given N-queen problem.
boardN :: Board -> Integer
boardN = toInteger . length

-- Indices of an (n x n) matrix.
indices :: Board -> [(Int,Int)]
indices b = ((,) `on` fromInteger) <$> [0..n-1] <*> [0..n-1]
    where n = boardN b

-- List ALL open spots on the given board. `rowSpots` is preferred.
openSpots :: Board -> [Posn]
openSpots b = map (uncurry Pos) $ foldr
                (\x y -> if snd x then fst x : y else y) [] mapped
    where mapped = zip (indices b) (concatMap id b)

-- Update the board after placing a queen on the given spot.
addQueen :: Board -> Posn -> Board
addQueen b p = buildBoard (boardN b)
                 (\x y -> not (isThreatened (pos x y) p) && boardRef b x y)

-- Return the next row if it has any empty spots, Nothing if it has none.
nextRow :: Board -> Maybe (Int,[Bool])
nextRow = listToMaybe . filter (or . snd) . zip [0..]

-- List any open spots on the next row.
rowSpots :: Board -> [Posn]
rowSpots b = case nextRow b of
               Nothing -> []
               Just x  -> uncurry (\n xs -> map (Pos n . fst)
                                   (filter snd $ zip [0..] xs)) x

nqueens :: Int -> Int
nqueens n = go board (rowSpots board) 0 (n,n)
    where board = replicate n $ replicate n True
          go :: Board -> [Posn] -> Int -> (Int,Int) -> Int
          go _ [] !c (0,0) = c+1 -- edge case.
          go _ [] !c (_,0) = c   -- reached last column.
          go _ [] !c (0,_) = c+1 -- reached last row.
          go _ [] !c _     = c   -- no moves left.
          go !b (p:ps) !c !(m',n') = let nb = addQueen b p
                                         os = rowSpots nb
                                         c' = go nb os 0 (m'-1,n')
                                     in go b ps (c+c') (m',n'-1)

main :: IO ()
main = do
  [n] <- getArgs
  print . nqueens $ read n
