import           Text.Printf

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
      "" -> []
      s' -> w : wordsWhen p s'' where (w, s'') = break p s'

main :: IO ()
main = do
      n <- getLine
      let list1 = wordsWhen (== ' ') n
      let a     = read (head list1) :: Double
      let b     = read (list1 !! 1) :: Double
      let c     = read (list1 !! 2) :: Double
      let ab    = a + b
      let ac    = a + c
      let bc    = b + c
      let aab   = abs (a - b)
      let aac   = abs (a - c)
      let abc   = abs (b - c)
      if (abc < a && a < bc) && (aac < b && b < ac) && (aab < c && a < ab)
            then printf "Perimetro = %.1f\n" (a + b + c)
            else printf "Area = %.1f\n" (((a + b) / 2) * c)
      return ()
