import           Text.Printf

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
      "" -> []
      s' -> w : wordsWhen p s'' where (w, s'') = break p s'

main :: IO ()
main = do
      pt1 <- getLine
      pt2 <- getLine
      let list1 = wordsWhen (== ' ') pt1
      let list2 = wordsWhen (== ' ') pt2
      let x1    = read (head list1) :: Double
      let y1    = read (list1 !! 1) :: Double
      let x2    = read (head list2) :: Double
      let y2    = read (list2 !! 1) :: Double
      printf "%.4f\n" (sqrt ((x2-x1)^2 + (y2-y1)^2))
      return ()
