import           Text.Printf

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
      "" -> []
      s' -> w : wordsWhen p s'' where (w, s'') = break p s'

main :: IO ()
main = do
      n <- getLine
      let list1 = wordsWhen (== ' ') n
      let a     = read (head list1) :: Int
      let b     = read (list1 !! 1) :: Int
      let c     = read (list1 !! 2) :: Int
      let d     = read (list1 !! 3) :: Int
      if b > c && d > a && c+d > a+b && c > 0 && d > 0 && mod a 2 == 0
            then printf "Valores aceitos\n"
            else printf "Valores nao aceitos\n"
      return ()
