import           Text.Printf

main = do
    a <- readLn :: IO Int
    b <- readLn :: IO Int
    printf "PROD = %d\n" (a * b)
