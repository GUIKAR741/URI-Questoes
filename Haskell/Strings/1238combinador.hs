import           Text.Printf

wordsWhen :: Char -> String -> [String]
wordsWhen p s = case dropWhile pp s of
    "" -> []
    s' -> w : wordsWhen p s'' where (w, s'') = break pp s'
    where pp = (== p)

concatena::String->String->String
concatena [] [] = []
concatena x [] = x
concatena [] y = y
concatena (x:xs) (y:ys) = x : y : concatena xs ys

executa :: Int -> IO ()
executa 0 = return ()
executa n = do
    linha <- getLine 
    let list1 = wordsWhen ' ' linha
    let linha1 = head list1
    let linha2 = list1 !! 1
    printf "%s\n" (concatena linha1 linha2) 
    executa (n-1)

main :: IO ()
main = do
    num <- readLn :: IO Int
    executa num
    return ()
