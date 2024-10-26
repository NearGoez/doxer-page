#include <httplib.h>
#include <iostream>
#include <ctime>
#include <iomanip>
using namespace std;

string get_timestamp(){
    auto now = chrono::system_clock::now();
    auto now_c = chrono::system_clock::to_time_t(now);
    stringstream ss;
    ss << put_time(localtime(&now_c),"%Y-%m-%d %H:%M:%S" );
    return ss.str();
};

int main(){
    httplib::Server svr;
    
    svr.set_logger([](const auto& req, const auto& res){
            cout << get_timestamp() << ": ";
            cout << req.remote_addr << " ";
            cout << res.status  << endl;
    });
    svr.set_mount_point("/", "./website/");


    svr.listen("0.0.0.0", 8000);
    return 0; 
}

