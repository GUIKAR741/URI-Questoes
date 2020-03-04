import           Text.Printf

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
      "" -> []
      s' -> w : wordsWhen p s'' where (w, s'') = break p s'

main :: IO ()
main = do
      n <- readLn :: IO Int
      let hora = floor (fromIntegral n / 3600) :: Int
      let min  = floor (fromIntegral(mod n 3600) / 60) :: Int
      let seg  = mod (mod n 3600) 60
      printf "%d:%d:%i\n" hora min seg
      return ()
