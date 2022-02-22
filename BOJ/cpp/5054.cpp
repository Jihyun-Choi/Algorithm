#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
    int turn, num, input, min = 100, max = -1;

    cin >> turn;

    for (int i = 0; i < turn; i++) {
        cin >> num;

        for (int r = 0; r < num; r++) {
            cin >> input;

            if (input <= min)
                min = input;
            if (max <= input)
                max = input;
        }
        cout << (max - min) * 2 << endl;
        min = 100;
        max = -1;
    }

}