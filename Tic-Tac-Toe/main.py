import random

rows = [[" ", "|", " ", "|", " "],
        ["-", "-", "-", "-", "-"],
        [" ", "|", " ", "|", " "],
        ["-", "-", "-", "-", "-"],
        [" ", "|", " ", "|", " "],]

def print_pattren():
    for row in rows:
        print()
        for column in row:
            print(column, end="")

def Rearrange_index(index):
    match index:
        case 1:
            index = 0
        case 2:
            index = 2
        case 3:
            index = 4
    
    return index

def chack_game_over():

    def wining_conditions(player):
        print_win = f"\n{player} Win's This game!!!"
        for i in range(0, 5, 2):
            if rows[i][0] == player and rows[i][2] == player and rows[i][4] == player:
                print(print_win)
                return False
            
        for i in range(0, 5, 2):
            if rows[0][i] == player and rows[2][i] == player and rows[4][i] == player:
                print(print_win)
                return False
        
        if rows[0][0] == player and rows[2][2] == player and rows[4][4] == player:
            print(print_win)
            return False
        
        elif rows[0][4] == player and rows[2][2] == player and rows[4][0] == player:
            print(print_win)
            return False
        
        elif rows[0][0] != " " and rows[0][2] != " " and rows[0][4] != " " and rows[2][0] != " " and rows[2][2] != " " and rows[2][4] != " " and rows[3][0] != " " and rows[3][2] != " " and rows[3][4] != " ":
            print("\nThis game Tie!!!")
            return False
        
        return True
    
    return wining_conditions("X") and wining_conditions("O")


def main():

    while chack_game_over():
        x_row = random.choice([1, 2, 3])
        x_column = random.choice([1, 2, 3])

        x_row = Rearrange_index(x_row)
        x_column = Rearrange_index(x_column)

        if rows[x_row][x_column] != " ":
            continue
        else:
            rows[x_row][x_column] = "X"
        
        print_pattren()
        
        try:
            o_row = int(input("\nWhich Row you chose: "))
            o_column = int(input("Which column you chose: "))
        except Exception as e:
            print("\nYou loose this game because you enter wrong key")
            break

        if o_row > 3 or o_column > 3:
            print("\nYou loose this game because you enter wrong key")
            break

        o_row = Rearrange_index(o_row)
        o_column = Rearrange_index(o_column)

        if rows[o_row][o_column] != " ":
            print("please chose empty box")
            continue
        else:
            rows[o_row][o_column] = "O"
    
    print("-------------------------------------")
    print_pattren()

if __name__ == "__main__":
    main()
