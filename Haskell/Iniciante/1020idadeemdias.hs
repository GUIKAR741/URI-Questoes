import           Text.Printf

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
      "" -> []
      s' -> w : wordsWhen p s'' where (w, s'') = break p s'

main :: IO ()
main = do
      n <- readLn :: IO Int
      let ano = floor (fromIntegral n / 365)
      let mes = floor (fromIntegral (n - (ano * 365)) / 30)
      let dia = n - (ano * 365 + 30 * mes)
      printf "%i ano(s)\n%i mes(es)\n%i dia(s)\n" ano mes dia
      return ()
