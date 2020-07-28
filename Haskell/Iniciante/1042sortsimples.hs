import           Text.Printf

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
      "" -> []
      s' -> w : wordsWhen p s'' where (w, s'') = break p s'

qsort :: (Ord a) => [a] -> [a]
qsort [] = []
qsort (x : xs) =
      qsort [ a | a <- xs, a < x ] ++ [x] ++ qsort [ b | b <- xs, b >= x ]

imprimeLista :: [Int] -> IO ()
imprimeLista = foldr ((>>) . printf "%d\n") (return ())

main :: IO ()
main = do
      n <- getLine
      let list1 = map (\x -> read x :: Int) (wordsWhen (== ' ') n)
      let a     = head list1
      let b     = list1 !! 1
      let c     = list1 !! 2
      imprimeLista (qsort list1)
      printf "\n"
      imprimeLista list1
      return ()
