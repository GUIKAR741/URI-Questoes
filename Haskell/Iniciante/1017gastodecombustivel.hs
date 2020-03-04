import           Text.Printf

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
      "" -> []
      s' -> w : wordsWhen p s'' where (w, s'') = break p s'

main :: IO ()
main = do
      p1 <- readLn :: IO Double
      p2 <- readLn :: IO Double
      printf "%.3f\n" ((p1 * p2) / 12)
      return ()
