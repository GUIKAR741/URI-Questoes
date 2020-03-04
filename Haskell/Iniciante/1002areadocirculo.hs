import           Text.Printf
area :: Double -> Double
area a = a * a * 3.14159

main = do
    a <- readLn :: IO Double
    let b = area a
    printf "A=%.4f\n" b
