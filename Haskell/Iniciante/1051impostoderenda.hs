import           Text.Printf

main :: IO ()
main = do
    salario <- readLn :: IO Double
    if 0 <= salario && salario <= 2000
        then printf "Isento\n"
        else if 2000 < salario && salario <= 3000
            then printf "R$ %.2f\n" ((salario - 2000) * 0.08)
            else if 3000 < salario && salario <= 4500
                then printf "R$ %.2f\n"
                            ((1000 * 0.08) + ((salario - 3000) * 0.18))
                else printf
                    "R$ %.2f\n"
                    ((1000 * 0.08) + (1500 * 0.18) + ((salario - 4500) * 0.28))
    return ()
