import time 


problem_number = 54


def order_hand(hand):
    index_list = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    for i in range(4):
        for j in range(4):
            if index_list.index(hand[j][0]) > index_list.index(hand[j + 1][0]):
                hand[j], hand[j + 1] = hand[j + 1], hand[j]
    
    return(hand)


def get_rank(hand):
    rank = [0, hand[-1][0]]
    index_list = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    
    one_pair_bool = False
    pair_value = ''
    for i in range(4):
        if hand[i][0] == hand[i + 1][0]:
            one_pair_bool = True
            pair_value = hand[i][0]
    if one_pair_bool:
        rank = [1, pair_value]
    
    nb = 0
    pair_value = ''
    for i in range(3): 
        if hand[i][0] == hand[i + 1][0] and hand[i][0] != hand[i + 2][0]:
            nb += 1
            pair_value = hand[i][0]
    if hand[4][0] == hand[3][0]:
        nb += 1
        pair_value = hand[4][0]
    if nb == 2:
        rank = [2, pair_value]
    
    three_value = ''
    three_bool = False
    for i in range(3):
        if hand[i][0] == hand[i + 1][0] and hand[i][0] == hand[i + 2][0]:
            three_bool = True
            three_value = hand[i][0]
    if three_bool:
        rank = [3, three_value]
    
    straight = 1
    for i in range(4):
         if index_list.index(hand[i][0]) + 1 == index_list.index(hand[i + 1][0]):
             straight += 1
    if straight == 5:
        rank = [4, hand[-1][0]]
    
    flush = 1
    for i in range(4):
         if hand[i][1] == hand[i + 1][0]:
             flush += 1
    if flush == 5:
        rank = [5, hand[-1][0]]
    
    if hand[0][0] == hand[1][0] and hand[0][0] == hand[2][0] and hand[4][0] == hand[3][0]:
        rank = [6, hand[3][0]]    
    if hand[3][0] == hand[4][0] and hand[3][0] == hand[2][0] and hand[1][0] == hand[0][0]:
        rank = [6, hand[4][0]]
    
    if  hand[0][0] == hand[1][0] and hand[0][0] == hand[2][0] and hand[0][0] == hand[3][0]:
        rank = [7, hand[-1][0]]    
    if  hand[4][0] == hand[1][0] and hand[4][0] == hand[4][0] and hand[4][0] == hand[3][0]:
        rank = [7, hand[-1][0]]
    
    if straight == 5 and flush == 5:
        rank =8
        
    return rank


def higer(hand_1, hand_2):
    index_list = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    if len(hand_1) == 1:
        if index_list.index(hand_1[0][0]) > index_list.index(hand_2[0][0]):
            return 1
        elif index_list.index(hand_1[0][0]) == index_list.index(hand_2[0][0]):
            return 0
        else:
            return 2
    else:
        if index_list.index(hand_1[-1][0]) > index_list.index(hand_2[-1][0]):
            return 1
        elif index_list.index(hand_1[-1][0]) == index_list.index(hand_2[-1][0]):
            return higer(hand_1[:-1], hand_2[:-1])
        else:
            return 2


#read data


number_file = open("data.txt", "r")
raw_data = number_file.read()
number_file.close()

game_list = []
string = ""
new_game = []

for char in raw_data:
    if char == "\n":
        new_game.append(string)
        string = ""
        game_list.append(new_game)
        new_game = []
    elif char == " ":
        new_game.append(string)
        string = ""
    else:
        string += char
        

#Solution


def solution(input_list):
    index_list = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    result = 0
    
    for game in input_list:
        Player_1_hand = order_hand(game[0:5])
        Player_2_hand = order_hand(game[5:])
        rank_1 = get_rank(Player_1_hand)
        rank_2 = get_rank(Player_2_hand)
        
        if rank_1[0] > rank_2[0]:
            result += 1
        elif rank_1[0] == rank_2[0]:
            if index_list.index(rank_1[1]) > index_list.index(rank_2[1]):
                result +=1
            elif index_list.index(rank_1[1]) == index_list.index(rank_2[1]):
                if higer(Player_1_hand, Player_2_hand) == 1:
                    result += 1   
        
    return result


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_problem = time.time()
problem_value = solution(game_list)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
