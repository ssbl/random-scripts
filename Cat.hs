-- Fundamentals
-- Concatenate files

import           System.Environment

main = do
  files <- getArgs
  text <- mapM readFile files
  putStrLn $ concat text
