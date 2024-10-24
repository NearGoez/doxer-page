#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main(){
    vector<string> data;
    ifstream archivo("website/21millones.txt");
    string linea;

    while(getline(archivo, linea)){
        data.push_back(linea);
        cout << linea << endl;
    }
    
    for(string persona : data){
        if (persona.find("DENIS") != string::npos){
            cout << persona << endl;
        }
    }
} 
