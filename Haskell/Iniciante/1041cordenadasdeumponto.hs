import           Text.Printf

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
      "" -> []
      s' -> w : wordsWhen p s'' where (w, s'') = break p s'

main :: IO ()
main = do
      n <- getLine
      let list1 = wordsWhen (== ' ') n
      let x     = read (head list1) :: Double
      let y     = read (list1 !! 1) :: Double
      if x == 0 && y == 0
            then printf "Origem\n"
            else if x == 0 && y /= 0
                  then printf "Eixo Y\n"
                  else if x /= 0 && y == 0
                        then printf "Eixo X\n"
                        else if x > 0 && y > 0
                              then printf "Q1\n"
                              else if x < 0 && y > 0
                                    then printf "Q2\n"
                                    else if x < 0 && y < 0
                                          then printf "Q3\n"
                                          else printf "Q4\n"
      return ()
