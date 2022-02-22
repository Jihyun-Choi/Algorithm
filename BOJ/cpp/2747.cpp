#include <iostream>//이건 왜 돼? 위에꺼랑 대체 차이가 뭔데?
#include <string>
using namespace std;

int main() {
    int arr[46];
    int num;

    arr[0] = 0;
    arr[1] = 1;

    cin >> num;

    for (int i = 2; i <= num; i++) {
        arr[i] = arr[i - 1] + arr[i - 2];
    }
    cout << arr[num];
}