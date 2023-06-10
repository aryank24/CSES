k = int(input())
for i in range(1, k+1):
    total_blocks_in_grid = i*i
    total_combs_for_two_knights = total_blocks_in_grid * (total_blocks_in_grid - 1) // 2  # total_blocks choose 2 
    num_of_2_by_3_blocks = (i-1)*(i-2)
    num_of_3_by_2_blocks = (i-2)*(i-1)
    # Each 2x3 or 3x2 block has 2 ways of Knights attacking each other
    answer = total_combs_for_two_knights - 2*(num_of_2_by_3_blocks + num_of_3_by_2_blocks)
    print(answer)