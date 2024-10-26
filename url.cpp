#include <httplib.h>
#include <iostream>
#include <chrono>
#include <ctime>
#include <iomanip>
#include <vector> 
#include <fstream>
#include <algorithm>
#include <string>

using namespace std;

string get_timestamp(){
    auto now = chrono::system_clock::now();
    auto now_c = chrono::system_clock::to_time_t(now);
    stringstream ss;
    ss << put_time(localtime(&now_c),"%Y-%m-%d %H:%M:%S" );
    return ss.str();
};


string buscar(string nombres, string apellidos, vector<string>& data){
    string retorno = "";
    int counter = 0;
    transform(nombres.begin(), nombres.end(), nombres.begin(), ::toupper);
    transform(apellidos.begin(), apellidos.end(), apellidos.begin(), ::toupper);

    cout << "busqueda:" << nombres << " - " << apellidos << endl ;
    for(string persona : data){
        if(persona.find(nombres) != string::npos && persona.find(apellidos)!= string::npos){
            retorno += persona;
            retorno += "<br>";
            counter++;
        }

    };
    retorno += "la busqueda retorno " + to_string(counter) +  " resultados en ";
    return retorno;
}

int main(){
    vector<string> data;

    for(int i = 18; i < 28; i++){
        string nombre = "website/";
        nombre += to_string(i);
        nombre += "millones.txt";
        ifstream archivo(nombre);
        string linea;

        while(getline(archivo, linea)){
            data.push_back(linea);
        }
    }
    
    httplib::Server svr;
    
    svr.set_logger([](const auto& req, const auto& res){
            cout << get_timestamp() << ": ";
            cout << req.remote_addr << " ";
            cout << req.path << " " ;
            cout << res.status  << endl;
    });
    svr.set_mount_point("/", "./website/");
    
    svr.Post("/resultado", [&data](const httplib::Request& req, httplib::Response& res) {
        auto inicio = chrono::high_resolution_clock::now();
        string nombres = req.has_param("nombres") ? req.get_param_value("nombres") :"No especificado";

        string apellidos = req.has_param("apellidos") ? req.get_param_value("apellidos") :"No especificado";
    
        string html = buscar(nombres, apellidos, data);
        auto termino = chrono::high_resolution_clock::now();
        auto duracion = chrono::duration_cast<chrono::milliseconds>(termino - inicio);
        float tiempo = duracion.count();
        tiempo /= 1000;
        html += to_string(tiempo) + " segundos";
        res.set_header("Content-Type", "text/html; charset=utf-8");
        res.set_content(html, "text/html");
        
    }); 

    svr.listen("0.0.0.0", 8050);
    return 0; 
}

