import Data.Char (isLetter, toUpper)
import Data.List (elemIndex)
import Data.Maybe (fromMaybe)

cleanText :: String -> String
cleanText = map toUpper . filter isLetter

encryptText :: String -> String -> Int -> String
encryptText alphabet plainText shift = map encryptChar plainText
  where
    encryptChar :: Char -> Char
    encryptChar c = alphabet !! (((charIndex alphabet c) + shift) `mod` lengthAlphabet)
    charIndex :: String -> Char -> Int
    charIndex alphabet c = fromMaybe (-1) $ elemIndex c alphabet
    lengthAlphabet = length alphabet

alphabet :: String
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

main :: IO ()
main = do
  putStrLn "Input text:"
  text <- getLine

  putStrLn "Input shift:"
  shift <- readLn

  let encryptedText = encryptText alphabet (cleanText text) shift

  putStrLn "Encrypted text:"
  putStrLn encryptedText
