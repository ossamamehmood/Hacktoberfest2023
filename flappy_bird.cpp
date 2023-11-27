#include <iostream>
#include <conio.h>
#include <windows.h>

using namespace std;

bool gameOver;
const int width = 20;
const int height = 10;
int x, y; // Bird's coordinates
int pipeX;
int pipeGap;
int score;

void Setup() {
    gameOver = false;
    x = width / 2;
    y = height / 2;
    pipeX = width;
    pipeGap = 4;
    score = 0;
}

void Draw() {
    system("cls"); // Clear the console
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            if (i == 0 || i == height - 1 || j == 0 || j == width - 1) {
                cout << "#";
            } else if (j == x && i == y) {
                cout << "O";
            } else if (j == pipeX && (i < pipeGap || i >= pipeGap + 3)) {
                cout << "#";
            } else {
                cout << " ";
            }
        }
        cout << endl;
    }
    cout << "Score: " << score << endl;
}

void Input() {
    if (_kbhit()) {
        char key = _getch();
        switch (key) {
        case 'w':
            y--;
            break;
        case 's':
            y++;
            break;
        case 'q':
            gameOver = true;
            break;
        }
    }
}

void Logic() {
    pipeX--;
    if (pipeX == 0) {
        pipeX = width;
        pipeGap = rand() % (height - 4) + 1;
        score++;
    }
    if (x == pipeX && (y < pipeGap || y >= pipeGap + 3))
        gameOver = true;
    if (y >= height - 1 || y <= 0)
        gameOver = true;
}

int main() {
    Setup();
    while (!gameOver) {
        Draw();
        Input();
        Logic();
        Sleep(100); // Sleep for 100 milliseconds
    }
    return 0;
}
