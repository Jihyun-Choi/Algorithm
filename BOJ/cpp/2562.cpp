#include <iostream>
#include <string>
using namespace std;

int main() {
    /*
    int arr[9];
    int max=0, n;

    for (int i = 0; i < 9; i++) {
        cin >> arr[i];
        if (arr[i] > max) {
            max = arr[i];
            n = i;
        }
        cout << max << endl << n + 1;
    }
    */
    int arr[100];
    int pNum = 0, Max = 0;


    for (int i = 1; i <= 9; i++)
    {
        cin >> arr[i];

        if (Max < arr[i])
        {
            Max = arr[i];
            pNum = i;
        }
    }

    cout << Max << " " << pNum << endl;

}