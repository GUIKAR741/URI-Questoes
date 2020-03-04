import           Text.Printf

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
      "" -> []
      s' -> w : wordsWhen p s'' where (w, s'') = break p s'

maior :: (Fractional a) => a -> a -> a
maior a b = (a + b + abs (a - b)) / 2

main :: IO ()
main = do
      linha <- getLine
      let list = wordsWhen (== ' ') linha
      let a    = read (head list) :: Double
      let b    = read (list !! 1) :: Double
      let c    = read (list !! 2) :: Double
      printf "%d eh o maior\n" (round (maior (maior a b) c) :: Int)
      return ()
