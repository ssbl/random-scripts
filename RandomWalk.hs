import System.Random
import Control.Monad
import Graphics.UI.GLUT
    
f :: Int -> IO [Int]
f n = do
  g <- newStdGen
  return (take n $ (randomRs (0, 1) g))

g :: IO [GLfloat]
g  = do
  xs <- f 20
  return (map (\x -> if x == 1 then (0.05) else (-0.05)) xs)

myPoints :: IO [(GLfloat, GLfloat, GLfloat)]
myPoints = do
  ys <- g
  let z = map (realToFrac :: Integer -> GLfloat) $ repeat 0
      x = iterate (+ 0.05) 0
      y = scanl (+) 0.0 ys
  return $ zip3 x y z

main :: IO ()
main  = do
  (_progname, _args) <- getArgsAndInitialize
  _window <- createWindow "Random walk"
  windowSize $= Size 640 480
  displayCallback $= display
  mainLoop

display :: DisplayCallback
display  = do
  clear [ ColorBuffer ]
  renderPrimitive LineStrip $ do
            points <- myPoints
            mapM_ (\(x, y, z) -> vertex $ Vertex3 x y z) points
  flush
