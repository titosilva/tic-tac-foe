#include <stdio.h>

void draw_game(char game[3][3]) {
    printf("   |   |   \n");
    printf(" %c | %c | %c \n", game[0][0], game[0][1], game[0][2]);
    printf("   |   |   \n");
    printf("___________\n");
    printf("   |   |   \n");
    printf(" %c | %c | %c \n", game[1][0], game[1][1], game[1][2]);
    printf("   |   |   \n");
    printf("___________\n");
    printf("   |   |   \n");
    printf(" %c | %c | %c \n", game[2][0], game[2][1], game[2][2]);
    printf("   |   |   \n");
}

char get_winner(char game[3][3]) {
    for (int i = 0; i < 3; i++) {
        if (game[i][0] == ' ') continue;

        if (game[i][0] == game[i][1] && game[i][1] == game[i][2]) {
            return game[i][0];
        }
    }

    for (int i = 0; i < 3; i++) {
        if (game[0][i] == ' ') continue;

        if (game[0][i] == game[1][i] && game[1][i] == game[2][i]) {
            return game[i][0];
        }
    }

    if (game[0][0] == game[1][1] && game[1][1] == game[2][2]) {
        return game[1][1];
    }

    if (game[0][2] == game[1][1] && game[1][1] == game[2][0]) {
        return game[1][1];
    }

    return ' ';
}

int is_full(char game[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (game[i][j] == ' ') return 0;
        }
    }

    return 1;
}

int main() {
    char game[3][3] = {
        { ' ', ' ', ' ', },
        { ' ', ' ', ' ', },
        { ' ', ' ', ' ', },
    };
    draw_game(game);

    char player = 'O';
    while (1) {
        int x, y;
        printf("\nPlayer %c, what is your move? ", player);
    
        if (scanf("%d %d", &x, &y) != 2) {
            printf("Invalid move!\n");
            continue;
        }

        if (x < 0 || x > 2 || y < 0 || y > 2) {
            printf("Invalid move!\n");
            continue;
        }

        if (game[x][y] != ' ') {
            printf("Invalid move!\n");
            continue;
        }

        game[x][y] = player;
        draw_game(game);

        char winner = get_winner(game);

        if (winner != ' ') {
            printf("Player %c wins!\n", winner);
            break;
        }

        if (is_full(game)) {
            printf("Draw!\n");
            break;
        }

        player = player == 'O'? 'X' : 'O';
    }

    return 0;
}