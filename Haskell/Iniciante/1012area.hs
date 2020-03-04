import           Text.Printf

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
      "" -> []
      s' -> w : wordsWhen p s'' where (w, s'') = break p s'

main :: IO ()
main = do
      linha <- getLine
      let list = wordsWhen (== ' ') linha
      let a    = read (head list) :: Double
      let b    = read (list !! 1) :: Double
      let c    = read (list !! 2) :: Double
      printf "TRIANGULO: %.3f\n" ((a * c) / 2)
      printf "CIRCULO: %.3f\n"   ((c ** 2) * 3.14159)
      printf "TRAPEZIO: %.3f\n"  (((a + b) / 2) * c)
      printf "QUADRADO: %.3f\n"  (b ** 2)
      printf "RETANGULO: %.3f\n" (a * b)
      return ()
