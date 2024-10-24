#include <httplib.h>
#include <iostream>
using namespace std;

int main(){
    httplib::Server svr;

    svr.set_mount_point("/", "./website/");


    svr.listen("0.0.0.0", 8000);
    return 0; 
}

