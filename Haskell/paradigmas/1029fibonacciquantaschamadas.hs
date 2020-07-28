import           Text.Printf


fib :: [(Int, Int)]
fib = [(0, 1), (2, 1), (4, 2), (8, 3)]


geraFib :: Int -> [(Int, Int)] -> [(Int, Int)]
geraFib i l = if i <= 39
    then geraFib
        (i + 1)
        (  l
        ++ [ ( fst (l !! (i - 2)) + fst (l !! (i - 3)) + 2
             , snd (l !! (i - 2)) + snd (l !! (i - 3))
             )
           ]
        )
    else l

listaFib = geraFib 5 fib

executa :: Int -> IO ()
executa 0   = return ()
executa num = do
    n <- readLn :: IO Int
    let nl = listaFib !! (n - 1)
    uncurry (printf "fib(%d) = %d calls = %d\n" n) nl
    executa (num - 1)

main :: IO ()
main = do
    n <- readLn :: IO Int
    executa n
    return ()
