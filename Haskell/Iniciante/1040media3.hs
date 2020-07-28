import           Text.Printf

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
      "" -> []
      s' -> w : wordsWhen p s'' where (w, s'') = break p s'

med :: Double -> Double -> Double -> Double -> Double
med x1 x2 x3 x4 = (x1 * 2 + x2 * 3 + x3 * 4 + x4) / 10

main :: IO ()
main = do
      n <- getLine
      let list1 = wordsWhen (== ' ') n
      let n1    = read (head list1) :: Double
      let n2    = read (list1 !! 1) :: Double
      let n3    = read (list1 !! 2) :: Double
      let n4    = read (list1 !! 3) :: Double
      let media = med n1 n2 n3 n4
      if media >= 7
            then printf "Media: %.1f\nAluno aprovado.\n" media
            else if media >= 5 && media < 7
                  then do
                        printf "Media: %.1f\nAluno em exame.\n" media
                        exame <- readLn :: IO Double
                        printf "Nota do exame: %.1f\n" exame
                        let nMed = (media + exame) / 2
                        if nMed >= 5
                              then printf "Aluno aprovado.\n"
                              else printf "Aluno reprovado.\n"
                        printf "Media final: %.1f\n" nMed
                  else printf "Media: %.1f\nAluno reprovado.\n" media
      return ()
