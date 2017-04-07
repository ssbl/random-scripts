import           Data.Char          (isSpace)
import           System.Environment (getArgs)

import qualified Data.Text          as T

isNotComment delim line
    | T.null line = False
    | T.isPrefixOf delim line = False
    | otherwise = True

count delim =
    length . filter (isNotComment delim) . map (T.dropWhile isSpace) . T.lines

main = do
  args <- getArgs
  case args of
    [] -> putStrLn "Usage: countlines <comment-delim>"
    (delim:_) -> do f <- getContents
                    print $ count (T.pack delim) (T.pack f)
