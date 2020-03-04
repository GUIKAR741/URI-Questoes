import           Text.Printf

main = do
    a <- getLine
    b <- readLn :: IO Float
    c <- readLn :: IO Float
    printf "TOTAL = R$ %.2f\n" (b + (c * 0.15))
