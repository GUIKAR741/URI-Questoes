import           Text.Printf

main = do
    a <- readLn :: IO Int
    b <- readLn :: IO Int
    printf "SOMA = %d\n" (a + b)
