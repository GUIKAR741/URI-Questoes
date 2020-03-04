import           Text.Printf

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
      "" -> []
      s' -> w : wordsWhen p s'' where (w, s'') = break p s'

main :: IO ()
main = do
      l1 <- getLine
      l2 <- getLine
      let list1    = wordsWhen (== ' ') l1
      let list2    = wordsWhen (== ' ') l2
      let codPeca1 = read (head list1) :: Int
      let numPeca1 = read (list1 !! 1) :: Float
      let valPeca1 = read (list1 !! 2) :: Float
      let codPeca2 = read (head list2) :: Int
      let numPeca2 = read (list2 !! 1) :: Float
      let valPeca2 = read (list2 !! 2) :: Float
      printf "VALOR A PAGAR: R$ %.2f\n"
             ((valPeca1 * numPeca1) + (valPeca2 * numPeca2))
      return ()
