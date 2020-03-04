import           Text.Printf

main = do
    a <- readLn :: IO Int
    b <- readLn :: IO Int
    printf "X = %d\n" (a + b)
