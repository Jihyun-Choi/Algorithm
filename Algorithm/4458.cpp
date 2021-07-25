#include <iostream>
#include <string> 
using namespace std;

int main(void) {
    int num;
    string str;

    cin >> num;
    cin.ignore();

    while (num--) {
        getline(cin, str);

        if ((str[0] >= 'a') && (str[0] <= 'z')) {
            str[0] = toupper(str[0]);
        }

        cout << str << endl;
        str = "";
    }
}