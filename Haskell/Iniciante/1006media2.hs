import           Text.Printf

main = do
    a <- readLn :: IO Float
    b <- readLn :: IO Float
    c <- readLn :: IO Float
    printf "MEDIA = %.1f\n" (((a * 2) + (b * 3) + (c * 5)) / 10)
