#include <iostream>
#include <chrono>

int main() {
    // Get the current time point
    auto currentTime = std::chrono::system_clock::now();

    // Convert the current time point to the duration since epoch
    auto durationSinceEpoch = currentTime.time_since_epoch();

    // Convert the duration to seconds
    auto seconds = std::chrono::duration_cast<std::chrono::seconds>(durationSinceEpoch);

    // Print the epoch time
    std::cout << "Epoch time: " << seconds.count() << " seconds since January 1, 1970." << std::endl;

    return 0;
}