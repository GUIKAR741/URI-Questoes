import           Text.Printf

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
      "" -> []
      s' -> w : wordsWhen p s'' where (w, s'') = break p s'

main :: IO ()
main = do
      pt1 <- readLn :: IO Int
      printf "%d minutos\n" (pt1 * 2)
      return ()
