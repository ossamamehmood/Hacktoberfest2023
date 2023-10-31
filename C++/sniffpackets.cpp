#include <iostream>
#include <pcap.h>

void packetHandler(unsigned char *userData, const struct pcap_pkthdr *pkthdr, const unsigned char *packet) {
    // Process packets here
}

int main() {
    char errbuf[PCAP_ERRBUF_SIZE];
    pcap_t *handle;
    const char *dev = "eth0"; // Change this to your network interface (e.g., eth0, wlan0)

    handle = pcap_open_live(dev, BUFSIZ, 1, 1000, errbuf);
    if (handle == nullptr) {
        std::cerr << "Error opening device: " << errbuf << std::endl;
        return 1;
    }

    pcap_loop(handle, 0, packetHandler, nullptr);

    pcap_close(handle);
    return 0;
}
