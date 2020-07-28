import           Text.Printf

wordsWhen :: Char -> String -> [String]
wordsWhen p s = case dropWhile pp s of
      "" -> []
      s' -> w : wordsWhen p s'' where (w, s'') = break pp s'
      where pp = (== p)

main :: IO ()
main = do
      n <- getLine
      let list1 = map (\x -> read x :: Int) (wordsWhen ' ' n)
      let ini   = head list1
      let fim   = list1 !! 1
      let tempo = fim - ini
      printf
            "O JOGO DUROU %i HORA(S)\n"
            (if ini == fim then 24 else if tempo < 0 then tempo + 24 else tempo)
      return ()
