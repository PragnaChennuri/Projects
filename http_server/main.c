#include <sys/socket.h>
#include <netinet/in.h>

// the struct that stores the IP address and the port #
struct sockaddr_in address = {
        AF_INET,
        0x901f, //opposite order for port # and socket API
        0
};

void main(){
    // AF_INET is the regular IPv4 Internet Protocol
    // SOCK_STREAM a simple TCP socket
    int n_s = socket(AF_INET, SOCK_STREAM, 0); //returns a file descriptor of the socket

    // binding the socket to a specific IP address and a specific port number
    // n_s is the socket descriptor we made from above
    // address: pointer that points to the struct which contains the IP address and port #
    // sizeof(address): size of the structure
    int b = bind(n_s, &address, sizeof(address));
}