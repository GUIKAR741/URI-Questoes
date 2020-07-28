import           Text.Printf

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
      "" -> []
      s' -> w : wordsWhen p s'' where (w, s'') = break p s'

executa::Int->IO ()
executa 0 = return ()
executa num = do
      n <- getLine
      let list1 = wordsWhen (== ' ') n
      let a     = read (head list1) :: Double
      let b     = read (list1 !! 1) :: Double
      let c     = read (list1 !! 2) :: Double
      printf "%.1f\n" ((a * 2 + b * 3 + c * 5)/ 10)
      executa (num-1)

main :: IO ()
main = do
      n <- readLn :: IO Int
      executa n      
      return ()
