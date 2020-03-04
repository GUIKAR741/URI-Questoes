import           Text.Printf

main = do
    a <- readLn :: IO Int
    b <- readLn :: IO Float
    c <- readLn :: IO Float
    printf "NUMBER = %d\n"      a
    printf "SALARY = U$ %.2f\n" (b * c)
