
relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((x, y):resto) = notElem (x, y) resto && notElem (y, x) resto && relacionesValidas resto


main :: IO ()
main = do
  let relaciones = [("a", "b"), ("c", "d"), ("b", "a")]

  putStrLn $ "¿Las relaciones son válidas? " ++ show (relacionesValidas relaciones)
