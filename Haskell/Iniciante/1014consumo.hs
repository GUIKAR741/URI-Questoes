import           Text.Printf

main :: IO ()
main = do
      dist <- readLn :: IO Double
      comb <- readLn :: IO Double
      printf "%.3f km/l\n" (dist/comb)
      return ()
