#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool checkRow(int board[9][9], int row, int n)
{
	for (int j = 0; j < 9; j++) {
		if (board[row][j] == n)
			return false;
	}
	return true;
}

bool checkCol(int board[9][9], int col, int n)
{
	for (int i = 0; i < 9; i++) {
		if (board[i][col] == n)
			return false;
	}
	return true;
}

bool checkBox(int board[9][9], int startRow, int startCol, int n)
{
	for (int i = startRow; i < startRow + 3; i++) {
		for (int j = startCol; j < startCol + 3; j++) {
			if (board[i][j] == n)
				return false;
		}
	}
	return true;
}

bool isPossible(int board[9][9], int row, int col, int n)
{
	return checkRow(board, row, n) && checkCol(board, col, n) && checkBox(board, row - row % 3, col - col % 3, n);
}

bool isSolved(int board[9][9], int *row, int *col)
{
	for (*row = 0; *row < 9; *row += 1) {
		for (*col = 0; *col < 9; *col += 1) {
			if (board[*row][*col] == 0)
				return false;
		}
	}
	return true;
}

bool solve(int board[9][9])
{
    int row, col;
 
    if (isSolved(board, &row, &col))
       return true;
 
    for (int n = 1; n <= 9; n++) {

        if (isPossible(board, row, col, n)) {
            
            board[row][col] = n;
 
            if (solve(board))
                return true;
 
            board[row][col] = 0;
        }
    }
    return false;
}

void printBoard(int board[9][9])
{
    for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++)
			printf("%2d", board[i][j]);
		printf("\n");
    }
}

void getBoards(int boards[50][9][9])
{
	FILE *f;
	char line[11];
	int i = 0, j = 0;

	f = fopen ("sudoku.txt", "rt");

	while (fgets(line, 11, f) != NULL) {
		
		if (j == 9) {
			j = 0;
			i++;
		}

		for (int k = 0; k < 9; k++)
			boards[i][j][k] = line[k] - '0';

		j++;
	}
	fclose(f);
}

int main(void)
{	
	int sum = 0;
	int boards[50][9][9];

	getBoards(boards);

	for (int i = 0; i < 50; i++) {
		if (solve(boards[i]) == true) {
			printf("Grid %d\n", i + 1);
		    printBoard(boards[i]);
			sum += 100 * boards[i][0][0] + 10 * boards[i][0][1] + boards[i][0][2];
			printf("Sum %d\n", sum);
		}
		else
		    printf("This Sudoku doesn't have a single answer.");
	    printf("\n");
	}
 
    return 0;
}
