# library
import chess as catur
import chess.engine as komputer

def main():
    print("Selamat datang di permainan catur")
    papan_catur = catur.Board()

    while not papan_catur.is_game_over():
        print(papan_catur)
        print("\nGiliran anda")
        user_move = input("Masukkan langkah anda (contoh: e2e4) : ").lower()

        # ! validasi langkah
        if user_move == "NYERAH".lower():
            break

        try:
            move = catur.Move.from_uci(user_move)
            if move in papan_catur.legal_moves:
                papan_catur.push(move)
            else:
                print("Langkah tidak valid")
                continue
        except ValueError:
            print("Langkah tidak valid")
            continue

        # ! breakpoint
        if papan_catur.is_game_over():
            break


        # ! komputer bergerak
        print("Giliran komputer")
        engine = komputer.SimpleEngine.popen_uci("D:\RANDOMIES\stockfish\stockfish\stockfish-windows-x86-64-avx2.exe") # ! sesuaikan dengan bot model yang anda gunakan
        result = engine.play(papan_catur, komputer.Limit(time=1))
        papan_catur.push(result.move)
        engine.quit()

        # ! breakpoint
        if papan_catur.is_game_over():
            break
    
    # ! hasil akhir
    print("Permainan selesai")
    print(papan_catur)
    if papan_catur.is_checkmate():
        if papan_catur.turn:
            print("Komputer menang")
        else:
            print("Anda menang")
    elif papan_catur.is_stalemate():
        print("Permainan remis")
    elif papan_catur.is_insufficient_material():
        print("Permainan seri")

# ! run program
if __name__ == "__main__":
    main()
