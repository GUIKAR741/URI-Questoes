import           Text.Printf

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
      "" -> []
      s' -> w : wordsWhen p s'' where (w, s'') = break p s'

main :: IO ()
main = do
      c <- readLn :: IO Double
      let c100 = floor (c / 100) :: Int
      let c50  = floor ((c - fromIntegral (100 * c100)) / 50) :: Int
      let c20  = floor ((c - fromIntegral (100 * c100 + 50 * c50)) / 20) :: Int
      let c10  = floor ((c - fromIntegral (100 * c100 + 50 * c50 + 20 * c20)) / 10) :: Int
      let c5   = floor ((c - fromIntegral (100 * c100 + 50 * c50 + 20 * c20 + 10 * c10)) / 5) :: Int
      let c2   = floor ((c - fromIntegral (100 * c100 + 50 * c50 + 20 * c20 + 10 * c10 + 5 * c5)) / 2) :: Int
      let c1   = floor (c - fromIntegral (100 * c100 + 50 * c50 + 20 * c20 + 10 * c10 + 5 * c5 + 2 * c2)) :: Int
      printf "%.0f\n"                      c
      printf "%i nota(s) de R$ 100,00\n" c100
      printf "%i nota(s) de R$ 50,00\n"  c50
      printf "%i nota(s) de R$ 20,00\n"  c20
      printf "%i nota(s) de R$ 10,00\n"  c10
      printf "%i nota(s) de R$ 5,00\n"   c5
      printf "%i nota(s) de R$ 2,00\n"   c2
      printf "%i nota(s) de R$ 1,00\n"     c1
      return ()
